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

## Iteration 28 — Migrate height model modules to hueforge/geometry
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved height_map, layers_to_mm, and add_border into hueforge/geometry and replaced legacy src/ops modules with shims; added equivalence tests.

## Iteration 29 — Migrate TD preview core to hueforge/physics
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved td_preview simulate_stack into hueforge/physics and replaced src/sim/td_preview with a shim; added equivalence test.

## Iteration 30 — Migrate mesh generation to hueforge/geometry
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved mesh_generation into hueforge/geometry, replaced src/geom/mesh_generation with a shim, and redirected hueforge/geometry/mesh.py to the new module; added equivalence test.

## Iteration 31 — Migrate colorplan export to hueforge/export
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved colorplan export into hueforge/export, replaced src/print/colorplan_export with a shim, and redirected hueforge/export/colorplan.py to the new module; added equivalence test.

## Iteration 32 — Hueforge shadow pipeline + hueforge-bundle CLI
Status: DONE
Tests: python3 -m pytest -q → PASS

Shadow path: added hueforge/core pipeline + bundle runner and new hueforge-bundle CLI command; added smoke test for zip output via hueforge path (uses width/height overrides to keep runtime short).

## Iteration 33 — Speed up hueforge-bundle smoke test
Status: DONE
Tests: python3 -m pytest -q → PASS

Tests: added tiny PNG fixture for hueforge-bundle smoke test to reduce runtime; pix1.png remains unchanged.

## Iteration 34 — Migrate palette suggestion to hueforge/palette
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved suggest_palette into hueforge/palette, replaced src/ops/palette_suggestion with a shim, and updated hueforge shadow pipeline to use the hueforge implementation; added equivalence test.

## Iteration 35 — Migrate filament assignment to hueforge/print
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved filament assignment into hueforge/print, replaced src/print/filament_assignment with a shim, and updated hueforge shadow pipeline to use the hueforge implementation; added equivalence test.

## Iteration 36 — Migrate filament catalog loader to hueforge/print
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved filament catalog loader into hueforge/print, replaced src/print/filaments with a shim, and updated hueforge shadow pipeline to use the hueforge implementation; added equivalence test.

## Iteration 37 — Migrate solver region_recipe to hueforge/solver
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved region_recipe solver into hueforge/solver, replaced src/solver/region_recipe with a shim, updated hueforge shadow pipeline to use hueforge solver, and added equivalence test.

## Iteration 38 — Migrate color distance utilities to hueforge
Status: DONE
Tests: python3 -m pytest -q → PASS

Migration: moved src/color/color_distance.py to hueforge/utils/color_distance.py, updated filament_assignment imports, and replaced src/color/color_distance with a shim; added equivalence tests.

## Iteration 39 — Add HueForge filament library adapter (td preserved 1:1)
Status: DONE
Tests: python3 -m pytest -q → PASS

Data adapter: load_catalog now recognizes HueForge library JSON (metadata + entries), maps hexCode → rgb and td → td_mm 1:1, validates inputs, and keeps legacy catalog support; added loader tests and fixture.

## Iteration 41 — Hueforge bundle artifacts verification (tiny fixture)
Status: DONE
Tests: python3 -m pytest -q → PASS

Command:
`python3 -m src.app.main hueforge-bundle --in tests/fixtures/tiny.png --out artifacts/hueforge_bundle_smoke/out.zip --debug artifacts/hueforge_bundle_smoke/dbg --width-mm 10 --height-mm 1`

Directory listing (recursive):
```
artifacts/hueforge_bundle_smoke:
out.zip
```

Directory listing with sizes:
```
artifacts/hueforge_bundle_smoke:
razem 20K
-rw-rw-r-- 1 marcin marcin 18K gru 30 14:49 out.zip
```

Total size:
```
24K	artifacts/hueforge_bundle_smoke
```

Zip contents (sizes inside archive):
```
  Length      Date    Time    Name
---------  ---------- -----   ----
   571916  2025-12-30 14:49   out.stl
      154  2025-12-30 14:49   out.colorplan.txt
       98  2025-12-30 14:49   preview.png
      106  2025-12-30 14:49   palette_suggested.json
       58  2025-12-30 14:49   palette_assigned.json
      189  2025-12-30 14:49   layer_plan.json
      860  2025-12-30 14:49   config.effective.json
---------                     -------
   573381                     7 files
```

STL sizes:
- `artifacts/hueforge_bundle_smoke/out.zip:out.stl` → 571,916 bytes
- Per-layer STL files: none present in this bundle

