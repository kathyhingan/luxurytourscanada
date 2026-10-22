# Build readiness audit: Luxury Tours Canada site repo

Audited 2026-10-21 by am-ltc-bot against the LTP stack inventory
(~/.hermes/profiles/am-ltc-bot/notes/ltp-stack-inventory.md). Verification only,
nothing built or changed on the site. Packet gate items stay open.

## What exists in this repo (built 2026-10-21 12:36-12:57)

- 18 static pages: home, destinations hub + 6 destination pages (Banff/Yoho,
  Jasper, Niagara-on-the-Lake, Prince Edward County, Salt Spring Island, Tofino),
  experiences hub + 5 (private, family, honeymoon, retirement, corporate-mice),
  journal hub + 2 posts, about.
- Generator architecture: docs/sitegen.py shell + 4 content modules +
  docs/build_all.py. Design system per assets/site.css header comment is derived
  from the approved artboards (Experience, Blog, Destination).
- Home journeyForm: exact LTP 15-field contract (name, email, journey_type,
  phone, dates, group_size, message, quiz_who, quiz_draw, quiz_pace, quiz_dest,
  quiz_luxury, quiz_archetype, source, timestamp, page), source=ltc-homepage.
- Transport: native form POST into a hidden iframe sink, the proven LTP pattern.
  assets/site.js stamps timestamp + page slug on submit, shows formOk.
- Zero em dashes across all html/py/js/css. No Arkipelago or Philippines brand
  content outside one code comment ("never the Arkipelago IDs") and one about-page
  line (see packet decision 5).
- Destination hub links resolve to all 6 destination pages; formOk element present.

## Verified NOT live or missing (build gaps)

1. Domain: luxurytourscanada.com has no DNS, no HTTP response. Site not deployed.
2. Not a git repository: no version control, nothing to push to GitHub Pages.
3. Apps Script web app does not exist: form action is the placeholder
   https://script.google.com/macros/s/LTC_APPS_SCRIPT_DEPLOY_TOKEN/exec (all pages).
4. Lead tracker sheet does not exist (LTP model: Leads 23 cols, partner DB 17 cols,
   4-color scheme; rebuild order and exact specs are in the stack inventory).
5. Capture surfaces: 1 of 5 vs LTP. Only the home form exists. Missing: MICE brief
   form on experiences/corporate-mice, the two interactive map magnets, weekends surface.
6. Missing infra files referenced by the pages: sitemap.xml, robots.txt, CNAME,
   favicon.svg, apple-touch-icon.png, 404.html, images/logo.png, every hero image
   (images/ is empty, all 18 pages reference /images/*.svg files that do not exist).
7. Phone normalization missing: LTP converts a leading + to 00 client-side so Sheets
   stores the value as text instead of dropping it. assets/site.js submit handler lacks it.
8. GA + Microsoft Clarity IDs are TBD placeholders in every head.
9. Journal is static (2 posts); LTP runs a posts.json-driven hub. Fine to stay static.

## Packet items still open (Kathy, per the goal row)

1. Kathy's personal story per destination: zero first-person content in any of the
   6 destination pages or their generator modules. The about page already carries
   her voice (27 years, six crossings by thumb, 700 km by bicycle). The
   per-destination storytelling layer, the stated LTP differentiator, is absent.
2. Confirmation of the personal notification email for lead alerts.
3. Which Google account owns the new sheet + Apps Script (and its token decision).
4. Lead/revenue goal numbers: nowhere in the repo.
5. Brand call: the about page tells prospects the operator designed private luxury
   journeys in the Philippines "through our sister brand". Public tie between the
   two brands is a positioning decision, Kathy's call, kept as written.
6. Hosting confirmation: generator and domain assume GitHub Pages + custom domain;
   not yet confirmed by Kathy.

## Ready-to-execute build order (unchanged, blocked on packet items 1 to 3)

1. Sheet (tabs + colors per inventory) -> 2. Apps Script web app (new deployment,
   new endpoint, replace the placeholder token, rebuild via docs/build_all.py) ->
   3. Missing infra files + images + phone normalization patch -> 4. git init +
   GitHub Pages deploy + CNAME + DNS -> 5. ops script clones (digest, cadence,
   snapshot, crons) -> 6. quality gate (Google Maps 4.2 rule) on the first partner pass.

MOFU and BOFU stay parked: no live capture surface exists until items 1 to 4 land.

## Addendum 2026-10-22 (am-ltc-bot verification pass)

Corrections to the gap list above, verified live today:

- Gap 2 CLOSED: the repo is now a git repository, commit 9fbd04b 2026-10-21
  16:42, working tree clean. The commit carries the infra files below.
- Gap 6 MOSTLY CLOSED: sitemap.xml, robots.txt, favicon.svg and
  apple-touch-icon.png exist, and images/ holds stand-in SVG art for every
  page (the commit message says stand-in art, so real photography remains a
  Kathy item, per the no-stock-photos rule). Still missing: CNAME, 404.html,
  images/logo.png.
- Gap 7 CLOSED 2026-10-22: phone normalization landed. assets/site.js
  converts a leading + to 00 on submit (client side, the LTP pattern, tested:
  +1 604 555 0142 becomes 001 604 555 0142), and docs/form-backend.md now
  normalizes server-side too, before the row is built, so testAppend and any
  direct POST cannot write a formula into the sheet.
- form-backend.md corrections: the endpoint token appears in exactly ONE page
  (index.html, home is the only page with a form today), not 18 as the doc
  said; the doc now says so.
- Packet item 1 preparation: docs/story-intake-2026-10-22.md gives Kathy a
  fill-in format for the six destination stories (page, current angle, three
  prompts each, 80 to 150 words) and the slotting mechanic.
- Re-verified today: python3 docs/build_all.py builds all 17 generated pages
  plus home with zero drift against the commit; zero em dashes repo-wide;
  luxurytourscanada.com still has no DNS (dig returns nothing for A or
  www CNAME); no packet files landed anywhere under Documents since Oct 21.

Build order unchanged, still blocked on packet items 1 to 3.
