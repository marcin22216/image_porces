from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from src.color.color_distance import color_distance, rgb_to_lab
from src.tools.filamentcolors_sync import hex_to_rgb

Rgb = Tuple[int, int, int]


def load_filament_catalog(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "filaments" in data:
        return list(data["filaments"])
    if "swatches" in data:
        return [
            {
                "id": item.get("filament_id"),
                "manufacturer": item.get("manufacturer"),
                "name": item.get("color_name"),
                "rgb": item.get("rgb"),
                "td_mm": item.get("td"),
            }
            for item in data["swatches"]
        ]
    return []


def parse_hex_color(text: str) -> Rgb:
    return hex_to_rgb(text)


def filter_filaments(
    filaments: Iterable[Dict[str, Any]],
    *,
    search: Optional[str] = None,
    td_min: Optional[float] = None,
    td_max: Optional[float] = None,
    include_missing_td: bool = False,
) -> List[Dict[str, Any]]:
    result = []
    search_lower = search.lower() if search else None
    for item in filaments:
        name = str(item.get("name") or "")
        manufacturer = str(item.get("manufacturer") or "")
        if search_lower and search_lower not in (name + " " + manufacturer).lower():
            continue
        td = item.get("td_mm")
        if td is None:
            if not include_missing_td and (td_min is not None or td_max is not None):
                continue
        else:
            td_value = float(td)
            if td_min is not None and td_value < td_min:
                continue
            if td_max is not None and td_value > td_max:
                continue
        result.append(item)
    return result


def nearest_filaments(
    filaments: Iterable[Dict[str, Any]],
    target: Rgb,
    top: int,
) -> List[Tuple[Dict[str, Any], float]]:
    scored = []
    target_item = {"rgb": list(target), "lab": list(rgb_to_lab(target))}
    for index, item in enumerate(filaments):
        rgb = item.get("rgb")
        if not rgb:
            continue
        dist = color_distance(target_item, item)
        scored.append((dist, index, item))
    scored.sort(key=lambda item: (item[0], item[1]))
    return [(item, dist) for dist, _, item in scored[:top]]


def apply_limit_offset(
    rows: List[Dict[str, Any]], *, limit: int, offset: int
) -> List[Dict[str, Any]]:
    start = max(0, offset)
    end = start + max(0, limit)
    return rows[start:end]


def format_table(rows: Iterable[Dict[str, Any]]) -> str:
    lines = ["id\tmanufacturer\tname\trgb\ttd_mm"]
    for item in rows:
        rgb = item.get("rgb")
        rgb_text = ",".join(str(v) for v in rgb) if rgb else ""
        td = item.get("td_mm")
        td_text = "" if td is None else str(td)
        lines.append(
            f"{item.get('id')}\t{item.get('manufacturer')}\t{item.get('name')}\t{rgb_text}\t{td_text}"
        )
    return "\n".join(lines)


def format_nearest_table(rows: Iterable[Tuple[Dict[str, Any], float]]) -> str:
    lines = ["id\tmanufacturer\tname\trgb\ttd_mm\tdistance"]
    for item, dist in rows:
        rgb = item.get("rgb")
        rgb_text = ",".join(str(v) for v in rgb) if rgb else ""
        td = item.get("td_mm")
        td_text = "" if td is None else str(td)
        lines.append(
            f"{item.get('id')}\t{item.get('manufacturer')}\t{item.get('name')}\t{rgb_text}\t{td_text}\t{dist:.6f}"
        )
    return "\n".join(lines)
