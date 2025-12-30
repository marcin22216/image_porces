# Optical Solver - Głęboka Analiza Techniczna
## Od Teorii Beer-Lambert do Implementacji

---

## CZĘŚĆ 1: PROBLEM FUNDAMENTALNY

### Forward Problem (Łatwy)

**Dane:**
- Stack filamentów: [Black, Pink, Indigo, Orange]
- Głębokość każdej warstwy: [d₁, d₂, d₃, d₄] w mm
- Transmission Distance dla każdego: [TD₁, TD₂, TD₃, TD₄]
- Światło wejściowe: białe [1.0, 1.0, 1.0]

**Pytanie:** Jaki kolor RGB zobaczy oko?

**Odpowiedź:** Proste - prawo Beer-Lambert:
```python
def forward_light_transmission(depths, TDs, colors):
    """
    depths: [d_black, d_pink, d_indigo, d_orange] w mm
    TDs: [TD_black, TD_pink, TD_indigo, TD_orange] w mm
    colors: [(R,G,B)_black, (R,G,B)_pink, ...]
    
    Returns: final RGB po przejściu przez wszystkie warstwy
    """
    light = np.array([1.0, 1.0, 1.0])  # białe światło
    
    for i, (depth, TD, color) in enumerate(zip(depths, TDs, colors)):
        # Absorpcja dla każdego kanału RGB
        absorption = 1.0 - color  # im ciemniejszy kolor, tym więcej pochłania
        
        # Beer-Lambert: I = I₀ * exp(-μ * d)
        # gdzie μ = 1/TD (współczynnik absorpcji)
        transmission = np.exp(-depth / TD * absorption)
        
        light *= transmission
    
    return light
```

---

### Inverse Problem (Trudny) - TO JEST HUEFORGE

**Dane:**
- Stack filamentów: [Black, Pink, Indigo, Orange]
- TDs: [0.80, 1.20, 1.00, 1.10]
- Docelowy kolor RGB: [0.5, 0.3, 0.7] (przykład)
- Max thickness: 2.24 mm

**Pytanie:** Jaka musi być **całkowita głębokość** stacka, żeby po przejściu światła przez wszystkie warstwy uzyskać docelowy RGB?

**To jest nieliniowy problem odwrotny.**

---

## CZĘŚĆ 2: METODY ROZWIĄZANIA

### Metoda 1: Optymalizacja Numeryczna (scipy.optimize)

**Zasada:**
```python
from scipy.optimize import minimize

def optical_solver_optimize(target_rgb, stack_colors, TDs, max_thickness):
    """
    Solve: jaka depth daje target_rgb?
    """
    
    def objective(depth):
        """
        Funkcja celu: różnica między symulowanym a docelowym kolorem
        """
        if depth < 0 or depth > max_thickness:
            return 1e6  # penalty za przekroczenie granic
        
        # Rozłóż depth proporcjonalnie na warstwy
        # (założenie: równy podział, ale może być bardziej zaawansowane)
        num_layers = len(stack_colors)
        depth_per_layer = depth / num_layers
        depths = [depth_per_layer] * num_layers
        
        # Forward simulation
        simulated_rgb = forward_light_transmission(depths, TDs, stack_colors)
        
        # Error (Euclidean distance w przestrzeni RGB)
        error = np.linalg.norm(simulated_rgb - target_rgb)
        
        return error
    
    # Optymalizacja
    result = minimize(
        objective,
        x0=max_thickness / 2,  # początkowe zgadnięcie
        bounds=[(0, max_thickness)],
        method='L-BFGS-B'
    )
    
    return result.x[0]  # optymalna depth
```

**Zalety:**
- Uniwersalne (działa dla każdego stacka)
- Precyzyjne (znajduje globalne minimum)
- Nie wymaga pre-computingu

**Wady:**
- Wolne (każdy piksel = oddzielna optymalizacja)
- Dla 1920×1080 = 2M optymalizacji!
- Może utknąć w lokalnym minimum

**Optymalizacja wydajności:**
```python
# Równoległe przetwarzanie
from multiprocessing import Pool

def solve_pixel(args):
    y, x, target_rgb = args
    return optical_solver_optimize(target_rgb, stack, TDs, max_thickness)

with Pool(processes=16) as pool:
    results = pool.map(solve_pixel, pixel_args)
```

