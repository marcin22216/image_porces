from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_catalog(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    hueforge_library = _normalize_hueforge_library(data)
    if hueforge_library is not None:
        data = hueforge_library
    elif "filaments" not in data and "swatches" in data:
        data = {"filaments": [_normalize_swatch(item) for item in data["swatches"]]}
    _validate_catalog(data)
    return data


def _normalize_hueforge_library(data: Dict[str, Any]) -> Dict[str, Any] | None:
    if not isinstance(data, dict):
        return None
    if "metadata" not in data:
        return None
    entries = None
    for key in ("filaments", "entries", "records"):
        if key in data:
            entries = data[key]
            break
    if entries is None or not isinstance(entries, list):
        return None
    if not any(
        isinstance(item, dict) and "hexCode" in item and "td" in item
        for item in entries
    ):
        return None
    normalized = _normalize_hueforge_entries(entries)
    return {"filaments": normalized, "metadata": data.get("metadata")}


def _normalize_hueforge_entries(entries: list[object]) -> list[Dict[str, Any]]:
    counts: Dict[str, int] = {}
    normalized: list[Dict[str, Any]] = []
    for item in entries:
        if not isinstance(item, dict):
            raise ValueError("hueforge library entries must be objects")
        manufacturer = _require_text(item, "manufacturer")
        material_type = _require_text(item, "type")
        color = _require_text(item, "color")
        hex_code = _require_text(item, "hexCode")
        td_value = item.get("td")
        if not isinstance(td_value, (int, float)) or td_value <= 0:
            raise ValueError("td must be > 0")
        rgb = _parse_hex_color(hex_code)
        base_id = _build_id([manufacturer, material_type, color])
        count = counts.get(base_id, 0) + 1
        counts[base_id] = count
        filament_id = base_id if count == 1 else f"{base_id}_{count}"
        normalized.append(
            {
                "id": filament_id,
                "name": f"{manufacturer} {material_type} {color}",
                "rgb": rgb,
                "td_mm": td_value,
                "manufacturer": manufacturer,
                "type": material_type,
                "color": color,
                "hexCode": hex_code,
            }
        )
    return normalized


def _require_text(item: Dict[str, Any], key: str) -> str:
    value = item.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be non-empty string")
    return value.strip()


def _parse_hex_color(value: str) -> list[int]:
    if not isinstance(value, str) or len(value) != 7 or value[0] != "#":
        raise ValueError("hexCode must be #RRGGBB")
    try:
        return [
            int(value[1:3], 16),
            int(value[3:5], 16),
            int(value[5:7], 16),
        ]
    except ValueError as exc:
        raise ValueError("hexCode must be #RRGGBB") from exc


def _build_id(parts: list[str]) -> str:
    slugged = [_slugify(part) for part in parts]
    value = "_".join([part for part in slugged if part])
    if not value:
        raise ValueError("id components must be non-empty")
    return value


def _slugify(value: str) -> str:
    output = []
    prev_underscore = False
    for char in value.strip().lower():
        if char.isalnum():
            output.append(char)
            prev_underscore = False
        else:
            if not prev_underscore:
                output.append("_")
                prev_underscore = True
    return "".join(output).strip("_")


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
