from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def export_colorplan_txt(
    stl_path: Path,
    plan: Dict[str, Any],
    catalog: Dict[str, Any],
    base_layer_mm: float,
    color_layer_mm: float,
) -> Path:
    if base_layer_mm < 0 or color_layer_mm <= 0:
        raise ValueError("layer thickness values must be >= 0 (color_layer_mm > 0)")
    total_layers = int(plan.get("total_layers", 1))

    output_path = stl_path.with_suffix(".colorplan.txt")
    lines = [
        "COLORPLAN v1",
        "UNITS mm",
        "LAYER_INDEXING zero_based",
        f"BASE_LAYER_MM {base_layer_mm:.6f}",
        f"COLOR_LAYER_MM {color_layer_mm:.6f}",
        f"TOTAL_LAYERS {total_layers}",
    ]
    start = plan.get("start")
    if start:
        lines.append(
            f"START {int(start['layer_index'])} {float(start['z_mm']):.6f} {start['filament_id']}"
        )
    for change in plan.get("changes", []):
        lines.append(
            f"CHANGE {int(change['layer_index'])} {float(change['z_mm']):.6f} {change['filament_id']}"
        )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
