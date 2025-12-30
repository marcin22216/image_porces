from __future__ import annotations

import math
from typing import Dict, Iterable, List, Tuple

import numpy as np

from hueforge.physics.td_preview import linear_to_srgb, srgb_to_linear
from hueforge.utils.color_distance import rgb_to_lab

Rgb = Tuple[int, int, int]


def build_height_map(
    image_rgb: np.ndarray,
    *,
    stack_filament_ids: List[str],
    stack_thresholds_mm: List[float],
    max_thickness_mm: float,
    step_mm: float,
    catalog: Dict[str, object],
    metric: str,
    color_space: str,
) -> np.ndarray:
    _validate_image(image_rgb)
    _validate_stack(stack_filament_ids, stack_thresholds_mm, max_thickness_mm)
    if step_mm <= 0:
        raise ValueError("optical step_mm must be > 0")
    if metric not in {"lab", "rgb"}:
        raise ValueError("optical metric must be 'lab' or 'rgb'")
    if color_space not in {"srgb", "linear_srgb"}:
        raise ValueError("optical color_space must be 'srgb' or 'linear_srgb'")

    height, width, _ = image_rgb.shape
    height_map = np.zeros((height, width), dtype=np.float32)
    for y in range(height):
        for x in range(width):
            target = tuple(int(v) for v in image_rgb[y, x])
            depth = solve_depth_for_pixel(
                target,
                stack_filament_ids,
                stack_thresholds_mm,
                max_thickness_mm=max_thickness_mm,
                step_mm=step_mm,
                catalog=catalog,
                metric=metric,
                color_space=color_space,
            )
            height_map[y, x] = depth
    return height_map


def solve_depth_for_pixel(
    target_rgb: Rgb,
    stack_filament_ids: List[str],
    stack_thresholds_mm: List[float],
    *,
    max_thickness_mm: float,
    step_mm: float,
    catalog: Dict[str, object],
    metric: str,
    color_space: str,
) -> float:
    best_depth = 0.0
    best_error = None
    for depth in _depth_samples(max_thickness_mm, step_mm):
        simulated = simulate_stack_color(
            depth,
            stack_filament_ids,
            stack_thresholds_mm,
            catalog=catalog,
            color_space=color_space,
        )
        error = _color_error(target_rgb, simulated, metric)
        if best_error is None or error < best_error:
            best_error = error
            best_depth = depth
    return float(best_depth)


def simulate_stack_color(
    depth_mm: float,
    stack_filament_ids: List[str],
    stack_thresholds_mm: List[float],
    *,
    catalog: Dict[str, object],
    color_space: str,
    light_profile: Tuple[float, float, float] = (1.0, 1.0, 1.0),
) -> Rgb:
    if depth_mm < 0:
        raise ValueError("depth_mm must be >= 0")
    if color_space not in {"srgb", "linear_srgb"}:
        raise ValueError("optical color_space must be 'srgb' or 'linear_srgb'")
    filament_map = _catalog_to_map(catalog)
    thicknesses = _depth_to_thicknesses(depth_mm, stack_thresholds_mm)
    current = light_profile
    for filament_id, thickness in zip(stack_filament_ids, thicknesses):
        if thickness <= 0:
            continue
        filament = filament_map[filament_id]
        layer_rgb = tuple(int(v) for v in filament["rgb"])
        if color_space == "linear_srgb":
            layer_color = srgb_to_linear(layer_rgb)
        else:
            layer_color = tuple(v / 255.0 for v in layer_rgb)
        td_value = filament.get("td_mm")
        if td_value is None:
            raise ValueError("td_mm is required for optical solver")
        td_mm = float(td_value)
        if td_mm <= 0:
            raise ValueError("td_mm must be > 0")
        transmission = math.exp(-thickness / td_mm)
        current = tuple(
            transmission * c + (1.0 - transmission) * lc
            for c, lc in zip(current, layer_color)
        )
    if color_space == "linear_srgb":
        return linear_to_srgb(current)
    return tuple(int(round(v * 255.0)) for v in current)


def _color_error(a: Rgb, b: Rgb, metric: str) -> float:
    if metric == "lab":
        a_lab = rgb_to_lab(a)
        b_lab = rgb_to_lab(b)
        return float(sum((x - y) ** 2 for x, y in zip(a_lab, b_lab)))
    return float(sum((int(x) - int(y)) ** 2 for x, y in zip(a, b)))


def _depth_samples(max_thickness_mm: float, step_mm: float) -> Iterable[float]:
    if max_thickness_mm < 0:
        raise ValueError("max_thickness_mm must be >= 0")
    steps = int(math.floor(max_thickness_mm / step_mm))
    for idx in range(steps + 1):
        yield idx * step_mm
    if steps * step_mm < max_thickness_mm:
        yield max_thickness_mm


def _depth_to_thicknesses(
    depth_mm: float, thresholds_mm: List[float]
) -> List[float]:
    thicknesses: List[float] = []
    prev = 0.0
    for threshold in thresholds_mm:
        segment = min(depth_mm, threshold) - prev
        if segment < 0:
            segment = 0.0
        thicknesses.append(segment)
        prev = threshold
    return thicknesses


def _validate_image(image_rgb: np.ndarray) -> None:
    if image_rgb.dtype != np.uint8:
        raise TypeError("image_rgb must be uint8")
    if image_rgb.ndim != 3 or image_rgb.shape[2] != 3:
        raise ValueError("image_rgb must have shape (H, W, 3)")


def _validate_stack(
    stack_filament_ids: List[str],
    stack_thresholds_mm: List[float],
    max_thickness_mm: float,
) -> None:
    if not stack_filament_ids:
        raise ValueError("stack_filament_ids must be non-empty")
    if len(stack_filament_ids) != len(stack_thresholds_mm):
        raise ValueError("stack_filament_ids and stack_thresholds_mm must match length")
    if max_thickness_mm <= 0:
        raise ValueError("max_thickness_mm must be > 0")
    if any(threshold <= 0 for threshold in stack_thresholds_mm):
        raise ValueError("stack_thresholds_mm must be > 0")
    if any(
        stack_thresholds_mm[idx] <= stack_thresholds_mm[idx - 1]
        for idx in range(1, len(stack_thresholds_mm))
    ):
        raise ValueError("stack_thresholds_mm must be strictly increasing")
    last = float(stack_thresholds_mm[-1])
    if abs(last - max_thickness_mm) > 1e-6:
        raise ValueError("last stack_thresholds_mm must equal max_thickness_mm")


def _catalog_to_map(catalog: Dict[str, object]) -> Dict[str, Dict[str, object]]:
    filaments = catalog.get("filaments", [])
    return {f["id"]: f for f in filaments}
