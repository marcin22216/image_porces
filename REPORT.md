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
