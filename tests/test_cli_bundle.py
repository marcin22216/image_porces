import subprocess
import sys
import zipfile
from pathlib import Path

from src.app.image_io import ImageData, save_image


def test_cli_bundle_smoke(tmp_path):
    input_path = tmp_path / "input.png"
    output_zip = tmp_path / "bundle.zip"

    pixels = (
        (10, 10, 10),
        (20, 20, 20),
        (230, 230, 230),
        (240, 240, 240),
    )
    image = ImageData(width=2, height=2, pixels=pixels)
    save_image(image, input_path)

    repo_root = Path(__file__).resolve().parents[1]
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
            "10",
            "--height-mm",
            "10",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )

    assert output_zip.exists()
    with zipfile.ZipFile(output_zip, "r") as archive:
        names = set(archive.namelist())
    base = "bundle"
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


def test_cli_bundle_input_directory_error(tmp_path):
    output_zip = tmp_path / "bundle.zip"
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "bundle",
            "--in",
            str(tmp_path),
            "--out",
            str(output_zip),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "directory" in (result.stderr + result.stdout).lower()
