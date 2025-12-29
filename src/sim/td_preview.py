from __future__ import annotations

import math
from typing import Dict, Iterable, List, Tuple


def srgb_to_linear(rgb_u8: Tuple[int, int, int]) -> Tuple[float, float, float]:
    return tuple(_srgb_channel_to_linear(c) for c in rgb_u8)


def linear_to_srgb(rgb_f: Tuple[float, float, float]) -> Tuple[int, int, int]:
    return tuple(_linear_channel_to_srgb(c) for c in rgb_f)


def simulate_stack(
    base_rgb: Tuple[int, int, int],
    layers: List[Tuple[str, int]],
    catalog: Dict[str, object],
    color_layer_mm: float,
) -> Tuple[int, int, int]:
    if color_layer_mm <= 0:
        raise ValueError("color_layer_mm must be > 0")

    current = srgb_to_linear(base_rgb)
    filament_map = _catalog_to_map(catalog)
    for filament_id, count in layers:
        if count <= 0:
            continue
        filament = filament_map[filament_id]
        layer_color = srgb_to_linear(tuple(filament["rgb"]))
        td_value = filament.get("td_mm")
        if td_value is None:
            td_value = 1.0
        td_mm = float(td_value)
        if td_mm <= 0:
            raise ValueError("td_mm must be > 0")
        thickness = color_layer_mm * count
        transmission = math.exp(-thickness / td_mm)
        current = tuple(
            transmission * c + (1.0 - transmission) * lc
            for c, lc in zip(current, layer_color)
        )
    return linear_to_srgb(current)


def _catalog_to_map(catalog: Dict[str, object]) -> Dict[str, Dict[str, object]]:
    filaments = catalog.get("filaments", [])
    return {f["id"]: f for f in filaments}


def _srgb_channel_to_linear(value: int) -> float:
    srgb = max(0.0, min(1.0, value / 255.0))
    if srgb <= 0.04045:
        return srgb / 12.92
    return ((srgb + 0.055) / 1.055) ** 2.4


def _linear_channel_to_srgb(value: float) -> int:
    linear = max(0.0, min(1.0, value))
    if linear <= 0.0031308:
        srgb = linear * 12.92
    else:
        srgb = 1.055 * (linear ** (1.0 / 2.4)) - 0.055
    return int(round(srgb * 255.0))
