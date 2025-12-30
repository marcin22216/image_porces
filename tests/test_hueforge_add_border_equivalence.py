import numpy as np

from hueforge.geometry.add_border import add_border as new_add_border
from src.ops.add_border import add_border as legacy_add_border


def test_add_border_zero_equivalence() -> None:
    height = np.array(
        [
            [0.32, 0.40],
            [0.48, 0.56],
        ],
        dtype=np.float32,
    )

    legacy = legacy_add_border(height, border_mm=0.0, mm_per_pixel=0.4, base_height_mm=0.32)
    new = new_add_border(height, border_mm=0.0, mm_per_pixel=0.4, base_height_mm=0.32)

    assert legacy.dtype == np.float32
    assert new.dtype == np.float32
    assert legacy.shape == height.shape
    assert new.shape == height.shape
    np.testing.assert_array_equal(legacy, new)


def test_add_border_px_equivalence() -> None:
    height = np.array(
        [
            [0.32, 0.40],
            [0.48, 0.56],
        ],
        dtype=np.float32,
    )

    legacy = legacy_add_border(height, border_mm=0.4, mm_per_pixel=0.4, base_height_mm=0.32)
    new = new_add_border(height, border_mm=0.4, mm_per_pixel=0.4, base_height_mm=0.32)

    assert legacy.dtype == np.float32
    assert new.dtype == np.float32
    assert legacy.shape == (4, 4)
    assert new.shape == (4, 4)
    np.testing.assert_array_equal(legacy, new)
