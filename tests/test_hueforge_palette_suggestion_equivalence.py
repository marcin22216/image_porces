import numpy as np

from hueforge.palette.palette_suggestion import suggest_palette as new_suggest_palette
from src.ops.palette_suggestion import suggest_palette as legacy_suggest_palette


def test_palette_suggestion_equivalence() -> None:
    image = np.array(
        [
            [[0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 0, 0]],
            [[0, 0, 0], [0, 255, 0], [255, 255, 255], [255, 0, 0]],
            [[0, 0, 255], [0, 255, 0], [255, 255, 255], [255, 0, 0]],
            [[0, 0, 255], [0, 255, 0], [255, 255, 255], [255, 0, 0]],
        ],
        dtype=np.uint8,
    )

    legacy = legacy_suggest_palette(image, n_colors=4)
    new = new_suggest_palette(image, n_colors=4)

    assert legacy == new
