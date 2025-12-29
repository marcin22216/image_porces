from __future__ import annotations

from typing import List, Tuple

import numpy as np


def segment(
    image: np.ndarray,
    *,
    n_segments: int = 100,
    compactness: float = 10.0,
    max_iter: int = 5,
    method: str = "slic",
) -> np.ndarray:
    _validate_image(image)

    if n_segments < 1:
        raise ValueError("n_segments must be >= 1")
    if compactness <= 0:
        raise ValueError("compactness must be > 0")
    if max_iter < 1:
        raise ValueError("max_iter must be >= 1")
    if method != "slic":
        raise ValueError(f"unsupported method: {method}")

    return _slic_segment(image, n_segments, compactness, max_iter)


def _validate_image(image: np.ndarray) -> None:
    if image.dtype != np.uint8:
        raise TypeError("image must be uint8")
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("image must have shape (H, W, 3)")


def _slic_segment(
    image: np.ndarray, n_segments: int, compactness: float, max_iter: int
) -> np.ndarray:
    height, width, _ = image.shape
    step = max(1, int(np.sqrt((height * width) / float(n_segments))))
    centers = _init_centers(image, step)
    labels = np.full((height, width), -1, dtype=np.int32)
    distances = np.full((height, width), np.inf, dtype=np.float32)

    compactness_scale = (compactness / float(step)) ** 2

    for _ in range(max_iter):
        distances.fill(np.inf)
        for idx, center in enumerate(centers):
            cy, cx, color = center
            y0 = max(0, cy - 2 * step)
            y1 = min(height, cy + 2 * step + 1)
            x0 = max(0, cx - 2 * step)
            x1 = min(width, cx + 2 * step + 1)
            region = image[y0:y1, x0:x1].astype(np.float32)
            dy = np.arange(y0, y1, dtype=np.float32)[:, None] - float(cy)
            dx = np.arange(x0, x1, dtype=np.float32)[None, :] - float(cx)
            spatial_dist = dy * dy + dx * dx
            color_diff = region - color
            color_dist = np.sum(color_diff * color_diff, axis=2)
            dist = color_dist + compactness_scale * spatial_dist

            current = distances[y0:y1, x0:x1]
            mask = dist < current
            current[mask] = dist[mask]
            labels[y0:y1, x0:x1][mask] = idx

        centers = _recompute_centers(image, labels, len(centers))

    return labels.astype(np.int32)


def _init_centers(image: np.ndarray, step: int) -> List[Tuple[int, int, np.ndarray]]:
    height, width, _ = image.shape
    centers: List[Tuple[int, int, np.ndarray]] = []
    offset = step // 2
    for y in range(offset, height, step):
        for x in range(offset, width, step):
            centers.append((y, x, image[y, x].astype(np.float32)))
    if not centers:
        centers.append((height // 2, width // 2, image[height // 2, width // 2].astype(np.float32)))
    return centers


def _recompute_centers(
    image: np.ndarray, labels: np.ndarray, n_centers: int
) -> List[Tuple[int, int, np.ndarray]]:
    centers: List[Tuple[int, int, np.ndarray]] = []
    for idx in range(n_centers):
        mask = labels == idx
        if not np.any(mask):
            continue
        ys, xs = np.nonzero(mask)
        cy = int(np.mean(ys))
        cx = int(np.mean(xs))
        color = image[ys, xs].mean(axis=0).astype(np.float32)
        centers.append((cy, cx, color))
    return centers
