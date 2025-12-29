import numpy as np

from ops.palette_mapping import map_palette


def test_palette_mapping_contract_and_colors():
    image = np.array(
        [
            [[10, 10, 10], [250, 250, 250]],
            [[30, 30, 30], [220, 220, 220]],
        ],
        dtype=np.uint8,
    )
    palette = np.array([[0, 0, 0], [255, 255, 255]], dtype=np.uint8)

    mapped = map_palette(image, palette)

    assert mapped.shape == image.shape
    assert mapped.dtype == np.uint8
    unique = np.unique(mapped.reshape(-1, 3), axis=0)
    assert unique.shape[0] <= palette.shape[0]
    assert {tuple(c) for c in unique}.issubset({(0, 0, 0), (255, 255, 255)})
