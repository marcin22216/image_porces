from src.color.color_distance import color_distance, lab_distance, rgb_distance, rgb_to_lab


def test_lab_distance_and_fallback():
    a = {"rgb": [10, 10, 10], "lab": [10.0, 0.0, 0.0]}
    b = {"rgb": [250, 250, 250], "lab": [20.0, 0.0, 0.0]}
    c = {"rgb": [12, 10, 10]}
    d = {"rgb": [10, 10, 10]}

    assert lab_distance((10.0, 0.0, 0.0), (20.0, 0.0, 0.0)) == 100.0
    assert rgb_distance((10, 10, 10), (12, 10, 10)) == 4.0
    assert color_distance(a, b) == 100.0
    assert color_distance(d, c) == 4.0


def test_rgb_to_lab_round_trip_basics():
    lab = rgb_to_lab((128, 128, 128))
    assert isinstance(lab[0], float)


def test_nearest_prefers_lab_when_available():
    target = {"rgb": [128, 128, 128], "lab": [50.0, 0.0, 0.0]}
    filament_a = {"id": "a", "rgb": [0, 0, 0], "lab": [49.0, 0.0, 0.0]}
    filament_b = {"id": "b", "rgb": [129, 129, 129], "lab": [90.0, 0.0, 0.0]}

    assert color_distance(target, filament_a) < color_distance(target, filament_b)
