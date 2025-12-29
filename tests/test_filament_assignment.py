from src.print.filament_assignment import assign_palette_to_filaments, nearest_filament


def test_nearest_filament_deterministic():
    catalog = {
        "filaments": [
            {"id": "a", "name": "A", "rgb": [0, 0, 0], "td_mm": 1.0},
            {"id": "b", "name": "B", "rgb": [10, 10, 10], "td_mm": 1.0},
            {"id": "c", "name": "C", "rgb": [250, 250, 250], "td_mm": 1.0},
        ]
    }

    assert nearest_filament((9, 9, 9), catalog, None) == "b"


def test_assign_palette_with_allowed_ids():
    catalog = {
        "filaments": [
            {"id": "a", "name": "A", "rgb": [0, 0, 0], "td_mm": 1.0},
            {"id": "b", "name": "B", "rgb": [120, 120, 120], "td_mm": 1.0},
            {"id": "c", "name": "C", "rgb": [250, 250, 250], "td_mm": 1.0},
        ]
    }
    palette = [(5, 5, 5), (200, 200, 200)]

    mapping = assign_palette_to_filaments(palette, catalog, ["b", "c"])

    assert mapping[0] == "b"
    assert mapping[1] == "c"
