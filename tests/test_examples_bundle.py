import subprocess
import sys
import zipfile
from pathlib import Path


def test_examples_bundle_smoke(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    input_path = repo_root / "examples" / "input.png"
    output_zip = tmp_path / "examples_bundle.zip"

    subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "bundle",
            "--in",
            str(input_path),
            "--out",
            str(output_zip),
            "--width-mm",
            "20",
            "--height-mm",
            "20",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )

    assert output_zip.exists()
    with zipfile.ZipFile(output_zip, "r") as archive:
        names = set(archive.namelist())

    assert any(name.endswith(".stl") for name in names)
    assert any(name.endswith(".colorplan.txt") for name in names)
    assert "preview.png" in names
    assert "config.effective.json" in names
