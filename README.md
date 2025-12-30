# Image-to-3D Layered Relief Generator

## What is this?
This tool turns a normal image into a multilayer 3D print: an STL file plus a simple color change plan.

## What problem does it solve?
With multi-color filament, you can print a relief where color and light depth come from stacked layers. The preview shows how translucency might look, and the output gives you a basic plan for changing filament at each layer.

## Direction (Claude plan) and migration status
Target direction: a modular HueForge-style codebase with clear module boundaries and testable units.

Target package layout (planned):
- hueforge/core: config, image loading, exceptions
- hueforge/preprocessing: resizing, linearization, filters, analysis
- hueforge/palette: palette management, transmission, calibration
- hueforge/gamut: gamut generation, KD-tree lookup, optimization, cache
- hueforge/mapping: pixel mapping, dithering, smoothing, edge handling
- hueforge/geometry: height maps, mesh generation, layer stacking
- hueforge/export: STL writers, multi-STL export, metadata, preview
- hueforge/physics: light simulation, Beer-Lambert, mixing
- hueforge/utils: validators, math helpers, logging

Current repo layout (legacy v1, still active):
- src/app: CLI and pipeline orchestration
- src/ops: image preprocessing + segmentation operations
- src/solver: layer recipe solving for preview
- src/geom: mesh generation
- src/print: colorplan + filament catalog tools
- src/sim: TD-based preview
- src/web: thin UI wrapper

Migration note: legacy CLI remains the entry point while the HueForge-style layout is introduced incrementally. Documentation below separates legacy behavior from target architecture.

## Docs
- `docs/reference/hueforge_documentation.md` — intended HueForge-like behavior (conceptual).
- `docs/reference/hueforge_technical_process.md` — step-by-step technical process (conceptual).
- `docs/MIGRATION.md` — mapping from legacy `src/` to target `hueforge/`.
- `docs/legacy/STRUKTURA.md` — legacy tree snapshot.

## Quick start (5 minutes)
Installation:
1) Create a virtual environment (optional) and activate it.
2) Install dependencies:
   `python3 -m pip install -e .`

## Quick commands
- `make doctor`
- `make sync-filaments`
- `make preview IMG=examples/input.png`
- `make bundle IMG=examples/input.png OUT=examples/output.zip`

Preview command:
`python3 -m src.app.main preview --in INPUT_IMAGE --debug preview_out`

Run command:
`python3 -m src.app.main run --in INPUT_IMAGE --out output.stl --debug run_out`

Filament catalog command:
`python3 -m src.app.main filaments --catalog PATH --search PLA`
Nearest colors example:
`python3 -m src.app.main filaments --catalog PATH --nearest "#ff8800" --top 10`
Nearest uses LAB if available (else RGB).
Limit/offset example:
`python3 -m src.app.main filaments --catalog PATH --limit 50 --offset 100`

Overrides examples:
Preview (auto palette):
`python3 -m src.app.main preview --in INPUT_IMAGE --debug preview_out --n-colors 3 --blend-depth 1.2`
Preview (manual sequence):
`python3 -m src.app.main preview --in INPUT_IMAGE --debug preview_out --sequence-mode manual --layer-sequence-ids white,black,red`
Run with allowed filaments:
`python3 -m src.app.main run --in INPUT_IMAGE --out output.stl --debug run_out --allowed-filaments white,black`

Bundle example:
`python3 -m src.app.main bundle --in INPUT_IMAGE --out output.zip`

## Brand presets
Generate a preset pack for a filament brand:
`python3 -m src.tools.preset_gen --catalog data/filament_catalog_filamentcolors.json --manufacturer "BrandName" --out presets/brand`

## Examples
See `examples/README.md`.

## Web server (optional)
Run server:
`python3 -m src.web.server`
or
`uvicorn src.web.server:app --host 0.0.0.0 --port 8000`

## WEB / UI quick start
1) Start the server:
   `python3 -m src.web.server`
2) Open:
   `http://127.0.0.1:8000/ui`
