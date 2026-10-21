"""Build every page. Run from the repo root:  python3 docs/build_all.py"""

import os, sys, importlib

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import sitegen as sg

MODULES = ["content_destinations", "content_experiences", "content_journal", "content_about"]

built = []
skipped = []

for name in MODULES:
    try:
        mod = importlib.import_module(name)
    except ModuleNotFoundError:
        skipped.append(name)
        continue
    for cfg in mod.ALL:
        h = cfg["hero"]
        hero_html = sg.hero(
            h["eyebrow"], h["h1"], h["sub"], h["img"], h["alt"],
            cta_text=h.get("cta", "Begin Your Journey"),
            cta_href=h.get("cta_href", "/#begin"),
            short=h.get("short", False),
        )
        if cfg.get("best_for"):
            hero_html += "\n  " + sg.bestfor(cfg["best_for"], cfg.get("best_for_label", "Best for"))
        body = cfg["body"]
        if cfg.get("cta_band"):
            body = body + "\n" + sg.cta_band(*cfg["cta_band"])
        nodes = cfg["extra_nodes"](sg) if cfg.get("extra_nodes") else None
        out = sg.page(
            path=cfg["path"], title=cfg["title"], desc=cfg["desc"],
            crumb_trail=cfg["crumb"], hero_html=hero_html, body_html=body,
            faq_pairs=cfg.get("faq"), extra_nodes=nodes,
            og_type=cfg.get("og_type", "website"),
            og_image=cfg.get("og_image", "/images/home-hero.svg"),
            with_breadcrumb_schema=bool(cfg["crumb"]) and len(cfg["crumb"]) > 1,
            date_line=cfg.get("date_line"),
        )
        built.append(out)

for b in built:
    print("built", b)
if skipped:
    print("not yet written:", ", ".join(skipped))
print("total pages:", len(built))