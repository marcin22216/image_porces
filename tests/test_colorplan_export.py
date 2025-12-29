from pathlib import Path

from src.print.colorplan_export import export_colorplan_txt


def test_colorplan_export_writes_file(tmp_path):
    stl_path = tmp_path / "output.stl"
    stl_path.write_text("solid test\nendsolid test\n", encoding="utf-8")

    plan = {
        "total_layers": 3,
        "start": {"layer_index": 0, "z_mm": 0.2, "filament_id": "white"},
        "changes": [
            {"layer_index": 1, "z_mm": 0.5, "filament_id": "c1"},
            {"layer_index": 2, "z_mm": 0.8, "filament_id": "c2"},
        ],
    }
    catalog = {
        "filaments": [
            {"id": "base", "name": "Base", "rgb": [255, 255, 255], "td_mm": 2.0}
        ]
    }

    output_path = export_colorplan_txt(
        Path(stl_path),
        plan,
        catalog,
        base_layer_mm=0.2,
        color_layer_mm=0.3,
    )

    assert output_path.exists()
    content = output_path.read_text(encoding="utf-8")
    assert "BASE_LAYER_MM 0.200000" in content
    assert "COLOR_LAYER_MM 0.300000" in content
    assert "START" in content
    assert "CHANGE" in content

    lines = [line.strip() for line in content.splitlines() if line.startswith(("START", "CHANGE"))]
    entries = []
    for line in lines:
        parts = line.split()
        entries.append((parts[0], int(parts[1]), float(parts[2])))
    assert entries[0][0] == "START"
    assert entries[0][1] == 0
    assert abs(entries[0][2] - 0.2) < 1e-6
    for name, idx, z in entries[1:]:
        assert name == "CHANGE"
        assert abs(z - (0.2 + idx * 0.3)) < 1e-6
