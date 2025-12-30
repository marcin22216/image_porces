from __future__ import annotations

import numpy as np


def layers_to_mm(
    height_layers: np.ndarray, base_layer_mm: float, color_layer_mm: float
) -> np.ndarray:
    _validate_layers(height_layers)
    if base_layer_mm < 0:
        raise ValueError("base_layer_mm must be >= 0")
    if color_layer_mm <= 0:
        raise ValueError("color_layer_mm must be > 0")

    heights = base_layer_mm + height_layers.astype(np.float32) * float(color_layer_mm)
    return heights.astype(np.float32)


def _validate_layers(height_layers: np.ndarray) -> None:
    if height_layers.dtype != np.int32:
        raise TypeError("height_layers must be int32")
    if height_layers.ndim != 2:
        raise ValueError("height_layers must have shape (H, W)")
    if np.any(height_layers < 0):
        raise ValueError("height_layers must be >= 0")
