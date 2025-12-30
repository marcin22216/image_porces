# DEVELOPMENT REPORT

## Iteration 1 — Project skeleton
Status: DONE
Tests: python3 -m pytest -q → PASS

## Iteration 2 — Image loading/saving
Status: DONE

komendy instalacji w venv:

python3 -m pip install pytest Pillow

testy:

python3 -m pytest -q → PASS (2 passed)

## Iteration 3 — Edge-preserving preprocessing
Status: DONE
komendy instalacji w venv:

python3 -m pip install numpy

testy:

python3 -m pytest -q → PASS

## Iteration 4 — Superpixel segmentation
Status: DONE
komendy instalacji w venv:

python3 -m pip install numpy

testy:

python3 -m pytest -q → PASS

## Iteration 5 — Merge small regions
Status: DONE
komendy instalacji w venv:

python3 -m pip install numpy

testy:

python3 -m pytest -q → PASS

## Iteration 6 — Palette mapping
Status: DONE
komendy instalacji w venv:

python3 -m pip install numpy

testy:

python3 -m pytest -q → PASS

## Iteration 7 — Height map generation
Status: DONE
komendy instalacji w venv:

python3 -m pip install numpy

testy:

python3 -m pytest -q → PASS

## Iteration 8 — Mesh generation
Status: DONE
komendy instalacji w venv:

python3 -m pip install numpy

testy:

python3 -m pytest -q → PASS

## Iteration 10 — CLI pipeline
Status: DONE
komendy instalacji w venv:

python3 -m pip install numpy Pillow

testy:

python3 -m pytest -q → PASS

## Iteration 10 — Canvas sizing (mm_per_pixel) + aspect ratio
Status: DONE
komendy instalacji w venv:

python3 -m pip install numpy Pillow

testy:

python3 -m pytest -q → PASS

Uwagi: mm_per_pixel jest przekazywane jawnie do generacji mesha.

## Iteration 10 — CLI import fix
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Border on base (heightmap expansion)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Colorplan export (STL + TXT)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Layer model (layers → mm conversion)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Translucency preview (TD simulation core)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Palette suggestion
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Palette to filament assignment
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Region recipe solver (one-click core)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — CLI pipeline v1 debug + preview + colorplan
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Colorplan global v1
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Global layer plan modes (manual/auto_palette)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — CLI preview command
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — FilamentColors.xyz sync + starter presets
Status: DONE
Tests: python3 -m pytest -q → PASS
Fix: FilamentColors uses hex_color field

## Extended — Filament catalog CLI
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Filament catalog CLI v2 (limit/offset/nearest)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — CLI overrides for presets
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — CLI overrides validation (manual/allowed)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — CLI UX errors + summaries
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — CLI bundle command
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — CLI input validation (directory)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Brand preset generator
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — LAB distance for color matching
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — LAB distance (RGB->LAB fallback)
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — FastAPI web wrapper
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — CLI v1 release prep
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Examples + license metadata
Status: DONE
Tests: python3 -m pytest -q → PASS

## Extended — Makefile quick commands
Status: DONE
Tests: not run (not required)

## Extended — FastAPI web wrapper deps fix
Status: DONE
Tests: python3 -m pytest -q → PASS

## Iteration 11 — Web UI thin wrapper
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 12 — UI live preview (debounce)
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

Audit Snapshot v1 created: AUDIT_REPORT_v1_2025-12-30.md
Foundation v1 formally closed after audit snapshot (AUDIT_REPORT_v1_2025-12-30.md).

## Iteration 13 — UI copy & status panel
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 14 — Manual UI test scenarios
Status: DONE
Tests: PYTHONPATH=. python3 -m src.app.main doctor → OK

## Iteration 15 — UI error states copy
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 16 — UI request summary
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 17 — UI manual test checklist
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 18 — UI result freshness
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 19 — UI payload details
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 20 — UI status states copy
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 21 — UI scope guardrails copy
Status: DONE
Tests: PYTHONPATH=. python3 -m pytest -q → PASS

## Iteration 22 — README status alignment
Status: DONE
Tests: PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. python3 -m pytest -q → PASS

UI: fixed stuck Rendering state by handling AbortError and ensuring latest-request-only state updates.
Tests: added regression test ensuring run_preview completes (timeout-guard) on pix1.png fixture.
Tools: added plan_audit.py to validate swap-by-layer plan heights and color IDs against canon.

