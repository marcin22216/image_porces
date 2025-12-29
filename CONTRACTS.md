# CONTRACTS.md (Frozen v1)
Single source of truth for data contracts, units, and artifacts.

This file defines NON-NEGOTIABLE technical contracts used across the project.
All modules, tests, CLI, and future GUI must follow these rules.

---

## 1. Units & Scaling

### 1.1 Coordinate systems
- **Image / labels space**: pixels (px)
- **Layer space**: integer number of color layers
- **Geometry space**: millimeters (mm)

No module may mix units implicitly.

---

### 1.2 Pixel ↔ millimeter mapping
- `mm_per_pixel` is computed **once**, in the `scale_to_canvas` stage.
- All subsequent operations operate on pixel grids but **must respect `mm_per_pixel`** when converting to geometry.

Rule:
```
XY_mm = pixel_index * mm_per_pixel
```

---

### 1.3 Height definition (Z axis)

Height is defined in two stages:

#### A) Discrete layer model
- `height_layers`: number of color layers per pixel (integer ≥ 0)

#### B) Conversion to millimeters
Final height in millimeters is:

```
height_mm = base_layer_mm + height_layers * color_layer_mm
```

Where:
- `base_layer_mm` – base (foundation) thickness
- `color_layer_mm` – thickness of a single color layer

This conversion is explicit and must not be embedded implicitly in mesh generation.

---

## 2. Data Contracts (Strict)

### 2.1 Core arrays

| Name            | Shape        | dtype      | Meaning |
|-----------------|--------------|------------|--------|
| `image`         | (H, W, 3)    | uint8      | RGB image |
| `labels`        | (H, W)       | int32      | Region labels |
| `height_layers` | (H, W)       | int32      | Number of color layers |
| `height_mm`     | (H, W)       | float32    | Height in millimeters |

Rules:
- `labels >= 0`
- `height_layers >= 0`
- `height_mm >= base_layer_mm`

---

### 2.2 Border handling
- Border is applied **on height maps**, not directly in mesh logic.
- Border pixels always have:
```
height_layers = 0
height_mm = base_layer_mm
```

Border size:
```
border_px = round(border_mm / mm_per_pixel)
```

This guarantees:
- border exists only on the base layer
- no interference with color logic or optics

---

## 3. Filament Catalog (Optical Model)

### 3.1 Filament definition
Each filament has:

- `id` (stable key)
- `name` (user-editable)
- `rgb` (reference color)
- `td_mm` (Transmission Distance, millimeters)

Transmission Distance is **per filament**, never global.

---

### 3.2 Optical meaning of TD
TD defines light attenuation using Beer–Lambert law:

```
T(t) = exp(-t / TD)
```

Where:
- `t` – material thickness in mm
- `TD` – transmission distance of filament

TD is used **only for preview / simulation**, never for geometry generation.

---

## 4. Color Layer Stack (Recipe)

A color recipe defines how color layers are stacked.

Conceptually:
- base layer (foundation)
- N color layers above it
- each color layer corresponds to one filament

Layer thickness is always:
```
color_layer_mm
```

Layer count is an integer and may be:
- user-defined
- scaled proportionally (e.g. blend depth)

---

## 5. Artifacts & Outputs

### 5.1 Geometry
- Primary geometry output:  
  ```
  <name>.stl
  ```
- STL units are millimeters.

---

### 5.2 Color change plan (sidecar file)
Alongside STL, the pipeline must generate:

```
<name>.colorplan.txt
```

This file describes filament changes per layer / height.

Minimal contents:
- base_layer_mm
- color_layer_mm
- filament catalog used
- list of color change events:
  - layer index
  - Z height in mm
  - filament id

This file is slicer-agnostic and acts as a bridge to:
- manual filament changes
- MMU / AMS systems
- future G-code generators

---

## 6. Module Responsibility Rules

- Image processing modules: **pixels only**
- Segmentation & palette: **labels only**
- Height logic: **layers first, mm second**
- Mesh generation: **pure geometry, mm only**
- Optical preview: **RGB + TD only**

No module may silently:
- convert units
- infer scale
- assume layer thickness

---

## 7. Non-negotiable Rules

1. No unit ambiguity – every function must state its unit domain.
2. Geometry must never depend on optical simulation.
3. Optical simulation must never affect STL output.
4. All conversions (px → mm, layers → mm) are explicit and testable.
5. CONTRACTS.md overrides any implicit behavior elsewhere.

---

## Breaking changes policy

- Breaking changes require a major version bump (v2+).
- Compatibility within v1 is expected for inputs, outputs, and file formats.

End of contracts.
