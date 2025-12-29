from __future__ import annotations

from typing import Tuple

import numpy as np


def process(image: np.ndarray, **params) -> np.ndarray:
    mode = params.get("mode", "bilateral")
    if mode != "bilateral":
        raise ValueError(f"unsupported mode: {mode}")

    _validate_image(image)

    sigma_space = float(params.get("sigma_space", 2.0))
    sigma_color = float(params.get("sigma_color", 25.0))
    radius = int(params.get("radius", 2))

    if sigma_space <= 0 or sigma_color <= 0:
        raise ValueError("sigma_space and sigma_color must be positive")
    if radius < 1:
        raise ValueError("radius must be >= 1")

    return _bilateral_filter(image, radius, sigma_space, sigma_color)


def _validate_image(image: np.ndarray) -> None:
    if image.dtype != np.uint8:
        raise TypeError("image must be uint8")
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("image must have shape (H, W, 3)")


def _bilateral_filter(
    image: np.ndarray, radius: int, sigma_space: float, sigma_color: float
) -> np.ndarray:
    height, width, _ = image.shape
    pad = radius
    padded = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode="reflect")
    output = np.zeros_like(image, dtype=np.float32)

    spatial = _spatial_kernel(radius, sigma_space)
    sigma_color_sq = 2.0 * (sigma_color**2)

    for y in range(height):
        for x in range(width):
            center = padded[y + pad, x + pad].astype(np.float32)
            weighted_sum = np.zeros(3, dtype=np.float32)
            weight_total = 0.0
            for dy in range(-radius, radius + 1):
                for dx in range(-radius, radius + 1):
                    neighbor = padded[y + pad + dy, x + pad + dx].astype(np.float32)
                    diff = center - neighbor
                    color_weight = np.exp(-float(np.dot(diff, diff)) / sigma_color_sq)
                    weight = spatial[dy + radius, dx + radius] * color_weight
                    weighted_sum += weight * neighbor
                    weight_total += weight
            output[y, x] = weighted_sum / weight_total

    return np.clip(np.rint(output), 0, 255).astype(np.uint8)


def _spatial_kernel(radius: int, sigma_space: float) -> np.ndarray:
    size = 2 * radius + 1
    coords = np.arange(-radius, radius + 1, dtype=np.float32)
    grid_y, grid_x = np.meshgrid(coords, coords, indexing="ij")
    return np.exp(-((grid_x**2 + grid_y**2) / (2.0 * (sigma_space**2))))