Artifact paths:
- Main STL: `artifacts/hueforge_bundle_smoke/out.zip:out.stl`
- Preview: `artifacts/hueforge_bundle_smoke/out.zip:preview.png`
- Colorplan: `artifacts/hueforge_bundle_smoke/out.zip:out.colorplan.txt`
- metadata.json: not present (config file present at `artifacts/hueforge_bundle_smoke/out.zip:config.effective.json`)

colorplan.txt (first 60 lines):
```
COLORPLAN v1
UNITS mm
LAYER_INDEXING zero_based
BASE_LAYER_MM 0.320000
COLOR_LAYER_MM 0.080000
TOTAL_LAYERS 2
START 0 0.320000 blue
CHANGE 1 0.400000 base
```

config.effective.json (selected fields):
- canvas.target_width_mm: 10.0
- canvas.target_height_mm: 1.0
- print.filament_catalog: filaments/default_catalog.json
- print.base_layer_mm: 0.0
- print.color_layer_mm: 0.2
- print.blend_depth: 1.0

pix1.png run: skipped to avoid large outputs (previous reports mention potential ~1GB artifacts).

## Iteration 42 — STL diagnostics tool (offline geometry metrics)
Status: DONE
Tests: python3 -m pytest -q → PASS

Tool: added `src/tools/stl_diagnostics.py` and CLI `python3 -m src.app.main stl-diagnostics --stl <path>`.

Example output (artifacts/hueforge_bundle_smoke/out.stl):
```
STL path: artifacts/hueforge_bundle_smoke/out.stl
Format: ascii
Size (bytes): 571916
Triangles: 2306
Bounding box min: (0.000000, 0.000000, 0.000000)
Bounding box max: (1.000000, 1.000000, 0.000000)
Dimensions: (1.000000, 1.000000, 0.000000)
```

## Iteration 43 — Hueforge bundle call-chain ground truth (grep + code excerpts)
Status: DONE
Tests: python3 -m pytest -q → PASS

Grep outputs:
- `grep -R "hueforge-bundle" -n src hueforge`
```
grep: src/app/__pycache__/main.cpython-311.pyc: plik binarny pasuje do wzorca
src/app/main.py:76:        "hueforge-bundle", help="Create ZIP bundle using hueforge pipeline"
src/app/main.py:125:        if args.command == "hueforge-bundle":
```

- `grep -R "def .*height" -n src hueforge`
```
src/app/pipeline.py:269:def _height_to_rgb(height_map: np.ndarray) -> np.ndarray:
hueforge/core/pipeline.py:275:def _height_to_rgb(height_map: np.ndarray) -> np.ndarray:
hueforge/preprocessing/preprocess_edge_preserving.py:82:def _resize_nearest(image: np.ndarray, height: int, width: int) -> np.ndarray:
hueforge/preprocessing/scale.py:58:def _resize_image(image: np.ndarray, width: int, height: int) -> np.ndarray:
hueforge/geometry/layers_to_mm.py:19:def _validate_layers(height_layers: np.ndarray) -> None:
hueforge/geometry/height_map.py:8:def generate_height_map(labels: np.ndarray, **params) -> np.ndarray:
hueforge/geometry/mesh_generation.py:15:def height_map_to_mesh(height_map: np.ndarray, mm_per_pixel: float) -> Mesh:
hueforge/geometry/mesh_generation.py:109:def _validate_height_map(height_map: np.ndarray) -> None:
hueforge/geometry/add_border.py:33:def _validate_height(height: np.ndarray) -> None:
```