---

### Metoda 2: Lookup Table (LUT) + Interpolacja

**Zasada:**
Pre-compute wszystkie możliwe kombinacje depth → color, zapisz w tablicy.

```python
def build_lut(stack_colors, TDs, max_thickness, resolution=1000):
    """
    Build lookup table: depth → RGB
    
    resolution: ile próbek (1000 = krok 0.00224 mm dla max 2.24mm)
    """
    depths = np.linspace(0, max_thickness, resolution)
    lut_rgb = np.zeros((resolution, 3))
    
    for i, depth in enumerate(depths):
        # Equal distribution across layers (simplification)
        num_layers = len(stack_colors)
        depth_per_layer = depth / num_layers
        layer_depths = [depth_per_layer] * num_layers
        
        lut_rgb[i] = forward_light_transmission(layer_depths, TDs, stack_colors)
    
    return depths, lut_rgb


def lut_inverse(target_rgb, depths, lut_rgb):
    """
    Find depth that gives closest RGB to target
    """
    # Euclidean distance do każdego wpisu w LUT
    distances = np.linalg.norm(lut_rgb - target_rgb, axis=1)
    
    # Znajdź najbliższy
    closest_idx = np.argmin(distances)
    
    # Interpolacja dla sub-pixel precision
    if closest_idx > 0 and closest_idx < len(depths) - 1:
        # Linear interpolation między sąsiadami
        # (lub cubic dla lepszej jakości)
        pass
    
    return depths[closest_idx]
```

**Zalety:**
- Bardzo szybkie (O(1) lookup + interpolacja)
- Dla 2M pikseli: sekundy, nie godziny
- Deterministyczne (zawsze ten sam wynik)

**Wady:**
- Wymaga pre-computingu (jednorazowy koszt)
- Pamięć: resolution × 3 floats (1000 × 3 × 4B = 12KB - OK)
- Ograniczona precyzja (zależy od resolution)

**Optymalizacja:**
```python
# 3D LUT dla różnych stacków
lut_cache = {}

def get_or_build_lut(stack_colors, TDs, max_thickness):
    cache_key = (tuple(map(tuple, stack_colors)), tuple(TDs), max_thickness)
    
    if cache_key not in lut_cache:
        lut_cache[cache_key] = build_lut(stack_colors, TDs, max_thickness)
    
    return lut_cache[cache_key]
```

---

### Metoda 3: Analityczna Inwersja (Jeśli Możliwa)

**Dla prostych przypadków (1-2 warstwy) można wyprowadzić wzór analityczny.**

**Przykład: 1 warstwa**
```python
def analytical_inverse_single_layer(target_rgb, color, TD, max_thickness):
    """
    Dla single layer: I_out = I_in * exp(-d/TD * absorption)
    
    Solve for d:
    d = -TD * ln(I_out / I_in) / absorption
    """
    absorption = 1.0 - np.array(color)
    
    # Avoid log(0)
    target_rgb = np.clip(target_rgb, 1e-6, 1.0)
    
    # Inverse Beer-Lambert
    # d = -TD * ln(target / 1.0) / absorption
    depth_per_channel = -TD * np.log(target_rgb) / (absorption + 1e-6)
    
    # Use average across RGB channels (or max, or weighted)
    depth = np.mean(depth_per_channel)
    
    return np.clip(depth, 0, max_thickness)
```

**Dla 2+ warstw:** Bardzo złożone, prawdopodobnie niemożliwe w closed form.

**Zalety:**
- Najszybsze (direct computation)
- Dokładne (bez numerycznych błędów)

**Wady:**
- Tylko dla prostych przypadków
- HueForge ma 4 warstwy → nie applicable

---

## CZĘŚĆ 3: ZAAWANSOWANE ZAGADNIENIA

### 3.1 Równomierne vs Nierównomierne Rozłożenie Głębokości

**Pytanie:** Jak rozłożyć total depth na poszczególne warstwy?

**Opcja A: Równomiernie**
```python
depth_per_layer = total_depth / num_layers
```

