from __future__ import annotations

from typing import Optional, Tuple

import numpy as np
from PIL import Image


def scale_image_to_canvas(
    image: np.ndarray,
    target_width_mm: Optional[float],
    target_height_mm: Optional[float],
) -> Tuple[np.ndarray, float]:
    _validate_image(image)

    if target_width_mm is None and target_height_mm is None:
        raise ValueError("at least one of target_width_mm or target_height_mm must be set")

    height_px, width_px, _ = image.shape

    width_ratio = (
        float(target_width_mm) / width_px if target_width_mm is not None else None
    )
    height_ratio = (
        float(target_height_mm) / height_px if target_height_mm is not None else None
    )

    if width_ratio is not None and width_ratio <= 0:
        raise ValueError("target_width_mm must be > 0")
    if height_ratio is not None and height_ratio <= 0:
        raise ValueError("target_height_mm must be > 0")

    if width_ratio is not None and height_ratio is not None:
        mm_per_pixel = min(width_ratio, height_ratio)
    else:
        mm_per_pixel = width_ratio if width_ratio is not None else height_ratio

    scaled = image
    if width_ratio is not None and height_ratio is not None:
        target_width_px = int(round(float(target_width_mm) / mm_per_pixel))
        target_height_px = int(round(float(target_height_mm) / mm_per_pixel))
        scale_factor = min(target_width_px / width_px, target_height_px / height_px)
        new_width = max(1, int(round(width_px * scale_factor)))
        new_height = max(1, int(round(height_px * scale_factor)))
        if new_width != width_px or new_height != height_px:
            scaled = _resize_image(image, new_width, new_height)

    return scaled.astype(np.uint8, copy=False), float(mm_per_pixel)


def _validate_image(image: np.ndarray) -> None:
    if image.dtype != np.uint8:
        raise TypeError("image must be uint8")
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("image must have shape (H, W, 3)")


def _resize_image(image: np.ndarray, width: int, height: int) -> np.ndarray:
    resized = Image.fromarray(image).resize((width, height), resample=Image.BILINEAR)
    return np.asarray(resized, dtype=np.uint8)
