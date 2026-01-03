import json
import struct
import subprocess
import sys
import zipfile
from pathlib import Path

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
            str(repo_root / "tests" / "fixtures" / "gradient_64.png"),
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


def _collect_vertex_z(stl_path: Path) -> list[float]:
    metrics = analyze_stl(stl_path)
    if metrics["format"] == "binary":
        return _collect_vertex_z_binary(stl_path)
    values: list[float] = []
    with stl_path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped.startswith("vertex "):
                continue
            parts = stripped.split()
            if len(parts) < 4:
                continue
            try:
                values.append(float(parts[3]))
            except ValueError:
                continue
    if not values:
        raise AssertionError("no vertices found in STL")
    return values


def _collect_vertex_z_binary(stl_path: Path) -> list[float]:
    values: list[float] = []
    with stl_path.open("rb") as handle:
        handle.seek(80)
        count_bytes = handle.read(4)
        if len(count_bytes) != 4:
            raise AssertionError("binary STL header is incomplete")
        tri_count = struct.unpack("<I", count_bytes)[0]
        for _ in range(tri_count):
            data = handle.read(50)
            if len(data) != 50:
                raise AssertionError("binary STL ended unexpectedly")
            unpacked = struct.unpack("<12fH", data)
            values.extend([unpacked[5], unpacked[8], unpacked[11]])
    if not values:
        raise AssertionError("no vertices found in binary STL")
    return values


def test_optical_hueforge_continuous_heightfield(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    base_preset = json.loads(
        (repo_root / "presets" / "default.json").read_text(encoding="utf-8")
    )
    base_preset["canvas"]["target_width_mm"] = 60.0
    base_preset["canvas"]["target_height_mm"] = 60.0
    base_preset["height_map"] = {"mode": "optical_hueforge"}
    base_preset["optical"] = {
        "stack_filament_ids": ["black"],
        "stack_thresholds_mm": [2.0],
        "metric": "rgb",
        "color_space": "linear_srgb",
        "step_mm": 0.02,
    }
    base_preset["print"]["max_thickness_mm"] = 2.0
    base_preset["print"]["color_layer_mm"] = 0.08

    preset_path = tmp_path / "optical_continuous.json"
    _write_preset(preset_path, base_preset)

    zip_path = tmp_path / "out.zip"
    _run_bundle(repo_root, preset_path, zip_path)

    stl_path = _read_stl_from_zip(zip_path)
    z_values = _collect_vertex_z(stl_path)
    unique_z = {round(value, 6) for value in z_values}
    min_z = min(z_values)
    max_z = max(z_values)
    z_range = max_z - min_z

    assert len(unique_z) > 10
    assert z_range > 0.5
