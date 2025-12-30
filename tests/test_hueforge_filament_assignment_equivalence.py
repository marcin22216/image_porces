from hueforge.print.filament_assignment import assign_palette_to_filaments as new_assign
from src.print.filament_assignment import assign_palette_to_filaments as legacy_assign


def test_filament_assignment_equivalence_unrestricted() -> None:
    palette = [
        (10, 10, 10),
        (200, 200, 200),
        (250, 0, 0),
    ]
    catalog = {
        "filaments": [
            {"id": "black", "rgb": [0, 0, 0]},
            {"id": "white", "rgb": [255, 255, 255]},
            {"id": "red", "rgb": [255, 0, 0]},
        ]
    }

    legacy = legacy_assign(palette, catalog, allowed_ids=None)
    new = new_assign(palette, catalog, allowed_ids=None)

    assert legacy == new


def test_filament_assignment_equivalence_allowed() -> None:
    palette = [
        (10, 10, 10),
        (200, 200, 200),
        (250, 0, 0),
    ]
    catalog = {
        "filaments": [
            {"id": "black", "rgb": [0, 0, 0]},
            {"id": "white", "rgb": [255, 255, 255]},
            {"id": "red", "rgb": [255, 0, 0]},
        ]
    }

    legacy = legacy_assign(palette, catalog, allowed_ids=["black", "white"])
    new = new_assign(palette, catalog, allowed_ids=["black", "white"])

    assert legacy == new
