from __future__ import annotations

from typing import List, Optional

from src.app.pipeline import run_pipeline


def run_preview(
    input_path: str,
    *,
    debug_dir: str,
    preset_path: Optional[str] = None,
    allowed_filaments: Optional[List[str]] = None,
    overrides: Optional[dict] = None,
) -> None:
    run_pipeline(
        input_path,
        output_path="",
        debug_dir=debug_dir,
        preset_path=preset_path,
        allowed_filaments=allowed_filaments,
        overrides=overrides,
        mode="preview",
    )
