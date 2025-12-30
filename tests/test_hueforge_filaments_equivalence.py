import json

import pytest

from hueforge.print.filaments import load_catalog as new_load_catalog
from src.print.filaments import load_catalog as legacy_load_catalog


def _write_catalog(path, data) -> None:
    path.write_text(json.dumps(data), encoding="utf-8")


def test_filaments_load_catalog_equivalence(tmp_path) -> None:
    data = {
        "filaments": [
            {"id": "f1", "name": "One", "rgb": [1, 2, 3], "td_mm": 1.2},
            {"id": "f2", "name": "Two", "rgb": [4, 5, 6], "td_mm": None},
        ]
    }
    path = tmp_path / "catalog.json"
    _write_catalog(path, data)

    legacy = legacy_load_catalog(path)
    new = new_load_catalog(path)

    assert legacy == new


def test_filaments_load_catalog_invalid_equivalence(tmp_path) -> None:
    data = {"filaments": [{"id": "f1", "name": "One", "td_mm": 1.0}]}
    path = tmp_path / "bad_catalog.json"
    _write_catalog(path, data)

    with pytest.raises(ValueError) as legacy_error:
        legacy_load_catalog(path)
    with pytest.raises(ValueError) as new_error:
        new_load_catalog(path)

    assert str(legacy_error.value) == str(new_error.value)
