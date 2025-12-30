import argparse
import sys
from pathlib import Path

from .cli_errors import CliError
from .doctor import run_doctor
from .pipeline import run_pipeline
from .version import __version__

def main():
    parser = argparse.ArgumentParser(description="Image-to-3D generator")
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    parser.add_argument("--about", action="store_true", help="Print about info and exit")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("doctor", help="Run environment checks")

    run_parser = subparsers.add_parser("run", help="Run full CLI pipeline")
    run_parser.add_argument("--in", dest="input_path", required=True)
    run_parser.add_argument("--out", dest="output_path", required=True)
    run_parser.add_argument("--debug", dest="debug_dir")
    run_parser.add_argument("--preset", dest="preset_path")
    run_parser.add_argument("--allowed-filaments", dest="allowed_filaments")
    run_parser.add_argument("--catalog", dest="catalog")
    run_parser.add_argument("--n-colors", dest="n_colors", type=int)
    run_parser.add_argument("--base-filament-id", dest="base_filament_id")
    run_parser.add_argument("--sequence-mode", dest="sequence_mode", choices=["manual", "auto_palette"])
    run_parser.add_argument("--layer-sequence-ids", dest="layer_sequence_ids")
    run_parser.add_argument("--blend-depth", dest="blend_depth", type=float)
    run_parser.add_argument("--width-mm", dest="width_mm", type=float)
    run_parser.add_argument("--height-mm", dest="height_mm", type=float)

    preview_parser = subparsers.add_parser("preview", help="Run preview-only pipeline")
    preview_parser.add_argument("--in", dest="input_path", required=True)
    preview_parser.add_argument("--debug", dest="debug_dir", required=True)
    preview_parser.add_argument("--preset", dest="preset_path")
    preview_parser.add_argument("--allowed-filaments", dest="allowed_filaments")
    preview_parser.add_argument("--catalog", dest="catalog")
    preview_parser.add_argument("--n-colors", dest="n_colors", type=int)
    preview_parser.add_argument("--base-filament-id", dest="base_filament_id")
    preview_parser.add_argument("--sequence-mode", dest="sequence_mode", choices=["manual", "auto_palette"])
    preview_parser.add_argument("--layer-sequence-ids", dest="layer_sequence_ids")
    preview_parser.add_argument("--blend-depth", dest="blend_depth", type=float)
    preview_parser.add_argument("--width-mm", dest="width_mm", type=float)
    preview_parser.add_argument("--height-mm", dest="height_mm", type=float)

    filaments_parser = subparsers.add_parser(
        "filaments", help="List and filter filament catalog"
    )
    filaments_parser.add_argument("--catalog", required=True)
    filaments_parser.add_argument("--search")
    filaments_parser.add_argument("--td-min", type=float, dest="td_min")
    filaments_parser.add_argument("--td-max", type=float, dest="td_max")
    filaments_parser.add_argument("--include-missing-td", action="store_true")
    filaments_parser.add_argument("--nearest")
    filaments_parser.add_argument("--top", type=int, default=10)
    filaments_parser.add_argument("--limit", type=int, default=50)
    filaments_parser.add_argument("--offset", type=int, default=0)

    bundle_parser = subparsers.add_parser("bundle", help="Create ZIP bundle")
    bundle_parser.add_argument("--in", dest="input_path", required=True)
    bundle_parser.add_argument("--out", dest="output_zip", required=True)
    bundle_parser.add_argument("--debug", dest="debug_dir")
    bundle_parser.add_argument("--preset", dest="preset_path")
    bundle_parser.add_argument("--allowed-filaments", dest="allowed_filaments")
    bundle_parser.add_argument("--catalog", dest="catalog")
    bundle_parser.add_argument("--n-colors", dest="n_colors", type=int)
    bundle_parser.add_argument("--base-filament-id", dest="base_filament_id")
    bundle_parser.add_argument("--sequence-mode", dest="sequence_mode", choices=["manual", "auto_palette"])
    bundle_parser.add_argument("--layer-sequence-ids", dest="layer_sequence_ids")
    bundle_parser.add_argument("--blend-depth", dest="blend_depth", type=float)
    bundle_parser.add_argument("--width-mm", dest="width_mm", type=float)
    bundle_parser.add_argument("--height-mm", dest="height_mm", type=float)

    hueforge_bundle_parser = subparsers.add_parser(
        "hueforge-bundle", help="Create ZIP bundle using hueforge pipeline"
    )
    hueforge_bundle_parser.add_argument("--in", dest="input_path", required=True)
    hueforge_bundle_parser.add_argument("--out", dest="output_zip", required=True)
    hueforge_bundle_parser.add_argument("--debug", dest="debug_dir")
    hueforge_bundle_parser.add_argument("--preset", dest="preset_path")
    hueforge_bundle_parser.add_argument("--allowed-filaments", dest="allowed_filaments")
    hueforge_bundle_parser.add_argument("--catalog", dest="catalog")
    hueforge_bundle_parser.add_argument("--n-colors", dest="n_colors", type=int)
    hueforge_bundle_parser.add_argument("--base-filament-id", dest="base_filament_id")
    hueforge_bundle_parser.add_argument(
        "--sequence-mode", dest="sequence_mode", choices=["manual", "auto_palette"]
    )
    hueforge_bundle_parser.add_argument("--layer-sequence-ids", dest="layer_sequence_ids")
    hueforge_bundle_parser.add_argument("--blend-depth", dest="blend_depth", type=float)
    hueforge_bundle_parser.add_argument("--width-mm", dest="width_mm", type=float)
    hueforge_bundle_parser.add_argument("--height-mm", dest="height_mm", type=float)

    stl_diag_parser = subparsers.add_parser(
        "stl-diagnostics", help="Report STL size/triangles/bounds"
    )
    stl_diag_parser.add_argument("--stl", dest="stl_path", required=True)

    args = parser.parse_args()
    try:
        if args.version:
            print(__version__)
            return
        if args.about:
            print(
                "Image-to-3D layered relief generator. Turns an image into STL + color change plan."
            )
            print("Author: Marcin Walczak. License: MIT.")
            return
        if args.command == "doctor":
            run_doctor()
            return
        if args.command == "run":
            _run_command(args)
            return
        if args.command == "preview":
            _preview_command(args)
            return
        if args.command == "filaments":
            _filaments_command(args)
            return
        if args.command == "bundle":
            _bundle_command(args)
            return
        if args.command == "hueforge-bundle":
            _hueforge_bundle_command(args)
            return
        if args.command == "stl-diagnostics":
            _stl_diagnostics_command(args)
            return
        parser.print_help()
    except CliError as exc:
        print(exc.message, file=sys.stderr)
        if exc.hint:
            print(exc.hint, file=sys.stderr)
        raise SystemExit(2)

