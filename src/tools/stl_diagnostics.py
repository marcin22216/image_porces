from __future__ import annotations

import argparse
import struct
from pathlib import Path
from typing import Dict, Iterable, Tuple


def analyze_stl(path: Path) -> Dict[str, object]:
    size_bytes = path.stat().st_size
    with path.open("rb") as handle:
        header = handle.read(80)
        count_bytes = handle.read(4)
        if len(count_bytes) == 4:
            tri_count = struct.unpack("<I", count_bytes)[0]
        else:
            tri_count = 0
        expected_size = 84 + tri_count * 50
        if tri_count > 0 and size_bytes == expected_size:
            fmt = "binary"
            triangles, bbox_min, bbox_max = _parse_binary_triangles(handle, tri_count)
        else:
            fmt = "ascii"
            handle.seek(0)
            content = handle.read().decode("utf-8", errors="ignore")
            triangles, bbox_min, bbox_max = _parse_ascii_triangles(content)

    dims = (
        bbox_max[0] - bbox_min[0],
        bbox_max[1] - bbox_min[1],
        bbox_max[2] - bbox_min[2],
    )
    return {
        "path": str(path),
        "format": fmt,
        "size_bytes": size_bytes,
        "triangles": triangles,
        "bbox_min": bbox_min,
        "bbox_max": bbox_max,
        "dims": dims,
    }


def format_report(metrics: Dict[str, object]) -> str:
    bbox_min = _format_vec(metrics["bbox_min"])
    bbox_max = _format_vec(metrics["bbox_max"])
    dims = _format_vec(metrics["dims"])
    lines = [
        f"STL path: {metrics['path']}",
        f"Format: {metrics['format']}",
        f"Size (bytes): {metrics['size_bytes']}",
        f"Triangles: {metrics['triangles']}",
        f"Bounding box min: {bbox_min}",
        f"Bounding box max: {bbox_max}",
        f"Dimensions: {dims}",
    ]
    return "\n".join(lines)


def _format_vec(value: Tuple[float, float, float]) -> str:
    return f"({value[0]:.6f}, {value[1]:.6f}, {value[2]:.6f})"


def _parse_binary_triangles(
    handle, tri_count: int
) -> Tuple[int, Tuple[float, float, float], Tuple[float, float, float]]:
    bbox_min = [float("inf"), float("inf"), float("inf")]
    bbox_max = [float("-inf"), float("-inf"), float("-inf")]
    triangles = 0
    for _ in range(tri_count):
        data = handle.read(50)
        if len(data) != 50:
            raise ValueError("binary STL ended unexpectedly")
        values = struct.unpack("<12fH", data)
        vertices = [
            values[3:6],
            values[6:9],
            values[9:12],
        ]
        _update_bounds(vertices, bbox_min, bbox_max)
        triangles += 1
    return triangles, tuple(bbox_min), tuple(bbox_max)


def _parse_ascii_triangles(
    content: str,
) -> Tuple[int, Tuple[float, float, float], Tuple[float, float, float]]:
    bbox_min = [float("inf"), float("inf"), float("inf")]
    bbox_max = [float("-inf"), float("-inf"), float("-inf")]
    triangles = 0
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("facet normal"):
            triangles += 1
            continue
        if stripped.startswith("vertex"):
            parts = stripped.split()
            if len(parts) < 4:
                continue
            try:
                vertex = (float(parts[1]), float(parts[2]), float(parts[3]))
            except ValueError:
                continue
            _update_bounds([vertex], bbox_min, bbox_max)
    if triangles == 0:
        raise ValueError("no facets found in ASCII STL")
    return triangles, tuple(bbox_min), tuple(bbox_max)


def _update_bounds(
    vertices: Iterable[Tuple[float, float, float]],
    bbox_min: list[float],
    bbox_max: list[float],
) -> None:
    for x, y, z in vertices:
        if x < bbox_min[0]:
            bbox_min[0] = x
        if y < bbox_min[1]:
            bbox_min[1] = y
        if z < bbox_min[2]:
            bbox_min[2] = z
        if x > bbox_max[0]:
            bbox_max[0] = x
        if y > bbox_max[1]:
            bbox_max[1] = y
        if z > bbox_max[2]:
            bbox_max[2] = z


def main() -> None:
    parser = argparse.ArgumentParser(description="STL diagnostics")
    parser.add_argument("--stl", required=True)
    args = parser.parse_args()
    metrics = analyze_stl(Path(args.stl))
    print(format_report(metrics))


if __name__ == "__main__":
    main()
