from __future__ import annotations

import json
import tempfile
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.app.cli_overrides import apply_overrides, load_preset
from src.app.pipeline import run_pipeline


def run_bundle(
    input_path: str,
    output_zip: str,
    *,
    debug_dir: Optional[str] = None,
    preset_path: Optional[str] = None,
    allowed_filaments: Optional[List[str]] = None,
    overrides: Optional[Dict[str, Any]] = None,
) -> List[str]:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        base_name = Path(output_zip).name
        if base_name.endswith(".zip"):
            base_name = base_name[:-4]
        output_stl = temp_path / f"{base_name}.stl"
        debug_path = temp_path / "debug"
        debug_path.mkdir(parents=True, exist_ok=True)

        run_pipeline(
            input_path,
            str(output_stl),
            debug_dir=str(debug_path),
            preset_path=preset_path,
            allowed_filaments=allowed_filaments,
            overrides=overrides,
        )

        effective = apply_overrides(load_preset(preset_path), overrides or {})
        config_path = temp_path / "config.effective.json"
        config_path.write_text(json.dumps(effective, indent=2), encoding="utf-8")

        required = [
            output_stl,
            output_stl.with_suffix(".colorplan.txt"),
            debug_path / "preview.png",
            debug_path / "palette_suggested.json",
            debug_path / "palette_assigned.json",
            debug_path / "layer_plan.json",
            config_path,
        ]

        output_path = Path(output_zip)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for item in required:
                archive.write(item, arcname=item.name)

        return [item.name for item in required]
