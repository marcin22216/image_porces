from __future__ import annotations

from typing import List, Tuple

import numpy as np


def suggest_palette(image: np.ndarray, n_colors: int = 4) -> List[Tuple[int, int, int]]:
    _validate_image(image)
    if n_colors < 2:
        raise ValueError("n_colors must be >= 2")

    pixels = image.reshape(-1, 3).astype(np.float32)
    unique = np.unique(pixels.astype(np.uint8), axis=0)
    if unique.shape[0] <= n_colors:
        palette = [tuple(map(int, rgb)) for rgb in unique]
        while len(palette) < n_colors:
            palette.append(palette[-1])
        return palette[:n_colors]

    rng = np.random.default_rng(0)
    centers = unique[rng.choice(unique.shape[0], size=n_colors, replace=False)].astype(
        np.float32
    )

    for _ in range(10):
        distances = np.sum((pixels[:, None, :] - centers[None, :, :]) ** 2, axis=2)
        labels = np.argmin(distances, axis=1)
        new_centers = np.zeros_like(centers)
        for idx in range(n_colors):
            mask = labels == idx
            if not np.any(mask):
                new_centers[idx] = centers[idx]
            else:
                new_centers[idx] = pixels[mask].mean(axis=0)
        if np.allclose(new_centers, centers):
            break
        centers = new_centers

    centers = np.clip(np.rint(centers), 0, 255).astype(np.uint8)
    return [tuple(map(int, rgb)) for rgb in centers]


def _validate_image(image: np.ndarray) -> None:
    if image.dtype != np.uint8:
        raise TypeError("image must be uint8")
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("image must have shape (H, W, 3)")
