from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_catalog(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if "filaments" not in data and "swatches" in data:
        data = {"filaments": [_normalize_swatch(item) for item in data["swatches"]]}
    _validate_catalog(data)
    return data


def _validate_catalog(data: Dict[str, Any]) -> None:
    filaments = data.get("filaments")
    if not isinstance(filaments, list) or not filaments:
        raise ValueError("catalog must include non-empty filaments list")
    for filament in filaments:
        if not isinstance(filament, dict):
            raise ValueError("filament entries must be objects")
        for key in ("id", "name", "rgb", "td_mm"):
            if key not in filament:
                raise ValueError(f"filament missing {key}")
        rgb = filament["rgb"]
        if not (
            isinstance(rgb, list)
            and len(rgb) == 3
            and all(isinstance(v, int) and 0 <= v <= 255 for v in rgb)
        ):
            raise ValueError("filament rgb must be list of 3 ints in [0, 255]")
        td_mm = filament["td_mm"]
        if td_mm is None:
            continue
        if not isinstance(td_mm, (int, float)) or td_mm <= 0:
            raise ValueError("filament td_mm must be > 0 or None")


def _normalize_swatch(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": item.get("filament_id") or item.get("id"),
        "name": item.get("color_name") or item.get("name"),
        "rgb": item.get("rgb"),
        "td_mm": item.get("td"),
    }
