import json
import subprocess
import sys
from pathlib import Path


def _write_preset(path: Path, preset: dict) -> None:
    path.write_text(json.dumps(preset, indent=2), encoding="utf-8")


def test_optical_hueforge_requires_optical_config(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    base_preset = json.loads(
        (repo_root / "presets" / "default.json").read_text(encoding="utf-8")
    )
    base_preset["height_map"] = {"mode": "optical_hueforge"}
    base_preset["print"]["max_thickness_mm"] = 0.72
    base_preset["print"]["color_layer_mm"] = 0.08
    base_preset["optical"] = {}

    preset_path = tmp_path / "missing_optical.json"
    _write_preset(preset_path, base_preset)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "hueforge-bundle",
            "--in",
            str(repo_root / "tests" / "fixtures" / "tiny.png"),
            "--out",
            str(tmp_path / "out.zip"),
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
    combined = result.stderr + result.stdout
    assert result.returncode != 0
    assert "optical_hueforge requires optical.*" in combined
