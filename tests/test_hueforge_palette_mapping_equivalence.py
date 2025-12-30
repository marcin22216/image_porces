import numpy as np

from hueforge.mapping.palette_mapping import map_palette as new_map_palette
from src.ops.palette_mapping import map_palette as legacy_map_palette


def test_palette_mapping_equivalence() -> None:
    image = np.array(
        [
            [[0, 0, 0], [10, 20, 30], [250, 250, 250]],
            [[5, 10, 15], [128, 128, 128], [255, 0, 0]],
        ],
        dtype=np.uint8,
    )
    palette = np.array(
        [
            [0, 0, 0],
            [128, 128, 128],
            [255, 255, 255],
        ],
        dtype=np.uint8,
    )

    legacy = legacy_map_palette(image, palette)
    new = new_map_palette(image, palette)

    assert legacy.dtype == np.uint8
    assert new.dtype == np.uint8
    assert legacy.shape == image.shape
    assert new.shape == image.shape
    np.testing.assert_array_equal(legacy, new)
