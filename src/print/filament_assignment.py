from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from src.color.color_distance import color_distance, rgb_to_lab

def nearest_filament(
    rgb: Tuple[int, int, int],
    catalog: Dict[str, object],
    allowed_ids: Optional[List[str]],
) -> str:
    candidates = _filter_filaments(catalog, allowed_ids)
    best_id = None
    best_dist = None
    target = {"rgb": list(rgb), "lab": list(rgb_to_lab(rgb))}
    for filament in candidates:
        dist = color_distance(target, filament)
        if best_dist is None:
            best_dist = dist
            best_id = filament["id"]
            continue
        if dist < best_dist or (
            dist == best_dist and filament["id"] < best_id
        ):
            best_dist = dist
            best_id = filament["id"]
    if best_id is None:
        raise ValueError("no filaments available for assignment")
    return best_id


def assign_palette_to_filaments(
    palette: List[Tuple[int, int, int]],
    catalog: Dict[str, object],
    allowed_ids: Optional[List[str]],
) -> Dict[int, str]:
    mapping: Dict[int, str] = {}
    for index, rgb in enumerate(palette):
        mapping[index] = nearest_filament(rgb, catalog, allowed_ids)
    return mapping


def _filter_filaments(
    catalog: Dict[str, object], allowed_ids: Optional[List[str]]
) -> List[Dict[str, object]]:
    filaments = catalog.get("filaments", [])
    if allowed_ids is None:
        return list(filaments)
    allowed = set(allowed_ids)
    return [filament for filament in filaments if filament["id"] in allowed]
