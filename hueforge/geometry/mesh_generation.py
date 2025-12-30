from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np


@dataclass(frozen=True)
class Mesh:
    vertices: np.ndarray
    faces: np.ndarray


def height_map_to_mesh(height_map: np.ndarray, mm_per_pixel: float) -> Mesh:
    _validate_height_map(height_map)
    if mm_per_pixel <= 0:
        raise ValueError("mm_per_pixel must be > 0")

    heights = height_map.astype(np.float32, copy=False)
    height, width = heights.shape

    vertices: List[Tuple[float, float, float]] = []
    faces: List[Tuple[int, int, int]] = []

    def add_quad(v0, v1, v2, v3) -> None:
        index = len(vertices)
        vertices.extend([v0, v1, v2, v3])
        faces.extend([(index, index + 1, index + 2), (index, index + 2, index + 3)])

    for y in range(height):
        for x in range(width):
            x0 = float(x) * mm_per_pixel
            x1 = float(x + 1) * mm_per_pixel
            y0 = float(y) * mm_per_pixel
            y1 = float(y + 1) * mm_per_pixel
            z = float(heights[y, x])
            add_quad(
                (x0, y0, z),
                (x1, y0, z),
                (x1, y1, z),
                (x0, y1, z),
            )

            if x + 1 < width:
                z2 = float(heights[y, x + 1])
                if z2 != z:
                    z_hi, z_lo = (z, z2) if z > z2 else (z2, z)
                    add_quad(
                        (x1, y0, z_hi),
                        (x1, y1, z_hi),
                        (x1, y1, z_lo),
                        (x1, y0, z_lo),
                    )
            else:
                add_quad(
                    (x1, y0, z),
                    (x1, y1, z),
                    (x1, y1, 0.0),
                    (x1, y0, 0.0),
                )

            if y + 1 < height:
                z2 = float(heights[y + 1, x])
                if z2 != z:
                    z_hi, z_lo = (z, z2) if z > z2 else (z2, z)
                    add_quad(
                        (x0, y1, z_hi),
                        (x1, y1, z_hi),
                        (x1, y1, z_lo),
                        (x0, y1, z_lo),
                    )
            else:
                add_quad(
                    (x0, y1, z),
                    (x1, y1, z),
                    (x1, y1, 0.0),
                    (x0, y1, 0.0),
                )

            if x == 0:
                add_quad(
                    (x0, y0, z),
                    (x0, y1, z),
                    (x0, y1, 0.0),
                    (x0, y0, 0.0),
                )
            if y == 0:
                add_quad(
                    (x0, y0, z),
                    (x1, y0, z),
                    (x1, y0, 0.0),
                    (x0, y0, 0.0),
                )

    add_quad(
        (0.0, 0.0, 0.0),
        (float(width) * mm_per_pixel, 0.0, 0.0),
        (float(width) * mm_per_pixel, float(height) * mm_per_pixel, 0.0),
        (0.0, float(height) * mm_per_pixel, 0.0),
    )

    return Mesh(
        vertices=np.asarray(vertices, dtype=np.float32),
        faces=np.asarray(faces, dtype=np.int32),
    )


def _validate_height_map(height_map: np.ndarray) -> None:
    if height_map.dtype != np.float32:
        raise TypeError("height_map must be float32")
    if height_map.ndim != 2:
        raise ValueError("height_map must have shape (H, W)")
    if not np.isfinite(height_map).all():
        raise ValueError("height_map must be finite")
    if np.any(height_map < 0):
        raise ValueError("height_map must be >= 0")
