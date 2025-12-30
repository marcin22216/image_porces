#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

CANON_BASE = 0.32
CANON_STEP = 0.08
CANON_MAX_COLORS = 4
TOL = 1e-3
KEYWORDS = ("plan", "color", "swap", "tool", "change", "palette")


def _is_candidate(name: str) -> bool:
    lower = name.lower()
    if lower.endswith((".txt", ".gcode", ".gc", ".nc")):
        return True
    return any(key in lower for key in KEYWORDS)


def _candidate_score(name: str) -> int:
    lower = name.lower()
    score = sum(1 for key in KEYWORDS if key in lower)
    if lower.endswith(".colorplan.txt"):
        score += 5
    if lower.endswith(".gcode"):
        score += 2
    if lower.endswith(".txt"):
        score += 1
    return score


def _looks_like_gcode(lines: list[str]) -> bool:
    for line in lines[:200]:
        stripped = line.lstrip()
        if not stripped:
            continue
        if stripped.startswith(("G0", "G1", "G00", "G01", "M", "T")):
            return True
    return False


def _parse_colorplan(lines: list[str]) -> dict | None:
    if not lines:
        return None
    if not lines[0].startswith("COLORPLAN"):
        return None
    events: list[dict] = []
    for idx, line in enumerate(lines, start=1):
        parts = line.strip().split()
        if not parts:
            continue
        if parts[0] not in ("START", "CHANGE"):
            continue
        if len(parts) < 4:
            continue
        kind = parts[0]
        try:
            height = float(parts[2])
        except ValueError:
            height = None
        tool = parts[3]
        events.append(
            {
                "kind": kind,
                "height": height,
                "tool": tool,
                "line_no": idx,
                "line": line.rstrip("\n"),
            }
        )
    return {"format": "colorplan", "events": events}


def _parse_table(lines: list[str]) -> dict | None:
    if not lines:
        return None
    header_idx = None
    delimiter = None
    for idx, line in enumerate(lines[:50]):
        if "," in line:
            delimiter = ","
        elif "\t" in line:
            delimiter = "\t"
        else:
            continue
        header = [h.strip().lower() for h in line.strip().split(delimiter)]
        if any(key in header for key in ("z", "height", "z_mm")):
            header_idx = idx
            break
    if header_idx is None or delimiter is None:
        return None

    header = [h.strip().lower() for h in lines[header_idx].strip().split(delimiter)]
    z_idx = next(
        (i for i, h in enumerate(header) if h in ("z", "height", "z_mm")),
        None,
    )
    tool_idx = next(
        (i for i, h in enumerate(header) if h in ("tool", "color", "material", "filament")),
        None,
    )
    if z_idx is None:
        return None

    events: list[dict] = []
    for offset, line in enumerate(lines[header_idx + 1 :], start=header_idx + 2):
        if not line.strip():
            continue
        parts = [p.strip() for p in line.strip().split(delimiter)]
        if len(parts) <= z_idx:
            continue
        try:
            height = float(parts[z_idx])
        except ValueError:
            continue
        tool = parts[tool_idx] if tool_idx is not None and tool_idx < len(parts) else None
        events.append(
            {
                "kind": "CHANGE",
                "height": height,
                "tool": tool,
                "line_no": offset,
                "line": line.rstrip("\n"),
            }
        )
    if not events:
        return None
    return {"format": "table", "events": events}


def _parse_key_value(lines: list[str]) -> dict | None:
    key_value = re.compile(r"([a-zA-Z_]+)\\s*[:=]\\s*([^\\s,;]+)")
    events: list[dict] = []
    for idx, line in enumerate(lines, start=1):
        pairs = {m.group(1).lower(): m.group(2) for m in key_value.finditer(line)}
        if not pairs:
            continue
        height_value = None
        for key in ("z", "height", "z_mm"):
            if key in pairs:
                try:
                    height_value = float(pairs[key])
                except ValueError:
                    height_value = None
                break
        if height_value is None:
            continue
        tool_value = None
        for key in ("tool", "color", "material", "filament"):
            if key in pairs:
                tool_value = pairs[key]
                break
        events.append(
            {
                "kind": "CHANGE",
                "height": height_value,
                "tool": tool_value,
                "line_no": idx,
                "line": line.rstrip("\n"),
            }
        )
    if not events:
        return None
    return {"format": "key_value", "events": events}


def _parse_gcode(lines: list[str]) -> dict | None:
    if not _looks_like_gcode(lines):
        return None
    events: list[dict] = []
    current_z = None
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith(";"):
            continue
        if stripped.startswith(("G0", "G1", "G00", "G01")):
            match = re.search(r"\\bZ(-?\\d+(?:\\.\\d+)?)", stripped)
            if match:
                current_z = float(match.group(1))
        tool_match = re.match(r"^T(\\d+)", stripped)
        if tool_match:
            events.append(
                {
                    "kind": "CHANGE",
                    "height": current_z,
                    "tool": tool_match.group(1),
                    "line_no": idx,
                    "line": line.rstrip("\n"),
                }
            )
            continue
        if stripped.startswith(("M600", "M0", "M25")):
            events.append(
                {
                    "kind": "CHANGE",
                    "height": current_z,
                    "tool": None,
                    "line_no": idx,
                    "line": line.rstrip("\n"),
                }
            )
    if not events:
        return None
    return {"format": "gcode", "events": events}


