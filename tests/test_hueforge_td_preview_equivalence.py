import numpy as np

from hueforge.physics.td_preview import simulate_stack as new_simulate_stack
from src.sim.td_preview import simulate_stack as legacy_simulate_stack


def test_td_preview_equivalence() -> None:
    base_rgb = (128, 128, 128)
    layers = [("white", 2), ("cyan", 1)]
    catalog = {
        "filaments": [
            {"id": "white", "rgb": (255, 255, 255), "td_mm": 2.0},
            {"id": "cyan", "rgb": (0, 255, 255), "td_mm": 1.5},
        ]
    }

    legacy = legacy_simulate_stack(base_rgb, layers, catalog, color_layer_mm=0.08)
    new = new_simulate_stack(base_rgb, layers, catalog, color_layer_mm=0.08)

    assert isinstance(legacy, tuple)
    assert isinstance(new, tuple)
    assert len(legacy) == 3
    assert len(new) == 3
    np.testing.assert_array_equal(np.array(legacy, dtype=np.uint8), np.array(new, dtype=np.uint8))
