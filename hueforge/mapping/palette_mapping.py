from __future__ import annotations

import numpy as np


def map_palette(
    image: np.ndarray,
    palette: np.ndarray,
    *,
    method: str = "nearest",
    metric: str = "rgb",
) -> np.ndarray:
    _validate_image(image)
    _validate_palette(palette)

    if method != "nearest":
        raise ValueError(f"unsupported method: {method}")
    if metric != "rgb":
        raise ValueError(f"unsupported metric: {metric}")

    flat = image.reshape(-1, 3).astype(np.int16)
    pal = palette.astype(np.int16)
    diffs = flat[:, None, :] - pal[None, :, :]
    dist = np.sum(diffs * diffs, axis=2)
    indices = np.argmin(dist, axis=1)
    mapped = palette[indices].reshape(image.shape)
    return mapped.astype(np.uint8)


def _validate_image(image: np.ndarray) -> None:
    if image.dtype != np.uint8:
        raise TypeError("image must be uint8")
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("image must have shape (H, W, 3)")


def _validate_palette(palette: np.ndarray) -> None:
    if palette.dtype != np.uint8:
        raise TypeError("palette must be uint8")
    if palette.ndim != 2 or palette.shape[1] != 3:
        raise ValueError("palette must have shape (N, 3)")
    if palette.shape[0] < 1:
        raise ValueError("palette must have at least one color")
