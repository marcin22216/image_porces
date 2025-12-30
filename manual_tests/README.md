# Manual UI Test Scenarios

## Setup
1) Start the server: `python3 -m src.web.server`
2) Open: `http://127.0.0.1:8000/ui`
3) Keep the Status panel visible while testing.

## Test data
- Use `examples/input.png` as the default image.
- For large-image tests, use a locally available high-resolution image if you have one.

## Scenarios

### MT-UI-01 — Happy path (defaults)
Goal: Confirm a basic preview works with default parameters.
Steps:
- Open `/ui`.
- Select `examples/input.png`.
- Leave `n_colors` and `blend_depth` empty.
- Click Preview.
Expected result:
- Status panel shows the file name/size and `default` for both parameters.
- Status goes from Rendering... to Done.
- Preview image appears.
Negative variant:
- If the server is not running, Status should show Error and the message should mention a network error.

### MT-UI-02 — n_colors low vs high
Goal: See a visible change when palette size changes.
Steps:
- With the same image selected, set `n_colors` to 2.
- Wait for live preview or click Preview.
- Change `n_colors` to 6.
- Wait for live preview or click Preview.
Expected result:
- Preview with 2 colors looks simpler/flatter than with 6 colors.
- Status reflects the current `n_colors` value and ends on Done.
Negative variant:
- Clear the file input and change `n_colors`; Status should remain Idle or Error and preview should not update.

### MT-UI-03 — blend_depth low vs high
Goal: Verify edge blending visibly changes.
Steps:
- Select `examples/input.png`.
- Set `blend_depth` to 0.5 and wait for preview.
- Set `blend_depth` to 2.0 and wait for preview.
Expected result:
- Lower blend depth shows harder transitions; higher blend depth shows smoother transitions.
- Status ends on Done after each change.
Negative variant:
- Enter a non-number (if the browser allows) and confirm preview does not update and Status shows Error.

### MT-UI-04 — Rapid changes (debounce + abort)
Goal: Confirm rapid input changes do not create inconsistent UI state.
Steps:
- Select an image.
- Quickly change `n_colors` across 3-4 values (e.g., 2, 3, 5, 4).
- Quickly change `blend_depth` across 3-4 values (e.g., 0.8, 1.2, 1.8).
Expected result:
- Status should stay Rendering during quick changes and end on Done.
- Preview should correspond to the last values entered.
Negative variant:
- If you click Preview mid-stream, the final preview should still reflect the last values.

### MT-UI-05 — Invalid or non-image file
Goal: Ensure the UI surfaces an error for bad input.
Steps:
- Create or choose a non-image file (e.g., a .txt file).
- Select it in the file input.
- Click Preview.
Expected result:
- Status shows Error.
- Error message indicates failure (e.g., Preview failed: 400).
Negative variant:
- If the file is rejected by the browser, the UI should keep Status as Idle and show no preview.

### MT-UI-06 — Network/API error
Goal: Ensure the UI surfaces a network error.
Steps:
- Stop the server.
- Refresh the UI page.
- Select a valid image and click Preview.
Expected result:
- Status shows Error.
- Error message says Network error.
Negative variant:
- Restart the server and retry; Status should recover and show Done with a preview.

### MT-UI-07 — Large image performance
Goal: Observe rendering time for a large image and confirm UI responsiveness.
Steps:
- Select a high-resolution image (e.g., several megapixels).
- Keep `n_colors`/`blend_depth` at defaults.
- Click Preview and wait.
Expected result:
- Status stays Rendering longer than for small images.
- UI remains responsive; Status ends on Done and preview appears.
Negative variant:
- If rendering takes too long, change a parameter to trigger a new preview; Status should still end on Done.
