# Plan Eksperymentów - Domknięcie Wiedzy o HueForge
## 4 Testy Które Rozstrzygną Wszystko

---

## EKSPERYMENT 1: Model Beer-Lambert - Przestrzeń Kolorów i Absorption

### Cel
Ustalić:
1. Czy `color` to linear RGB czy sRGB
2. Czy absorption jest `1 - color` czy coś innego
3. Czy światło to [1,1,1] czy 4000K profile
4. Czy error metric to RGB, LAB, czy inny

### Test Case
**Wygeneruj w HueForge 3 bardzo proste obrazy:**

#### Image A: Pure Red Gradient
```
┌─────────────────┐
│ 255,0,0         │ ← czerwony
│    ↓            │
│ 127,0,0         │ ← ciemny czerwony
│    ↓            │
│   0,0,0         │ ← czarny
└─────────────────┘
```

**Settings:**
- Stack: **TYLKO Red filament** (1 kolor!)
- TD: 1.0 mm (standardowe)
- Max thickness: 2.0 mm
- Light: Natural White 4000K (default)

**Co to rozstrzyga:**
Dla single layer możemy analitycznie odwrócić Beer-Lambert:
```
depth = -TD * ln(I_out / I_in) / absorption
```

Zmierz depth w 3 punktach:
- Red (255,0,0): depth = ?
- Dark Red (127,0,0): depth = ?
- Black (0,0,0): depth = ?

**Analiza wyników:**

**Test 1: sRGB vs Linear**
```python
# Jeśli HueForge używa sRGB:
depth_127 / depth_255 ≈ 0.5

# Jeśli używa Linear RGB:
depth_127 / depth_255 ≈ 0.22  # bo srgb_to_linear(127/255) ≈ 0.22
```

**Test 2: Absorption model**
```python
# Jeśli absorption = 1 - color:
# dla red filament (1, 0, 0):
# absorption = (0, 1, 1)  # pochłania G i B, przepuszcza R

# Dla red pixel target (1, 0, 0):
# tylko R channel ma znaczenie
# depth ∝ -ln(1/1) = 0  ← płasko!

# Więc albo:
# A) absorption nie jest 1-color
# B) jest weighted sum kanałów
# C) solver używa luminance, nie per-channel
```

**Jak wykonać pomiar:**
1. Wygeneruj STL w HueForge
2. Otwórz w MeshLab/Blender
3. Zaznacz punkt (vertex selection)
4. Odczytaj współrzędną Z (to jest depth!)
5. Powtórz dla 3 punktów gradientu

---

#### Image B: RGB Color Cube Corners
```
┌─────┬─────┬─────┐
│ Red │Yellow│Green│  ← (255,0,0), (255,255,0), (0,255,0)
├─────┼─────┼─────┤
│Blue │White │Cyan │  ← (0,0,255), (255,255,255), (0,255,255)
├─────┼─────┼─────┤
│Black│Gray │Mag. │  ← (0,0,0), (127,127,127), (255,0,255)
└─────┴─────┴─────┘
```

**Settings:**
- Stack: **CMYK lub RGB** (pełna paleta)
- TD: wszystkie 1.0 mm
- Max thickness: 2.0 mm

**Co to rozstrzyga:**
- Jeśli error metric = RGB Euclidean:
  - Gray (127,127,127) będzie w środku zakresu depth
  
- Jeśli error metric = LAB:
  - Gray może mieć inną depth (bo LAB jest non-linear)

**Pomiar:**
Zmierz depth dla każdego z 9 kolorów, zrób wykres:
```
depth vs luminance (0.299*R + 0.587*G + 0.114*B)
depth vs LAB L*
depth vs RGB magnitude (sqrt(R² + G² + B²))
```

Która korelacja jest najlepsza = używana metric.

---

#### Image C: White Point Test
```
Solid white image (255, 255, 255)
```

**Settings:**
- Stack: White filament tylko
- TD: 1.0 mm
- Light: **zmień na różne** (Natural 4000K, Cool 6500K, Warm 3000K)

**Co to rozstrzyga:**
Jeśli light temperature wpływa na depth:
- Różne temperatury → różne depth dla tego samego obrazu
- To znaczy, że model uwzględnia spektrum światła

Jeśli depth jest zawsze taka sama:
- Light temperature to tylko UI preview, solver używa [1,1,1]

---

### Dostarczenie Wyników

**Dla każdego testu prześlij:**
1. Screenshot ustawień HueForge (full UI)
2. Wygenerowany STL
3. Colorplan (jeśli applicable)
4. Screenshot z MeshLab/Blender pokazujący Z coordinates

