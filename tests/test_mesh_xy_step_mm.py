import json
import subprocess
import sys
import zipfile
from pathlib import Path

from src.tools.stl_diagnostics import analyze_stl


def _write_preset(path: Path, step_mm: float) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    preset = json.loads((repo_root / "presets" / "default.json").read_text(encoding="utf-8"))
    preset["canvas"]["target_width_mm"] = 20.0
    preset["canvas"]["target_height_mm"] = 20.0
    preset.setdefault("mesh", {})["xy_step_mm"] = step_mm
    path.write_text(json.dumps(preset, indent=2), encoding="utf-8")


def _run_bundle(repo_root: Path, preset_path: Path, output_zip: Path) -> None:
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
            "--preset",
            str(preset_path),
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


def test_mesh_xy_step_mm_controls_triangle_count(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    preset_020 = tmp_path / "step_020.json"
    preset_010 = tmp_path / "step_010.json"
    _write_preset(preset_020, 0.20)
    _write_preset(preset_010, 0.10)

    zip_020 = tmp_path / "out_020.zip"
    zip_010 = tmp_path / "out_010.zip"
    _run_bundle(repo_root, preset_020, zip_020)
    _run_bundle(repo_root, preset_010, zip_010)

    stl_020 = _read_stl_from_zip(zip_020)
    stl_010 = _read_stl_from_zip(zip_010)
    triangles_020 = analyze_stl(stl_020)["triangles"]
    triangles_010 = analyze_stl(stl_010)["triangles"]

    assert triangles_010 > triangles_020
