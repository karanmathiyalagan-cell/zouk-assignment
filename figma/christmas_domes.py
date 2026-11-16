#!/usr/bin/env python3
"""
Christmas category tiles ("domes") in four versions:

    garland   cream box, green/red frame, pine garland, five hanging baubles
    minimal   cream box, thin green/red outline, three hanging baubles
    red       red box, three white baubles
    premium   wine-red card, gold hairline, pearl ornament, outlined bag, optional gold tag

Input:  product images with a transparent background (PNG), one per tile.
Output: for every version and product, an SVG tile (352x440) and, when the
        `rsvg-convert` tool is installed, PNGs at 352x440 and 704x880.
        Empty frames (no product) are written to <out>/frames/.
"""
import argparse
import base64
import io
import math
import random
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageFilter

W, H = 352, 440                      # tile size

RED = ("#E2405A", "#B3203A", "#640E20")
GREEN = ("#3DAE76", "#1D7549", "#0B4329")
GOLD = ("#FBEBB5", "#DDB65A", "#9C6E22")
WHITE = ("#FFFFFF", "#F6F2EA", "#CFC6B6")

CREAM_PANEL = ("#FFFDF7", "#FAF0DC", "#F0DDBB")
RED_PANEL = ("#DC3F57", "#C02640", "#931A31")
GREEN_FRAME = ("#1F7A50", "#0E4F33")
RED_FRAME = ("#B3203A", "#7C1226")
DARK_RED_FRAME = ("#8E1A30", "#6B0F22")

VERSIONS = {
    "garland": dict(
        frames=[GREEN_FRAME, RED_FRAME], frame_width=9, radius=(34, 26),
        panel=CREAM_PANEL, gold_line=True, sparkles=True, garland=True,
        accents=[(RED, GREEN), (GREEN, RED)],
        balls=[(50, 110, 22, "A"), (108, 78, 16, GOLD), (176, 100, 20, "B"), (244, 74, 15, GOLD), (302, 116, 22, "A")],
        string="#B98A2E", ball_shadow=("#5B3A1E", 0.16), bag_shadow=("#5B3A1E", 0.30),
    ),
    "minimal": dict(
        frames=[GREEN_FRAME, RED_FRAME], frame_width=5, radius=(32, 27),
        panel=CREAM_PANEL, gold_line=False, sparkles=False, garland=False,
        accents=[(RED, GREEN), (GREEN, RED)],
        balls=[(96, 76, 17, GOLD), (176, 110, 22, "A"), (258, 88, 19, "B")],
        string="#B98A2E", ball_shadow=("#5B3A1E", 0.16), bag_shadow=("#5B3A1E", 0.30),
    ),
    "red": dict(
        frames=[DARK_RED_FRAME], frame_width=5, radius=(32, 27),
        panel=RED_PANEL, gold_line=False, sparkles=False, garland=False,
        accents=[(WHITE, WHITE)],
        balls=[(96, 76, 17, WHITE), (176, 110, 22, WHITE), (258, 88, 19, WHITE)],
        string="#F3DC98", ball_shadow=("#4A0814", 0.35), bag_shadow=("#4A0814", 0.50),
    ),
}

BAG_CENTER_X, BAG_BOTTOM_Y = 176, 392
BAG_MAX_W, BAG_MAX_H, BAG_MAX_AREA = 270, 238, 48_000

DEFS = (
    '<filter id="soft" x="-40%" y="-300%" width="180%" height="700%"><feGaussianBlur stdDeviation="6"/></filter>'
    '<filter id="ballsh" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="4"/></filter>'
    '<linearGradient id="goldH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#A9792A"/>'
    '<stop offset=".3" stop-color="#F8E7AE"/><stop offset=".62" stop-color="#D9B257"/><stop offset="1" stop-color="#9C6E22"/></linearGradient>'
    '<linearGradient id="goldV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3DC98"/>'
    '<stop offset="1" stop-color="#B98A2E"/></linearGradient>'
)