**Ja zrobię:**
- Analiza depth values
- Fitting do modeli matematycznych
- Reverse-engineer dokładnej formuły

---

## EKSPERYMENT 2: Rozkład Depth Na Warstwy Stacka

### Cel
Ustalić, czy HueForge:
- A) Solver tylko total depth, rozkład na warstwy fixed (równo/proporcjonalnie)
- B) Solver depth per layer (optimization)

### Test Case

#### Image: Half-and-Half
```
┌──────────┬──────────┐
│          │          │
│  Color A │ Color B  │
│          │          │
└──────────┴──────────┘
```

**Test 1: A=Red, B=Blue**
- Stack: [White base, Red, Blue]
- TD: wszystkie 1.0 mm

**Test 2: A=Red, B=Red** (control)
- Stack: [White base, Red]
- TD: 1.0 mm

**Pytanie:** 
Dla Test 1:
- Czy Red side ma depth głównie w Red layer?
- Czy Blue side ma depth głównie w Blue layer?

**Jeśli TAK:**
- HueForge robi per-layer optimization (zaawansowane)

**Jeśli NIE (depth jest rozłożone równo):**
- HueForge robi tylko total depth (prostsze)

### Jak to zmierzyć?

**Nie możesz zmierzyć bezpośrednio z STL** (bo STL ma tylko total Z).

**Ale możesz sprawdzić colorplan:**
```
# Dla Red side:
Layer 0-5: White (base)
Layer 6-15: Red    ← czy tu jest więcej warstw?
Layer 16-20: Blue  ← czy tu jest mniej?

# Dla Blue side:
Layer 0-5: White
Layer 6-10: Red    ← mniej
Layer 11-20: Blue  ← więcej
```

**Jeśli colorplan pokazuje różnice per-region:**
- HueForge ma spatial awareness (per-layer optimization)

**Jeśli colorplan jest jednolity dla całego obrazu:**
- HueForge rozkłada równomiernie

---

## EKSPERYMENT 3: Ciągłość vs Kwantowanie Height Map

### Cel
Rozstrzygnąć: czy height map jest float czy kwantowana do layer_height.

### Test Case

#### Image: Smooth Gradient
```
┌─────────────────────────┐
│ 255 ────────────────► 0 │  bardzo płynny gradient
└─────────────────────────┘
```

**Settings:**
- Stack: Black only
- TD: 1.0 mm
- Max thickness: 2.0 mm
- **Layer height: 0.08 mm** (default)
- Width: 100 pikseli (mały obraz dla łatwej analizy)

**Pomiar:**
1. Wygeneruj STL
2. Otwórz w MeshLab
3. Export jako ASCII STL (nie binary!)
4. Przeanalizuj wartości Z w pliku tekstowym

**ASCII STL wygląda tak:**
```
solid name
  facet normal 0 0 1
    outer loop
      vertex 0.0 0.0 0.123456
      vertex 1.0 0.0 0.234567
      vertex 1.0 1.0 0.345678
    endloop
  endfacet
  ...
endsolid
```

**Ekstrahuj wszystkie unikalne wartości Z:**
```python
import re

z_values = set()
with open('gradient.stl', 'r') as f:
    for line in f:
        if 'vertex' in line:
            # vertex X Y Z
            parts = line.strip().split()
            z = float(parts[3])
            z_values.add(z)

z_sorted = sorted(z_values)
differences = [z_sorted[i+1] - z_sorted[i] for i in range(len(z_sorted)-1)]

print(f"Unique Z values: {len(z_values)}")
print(f"Min difference: {min(differences):.6f}")
print(f"Max difference: {max(differences):.6f}")
```

**Interpretacja:**

**Jeśli kwantowane do layer_height:**
```
Unique Z values: ~25 (2.0mm / 0.08mm)
Min difference: 0.080000
Max difference: 0.080000
Wszystkie różnice = 0.08mm (lub wielokrotność)
```

**Jeśli ciągłe (float):**
```
Unique Z values: 100+ (jeden per piksel lub więcej)
Min difference: 0.000001 - 0.001
Max difference: 0.02+
Różnice są nieregularne
```

---

## EKSPERYMENT 4: Spike Removal i Post-Processing

### Cel
Ustalić:
1. Czy HueForge robi smoothing height map
2. Gdzie działa "Spike Removal" slider (pre-processing obrazu vs post-processing height map)

### Test Case A: Spike Removal OFF vs ON

#### Image: Salt-and-Pepper Noise
```
┌─────────────────────┐
│ ▓░▓░░▓░▓░▓░░▓░▓░░▓ │  random black/white pixels
│ ░▓░▓░░▓░▓░░▓░▓░▓░░ │
│ ▓░░▓░▓░░▓░▓░░▓░▓░▓ │
└─────────────────────┘
```

