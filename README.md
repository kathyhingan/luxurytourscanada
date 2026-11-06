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
12. DONE 2026-10-29 (open since 2026-10-24): notification-email gate closed on
    Kathy's YES. Production probe through the deployed /exec: {"ok":true},
    probe row landed on `Leads Canada` with exact values (server-side phone
    +1 -> 001 normalization working), 19 headers intact. ok:true proves
    appendRow AND MailApp.sendEmail ran without exception; alert recipient is
    kathyhingan@gmail.com (Code.gs NOTIFY), subject "LTC Lead: <name>". Inbox
    receipt not directly verifiable from Hermes (all Gmail tokens read
    journey@; the alert never routes through journey@, zero hits there), so
    the probe email was left in her inbox as the receipt artifact for a
    one-glance confirm. Probe row deleted safely afterwards (locate by value,
    re-read assert, deleteRange shiftDimension ROWS, full re-read: 19 headers,
    0 rows, no leftovers; LTP Leads 45 rows, zero contamination).
13. 2026-10-29 (two changes staged, ride the next push):
    (a) Salt Spring rebuilt on the LTP destination architecture (same sections
    as Tofino), 1,346 words, FAQ and attraction schema kept, no personal-band
    placeholder; sitemap lastmod bumped to 2026-10-29 for the push.
    (b) CAPTURE BUG FIXED (found 2026-10-29, live since 2026-10-24): page()
    shipped the literal {FORM_ACTION} placeholder in the footer form of every
    generated interior page, so the quote form on all 18 interior pages
    silently never reached Apps Script; only the hand-maintained homepage
    carried the real /exec URL. sitegen.py now substitutes the token before
    write (commit 44e82da); all 20 pages verified carrying the real action,
    zero placeholders. The homepage capture E2E proof from Oct 24/29 stands
    unaffected; interior-page capture is fixed as of this push and is
    re-provable with the capture-e2e recipe if needed.
14. DONE 2026-10-30: Jasper rebuilt on the LTP destination architecture (facts
    strip, intro split, 6-card highlights carousel, traveller strip with
    cross-links, 6 planning cards, design band, cross-link, CTA band), 1,508
    words, FAQ and attraction schema kept, no personal-band placeholder. All
    11 Jasper photos already on disk were reused; no new harvest needed.
    PUSHED AND LIVE 2026-10-30 under the standing push-all order: commit
    f7933c8 on origin/main, Pages build verified "built" in 40s, live-verified
    on the custom domain (200, all six sections present, real /exec form
    action, zero placeholders), sitemap lastmod bumped to the live date
    2026-10-30 and confirmed live. Gates: audit exit 0 on all 20 pages, zero
    em/en dashes, zero forbidden words, all image refs resolve, zero overflow
    at 390/1440, carousel drag delta 336 via MouseEvents, FAQ one-open
    verified, Leads Canada re-read 19 headers 0 rows. Remaining rewrites:
    Banff and Yoho, PEC, Niagara-on-the-Lake, the two hubs, the five
    experience pages.