**Opcja B: Proporcjonalnie do TD**
```python
# Warstwy z dużym TD "zjadają" więcej głębokości
weights = TDs / np.sum(TDs)
depths = total_depth * weights
```

**Opcja C: Optymalizacja per-layer**
```python
# Dla każdego piksela optymalizuj nie tylko total depth, 
# ale rozkład depth_per_layer
# 
# To jest ZNACZNIE droższe, ale bardziej precyzyjne
```

**HueForge prawdopodobnie robi:** Opcja A lub B (kompromis szybkość/jakość)

---

### 3.2 Przestrzeń Kolorów dla Error Metric

**Pytanie:** W jakiej przestrzeni mierzyć error?

**Opcja A: RGB (Euclidean)**
```python
error = np.linalg.norm(simulated_rgb - target_rgb)
```
- Prosty, szybki
- Ale RGB nie jest perceptual (różnice niewidoczne dla oka mogą być duże numerycznie)

**Opcja B: LAB (Perceptual)**
```python
simulated_lab = rgb_to_lab(simulated_rgb)
target_lab = rgb_to_lab(target_rgb)
error = np.linalg.norm(simulated_lab - target_lab)  # ΔE
```
- Lepiej oddaje percepcję ludzką
- Droższe (konwersja RGB→LAB)

**Opcja C: Weighted RGB**
```python
# Ludzkie oko jest bardziej czułe na zieleń
weights = [0.299, 0.587, 0.114]  # luminance weights
error = np.linalg.norm(weights * (simulated_rgb - target_rgb))
```

**HueForge prawdopodobnie:** LAB lub Weighted RGB

---

### 3.3 Handling Out-of-Gamut Colors

**Problem:** Nie każdy kolor RGB można osiągnąć z danym stackiem.

**Przykład:**
- Stack: [Black, Red]
- Target: Pure Blue [0, 0, 1]
- Niemożliwe! (brak niebieskiego filamentu)

**Rozwiązania:**

**A. Clipping (naiwny)**
```python
if error > threshold:
    return closest_achievable_depth
```

**B. Gamut mapping (zaawansowany)**
```python
# Znajdź najbliższy kolor w gamut
achievable_rgb = find_closest_in_gamut(target_rgb, stack, TDs)
depth = solve_for(achievable_rgb)
```

**C. Dithering (jak inkjet)**
```python
# Zamiast jednego koloru, użyj wzoru (spatial dithering)
# Lub error diffusion (Floyd-Steinberg)
```

**HueForge prawdopodobnie:** A lub B (C byłoby widoczne w STL)

---

## CZĘŚĆ 4: PRZYPADEK TESTOWY (WERYFIKACJA)

### Test 1: Single Color, Gradient

**Input:**
- Stack: [Black only]
- TD: 0.80 mm
- Image: Grayscale gradient (0 → 255)
- Max thickness: 2.24 mm

**Expected behavior:**
```python
# Dla luminance = 0 (czarny):
depth ≈ max_thickness (2.24 mm) - grube = ciemne

# Dla luminance = 255 (biały):
depth ≈ 0 mm - cienkie = jasne (prześwieca tło)

# Dla luminance = 127 (szary):
depth ≈ 1.12 mm - środek
```

**Test:** Czy solver daje taki wynik?

---

### Test 2: Two Colors, Simple Transition

**Input:**
- Stack: [White, Black]
- TDs: [1.5, 0.8]
- Image: Half white, half black (sharp edge)

**Expected:**
```python
# White region:
depth ≈ 0 (tylko biała baza, brak czarnego)

# Black region:
depth ≈ max (gruba warstwa czarnego)

# Edge:
depth = gradient (płynne przejście)
```

---

## CZĘŚĆ 5: PROPOZYCJA IMPLEMENTACJI

### Hybrydowe Podejście (Jakość + Wydajność)

