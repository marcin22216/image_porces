from pathlib import Path

from hueforge.export.colorplan_export import export_colorplan_txt as new_export
from src.print.colorplan_export import export_colorplan_txt as legacy_export


def test_colorplan_export_equivalence(tmp_path: Path) -> None:
    plan = {
        "total_layers": 3,
        "start": {"layer_index": 0, "z_mm": 0.32, "filament_id": "white"},
        "changes": [{"layer_index": 1, "z_mm": 0.40, "filament_id": "black"}],
    }
    catalog = {
        "filaments": [
            {"id": "white", "name": "White", "rgb": [255, 255, 255], "td_mm": 1.0},
            {"id": "black", "name": "Black", "rgb": [0, 0, 0], "td_mm": 1.0},
        ]
    }

    legacy_stl = tmp_path / "legacy.stl"
    new_stl = tmp_path / "new.stl"

    legacy_path = legacy_export(legacy_stl, plan, catalog, base_layer_mm=0.32, color_layer_mm=0.08)
    new_path = new_export(new_stl, plan, catalog, base_layer_mm=0.32, color_layer_mm=0.08)

    assert legacy_path.read_text(encoding="utf-8") == new_path.read_text(encoding="utf-8")
