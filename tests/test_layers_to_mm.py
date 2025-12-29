import numpy as np

from ops.layers_to_mm import layers_to_mm


def test_layers_to_mm_base_only():
    layers = np.zeros((2, 2), dtype=np.int32)
    heights = layers_to_mm(layers, base_layer_mm=0.2, color_layer_mm=0.1)

    assert heights.dtype == np.float32
    assert np.allclose(heights, 0.2)


def test_layers_to_mm_scale():
    layers = np.array([[3]], dtype=np.int32)
    heights = layers_to_mm(layers, base_layer_mm=0.16, color_layer_mm=0.08)

    assert np.isclose(float(heights[0, 0]), 0.40)
