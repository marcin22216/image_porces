import numpy as np

from hueforge.geometry.height_map import generate_height_map as new_generate_height_map
from src.ops.height_map import generate_height_map as legacy_generate_height_map


def test_height_map_by_index_equivalence() -> None:
    labels = np.array(
        [
            [0, 1, 1],
            [2, 2, 3],
            [3, 3, 3],
        ],
        dtype=np.int32,
    )

    legacy = legacy_generate_height_map(labels, mode="by_index", scale=1.0)
    new = new_generate_height_map(labels, mode="by_index", scale=1.0)

    assert legacy.dtype == np.int32
    assert new.dtype == np.int32
    assert legacy.shape == labels.shape
    assert new.shape == labels.shape
    np.testing.assert_array_equal(legacy, new)


def test_height_map_by_table_equivalence() -> None:
    labels = np.array(
        [
            [0, 1],
            [2, 2],
        ],
        dtype=np.int32,
    )
    table = {0: 0.0, 1: 2.0, 2: 4.0}

    legacy = legacy_generate_height_map(labels, mode="by_table", table=table)
    new = new_generate_height_map(labels, mode="by_table", table=table)

    assert legacy.dtype == np.int32
    assert new.dtype == np.int32
    assert legacy.shape == labels.shape
    assert new.shape == labels.shape
    np.testing.assert_array_equal(legacy, new)
