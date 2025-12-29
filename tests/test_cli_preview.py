import subprocess
import sys
from pathlib import Path

from src.app.image_io import ImageData, save_image


def test_cli_preview_smoke(tmp_path):
    input_path = tmp_path / "input.png"
    debug_dir = tmp_path / "debug"

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
            "preview",
            "--in",
            str(input_path),
            "--debug",
            str(debug_dir),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )

    assert (debug_dir / "preview.png").exists()
    assert (debug_dir / "palette_suggested.json").exists()
    assert (debug_dir / "palette_assigned.json").exists()
    assert (debug_dir / "layer_plan.json").exists()
    assert not (debug_dir / "output.stl").exists()
    assert not (debug_dir / "output.colorplan.txt").exists()