## STL Z-axis analysis
- Files/functions:
  - src/app/pipeline.py: run_pipeline() builds height_layers, converts to height_map via layers_to_mm(), then height_map_to_mesh(); _write_ascii_stl() writes STL.
  - src/geom/mesh_generation.py: height_map_to_mesh() sets vertex Z from height_map[y, x] for each quad.
  - src/ops/height_map.py: generate_height_map() -> _layers_by_index() maps labels (region ids) to height_layers.
  - src/ops/layers_to_mm.py: layers_to_mm() converts height_layers to mm via base_layer_mm + layers * color_layer_mm.
  - src/ops/add_border.py: add_border() inserts base_height_mm around the height map edges.
- Z semantics (current):
  - Z is taken directly from height_map values (float32 mm) computed from label-based height_layers, then scaled by color_layer_mm and offset by base_layer_mm/base_height_mm.
  - Z is therefore a function of region labels (image segmentation), not a fixed layer stack count.
- Z flow (image → STL):
  image → preprocess/segment/merge → labels (int32 region ids) → generate_height_map(by_index) → height_layers
  → blend_depth scaling → layers_to_mm(base_layer_mm + layers * color_layer_mm) → add_border(base_height_mm)
  → height_map_to_mesh (Z = height_map[y,x]) → _write_ascii_stl
- Why STL height > 1 cm:
  - height_layers are derived from raw label indices (often large counts), then multiplied by color_layer_mm; this creates large Z values.
- Root cause in code (decision point):
  - src/ops/height_map.py:_layers_by_index() uses label ids directly as layer counts (labels * scale), which then propagate to Z via layers_to_mm().
- One-line conclusion:
  - Z is currently interpreted as a label-index-derived heightmap, not a constrained print layer stack.

## HueForge parity report (current vs intended)
A) Current outputs (artifacts + where generated)
- bundle.zip contents (src/app/bundle_runner.py:run_bundle): `<name>.stl`, `<name>.colorplan.txt`, `preview.png`, `palette_suggested.json`, `palette_assigned.json`, `layer_plan.json`, `config.effective.json`.
- STL geometry: src/app/pipeline.py:run_pipeline → src/geom/mesh_generation.py:height_map_to_mesh → src/app/pipeline.py:_write_ascii_stl.
- COLORPLAN v1: src/app/pipeline.py:_write_colorplan → src/print/colorplan_export.py:export_colorplan_txt (global START/CHANGE only).
- XY-bearing artifacts exist only as debug outputs: `labels.png`, `height.png`, `height_layers.npy`, `height_mm.npy` in debug dir (src/app/pipeline.py:_write_debug). These are not used by the plan or STL.
- Output contract has no per-layer XY masks, no per-color STL set, and no toolpath with spatial regions.

B) Intended behavior summary (from docs/reference/hueforge_documentation.md)
- Per-pixel color decomposition mapped to available filament palette.
- Each color layer is a spatially varying thickness map (not a full-plane fill).
- Image is “drawn” by stacking multiple color layers with controlled thickness per pixel.
- Mixing is optical (light transmission), not pigment mixing; order and thickness matter.
- Base layer provides uniform backing; colored content begins above base.
- Layer thickness follows print-layer grid (typically 0.1–0.2 mm steps).
- Per-layer geometry corresponds to image regions (XY), not just global swaps.
- Output requires a carrier of XY information for each layer/color (masks or geometry).

C) Gap analysis (Required → Present? → Evidence)
- Per-layer XY mask/geometry per color → No → bundle.zip includes only one STL + global colorplan; no per-layer masks.
- Per-pixel thickness maps per color → No → only single height_map used for one STL; debug maps not tied to per-color layers.
- Toolpath with spatial swaps (G-code or per-region toolchanges) → No → COLORPLAN v1 is global START/CHANGE only.
- Optical mixing via TD is simulated → Yes → src/sim/td_preview.py and preview.png.
- Palette assignment to real filament IDs → Yes → src/print/filament_assignment.py, palette_assigned.json.

