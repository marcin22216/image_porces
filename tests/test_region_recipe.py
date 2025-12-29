import numpy as np

from src.solver.region_recipe import solve_layers_by_label, solve_layers_for_label


def test_solve_layers_for_label_uses_allowed_filaments():
    catalog = {
        "filaments": [
            {"id": "a", "name": "A", "rgb": [0, 0, 0], "td_mm": 1.0},
            {"id": "b", "name": "B", "rgb": [255, 0, 0], "td_mm": 1.0},
            {"id": "c", "name": "C", "rgb": [0, 255, 0], "td_mm": 1.0},
        ]
    }
    layers = solve_layers_for_label(
        target_rgb=(250, 0, 0),
        filament_ids=["b", "c"],
        catalog=catalog,
        color_layer_mm=0.2,
        max_layers=2,
    )

    assert all(fid in {"b", "c"} for fid, _ in layers)
    assert sum(count for _, count in layers) <= 2


def test_solve_layers_by_label_returns_all_labels():
    labels = np.array([[0, 1], [1, 2]], dtype=np.int32)
    base_rgb_by_label = {0: (10, 10, 10), 1: (200, 0, 0), 2: (0, 200, 0)}
    catalog = {
        "filaments": [
            {"id": "a", "name": "A", "rgb": [0, 0, 0], "td_mm": 1.0},
            {"id": "b", "name": "B", "rgb": [200, 0, 0], "td_mm": 1.0},
            {"id": "c", "name": "C", "rgb": [0, 200, 0], "td_mm": 1.0},
        ]
    }

    result = solve_layers_by_label(
        labels,
        base_rgb_by_label,
        filament_ids=["a", "b", "c"],
        catalog=catalog,
        color_layer_mm=0.2,
        max_layers=3,
    )

    assert set(result.keys()) == {0, 1, 2}
    assert all(sum(count for _, count in layers) <= 3 for layers in result.values())
