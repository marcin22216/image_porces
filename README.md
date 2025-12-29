# Image-to-3D Layered Relief Generator

## What is this?
This tool turns a normal image into a multilayer 3D print: an STL file plus a simple color change plan.

## What problem does it solve?
With multi-color filament, you can print a relief where color and light depth come from stacked layers. The preview shows how translucency might look, and the output gives you a basic plan for changing filament at each layer.

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
- CLI: stable
- GUI/Web: planned

## Roadmap (short)
- GUI
- Live preview

## Optional: FilamentColors.xyz catalog
You can download a larger filament catalog from FilamentColors.xyz.
Niektóre swatche w API mogą być niekompletne; są pomijane.

Sync command:
`python3 -m src.tools.filamentcolors_sync`

This creates `data/filament_catalog_filamentcolors.json`. Use a preset that points to it (for example `presets/default_4_auto.json`).

## Troubleshooting
- “Input not found”: check the path passed to `--in`.
- “Catalog not found”: run `python3 -m src.tools.filamentcolors_sync`.
- Manual mode requires `--layer-sequence-ids`.