D) Critical missing pieces (minimum to enable HueForge-like behavior)
- A print-time carrier for XY regions per color layer (multi-STL masks or spatial toolpath).
- Per-color or per-layer thickness maps that “draw” the image in XY (not a single global height_map).
- A plan format that connects XY regions to specific filaments per layer (beyond global START/CHANGE).
- A consistent mapping from image pixels → per-color layer thickness → exported geometry/toolpath.

E) Decision inputs (must be resolved next)
- Do we export multi-STL masks per color/layer, or emit a single toolpath with spatial toolchanges?
- Should the plan remain global (START/CHANGE) or encode per-layer/region assignments?
- What is the canonical artifact for per-pixel thickness per color (depth maps vs per-layer masks)?

## Multi-STL export feasibility (no G-code)
A) Goal statement
- No G-code generation; slicer handles toolpaths and filament assignment. We export geometry masks as multiple STLs.

B) Variant A: per-color STL
- Required data: per-pixel color assignment (which filament owns each XY), plus a thickness map for that color.
- Present data: paletted image exists in pipeline (`paletted` in `src/app/pipeline.py`), palette assignment exists (`palette_assigned.json`); labels map regions but are not per-color.
- Missing data/artifacts: no persisted per-pixel color index in bundle; no per-color height maps exported; bundle has only one STL.
- Export path: build N height maps by masking the global height map with per-color masks, then reuse `height_map_to_mesh()` to emit N STLs.
- Proof of image in slicer: slicer assigns each STL to a filament; overlapping XY masks yield visible colored image in preview.

C) Variant B: per-layer STL
- Required data: per-pixel layer count or binary mask for each layer index (k), plus a global plan mapping layer index → filament.
- Present data: `height_layers` and `height_mm` are computed in pipeline (`src/app/pipeline.py`) and written to debug dir; `layer_plan.json` is generated but contains only global Z/filament (no XY).
- Missing data/artifacts: bundle does not include `height_layers.npy`/`height_mm.npy`; no per-layer masks/STLs are exported.
- Export path: for each k, build mask = `height_layers >= k` (or equivalent) and create a height map for that layer; use `height_map_to_mesh()` to export per-layer STL.
- Proof of image in slicer: slicer assigns each layer STL to the matching filament ID from `layer_plan.json`, producing a stack that encodes XY patterns.

D) Recommendation for next implementation iteration
- Choose Variant B (per-layer STL) as the most feasible next step.
- Rationale:
  1) `height_layers` already exists and is bounded to 0..7, matching the canon grid.
  2) `layer_plan.json` already provides global filament order per layer (no new plan format needed).
  3) Per-layer STLs align with existing height model without needing per-color thickness decomposition.

E) Minimal acceptance criteria for next iteration
- bundle.zip contains N per-layer STL files with deterministic names.
- Each STL height is bounded to <= 0.88 mm.
- `layer_plan.json` references each layer index used in the STLs.
- Slicer can assign one filament per STL and preview shows the intended XY image.
- No changes to G-code generation (none produced).

Bundle: export per-layer STL masks (Variant B) for slicer-based filament assignment; enables XY image without G-code.

## Iteration 23 — Claude plan doc alignment
Status: DONE
Tests: python3 -m pytest -q → PASS

Docs: aligned README and HueForge reference docs to the Claude plan, and recorded the migration phase in ROADMAP.md.

## Iteration 24 — Repo hygiene + docs relocation
Status: DONE
Tests: python3 -m pytest -q → PASS

Docs: moved HueForge reference files into docs/, added docs/README.md and docs/MIGRATION.md, and updated README/REPORT links.
Repo: cleaned generated artifacts (debug/, bundle.zip, result.zip, bundle_out/, egg-info, __pycache__) and expanded .gitignore.

## Iteration 25 — Hueforge scaffold shims
Status: DONE
Tests: python3 -m pytest -q → PASS

Scaffold: added hueforge/ package layout and minimal shims for scale, mesh, and colorplan; added import test.

## Iteration 26 — Migrate preprocessing modules to hueforge/preprocessing
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved scale/preprocess/segment/merge implementations into hueforge/preprocessing and replaced legacy src/ops modules with shims.

## Iteration 27 — Migrate palette mapping to hueforge/mapping
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved palette mapping into hueforge/mapping and replaced src/ops/palette_mapping with a shim; added equivalence test.
