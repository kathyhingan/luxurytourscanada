"""Generate stand-in artwork, favicon, touch icon, robots.txt and sitemap.xml.

Stand-ins follow the approved artboards' placeholder language (glacier ground,
dashed slate frame, labelled subject) so the design reads as designed, not as
missing files. The manifest lists the real photograph intended for each slot.

Run from the repo root:  python3 docs/make_assets.py
"""

import glob, re, os, zlib, struct, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

PAGES = sorted(set(glob.glob("**/index.html", recursive=True) + ["index.html"]))

IMG_RE = re.compile(
    r'<img\s+src="(/images/[^"]+\.svg)"\s+width="(\d+)"\s+height="(\d+)"\s+alt="([^"]*)"'
)


def esc(s):
    return s.replace("&", "&").replace("<", "<").replace(">", ">")


def label_lines(alt, w, h):
    """Turn the alt text into up to 4 short label lines."""
    words = alt.split()
    per = max(3, int(w / 110))
    lines, cur = [], []
    for word in words:
        cur.append(word)
        if len(cur) >= per:
            lines.append(" ".join(cur))
            cur = []
    if cur:
        lines.append(" ".join(cur))
    lines = lines[:4]
    return ["PHOTO"] + lines


def make_svg(path, w, h, alt):
    lines = label_lines(alt, w, h)
    font = max(26, min(46, w // 22))
    tspans = []
    total = len(lines)
    for i, line in enumerate(lines):
        size = font if i == 0 else font - 6
        weight = "600" if i == 0 else "400"
        fill = "#4A5568" if i else "#10281F"
        spacing = "0.25em" if i == 0 else "0.04em"
        y = h / 2 + (i - (total - 1) / 2) * (size + 14) + size * 0.35
        tspans.append(
            f'<text x="50%" y="{y:.0f}" text-anchor="middle" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" letter-spacing="{spacing}" '
            f'font-family="Montserrat,Verdana,sans-serif" '
            f'text-transform="uppercase">{esc(line)}</text>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect width="{w}" height="{h}" fill="#DCE6E4"/>
<rect x="10" y="10" width="{w-20}" height="{h-20}" fill="none" stroke="#4A5568" stroke-width="2" stroke-dasharray="10 8"/>
{''.join(tspans)}
</svg>
"""


manifest = ["# Image slot manifest: Luxury Tours Canada",
            "",
            "Every image on the site is a labelled stand-in in the brand palette.",
            "Drop the real photograph over the path named in the last column (convert to",
            "WebP with a JPEG fallback per 07-SKILL-PAGE-DESIGN, hero at 1600px wide and",
            "250 KB or less, everything else 150 KB or less), update the extension in the",
            "page, and delete the stand-in. Never ship these to production.",
            "",
            "| Slot (stand-in) | Size | Intended subject (from alt text) | Real asset name |",
            "| --- | --- | --- | --- |"]

count = 0
for page in PAGES:
    html_src = open(page, encoding="utf-8").read()
    for m in IMG_RE.finditer(html_src):
        src, w, h, alt = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        fs = src.lstrip("/")
        existing = open(fs, encoding="utf-8").read() if os.path.exists(fs) else ""
        want = make_svg(src, w, h, alt)
        if existing != want:
            os.makedirs(os.path.dirname(fs), exist_ok=True)
            open(fs, "w", encoding="utf-8").write(want)
        slug = os.path.splitext(os.path.basename(fs))[0]
        manifest.append(f"| {src} | {w}x{h} | {esc(alt)} | {slug}.webp |")
        count += 1

open("docs/image-manifest.md", "w", encoding="utf-8").write("\n".join(manifest) + "\n")
print(f"stand-ins ensured: {count}, manifest: docs/image-manifest.md")

# ---------------------------------------------------------------- favicon

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs>
<linearGradient id="leaf" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#B3202A"/><stop offset=".55" stop-color="#C4622D"/><stop offset="1" stop-color="#E3B04B"/>
</linearGradient>
</defs>
<rect width="64" height="64" rx="14" fill="#10281F"/>
<path d="M32 8c2.6 4.4 6.8 7.2 12.4 8.4-1.6 3-1.4 5.6.6 7.8-2.8-.2-4.8.8-6 3 2.8 1.2 4.6 3.2 5.4 6-3-.8-5.4-.2-7.2 1.8 1.6 2.6 1.6 5.2 0 7.8-1.8-2-4-2.6-6.6-1.8l1.6 13h-.4l1.6-13c-2.6-.8-4.8-.2-6.6 1.8-1.6-2.6-1.6-5.2 0-7.8-1.8-2-4.2-2.6-7.2-1.8.8-2.8 2.6-4.8 5.4-6-1.2-2.2-3.2-3.2-6-3 2-2.2 2.2-4.8.6-7.8C25.2 15.2 29.4 12.4 32 8z" fill="url(#leaf)"/>
<path d="M32 8v43" stroke="#10281F" stroke-width="1.6"/>
</svg>
"""
open("favicon.svg", "w", encoding="utf-8").write(FAVICON)
print("favicon.svg written (custom stylised leaf, gradient maple to gold)")

# ------------------------------------------------- touch icon (stdlib PNG)

def png(path, w, h, pixel_fn):
    raw = b"".join(b"\x00" + b"".join(struct.pack("BBB", *pixel_fn(x, y)) for x in range(w)) for y in range(h))
    def chunk(tag, data):
        c = struct.pack(">I", len(data)) + tag + data
        return c + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    open(path, "wb").write(
        b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")
    )

def leaf_fn(x, y):
    # Deep Spruce ground with an amber leaf bar as a stand-in mark
    cx, cy = x - 90, y - 90
    inside = abs(cx) < 26 and abs(cy) < 52 and not (abs(cx) < 5 and cy > -30)
    if inside:
        return (0xD9, 0x8A, 0x2B)
    return (0x10, 0x28, 0x1F)

png("apple-touch-icon.png", 180, 180, leaf_fn)
print("apple-touch-icon.png written (stand-in mark; replace with logo export)")

# ---------------------------------------------------------------- robots

open("robots.txt", "w", encoding="utf-8").write(
    "User-agent: *\nAllow: /\n\n"
    "# Retrieval crawlers stay allowed; training crawlers are optional to block.\n"
    "User-agent: OAI-SearchBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\n"
    "User-agent: Claude-SearchBot\nAllow: /\nUser-agent: Bingbot\nAllow: /\nUser-agent: Googlebot\nAllow: /\n\n"
    "Sitemap: https://luxurytourscanada.com/sitemap.xml\n"
)
print("robots.txt written")

# ---------------------------------------------------------------- sitemap

DOMAIN = "https://luxurytourscanada.com"
today = datetime.date.today().isoformat()
urls = []
for page in PAGES:
    if page == "index.html":
        loc = DOMAIN + "/"
        pri = "1.0"
    else:
        loc = DOMAIN + "/" + os.path.dirname(page) + "/"
        pri = "0.8"
    urls.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod><priority>{pri}</priority></url>")
open("sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
)
print(f"sitemap.xml written ({len(urls)} URLs)")