- `grep -R "height_map" -n src hueforge`
```
grep: src/ops/__pycache__/height_map.cpython-311.pyc: plik binarny pasuje do wzorca
src/ops/height_map.py:1:from hueforge.geometry.height_map import generate_height_map
src/ops/height_map.py:3:__all__ = ["generate_height_map"]
grep: src/app/__pycache__/pipeline.cpython-311.pyc: plik binarny pasuje do wzorca
src/app/pipeline.py:10:from src.geom.mesh_generation import Mesh, height_map_to_mesh
src/app/pipeline.py:11:from src.ops.height_map import generate_height_map
src/app/pipeline.py:76:    height_layers = generate_height_map(merged_labels, **preset["height_map"])
src/app/pipeline.py:95:    height_map = layers_to_mm(height_layers, base_layer_mm, color_layer_mm)
src/app/pipeline.py:98:    height_map = add_border(height_map, border_mm, mm_per_pixel, base_height_mm)
src/app/pipeline.py:110:        mesh = height_map_to_mesh(height_map, mm_per_pixel=mm_per_pixel)
src/app/pipeline.py:130:            layer_mesh = height_map_to_mesh(layer_map, mm_per_pixel=mm_per_pixel)
src/app/pipeline.py:156:            height_map=height_map,
src/app/pipeline.py:218:    height_map: np.ndarray,
src/app/pipeline.py:232:    save_image(_array_to_image(_height_to_rgb(height_map)), path / "height.png")
src/app/pipeline.py:237:    np.save(path / "height_mm.npy", height_map)
src/app/pipeline.py:269:def _height_to_rgb(height_map: np.ndarray) -> np.ndarray:
src/app/pipeline.py:270:    max_height = float(np.max(height_map)) if height_map.size else 0.0
src/app/pipeline.py:272:        scaled = np.zeros(height_map.shape, dtype=np.uint8)
src/app/pipeline.py:274:        scaled = np.rint(height_map / max_height * 255.0).astype(np.uint8)
grep: src/geom/__pycache__/mesh_generation.cpython-311.pyc: plik binarny pasuje do wzorca
grep: hueforge/core/__pycache__/pipeline.cpython-311.pyc: plik binarny pasuje do wzorca
src/geom/mesh_generation.py:1:from hueforge.geometry.mesh_generation import Mesh, height_map_to_mesh
src/geom/mesh_generation.py:3:__all__ = ["Mesh", "height_map_to_mesh"]
hueforge/core/pipeline.py:11:from hueforge.geometry.height_map import generate_height_map
hueforge/core/pipeline.py:13:from hueforge.geometry.mesh_generation import Mesh, height_map_to_mesh
hueforge/core/pipeline.py:78:    height_layers = generate_height_map(merged_labels, **preset["height_map"])
hueforge/core/pipeline.py:97:    height_map = layers_to_mm(height_layers, base_layer_mm, color_layer_mm)
hueforge/core/pipeline.py:100:    height_map = add_border(height_map, border_mm, mm_per_pixel, base_height_mm)
hueforge/core/pipeline.py:114:        mesh = height_map_to_mesh(height_map, mm_per_pixel=mm_per_pixel)
hueforge/core/pipeline.py:134:            layer_mesh = height_map_to_mesh(layer_map, mm_per_pixel=mm_per_pixel)
hueforge/core/pipeline.py:160:            height_map=height_map,
hueforge/core/pipeline.py:224:    height_map: np.ndarray,
hueforge/core/pipeline.py:238:    save_image(_array_to_image(_height_to_rgb(height_map)), path / "height.png")
hueforge/core/pipeline.py:243:    np.save(path / "height_mm.npy", height_map)
hueforge/core/pipeline.py:275:def _height_to_rgb(height_map: np.ndarray) -> np.ndarray:
hueforge/core/pipeline.py:276:    max_height = float(np.max(height_map)) if height_map.size else 0.0
hueforge/core/pipeline.py:278:        scaled = np.zeros(height_map.shape, dtype=np.uint8)
hueforge/core/pipeline.py:280:        scaled = np.rint(height_map / max_height * 255.0).astype(np.uint8)
grep: hueforge/geometry/__pycache__/height_map.cpython-311.pyc: plik binarny pasuje do wzorca
hueforge/geometry/height_map.py:8:def generate_height_map(labels: np.ndarray, **params) -> np.ndarray:
hueforge/geometry/height_map.py:68:    height_map = np.zeros(labels.shape, dtype=np.int32)
hueforge/geometry/height_map.py:73:        height_map[labels == label] = int(round(value))
hueforge/geometry/height_map.py:74:    return height_map
grep: hueforge/geometry/__pycache__/mesh_generation.cpython-311.pyc: plik binarny pasuje do wzorca
grep: hueforge/geometry/__pycache__/mesh.cpython-311.pyc: plik binarny pasuje do wzorca
hueforge/geometry/mesh_generation.py:15:def height_map_to_mesh(height_map: np.ndarray, mm_per_pixel: float) -> Mesh:
hueforge/geometry/mesh_generation.py:16:    _validate_height_map(height_map)
hueforge/geometry/mesh_generation.py:20:    heights = height_map.astype(np.float32, copy=False)
hueforge/geometry/mesh_generation.py:109:def _validate_height_map(height_map: np.ndarray) -> None:
hueforge/geometry/mesh_generation.py:110:    if height_map.dtype != np.float32:
hueforge/geometry/mesh_generation.py:111:        raise TypeError("height_map must be float32")
hueforge/geometry/mesh_generation.py:112:    if height_map.ndim != 2:
hueforge/geometry/mesh_generation.py:113:        raise ValueError("height_map must have shape (H, W)")
hueforge/geometry/mesh_generation.py:114:    if not np.isfinite(height_map).all():
hueforge/geometry/mesh_generation.py:115:        raise ValueError("height_map must be finite")
hueforge/geometry/mesh_generation.py:116:    if np.any(height_map < 0):
hueforge/geometry/mesh_generation.py:117:        raise ValueError("height_map must be >= 0")
hueforge/geometry/mesh.py:1:from hueforge.geometry.mesh_generation import Mesh, height_map_to_mesh
hueforge/geometry/mesh.py:3:__all__ = ["height_map_to_mesh", "Mesh"]
```

