import json
from pathlib import Path

import pytest

from hueforge.print.filaments import load_catalog as new_load_catalog
from src.print.filaments import load_catalog as legacy_load_catalog


def _write_library(path: Path, entries) -> None:
    data = {"metadata": {"source": "hueforge", "version": "1"}, "filaments": entries}
    path.write_text(json.dumps(data), encoding="utf-8")


def test_hueforge_library_happy_path(tmp_path) -> None:
    entries = [
        {
            "manufacturer": "Maker Co",
            "type": "PLA+",
            "color": "Ocean Blue",
            "hexCode": "#112233",
            "td": 1.5,
        },
        {
            "manufacturer": "Maker Co",
            "type": "PLA+",
            "color": "Ocean Blue",
            "hexCode": "#445566",
            "td": 2.0,
        },
    ]
    path = tmp_path / "library.json"
    _write_library(path, entries)

    legacy = legacy_load_catalog(path)
    new = new_load_catalog(path)

    assert legacy == new
    assert [item["id"] for item in new["filaments"]] == [
        "maker_co_pla_ocean_blue",
        "maker_co_pla_ocean_blue_2",
    ]
    assert [item["rgb"] for item in new["filaments"]] == [
        [17, 34, 51],
        [68, 85, 102],
    ]
    assert [item["td_mm"] for item in new["filaments"]] == [1.5, 2.0]


def test_hueforge_library_fixture_smoke() -> None:
    fixture = Path(__file__).resolve().parent / "fixtures" / "hueforge_library_fixture.json"
    result = new_load_catalog(fixture)
    assert len(result["filaments"]) == 2
    assert result["filaments"][0]["td_mm"] == 1.5


def test_hueforge_library_invalid_hex(tmp_path) -> None:
    entries = [
        {
            "manufacturer": "Maker",
            "type": "PLA",
            "color": "Bad",
            "hexCode": "112233",
            "td": 1.5,
        }
    ]
    path = tmp_path / "bad_hex.json"
    _write_library(path, entries)

    with pytest.raises(ValueError) as legacy_error:
        legacy_load_catalog(path)
    with pytest.raises(ValueError) as new_error:
        new_load_catalog(path)

    assert str(legacy_error.value) == str(new_error.value)


def test_hueforge_library_invalid_td(tmp_path) -> None:
    entries = [
        {
            "manufacturer": "Maker",
            "type": "PLA",
            "color": "Bad",
            "hexCode": "#112233",
            "td": 0,
        }
    ]
    path = tmp_path / "bad_td.json"
    _write_library(path, entries)

    with pytest.raises(ValueError) as legacy_error:
        legacy_load_catalog(path)
    with pytest.raises(ValueError) as new_error:
        new_load_catalog(path)

    assert str(legacy_error.value) == str(new_error.value)
