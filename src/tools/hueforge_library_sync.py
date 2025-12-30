from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable

from hueforge.print.filaments import load_catalog


def sync_hueforge_library(
    *,
    hueforge_path: Path,
    target_path: Path,
    output_path: Path | None = None,
) -> Path:
    raw_hueforge = _read_json(hueforge_path)
    _ensure_hueforge_library(raw_hueforge)
    source_catalog = load_catalog(hueforge_path)
    target_data = _read_json(target_path)
    _ensure_target_catalog(target_data)

    source_by_id = {item["id"]: item for item in source_catalog["filaments"]}
    source_by_meta = _build_meta_index(source_catalog["filaments"])

    updated = 0
    for filament in target_data["filaments"]:
        target_id = filament["id"]
        match = source_by_id.get(target_id)
        if match is None:
            meta_key = _meta_key(filament)
            if meta_key is not None:
                match = source_by_meta.get(meta_key)
        if match is None:
            continue
        filament["td_mm"] = match["td_mm"]
        updated += 1

    output_path = output_path or target_path.with_suffix(".synced.json")
    output_path.write_text(
        json.dumps(target_data, indent=2), encoding="utf-8"
    )
    print(f"HueForge sync: updated={updated} output={output_path}")
    return output_path


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _ensure_hueforge_library(data: Dict[str, Any]) -> None:
    if not isinstance(data, dict) or "metadata" not in data:
        raise ValueError("hueforge library must include metadata")
    entries = _extract_entries(data)
    if not entries:
        raise ValueError("hueforge library must include entries")
    for item in entries:
        if not isinstance(item, dict):
            raise ValueError("hueforge library entries must be objects")
        if "hexCode" not in item:
            raise ValueError("hueforge entry missing hexCode")
        if "td" not in item:
            raise ValueError("hueforge entry missing td")


def _extract_entries(data: Dict[str, Any]) -> list[object]:
    for key in ("filaments", "entries", "records"):
        entries = data.get(key)
        if isinstance(entries, list):
            return entries
    return []


def _ensure_target_catalog(data: Dict[str, Any]) -> None:
    filaments = data.get("filaments")
    if not isinstance(filaments, list) or not filaments:
        raise ValueError("target catalog must include non-empty filaments list")
    for filament in filaments:
        if not isinstance(filament, dict):
            raise ValueError("target filament entries must be objects")
        if "id" not in filament:
            raise ValueError("target filament missing id")


def _build_meta_index(
    entries: Iterable[Dict[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    index: Dict[str, Dict[str, Any]] = {}
    collisions: set[str] = set()
    for entry in entries:
        meta_key = _meta_key(entry)
        if meta_key is None:
            continue
        if meta_key in index:
            collisions.add(meta_key)
            continue
        index[meta_key] = entry
    for key in collisions:
        index.pop(key, None)
    return index


def _meta_key(entry: Dict[str, Any]) -> str | None:
    manufacturer = entry.get("manufacturer")
    material_type = entry.get("type")
    color = entry.get("color")
    if not all(
        isinstance(value, str) and value.strip()
        for value in (manufacturer, material_type, color)
    ):
        return None
    return _build_id([manufacturer, material_type, color])


def _build_id(parts: list[str]) -> str:
    slugged = [_slugify(part) for part in parts]
    value = "_".join([part for part in slugged if part])
    if not value:
        raise ValueError("id components must be non-empty")
    return value


def _slugify(value: str) -> str:
    output = []
    prev_underscore = False
    for char in value.strip().lower():
        if char.isalnum():
            output.append(char)
            prev_underscore = False
        else:
            if not prev_underscore:
                output.append("_")
                prev_underscore = True
    return "".join(output).strip("_")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync default filament catalog with HueForge library TD values."
    )
    parser.add_argument("--hueforge", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    sync_hueforge_library(
        hueforge_path=Path(args.hueforge),
        target_path=Path(args.target),
        output_path=Path(args.out) if args.out else None,
    )


if __name__ == "__main__":
    main()
