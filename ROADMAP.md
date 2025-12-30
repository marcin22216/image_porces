# ROADMAP

# Foundation v1 — CLOSED
Foundation v1 covered the core 2D->3D pipeline, CLI commands, and the FastAPI web wrapper with UI live preview.
The phase is formally closed after the audit snapshot (AUDIT_REPORT_v1_2025-12-30.md).
Further work will be tracked as separate phases.

- [x] 01 Project skeleton & test runner
- [x] 02 Image loading/saving
- [x] 03 Edge-preserving preprocessing
- [x] 04 Superpixel segmentation
- [x] 05 Merge small regions
- [x] 06 Palette mapping
- [x] 07 Height map generation
- [x] 08 Mesh generation
- [x] 09 STL export
- [x] 10 CLI pipeline
- [x] 11 GUI skeleton
- [x] 12 Translucency preview

# Extended roadmap items
- [x] Canvas sizing (mm_per_pixel) + aspect ratio
- [x] Border on base (heightmap expansion)
- [x] Layer model (layers → mm conversion)
- [x] Colorplan export (STL + TXT)
- [x] Translucency preview (TD simulation core)
- [x] Palette to filament assignment
- [x] Region recipe solver (one-click core)
- [x] Palette suggestion
- [x] CLI pipeline v1 debug + preview + colorplan
- [x] Colorplan global v1
- [x] Global layer plan modes (manual/auto_palette)
- [x] CLI preview command
- [x] FilamentColors.xyz sync + presets
- [x] Filament catalog CLI
- [x] Filament catalog CLI v2 (limit/offset/nearest)
- [x] CLI overrides for presets
- [x] CLI overrides validation (manual/allowed)
- [x] CLI UX errors + summaries
- [x] CLI bundle command
- [x] LAB distance for color matching
- [x] LAB distance (RGB->LAB fallback)
- [x] Brand preset generator
- [x] FastAPI web wrapper
- [x] UI live preview (debounce)
- [x] CLI v1 release prep
- [x] Examples + license metadata
- [x] Makefile quick commands
- [x] UI copy & status panel
- [x] Manual UI test scenarios
