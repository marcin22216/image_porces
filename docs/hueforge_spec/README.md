Confirmed HueForge-like contract and implementation notes.

- hueforge_reality_check.md
- optical_solver_analysis.md
- hueforge_experiments.md

Optical heightfield config (preset):
- height_map.mode: "optical_hueforge"
- print.max_thickness_mm
- print.color_layer_mm
- optical.stack_filament_ids
- optical.stack_thresholds_mm (last == max_thickness_mm)
- optical.metric ("lab" or "rgb")
- optical.color_space ("srgb" or "linear_srgb")
- optical.step_mm
