import subprocess
import sys
from pathlib import Path

from src.app.image_io import ImageData, save_image


def test_cli_pipeline_smoke(tmp_path):
    input_path = tmp_path / "input.png"
    output_path = tmp_path / "output.stl"
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
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "run",
            "--in",
            str(input_path),
            "--out",
            str(output_path),
            "--debug",
            str(debug_dir),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )

    assert output_path.exists()
    assert output_path.stat().st_size > 0
    assert (debug_dir / "height.png").exists()
    assert (debug_dir / "labels.png").exists()
    assert (debug_dir / "palette_suggested.json").exists()
    assert (debug_dir / "palette_assigned.json").exists()
    assert (debug_dir / "layers_by_label.json").exists()
    assert (debug_dir / "preview.png").exists()
    assert (debug_dir / "height_layers.npy").exists()
    assert (debug_dir / "height_mm.npy").exists()
    colorplan = output_path.with_suffix(".colorplan.txt")
    assert colorplan.exists()
    content = colorplan.read_text(encoding="utf-8")
    assert "START" in content
    assert "CHANGE" in content