def sparkle(x, y, r, fill, opacity=1.0):
    a = 0.15 * r
    return (f'<path d="M{x},{y-r} Q{x+a},{y-a} {x+r},{y} Q{x+a},{y+a} {x},{y+r} '
            f'Q{x-a},{y+a} {x-r},{y} Q{x-a},{y-a} {x},{y-r}Z" fill="{fill}" opacity="{opacity}"/>')


def garland_y(x):
    t = (x - 12) / 328
    return 25 + 14 * abs(math.sin(t * math.pi * 2)) ** 0.9


def garland(seed):
    rnd = random.Random(seed)
    greens = ["#0F5A38", "#1D7549", "#2E9A62", "#17694A"]
    out = ""
    for layer in range(2):
        x = 6
        while x < 348:
            y = garland_y(x)
            for side in (-1, 1):
                angle = math.radians(rnd.uniform(35, 80)) * side + math.radians(90)
                length = rnd.uniform(14, 21) * (1 if layer == 0 else 0.8)
                colour = greens[rnd.randrange(2)] if layer == 0 else greens[2 + rnd.randrange(2)]
                dx, dy = math.cos(angle) * length, abs(math.sin(angle) * length) * side
                out += (f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x+dx:.1f}" y2="{y+dy:.1f}" stroke="{colour}" '
                        f'stroke-width="{3.4 if layer == 0 else 2.6}" stroke-linecap="round"/>')
            x += rnd.uniform(3.2, 4.6)
    for bx in (34, 78, 140, 212, 274, 318):
        by = garland_y(bx) + rnd.uniform(-3, 5)
        out += (f'<circle cx="{bx}" cy="{by:.1f}" r="4.2" fill="#D9263F"/>'
                f'<circle cx="{bx-1.2}" cy="{by-1.4:.1f}" r="1.2" fill="#fff" opacity=".8"/>')
    return out


def bauble(index, x, cy, r, colour, string_top, cfg):
    hi, mid, lo = colour
    gid = f"ball{index}"
    defs = (f'<radialGradient id="{gid}" gradientUnits="userSpaceOnUse" cx="{x-r*0.35:.1f}" cy="{cy-r*0.4:.1f}" r="{r*1.5:.1f}">'
            f'<stop offset="0" stop-color="{hi}"/><stop offset=".5" stop-color="{mid}"/><stop offset="1" stop-color="{lo}"/></radialGradient>')
    cap_w, cap_h = r * 0.5, r * 0.34
    sh_colour, sh_opacity = cfg["ball_shadow"]
    hx, hy = x - r * 0.36, cy - r * 0.42
    shapes = (
        f'<line x1="{x}" y1="{string_top:.1f}" x2="{x}" y2="{cy-r-cap_h+1:.1f}" stroke="{cfg["string"]}" stroke-width="1.8"/>'
        f'<ellipse cx="{x+2}" cy="{cy+r*0.2:.1f}" rx="{r}" ry="{r}" fill="{sh_colour}" opacity="{sh_opacity}" filter="url(#ballsh)"/>'
        f'<rect x="{x-cap_w/2:.1f}" y="{cy-r-cap_h+1:.1f}" width="{cap_w:.1f}" height="{cap_h+2:.1f}" rx="2" fill="url(#goldH)"/>'
        f'<circle cx="{x}" cy="{cy}" r="{r}" fill="url(#{gid})"/>'
        f'<ellipse cx="{hx:.1f}" cy="{hy:.1f}" rx="{r*0.26:.1f}" ry="{r*0.15:.1f}" '
        f'transform="rotate(-35 {hx:.1f} {hy:.1f})" fill="#fff" opacity=".6"/>')
    return defs, shapes


