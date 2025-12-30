from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

from src.sim.td_preview import simulate_stack

Rgb = Tuple[int, int, int]


def solve_layers_for_label(
    target_rgb: Rgb,
    filament_ids: List[str],
    catalog: Dict[str, object],
    color_layer_mm: float,
    max_layers: int,
) -> List[Tuple[str, int]]:
    if max_layers < 0:
        raise ValueError("max_layers must be >= 0")
    if not filament_ids:
        raise ValueError("filament_ids must be non-empty")

    best_layers: List[Tuple[str, int]] = [(filament_ids[0], 0)]
    best_error = None

    candidates = _generate_candidates(filament_ids, max_layers)
    for layers in candidates:
        result = simulate_stack(target_rgb, layers, catalog, color_layer_mm)
        error = _rgb_error(target_rgb, result)
        if best_error is None or error < best_error:
            best_error = error
            best_layers = layers

    return best_layers


def solve_layers_by_label(
    labels: "np.ndarray",
    base_rgb_by_label: Dict[int, Rgb],
    filament_ids: List[str],
    catalog: Dict[str, object],
    color_layer_mm: float,
    max_layers: int,
) -> Dict[int, List[Tuple[str, int]]]:
    import numpy as np

    if labels.dtype != np.int32 or labels.ndim != 2:
        raise ValueError("labels must be (H, W) int32")
    result: Dict[int, List[Tuple[str, int]]] = {}
    for label in np.unique(labels):
        label_int = int(label)
        target = base_rgb_by_label[label_int]
        result[label_int] = solve_layers_for_label(
            target, filament_ids, catalog, color_layer_mm, max_layers
        )
    return result


def _generate_candidates(
    filament_ids: List[str], max_layers: int
) -> List[List[Tuple[str, int]]]:
    candidates: List[List[Tuple[str, int]]] = []
    for filament_id in filament_ids:
        for count in range(max_layers + 1):
            candidates.append([(filament_id, count)])
    for first in filament_ids:
        for second in filament_ids:
            if first == second:
                continue
            for count_a in range(max_layers + 1):
                for count_b in range(max_layers + 1 - count_a):
                    candidates.append([(first, count_a), (second, count_b)])
    return candidates


def _rgb_error(a: Rgb, b: Rgb) -> int:
    return sum((int(x) - int(y)) ** 2 for x, y in zip(a, b))