3) Upload an image, set `n_colors` and `blend_depth` if needed, then click Generate preview.
4) Adjusting `n_colors` or `blend_depth` triggers live preview after a short debounce.
The status panel shows the selected file, current parameter values, and the request state.
Idle means no request is running, Rendering means a request is in progress, Done means preview is ready, and Error indicates failure.
The UI includes a Status states (how to interpret) block that summarizes when each state appears.
/ui is a thin wrapper around POST /preview only.
It does not run /bundle or generate STL/colorplan; use bundle/CLI for those outputs.
Error means the preview request failed and no STL or colorplan is generated.
Details are visible in the Status panel message.
The status panel also shows a Request summary with endpoint, method, payload, and the current field values.
Use it to verify exactly what /ui sends without DevTools.
Included/omitted fields show which multipart values will be sent based on current inputs.
The /ui screen includes a manual test checklist with action/expect items for quick verification.
Last updated shows when the last preview request ended, and the freshness line indicates whether the preview matches current inputs.
For repeatable UI checks, see `manual_tests/README.md`.

Preview:
`curl -F "file=@examples/input.png" -F "catalog=data/filament_catalog_filamentcolors.json" http://127.0.0.1:8000/preview --output preview.png`

Bundle:
`curl -F "file=@examples/input.png" -F "catalog=data/filament_catalog_filamentcolors.json" http://127.0.0.1:8000/bundle --output bundle.zip`

## Preview vs Run (important)
Preview = fast, visual check. It writes preview images and JSON files, but does not create STL or colorplan.
Run = full output. It creates STL + .colorplan.txt for printing.

## Input / Output
Input:
- One image file (PNG/JPG recommended)

Output:
- `preview.png` (when using preview)
- `output.stl`
- `output.colorplan.txt`

## Colorplan.txt – how to read it
The file is a simple layer-by-layer plan:
- `START` sets the base layer filament
- `CHANGE` lines list: layer index, Z height in mm, filament id

Example idea:
Layer 0 uses the base filament, then each next layer switches as listed in the plan.

## Typical workflows
“I have 4 colors”
1) Run preview to see the look.
2) Run full output to get STL + colorplan.
3) Print and change filament when the plan says.

“I have different colors than the program suggests”
1) Use `--allowed-filaments` to limit choices to what you own.
2) Run preview and check the result.
3) Run full output when it looks OK.

## Limitations (honest)
- Preview is a fast approximation, not a perfect print simulation.
- The colorplan is a global layer plan (not per-region yet).

## Stability & roadmap
- Legacy CLI: stable (v1 pipeline)
- Web wrapper + /ui: available (preview-only thin wrapper)
- Architecture migration to Claude plan: in progress

## Project status
Foundation v1 is complete. Core pipeline, CLI, and the web wrapper are stable.
The next phase is a structural migration to the Claude plan modules without breaking the CLI.
Docs are being updated first to avoid confusion between legacy and target behavior.

## User Contract (v1)
- Inputs: one image file (PNG/JPG recommended); WEB upload limit is 20MB per request; CLI accepts any Pillow-readable image file.
- Main user parameters: `n_colors` (palette size), `blend_depth` (layer scaling), and output size in mm via `--width-mm` / `--height-mm` (CLI only).
- Preview does: runs the full preview pipeline and outputs `preview.png` plus debug artifacts; it does not generate STL or colorplan.
- Bundle does: creates a ZIP with STL, `.colorplan.txt`, preview image, and effective config; it does not create G-code or slicer-specific files.
- Explicit limitations: no G-code output, no AI/prompt generation, no session storage, and WEB/UI remains a thin wrapper over CLI behavior.

## Common failure modes
- Preview is slow: CPU-heavy preprocessing (bilateral), segmentation (SLIC), and layer solving run on full-resolution images.
- Image is rejected: input path is missing or is a directory (CLI), file exceeds 20MB (WEB), or the image cannot be decoded by Pillow.
- Colors do not match the screen: palette is constrained by filament catalog entries, matching uses LAB/RGB approximations, and preview simulates translucency (TD) rather than exact print appearance.

## Roadmap (short)
- UI is available at /ui (preview-only)
- Architecture migration (Claude plan) is in progress

## Optional: FilamentColors.xyz catalog
You can download a larger filament catalog from FilamentColors.xyz.
Niektóre swatche w API mogą być niekompletne; są pomijane.

Sync command:
`python3 -m src.tools.filamentcolors_sync`

This creates `data/filament_catalog_filamentcolors.json`. Use a preset that points to it (for example `presets/default_4_auto.json`).

HueForge library TD sync (updates `td_mm` only):
`python3 -m src.tools.hueforge_library_sync --hueforge hueforge_filament_library.json --target filaments/default_catalog.json --out filaments/default_catalog.synced.json`

## Troubleshooting
- “Input not found”: check the path passed to `--in`.
- “Catalog not found”: run `python3 -m src.tools.filamentcolors_sync`.
- Manual mode requires `--layer-sequence-ids`.