def _run_command(args: argparse.Namespace) -> None:
    from .cli_overrides import apply_overrides, build_overrides, load_preset, parse_id_list, validate_overrides

    input_path = Path(args.input_path)
    if not input_path.exists():
        raise CliError(f"Input not found: {args.input_path}")
    if input_path.is_dir():
        raise CliError(f"Input is a directory, expected an image file: {args.input_path}")

    allowed_filaments = parse_id_list(args.allowed_filaments)
    overrides = build_overrides(args)
    try:
        validate_overrides(overrides)
    except ValueError as exc:
        raise CliError(str(exc))

    preset = apply_overrides(load_preset(args.preset_path), overrides)
    catalog_path = Path(
        preset.get("print", {}).get("filament_catalog", "filaments/default_catalog.json")
    )
    if not catalog_path.exists():
        raise CliError(
            f"Catalog not found: {catalog_path}",
            "Hint: run filamentcolors_sync to create data/filament_catalog_filamentcolors.json",
        )
    if allowed_filaments:
        missing = _find_missing_allowed(catalog_path, allowed_filaments)
        if missing:
            raise CliError(
                "allowed-filaments not in catalog: " + ", ".join(missing[:5])
            )

    try:
        run_pipeline(
            args.input_path,
            args.output_path,
            debug_dir=args.debug_dir,
            preset_path=args.preset_path,
            allowed_filaments=allowed_filaments,
            overrides=overrides,
        )
    except ValueError as exc:
        raise CliError(str(exc))

    summary = _format_summary(
        "run",
        args.input_path,
        args.output_path,
        args.debug_dir,
        preset,
        allowed_filaments,
    )
    print("\n".join(summary))


