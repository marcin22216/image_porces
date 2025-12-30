# Migration to Claude plan (hueforge/)

## Scope
This repo is migrating from legacy `src/` modules to a HueForge-style package layout under `hueforge/`.
The legacy CLI remains the source of truth until the migration is complete.

## Mapping (legacy -> target)
- `src/app` -> `hueforge/core` (CLI orchestration, config, IO), plus `hueforge/export` for bundle assembly.
- `src/ops` -> split across:
  - `hueforge/preprocessing` (scale_to_canvas, preprocess_edge_preserving, segment, merge)
  - `hueforge/geometry` (height_map, layers_to_mm, add_border)
- `src/geom` -> `hueforge/geometry` (mesh generation).
- `src/print` -> split across:
  - `hueforge/palette` (filaments, filament assignment)
  - `hueforge/export` (colorplan, STL writers).
- `src/sim` -> `hueforge/physics` (TD/Beer-Lambert preview).
- `src/solver` -> `hueforge/mapping` (layer/recipe solving).
- `src/color` -> `hueforge/core` or `hueforge/gamut` (color distance utilities).
- `src/tools` -> `hueforge/utils` or `tools/` (CLI helpers and maintenance scripts).

## Non-goals for migration iterations
- No breaking changes to CLI behavior.
- No deletion of legacy modules without explicit approval.
- No new dependencies unless required by a specific module.

## HueForge library catalog input
`hueforge.print.filaments.load_catalog` now accepts the HueForge filament library format
(metadata + entries with manufacturer/type/color/hexCode/td). The adapter preserves `td`
values 1:1 as `td_mm` and converts `hexCode` to `rgb` without normalization.

## Pending cleanup tasks
- Unify `tools/` (root scripts) vs `src/tools` (CLI helpers) once compatibility shims are defined.
- Move tests into `tests/unit` and `tests/integration` after updating repo-root path logic.

## Safety notes
- Many tests derive repo root via `Path(__file__).resolve().parents[1]` and will break if moved.
- Keep `pix1.png` available for the regression test until fixtures are relocated.
