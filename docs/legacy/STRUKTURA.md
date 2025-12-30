Legacy tree snapshot (current repo layout). Target Claude-plan layout will introduce a hueforge/ package and docs/ structure; see README.md for the migration plan.

.
├── assets
│   └── samples
│       └── README.md
├── data
│   ├── filament_catalog_filamentcolors.json
│   └── filamentcolors_state.json
├── debug
│   ├── height_layers.npy
│   ├── height_mm.npy
│   ├── height.png
│   ├── labels.png
│   ├── layer_plan.json
│   ├── layers_by_label.json
│   ├── palette_assigned.json
│   ├── palette.png
│   ├── palette_suggested.json
│   ├── preprocess.png
│   └── preview.png
├── examples
│   ├── input.png
│   └── README.md
├── filaments
│   └── default_catalog.json
├── manual_tests
│   └── README.md
├── presets
│   ├── cmyk_like_auto.json
│   ├── default_4_auto.json
│   ├── default_4_manual.json
│   └── default.json
├── src
│   ├── app
│   │   ├── __pycache__
│   │   │   ├── bundle_runner.cpython-311.pyc
│   │   │   ├── cli_errors.cpython-311.pyc
│   │   │   ├── cli_overrides.cpython-311.pyc
│   │   │   ├── doctor.cpython-311.pyc
│   │   │   ├── image_io.cpython-311.pyc
│   │   │   ├── main.cpython-311.pyc
│   │   │   ├── pipeline.cpython-311.pyc
│   │   │   ├── preview_runner.cpython-311.pyc
│   │   │   └── version.cpython-311.pyc
│   │   ├── bundle_runner.py
│   │   ├── cli_errors.py
│   │   ├── cli_overrides.py
│   │   ├── doctor.py
│   │   ├── image_io.py
│   │   ├── logging.py
│   │   ├── main.py
│   │   ├── pipeline.py
│   │   ├── preview_runner.py
│   │   ├── types.py
│   │   └── version.py
│   ├── color
│   │   ├── __pycache__
│   │   │   └── color_distance.cpython-311.pyc
│   │   └── color_distance.py
│   ├── geom
│   │   ├── __pycache__
│   │   │   └── mesh_generation.cpython-311.pyc
│   │   └── mesh_generation.py
│   ├── image_to_3d_relief.egg-info
│   │   ├── dependency_links.txt
│   │   ├── PKG-INFO
│   │   ├── requires.txt
│   │   ├── SOURCES.txt
│   │   └── top_level.txt
│   ├── ops
│   │   ├── __pycache__
│   │   │   ├── add_border.cpython-311.pyc
│   │   │   ├── height_map.cpython-311.pyc
│   │   │   ├── layers_to_mm.cpython-311.pyc
│   │   │   ├── merge_small_regions.cpython-311.pyc
│   │   │   ├── palette_mapping.cpython-311.pyc
│   │   │   ├── palette_suggestion.cpython-311.pyc
│   │   │   ├── preprocess_edge_preserving.cpython-311.pyc
│   │   │   ├── scale_to_canvas.cpython-311.pyc
│   │   │   └── segment_superpixels.cpython-311.pyc
│   │   ├── add_border.py
│   │   ├── height_map.py
│   │   ├── layers_to_mm.py
│   │   ├── merge_small_regions.py
│   │   ├── palette_mapping.py
│   │   ├── palette_suggestion.py
│   │   ├── preprocess_edge_preserving.py
│   │   ├── scale_to_canvas.py
│   │   └── segment_superpixels.py
│   ├── print
│   │   ├── __pycache__
│   │   │   ├── colorplan_export.cpython-311.pyc
│   │   │   ├── filament_assignment.cpython-311.pyc
│   │   │   └── filaments.cpython-311.pyc
│   │   ├── colorplan_export.py
│   │   ├── filament_assignment.py
│   │   └── filaments.py
│   ├── sim
│   │   ├── __pycache__
│   │   │   └── td_preview.cpython-311.pyc
│   │   └── td_preview.py
│   ├── solver
│   │   ├── __pycache__
│   │   │   └── region_recipe.cpython-311.pyc
│   │   └── region_recipe.py
│   ├── tools
│   │   ├── __pycache__
│   │   │   ├── filamentcolors_sync.cpython-311.pyc
│   │   │   ├── filaments_cli.cpython-311.pyc
│   │   │   └── preset_gen.cpython-311.pyc
│   │   ├── filamentcolors_sync.py
│   │   ├── filaments_cli.py
│   │   └── preset_gen.py
│   └── web
│       ├── __pycache__
│       │   └── server.cpython-311.pyc
│       ├── static
│       │   ├── app.js
│       │   └── index.html
│       └── server.py
├── tests
│   ├── __pycache__
│   │   ├── test_add_border.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_cli_bundle.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_cli_overrides.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_cli_overrides_subprocess.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_cli_pipeline.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_cli_preview.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_cli_version.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_color_distance.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_colorplan_export.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_colorplan_plan.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_examples_bundle.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_filament_assignment.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_filamentcolors_sync.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_filaments_cli.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_height_map.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_image_io.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_layers_to_mm.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_merge_small_regions.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_mesh_generation.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_palette_mapping.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_palette_suggestion.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_preprocess_edge_preserving.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_preset_gen.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_region_recipe.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_scale_to_canvas.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_segment_superpixels.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_smoke.cpython-311-pytest-9.0.2.pyc
│   │   ├── test_td_preview.cpython-311-pytest-9.0.2.pyc
│   │   └── test_web_server.cpython-311-pytest-9.0.2.pyc
│   ├── test_add_border.py
│   ├── test_cli_bundle.py
│   ├── test_cli_overrides.py
│   ├── test_cli_overrides_subprocess.py
│   ├── test_cli_pipeline.py
│   ├── test_cli_preview.py
│   ├── test_cli_version.py
│   ├── test_color_distance.py
│   ├── test_colorplan_export.py
│   ├── test_colorplan_plan.py
│   ├── test_examples_bundle.py
│   ├── test_filament_assignment.py
│   ├── test_filamentcolors_sync.py
│   ├── test_filaments_cli.py
│   ├── test_height_map.py
│   ├── test_image_io.py
│   ├── test_layers_to_mm.py
│   ├── test_merge_small_regions.py
│   ├── test_mesh_generation.py
│   ├── test_palette_mapping.py
│   ├── test_palette_suggestion.py
│   ├── test_preprocess_edge_preserving.py
│   ├── test_preset_gen.py
│   ├── test_region_recipe.py
│   ├── test_scale_to_canvas.py
│   ├── test_segment_superpixels.py
│   ├── test_smoke.py
│   ├── test_td_preview.py
│   └── test_web_server.py
├── AUDIT_REPORT_v1_2025-12-30.md
├── CHANGELOG.md
├── CODEX_RULES.md
├── CONTRACTS.md
├── DECISIONS.md
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
├── REPORT.md
├── result.zip
├── ROADMAP.md
├── STRUKTURA1.md
└── STRUKTURA.md

32 directories, 161 files
