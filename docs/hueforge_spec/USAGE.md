# HueForge-like optical_hueforge usage contract

This document is the single place to run, validate, and troubleshoot the
optical_hueforge heightfield pipeline. It is written for users and developers.

## What optical_hueforge does (contract)
- Output geometry is a single STL with a continuous height map in mm (float).
- Colorplan is layer-swap guidance only; it must NOT encode the image.
- Beer-Lambert solver is preserved; do not change its physics.

## Required config fields
These are mandatory for optical_hueforge (fail-fast if missing):
- height_map.mode = "optical_hueforge"
- print.max_thickness_mm
- print.color_layer_mm
- optical.stack_filament_ids
- optical.stack_thresholds_mm (strictly increasing; last == max_thickness_mm)
- optical.metric ("lab" or "rgb")
- optical.color_space ("srgb" or "linear_srgb")
- optical.step_mm

## Minimal config (2-stack) + why it can look stepped
Minimal (uses default catalog with ids: base, black):
```json
{
  "canvas": {
    "target_width_mm": 60.0,
    "target_height_mm": 60.0
  },
  "height_map": {
    "mode": "optical_hueforge"
  },
  "optical": {
    "stack_filament_ids": ["base", "black"],
    "stack_thresholds_mm": [0.36, 0.72],
    "metric": "rgb",
    "color_space": "linear_srgb",
    "step_mm": 0.02
  },
  "print": {
    "max_thickness_mm": 0.72,
    "color_layer_mm": 0.08,
    "filament_catalog": "filaments/default_catalog.json",
    "base_layer_mm": 0.0,
    "base_height_mm": 0.0
  }
}
```

Why binary/stepped output happens:
- With a 2-stack and a binary image (pure black/white), the solver only needs
  two depths (near 0 and near max_thickness), so Z collapses to two levels.
- Large optical.step_mm also increases "stair stepping" because depth sampling
  is coarse, even for gradients.

## Recommended config (4-stack)
Example using the bundled HueForge library (ids are generated from
manufacturer/type/color in hueforge_filament_library.json). Default
hueforge-bundle uses filaments/default_catalog.json (3 filaments), so
for a 4-stack you must point print.filament_catalog to a richer catalog.
```json
{
  "canvas": {
    "target_width_mm": 200.0,
    "target_height_mm": 200.0
  },
  "height_map": {
    "mode": "optical_hueforge"
  },
  "optical": {
    "stack_filament_ids": [
      "prusament_pla_blend_my_silverness",
      "prusament_pla_jet_black",
      "prusament_pla_azure_blue",
      "prusament_pla_blend_ms_pink"
    ],
    "stack_thresholds_mm": [0.5, 1.0, 1.5, 2.0],
    "metric": "rgb",
    "color_space": "linear_srgb",
    "step_mm": 0.02
  },
  "print": {
    "max_thickness_mm": 2.0,
    "color_layer_mm": 0.08,
    "filament_catalog": "hueforge_filament_library.json",
    "base_layer_mm": 0.0,
    "base_height_mm": 0.0
  }
}
```
Notes:
- Replace stack ids if your catalog differs. Use
  `python3 -m src.app.main filaments --catalog hueforge_filament_library.json --limit 10`
  to verify ids.
- The sanity preset explicitly sets print.filament_catalog to
  hueforge_filament_library.json, so the command below works as-is.
- If you use another catalog, set print.filament_catalog and update stack ids
  to match that catalog.
- stack_thresholds_mm must end at max_thickness_mm; thresholds define swap
  depths only (not geometry quantization).

## Known good fixtures
- tests/fixtures/gradient_64.png
  - Purpose: validate continuous heightfield (unique_z > 10, z_range > 0.5).
  - Recommended for quick sanity.
- tests/fixtures/by_index_two_regions.png
  - Purpose: by_index non-regression only (not optical).
- pix1.png
  - Purpose: real benchmark for artifact quality and size.
  - Warning: large runtime and large STL/ZIP outputs.

## Parameter -> effect
| Parameter | Effect on output | Typical guidance |
| --- | --- | --- |
| print.max_thickness_mm | Max Z range of heightfield | Higher gives stronger relief but larger z_range and more swap layers. |
| optical.step_mm | Depth sampling resolution | Too large causes stair stepping; 0.02 is a practical baseline. |
| optical.stack_thresholds_mm | Swap depths for colorplan | Must be strictly increasing and end at max_thickness_mm. |
| print.color_layer_mm (layer_height_mm) | Layer swap granularity | Smaller = more layers; affects colorplan indices, not geometry. |
| canvas.target_width_mm / target_height_mm | XY size and mm_per_pixel | Larger canvas increases STL size and triangle count. |

## Quality metrics (how to judge output)
1) unique_z (count of distinct vertex Z):
   - Expected for gradient_64: > 10 (continuous relief).
2) z_range (maxZ - minZ):
   - Expected for gradient_64: > 0.5 mm.
3) triangle count and file size:
   - Triangles scale ~O(W*H); STL size grows quickly with resolution.
   - ASCII STL is larger than binary; expect multi-MB for pix1.png.

## Diagnostics (quick recipes)
Run bundle (optical_hueforge):
`python3 -m src.app.main hueforge-bundle --in tests/fixtures/gradient_64.png --out artifacts/optical_hueforge_sanity.zip --preset docs/hueforge_spec/presets/optical_hueforge_sanity.json`

STL bounds and triangle count:
`python3 -m src.tools.stl_diagnostics --stl path/to/output.stl`

Unique Z count (ASCII STL):
```python
z_values = set()
with open("output.stl", "r", encoding="utf-8", errors="ignore") as handle:
    for line in handle:
        if line.strip().startswith("vertex "):
            z_values.add(round(float(line.split()[3]), 6))
print(len(z_values))
```

## Risk map (pitfalls + detection)
| Risk | Symptom | Detection | Mitigation |
| --- | --- | --- | --- |
| Binary image + 2-stack | Only two Z levels | unique_z ~2 | Use gradient input or 4-stack. |
| optical.step_mm too large | Stair-stepped relief | unique_z small, z diffs == step | Decrease step_mm (e.g. 0.02). |
| thresholds != max_thickness_mm | CLI error or wrong swaps | run fails or colorplan mismatch | Ensure last threshold == max_thickness_mm. |
| Missing filament ids | CLI error | "filament id not found" | Verify ids with filaments CLI. |
| Large input (pix1.png) | Long runtime, huge STL | large file size, slow run | Use smaller fixtures for sanity runs. |
| base_height_mm > 0 | minZ > 0 | STL minZ not zero | Set base_height_mm to 0 if needed. |
| sRGB vs linear mismatch | dull contrast | preview looks flat | Try linear_srgb and rgb metric. |
