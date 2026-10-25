# Keyword ownership map and the 2+2 cadence (2026-10-25)

Working map for the publishing cadence in 06-SKILL-SEO-COPYWRITING: "two
destination pages and two journal posts per month", planned ahead of the
seasonal calendar in the same doc. Three parts: the keyword ownership ledger
for the live 18 pages, the slot plan from November 2026, and the Search
Console export workflow that starts once the domain resolves.

Prepared by am-ltc-bot, 2026-10-25. Nothing here is published content; every
new page and post still passes Kathy's approval gate before it goes live.

## Part 1. Keyword ownership, live pages

Primary keywords read from the built HTML on 2026-10-25 (title tag and H1).
Each page owns one primary keyword and no keyword is shared. The audit gate
(audit-multipage.py, re-run 2026-10-25: 18 pages, zero broken links, zero
dashes, titles and metas distinct, one H1 per page) covers the mechanical
placement rules; the keyword strings themselves live here.

| Page | Type | Primary keyword (live in title and H1) |
|---|---|---|
| / | home | luxury tours canada |
| /destinations/ | hub | private canada tours |
| /destinations/banff-yoho-private-tour/ | destination | icefields parkway private tour |
| /destinations/jasper-private-tour/ | destination | jasper private tour |
| /destinations/niagara-on-the-lake-private-tour/ | destination | niagara-on-the-lake private tour |
| /destinations/prince-edward-county-private-tour/ | destination | prince edward county private tour |
| /destinations/salt-spring-island-private-tour/ | destination | salt spring island private tour |
| /destinations/tofino-private-tour/ | destination | tofino private tour |
| /experiences/ | hub | private guided tours canada |
| /experiences/private-tours/ | segment | private tours canada |
| /experiences/corporate-mice/ | segment | canada corporate retreat luxury |
| /experiences/family-tours/ | segment | luxury family tour canada |
| /experiences/honeymoon-proposals/ | segment | canada honeymoon luxury |
| /experiences/retirement-travel/ | segment | retiree travel canada luxury |
| /about/ | about | about luxury tours canada |
| /journal/ | hub | private canada travel guides |
| /journal/jasper-what-the-banff-coaches-miss/ | journal | private luxury tours in jasper |
| /journal/tofino-storm-season-guide/ | journal | tofino storm season |

Close-variant splits, deliberate per the build spec:

- private tours canada (segment page) vs private guided tours canada
  (experiences hub) vs private canada tours (destinations hub).
- icefields parkway private tour (banff-yoho page) leaves "banff luxury tour"
  free for a future standalone Banff page (candidate in Part 2).
- family-tours title uses the singular form (luxury family tour canada), the
  H1 the plural. The title form is the owned string; the plural stays a
  secondary term on that page only.

Secondary keywords for each page come from the region keyword lists in
03-DESTINATIONS (for example British Columbia luxury tour, Clayoquot Sound
private boat, luxury Rockies tour, Canadian Rockies private guided tour,
luxury Ontario wine tour, Kingston Thousand Islands private cruise, Point
Pelee private tour). Any of those promoted to a primary keyword on a new page
must first be checked against this table.

## Part 2. Cadence slots, November 2026 onward

The 06 seasonal calendar:

| Season content | Publish | Why |
|---|---|---|
| Summer (Rockies, BC coast, lakeshore) | December to February | Peak planning window is January to March |
| Autumn (larches, harvest, colour) | June to August | Autumn trips are planned in summer |
| Winter (storm-watching, aurora, icewine, skiing) | August to October | Winter holidays are planned in autumn |

Where the site stands: launch was 2026-10-24, the tail of the winter publish
window. The Tofino storm season guide landed inside it. November begins the
ramp into the December to February summer window, which is the heaviest
planning window of the year, so early indexation of summer content matters
more than perfect month boundaries.

Standing dependencies, unchanged:

- New destination pages gate on Kathy's personal story for the destination
  (packet item; prompts pattern in docs/story-intake-2026-10-22.md). Pages can
  be staged with cluster positioning only, but they do not go live before her
  story lands.
- Journal posts can be drafted by Hermes from the 06 formula (season +
  destination + private tour, 900 to 1,200 words) and go live only on her
  approval of the exact text.
- Rockies content carries the 03 verify item: confirm current Jasper trail,
  road and service status after the 2024 wildfire before any publish.

Month plan:

- November 2026. Destination slots (2): stage Kingston and the Thousand
  Islands (primary keyword candidate: Kingston Thousand Islands private
  cruise) and Point Pelee (primary keyword candidate: Point Pelee private
  tour), both from 03-DESTINATIONS, both inside the live Ontario Lakeshore
  region, no keyword clash with the 18 live pages. Journal slots (2): summer
  window posts off the live pages, candidates: an Icefields Parkway summer
  drive guide (links the banff-yoho page) and a Salt Spring summer markets
  and farms guide (links the salt spring page).
- December 2026. Destination slots (2): Banff luxury tour page (keyword from
  03, distinct from the banff-yoho page) plus whichever November staging has
  its story. Journal slots (2): continue the summer set (BC coast candidate:
  Clayoquot Sound private boat days; Rockies candidate: Lake Louise at
  sunrise).
- January to February 2027 (peak summer planning window). Destination slots:
  publish everything that has cleared story intake; hold un-cleared slots
  empty rather than publishing cluster-only pages. Journal slots (2 per
  month): booking-intent angles (how many days, when to book, drive times).
- March to April 2027. Begin the autumn set for the June to August window:
  larches in the Rockies, harvest in Prince Edward County and Niagara,
  autumn colour timing. Verify each season claim against 03 before drafting.

Slot ledger lives in docs/keyword-export-template.csv (status column:
planned, drafted, approved, live). Update it on every build, not in chat.

## Part 3. Search Console export and tracking

Blocked until the DNS cutover lands (runbook:
docs/dns-cutover-2026-10-24.md). Once luxurytourscanada.com serves the Pages
build and Enforce HTTPS is on:

1. Verify the domain property in Google Search Console (DNS TXT record on
   Namecheap, or the URL-prefix method on the live site).
2. Submit https://luxurytourscanada.com/sitemap.xml.
3. Monthly export on the first run of each month: Performance, Search
   results, 3-month window, page filter, export CSV, paste impressions,
   clicks and average position into docs/keyword-export-template.csv.
4. Review: any page with impressions and no clicks after 8 weeks gets a title
   and meta pass; any keyword drifting onto a second page gets split or
   refocused before it cannibalises.

The CSV ships with the 18 live rows pre-filled (status live, published
2026-10-24) plus the three November candidates as planned rows.
