from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from hueforge.export.colorplan_export import export_colorplan_txt
from hueforge.geometry.add_border import add_border
from hueforge.geometry.height_map import generate_height_map
from hueforge.geometry.layers_to_mm import layers_to_mm
from hueforge.geometry.mesh_generation import Mesh, height_map_to_mesh
from hueforge.mapping.palette_mapping import map_palette
from hueforge.physics.td_preview import simulate_stack
from hueforge.preprocessing.merge_small_regions import merge
from hueforge.preprocessing.preprocess_edge_preserving import process
from hueforge.preprocessing.scale import scale_image_to_canvas
from hueforge.preprocessing.segment_superpixels import segment
from src.app.image_io import ImageData, load_image, save_image
from hueforge.palette.palette_suggestion import suggest_palette
from src.print.filament_assignment import assign_palette_to_filaments
from src.print.filaments import load_catalog
from src.solver.region_recipe import solve_layers_by_label

# TODO migrate: src.app.image_io, src.ops.palette_suggestion, src.print.*, src.solver.*


def run_pipeline_hueforge(
    input_path: str,
    output_stl_path: str,
    *,
    debug_dir: str | None,
    preset_path: str | None,
    allowed_filaments: list[str] | None,
    overrides: dict | None,
    mode: str = "full",
) -> dict:
    preset = _load_preset(preset_path)
    if overrides:
        preset = _apply_overrides(preset, overrides)

    image_data = load_image(input_path)
    image = _image_to_array(image_data)
    canvas = preset.get("canvas", {})
    image, mm_per_pixel = scale_image_to_canvas(
        image,
        canvas.get("target_width_mm"),
        canvas.get("target_height_mm"),
    )

    preprocessed = process(image, **preset["preprocess"])
    labels = segment(preprocessed, **preset["segment"])
    merged_labels = merge(labels, preprocessed, **preset["merge"])

    palette_config = dict(preset["palette"])
    palette_colors = palette_config.pop("colors", None)
    if palette_colors:
        n_colors = len(palette_colors)
    else:
        n_colors = int(palette_config.pop("n_colors", 4))
    suggested_palette = suggest_palette(preprocessed, n_colors=n_colors)
    print_config = preset.get("print", {})
    catalog_path = Path(
        print_config.get("filament_catalog", "filaments/default_catalog.json")
    )
    catalog = load_catalog(catalog_path)
    _validate_allowed_filaments(catalog, allowed_filaments)
    assigned = assign_palette_to_filaments(
        suggested_palette, catalog, allowed_filaments
    )
    catalog_map = {item["id"]: item for item in catalog.get("filaments", [])}
    assigned_palette = [
        tuple(catalog_map[assigned[idx]]["rgb"]) for idx in range(len(suggested_palette))
    ]
    palette_colors = np.asarray(assigned_palette, dtype=np.uint8)
    paletted = map_palette(preprocessed, palette_colors, **palette_config)
    height_layers = generate_height_map(merged_labels, **preset["height_map"])
    base_layer_mm = float(print_config.get("base_layer_mm", 0.0))
    color_layer_mm = float(print_config.get("color_layer_mm", 0.2))
    blend_depth = float(print_config.get("blend_depth", 1.0))
    if blend_depth <= 0:
        raise ValueError("blend_depth must be > 0")
    height_layers = np.rint(height_layers.astype(np.float32) * blend_depth).astype(
        np.int32
    )
    height_layers[height_layers < 0] = 0
    base_rgb_by_label = _mean_color_by_label(preprocessed, merged_labels)
    layers_by_label = solve_layers_by_label(
        merged_labels,
        base_rgb_by_label,
        list({value for value in assigned.values()}),
        catalog,
        color_layer_mm,
        max_layers=int(round(blend_depth)),
    )
    height_map = layers_to_mm(height_layers, base_layer_mm, color_layer_mm)
    border_mm = float(print_config.get("border_mm", 0.0))
    base_height_mm = float(print_config.get("base_height_mm", base_layer_mm))
    height_map = add_border(height_map, border_mm, mm_per_pixel, base_height_mm)
    max_layers = int(height_layers.max()) if height_layers.size else 0
    total_layers = max_layers + 1
    base_filament_id = str(print_config.get("base_filament_id", "white"))
    sequence_mode = str(print_config.get("sequence_mode", "auto_palette"))
    manual_sequence = print_config.get("layer_sequence_ids", [])
    if sequence_mode == "manual":
        layer_sequence_ids = [str(item) for item in manual_sequence]
    else:
        layer_sequence_ids = _sequence_from_assignment(assigned, len(suggested_palette))
    layer_plan = _layer_plan(
        base_filament_id, layer_sequence_ids, total_layers, base_layer_mm, color_layer_mm
    )
    if mode != "preview":
        mesh = height_map_to_mesh(height_map, mm_per_pixel=mm_per_pixel)
        _write_ascii_stl(mesh, output_stl_path)
        _write_colorplan(
            output_stl_path,
            print_config,
            base_layer_mm,
            color_layer_mm,
            base_filament_id,
            layer_sequence_ids,
            total_layers,
        )
        per_layer = []
        base_mm = 0.32
        step_mm = 0.08
        output_dir = Path(output_stl_path).parent
        for layer_index in range(1, max_layers + 1):
            layer_height = base_mm + layer_index * step_mm
            layer_map = np.where(height_layers >= layer_index, layer_height, 0.0).astype(
                np.float32
            )
            layer_mesh = height_map_to_mesh(layer_map, mm_per_pixel=mm_per_pixel)
            layer_name = f"layer_{layer_index:02d}.stl"
            _write_ascii_stl(layer_mesh, str(output_dir / layer_name))
            per_layer.append(
                {
                    "layer": layer_index,
                    "stl": layer_name,
                    "filament": layer_plan["layers"][layer_index]["filament_id"],
                }
            )
        if per_layer:
            layer_plan["stl_layers"] = per_layer

    if debug_dir:
        preview = _preview_image_by_label(
            merged_labels,
            base_rgb_by_label,
            layers_by_label,
            catalog,
            color_layer_mm,
        )
        _write_debug(
            debug_dir,
            preprocessed=preprocessed,
            labels=merged_labels,
            paletted=paletted,
            height_map=height_map,
            height_layers=height_layers,
            preview=preview,
            palette_suggested=suggested_palette,
            palette_assigned=assigned,
            layers_by_label=layers_by_label,
            layer_plan=layer_plan,
        )

    return {"layer_plan": layer_plan}


