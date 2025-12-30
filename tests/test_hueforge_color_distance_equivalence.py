from hueforge.utils.color_distance import (
    color_distance as new_color_distance,
    lab_distance as new_lab_distance,
    rgb_distance as new_rgb_distance,
    rgb_to_lab as new_rgb_to_lab,
)
from src.color.color_distance import (
    color_distance as legacy_color_distance,
    lab_distance as legacy_lab_distance,
    rgb_distance as legacy_rgb_distance,
    rgb_to_lab as legacy_rgb_to_lab,
)


def test_color_distance_equivalence_rgb() -> None:
    legacy = legacy_rgb_distance((0, 0, 0), (10, 20, 30))
    new = new_rgb_distance((0, 0, 0), (10, 20, 30))
    assert legacy == new


def test_color_distance_equivalence_lab() -> None:
    legacy = legacy_lab_distance((1.0, 2.0, 3.0), (2.0, 4.0, 6.0))
    new = new_lab_distance((1.0, 2.0, 3.0), (2.0, 4.0, 6.0))
    assert legacy == new


def test_color_distance_equivalence_rgb_to_lab() -> None:
    legacy = legacy_rgb_to_lab((255, 0, 0))
    new = new_rgb_to_lab((255, 0, 0))
    assert legacy == new


def test_color_distance_equivalence_color_distance() -> None:
    a = {"rgb": [10, 10, 10], "lab": [1.0, 2.0, 3.0]}
    b = {"rgb": [11, 11, 11], "lab": [2.0, 3.0, 4.0]}
    c = {"rgb": [10, 10, 10]}

    assert legacy_color_distance(a, b) == new_color_distance(a, b)
    assert legacy_color_distance(a, c) == new_color_distance(a, c)
    assert legacy_color_distance(c, b) == new_color_distance(c, b)
