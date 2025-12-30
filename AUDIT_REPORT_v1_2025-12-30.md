# Audit Report v1 (Snapshot 2025-12-30)

A. Executive Summary
- Status ogolny: aplikacja ma kompletna, stabilna sciezke CLI oraz cienka nakladke WEB/UI; roadmapa i raport wskazuja DONE dla glownej funkcjonalnosci. 
- Najwieksze mocne strony: scisle kontrakty danych + walidacje typow/ksztaltow, wyrazny podzial IO vs czyste operacje, testy integracyjne CLI i TestClient dla WEB. 
- Najwieksze ryzyka: rozjazd wersji (CHANGELOG v1.0.1 vs src/app/version.py 1.0.0), rozjazd komunikatu w README ("GUI/Web: planned") vs ROADMAP/REPORT (GUI/live preview DONE), potencjalna niespojnosc borderu gdy base_height_mm != base_layer_mm.

B. Zgodnosc z zasadami (tabela)

| Zasada | Ocena | Dowod (pliki/moduly) | Uwagi |
| --- | --- | --- | --- |
| One change per iteration | OK | REPORT.md | Iteracje zarejestrowane sekwencyjnie; brak edycji kontraktow w tym snapshotcie. |
| Tests are mandatory | OK | REPORT.md | Kazda iteracja ma zapis testow; canonical pytest command wskazany w CODEX_RULES.md. |
| No logic in GUI | OK | src/web/static/index.html, src/web/static/app.js | UI zbiera dane i wywoluje /preview; brak logiki domenowej. |
| Pure operations | OK | src/ops/*, src/geom/mesh_generation.py, src/sim/td_preview.py, src/solver/region_recipe.py | Moduly operacji nie wykonuje IO; IO znajduje sie w src/app/*, src/print/*, src/web/server.py, src/tools/*. |
| Stable data contracts | OK | CONTRACTS.md, src/ops/layers_to_mm.py, src/geom/mesh_generation.py | Jawne przeliczenia warstw na mm; wymagane dtype/shape. |
| CLI source of truth | OK | src/app/main.py, src/app/pipeline.py, src/web/server.py | WEB wrapuje run_preview/run_bundle bez modyfikacji pipeline. |
| Brak "magii" i domyslow | WARN | src/web/server.py | Web ustawia domyslny catalog na data/filament_catalog_filamentcolors.json, jesli plik istnieje. |
| Brak breaking changes | OK | CHANGELOG.md, src/app/version.py | Brak sygnalow zmian kontraktow; wersja pozostaje v1.0.0 (patrz ryzyko rozjazdu). |

C. Architektura i moduly
- src/app: CLI i orchestracja pipeline (argumenty, walidacje, presety, uruchomienie). Dowod: src/app/main.py, src/app/pipeline.py, src/app/cli_overrides.py.
- src/ops: czyste operacje na obrazach i etykietach (preprocess, segment, merge, palette, height). Dowod: src/ops/*.py.
- src/geom: generacja siatki z height map w mm. Dowod: src/geom/mesh_generation.py.
- src/sim: optyczny preview (Beer-Lambert, TD), bez wplywu na STL. Dowod: src/sim/td_preview.py.
- src/solver: solver warstw per etykieta uzywany w preview. Dowod: src/solver/region_recipe.py.
- src/print: katalog filamentow, przypisanie palety, export colorplan. Dowod: src/print/*.py.
- src/tools: narzedzia pomocnicze (sync katalogu, CLI filaments, generacja presetow). Dowod: src/tools/*.py.
- src/web: FastAPI wrapper i statyczny UI. Dowod: src/web/server.py, src/web/static/*.
- Czyste funkcje vs IO: czyste operacje sa w src/ops, src/geom, src/sim, src/solver; IO jest w src/app/image_io.py, src/app/pipeline.py (debug/eksport), src/print/colorplan_export.py, src/tools/*, src/web/server.py.
- Stabilne kontrakty danych sa wymuszane przez walidacje dtype/shape w src/ops/* i src/geom/mesh_generation.py oraz przez kontrakty w CONTRACTS.md.

D. Kontrakty danych (CONTRACTS.md)
- Jednostki: px (image/labels), layers (int), mm (geometry). Dowod: CONTRACTS.md; przeliczenia w src/ops/layers_to_mm.py i src/geom/mesh_generation.py.
- mm_per_pixel liczony raz: src/ops/scale_to_canvas.py, przekazywany do src/geom/mesh_generation.py i src/ops/add_border.py w src/app/pipeline.py.
- Height layers -> height_mm: src/ops/layers_to_mm.py (float32), wywolywany w src/app/pipeline.py.
- Border na height map: src/ops/add_border.py; zastosowanie w src/app/pipeline.py.
- Filament contract: id/name/rgb/td_mm walidowane w src/print/filaments.py.
- Zgodnosc: testy kontraktow w tests/test_layers_to_mm.py, tests/test_height_map.py, tests/test_mesh_generation.py, tests/test_colorplan_export.py.
- Niejawne konwersje/ryzyka: src/sim/td_preview.py ustawia td_mm=1.0 jesli brak w katalogu (domyslne zalozenie); src/app/pipeline.py uzywa base_height_mm przy borderze (moze odbiegac od base_layer_mm z kontraktu borderu).

E. Pipeline 2D->3D (end-to-end)
- 1) Load image: PIL -> ImageData -> ndarray uint8. Dowod: src/app/image_io.py, src/app/pipeline.py.
- 2) Scale to canvas + mm_per_pixel: src/ops/scale_to_canvas.py.
- 3) Preprocess (bilateral): src/ops/preprocess_edge_preserving.py.
- 4) Segment (SLIC): src/ops/segment_superpixels.py.
- 5) Merge small regions: src/ops/merge_small_regions.py.
- 6) Suggest palette (deterministyczny RNG seed=0): src/ops/palette_suggestion.py.
- 7) Assign palette to filaments (LAB/RGB): src/print/filament_assignment.py, src/color/color_distance.py.
- 8) Palette mapping: src/ops/palette_mapping.py.
- 9) Height layers: src/ops/height_map.py + blend_depth scaling w src/app/pipeline.py.
- 10) Layers -> mm: src/ops/layers_to_mm.py.
- 11) Border on height map: src/ops/add_border.py.
- 12) Layer plan + colorplan: src/app/pipeline.py, src/print/colorplan_export.py.
- 13) Mesh + STL ASCII: src/geom/mesh_generation.py, zapis w src/app/pipeline.py.
- 14) Debug artifacts: preview.png, palette/labels/height/plan JSON/NPY w src/app/pipeline.py.
- Deterministycznosc: brak losowosci poza seed=0 w palette_suggestion; brak globalnych seedow w innych modulach.

F. Kolor / TD / warstwy
- Filamenty: format {id,name,rgb,td_mm} + walidacje. Dowod: src/print/filaments.py.
- Dobor filamentow: nearest_filament z LAB preferowane, fallback RGB. Dowod: src/print/filament_assignment.py, src/color/color_distance.py.
- TD model: Beer-Lambert w simulate_stack; tylko dla preview. Dowod: src/sim/td_preview.py.
- Colorplan: generowany w src/app/pipeline.py i zapisywany przez src/print/colorplan_export.py; format w CONTRACTS.md.
- Warstwy per etykieta dla preview: solver dopasowuje warstwy do barwy bazowej. Dowod: src/solver/region_recipe.py.

G. WEB + UI
- FastAPI wrapper: /health, /ui, /preview, /bundle, /static. Dowod: src/web/server.py.
- Web wywoluje core: /preview -> run_preview, /bundle -> run_bundle. Dowod: src/web/server.py, src/app/preview_runner.py, src/app/bundle_runner.py.
- UI: statyczny index + JS, brak logiki domenowej. Dowod: src/web/static/index.html, src/web/static/app.js.
- Live preview: debounce 500ms na n_colors/blend_depth, AbortController, blokada przycisku, status "Rendering...". Dowod: src/web/static/app.js.
- Ograniczenia: UI obsluguje tylko /preview; brak ustawien katalogu/sequence; plik wymagany przed pierwszym preview.

H. Testy i jakosc
- Pokrycie: testy unit dla ops/geom/color/sim/solver/print; integracje CLI; TestClient dla WEB. Dowod: tests/test_*.py.
- Typy testow: unit (np. tests/test_height_map.py), subprocess CLI (tests/test_cli_*.py), TestClient (tests/test_web_server.py).
- Najslabsze miejsca: brak testow zachowania JS/UI (live preview, debounce, abort), brak testow DOM/UX.

I. Roadmap vs rzeczywistosc
- DONE wg ROADMAP/REPORT: core pipeline, CLI, preview TD, web wrapper, UI live preview. Dowod: ROADMAP.md, REPORT.md.
- NEXT: brak niezaznaczonych punktow w ROADMAP.md.
- Dryf dokumentacyjny: README nadal mowi "GUI/Web: planned" i "Roadmap (short): GUI, Live preview" mimo ze ROADMAP/REPORT maja DONE. Dowod: README.md.
- Dryf wersji: CHANGELOG.md wskazuje v1.0.1, a src/app/version.py wskazuje 1.0.0. Dowod: CHANGELOG.md, src/app/version.py.

J. Known risks / edge cases
- Border i base height: border korzysta z base_height_mm, niekoniecznie base_layer_mm (kontrakt borderu). Dowod: src/app/pipeline.py, CONTRACTS.md.
- Domyslne domieszanie katalogu w WEB: /preview i /bundle uzywaja data/filament_catalog_filamentcolors.json gdy plik istnieje. Dowod: src/web/server.py.
- Brak walidacji manual sequence w presetach (walidacja tylko w overrides). Dowod: src/app/cli_overrides.py, src/app/pipeline.py.
- Wydajnosc: bilateral + SLIC to petle po pikselach, koszt rosnie z rozmiarem obrazu. Dowod: src/ops/preprocess_edge_preserving.py, src/ops/segment_superpixels.py.
- Limit uploadu WEB: 20MB, wieksze pliki odrzucane. Dowod: src/web/server.py.
