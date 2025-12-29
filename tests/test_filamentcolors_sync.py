from pathlib import Path

from src.tools.filamentcolors_sync import hex_to_rgb, normalize_swatch, sync_catalog


def test_hex_to_rgb_parses():
    assert hex_to_rgb("#00ff10") == (0, 255, 16)
    assert hex_to_rgb("AABBCC") == (170, 187, 204)


def test_normalize_swatch_basic():
    swatch = {
        "id": 123,
        "manufacturer": {"name": "Maker"},
        "color_name": "Ocean",
        "filament_type": {"name": "PLA"},
        "hex_color": "#112233",
        "lab_l": 10.0,
        "lab_a": 2.0,
        "lab_b": -3.0,
        "td": 1.5,
    }
    record = normalize_swatch(swatch)

    assert record["filament_id"] == "filamentcolors:123"
    assert record["manufacturer"] == "Maker"
    assert record["color_name"] == "Ocean"
    assert record["filament_type"] == "PLA"
    assert record["rgb"] == [17, 34, 51]
    assert record["lab"] == [10.0, 2.0, -3.0]
    assert record["td"] == 1.5


def test_sync_skips_missing_hex(tmp_path, monkeypatch):
    def fake_fetch_json(url: str):
        if url.endswith("/api/version/"):
            return {"db_last_modified": "2024-01-01"}
        return {
            "results": [
                {
                    "id": 1,
                    "manufacturer": {"name": "Maker"},
                    "color_name": "Good",
                    "filament_type": {"name": "PLA"},
                    "hex_color": "#112233",
                },
                {
                    "id": 2,
                    "manufacturer": {"name": "Maker"},
                    "color_name": "Bad",
                    "filament_type": {"name": "PLA"},
                },
            ],
            "next": None,
        }

    monkeypatch.setattr(
        "src.tools.filamentcolors_sync._fetch_json", fake_fetch_json
    )
    output = sync_catalog(
        base_url="https://example.test",
        output_path=Path(tmp_path / "catalog.json"),
        state_path=Path(tmp_path / "state.json"),
    )
    data = output.read_text(encoding="utf-8")
    assert "filamentcolors:1" in data
    assert "filamentcolors:2" not in data
