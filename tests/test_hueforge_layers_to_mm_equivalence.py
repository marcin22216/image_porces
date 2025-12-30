import numpy as np

from hueforge.geometry.layers_to_mm import layers_to_mm as new_layers_to_mm
from src.ops.layers_to_mm import layers_to_mm as legacy_layers_to_mm


def test_layers_to_mm_equivalence() -> None:
    height_layers = np.array(
        [
            [0, 1],
            [2, 3],
        ],
        dtype=np.int32,
    )

    legacy = legacy_layers_to_mm(height_layers, base_layer_mm=0.32, color_layer_mm=0.08)
    new = new_layers_to_mm(height_layers, base_layer_mm=0.32, color_layer_mm=0.08)

    assert legacy.dtype == np.float32
    assert new.dtype == np.float32
    assert legacy.shape == height_layers.shape
    assert new.shape == height_layers.shape
    np.testing.assert_allclose(legacy, new)
