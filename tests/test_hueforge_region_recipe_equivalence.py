import numpy as np

from hueforge.solver.region_recipe import solve_layers_by_label as new_solver
from src.solver.region_recipe import solve_layers_by_label as legacy_solver


def test_region_recipe_equivalence() -> None:
    labels = np.array([[0, 1], [1, 0]], dtype=np.int32)
    base_rgb_by_label = {
        0: (10, 10, 10),
        1: (200, 0, 0),
    }
    catalog = {
        "filaments": [
            {"id": "a", "name": "A", "rgb": [0, 0, 0], "td_mm": 1.0},
            {"id": "b", "name": "B", "rgb": [255, 0, 0], "td_mm": 1.0},
        ]
    }
    filament_ids = ["a", "b"]

    legacy = legacy_solver(
        labels,
        base_rgb_by_label,
        filament_ids=filament_ids,
        catalog=catalog,
        color_layer_mm=0.2,
        max_layers=2,
    )
    new = new_solver(
        labels,
        base_rgb_by_label,
        filament_ids=filament_ids,
        catalog=catalog,
        color_layer_mm=0.2,
        max_layers=2,
    )

    assert legacy == new
