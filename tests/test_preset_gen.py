import json
from pathlib import Path

from src.tools.preset_gen import run_preset_gen


def test_preset_gen_filters_and_base(tmp_path):
    catalog = {
        "filaments": [
            {"id": "a1", "manufacturer": "BrandA", "name": "White-ish", "rgb": [250, 250, 250], "td_mm": 1.0},
            {"id": "a2", "manufacturer": "BrandA", "name": "Dark", "rgb": [10, 10, 10], "td_mm": 1.0},
            {"id": "b1", "manufacturer": "BrandB", "name": "Other", "rgb": [200, 0, 0], "td_mm": 1.0},
        ]
    }
    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(json.dumps(catalog), encoding="utf-8")

    output_dir = tmp_path / "out"
    output_path = run_preset_gen(
        catalog_path,
        "BrandA",
        output_dir,
        n_colors=4,
        max_filaments=80,
    )

    preset = json.loads(output_path.read_text(encoding="utf-8"))
    allowed = preset["print"]["allowed_filaments"]
    assert allowed == ["a1", "a2"]
    assert preset["print"]["base_filament_id"] == "a1"
