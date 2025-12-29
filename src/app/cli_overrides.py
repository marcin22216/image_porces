from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


def parse_id_list(text: Optional[str]) -> Optional[List[str]]:
    if not text:
        return None
    items = [item.strip() for item in text.split(",") if item.strip()]
    return items or None


def build_overrides(args: Any) -> Dict[str, Any]:
    overrides: Dict[str, Any] = {}
    if args.catalog:
        overrides.setdefault("print", {})["filament_catalog"] = args.catalog
    if args.n_colors is not None:
        overrides.setdefault("palette", {})["n_colors"] = int(args.n_colors)
    if args.base_filament_id:
        overrides.setdefault("print", {})["base_filament_id"] = args.base_filament_id
    if args.sequence_mode:
        overrides.setdefault("print", {})["sequence_mode"] = args.sequence_mode
    if args.layer_sequence_ids is not None:
        overrides.setdefault("print", {})["layer_sequence_ids"] = parse_id_list(
            args.layer_sequence_ids
        )
    if args.blend_depth is not None:
        overrides.setdefault("print", {})["blend_depth"] = float(args.blend_depth)
    if args.width_mm is not None or args.height_mm is not None:
        canvas = overrides.setdefault("canvas", {})
        if args.width_mm is not None:
            canvas["target_width_mm"] = float(args.width_mm)
        if args.height_mm is not None:
            canvas["target_height_mm"] = float(args.height_mm)
    return overrides


def validate_overrides(overrides: Dict[str, Any]) -> None:
    print_cfg = overrides.get("print", {})
    if print_cfg.get("sequence_mode") == "manual":
        ids = print_cfg.get("layer_sequence_ids")
        if not ids:
            raise ValueError("manual sequence_mode requires --layer-sequence-ids")


def load_preset(path: Optional[str]) -> Dict[str, Any]:
    if path is None:
        path = str(Path("presets") / "default.json")
    return json.loads(Path(path).read_text(encoding="utf-8"))


def apply_overrides(preset: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    merged = json.loads(json.dumps(preset))
    _deep_update(merged, overrides)
    if "palette" in overrides and "n_colors" in overrides["palette"]:
        merged.get("palette", {}).pop("colors", None)
    return merged


def _deep_update(target: Dict[str, Any], updates: Dict[str, Any]) -> None:
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _deep_update(target[key], value)
        else:
            target[key] = value