def bag(image_path, cfg):
    pw, ph = Image.open(image_path).size
    k = min(BAG_MAX_W / pw, BAG_MAX_H / ph)
    k = min(k, math.sqrt(BAG_MAX_AREA / (pw * ph)))
    w, h = pw * k, ph * k
    data = base64.b64encode(Path(image_path).read_bytes()).decode()
    sh_colour, sh_opacity = cfg["bag_shadow"]
    return (
        f'<ellipse cx="{BAG_CENTER_X}" cy="{BAG_BOTTOM_Y-3}" rx="{w*0.47:.1f}" ry="10" fill="{sh_colour}" '
        f'opacity="{sh_opacity}" filter="url(#soft)"/>'
        f'<image x="{BAG_CENTER_X-w/2:.1f}" y="{BAG_BOTTOM_Y-h:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'xlink:href="data:image/png;base64,{data}"/>')


def tile(version, index=0, image_path=None):
    cfg = VERSIONS[version]
    f_top, f_bottom = cfg["frames"][index % len(cfg["frames"])]
    accent_a, accent_b = cfg["accents"][index % len(cfg["accents"])]
    inset = cfg["frame_width"]
    r_out, r_in = cfg["radius"]
    p0, p1, p2 = cfg["panel"]

    defs = DEFS + (
        f'<linearGradient id="frame" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{f_top}"/>'
        f'<stop offset="1" stop-color="{f_bottom}"/></linearGradient>'
        f'<radialGradient id="panel" gradientUnits="userSpaceOnUse" cx="176" cy="270" r="300">'
        f'<stop offset="0" stop-color="{p0}"/><stop offset=".5" stop-color="{p1}"/><stop offset="1" stop-color="{p2}"/></radialGradient>'
        f'<clipPath id="pclip"><rect x="{inset}" y="{inset}" width="{W-2*inset}" height="{H-2*inset}" rx="{r_in}"/></clipPath>')

    body = (f'<rect x="0" y="0" width="{W}" height="{H}" rx="{r_out}" fill="url(#frame)"/>'
            f'<rect x="{inset}" y="{inset}" width="{W-2*inset}" height="{H-2*inset}" rx="{r_in}" fill="url(#panel)"/>')
    if cfg["gold_line"]:
        body += (f'<rect x="{inset+7}" y="{inset+7}" width="{W-2*inset-14}" height="{H-2*inset-14}" rx="{r_in-6}" '
                 f'fill="none" stroke="url(#goldV)" stroke-width="2.2"/>')
    if cfg["sparkles"]:
        body += (sparkle(34, 236, 7, "#9B1B33", .8) + sparkle(320, 250, 7, "#9B1B33", .8)
                 + sparkle(38, 402, 6, "#C99C3F") + sparkle(314, 402, 6, "#C99C3F"))

    if image_path:
        body += bag(image_path, cfg)

    hanging = ""
    for n, (x, cy, r, colour) in enumerate(cfg["balls"]):
        colour = {"A": accent_a, "B": accent_b}.get(colour, colour)
        string_top = garland_y(x) + 4 if cfg["garland"] else inset - 4
        d, shapes = bauble(n, x, cy, r, colour, string_top, cfg)
        defs += d
        hanging += shapes
    if cfg["garland"]:
        hanging += garland(11 + index)
    body += f'<g clip-path="url(#pclip)">{hanging}</g>'

    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {W} {H}" width="{W}" height="{H}"><defs>{defs}</defs>{body}</svg>')


PREMIUM_OUTLINE = 5.0

PREMIUM_DEFS = (
    '<filter id="soft" x="-40%" y="-300%" width="180%" height="700%"><feGaussianBlur stdDeviation="7"/></filter>'
    '<filter id="blur10" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="10"/></filter>'
    '<filter id="blur4" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="4"/></filter>'
    '<filter id="blur2" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="2"/></filter>'
    '<linearGradient id="card" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#A5182E"/>'
    '<stop offset=".55" stop-color="#84122A"/><stop offset="1" stop-color="#560A19"/></linearGradient>'
    '<radialGradient id="spot" gradientUnits="userSpaceOnUse" cx="176" cy="292" r="210">'
    '<stop offset="0" stop-color="#E0506A" stop-opacity=".85"/><stop offset=".5" stop-color="#C02A45" stop-opacity=".35"/>'
    '<stop offset="1" stop-color="#C02A45" stop-opacity="0"/></radialGradient>'
    '<radialGradient id="vig" gradientUnits="userSpaceOnUse" cx="176" cy="230" r="300">'
    '<stop offset=".55" stop-color="#2A0309" stop-opacity="0"/><stop offset="1" stop-color="#2A0309" stop-opacity=".55"/></radialGradient>'
    '<linearGradient id="sheen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/>'
    '<stop offset=".22" stop-color="#fff" stop-opacity="0"/></linearGradient>'
    '<linearGradient id="goldH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B8862D"/>'
    '<stop offset=".28" stop-color="#FBEDB9"/><stop offset=".6" stop-color="#E2BC62"/><stop offset="1" stop-color="#A9792A"/></linearGradient>'
    '<linearGradient id="goldV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7E3A4"/>'
    '<stop offset="1" stop-color="#B98A2E"/></linearGradient>'
    '<linearGradient id="foil" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F9E9B0"/>'
    '<stop offset=".45" stop-color="#E4BE66"/><stop offset=".7" stop-color="#F6E2A0"/><stop offset="1" stop-color="#C4952F"/></linearGradient>'
    '<linearGradient id="floor" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F7E3A4" stop-opacity="0"/>'
    '<stop offset=".5" stop-color="#F7E3A4" stop-opacity=".95"/><stop offset="1" stop-color="#F7E3A4" stop-opacity="0"/></linearGradient>'
    '<radialGradient id="pearl" gradientUnits="userSpaceOnUse" cx="252" cy="70" r="92">'
    '<stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#F4EFE6"/><stop offset=".8" stop-color="#D9CFBF"/>'
    '<stop offset="1" stop-color="#B9AC98"/></radialGradient>'
    '<radialGradient id="pearlrim" gradientUnits="userSpaceOnUse" cx="268" cy="92" r="46">'
    '<stop offset=".82" stop-color="#F3B6BF" stop-opacity="0"/><stop offset="1" stop-color="#F3B6BF" stop-opacity=".55"/></radialGradient>'
    '<radialGradient id="gball" gradientUnits="userSpaceOnUse" cx="322" cy="146" r="34">'
    '<stop offset="0" stop-color="#FFF4C8"/><stop offset=".5" stop-color="#E0B95E"/><stop offset="1" stop-color="#946A20"/></radialGradient>'
    '<clipPath id="cardclip"><rect x="0" y="0" width="352" height="440" rx="36"/></clipPath>'
    '<clipPath id="pearlclip"><circle cx="268" cy="92" r="46"/></clipPath>'
)


def snowflake(cx, cy, r, stroke="#C9A24B", width=1.5, op=0.9, rot=0):
    d = ""
    for k in range(6):
        a = math.radians(rot + 60 * k)
        ux, uy = math.cos(a), math.sin(a)
        d += f"M{cx:.1f},{cy:.1f} L{cx+ux*r:.1f},{cy+uy*r:.1f} "
        for frac, bl in ((0.45, 0.28), (0.72, 0.2)):
            px, py = cx + ux * r * frac, cy + uy * r * frac
            for s in (-1, 1):
                b = a + s * math.radians(55)
                d += f"M{px:.1f},{py:.1f} L{px+math.cos(b)*r*bl:.1f},{py+math.sin(b)*r*bl:.1f} "
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" opacity="{op}"/>'


def outlined(path, r):
    im = Image.open(path).convert("RGBA")
    pad = int(round(2 * r))
    big = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    big.alpha_composite(im, (pad, pad))
    a = big.getchannel("A").point(lambda v: 255 if v > 90 else 0)
    grow = a.filter(ImageFilter.GaussianBlur(r)).point(lambda v: 255 if v > 18 else 0).filter(ImageFilter.GaussianBlur(1.2))
    out = Image.new("RGBA", big.size, (255, 255, 255, 0)); out.putalpha(grow)
    out.alpha_composite(big)
    buf = io.BytesIO(); out.save(buf, "PNG")
    return buf.getvalue()


def premium_bag(image_path):
    p = Path(image_path)
    pw, ph = Image.open(p).size
    k = min(262 / pw, 226 / ph)
    k = min(k, math.sqrt(46_000 / (pw * ph)))
    w, h = pw * k, ph * k
    pad = PREMIUM_OUTLINE * 2
    data = base64.b64encode(outlined(p, PREMIUM_OUTLINE / k)).decode()
    bottom = 384
    return (
        f'<ellipse cx="176" cy="{bottom+2}" rx="{w*0.5:.1f}" ry="12" fill="#2A0309" opacity=".7" filter="url(#soft)"/>'
        f'<image x="{176-w/2-pad:.1f}" y="{bottom-h-pad:.1f}" width="{w+2*pad:.1f}" height="{h+2*pad:.1f}" '
        f'xlink:href="data:image/png;base64,{data}"/>')


def premium_tag(text):
    x, y, w, h = 24, 26, 136, 46
    return (
        f'<rect x="{x+1}" y="{y+4}" width="{w}" height="{h}" rx="12" fill="#2A0309" opacity=".45" filter="url(#blur4)"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="url(#foil)"/>'
        f'<rect x="{x+3.5}" y="{y+3.5}" width="{w-7}" height="{h-7}" rx="9" fill="none" stroke="#8A5E16" stroke-width="1" opacity=".55"/>'
        f'<text x="{x+w/2+1.5}" y="{y+h/2+10.2}" text-anchor="middle" font-family="Inter" font-weight="900" '
        f'font-size="28" letter-spacing="3" fill="#6B0F22">{text}</text>')


def premium_card():
    return (
        '<rect x="0" y="0" width="352" height="440" rx="36" fill="url(#card)"/>'
        '<g clip-path="url(#cardclip)">'
        '<rect x="0" y="0" width="352" height="440" fill="url(#spot)"/>'
        '<rect x="0" y="0" width="352" height="440" fill="url(#vig)"/>'
        '<rect x="0" y="0" width="352" height="440" fill="url(#sheen)"/>'
        '</g>'
        '<rect x="8.5" y="8.5" width="335" height="423" rx="28.5" fill="none" stroke="url(#goldV)" stroke-width="1.4" opacity=".9"/>'
        '<ellipse cx="176" cy="398" rx="120" ry="7" fill="#F7C9A4" opacity=".35" filter="url(#blur4)"/>'
        '<rect x="56" y="397.2" width="240" height="1.6" fill="url(#floor)"/>'
        + sparkle(40, 196, 6, "#F7E3A4", .9) + sparkle(318, 228, 5, "#F7E3A4", .8) + sparkle(64, 120, 4, "#F7E3A4", .6)
        + sparkle(196, 150, 4, "#F7E3A4", .55) + sparkle(304, 404, 5, "#F7E3A4", .75) + sparkle(46, 408, 4, "#F7E3A4", .6))


def premium_ornaments():
    cx, cy, r = 268, 92, 46
    return (
        '<g clip-path="url(#cardclip)">'
        '<line x1="330" y1="0" x2="330" y2="118" stroke="#E2BC62" stroke-width="1.3"/>'
        '<ellipse cx="333" cy="152" rx="20" ry="20" fill="#2A0309" opacity=".45" filter="url(#blur4)"/>'
        '<rect x="325.5" y="117" width="9" height="8" rx="1.5" fill="url(#goldH)"/>'
        '<circle cx="330" cy="144" r="20" fill="url(#gball)"/>'
        '<ellipse cx="323" cy="136" rx="5" ry="3" transform="rotate(-35 323 136)" fill="#fff" opacity=".7"/>'
        f'<line x1="{cx}" y1="0" x2="{cx}" y2="26" stroke="#E2BC62" stroke-width="1.5"/>'
        f'<ellipse cx="{cx+5}" cy="{cy+10}" rx="{r}" ry="{r}" fill="#2A0309" opacity=".5" filter="url(#blur10)"/>'
        f'<circle cx="{cx}" cy="29" r="6" fill="none" stroke="url(#goldV)" stroke-width="2.4"/>'
        f'<rect x="{cx-12}" y="34" width="24" height="15" rx="3.5" fill="url(#goldH)"/>'
        + "".join(f'<line x1="{cx+dx}" y1="36" x2="{cx+dx}" y2="48" stroke="#8A5E16" stroke-width="1" opacity=".45"/>' for dx in (-6, 0, 6)) +
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#pearl)"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#pearlrim)"/>'
        f'<g clip-path="url(#pearlclip)">'
        + snowflake(cx + 6, cy + 6, 21, rot=12)
        + snowflake(cx - 22, cy + 24, 9, width=1.1, op=.7, rot=30)
        + snowflake(cx + 30, cy - 18, 8, width=1.1, op=.6)
        + sparkle(cx - 14, cy - 4, 4, "#C9A24B", .7) + sparkle(cx + 24, cy + 30, 3.4, "#C9A24B", .7) +
        '</g>'
        f'<ellipse cx="{cx-17}" cy="{cy-20}" rx="13" ry="7" transform="rotate(-38 {cx-17} {cy-20})" fill="#fff" opacity=".95" filter="url(#blur2)"/>'
        '</g>')


def premium_tile(image_path=None, label=None):
    body = premium_card()
    if image_path:
        body += premium_bag(image_path)
    body += premium_ornaments()
    if label:
        body += premium_tag(label)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {W} {H}" width="{W}" height="{H}"><defs>{PREMIUM_DEFS}</defs>{body}</svg>')


def save(svg_text, svg_path, png_widths):
    svg_path.write_text(svg_text)
    if not shutil.which("rsvg-convert"):
        return False
    for width in png_widths:
        suffix = "" if width == W else f"@{width // W}x"
        png = svg_path.with_name(f"{svg_path.stem}{suffix}.png")
        subprocess.run(["rsvg-convert", "-w", str(width), "-o", str(png), str(svg_path)], check=True)
    return True


def main():
    ap = argparse.ArgumentParser(description="Build Christmas category tiles from product images.")
    ap.add_argument("products", nargs="+", help="product PNGs with transparent backgrounds, in row order")
    ap.add_argument("--version", choices=[*VERSIONS, "premium", "all"], default="all")
    ap.add_argument("--tags", default="", help='premium tag text per product, comma-separated, e.g. "BOGO,,,BOGO"')
    ap.add_argument("-o", "--output", default="christmas_domes", help="output folder")
    args = ap.parse_args()

    out = Path(args.output)
    (out / "frames").mkdir(parents=True, exist_ok=True)
    versions = [*VERSIONS, "premium"] if args.version == "all" else [args.version]
    tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
    made_png = True
    for version in versions:
        if version == "premium":
            for i, path in enumerate(args.products):
                label = tags[i] if i < len(tags) and tags[i] else None
                made_png &= save(premium_tile(path, label), out / f"premium_{Path(path).stem}.svg", [W, 2 * W])
            made_png &= save(premium_tile(), out / "frames" / "premium_frame.svg", [4 * W])
            continue
        for i, path in enumerate(args.products):
            made_png &= save(tile(version, i, path), out / f"{version}_{Path(path).stem}.svg", [W, 2 * W])
        for i in range(len(VERSIONS[version]["frames"])):
            made_png &= save(tile(version, i), out / "frames" / f"{version}_frame_{i + 1}.svg", [4 * W])
    print(f"Wrote {', '.join(versions)} to {out}/")
    if not made_png:
        print("rsvg-convert was not found, so only SVG files were written (see the notes at the top of this script).")


if __name__ == "__main__":
    main()
