import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path

from src.tools.stl_diagnostics import analyze_stl


def _write_preset(path: Path, preset: dict) -> None:
    path.write_text(json.dumps(preset, indent=2), encoding="utf-8")


def _run_bundle(repo_root: Path, preset_path: Path, output_zip: Path, debug_dir: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "hueforge-bundle",
            "--in",
            str(repo_root / "tests" / "fixtures" / "tiny.png"),
            "--out",
            str(output_zip),
            "--debug",
            str(debug_dir),
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


def test_optical_hueforge_heightfield_smoke(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    base_preset = json.loads(
        (repo_root / "presets" / "default.json").read_text(encoding="utf-8")
    )
    base_preset["height_map"] = {"mode": "optical_hueforge"}
    base_preset["optical"] = {
        "stack_filament_ids": ["base", "black", "blue"],
        "stack_thresholds_mm": [0.24, 0.48, 0.72],
        "metric": "rgb",
        "color_space": "linear_srgb",
        "step_mm": 0.02,
    }
    base_preset["print"]["max_thickness_mm"] = 0.72
    base_preset["print"]["color_layer_mm"] = 0.08

    preset_path = tmp_path / "optical.json"
    _write_preset(preset_path, base_preset)

    zip_path = tmp_path / "out.zip"
    debug_dir = tmp_path / "dbg"
    _run_bundle(repo_root, preset_path, zip_path, debug_dir)

    stl_path = _read_stl_from_zip(zip_path)
    metrics = analyze_stl(stl_path)
    z_range = metrics["bbox_max"][2] - metrics["bbox_min"][2]
    assert z_range > 0.05

    total_layers = _read_total_layers(zip_path)
    assert total_layers > 5

    zip_path_2 = tmp_path / "out2.zip"
    debug_dir_2 = tmp_path / "dbg2"
    _run_bundle(repo_root, preset_path, zip_path_2, debug_dir_2)
    stl_path_2 = _read_stl_from_zip(zip_path_2)
    digest_1 = hashlib.sha256(stl_path.read_bytes()).hexdigest()
    digest_2 = hashlib.sha256(stl_path_2.read_bytes()).hexdigest()
    assert digest_1 == digest_2
