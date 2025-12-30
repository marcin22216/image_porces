from __future__ import annotations

import numpy as np


def add_border(
    height: np.ndarray,
    border_mm: float,
    mm_per_pixel: float,
    base_height_mm: float,
) -> np.ndarray:
    _validate_height(height)
    if mm_per_pixel <= 0:
        raise ValueError("mm_per_pixel must be > 0")
    if border_mm < 0:
        raise ValueError("border_mm must be >= 0")
    if base_height_mm < 0:
        raise ValueError("base_height_mm must be >= 0")

    border_px = int(round(border_mm / mm_per_pixel))
    if border_px <= 0:
        return height.copy()

    height_out = np.full(
        (height.shape[0] + 2 * border_px, height.shape[1] + 2 * border_px),
        base_height_mm,
        dtype=height.dtype,
    )
    height_out[border_px:-border_px, border_px:-border_px] = height
    return height_out


def _validate_height(height: np.ndarray) -> None:
    if height.ndim != 2:
        raise ValueError("height must have shape (H, W)")
