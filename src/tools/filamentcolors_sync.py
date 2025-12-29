from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.request import urlopen


def hex_to_rgb(value: str) -> Tuple[int, int, int]:
    text = value.strip().lstrip("#")
    if len(text) != 6:
        raise ValueError("hex color must be 6 characters")
    red = int(text[0:2], 16)
    green = int(text[2:4], 16)
    blue = int(text[4:6], 16)
    return red, green, blue


def normalize_swatch(swatch: Dict[str, Any]) -> Dict[str, Any]:
    swatch_id = swatch.get("id")
    if swatch_id is None:
        raise ValueError("swatch missing id")
    rgb_hex = swatch.get("hex_color")
    if not rgb_hex:
        raise ValueError("swatch missing rgb/hex")
    rgb = hex_to_rgb(str(rgb_hex))
    manufacturer = swatch.get("manufacturer")
    if isinstance(manufacturer, dict):
        manufacturer = manufacturer.get("name")
    filament_type = swatch.get("filament_type")
    if isinstance(filament_type, dict):
        filament_type = filament_type.get("name")
    record: Dict[str, Any] = {
        "filament_id": f"filamentcolors:{swatch_id}",
        "manufacturer": manufacturer or "",
        "color_name": swatch.get("color_name") or "",
        "filament_type": filament_type or "",
        "rgb": list(rgb),
    }
    if (
        swatch.get("lab_l") is not None
        and swatch.get("lab_a") is not None
        and swatch.get("lab_b") is not None
    ):
        record["lab"] = [swatch["lab_l"], swatch["lab_a"], swatch["lab_b"]]
    if swatch.get("td") is not None:
        record["td"] = swatch["td"]
    return record


def sync_catalog(
    *,
    base_url: str = "https://filamentcolors.xyz",
    output_path: Path = Path("data/filament_catalog_filamentcolors.json"),
    state_path: Path = Path("data/filamentcolors_state.json"),
) -> Path:
    version = _fetch_json(f"{base_url}/api/version/")
    db_last_modified = version.get("db_last_modified")
    state = _read_state(state_path)
    if (
        state is not None
        and state.get("db_last_modified") == db_last_modified
        and output_path.exists()
    ):
        return output_path

    swatches = _fetch_all_swatches(base_url)
    normalized = []
    skipped = 0
    reasons: Dict[str, int] = {}
    for swatch in swatches:
        try:
            normalized.append(normalize_swatch(swatch))
        except ValueError as exc:
            skipped += 1
            reason = str(exc)
            reasons[reason] = reasons.get(reason, 0) + 1
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            {
                "source": "filamentcolors.xyz",
                "db_last_modified": db_last_modified,
                "swatches": normalized,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps({"db_last_modified": db_last_modified, "version": version}, indent=2),
        encoding="utf-8",
    )
    _print_summary(len(swatches), len(normalized), skipped, reasons)
    return output_path


def _print_summary(
    fetched: int, saved: int, skipped: int, reasons: Dict[str, int]
) -> None:
    print(f"FilamentColors sync: fetched={fetched} saved={saved} skipped={skipped}")
    if reasons:
        for reason, count in sorted(reasons.items()):
            print(f"Skipped ({reason}): {count}")


def _fetch_all_swatches(base_url: str) -> List[Dict[str, Any]]:
    swatches: List[Dict[str, Any]] = []
    page = 1
    while True:
        data = _fetch_json(
            f"{base_url}/api/swatch/?page={page}&page_size=100"
        )
        results = data.get("results", [])
        swatches.extend(results)
        if not data.get("next"):
            break
        page += 1
    return swatches


def _fetch_json(url: str) -> Dict[str, Any]:
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def _read_state(path: Path) -> Optional[Dict[str, Any]]:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync FilamentColors.xyz catalog")
    parser.add_argument("--base-url", default="https://filamentcolors.xyz")
    parser.add_argument(
        "--output", default="data/filament_catalog_filamentcolors.json"
    )
    parser.add_argument("--state", default="data/filamentcolors_state.json")
    args = parser.parse_args()
    sync_catalog(
        base_url=args.base_url,
        output_path=Path(args.output),
        state_path=Path(args.state),
    )


if __name__ == "__main__":
    main()
