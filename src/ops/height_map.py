from __future__ import annotations

from typing import Dict

import numpy as np


def generate_height_map(labels: np.ndarray, **params) -> np.ndarray:
    _validate_labels(labels)

    mode = params.get("mode", "by_index")
    if mode == "by_index":
        scale = float(params.get("scale", 1.0))
        if scale < 0:
            raise ValueError("scale must be >= 0")
        return _layers_by_index(labels, scale)
    if mode == "by_table":
        table = params.get("table")
        if table is None:
            raise ValueError("table is required for by_table mode")
        return _layers_by_table(labels, table)
    raise ValueError(f"unsupported mode: {mode}")


def _validate_labels(labels: np.ndarray) -> None:
    if labels.dtype != np.int32:
        raise TypeError("labels must be int32")
    if labels.ndim != 2:
        raise ValueError("labels must have shape (H, W)")


def _layers_by_index(labels: np.ndarray, scale: float) -> np.ndarray:
    unique_labels = np.unique(labels)
    layers = np.zeros(labels.shape, dtype=np.int32)
    if unique_labels.size == 0:
        return layers

    if 0 in unique_labels:
        mapped_labels = unique_labels[unique_labels != 0]
    else:
        mapped_labels = unique_labels

    count = mapped_labels.size
    if count == 0:
        return layers

    max_layers = int(round(7 * float(scale)))
    if max_layers < 1:
        return layers
    if max_layers > 7:
        max_layers = 7

    target_max = min(max_layers, count)
    if count <= target_max:
        for idx, label in enumerate(mapped_labels, start=1):
            layers[labels == label] = idx
    else:
        denom = count - 1
        for idx, label in enumerate(mapped_labels):
            layer = 1 + int(round(idx * (target_max - 1) / denom))
            if layer > target_max:
                layer = target_max
            layers[labels == label] = layer
    return layers


def _layers_by_table(labels: np.ndarray, table: Dict[int, float]) -> np.ndarray:
    height_map = np.zeros(labels.shape, dtype=np.int32)
    for label in np.unique(labels):
        value = float(table.get(int(label), 0.0))
        if value < 0:
            raise ValueError("layer values must be >= 0")
        height_map[labels == label] = int(round(value))
    return height_map
