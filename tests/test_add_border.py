import numpy as np

from ops.add_border import add_border


def test_add_border_expands_and_fills():
    height = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)

    result = add_border(height, border_mm=1.0, mm_per_pixel=0.5, base_height_mm=0.2)

    assert result.shape == (6, 6)
    assert result.dtype == height.dtype
    assert np.all(result[:2, :] == 0.2)
    assert np.all(result[-2:, :] == 0.2)
    assert np.all(result[:, :2] == 0.2)
    assert np.all(result[:, -2:] == 0.2)
    assert np.array_equal(result[2:4, 2:4], height)