def _parse_plan(lines: list[str]) -> dict | None:
    for parser in (_parse_colorplan, _parse_table, _parse_key_value, _parse_gcode):
        result = parser(lines)
        if result:
            return result
    return None


def _load_text(zf: zipfile.ZipFile, name: str) -> list[str]:
    content = zf.read(name).decode("utf-8", errors="replace")
    return content.splitlines()


def _audit_plan(events: list[dict]) -> dict:
    start_events = [ev for ev in events if ev["kind"] == "START"]
    change_events = [ev for ev in events if ev["kind"] != "START"]

    color_ids = {ev["tool"] for ev in events if ev.get("tool") not in (None, "")}
    unique_colors = sorted(color_ids, key=str)

    heights = [ev["height"] for ev in change_events if ev.get("height") is not None]
    min_height = min(heights) if heights else None
    max_height = max(heights) if heights else None

    violations: list[dict] = []
    if len(unique_colors) > CANON_MAX_COLORS:
        violations.append(
            {
                "rule": "unique_colors",
                "line_no": None,
                "line": f"unique_colors={len(unique_colors)}",
            }
        )

    for ev in change_events:
        height = ev.get("height")
        if height is None:
            violations.append(
                {
                    "rule": "missing_height",
                    "line_no": ev["line_no"],
                    "line": ev["line"],
                }
            )
            continue
        if height < CANON_BASE - TOL:
            violations.append(
                {
                    "rule": "below_base",
                    "line_no": ev["line_no"],
                    "line": ev["line"],
                }
            )
            continue
        steps = (height - CANON_BASE) / CANON_STEP
        if abs(steps - round(steps)) > TOL:
            violations.append(
                {
                    "rule": "off_grid",
                    "line_no": ev["line_no"],
                    "line": ev["line"],
                }
            )

    return {
        "start_events": start_events,
        "change_events": change_events,
        "unique_colors": unique_colors,
        "min_height": min_height,
        "max_height": max_height,
        "violations": violations,
    }


def _print_changes(change_events: list[dict], start_tool: str | None) -> None:
    prev_tool = start_tool
    for ev in change_events[:30]:
        from_tool = prev_tool if prev_tool is not None else "?"
        to_tool = ev.get("tool") if ev.get("tool") not in (None, "") else "?"
        height = ev.get("height")
        height_str = f"{height:.6f}" if height is not None else "unknown"
        print(f"- {height_str} mm: {from_tool} -> {to_tool}")
        if ev.get("tool") not in (None, ""):
            prev_tool = ev["tool"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit color/swap plan heights in a bundle.")
    parser.add_argument("bundle", nargs="?", default="bundle.zip")
    args = parser.parse_args()

    bundle_path = Path(args.bundle)
    if not bundle_path.exists():
        print(f"Bundle not found: {bundle_path}")
        return 2

    with zipfile.ZipFile(bundle_path) as zf:
        names = zf.namelist()
        candidates = [name for name in names if _is_candidate(name)]
        if not candidates:
            print("No plan-like files found in bundle.")
            for name in names:
                print(f"- {name}")
            return 2
        candidates = sorted(candidates, key=_candidate_score, reverse=True)

        chosen = None
        parsed = None
        for name in candidates:
            lines = _load_text(zf, name)
            parsed = _parse_plan(lines)
            if parsed:
                chosen = name
                break

        if chosen is None or parsed is None:
            first = candidates[0]
            print(f"Could not parse any plan-like file. First candidate: {first}")
            lines = _load_text(zf, first)
            for line in lines[:50]:
                print(line)
            return 3

    events = parsed["events"]
    report = _audit_plan(events)

    print(f"Plan file: {chosen}")
    print(f"Detected format: {parsed['format']}")
    print(f"Unique colors: {len(report['unique_colors'])} -> {report['unique_colors']}")
    print(f"Total changes: {len(report['change_events'])}")
    if report["min_height"] is not None:
        print(f"Change heights: min={report['min_height']:.6f} max={report['max_height']:.6f}")
    else:
        print("Change heights: none detected")

    counts = {}
    for item in report["violations"]:
        counts[item["rule"]] = counts.get(item["rule"], 0) + 1
    print("Violations:")
    for rule in ("unique_colors", "missing_height", "below_base", "off_grid"):
        print(f"- {rule}: {counts.get(rule, 0)}")

    print("First 20 violations:")
    for item in report["violations"][:20]:
        line_no = item.get("line_no")
        prefix = f"line {line_no}" if line_no else "global"
        print(f"- {prefix} [{item['rule']}] {item['line']}")

    start_tool = report["start_events"][0]["tool"] if report["start_events"] else None
    print("Top 30 changes:")
    _print_changes(report["change_events"], start_tool)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
