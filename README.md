# Luxury Tours Canada: static site build

Sister brand to Arkipelago (luxurytoursphilippines.com), built to the same stack:
static HTML pages, forms posting to a Google Apps Script web app that writes a
lead sheet and emails Kathy's personal Gmail. Domain luxurytourscanada.com is
PURCHASED (2026-10-23): every canonical, og:url and schema URL already uses it.
Leads land in the shared Arkipelago tracker sheet, tab `Leads Canada`.

## Status: LIVE since 2026-10-24 (published on Kathy's explicit order).

Repo: github.com/kathyhingan/luxurytourscanada (public, free-plan Pages),
GitHub Pages builds from main (last verified "built" at 9b06d56 on
2026-10-27), custom domain attached from the CNAME file. LIVE on the custom
domain since 2026-10-27: DNS cutover done (apex on the four 185.199.x.153
records, www CNAME to kathyhingan.github.io), Let's Encrypt cert issued the
same day (valid to 2027-01-24), Enforce HTTPS ticked. Full live verification
2026-10-27: all 20 sitemap URLs return 200 with self-canonicals, robots.txt
declares the sitemap, capture E2E re-run from the live origin (ok:true, see
item 10), quiz-to-form data path verified. Content tree = origin; doc-only
commits from the cutover verification ride the next push.
Capture is proven end to end (2026-10-24): real submit on the local build
landed exact values on the `Leads Canada` tab, fetch probe ok:true, Gmail
alert path ran, LTP `Leads` tab untouched.

## Structure

```
index.html                  homepage + quote form at /#begin
destinations/               hub + Tofino, Salt Spring, Jasper, Banff & Yoho, PEC, Niagara-on-the-Lake
experiences/                hub + private tours, honeymoons & proposals, families, retirees, corporate & MICE
journal/                    hub + 4 posts (2 live seeds, 2 November drafts staged locally)
about/                      brand story, how we work
assets/site.css, site.js    shared design system and behaviours
images/                     171 labelled SVG stand-ins (real photos replace them)
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

1. DONE 2026-10-27: Namecheap DNS cutover completed by Kathy (four apex A
   records 185.199.108-111.153, www CNAME kathyhingan.github.io), Let's
   Encrypt cert issued the same day, Enforce HTTPS ticked on Pages. Runbook
   kept for the record: docs/dns-cutover-2026-10-24.md. The legacy Google
   sitemap ping endpoint is deprecated (404, sunset June 2023), so indexing
   runs through Search Console: see item 10.
2. DONE 2026-10-24: `Leads Canada` tab live with the 19 headers, standalone
   Apps Script deployed by Kathy, token swapped in index.html and
   docs/sitegen.py (commit 24e0f7d), E2E readback proof on the exact
   submitted values.
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
8. DONE 2026-10-25: post dates reset to the publish date (2026-10-24) in
   content_journal.py and the two journal sitemap lastmod entries bumped.
   Rides the next push; not live until then.
9. STAGED 2026-10-26, needs Kathy's approval of the exact text: the two
   November journal posts are drafted in content_journal.py (Icefields
   Parkway summer drive, primary keyword "icefields parkway summer drive",
   planned 2026-11-07; Salt Spring Island Saturday Market, primary keyword
   "salt spring island saturday market", planned 2026-11-14). Facts verified
   live 2026-10-26: market season April 4 to October 31, 9 to 3 shoulder /
   9 to 4 high season (saltspringmarket.com + 2026 vendor guidelines);
   parkway fully open, fuel stop May to mid-October, Maligne Canyon and
   Cavell Road closed for 2026 (Parks Canada recovery report + 2026 season
   sources). On approval: set both date_line values and the sitemap lastmod
   rows to the real publish date, then the tree rides the next push. Full
   verification passed 2026-10-26: audit 20 pages clean, sweep 390/1440,
   FAQ one-open-at-a-time, keyword ledger updated (drafted).
10. RESOLVED 2026-10-28 (a pending since 2026-10-27): the two DNS-cutover test
    rows are GONE from the `Leads Canada` tab (verified by full-tab readback:
    19 headers, zero data rows; the two Gmail alerts to Kathy's personal inbox
    remain the live alert-path proof). The LTP `Leads` tab contamination
    spot-check also ran clean the same day: zero LTC markers across all 45
    data rows. Item (a) Search Console (verify, submit sitemap.xml, request
    indexing) remains with Kathy.
11. Interior LTP-pattern rewrite STARTED 2026-10-28: Tofino is the first page
    rebuilt on the LTP destination architecture (hero facts strip, intro
    split, 6-card highlights carousel, traveller strip, planning cards,
    cross-link, CTA band). The shared component CSS (quiz, phil-stat,
    hiw-step, exp-grid, hc-carousel) moved into assets/site.css so interior
    pages can use it; the homepage keeps its identical inline copy. Remaining:
    Salt Spring, Jasper, Banff and Yoho, PEC, Niagara-on-the-Lake, the
    destinations and experiences hubs, the five experience pages. Kathy's
    destination stories slot into a personal band per page when they arrive
    (docs/story-intake-2026-10-22.md); none of the rewritten pages carries a
    placeholder. PUSHED AND LIVE 2026-10-29 on Kathy's explicit push order:
    commits f43abc3 + 9c40d04 on origin/main, Pages build verified "built",
    Tofino live-verified on the custom domain (200 + hc-carousel present) and
    the favicon fix is live on every page. Tofino sitemap lastmod bumped to the
    live date 2026-10-29 in the same push.

## Brand rules enforced on every page

All CTAs to /#begin. No prices. No hotel recommendation sections. No em or en
dashes. Forbidden words excluded. lang="en-CA". Single H1. Analytics order,
favicon, then SEO head per 07-SKILL-PAGE-DESIGN. No Malaya Publishing or agency
names anywhere in prospect-facing content.
