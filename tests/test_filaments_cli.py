from src.tools.filaments_cli import (
    filter_filaments,
    nearest_filaments,
    parse_hex_color,
)


def test_parse_hex_color():
    assert parse_hex_color("#00ff10") == (0, 255, 16)


def test_filter_and_nearest():
    catalog = [
        {"id": "a", "manufacturer": "Maker", "name": "Red", "rgb": [250, 0, 0], "td_mm": 1.0},
        {"id": "b", "manufacturer": "Maker", "name": "Green", "rgb": [0, 250, 0], "td_mm": 2.0},
        {"id": "c", "manufacturer": "Other", "name": "Blue", "rgb": [0, 0, 250], "td_mm": None},
    ]
    filtered = filter_filaments(catalog, search="Maker", td_min=1.5)
    assert [item["id"] for item in filtered] == ["b"]

    filtered = filter_filaments(catalog, td_min=1.5, td_max=3.0, include_missing_td=True)
    assert {item["id"] for item in filtered} == {"b", "c"}

    nearest = nearest_filaments(catalog, (240, 0, 0), top=2)
    assert [item["id"] for item, _ in nearest] == ["a", "b"]


def test_nearest_uses_lab_when_available():
    from src.color.color_distance import rgb_to_lab

    target_rgb = (128, 128, 128)
    target_lab = list(rgb_to_lab(target_rgb))
    catalog = [
        {"id": "a", "manufacturer": "M", "name": "LabGood", "rgb": [0, 0, 0], "lab": target_lab},
        {"id": "b", "manufacturer": "M", "name": "RgbCloser", "rgb": [120, 120, 120], "lab": [0.0, 0.0, 0.0]},
    ]
    nearest = nearest_filaments(catalog, target_rgb, top=1)
    assert nearest[0][0]["id"] == "a"