**Settings Test 1:**
- Spike Removal: **OFF** (0%)
- Smoothness: **OFF** (jeśli osobny slider)
- Stack: Black only
- TD: 1.0 mm

**Settings Test 2:**
- Spike Removal: **100%** (max)
- Reszta jak wyżej

**Pomiar:**
1. Wygeneruj oba STL
2. Porównaj number of vertices/faces:
   ```
   meshlab: Filters → Show Current Mesh Info
   ```

**Interpretacja:**

**Jeśli spike removal działa na obrazie (pre-processing):**
- Test 2 będzie miał mniej unikalnych Z values (bo usunięto outliers z obrazu)
- Ale STL geometry może być podobna

**Jeśli spike removal działa na height map (post-processing):**
- Test 2 będzie miał znacznie mniej vertices/faces
- Height map będzie wygładzona (lokalne minima/maxima usunięte)

---

### Test Case B: Sharp Edge Preservation

#### Image: Black Square on White
```
┌─────────────────────┐
│                     │
│     ┌─────┐         │
│     │█████│         │  hard edge
│     │█████│         │
│     └─────┘         │
└─────────────────────┘
```

**Settings:**
- Spike Removal: OFF
- Smoothness: vary (0%, 50%, 100%)

**Pytanie:**
Czy przy Smoothness=100% krawędź kwadratu jest:
- Nadal ostra (steep slope w height map)
- Rozmyta (gradual slope)

**Pomiar:**
Export cross-section profile:
1. MeshLab: Filters → Sampling → Cross Section
2. Export jako punkty (X, Y, Z)
3. Plot Z vs X dla linii przechodzącej przez krawędź

**Jeśli smoothness zachowuje krawędzie:**
```
     ┌─────
    /      
   /       
──┘        sharp rise
```

**Jeśli smoothness rozmywa:**
```
      ╭────
    ╭╯    
  ╭╯      
─╯        gradual slope
```

---

## PODSUMOWANIE: CO DOSTANĘ

**Po wykonaniu wszystkich 4 eksperymentów będę mógł napisać:**

### Dokument 3: "HueForge - Confirmed Specification"

**Zawartość:**
```markdown
## Beer-Lambert Model (CONFIRMED)

Color space: [sRGB / Linear RGB / LAB]
Absorption formula: [exact equation]
Light source: [1,1,1 / 4000K spectrum / other]
Error metric: [RGB Euclidean / LAB ΔE / Weighted]

## Layer Distribution (CONFIRMED)

Method: [Equal / Proportional to TD / Per-layer optimization]
Formula: depth_per_layer = [exact calculation]

## Height Map Properties (CONFIRMED)

Type: [Continuous float / Quantized to layer_height]
Resolution: [sub-layer / layer-aligned]

## Post-Processing (CONFIRMED)

Spike removal: [operates on image / operates on height map]
Smoothness: [gaussian blur σ=X / median filter / other]
Edge handling: [preserved / smoothed]
```

**Plus gotowa implementacja:**
```python
class HueForgeClone:
    """
    100% confirmed implementation based on experiments
    No guessing, only facts
    """
    
    def beer_lambert_model(self, ...):
        # EXACT formulas from experiments
        pass
    
    def optical_solver(self, ...):
        # CONFIRMED method
        pass
    
    def post_processing(self, ...):
        # CONFIRMED filters
        pass
```

---

## CO POTRZEBUJĘ OD CIEBIE

**Dla każdego z 4 eksperymentów:**

1. **Screenshots:**
   - HueForge UI (full window, wszystkie ustawienia widoczne)
   - MeshLab/Blender z zaznaczonymi Z coordinates

2. **Pliki:**
   - Obrazy wejściowe (.png) - mogę je przygotować, ale lepiej jak ty wygenerujesz identyczne
   - STL output
   - Colorplan (if applicable)
   - ASCII STL export (dla Exp 3)

3. **Measurements:**
   - Z values dla kluczowych punktów
   - Vertex/face counts
   - Cross-section data (dla Exp 4)

**Mogę pomóc:**
- Wygenerować test images (Python/PIL)
- Napisać skrypty do analizy STL
- Przygotować mesh analysis tools

**Timeline:**
- Exp 1: ~30 min (3 obrazy × 10 min każdy)
- Exp 2: ~20 min (2 obrazy)
- Exp 3: ~15 min (1 obraz + ASCII export)
- Exp 4: ~30 min (3 obrazy + analysis)

**Total: ~2h pure HueForge work**

Po tym będę mógł napisać definitywną specyfikację i implementację **bez żadnego zgadywania**.

---

*Plan eksperymentów - ready to execute*