def _preview_command(args: argparse.Namespace) -> None:
    from .preview_runner import run_preview
    from .cli_overrides import apply_overrides, build_overrides, load_preset, parse_id_list, validate_overrides

    input_path = Path(args.input_path)
    if not input_path.exists():
        raise CliError(f"Input not found: {args.input_path}")
    if input_path.is_dir():
        raise CliError(f"Input is a directory, expected an image file: {args.input_path}")

    allowed_filaments = parse_id_list(args.allowed_filaments)
    overrides = build_overrides(args)
    try:
        validate_overrides(overrides)
    except ValueError as exc:
        raise CliError(str(exc))

    preset = apply_overrides(load_preset(args.preset_path), overrides)
    catalog_path = Path(
        preset.get("print", {}).get("filament_catalog", "filaments/default_catalog.json")
    )
    if not catalog_path.exists():
        raise CliError(
            f"Catalog not found: {catalog_path}",
            "Hint: run filamentcolors_sync to create data/filament_catalog_filamentcolors.json",
        )
    if allowed_filaments:
        missing = _find_missing_allowed(catalog_path, allowed_filaments)
        if missing:
            raise CliError(
                "allowed-filaments not in catalog: " + ", ".join(missing[:5])
            )

    try:
        run_preview(
            args.input_path,
            debug_dir=args.debug_dir,
            preset_path=args.preset_path,
            allowed_filaments=allowed_filaments,
            overrides=overrides,
        )
    except ValueError as exc:
        raise CliError(str(exc))

    summary = _format_summary(
        "preview",
        args.input_path,
        None,
        args.debug_dir,
        preset,
        allowed_filaments,
    )
    print("\n".join(summary))


def _filaments_command(args: argparse.Namespace) -> None:
    from src.tools.filaments_cli import (
        apply_limit_offset,
        filter_filaments,
        format_nearest_table,
        format_table,
        load_filament_catalog,
        nearest_filaments,
        parse_hex_color,
    )

    catalog_path = Path(args.catalog)
    if not catalog_path.exists():
        raise CliError(
            f"Catalog not found: {catalog_path}",
            "Hint: run filamentcolors_sync to create data/filament_catalog_filamentcolors.json",
        )
    catalog = load_filament_catalog(catalog_path)
    filtered = filter_filaments(
        catalog,
        search=args.search,
        td_min=args.td_min,
        td_max=args.td_max,
        include_missing_td=args.include_missing_td,
    )
    if args.nearest:
        try:
            target = parse_hex_color(args.nearest)
        except ValueError as exc:
            raise CliError(str(exc))
        nearest = nearest_filaments(filtered, target, args.top)
        print(format_nearest_table(nearest))
        print(f"Metric: LAB if available, else RGB; top={args.top}")
        return
    filtered = apply_limit_offset(filtered, limit=args.limit, offset=args.offset)
    print(format_table(filtered))


def _bundle_command(args: argparse.Namespace) -> None:
    from .bundle_runner import run_bundle
    from .cli_overrides import apply_overrides, build_overrides, load_preset, parse_id_list, validate_overrides

    input_path = Path(args.input_path)
    if not input_path.exists():
        raise CliError(f"Input not found: {args.input_path}")
    if input_path.is_dir():
        raise CliError(f"Input is a directory, expected an image file: {args.input_path}")

    allowed_filaments = parse_id_list(args.allowed_filaments)
    overrides = build_overrides(args)
    try:
        validate_overrides(overrides)
    except ValueError as exc:
        raise CliError(str(exc))

    preset = apply_overrides(load_preset(args.preset_path), overrides)
    catalog_path = Path(
        preset.get("print", {}).get("filament_catalog", "filaments/default_catalog.json")
    )
    if not catalog_path.exists():
        raise CliError(
            f"Catalog not found: {catalog_path}",
            "Hint: run filamentcolors_sync to create data/filament_catalog_filamentcolors.json",
        )
    if allowed_filaments:
        missing = _find_missing_allowed(catalog_path, allowed_filaments)
        if missing:
            raise CliError(
                "allowed-filaments not in catalog: " + ", ".join(missing[:5])
            )

    try:
        files = run_bundle(
            args.input_path,
            args.output_zip,
            debug_dir=args.debug_dir,
            preset_path=args.preset_path,
            allowed_filaments=allowed_filaments,
            overrides=overrides,
        )
    except ValueError as exc:
        raise CliError(str(exc))

    print(f"Bundle: {args.output_zip}")
    print("Files:")
    for name in files:
        print(f"- {name}")


