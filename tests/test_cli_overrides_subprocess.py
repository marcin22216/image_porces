import subprocess
import sys
from pathlib import Path

from src.app.image_io import ImageData, save_image


def test_preview_with_overrides_creates_preview(tmp_path):
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
    catalog = repo_root / "data" / "filament_catalog_filamentcolors.json"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "preview",
            "--in",
            str(input_path),
            "--debug",
            str(debug_dir),
            "--n-colors",
            "3",
            "--blend-depth",
            "1.2",
            "--catalog",
            str(catalog),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )

    assert (debug_dir / "preview.png").exists()
    assert "preview.png" in result.stdout


def test_manual_mode_requires_layer_sequence_ids(tmp_path):
    input_path = tmp_path / "input.png"
    debug_dir = tmp_path / "debug"

    pixels = ((10, 10, 10), (20, 20, 20), (230, 230, 230), (240, 240, 240))
    image = ImageData(width=2, height=2, pixels=pixels)
    save_image(image, input_path)

    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "preview",
            "--in",
            str(input_path),
            "--debug",
            str(debug_dir),
            "--sequence-mode",
            "manual",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "layer-sequence-ids" in (result.stderr + result.stdout)


def test_missing_input_error(tmp_path):
    debug_dir = tmp_path / "debug"
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "preview",
            "--in",
            str(tmp_path / "missing.png"),
            "--debug",
            str(debug_dir),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "Input not found" in (result.stderr + result.stdout)


def test_missing_catalog_error(tmp_path):
    input_path = tmp_path / "input.png"
    debug_dir = tmp_path / "debug"
    pixels = ((10, 10, 10), (20, 20, 20), (230, 230, 230), (240, 240, 240))
    image = ImageData(width=2, height=2, pixels=pixels)
    save_image(image, input_path)

    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "preview",
            "--in",
            str(input_path),
            "--debug",
            str(debug_dir),
            "--catalog",
            str(tmp_path / "missing.json"),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "filamentcolors_sync" in (result.stderr + result.stdout)


def test_preview_input_directory_error(tmp_path):
    debug_dir = tmp_path / "debug"
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.main",
            "preview",
            "--in",
            str(tmp_path),
            "--debug",
            str(debug_dir),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "directory" in (result.stderr + result.stdout).lower()
