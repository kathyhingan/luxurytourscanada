# Luxury Tours Canada: static site build

Sister brand to Arkipelago (luxurytoursphilippines.com), built to the same stack:
static HTML pages, forms posting to a Google Apps Script web app that writes a
lead sheet and emails Kathy's personal Gmail. Domain luxurytourscanada.com is
PURCHASED (2026-10-23): every canonical, og:url and schema URL already uses it.
Leads land in the shared Arkipelago tracker sheet, tab `Leads Canada`.

## Status: draft v1 for Kathy review. Not deployed, not pushed.

## Structure

```
index.html                  homepage + quote form at /#begin
destinations/               hub + Tofino, Salt Spring, Jasper, Banff & Yoho, PEC, Niagara-on-the-Lake
experiences/                hub + private tours, honeymoons & proposals, families, retirees, corporate & MICE
journal/                    hub + 2 seed posts (Tofino storm season, Jasper)
about/                      brand story, how we work
assets/site.css, site.js    shared design system and behaviours
images/                     153 labelled SVG stand-ins (real photos replace them)
favicon.svg                 custom stylised leaf (NOT the official 11-point leaf)
docs/                       generator, content modules, form backend, manifest
```

Rebuild after editing content: `python3 docs/build_all.py` then
`python3 docs/make_assets.py`. Pages are generated from docs/content_*.py.

## Verification run (2026-10-21)

- audit-multipage.py: 18 pages, broken links NONE, JSON-LD valid, titles and
  metas unique, one H1 per page, no em or en dashes, FAQ markup/schema paired,
  all pages 550+ words (destination 830 to 990, posts 1000+).
- 685 internal hrefs resolve. 153/153 images load.
- Browser sweep at 390px and 1440px: no horizontal overflow, body 17px mobile /
  19px desktop, line height 1.80, CTA above the fold on every checked page.
- Interactions: FAQ one-open-at-a-time verified, mobile drawer verified, form
  submit stamps page + timestamp and shows the confirmation.

## Open items (Kathy)

1. Push to a GitHub repo + Pages (CNAME file is in the repo), then point DNS:
   apex A records 185.199.108.153/154/155/156 and www CNAME kathyhingan.github.io.
   Full click-by-click runbook with the live DNS state:
   docs/dns-cutover-2026-10-24.md.
2. Add the `Leads Canada` tab (19 headers) to the shared tracker, deploy the
   STANDALONE Apps Script from docs/form-backend.md, then replace
   LTC_APPS_SCRIPT_DEPLOY_TOKEN in index.html (the one form action).
3. Photography: replace the 153 stand-ins per docs/image-manifest.md. WebP +
   JPEG fallback, hero 250 KB max, others 150 KB max.
4. Analytics: create NEW GA4 and Clarity IDs, paste into the head block
   placeholders. Never reuse the Arkipelago IDs.
5. Tagline still marked CONFIRM in the packet: pages use "Private Journeys,
   Coast to Coast" (from 01-BRAND sub-brand line) as the working tagline.
6. Road-experience byline: posts carry Kathy Hingan on the planning angle.
   Add husband-bylined road pieces once his name is confirmed for publication.
7. Coordinates in TouristAttraction schema are standard published values;
   re-verify each before launch (listed in docs/sitegen.py node_attraction calls).
8. Publish dates on the two posts are the build date; reset at publish.

## Brand rules enforced on every page

All CTAs to /#begin. No prices. No hotel recommendation sections. No em or en
dashes. Forbidden words excluded. lang="en-CA". Single H1. Analytics order,
favicon, then SEO head per 07-SKILL-PAGE-DESIGN. No Malaya Publishing or agency
names anywhere in prospect-facing content.