15. DONE 2026-11-01: Banff and Yoho rebuilt on the LTP destination
    architecture (facts strip, intro split, 6-card highlights carousel,
    traveller strip with cross-links, 6 planning cards, design band,
    cross-link, CTA band), 1,590 words, FAQ and attraction schema kept, no
    personal-band placeholder. All 10 Banff photos already on disk were
    reused; 9 slot in, banff-mosaic-2 (lodge fireplace) no longer
    referenced. Keyword ownership unchanged ("icefields parkway private
    tour" in title and H1). PUSHED AND LIVE 2026-11-01 under the standing
    push-all order: commit 4f075db on origin/main, Pages build verified
    "built", live-verified on the custom domain (200, all seven sections,
    real /exec form action, zero placeholders), sitemap lastmod bumped to
    the live date 2026-11-01 and confirmed live. Gates: audit exit 0 on all
    20 pages, zero em/en dashes, zero forbidden words, all image refs
    resolve on disk and live, zero overflow at 390/1440, carousel drag
    delta exactly 336 leftward via MouseEvents, FAQ one-open verified
    (details[open] state), hero CTA above the fold at both widths (572 at
    390, 689 at 1440), body 17px/19px. Leads Canada re-read 19 headers
    0 rows. Remaining rewrites: PEC, the two hubs, the five experience pages.
16. DONE 2026-11-02: Niagara-on-the-Lake rebuilt on the LTP destination
    architecture (facts strip, intro split, 6-card highlights carousel,
    traveller strip with cross-links, 6 planning cards, design band,
    cross-link, CTA band), 1,651 words, FAQ and attraction schema kept, no
    personal-band placeholder. 8 of the 10 NOTL photos already on disk are
    referenced; notl-mosaic-2 (barrels) and notl-mosaic-3 (heritage houses)
    are no longer used. Keyword ownership unchanged ("niagara-on-the-lake
    private tour" in title and H1). Hero sub drive time corrected to the
    honest "an hour and a half from Toronto" to match the FAQ and the new
    facts strip. PUSHED AND LIVE 2026-11-02 under the standing push-all
    order: Pages build verified "built", live-verified on the custom domain
    (200, all seven sections, real /exec form action, zero placeholders),
    sitemap lastmod bumped to the live date 2026-11-02 and confirmed live.
    Gates: audit exit 0 on all 20 pages, zero em/en dashes, zero forbidden
    words, all image refs resolve on disk, zero overflow at 390/1440,
    carousel drag delta exactly 336 leftward via MouseEvents, FAQ one-open
    verified (details[open] state), hero CTA above the fold at both widths
    (556 at 390, 607 at 1440), body 17px/19px, mobile drawer opens and
    recloses. Leads Canada re-read 19 headers 0 rows. Remaining rewrites:
    PEC, the two hubs, the five experience pages.
17. DONE 2026-11-04: Prince Edward County rebuilt on the LTP destination
    architecture (facts strip, intro split, 6-card highlights carousel,
    traveller strip with cross-links, 6 planning cards, design band,
    cross-link, CTA band), 1,639 words, FAQ and attraction schema kept, no
    personal-band placeholder. 9 of the 11 PEC photos already on disk are
    referenced; pec-mosaic-1 (limestone heritage) is no longer used and
    pec-mosaic-2 and pec-mosaic-3 moved into the carousel cards. Keyword
    ownership unchanged ("prince edward county private tour" in title and
    H1). PUSHED AND LIVE 2026-11-04 under the standing push-all order:
    commit 84b8b27 on origin/main, Pages build verified "built", live
    verification on the custom domain (200, all seven sections, six
    carousel cards, real /exec form action, zero placeholders), sitemap
    lastmod bumped to the live date 2026-11-04 and confirmed live. Gates:
    audit exit 0 on all 20 pages, zero em/en dashes, zero forbidden words,
    all image refs resolve on disk and live, zero overflow at 390/1440,
    carousel drag delta exactly 336 leftward via MouseEvents at both
    widths, FAQ one-open verified with settle gaps (details[open] state),
    hero CTA above the fold at both widths (572 at 390, 689 at 1440), body
    1440), body 17px/19px. Conversion-path sweep: all 20 sitemap URLs live 200 with the
    real form action and zero placeholders. Leads Canada re-read 19 headers
    0 rows. Remaining rewrites: the two hubs, the five experience pages.
18. DONE 2026-11-05: the destinations and experiences hubs rebuilt on the LTP
    interior architecture (facts strip, intro split, card grids, traveller
    strip with experience cross-links on the destinations hub, six segment
    planning cards on the experiences hub, design band, cross-link, CTA
    band). 1,483 and 1,083 words, keyword ownership unchanged (private canada
    tours / private guided tours canada in title and H1), FAQ and trip schema
    kept, Point Pelee folded into the destinations hub intro as the on-request
    seventh corner. PUSHED AND LIVE 2026-11-05 under the standing push-all
    order: commit f92b7e6 on origin/main, Pages build verified "built",
    live-verified on the custom domain (200, all sections, real /exec form
    action, zero placeholders), sitemap lastmod bumped to the live date and
    confirmed live. Gates: audit exit 0 on 20 pages, zero em/en dashes, zero
    forbidden words, all image refs resolve on disk and live, zero overflow
    at 390/1440, exp-grid renders grid in a fresh session, FAQ one-open
    verified, hero CTA above the fold at both widths (572 at 390, 689 at
    1440), body 17px/20px, mobile drawer opens and recloses. Remaining
    rewrites: the five experience pages.
19. DONE 2026-11-06: the private tours experience page rebuilt on the LTP
    interior architecture (facts strip, intro split, 6-card highlights
    carousel, 4-card region strip cross-linking the destination pages, six
    planning cards plus the included/not-included lists, design band,
    cross-link, CTA band), 1,452 words, best-for strip added, FAQ and trip
    schema kept, keyword ownership unchanged ("private tours canada" in title
    and H1). PUSHED AND LIVE 2026-11-06 under the standing push-all order:
    sitemap lastmod bumped to the live date and confirmed live. Gates: audit
    exit 0 on 20 pages, zero em/en dashes, zero forbidden words, all image
    refs resolve on disk, zero overflow at 390/1440, hc-carousel and exp-grid
    render in a fresh session, carousel drag delta exactly 336 leftward via
    MouseEvents, FAQ one-open verified with settle gaps (details[open]),
    hero CTA above the fold at both widths (572 at 390, 689 at 1440), body
    17px/19px, mobile drawer toggles aria-expanded. Remaining rewrites: the
    other four experience pages.
20. 2026-11-06, MOFU: the `Leads Canada` tab recorded its first four data rows,
    all automated spam (three @formtests.info submissions 5:42 to 5:43 that
    randomised every text field while keeping the real hidden `source` and
    `page` defaults, plus one gmx.com link-spam message at 6:41). No real
    inquiry. A honeypot guard is specified in
    `docs/form-spam-guard-2026-11-06.md` and NOT applied: it waits on Kathy's
    go plus her paste and redeploy of the standalone `Code.gs`. Deleting the
    four rows is also hers to rule on.

## Brand rules enforced on every page

All CTAs to /#begin. No prices. No hotel recommendation sections. No em or en
dashes. Forbidden words excluded. lang="en-CA". Single H1. Analytics order,
favicon, then SEO head per 07-SKILL-PAGE-DESIGN. No Malaya Publishing or agency
names anywhere in prospect-facing content.