- `grep -R -E "write_stl|stl" -n src hueforge`
```
grep: src/app/__pycache__/pipeline.cpython-311.pyc: plik binarny pasuje do wzorca
grep: src/app/__pycache__/main.cpython-311.pyc: plik binarny pasuje do wzorca
src/app/main.py:94:    stl_diag_parser = subparsers.add_parser(
src/app/main.py:95:        "stl-diagnostics", help="Report STL size/triangles/bounds"
src/app/main.py:97:    stl_diag_parser.add_argument("--stl", dest="stl_path", required=True)
src/app/main.py:128:        if args.command == "stl-diagnostics":
src/app/main.py:129:            _stl_diagnostics_command(args)
src/app/main.py:388:def _stl_diagnostics_command(args: argparse.Namespace) -> None:
src/app/main.py:389:    from src.tools.stl_diagnostics import analyze_stl, format_report
src/app/main.py:391:    stl_path = Path(args.stl_path)
src/app/main.py:392:    if not stl_path.exists():
src/app/main.py:393:        raise CliError(f"STL not found: {args.stl_path}")
src/app/main.py:394:    metrics = analyze_stl(stl_path)
src/app/pipeline.py:111:        _write_ascii_stl(mesh, output_path)
src/app/pipeline.py:131:            layer_name = f"layer_{layer_index:02d}.stl"
src/app/pipeline.py:132:            _write_ascii_stl(layer_mesh, str(output_dir / layer_name))
src/app/pipeline.py:136:                    "stl": layer_name,
src/app/pipeline.py:141:            layer_plan["stl_layers"] = per_layer
src/app/pipeline.py:289:def _write_ascii_stl(mesh: Mesh, path: str) -> None:
src/app/bundle_runner.py:27:        output_stl = temp_path / f"{base_name}.stl"
src/app/bundle_runner.py:33:            str(output_stl),
src/app/bundle_runner.py:44:        layer_stls = sorted(temp_path.glob("layer_*.stl"))
src/app/bundle_runner.py:46:            output_stl,
src/app/bundle_runner.py:47:            output_stl.with_suffix(".colorplan.txt"),
src/app/bundle_runner.py:54:        required.extend(layer_stls)
grep: src/app/__pycache__/bundle_runner.cpython-311.pyc: plik binarny pasuje do wzorca
grep: src/tools/__pycache__/stl_diagnostics.cpython-311.pyc: plik binarny pasuje do wzorca
grep: hueforge/core/__pycache__/pipeline.cpython-311.pyc: plik binarny pasuje do wzorca
grep: src/tools/stl_diagnostics.py:9:def analyze_stl(path: Path) -> Dict[str, object]:
src/tools/stl_diagnostics.py:132:    parser.add_argument("--stl", required=True)
src/tools/stl_diagnostics.py:134:    metrics = analyze_stl(Path(args.stl))
hueforge/core/pipeline.py:31:    output_stl_path: str,
hueforge/core/pipeline.py:115:        _write_ascii_stl(mesh, output_stl_path)
hueforge/core/pipeline.py:117:            output_stl_path,
hueforge/core/pipeline.py:128:        output_dir = Path(output_stl_path).parent
hueforge/core/pipeline.py:135:            layer_name = f"layer_{layer_index:02d}.stl"
hueforge/core/pipeline.py:136:            _write_ascii_stl(layer_mesh, str(output_dir / layer_name))
hueforge/core/pipeline.py:140:                    "stl": layer_name,
hueforge/core/pipeline.py:145:            layer_plan["stl_layers"] = per_layer
hueforge/core/pipeline.py:295:def _write_ascii_stl(mesh: Mesh, path: str) -> None:
hueforge/core/bundle_runner.py:29:        output_stl = temp_path / f"{base_name}.stl"
hueforge/core/bundle_runner.py:35:            str(output_stl),
hueforge/core/bundle_runner.py:46:        layer_stls = sorted(temp_path.glob("layer_*.stl"))
hueforge/core/bundle_runner.py:48:            output_stl,
hueforge/core/bundle_runner.py:49:            output_stl.with_suffix(".colorplan.txt"),
hueforge/core/bundle_runner.py:56:        required.extend(layer_stls)
hueforge/core/__pycache__/bundle_runner.cpython-311.pyc: plik binarny pasuje do wzorca
grep: hueforge/export/__pycache__/colorplan_export.cpython-311.pyc: plik binarny pasuje do wzorca
hueforge/export/colorplan_export.py:8:    stl_path: Path,
hueforge/export/colorplan_export.py:18:    output_path = stl_path.with_suffix(".colorplan.txt")
```

