import pytest

from src.app.cli_overrides import parse_id_list, validate_overrides


def test_parse_id_list():
    assert parse_id_list("a,b,,c") == ["a", "b", "c"]
    assert parse_id_list("") is None


def test_manual_mode_requires_sequence_ids():
    overrides = {"print": {"sequence_mode": "manual"}}
    with pytest.raises(ValueError) as exc:
        validate_overrides(overrides)
    assert "layer-sequence-ids" in str(exc.value)
