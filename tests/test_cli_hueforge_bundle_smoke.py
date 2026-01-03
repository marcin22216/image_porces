import json
import subprocess
import sys
import zipfile
from pathlib import Path

from src.tools.stl_diagnostics import analyze_stl


def test_cli_hueforge_bundle_smoke(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    input_path = repo_root / "tests" / "fixtures" / "tiny.png"
    output_zip = tmp_path / "out.zip"
    debug_dir = tmp_path / "dbg"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "hueforge-bundle",
            "--in",
            str(input_path),
            "--out",
            str(output_zip),
            "--debug",
            str(debug_dir),
            "--width-mm",
            "10",
            "--height-mm",
            "1",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr + result.stdout
    assert output_zip.exists()
    stage_names = [
        "load_preprocess",
        "segment_merge",
        "heightfield",
        "mesh_generation",
        "stl_write",
    ]
    for stage in stage_names:
        assert f"STAGE_TIME_SEC stage_name={stage}" in result.stdout

    base = output_zip.stem
    with zipfile.ZipFile(output_zip, "r") as archive:
        names = set(archive.namelist())
        layer_plan = json.loads(archive.read("layer_plan.json").decode("utf-8"))
        stl_path = tmp_path / f"{base}.stl"
        stl_path.write_bytes(archive.read(f"{base}.stl"))

    expected = {
        f"{base}.stl",
        f"{base}.colorplan.txt",
        "preview.png",
        "palette_suggested.json",
        "palette_assigned.json",
        "layer_plan.json",
        "config.effective.json",
    }
    assert expected.issubset(names)

    _layer_stls = [
        name for name in names if name.startswith("layer_") and name.endswith(".stl")
    ]

    metrics = analyze_stl(stl_path)
    assert metrics["format"] == "binary"
