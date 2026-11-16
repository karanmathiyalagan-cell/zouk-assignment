"""
Christmas domes v2: snow globes and hanging baubles.

Input:  product PNGs with transparent backgrounds, in this order:
        sling.png office.png backpack.png tote.png
Output: SnowGlobe_<product>.png / Bauble_<product>.png (352x440, plus @2x),
        SVG sources, and empty frames in <out>/frames/.

Requires:  pip install pillow
           rsvg-convert (librsvg)   macOS: brew install librsvg
                                    Ubuntu: sudo apt install librsvg2-bin

Run:       python christmas_domes_v2.py <folder_with_product_pngs> <output_folder>
"""
import base64, math, random, subprocess, sys
from pathlib import Path
from PIL import Image

PROD, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "frames").mkdir(exist_ok=True)
PRODUCTS = ["sling", "office", "backpack", "tote"]
W, H = 352, 440
GOLD = "#EBCB7A"
CREAM = "#FFF6E0"


def sparkle(x, y, r, fill=GOLD, op=1):
    a = 0.15 * r
    return (f'<path d="M{x},{y-r} Q{x+a},{y-a} {x+r},{y} Q{x+a},{y+a} {x},{y+r} '
            f'Q{x-a},{y+a} {x-r},{y} Q{x-a},{y-a} {x},{y-r}Z" fill="{fill}" opacity="{op}"/>')


def product(name, cx, bottom, max_w, max_h, shadow=0.35, shadow_color="#000", clip=None):
    p = PROD / f"{name}.png"
    pw, ph = Image.open(p).size
    k = min(max_w / pw, max_h / ph)
    w, h = pw * k, ph * k
    b64 = base64.b64encode(p.read_bytes()).decode()
    s = (f'<ellipse cx="{cx}" cy="{bottom-3}" rx="{w*0.47:.1f}" ry="10" fill="{shadow_color}" '
         f'opacity="{shadow}" filter="url(#soft)"/>') if shadow else ""
    s += (f'<image x="{cx-w/2:.1f}" y="{bottom-h:.1f}" width="{w:.1f}" height="{h:.1f}" '
          f'xlink:href="data:image/png;base64,{b64}"/>')
    return f'<g clip-path="url(#{clip})">{s}</g>' if clip else s


COMMON_DEFS = (
    '<filter id="soft" x="-40%" y="-300%" width="180%" height="700%"><feGaussianBlur stdDeviation="6"/></filter>'
    '<filter id="glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="14"/></filter>'
    '<filter id="spec" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="9"/></filter>'
    # brushed-gold: dark edge, bright band, mid, dark edge
    '<linearGradient id="goldH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#A9792A"/>'
    '<stop offset=".3" stop-color="#F8E7AE"/><stop offset=".62" stop-color="#D9B257"/><stop offset="1" stop-color="#9C6E22"/></linearGradient>'
    '<linearGradient id="goldV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3DC98"/>'
    '<stop offset="1" stop-color="#B98A2E"/></linearGradient>'
)


