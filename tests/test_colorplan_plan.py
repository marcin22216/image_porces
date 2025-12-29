from src.app.pipeline import _build_colorplan, _sequence_from_assignment


def test_manual_sequence_respected():
    plan = _build_colorplan(
        base_filament_id="white",
        layer_sequence_ids=["a", "b"],
        base_layer_mm=0.2,
        color_layer_mm=0.1,
        catalog={"filaments": [{"id": "a"}, {"id": "b"}]},
        total_layers=5,
    )

    changes = plan["changes"]
    assert [c["filament_id"] for c in changes] == ["a", "b", "a", "b"]


def test_auto_palette_sequence_allowed():
    assignment = {0: "b", 1: "a", 2: "b"}
    sequence = _sequence_from_assignment(assignment, 3)
    plan = _build_colorplan(
        base_filament_id="white",
        layer_sequence_ids=sequence,
        base_layer_mm=0.2,
        color_layer_mm=0.1,
        catalog={"filaments": [{"id": "a"}, {"id": "b"}]},
        total_layers=3,
    )

    used = set(sequence)
    used.add(plan["start"]["filament_id"])
    used.update(c["filament_id"] for c in plan["changes"])
    assert used.issubset({"white", "a", "b"})