- `grep -R "layer_plan" -n src hueforge`
```
grep: src/app/__pycache__/pipeline.cpython-311.pyc: plik binarny pasuje do wzorca
grep: src/app/__pycache__/main.cpython-311.pyc: plik binarny pasuje do wzorca
src/app/main.py:432:        lines.append(f"Artifacts: {Path(debug_dir) / 'layer_plan.json'}")
src/app/pipeline.py:108:    layer_plan = _layer_plan(base_filament_id, layer_sequence_ids, total_layers, base_layer_mm, color_layer_mm)
src/app/pipeline.py:137:                    "filament": layer_plan["layers"][layer_index]["filament_id"],
src/app/pipeline.py:141:            layer_plan["stl_layers"] = per_layer
src/app/pipeline.py:162:            layer_plan=layer_plan,
src/app/pipeline.py:224:    layer_plan: Optional[Dict[str, Any]] = None,
src/app/pipeline.py:253:    if layer_plan is not None:
src/app/pipeline.py:254:        (path / "layer_plan.json").write_text(
src/app/pipeline.py:255:            json.dumps(layer_plan, indent=2),
src/app/pipeline.py:395:    plan = _layer_plan(
src/app/pipeline.py:426:def _layer_plan(
src/app/bundle_runner.py:51:            debug_path / "layer_plan.json",
grep: src/app/__pycache__/bundle_runner.cpython-311.pyc: plik binarny pasuje do wzorca
grep: hueforge/core/__pycache__/pipeline.cpython-311.pyc: plik binarny pasuje do wzorca
grep: hueforge/core/__pycache__/bundle_runner.cpython-311.pyc: plik binarny pasuje do wzorca
hueforge/core/pipeline.py:110:    layer_plan = _layer_plan(
hueforge/core/pipeline.py:141:                    "filament": layer_plan["layers"][layer_index]["filament_id"],
hueforge/core/pipeline.py:145:            layer_plan["stl_layers"] = per_layer
hueforge/core/pipeline.py:166:            layer_plan=layer_plan,
hueforge/core/pipeline.py:169:    return {"layer_plan": layer_plan}
hueforge/core/pipeline.py:230:    layer_plan: Optional[Dict[str, Any]] = None,
hueforge/core/pipeline.py:259:    if layer_plan is not None:
hueforge/core/pipeline.py:260:        (path / "layer_plan.json").write_text(
hueforge/core/pipeline.py:261:            json.dumps(layer_plan, indent=2),
hueforge/core/pipeline.py:401:    plan = _layer_plan(
hueforge/core/pipeline.py:432:def _layer_plan(
hueforge/core/bundle_runner.py:53:            debug_path / "layer_plan.json",
```

