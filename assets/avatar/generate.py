import math

# --- monogram, drawn as stroked paths (font-independent) --------------------
# Natural bounding box of the artwork below, including stroke width:
MONO_BOX = (163, 135, 509, 379)          # x0, y0, x1, y1
MX = (MONO_BOX[0] + MONO_BOX[2]) / 2      # 336.0
MY = (MONO_BOX[1] + MONO_BOX[3]) / 2      # 257.0
MONO_W = MONO_BOX[2] - MONO_BOX[0]        # 346.0

def monogram(color, sw=46):
    return f'''
  <g fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"
     stroke-linejoin="round">
    <path d="M 298 158 V 286 A 56 56 0 0 1 186 286" />
    <path d="M 366 158 V 356" />
    <path d="M 476 158 L 382 256" />
    <path d="M 404 236 L 486 356" />
  </g>'''

def place(color, target_w, cx=256, cy=256, sw=46):
    """Scale the monogram to target_w and centre its bbox on (cx, cy).
    translate() is written to apply AFTER scale(), so it is not itself scaled."""
    s = target_w / MONO_W
    tx, ty = cx - s * MX, cy - s * MY
    return f'<g transform="translate({tx:.2f},{ty:.2f}) scale({s:.4f})">{monogram(color, sw)}</g>'

DEEP, ACCENT, DEEP_A, LIGHT = "#0d1117", "#2f81f7", "#0969da", "#e6edf3"

# ---- A: shield -------------------------------------------------------------
A = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs><linearGradient id="ga" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{ACCENT}"/><stop offset="1" stop-color="{DEEP_A}"/>
  </linearGradient></defs>
  <rect width="512" height="512" rx="104" fill="{DEEP}"/>
  <path d="M 256 58 L 420 118 V 258 C 420 348 348 410 256 448
           C 164 410 92 348 92 258 V 118 Z" fill="url(#ga)"/>
  {place(LIGHT, 216, cy=246)}
</svg>'''

# ---- B: hex supply-chain node ---------------------------------------------
pts, nodes = [], []
for a in range(-90, 270, 60):
    x, y = 256 + 190*math.cos(math.radians(a)), 256 + 190*math.sin(math.radians(a))
    pts.append(f"{x:.1f},{y:.1f}")
    nodes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="25" fill="{ACCENT}"/>')
B = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <rect width="512" height="512" rx="104" fill="{DEEP}"/>
  <polygon points="{' '.join(pts)}" fill="none" stroke="{DEEP_A}" stroke-width="17"/>
  {''.join(nodes)}
  {place(LIGHT, 232)}
</svg>'''

# ---- C: terminal -----------------------------------------------------------
# chevron occupies x 108..182; monogram centred at 322 so the pair reads as one line
C = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <rect width="512" height="512" rx="104" fill="{DEEP}"/>
  <rect x="36" y="36" width="440" height="440" rx="76" fill="none"
        stroke="{DEEP_A}" stroke-width="15"/>
  <g fill="none" stroke="{ACCENT}" stroke-width="38" stroke-linecap="round" stroke-linejoin="round">
    <path d="M 116 202 L 182 256 L 116 310"/>
  </g>
  {place(LIGHT, 196, cx=326)}
</svg>'''

# ---- D: chain link ---------------------------------------------------------
D = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs><linearGradient id="gd" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{ACCENT}"/><stop offset="1" stop-color="{DEEP_A}"/>
  </linearGradient></defs>
  <rect width="512" height="512" rx="104" fill="url(#gd)"/>
  <circle cx="256" cy="256" r="198" fill="none" stroke="{LIGHT}" stroke-width="13" opacity="0.28"/>
  <circle cx="256" cy="256" r="198" fill="none" stroke="{DEEP}" stroke-width="13"
          stroke-dasharray="64 60" stroke-linecap="round" opacity="0.5"/>
  <circle cx="256" cy="256" r="168" fill="{DEEP}" opacity="0.18"/>
  {place("#ffffff", 246)}
</svg>'''

for name, svg in [("a-shield",A),("b-hex",B),("c-terminal",C),("d-chain",D)]:
    open(f"{name}.svg","w").write(svg)
    open(f"{name}.html","w").write(
        f'<html><body style="margin:0;width:512px;height:512px">{svg}</body></html>')
print("regenerated 4 variants")
