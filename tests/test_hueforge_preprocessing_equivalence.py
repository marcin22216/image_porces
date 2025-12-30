import numpy as np

from hueforge.preprocessing.merge_small_regions import merge as new_merge
from hueforge.preprocessing.preprocess_edge_preserving import process as new_process
from hueforge.preprocessing.scale import scale_image_to_canvas as new_scale
from hueforge.preprocessing.segment_superpixels import segment as new_segment
from src.ops.merge_small_regions import merge as legacy_merge
from src.ops.preprocess_edge_preserving import process as legacy_process
from src.ops.scale_to_canvas import scale_image_to_canvas as legacy_scale
from src.ops.segment_superpixels import segment as legacy_segment


def test_scale_equivalence() -> None:
    image = np.array(
        [
            [[0, 0, 0], [10, 20, 30]],
            [[40, 50, 60], [70, 80, 90]],
        ],
        dtype=np.uint8,
    )

    legacy_scaled, legacy_mm = legacy_scale(image, 20.0, None)
    new_scaled, new_mm = new_scale(image, 20.0, None)

    assert legacy_mm == new_mm
    np.testing.assert_array_equal(legacy_scaled, new_scaled)


def test_preprocess_equivalence() -> None:
    image = np.array(
        [
            [[10, 20, 30], [40, 50, 60]],
            [[70, 80, 90], [100, 110, 120]],
        ],
        dtype=np.uint8,
    )

    legacy = legacy_process(image, radius=1, sigma_space=1.0, sigma_color=10.0)
    new = new_process(image, radius=1, sigma_space=1.0, sigma_color=10.0)

    np.testing.assert_array_equal(legacy, new)


def test_segment_equivalence() -> None:
    image = np.array(
        [
            [[0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255]],
            [[0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255]],
            [[10, 10, 10], [10, 10, 10], [200, 200, 200], [200, 200, 200]],
            [[10, 10, 10], [10, 10, 10], [200, 200, 200], [200, 200, 200]],
        ],
        dtype=np.uint8,
    )

    legacy = legacy_segment(image, n_segments=2, compactness=1.0, max_iter=1)
    new = new_segment(image, n_segments=2, compactness=1.0, max_iter=1)

    np.testing.assert_array_equal(legacy, new)


def test_merge_equivalence() -> None:
    labels = np.array(
        [
            [0, 0, 1],
            [0, 2, 2],
            [3, 3, 2],
        ],
        dtype=np.int32,
    )
    image = np.array(
        [
            [[0, 0, 0], [0, 0, 0], [255, 255, 255]],
            [[0, 0, 0], [128, 128, 128], [255, 255, 255]],
            [[10, 10, 10], [10, 10, 10], [255, 255, 255]],
        ],
        dtype=np.uint8,
    )

    legacy = legacy_merge(labels, image, min_area=2)
    new = new_merge(labels, image, min_area=2)

    np.testing.assert_array_equal(legacy, new)
