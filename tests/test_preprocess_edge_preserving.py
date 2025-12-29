import numpy as np

from ops.preprocess_edge_preserving import process


def test_bilateral_preserves_edge():
    image = np.zeros((5, 5, 3), dtype=np.uint8)
    image[:, 3:, :] = 255

    result = process(
        image,
        mode="bilateral",
        radius=1,
        sigma_space=1.0,
        sigma_color=10.0,
    )

    assert result.shape == image.shape
    assert result.dtype == np.uint8
    assert result[2, 1, 0] <= 5
    assert result[2, 4, 0] >= 250
    assert int(result[2, 2, 0]) - int(result[2, 3, 0]) <= -200
