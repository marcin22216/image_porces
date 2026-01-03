import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path

import numpy as np

from hueforge.geometry.height_map import generate_height_map
from hueforge.geometry.layers_to_mm import layers_to_mm
from hueforge.preprocessing.merge_small_regions import merge
from hueforge.preprocessing.preprocess_edge_preserving import process
from hueforge.preprocessing.scale import scale_image_to_canvas
from hueforge.preprocessing.segment_superpixels import segment
from src.app.image_io import load_image
from src.tools.stl_diagnostics import analyze_stl


def _write_preset(path: Path, preset: dict) -> None:
    path.write_text(json.dumps(preset, indent=2), encoding="utf-8")


def _run_bundle(repo_root: Path, preset_path: Path, output_zip: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "hueforge-bundle",
            "--in",
            str(repo_root / "tests" / "fixtures" / "by_index_two_regions.png"),
            "--out",
            str(output_zip),
            "--preset",
            str(preset_path),
            "--width-mm",
            "40",
            "--height-mm",
            "40",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def _read_stl_from_zip(zip_path: Path) -> Path:
    stl_name = f"{zip_path.stem}.stl"
    stl_path = zip_path.parent / stl_name
    with zipfile.ZipFile(zip_path, "r") as archive:
        stl_path.write_bytes(archive.read(stl_name))
    return stl_path


def _read_total_layers(zip_path: Path) -> int:
    plan_name = f"{zip_path.stem}.colorplan.txt"
    with zipfile.ZipFile(zip_path, "r") as archive:
        text = archive.read(plan_name).decode("utf-8")
    for line in text.splitlines():
        if line.startswith("TOTAL_LAYERS"):
            return int(line.split()[1])
    raise AssertionError("TOTAL_LAYERS not found")


def test_height_map_by_index_non_regression(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    base_preset = json.loads(
        (repo_root / "presets" / "default.json").read_text(encoding="utf-8")
    )
    base_preset["height_map"] = {"mode": "by_index", "scale": 0.5}
    base_preset.setdefault("mesh", {})["xy_step_mm"] = 0.5

    preset_path = tmp_path / "by_index.json"
    _write_preset(preset_path, base_preset)

    image = load_image(
        repo_root / "tests" / "fixtures" / "by_index_two_regions.png"
    )
    image_array = np.asarray(image.pixels, dtype=np.uint8).reshape(
        image.height, image.width, 3
    )
    canvas = base_preset.get("canvas", {})
    image_array, _ = scale_image_to_canvas(
        image_array,
        canvas.get("target_width_mm"),
        canvas.get("target_height_mm"),
    )
    preprocessed = process(image_array, **base_preset["preprocess"])
    labels = segment(preprocessed, **base_preset["segment"])
    merged_labels = merge(labels, preprocessed, **base_preset["merge"])
    unique_labels = np.unique(merged_labels)
    height_layers = generate_height_map(
        merged_labels, mode="by_index", scale=0.5
    )
    unique_layers = np.unique(height_layers)
    base_layer_mm = float(base_preset["print"].get("base_layer_mm", 0.0))
    color_layer_mm = float(base_preset["print"].get("color_layer_mm", 0.2))
    height_mm = layers_to_mm(height_layers, base_layer_mm, color_layer_mm)
    height_min = float(height_mm.min(initial=0.0))
    height_max = float(height_mm.max(initial=0.0))

    assert unique_labels.size > 1
    assert unique_layers.size > 1
    assert height_max > height_min

    zip_path = tmp_path / "out.zip"
    _run_bundle(repo_root, preset_path, zip_path)

    stl_path = _read_stl_from_zip(zip_path)
    metrics = analyze_stl(stl_path)
    z_range = metrics["bbox_max"][2] - metrics["bbox_min"][2]
    assert z_range > 0.05

    total_layers = _read_total_layers(zip_path)
    assert total_layers > 1

    zip_path_2 = tmp_path / "out2.zip"
    _run_bundle(repo_root, preset_path, zip_path_2)
    stl_path_2 = _read_stl_from_zip(zip_path_2)
    digest_1 = hashlib.sha256(stl_path.read_bytes()).hexdigest()
    digest_2 = hashlib.sha256(stl_path_2.read_bytes()).hexdigest()
    assert digest_1 == digest_2
