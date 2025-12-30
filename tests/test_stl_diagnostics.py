import struct
from pathlib import Path

from src.tools.stl_diagnostics import analyze_stl


def _write_binary_stl(path: Path) -> None:
    header = b"Binary STL".ljust(80, b"\0")
    triangle_count = 1
    normal = (0.0, 0.0, 1.0)
    v1 = (0.0, 0.0, 0.0)
    v2 = (1.0, 0.0, 0.0)
    v3 = (0.0, 2.0, 0.0)
    triangle = struct.pack("<12fH", *(normal + v1 + v2 + v3), 0)
    path.write_bytes(header + struct.pack("<I", triangle_count) + triangle)


def test_stl_diagnostics_binary(tmp_path) -> None:
    path = tmp_path / "test_binary.stl"
    _write_binary_stl(path)
    metrics = analyze_stl(path)
    assert metrics["format"] == "binary"
    assert metrics["triangles"] == 1
    assert metrics["bbox_min"] == (0.0, 0.0, 0.0)
    assert metrics["bbox_max"] == (1.0, 2.0, 0.0)
    assert metrics["dims"] == (1.0, 2.0, 0.0)