- `grep -R "config" -n src hueforge | head -n 200`
```
grep: src/app/__pycache__/pipeline.cpython-311.pyc: plik binarny pasuje do wzorca
grep: src/app/__pycache__/bundle_runner.cpython-311.pyc: plik binarny pasuje do wzorca
grep: hueforge/core/__pycache__/pipeline.cpython-311.pyc: plik binarny pasuje do wzorca
grep: hueforge/core/__pycache__/bundle_runner.cpython-311.pyc: plik binarny pasuje do wzorca
src/app/pipeline.py:54:    palette_config = dict(preset["palette"])
src/app/pipeline.py:55:    palette_colors = palette_config.pop("colors", None)
src/app/pipeline.py:59:        n_colors = int(palette_config.pop("n_colors", 4))
src/app/pipeline.py:61:    print_config = preset.get("print", {})
src/app/pipeline.py:63:        print_config.get("filament_catalog", "filaments/default_catalog.json")
src/app/pipeline.py:75:    paletted = map_palette(preprocessed, palette_colors, **palette_config)
src/app/pipeline.py:77:    base_layer_mm = float(print_config.get("base_layer_mm", 0.0))
src/app/pipeline.py:78:    color_layer_mm = float(print_config.get("color_layer_mm", 0.2))
src/app/pipeline.py:79:    blend_depth = float(print_config.get("blend_depth", 1.0))
src/app/pipeline.py:96:    border_mm = float(print_config.get("border_mm", 0.0))
src/app/pipeline.py:97:    base_height_mm = float(print_config.get("base_height_mm", base_layer_mm))
src/app/pipeline.py:101:    base_filament_id = str(print_config.get("base_filament_id", "white"))
src/app/pipeline.py:102:    sequence_mode = str(print_config.get("sequence_mode", "auto_palette"))
src/app/pipeline.py:103:    manual_sequence = print_config.get("layer_sequence_ids", [])
src/app/pipeline.py:114:            print_config,
src/app/pipeline.py:318:    print_config: Dict[str, Any],
src/app/pipeline.py:328:    catalog_path = Path(print_config.get("filament_catalog", "filaments/default_catalog.json"))
src/app/bundle_runner.py:41:        config_path = temp_path / "config.effective.json"
src/app/bundle_runner.py:42:        config_path.write_text(json.dumps(effective, indent=2), encoding="utf-8")
src/app/bundle_runner.py:52:            config_path,
hueforge/core/pipeline.py:56:    palette_config = dict(preset["palette"])
hueforge/core/pipeline.py:57:    palette_colors = palette_config.pop("colors", None)
hueforge/core/pipeline.py:61:        n_colors = int(palette_config.pop("n_colors", 4))
hueforge/core/pipeline.py:63:    print_config = preset.get("print", {})
hueforge/core/pipeline.py:65:        print_config.get("filament_catalog", "filaments/default_catalog.json")
hueforge/core/pipeline.py:77:    paletted = map_palette(preprocessed, palette_colors, **palette_config)
hueforge/core/pipeline.py:79:    base_layer_mm = float(print_config.get("base_layer_mm", 0.0))
hueforge/core/pipeline.py:80:    color_layer_mm = float(print_config.get("color_layer_mm", 0.2))
hueforge/core/pipeline.py:81:    blend_depth = float(print_config.get("blend_depth", 1.0))
hueforge/core/pipeline.py:98:    border_mm = float(print_config.get("border_mm", 0.0))
hueforge/core/pipeline.py:99:    base_height_mm = float(print_config.get("base_height_mm", base_layer_mm))
hueforge/core/pipeline.py:103:    base_filament_id = str(print_config.get("base_filament_id", "white"))
hueforge/core/pipeline.py:104:    sequence_mode = str(print_config.get("sequence_mode", "auto_palette"))
hueforge/core/pipeline.py:105:    manual_sequence = print_config.get("layer_sequence_ids", [])
hueforge/core/pipeline.py:118:            print_config,
hueforge/core/pipeline.py:324:    print_config: Dict[str, Any],
hueforge/core/pipeline.py:334:    catalog_path = Path(print_config.get("filament_catalog", "filaments/default_catalog.json"))
hueforge/core/bundle_runner.py:43:        config_path = temp_path / "config.effective.json"
hueforge/core/bundle_runner.py:44:        config_path.write_text(json.dumps(effective, indent=2), encoding="utf-8")
hueforge/core/bundle_runner.py:54:            config_path,
```

SECTION 1: Entry point bundle

src/app/main.py (CLI registration + dispatch)
```
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
    ...
        if args.command == "hueforge-bundle":
            _hueforge_bundle_command(args)
            return
```

src/app/main.py (_hueforge_bundle_command -> run_bundle_hueforge)
```
def _hueforge_bundle_command(args: argparse.Namespace) -> None:
    from hueforge.core.bundle_runner import run_bundle_hueforge
    from .cli_overrides import apply_overrides, build_overrides, load_preset, parse_id_list, validate_overrides
    ...
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
```

hueforge/core/bundle_runner.py (bundle entry -> run_pipeline_hueforge)
```
def run_bundle_hueforge(
    input_path: str,
    output_zip: str,
    *,
    debug_dir: Optional[str] = None,
    preset_path: Optional[str] = None,
    allowed_filaments: Optional[List[str]] = None,
    overrides: Optional[Dict[str, Any]] = None,
) -> List[str]:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        base_name = Path(output_zip).name
        if base_name.endswith(".zip"):
            base_name = base_name[:-4]
        output_stl = temp_path / f"{base_name}.stl"
        debug_path = temp_path / "debug"
        debug_path.mkdir(parents=True, exist_ok=True)

        run_pipeline_hueforge(
            input_path,
            str(output_stl),
            debug_dir=str(debug_path),
            preset_path=preset_path,
            allowed_filaments=allowed_filaments,
            overrides=overrides,
        )
```