def _hueforge_bundle_command(args: argparse.Namespace) -> None:
    from hueforge.core.bundle_runner import run_bundle_hueforge
    from .cli_overrides import apply_overrides, build_overrides, load_preset, parse_id_list, validate_overrides

    input_path = Path(args.input_path)
    if not input_path.exists():
        raise CliError(f"Input not found: {args.input_path}")
    if input_path.is_dir():
        raise CliError(f"Input is a directory, expected an image file: {args.input_path}")

    allowed_filaments = parse_id_list(args.allowed_filaments)
    overrides = build_overrides(args)
    try:
        validate_overrides(overrides)
    except ValueError as exc:
        raise CliError(str(exc))

    preset = apply_overrides(load_preset(args.preset_path), overrides)
    catalog_path = Path(
        preset.get("print", {}).get("filament_catalog", "filaments/default_catalog.json")
    )
    if not catalog_path.exists():
        raise CliError(
            f"Catalog not found: {catalog_path}",
            "Hint: run filamentcolors_sync to create data/filament_catalog_filamentcolors.json",
        )
    if allowed_filaments:
        missing = _find_missing_allowed(catalog_path, allowed_filaments)
        if missing:
            raise CliError(
                "allowed-filaments not in catalog: " + ", ".join(missing[:5])
            )

    try:
        files = run_bundle_hueforge(
            args.input_path,
            args.output_zip,
            debug_dir=args.debug_dir,
            preset_path=args.preset_path,
            allowed_filaments=allowed_filaments,
            overrides=overrides,
        )
    except ValueError as exc:
        raise CliError(str(exc))

    print(f"Bundle: {args.output_zip}")
    print("Files:")
    for name in files:
        print(f"- {name}")


def _stl_diagnostics_command(args: argparse.Namespace) -> None:
    from src.tools.stl_diagnostics import analyze_stl, format_report

    stl_path = Path(args.stl_path)
    if not stl_path.exists():
        raise CliError(f"STL not found: {args.stl_path}")
    metrics = analyze_stl(stl_path)
    print(format_report(metrics))

def _find_missing_allowed(catalog_path: Path, allowed_filaments: list[str]) -> list[str]:
    from src.print.filaments import load_catalog

    catalog = load_catalog(catalog_path)
    catalog_ids = {item["id"] for item in catalog.get("filaments", [])}
    return [fid for fid in allowed_filaments if fid not in catalog_ids]


def _format_summary(
    mode: str,
    input_path: str,
    output_path: str | None,
    debug_dir: str | None,
    preset: dict,
    allowed_filaments: list[str] | None,
) -> list[str]:
    palette = preset.get("palette", {})
    n_colors = palette.get("n_colors")
    if n_colors is None and "colors" in palette:
        n_colors = len(palette["colors"])
    print_cfg = preset.get("print", {})
    blend_depth = print_cfg.get("blend_depth")
    sequence_mode = print_cfg.get("sequence_mode")
    base_filament = print_cfg.get("base_filament_id")
    allowed_count = len(allowed_filaments) if allowed_filaments else 0

    lines = [
        f"Input: {input_path}",
        f"Debug dir: {debug_dir}",
        f"n_colors={n_colors} blend_depth={blend_depth} sequence_mode={sequence_mode} base_filament={base_filament} allowed_filaments_count={allowed_count}",
    ]
    if debug_dir:
        lines.append(f"Artifacts: {Path(debug_dir) / 'preview.png'}")
        lines.append(f"Artifacts: {Path(debug_dir) / 'palette_suggested.json'}")
        lines.append(f"Artifacts: {Path(debug_dir) / 'palette_assigned.json'}")
        lines.append(f"Artifacts: {Path(debug_dir) / 'layer_plan.json'}")
    if mode == "run" and output_path:
        lines.append(f"Output: {output_path}")
        lines.append(f"Output: {Path(output_path).with_suffix('.colorplan.txt')}")
    return lines


if __name__ == "__main__":
    main()
