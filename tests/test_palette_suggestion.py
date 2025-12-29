import numpy as np

from ops.palette_suggestion import suggest_palette


def test_suggest_palette_returns_n_colors():
    image = np.zeros((4, 4, 3), dtype=np.uint8)
    image[:2, :, :] = [10, 20, 30]
    image[2:, :, :] = [200, 210, 220]

    palette = suggest_palette(image, n_colors=3)

    assert len(palette) == 3
    for color in palette:
        assert all(0 <= channel <= 255 for channel in color)
