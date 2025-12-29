from src.sim.td_preview import simulate_stack


def test_td_small_pushes_to_top_layer():
    catalog = {
        "filaments": [
            {"id": "base", "name": "Base", "rgb": [0, 0, 0], "td_mm": 1.0},
            {"id": "top", "name": "Top", "rgb": [255, 0, 0], "td_mm": 0.01},
        ]
    }
    result = simulate_stack(
        base_rgb=(0, 0, 0),
        layers=[("top", 1)],
        catalog=catalog,
        color_layer_mm=0.2,
    )

    assert result[0] >= 250
    assert result[1] <= 5
    assert result[2] <= 5


def test_td_large_keeps_base():
    catalog = {
        "filaments": [
            {"id": "base", "name": "Base", "rgb": [10, 20, 30], "td_mm": 1.0},
            {"id": "top", "name": "Top", "rgb": [200, 50, 50], "td_mm": 1000.0},
        ]
    }
    result = simulate_stack(
        base_rgb=(10, 20, 30),
        layers=[("top", 1)],
        catalog=catalog,
        color_layer_mm=0.2,
    )

    assert abs(result[0] - 10) <= 1
    assert abs(result[1] - 20) <= 1
    assert abs(result[2] - 30) <= 1


def test_zero_layers_returns_base():
    catalog = {
        "filaments": [
            {"id": "base", "name": "Base", "rgb": [10, 20, 30], "td_mm": 1.0}
        ]
    }
    result = simulate_stack(
        base_rgb=(10, 20, 30),
        layers=[("base", 0)],
        catalog=catalog,
        color_layer_mm=0.2,
    )

    assert result == (10, 20, 30)
