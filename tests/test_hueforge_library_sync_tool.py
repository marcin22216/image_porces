import json
from pathlib import Path

from src.tools.hueforge_library_sync import sync_hueforge_library


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def test_hueforge_library_sync_updates_td_only(tmp_path) -> None:
    hueforge_data = {
        "metadata": {"source": "hueforge", "version": "1"},
        "filaments": [
            {
                "manufacturer": "Maker Co",
                "type": "PLA+",
                "color": "Ocean Blue",
                "hexCode": "#112233",
                "td": 1.5,
            }
        ],
    }
    target_data = {
        "filaments": [
            {
                "id": "maker_co_pla_ocean_blue",
                "name": "Keep Name",
                "rgb": [9, 9, 9],
                "td_mm": 9.9,
            },
            {
                "id": "unmatched",
                "name": "Stay",
                "rgb": [1, 2, 3],
                "td_mm": 3.3,
            },
        ]
    }
    hueforge_path = tmp_path / "hueforge.json"
    target_path = tmp_path / "target.json"
    out_path = tmp_path / "out.json"
    _write_json(hueforge_path, hueforge_data)
    _write_json(target_path, target_data)

    result_path = sync_hueforge_library(
        hueforge_path=hueforge_path,
        target_path=target_path,
        output_path=out_path,
    )
    result = json.loads(result_path.read_text(encoding="utf-8"))

    assert result["filaments"][0]["td_mm"] == 1.5
    assert result["filaments"][0]["name"] == "Keep Name"
    assert result["filaments"][0]["rgb"] == [9, 9, 9]
    assert result["filaments"][1]["td_mm"] == 3.3


def test_hueforge_library_sync_deterministic(tmp_path) -> None:
    hueforge_data = {
        "metadata": {"source": "hueforge", "version": "1"},
        "filaments": [
            {
                "manufacturer": "Maker Co",
                "type": "PLA",
                "color": "Black",
                "hexCode": "#000000",
                "td": 2.0,
            }
        ],
    }
    target_data = {
        "filaments": [
            {
                "id": "maker_co_pla_black",
                "name": "Black",
                "rgb": [0, 0, 0],
                "td_mm": 1.0,
            }
        ]
    }
    hueforge_path = tmp_path / "hueforge.json"
    target_path = tmp_path / "target.json"
    out_path = tmp_path / "out.json"
    out_path_2 = tmp_path / "out2.json"
    _write_json(hueforge_path, hueforge_data)
    _write_json(target_path, target_data)

    sync_hueforge_library(
        hueforge_path=hueforge_path,
        target_path=target_path,
        output_path=out_path,
    )
    sync_hueforge_library(
        hueforge_path=hueforge_path,
        target_path=target_path,
        output_path=out_path_2,
    )

    assert out_path.read_text(encoding="utf-8") == out_path_2.read_text(
        encoding="utf-8"
    )
