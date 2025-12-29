from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.color.color_distance import color_distance, rgb_to_lab
from src.tools.filaments_cli import load_filament_catalog


def generate_preset(
    catalog: List[Dict[str, Any]],
    manufacturer: str,
    catalog_path: str,
    *,
    n_colors: int = 4,
    max_filaments: int = 80,
) -> Dict[str, Any]:
    filtered = [item for item in catalog if _match_manufacturer(item, manufacturer)]
    if max_filaments > 0:
        filtered = filtered[:max_filaments]
    allowed = [item["id"] for item in filtered]

    base_id = None
    if filtered:
        base_id = _nearest_to_white(filtered)
    if base_id is None and allowed:
        base_id = allowed[0]

    return {
        "palette": {"n_colors": int(n_colors)},
        "print": {
            "filament_catalog": catalog_path,
            "sequence_mode": "auto_palette",
            "allowed_filaments": allowed,
            "base_filament_id": base_id,
        },
    }


def run_preset_gen(
    catalog_path: Path,
    manufacturer: str,
    output_dir: Path,
    *,
    n_colors: int = 4,
    max_filaments: int = 80,
) -> Path:
    catalog = load_filament_catalog(catalog_path)
    preset = generate_preset(
        catalog,
        manufacturer,
        _relativize_path(catalog_path),
        n_colors=n_colors,
        max_filaments=max_filaments,
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "default_4_auto.json"
    output_path.write_text(json.dumps(preset, indent=2), encoding="utf-8")
    return output_path


def _match_manufacturer(item: Dict[str, Any], manufacturer: str) -> bool:
    value = str(item.get("manufacturer") or "")
    return value.lower() == manufacturer.lower()


def _nearest_to_white(items: List[Dict[str, Any]]) -> Optional[str]:
    target_rgb = (255, 255, 255)
    target = {"rgb": list(target_rgb), "lab": list(rgb_to_lab(target_rgb))}
    best_id = None
    best_dist = None
    for item in items:
        if not item.get("rgb"):
            continue
        dist = color_distance(target, item)
        if best_dist is None or dist < best_dist or (
            dist == best_dist and item["id"] < best_id
        ):
            best_dist = dist
            best_id = item["id"]
    return best_id


def _relativize_path(path: Path) -> str:
    try:
        repo_root = Path(__file__).resolve().parents[2]
        rel = path.resolve().relative_to(repo_root)
        return str(rel)
    except ValueError:
        return str(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate brand preset packs")
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--manufacturer", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--n-colors", type=int, default=4)
    parser.add_argument("--max-filaments", type=int, default=80)
    args = parser.parse_args()
    run_preset_gen(
        Path(args.catalog),
        args.manufacturer,
        Path(args.out),
        n_colors=args.n_colors,
        max_filaments=args.max_filaments,
    )


if __name__ == "__main__":
    main()
