# Story intake: Kathy's personal story per destination

Created 2026-10-22 by am-ltc-bot. This is packet item 1, the per-destination
storytelling layer, the stated LTP differentiator. Nothing here is client-facing
until Kathy's stories land and are slotted in.

Verified 2026-10-22: zero first-person sentences in all six destination pages.
The about page already carries her voice (27 years in travel, six crossings by
thumb, 700 km by bicycle) and is the reference register.

## How to answer

Reply in plain text, one block per destination, in any order. 80 to 150 words
each is enough. I slot each block into the destination's generator module
(docs/content_destinations.py), rebuild, and verify. Nothing else needed from
you for this item.

## Per destination: page, current angle, prompts

### 1. Banff and Yoho
Page: destinations/banff-yoho-private-tour/
Current angle: Icefields Parkway in the quiet hours, honest seasons, second
options for outdoor days.
Prompts: When were you last on the Icefields Parkway and what hour was it?
What do you do differently there than a coach tour would? One specific moment
(a lake at first light, a switchback, a shutdown for snow) you would retell to
a guest.

### 2. Jasper
Page: destinations/jasper-private-tour/
Current angle: dark skies, empty switchbacks, wildfire-season planning.
Prompts: What is your darkest-sky memory in Jasper? What do you tell guests
about the drive in? A moment where the mountain weather turned and your plan
B saved the day.

### 3. Niagara-on-the-Lake
Page: destinations/niagara-on-the-lake-private-tour/
Current angle: winery visits with the winemaker, not the tasting bar.
Prompts: Which winery door did you first walk through, and who let you in the
back? What does "with the winemaker" actually look like when you set it up?
One bottle or one barrel room you remember.

### 4. Prince Edward County
Page: destinations/prince-edward-county-private-tour/
Current angle: farm tables, Sandbanks dunes, Kingston pairings.
Prompts: Your first farm-table meal in the County: where, who cooked, what was
on it? What do you know about Sandbanks in shoulder season that the summer
crowd does not?

### 5. Salt Spring Island
Page: destinations/salt-spring-island-private-tour/
Current angle: farm stands, the Saturday market, slow island pacing.
Prompts: Which farm stand do you stop at first off the ferry? What have you
bought there that ended up in a guest's picnic? One artist or market vendor
whose story you retell.

### 6. Tofino
Page: destinations/tofino-private-tour/
Current angle: the road ends at the Pacific, storm season, honesty about
drive times.
Prompts: Your first arrival in Tofino: which storm or which flat calm? What do
you tell guests about the last 40 km of road? A moment on Chesterman Beach or
in the rainforest you would put at the top of a trip.

## Slotting mechanic (Hermes side, after the stories land)

Each story becomes a prose block near the top of its destination body in
docs/content_destinations.py, then docs/build_all.py rebuilds and the page is
verified. Journal post 1 (tofino-storm-season-guide) already proves the voice
works on this site.

## Hard rules for every story block

- First person, Kathy's own words, light edit only.
- Zero em dashes anywhere.
- No agency names, no Malaya, no Arkipelago or Philippines tie-ins inside the
  destination pages (the about-page sister-brand line is packet decision 5,
  separate).
- No client names, no property names from current holds.
- No stock-photo language: Kathy sources all images herself, photo slots get
  labeled placeholders naming the exact shot.