def _load_preset(preset_path: Optional[str]) -> Dict[str, Any]:
    if preset_path is None:
        preset_path = str(Path("presets") / "default.json")
    with open(preset_path, "r", encoding="utf-8") as handle:
        preset = json.load(handle)
    return preset


def _apply_overrides(preset: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    merged = json.loads(json.dumps(preset))
    _deep_update(merged, overrides)
    if "palette" in overrides and "n_colors" in overrides["palette"]:
        merged.get("palette", {}).pop("colors", None)
    return merged


def _deep_update(target: Dict[str, Any], updates: Dict[str, Any]) -> None:
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _deep_update(target[key], value)
        else:
            target[key] = value


def _validate_allowed_filaments(
    catalog: Dict[str, Any], allowed_filaments: Optional[List[str]]
) -> None:
    if not allowed_filaments:
        return
    catalog_ids = {item["id"] for item in catalog.get("filaments", [])}
    missing = [fid for fid in allowed_filaments if fid not in catalog_ids]
    if missing:
        raise ValueError(f"allowed_filaments not in catalog: {', '.join(missing)}")


def _image_to_array(image: ImageData) -> np.ndarray:
    array = np.asarray(image.pixels, dtype=np.uint8)
    return array.reshape(image.height, image.width, 3)


def _array_to_image(array: np.ndarray) -> ImageData:
    height, width, _ = array.shape
    pixels = tuple(map(tuple, array.reshape(-1, 3)))
    return ImageData(width=width, height=height, pixels=pixels)


def _write_debug(
    debug_dir: str,
    *,
    preprocessed: np.ndarray,
    labels: np.ndarray,
    paletted: np.ndarray,
    height_map: np.ndarray,
    height_layers: Optional[np.ndarray] = None,
    preview: Optional[np.ndarray] = None,
    palette_suggested: Optional[List[Tuple[int, int, int]]] = None,
    palette_assigned: Optional[Dict[int, str]] = None,
    layers_by_label: Optional[Dict[int, List[Tuple[str, int]]]] = None,
    layer_plan: Optional[Dict[str, Any]] = None,
) -> None:
    path = Path(debug_dir)
    path.mkdir(parents=True, exist_ok=True)

    save_image(_array_to_image(preprocessed), path / "preprocess.png")
    save_image(_array_to_image(paletted), path / "palette.png")
    save_image(_array_to_image(_labels_to_rgb(labels)), path / "labels.png")
    save_image(_array_to_image(_height_to_rgb(height_map)), path / "height.png")
    if preview is not None:
        save_image(_array_to_image(preview), path / "preview.png")
    if height_layers is not None:
        np.save(path / "height_layers.npy", height_layers)
    np.save(path / "height_mm.npy", height_map)
    if palette_suggested is not None:
        (path / "palette_suggested.json").write_text(
            json.dumps({"palette": palette_suggested}, indent=2),
            encoding="utf-8",
        )
    if palette_assigned is not None:
        (path / "palette_assigned.json").write_text(
            json.dumps({"assignment": palette_assigned}, indent=2),
            encoding="utf-8",
        )
    if layers_by_label is not None:
        (path / "layers_by_label.json").write_text(
            json.dumps({"layers_by_label": layers_by_label}, indent=2),
            encoding="utf-8",
        )
    if layer_plan is not None:
        (path / "layer_plan.json").write_text(
            json.dumps(layer_plan, indent=2),
            encoding="utf-8",
        )


def _labels_to_rgb(labels: np.ndarray) -> np.ndarray:
    max_label = int(labels.max(initial=0))
    if max_label == 0:
        scaled = np.zeros(labels.shape, dtype=np.uint8)
    else:
        scaled = np.rint(labels.astype(np.float32) / max_label * 255.0).astype(np.uint8)
    return np.repeat(scaled[:, :, None], 3, axis=2)


def _height_to_rgb(height_map: np.ndarray) -> np.ndarray:
    max_height = float(np.max(height_map)) if height_map.size else 0.0
    if max_height == 0.0:
        scaled = np.zeros(height_map.shape, dtype=np.uint8)
    else:
        scaled = np.rint(height_map / max_height * 255.0).astype(np.uint8)
    return np.repeat(scaled[:, :, None], 3, axis=2)


def _mean_color_by_label(
    image: np.ndarray, labels: np.ndarray
) -> Dict[int, Tuple[int, int, int]]:
    means: Dict[int, Tuple[int, int, int]] = {}
    for label in np.unique(labels):
        mask = labels == label
        rgb = image[mask].mean(axis=0)
        means[int(label)] = tuple(int(round(v)) for v in rgb)
    return means


def _write_ascii_stl(mesh: Mesh, path: str) -> None:
    vertices = mesh.vertices
    faces = mesh.faces
    lines = ["solid relief"]
    for face in faces:
        v0, v1, v2 = vertices[face]
        normal = np.cross(v1 - v0, v2 - v0)
        norm = np.linalg.norm(normal)
        if norm == 0:
            normal = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        else:
            normal = normal / norm
        lines.append(
            f"  facet normal {normal[0]:.6e} {normal[1]:.6e} {normal[2]:.6e}"
        )
        lines.append("    outer loop")
        lines.append(f"      vertex {v0[0]:.6e} {v0[1]:.6e} {v0[2]:.6e}")
        lines.append(f"      vertex {v1[0]:.6e} {v1[1]:.6e} {v1[2]:.6e}")
        lines.append(f"      vertex {v2[0]:.6e} {v2[1]:.6e} {v2[2]:.6e}")
        lines.append("    endloop")
        lines.append("  endfacet")
    lines.append("endsolid relief")

    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def _write_colorplan(
    output_path: str,
    print_config: Dict[str, Any],
    base_layer_mm: float,
    color_layer_mm: float,
    base_filament_id: str,
    layer_sequence_ids: List[str],
    total_layers: int,
) -> None:
    base_layer_mm = 0.32
    color_layer_mm = 0.08
    max_layers = 7
    catalog_path = Path(print_config.get("filament_catalog", "filaments/default_catalog.json"))
    catalog = load_catalog(catalog_path)
    if not layer_sequence_ids:
        layer_sequence_ids = [_fallback_filament_id(catalog)]
    base_filament_id = layer_sequence_ids[0]
    if len(layer_sequence_ids) == 1:
        for item in catalog.get("filaments", []):
            candidate = str(item.get("id", "")).strip()
            if not candidate or candidate == base_filament_id or candidate == "white":
                continue
            layer_sequence_ids = [base_filament_id, candidate]
            break
    if total_layers < 2:
        total_layers = 2
    total_layers = min(total_layers, max_layers + 1, len(layer_sequence_ids) + 1)
    if total_layers < 1:
        total_layers = 1

    layers = []
    for idx in range(total_layers):
        if idx == 0:
            filament_id = base_filament_id
        else:
            seq_index = idx
            if seq_index >= len(layer_sequence_ids):
                seq_index = len(layer_sequence_ids) - 1
            filament_id = layer_sequence_ids[seq_index]
        layers.append(
            {
                "layer_index": idx,
                "z_mm": base_layer_mm + idx * color_layer_mm,
                "filament_id": filament_id,
            }
        )

    start = layers[0]
    changes: List[Dict[str, Any]] = []
    current_id = start["filament_id"]
    for layer in layers[1:]:
        if layer["filament_id"] == current_id:
            continue
        changes.append(layer)
        current_id = layer["filament_id"]

    all_layers = [start] + changes
    total_layers = 1 + max(item["layer_index"] for item in all_layers)
    plan = {
        "total_layers": total_layers,
        "start": start,
        "changes": changes,
    }
    export_colorplan_txt(Path(output_path), plan, catalog, base_layer_mm, color_layer_mm)


def _build_colorplan(
    base_filament_id: str,
    layer_sequence_ids: List[str],
    base_layer_mm: float,
    color_layer_mm: float,
    catalog: Dict[str, Any],
    total_layers: int,
) -> Dict[str, Any]:
    if total_layers < 2:
        total_layers = 2
    if not layer_sequence_ids:
        layer_sequence_ids = [_fallback_filament_id(catalog)]

    plan = _layer_plan(
        base_filament_id, layer_sequence_ids, total_layers, base_layer_mm, color_layer_mm
    )
    start = plan["layers"][0]
    changes = plan["layers"][1:]

    return {
        "total_layers": total_layers,
        "start": start,
        "changes": changes,
    }


def _fallback_filament_id(catalog: Dict[str, Any]) -> str:
    filaments = catalog.get("filaments", [])
    if not filaments:
        return "base"
    return str(filaments[0]["id"])


def _sequence_from_assignment(
    assignment: Dict[int, str], palette_len: int
) -> List[str]:
    sequence: List[str] = []
    for idx in range(palette_len):
        filament_id = assignment.get(idx)
        if filament_id and filament_id not in sequence:
            sequence.append(filament_id)
    return sequence


def _layer_plan(
    base_filament_id: str,
    layer_sequence_ids: List[str],
    total_layers: int,
    base_layer_mm: float,
    color_layer_mm: float,
) -> Dict[str, Any]:
    base_mm = 0.32
    step_mm = 0.08
    max_layers = 7

    if total_layers < 2:
        total_layers = 2
    if not layer_sequence_ids:
        layer_sequence_ids = [base_filament_id]
    if base_filament_id not in layer_sequence_ids:
        base_filament_id = layer_sequence_ids[0]
    if total_layers > max_layers + 1:
        total_layers = max_layers + 1

    layers = []
    for idx in range(total_layers):
        if idx == 0:
            filament_id = base_filament_id
        else:
            filament_id = layer_sequence_ids[(idx - 1) % len(layer_sequence_ids)]
        layers.append(
            {
                "layer_index": idx,
                "z_mm": base_mm + idx * step_mm,
                "filament_id": filament_id,
            }
        )
    return {"layers": layers}


def _preview_image_by_label(
    labels: np.ndarray,
    base_rgb_by_label: Dict[int, Tuple[int, int, int]],
    layers_by_label: Dict[int, List[Tuple[str, int]]],
    catalog: Dict[str, Any],
    color_layer_mm: float,
) -> np.ndarray:
    preview_map: Dict[int, Tuple[int, int, int]] = {}
    for label, base_rgb in base_rgb_by_label.items():
        stack = layers_by_label.get(label, [])
        preview_map[label] = simulate_stack(base_rgb, stack, catalog, color_layer_mm)
    output = np.zeros((*labels.shape, 3), dtype=np.uint8)
    for label, rgb in preview_map.items():
        output[labels == label] = rgb
    return output
