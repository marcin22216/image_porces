from __future__ import annotations

import json
import math
import struct
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from src.app.image_io import ImageData, load_image, save_image
from src.geom.mesh_generation import Mesh, height_map_to_mesh
from src.ops.height_map import generate_height_map
from src.ops.layers_to_mm import layers_to_mm
from src.ops.add_border import add_border
from src.ops.palette_suggestion import suggest_palette
from src.print.colorplan_export import export_colorplan_txt
from src.print.filament_assignment import assign_palette_to_filaments
from src.print.filaments import load_catalog
from src.solver.region_recipe import solve_layers_by_label
from src.sim.td_preview import simulate_stack
from src.ops.merge_small_regions import merge
from src.ops.palette_mapping import map_palette
from src.ops.preprocess_edge_preserving import process
from src.ops.scale_to_canvas import scale_image_to_canvas
from src.ops.segment_superpixels import segment


def run_pipeline(
    input_path: str,
    output_path: str,
    *,
    debug_dir: Optional[str] = None,
    preset_path: Optional[str] = None,
    allowed_filaments: Optional[List[str]] = None,
    overrides: Optional[Dict[str, Any]] = None,
    mode: str = "full",
) -> None:
    preset = _load_preset(preset_path)
    if overrides:
        preset = _apply_overrides(preset, overrides)

    stage_start = time.monotonic()
    xy_step_mm = _resolve_xy_step_mm(preset)
    image_data = load_image(input_path)
    image = _image_to_array(image_data)
    canvas = preset.get("canvas", {})
    image, mm_per_pixel = scale_image_to_canvas(
        image,
        canvas.get("target_width_mm"),
        canvas.get("target_height_mm"),
    )
    _report_guardrails(
        input_px=(image_data.width, image_data.height),
        scaled_px=(image.shape[1], image.shape[0]),
        mm_per_pixel=mm_per_pixel,
        xy_step_mm=xy_step_mm,
    )
    preprocessed = process(image, **preset["preprocess"])
    _log_stage_time("load_preprocess", stage_start)

    stage_start = time.monotonic()
    labels = segment(preprocessed, **preset["segment"])
    merged_labels = merge(labels, preprocessed, **preset["merge"])
    _log_stage_time("segment_merge", stage_start)

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
    height_mode = preset.get("height_map", {}).get("mode", "by_index")
    base_layer_mm = float(print_config.get("base_layer_mm", 0.0))
    color_layer_mm = float(print_config.get("color_layer_mm", 0.2))
    blend_depth = float(print_config.get("blend_depth", 1.0))
    if blend_depth <= 0:
        raise ValueError("blend_depth must be > 0")
    stage_start = time.monotonic()
    if height_mode == "optical_hueforge":
        max_thickness_mm = print_config.get("max_thickness_mm")
        if max_thickness_mm is None:
            raise ValueError("print.max_thickness_mm is required for optical_hueforge")
        height_map = generate_height_map(
            preprocessed,
            mode="optical_hueforge",
            image_rgb=preprocessed,
            optical=preset.get("optical", {}),
            catalog=catalog,
            max_thickness_mm=max_thickness_mm,
        )
        height_layers = _height_mm_to_layers(height_map, color_layer_mm)
    else:
        height_layers = generate_height_map(merged_labels, **preset["height_map"])
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
    if height_mode != "optical_hueforge":
        height_map = layers_to_mm(height_layers, base_layer_mm, color_layer_mm)
    border_mm = float(print_config.get("border_mm", 0.0))
    base_height_mm = float(print_config.get("base_height_mm", base_layer_mm))
    height_map = add_border(height_map, border_mm, mm_per_pixel, base_height_mm)
    _log_stage_time("heightfield", stage_start)
    max_layers = int(height_layers.max()) if height_layers.size else 0
    base_filament_id = str(print_config.get("base_filament_id", "white"))
    sequence_mode = str(print_config.get("sequence_mode", "auto_palette"))
    manual_sequence = print_config.get("layer_sequence_ids", [])
    if height_mode == "optical_hueforge":
        stack_ids, thresholds = _load_optical_stack(preset.get("optical", {}))
        base_filament_id = stack_ids[0]
        layer_sequence_ids = stack_ids
        total_layers = _total_layers_from_thresholds(
            thresholds, color_layer_mm, rounding="ceil"
        )
        layer_plan = _layer_plan_optical(
            stack_ids, thresholds, total_layers, base_layer_mm, color_layer_mm
        )
    else:
        if sequence_mode == "manual":
            layer_sequence_ids = [str(item) for item in manual_sequence]
        else:
            layer_sequence_ids = _sequence_from_assignment(
                assigned, len(suggested_palette)
            )
        total_layers = max_layers + 1
        layer_plan = _layer_plan(
            base_filament_id,
            layer_sequence_ids,
            total_layers,
            base_layer_mm,
            color_layer_mm,
        )
    if mode != "preview":
        stl_format = _resolve_stl_format(preset)
        stage_start = time.monotonic()
        mesh = height_map_to_mesh(
            height_map, mm_per_pixel=mm_per_pixel, xy_step_mm=xy_step_mm
        )
        _log_stage_time("mesh_generation", stage_start)
        stage_start = time.monotonic()
        _write_stl(mesh, output_path, stl_format)
        _log_stage_time("stl_write", stage_start)
        if height_mode == "optical_hueforge":
            _write_colorplan_optical(
                output_path,
                print_config,
                stack_ids,
                thresholds,
                base_layer_mm,
                color_layer_mm,
            )
        else:
            _write_colorplan(
                output_path,
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
            output_dir = Path(output_path).parent
            for layer_index in range(1, max_layers + 1):
                layer_height = base_mm + layer_index * step_mm
                layer_map = np.where(
                    height_layers >= layer_index, layer_height, 0.0
                ).astype(np.float32)
                layer_mesh = height_map_to_mesh(
                    layer_map, mm_per_pixel=mm_per_pixel, xy_step_mm=xy_step_mm
                )
                layer_name = f"layer_{layer_index:02d}.stl"
                _write_stl(layer_mesh, str(output_dir / layer_name), stl_format)
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


def _write_binary_stl(mesh: Mesh, path: str) -> None:
    vertices = mesh.vertices
    faces = mesh.faces
    header = b"hueforge binary stl"
    header = header.ljust(80, b" ")
    with open(path, "wb") as handle:
        handle.write(header[:80])
        handle.write(struct.pack("<I", len(faces)))
        for face in faces:
            v0, v1, v2 = vertices[face]
            normal = np.cross(v1 - v0, v2 - v0)
            norm = np.linalg.norm(normal)
            if norm == 0:
                normal = np.array([0.0, 0.0, 0.0], dtype=np.float32)
            else:
                normal = normal / norm
            handle.write(
                struct.pack(
                    "<12fH",
                    float(normal[0]),
                    float(normal[1]),
                    float(normal[2]),
                    float(v0[0]),
                    float(v0[1]),
                    float(v0[2]),
                    float(v1[0]),
                    float(v1[1]),
                    float(v1[2]),
                    float(v2[0]),
                    float(v2[1]),
                    float(v2[2]),
                    0,
                )
            )


def _write_stl(mesh: Mesh, path: str, stl_format: str) -> None:
    if stl_format == "ascii":
        _write_ascii_stl(mesh, path)
        return
    if stl_format == "binary":
        _write_binary_stl(mesh, path)
        return
    raise ValueError("mesh.stl_format must be 'binary' or 'ascii'")


def _resolve_stl_format(preset: Dict[str, Any]) -> str:
    mesh_config = preset.get("mesh") or {}
    stl_format = str(mesh_config.get("stl_format", "binary")).strip().lower()
    if stl_format not in {"binary", "ascii"}:
        raise ValueError("mesh.stl_format must be 'binary' or 'ascii'")
    return stl_format


def _resolve_xy_step_mm(preset: Dict[str, Any]) -> float:
    mesh_config = preset.get("mesh") or {}
    xy_step_mm = mesh_config.get("xy_step_mm")
    if xy_step_mm is None:
        xy_step_mm = mesh_config.get("detail_size_mm")
    if xy_step_mm is None:
        xy_step_mm = 0.20
    xy_step_mm = float(xy_step_mm)
    if xy_step_mm <= 0:
        raise ValueError("mesh.xy_step_mm must be > 0")
    return xy_step_mm


def _log_stage_time(stage_name: str, started_at: float) -> None:
    elapsed = time.monotonic() - started_at
    print(f"STAGE_TIME_SEC stage_name={stage_name} seconds={elapsed:.6f}")


def _report_guardrails(
    *,
    input_px: tuple[int, int],
    scaled_px: tuple[int, int],
    mm_per_pixel: float,
    xy_step_mm: float,
) -> None:
    width_px, height_px = scaled_px
    width_mm = width_px * mm_per_pixel
    height_mm = height_px * mm_per_pixel
    grid_width = max(1, int(math.ceil(width_mm / xy_step_mm)))
    grid_height = max(1, int(math.ceil(height_mm / xy_step_mm)))
    expected_triangles = int(grid_width * grid_height * 2)
    print(
        "GUARDRAIL_INFO "
        f"input_px={input_px[0]}x{input_px[1]} "
        f"canvas_mm={width_mm:.3f}x{height_mm:.3f} "
        f"effective_grid={grid_width}x{grid_height} "
        f"expected_triangles={expected_triangles}"
    )
    _enforce_guardrails(grid_width, grid_height, expected_triangles)


def _enforce_guardrails(width_px: int, height_px: int, expected_triangles: int) -> None:
    max_dim = 2048
    max_triangles = 2_000_000
    if width_px > max_dim or height_px > max_dim or expected_triangles > max_triangles:
        raise ValueError(
            "Guardrail: configuration too heavy for this CLI. "
            f"effective_grid={width_px}x{height_px} expected_triangles={expected_triangles}. "
            "Consider downscaling the input or reducing canvas size."
        )


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


def _height_mm_to_layers(height_map: np.ndarray, layer_height_mm: float) -> np.ndarray:
    if layer_height_mm <= 0:
        raise ValueError("color_layer_mm must be > 0")
    layers = np.floor(height_map / float(layer_height_mm) + 1e-6).astype(np.int32)
    layers[layers < 0] = 0
    return layers


def _load_optical_stack(optical: Dict[str, Any]) -> Tuple[List[str], List[float]]:
    stack_ids = optical.get("stack_filament_ids")
    thresholds = optical.get("stack_thresholds_mm")
    if not isinstance(stack_ids, list) or not stack_ids:
        raise ValueError("optical.stack_filament_ids must be non-empty list")
    if not isinstance(thresholds, list) or not thresholds:
        raise ValueError("optical.stack_thresholds_mm must be non-empty list")
    if len(stack_ids) != len(thresholds):
        raise ValueError("optical stack ids and thresholds must match length")
    return [str(item) for item in stack_ids], [float(item) for item in thresholds]


def _total_layers_from_thresholds(
    thresholds: List[float], layer_height_mm: float, rounding: str
) -> int:
    indices = _thresholds_to_layer_indices(thresholds, layer_height_mm, rounding)
    if not indices:
        return 1
    return max(indices) + 1


def _thresholds_to_layer_indices(
    thresholds: List[float], layer_height_mm: float, rounding: str
) -> List[int]:
    if layer_height_mm <= 0:
        raise ValueError("color_layer_mm must be > 0")
    indices: List[int] = []
    for threshold in thresholds:
        ratio = threshold / layer_height_mm
        if rounding == "ceil":
            idx = int(math.ceil(ratio))
        elif rounding == "floor":
            idx = int(math.floor(ratio))
        else:
            raise ValueError("rounding must be 'ceil' or 'floor'")
        if idx < 0:
            idx = 0
        indices.append(idx)
    return indices


def _filament_for_depth(
    depth_mm: float, stack_ids: List[str], thresholds: List[float]
) -> str:
    for filament_id, threshold in zip(stack_ids, thresholds):
        if depth_mm <= threshold:
            return filament_id
    return stack_ids[-1]


def _layer_plan_optical(
    stack_ids: List[str],
    thresholds: List[float],
    total_layers: int,
    base_layer_mm: float,
    color_layer_mm: float,
) -> Dict[str, Any]:
    layers = []
    for idx in range(total_layers):
        depth = float(idx) * color_layer_mm
        filament_id = _filament_for_depth(depth, stack_ids, thresholds)
        layers.append(
            {
                "layer_index": idx,
                "z_mm": base_layer_mm + idx * color_layer_mm,
                "filament_id": filament_id,
            }
        )
    return {"layers": layers}


def _write_colorplan_optical(
    output_path: str,
    print_config: Dict[str, Any],
    stack_ids: List[str],
    thresholds: List[float],
    base_layer_mm: float,
    color_layer_mm: float,
) -> None:
    catalog_path = Path(
        print_config.get("filament_catalog", "filaments/default_catalog.json")
    )
    catalog = load_catalog(catalog_path)
    change_indices = _thresholds_to_layer_indices(
        thresholds[:-1], color_layer_mm, rounding="ceil"
    )
    changes = []
    last_layer_index = 0
    current_id = stack_ids[0]
    for idx, layer_index in enumerate(change_indices):
        if layer_index <= last_layer_index:
            continue
        filament_id = stack_ids[idx + 1]
        if filament_id == current_id:
            continue
        changes.append(
            {
                "layer_index": layer_index,
                "z_mm": base_layer_mm + layer_index * color_layer_mm,
                "filament_id": filament_id,
            }
        )
        last_layer_index = layer_index
        current_id = filament_id
    total_layers = _total_layers_from_thresholds(
        thresholds, color_layer_mm, rounding="ceil"
    )
    plan = {
        "total_layers": total_layers,
        "start": {
            "layer_index": 0,
            "z_mm": base_layer_mm,
            "filament_id": stack_ids[0],
        },
        "changes": changes,
    }
    export_colorplan_txt(Path(output_path), plan, catalog, base_layer_mm, color_layer_mm)


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