hueforge/core/pipeline.py (run_pipeline_hueforge -> _write_ascii_stl)
```
    height_map = layers_to_mm(height_layers, base_layer_mm, color_layer_mm)
    border_mm = float(print_config.get("border_mm", 0.0))
    base_height_mm = float(print_config.get("base_height_mm", base_layer_mm))
    height_map = add_border(height_map, border_mm, mm_per_pixel, base_height_mm)
    ...
    if mode != "preview":
        mesh = height_map_to_mesh(height_map, mm_per_pixel=mm_per_pixel)
        _write_ascii_stl(mesh, output_stl_path)
        _write_colorplan(
            output_stl_path,
            print_config,
            base_layer_mm,
            color_layer_mm,
            base_filament_id,
            layer_sequence_ids,
            total_layers,
        )
```

SECTION 2: Config loading / effective config

src/app/cli_overrides.py (CLI overrides for print/canvas)
```
def build_overrides(args: Any) -> Dict[str, Any]:
    overrides: Dict[str, Any] = {}
    if args.catalog:
        overrides.setdefault("print", {})["filament_catalog"] = args.catalog
    if args.n_colors is not None:
        overrides.setdefault("palette", {})["n_colors"] = int(args.n_colors)
    if args.base_filament_id:
        overrides.setdefault("print", {})["base_filament_id"] = args.base_filament_id
    if args.sequence_mode:
        overrides.setdefault("print", {})["sequence_mode"] = args.sequence_mode
    if args.layer_sequence_ids is not None:
        overrides.setdefault("print", {})["layer_sequence_ids"] = parse_id_list(
            args.layer_sequence_ids
        )
    if args.blend_depth is not None:
        overrides.setdefault("print", {})["blend_depth"] = float(args.blend_depth)
    if args.width_mm is not None or args.height_mm is not None:
        canvas = overrides.setdefault("canvas", {})
        if args.width_mm is not None:
            canvas["target_width_mm"] = float(args.width_mm)
        if args.height_mm is not None:
            canvas["target_height_mm"] = float(args.height_mm)
    return overrides
```

hueforge/core/pipeline.py (preset load + print_config usage)
```
def _load_preset(preset_path: Optional[str]) -> Dict[str, Any]:
    if preset_path is None:
        preset_path = str(Path("presets") / "default.json")
    with open(preset_path, "r", encoding="utf-8") as handle:
        preset = json.load(handle)
    return preset

def _apply_overrides(preset: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    merged = json.loads(json.dumps(preset))
    _deep_update(merged, overrides)
    if "palette" in overrides and "n_colors" in overrides["palette"]:
        merged.get("palette", {}).pop("colors", None)
    return merged
```

```
    print_config = preset.get("print", {})
    ...
    base_layer_mm = float(print_config.get("base_layer_mm", 0.0))
    color_layer_mm = float(print_config.get("color_layer_mm", 0.2))
    blend_depth = float(print_config.get("blend_depth", 1.0))
    ...
    border_mm = float(print_config.get("border_mm", 0.0))
    base_height_mm = float(print_config.get("base_height_mm", base_layer_mm))
```

hueforge/core/bundle_runner.py (config.effective.json)
```
        effective = apply_overrides(load_preset(preset_path), overrides or {})
        config_path = temp_path / "config.effective.json"
        config_path.write_text(json.dumps(effective, indent=2), encoding="utf-8")
```

SECTION 3: Height map generation

hueforge/geometry/height_map.py (generate_height_map -> int32 layer counts)
```
def generate_height_map(labels: np.ndarray, **params) -> np.ndarray:
    _validate_labels(labels)

    mode = params.get("mode", "by_index")
    if mode == "by_index":
        scale = float(params.get("scale", 1.0))
        if scale < 0:
            raise ValueError("scale must be >= 0")
        return _layers_by_index(labels, scale)
    if mode == "by_table":
        table = params.get("table")
        if table is None:
            raise ValueError("table is required for by_table mode")
        return _layers_by_table(labels, table)
    raise ValueError(f"unsupported mode: {mode}")
```

```
def _layers_by_index(labels: np.ndarray, scale: float) -> np.ndarray:
    unique_labels = np.unique(labels)
    layers = np.zeros(labels.shape, dtype=np.int32)
    ...
    max_layers = int(round(7 * float(scale)))
    ...
    return layers
```

hueforge/core/pipeline.py (layers -> mm conversion)
```
    height_layers = generate_height_map(merged_labels, **preset["height_map"])
    base_layer_mm = float(print_config.get("base_layer_mm", 0.0))
    color_layer_mm = float(print_config.get("color_layer_mm", 0.2))
    ...
    height_map = layers_to_mm(height_layers, base_layer_mm, color_layer_mm)
    border_mm = float(print_config.get("border_mm", 0.0))
    base_height_mm = float(print_config.get("base_height_mm", base_layer_mm))
    height_map = add_border(height_map, border_mm, mm_per_pixel, base_height_mm)
```