```python
class OpticalSolver:
    def __init__(self, stack_colors, TDs, max_thickness, 
                 use_lut=True, lut_resolution=1000):
        self.stack_colors = stack_colors
        self.TDs = TDs
        self.max_thickness = max_thickness
        
        if use_lut:
            self.depths_lut, self.rgb_lut = self._build_lut(lut_resolution)
        else:
            self.depths_lut = None
    
    def _build_lut(self, resolution):
        """Pre-compute LUT for fast lookup"""
        depths = np.linspace(0, self.max_thickness, resolution)
        rgb_lut = np.zeros((resolution, 3))
        
        for i, depth in enumerate(depths):
            num_layers = len(self.stack_colors)
            depth_per_layer = depth / num_layers
            layer_depths = [depth_per_layer] * num_layers
            
            rgb_lut[i] = self._forward_transmission(layer_depths)
        
        return depths, rgb_lut
    
    def _forward_transmission(self, layer_depths):
        """Forward Beer-Lambert simulation"""
        light = np.array([1.0, 1.0, 1.0])
        
        for depth, TD, color in zip(layer_depths, self.TDs, self.stack_colors):
            absorption = 1.0 - np.array(color)
            transmission = np.exp(-depth / TD * absorption)
            light *= transmission
        
        return light
    
    def solve(self, target_rgb):
        """
        Main solver: target RGB → depth
        
        Strategy:
        1. Try LUT first (fast)
        2. If error > threshold, refine with optimization
        """
        if self.depths_lut is not None:
            # LUT lookup
            depth_lut = self._lut_lookup(target_rgb)
            
            # Verify error
            simulated = self._forward_transmission(
                [depth_lut / len(self.stack_colors)] * len(self.stack_colors)
            )
            error = np.linalg.norm(simulated - target_rgb)
            
            if error < 0.05:  # threshold
                return depth_lut
        
        # Fallback to optimization
        return self._optimize(target_rgb)
    
    def _lut_lookup(self, target_rgb):
        """Fast LUT-based lookup with interpolation"""
        distances = np.linalg.norm(self.rgb_lut - target_rgb, axis=1)
        closest_idx = np.argmin(distances)
        
        # TODO: interpolation for sub-step precision
        
        return self.depths_lut[closest_idx]
    
    def _optimize(self, target_rgb):
        """Slow but accurate optimization"""
        from scipy.optimize import minimize
        
        def objective(depth):
            if depth < 0 or depth > self.max_thickness:
                return 1e6
            
            num_layers = len(self.stack_colors)
            layer_depths = [depth / num_layers] * num_layers
            simulated = self._forward_transmission(layer_depths)
            
            return np.linalg.norm(simulated - target_rgb)
        
        result = minimize(
            objective,
            x0=self.max_thickness / 2,
            bounds=[(0, self.max_thickness)],
            method='L-BFGS-B'
        )
        
        return result.x[0]
```

**Usage:**
```python
# Initialize solver
solver = OpticalSolver(
    stack_colors=[(0,0,0), (1,0.5,0.5), (0.3,0,0.6), (1,0.5,0)],  # CMYK-ish
    TDs=[0.80, 1.20, 1.00, 1.10],
    max_thickness=2.24,
    use_lut=True
)

# Solve for entire image
height_map = np.zeros((H, W), dtype=np.float32)

for y in range(H):
    for x in range(W):
        target_rgb = image[y, x] / 255.0  # normalize
        height_map[y, x] = solver.solve(target_rgb)

# Now height_map is ready for mesher!
```

---

## CZĘŚĆ 6: ODPOWIEDZI NA 5 PYTAŃ

### Odpowiedź 1: Metoda liczenia height

**Prawdopodobnie:** LUT + fallback optimization
- LUT dla 99% pikseli (szybko)
- Optimization dla trudnych przypadków (precyzja)

### Odpowiedź 2: Ciągłość vs kwantowanie

**Prawdopodobnie:** Ciągła w solverze, kwantowana w mesherze
- Solver zwraca float mm
- Mesher zaokrągla do layer_height przy generowaniu G-code (ale STL jest ciągły)

### Odpowiedź 3: Przestrzeń kolorów

**Prawdopodobnie:** LAB lub Weighted RGB
- Error metric w przestrzeni perceptual
- Forward simulation w Linear RGB

### Odpowiedź 4: Rola TD

**Tylko solver** - TD określa optical properties, nie smoothing

### Odpowiedź 5: Przypadek 1 kolor

**Height = f(luminance, TD)** - nie zero, nie pure luminance
- Analytic inversion dla single layer

---

*Dokument techniczny - gotowy do implementacji*