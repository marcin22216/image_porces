from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

import numpy as np

Label = int


def merge(
    labels: np.ndarray, image: np.ndarray, **params
) -> np.ndarray:
    min_area = int(params.get("min_area", 20))
    if min_area < 1:
        raise ValueError("min_area must be >= 1")

    _validate_inputs(labels, image)

    current = labels.astype(np.int32, copy=True)
    while True:
        areas, means = _region_stats(current, image)
        small = [label for label, area in areas.items() if area < min_area]
        if not small:
            break
        adjacency = _adjacent_labels(current)
        merged_any = False
        for label in small:
            neighbors = adjacency.get(label, [])
            if not neighbors:
                neighbors = [n for n in areas.keys() if n != label]
            if not neighbors:
                continue
            target = _closest_by_color(label, neighbors, means)
            if target != label:
                current[current == label] = target
                merged_any = True
        if not merged_any:
            break
    return _reindex_labels(current)


def _validate_inputs(labels: np.ndarray, image: np.ndarray) -> None:
    if labels.dtype != np.int32:
        raise TypeError("labels must be int32")
    if labels.ndim != 2:
        raise ValueError("labels must have shape (H, W)")
    if image.dtype != np.uint8:
        raise TypeError("image must be uint8")
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("image must have shape (H, W, 3)")
    if labels.shape != image.shape[:2]:
        raise ValueError("labels and image spatial dimensions must match")


def _region_stats(
    labels: np.ndarray, image: np.ndarray
) -> Tuple[Dict[Label, int], Dict[Label, np.ndarray]]:
    flat_labels = labels.reshape(-1)
    flat_image = image.reshape(-1, 3).astype(np.float32)
    areas: Dict[Label, int] = {}
    sums: Dict[Label, np.ndarray] = {}
    for label, color in zip(flat_labels, flat_image):
        areas[label] = areas.get(label, 0) + 1
        if label not in sums:
            sums[label] = color.copy()
        else:
            sums[label] += color
    means = {label: sums[label] / areas[label] for label in areas}
    return areas, means


def _adjacent_labels(labels: np.ndarray) -> Dict[Label, List[Label]]:
    adjacency: Dict[Label, List[Label]] = {}
    height, width = labels.shape
    for y in range(height):
        for x in range(width):
            current = int(labels[y, x])
            neighbors = adjacency.setdefault(current, [])
            if y + 1 < height:
                below = int(labels[y + 1, x])
                if below != current and below not in neighbors:
                    neighbors.append(below)
            if x + 1 < width:
                right = int(labels[y, x + 1])
                if right != current and right not in neighbors:
                    neighbors.append(right)
    return adjacency


def _closest_by_color(
    label: Label, neighbors: Iterable[Label], means: Dict[Label, np.ndarray]
) -> Label:
    base = means[label]
    best = None
    best_dist = float("inf")
    for neighbor in neighbors:
        dist = float(np.sum((means[neighbor] - base) ** 2))
        if dist < best_dist:
            best_dist = dist
            best = neighbor
    return label if best is None else best


def _reindex_labels(labels: np.ndarray) -> np.ndarray:
    unique = np.unique(labels)
    mapping = {old: new for new, old in enumerate(unique)}
    vectorized = np.vectorize(mapping.get, otypes=[np.int32])
    return vectorized(labels).astype(np.int32)