SECTION 4: Mesh/STL generation (Z assignment)

hueforge/geometry/mesh_generation.py (Z from height_map values)
```
def height_map_to_mesh(height_map: np.ndarray, mm_per_pixel: float) -> Mesh:
    _validate_height_map(height_map)
    if mm_per_pixel <= 0:
        raise ValueError("mm_per_pixel must be > 0")

    heights = height_map.astype(np.float32, copy=False)
    height, width = heights.shape
    ...
    for y in range(height):
        for x in range(width):
            x0 = float(x) * mm_per_pixel
            x1 = float(x + 1) * mm_per_pixel
            y0 = float(y) * mm_per_pixel
            y1 = float(y + 1) * mm_per_pixel
            z = float(heights[y, x])
            add_quad(
                (x0, y0, z),
                (x1, y0, z),
                (x1, y1, z),
                (x0, y1, z),
            )
```

hueforge/core/pipeline.py (_write_ascii_stl writes mesh vertex Z)
```
def _write_ascii_stl(mesh: Mesh, path: str) -> None:
    vertices = mesh.vertices
    faces = mesh.faces
    lines = ["solid relief"]
    for face in faces:
        v0, v1, v2 = vertices[face]
        ...
        lines.append(f"      vertex {v0[0]:.6e} {v0[1]:.6e} {v0[2]:.6e}")
        lines.append(f"      vertex {v1[0]:.6e} {v1[1]:.6e} {v1[2]:.6e}")
        lines.append(f"      vertex {v2[0]:.6e} {v2[1]:.6e} {v2[2]:.6e}")
```

SECTION 5: Layer plan generation

hueforge/core/pipeline.py (call + per-layer STL mapping)
```
    layer_plan = _layer_plan(
        base_filament_id, layer_sequence_ids, total_layers, base_layer_mm, color_layer_mm
    )
    if mode != "preview":
        ...
        per_layer = []
        base_mm = 0.32
        step_mm = 0.08
        output_dir = Path(output_stl_path).parent
        for layer_index in range(1, max_layers + 1):
            layer_height = base_mm + layer_index * step_mm
            layer_map = np.where(height_layers >= layer_index, layer_height, 0.0).astype(
                np.float32
            )
            layer_mesh = height_map_to_mesh(layer_map, mm_per_pixel=mm_per_pixel)
            layer_name = f"layer_{layer_index:02d}.stl"
            _write_ascii_stl(layer_mesh, str(output_dir / layer_name))
            per_layer.append(
                {
                    "layer": layer_index,
                    "stl": layer_name,
                    "filament": layer_plan["layers"][layer_index]["filament_id"],
                }
            )
        if per_layer:
            layer_plan["stl_layers"] = per_layer
```

```
def _layer_plan(
    base_filament_id: str,
    layer_sequence_ids: List[str],
    total_layers: int,
    base_layer_mm: float,
    color_layer_mm: float,
) -> Dict[str, Any]:
    base_mm = 0.32
    step_mm = 0.08
    max_layers = 7
    ...
    layers = []
    for idx in range(total_layers):
        if idx == 0:
            filament_id = base_filament_id
        else:
            filament_id = layer_sequence_ids[(idx - 1) % len(layer_sequence_ids)]
        layers.append(
            {
                "layer_index": idx,
                "z_mm": base_mm + idx * step_mm,
                "filament_id": filament_id,
            }
        )
    return {"layers": layers}
```

Mapa ścieżki wykonania:
| Step | File::Function |
| --- | --- |
| Start (CLI) | src/app/main.py::main (hueforge-bundle) |
| CLI handler | src/app/main.py::_hueforge_bundle_command |
| Bundle runner | hueforge/core/bundle_runner.py::run_bundle_hueforge |
| Config load/override | src/app/cli_overrides.py::load_preset + apply_overrides; hueforge/core/pipeline.py::_load_preset + _apply_overrides |
| Height map | hueforge/geometry/height_map.py::generate_height_map; hueforge/core/pipeline.py::run_pipeline_hueforge (layers_to_mm) |
| Mesh build | hueforge/geometry/mesh_generation.py::height_map_to_mesh |
| STL write | hueforge/core/pipeline.py::_write_ascii_stl |
| Layer plan | hueforge/core/pipeline.py::_layer_plan + layer_plan.json in _write_debug |

## Iteration 40 — Add HueForge library sync tool (td preserved 1:1)
Status: DONE
Tests: python3 -m pytest -q → PASS

Tooling: added src/tools/hueforge_library_sync.py to update td_mm in default_catalog.json from HueForge library JSON without changing other fields; added sync tests and README note.
