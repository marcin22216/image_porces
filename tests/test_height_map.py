import numpy as np

from ops.height_map import generate_height_map
from ops.layers_to_mm import layers_to_mm


def test_height_map_by_index_contract_and_constancy():
    labels = np.array(
        [
            [0, 0, 1],
            [0, 2, 2],
        ],
        dtype=np.int32,
    )

    heights = generate_height_map(labels, mode="by_index", scale=1.0)

    assert heights.shape == labels.shape
    assert heights.dtype == np.int32
    assert np.isfinite(heights).all()
    assert np.all(heights >= 0)
    assert float(heights[0, 0]) == float(heights[0, 1])
    assert float(heights[1, 1]) == float(heights[1, 2])


def test_height_map_by_table_contract_and_constancy():
    labels = np.array(
        [
            [1, 1, 2],
            [1, 3, 3],
        ],
        dtype=np.int32,
    )
    table = {1: 1, 2: 3, 3: 2}

    heights = generate_height_map(labels, mode="by_table", table=table)

    assert heights.shape == labels.shape
    assert heights.dtype == np.int32
    assert np.isfinite(heights).all()
    assert np.all(heights >= 0)
    assert float(heights[0, 0]) == float(heights[0, 1])
    assert float(heights[1, 1]) == float(heights[1, 2])


def test_blend_depth_scales_layers_to_mm():
    labels = np.array([[1, 2]], dtype=np.int32)
    layers = generate_height_map(labels, mode="by_index", scale=1.0)
    blended = np.rint(layers.astype(np.float32) * 2.0).astype(np.int32)
    heights = layers_to_mm(blended, base_layer_mm=0.16, color_layer_mm=0.08)

    assert heights.dtype == np.float32
    assert np.isclose(float(heights[0, 0]), 0.32)
    assert np.isclose(float(heights[0, 1]), 0.48)