def svg(defs, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {W} {H}" width="{W}" height="{H}"><defs>{COMMON_DEFS}{defs}</defs>{body}</svg>')


# =============================================================== snow globe
GX, GY, GR = 176, 170, 164


def snowfall(seed):
    rnd, pts, out = random.Random(seed), [], ""
    tries = 0
    while len(pts) < 17 and tries < 4000:
        tries += 1
        a, d = rnd.uniform(0, math.tau), (GR - 22) * math.sqrt(rnd.random())
        x, y = GX + d * math.cos(a), GY + d * math.sin(a)
        if y > 236 or (x < 150 and y < 120 and (x - 40) + (y - 20) < 160):   # keep clear of snow line and glass highlight
            continue
        if any(math.hypot(x - px, y - py) < 36 for px, py in pts):
            continue
        pts.append((x, y))
    for i, (x, y) in enumerate(pts):
        if i % 6 == 0:
            out += sparkle(round(x), round(y), rnd.choice([6, 7, 8]), op=.95)
        else:
            r = rnd.choice([1.8, 2.4, 2.4, 3.2, 4.2])
            out += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" opacity="{0.55 + 0.11 * r:.2f}"/>'
    return out


GLOBE_DEFS = (
    f'<radialGradient id="sky" gradientUnits="userSpaceOnUse" cx="{GX}" cy="{GY+34}" r="{GR+40}">'
    '<stop offset="0" stop-color="#2B8696"/><stop offset=".55" stop-color="#14596A"/><stop offset="1" stop-color="#08323D"/></radialGradient>'
    f'<radialGradient id="rim" gradientUnits="userSpaceOnUse" cx="{GX}" cy="{GY}" r="{GR}">'
    '<stop offset=".80" stop-color="#fff" stop-opacity="0"/><stop offset=".96" stop-color="#fff" stop-opacity=".20"/>'
    '<stop offset="1" stop-color="#fff" stop-opacity=".42"/></radialGradient>'
    '<linearGradient id="snowF" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#E3EEF3"/></linearGradient>'
    '<linearGradient id="base" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#AE2440"/><stop offset="1" stop-color="#6E1024"/></linearGradient>'
    '<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
    '<stop offset=".28" stop-color="#fff" stop-opacity=".20"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>'
    f'<clipPath id="gclip"><circle cx="{GX}" cy="{GY}" r="{GR}"/></clipPath>'
)
BASE = "M70,344 L282,344 L306,414 Q310,426 298,426 L54,426 Q42,426 46,414Z"


def globe_layers(seed):
    back = (
        f'<circle cx="{GX}" cy="{GY}" r="{GR}" fill="url(#sky)"/>'
        f'<g clip-path="url(#gclip)">'
        f'<ellipse cx="{GX}" cy="232" rx="118" ry="78" fill="#BFF3F5" opacity=".20" filter="url(#glow)"/>'
        + snowfall(seed) +
        # far drift (cool), then near drift behind the product
        '<path d="M0,270 C50,246 96,250 150,262 S262,278 352,250 L352,360 L0,360Z" fill="#A9CCD6"/>'
        '<path d="M0,286 C64,262 120,272 176,280 S286,270 352,282 L352,360 L0,360Z" fill="#D8E9EE"/>'
        '</g>')
    front = (
        f'<g clip-path="url(#gclip)">'
        '<path d="M0,304 C58,286 118,296 176,300 S292,288 352,302 L352,360 L0,360Z" fill="url(#snowF)"/></g>'
        # glass: rim light, crescent highlight, glint, lower reflection
        f'<circle cx="{GX}" cy="{GY}" r="{GR}" fill="url(#rim)"/>'
        '<path d="M44,112 A146,146 0 0 1 134,30 A520,520 0 0 0 44,112Z" fill="#fff" opacity=".42"/>'
        '<circle cx="150" cy="28" r="3.6" fill="#fff" opacity=".6"/>'
        '<path d="M300,236 A140,140 0 0 1 262,282" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".22"/>'
        f'<circle cx="{GX}" cy="{GY}" r="{GR+1.5}" fill="none" stroke="url(#goldV)" stroke-width="3"/>'
        # base: gold collar, maroon body with sheen, gold foot
        '<rect x="82" y="322" width="188" height="26" rx="9" fill="url(#goldH)"/>'
        '<rect x="82" y="341" width="188" height="7" fill="#7A5518" opacity=".35"/>'
        f'<path d="{BASE}" fill="url(#base)"/><path d="{BASE}" fill="url(#sheen)"/>'
        '<path d="M66,356 L286,356" stroke="#EBCB7A" stroke-width="1.6" opacity=".8"/>'
        '<rect x="34" y="418" width="284" height="18" rx="9" fill="url(#goldH)"/>'
        + sparkle(176, 388, 12))
    return back, front


def globe(name, i):
    back, front = globe_layers(40 + i)
    box = {"sling": (228, 150), "office": (214, 160), "backpack": (150, 204), "tote": (206, 172)}[name]
    return svg(GLOBE_DEFS, back + product(name, GX, 306, *box, shadow=0.30, shadow_color="#0A3A47", clip="gclip") + front)


# =============================================================== bauble
BX, BY, BR = 176, 264, 166
PALETTE = [("#D2334F", "#A41D36", "#5C0D1E", "#3F0713"),      # maroon
           ("#36A06C", "#1D7549", "#0B4329", "#062B19")]      # green


def bauble_layers(i):
    hi, mid, lo, shade = PALETTE[i % 2]
    defs = (
        f'<radialGradient id="ball" gradientUnits="userSpaceOnUse" cx="{BX-52}" cy="{BY-70}" r="{BR*1.55}">'
        f'<stop offset="0" stop-color="{hi}"/><stop offset=".42" stop-color="{mid}"/><stop offset="1" stop-color="{lo}"/></radialGradient>'
        f'<radialGradient id="brim" gradientUnits="userSpaceOnUse" cx="{BX}" cy="{BY}" r="{BR}">'
        f'<stop offset=".78" stop-color="{shade}" stop-opacity="0"/><stop offset="1" stop-color="{shade}" stop-opacity=".55"/></radialGradient>'
        f'<clipPath id="bclip"><circle cx="{BX}" cy="{BY}" r="{BR}"/></clipPath>')
    ribs = "".join(f'<line x1="{x}" y1="66" x2="{x}" y2="92" stroke="#8A6218" stroke-width="1.4" opacity=".45"/>' for x in range(156, 200, 8))
    scallops = \
        "".join(f'<circle cx="{153 + k * 9.2:.1f}" cy="94" r="5.2" fill="#C99C3F"/>' for k in range(6))
    back = (
        # string, loop, cap
        '<line x1="176" y1="0" x2="176" y2="40" stroke="#C39A3F" stroke-width="2.4"/>'
        '<circle cx="176" cy="50" r="10.5" fill="none" stroke="url(#goldV)" stroke-width="4"/>'
        + scallops +
        '<rect x="148" y="60" width="56" height="34" rx="7" fill="url(#goldH)"/>' + ribs +
        '<rect x="148" y="60" width="56" height="6" rx="3" fill="#FFF3C9" opacity=".7"/>'
        # ball with shaded rim
        f'<circle cx="{BX}" cy="{BY}" r="{BR}" fill="url(#ball)"/>'
        f'<circle cx="{BX}" cy="{BY}" r="{BR}" fill="url(#brim)"/>'
        # gold detailing: fine ring + beaded ring
        f'<circle cx="{BX}" cy="{BY}" r="{BR-13}" fill="none" stroke="{GOLD}" stroke-width="1.8" opacity=".95"/>'
        f'<circle cx="{BX}" cy="{BY}" r="{BR-23}" fill="none" stroke="{GOLD}" stroke-width="3.4" stroke-linecap="round" '
        f'stroke-dasharray="0 11.23" opacity=".9"/>'
        # soft specular + crisp glint
        f'<g clip-path="url(#bclip)"><ellipse cx="112" cy="176" rx="50" ry="24" transform="rotate(-38 112 176)" fill="#fff" opacity=".34" filter="url(#spec)"/>'
        f'<path d="M300,300 A132,132 0 0 1 244,376" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".10"/></g>'
        '<path d="M70,196 A126,126 0 0 1 112,146 A420,420 0 0 0 70,196Z" fill="#fff" opacity=".5"/>'
        + sparkle(176, 142, 9) + sparkle(84, 276, 6, op=.9) + sparkle(270, 262, 6, op=.9))
    return defs, back, shade


def bauble(name, i):
    defs, back, shade = bauble_layers(i)
    box = {"sling": (258, 168), "office": (246, 182), "backpack": (164, 228), "tote": (234, 196)}[name]
    bottom = {"sling": 362, "office": 368, "backpack": 388, "tote": 376}[name]
    return svg(defs, back + product(name, BX, bottom, *box, shadow=0.55, shadow_color=shade))


# =============================================================== render
def render(svg_text, path, width):
    path.with_suffix(".svg").write_text(svg_text)
    subprocess.run(["rsvg-convert", "-w", str(width), "-o", str(path), str(path.with_suffix(".svg"))], check=True)


CONCEPTS = {"SnowGlobe": globe, "Bauble": bauble}
for cname, fn in CONCEPTS.items():
    for i, p in enumerate(PRODUCTS):
        big = OUT / f"{cname}_{p}@2x.png"
        render(fn(p, i), big, 704)
        Image.open(big).resize((W, H), Image.LANCZOS).save(OUT / f"{cname}_{p}.png")
        big.with_suffix(".svg").unlink()

# empty frames; the globe is split into back and front so a product can sit between them
gb, gf = globe_layers(40)
render(svg(GLOBE_DEFS, gb), OUT / "frames" / "SnowGlobe_back@4x.png", 1408)
render(svg(GLOBE_DEFS, gf), OUT / "frames" / "SnowGlobe_front@4x.png", 1408)
for i, col in enumerate(["red", "green"]):
    d, b, _ = bauble_layers(i)
    render(svg(d, b), OUT / "frames" / f"Bauble_{col}@4x.png", 1408)

sheet = Image.new("RGBA", (4 * 704 + 5 * 60, 2 * 880 + 3 * 60), (255, 255, 255, 255))
for r, cname in enumerate(CONCEPTS):
    for c, p in enumerate(PRODUCTS):
        sheet.alpha_composite(Image.open(OUT / f"{cname}_{p}@2x.png"), (60 + c * 764, 60 + r * 940))
sheet.resize((sheet.width // 2, sheet.height // 2), Image.LANCZOS).convert("RGB").save(OUT / "tiles_sheet_v2.png")
print("ok")
