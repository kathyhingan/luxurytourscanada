"""Journal hub and two seed posts. Blog template: 07-SKILL-PAGE-DESIGN Template 2.
Posts are written from the planning and operations angle, so the byline rule
(road-experience pieces carry the road author's name) is respected while the
road author's name is still to be confirmed.
"""

PUBDATE = "2026-10-24"

# ---------------------------------------------------------------- hub

HUB = dict(
    path="journal/",
    title="Journal | Private Canada Travel Guides | Luxury Tours Canada",
    desc="Honest private Canada travel guides: when to go, what the crowds do, and what a private journey actually looks like on the ground, written before you book.",
    crumb=[("Home", "/"), ("Journal", "/journal/")],
    og_image="/images/journal-clusters.svg",
    hero=dict(
        eyebrow="Field notes",
        h1="The Journal: Honest Guides to Travelling Canada Privately",
        short=True,
        sub="Seasons, crowds, drive times, and the trade-offs nobody puts in a brochure. Written by the people who design the journeys.",
        img="/images/journal-hero.svg",
        alt="Journal of private Canada travel guides: a mountain road and a notebook at first light",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <p>Canadian travel is planned ahead of the season, which means most of our guests read before they write to us. These guides exist for that moment: what a region is genuinely like in each month, which hours the famous places stay quiet, and what a private journey changes about the experience.</p>
        <p>We publish two destination pages and two journal posts a month, ahead of each season's planning window. Autumn trips are planned in summer, winter journeys in autumn, and the Rockies in January.</p>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/journal-tofino-card.svg" width="600" height="400" alt="Pacific storm seen from a lodge window on the Tofino coast" loading="lazy"></figure>
          <div class="body"><div class="lab">Guide, BC coast</div><h3 class="card-title">Tofino in Storm Season: A Private Guide to the Quiet Coast</h3><p>Why November to February is the best-kept window on the Pacific, and how to do it properly.</p><a class="more" href="/journal/tofino-storm-season-guide/">Read the guide</a></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/journal-jasper-card.svg" width="600" height="400" alt="Maligne Lake at dawn in Jasper before the day visitors arrive" loading="lazy"></figure>
          <div class="body"><div class="lab">Guide, Canadian Rockies</div><h3 class="card-title">Private Luxury Tours in Jasper: What the Banff Coaches Never Show You</h3><p>Dark skies, empty switchbacks, and why Jasper leads every Rockies journey we design.</p><a class="more" href="/journal/jasper-what-the-banff-coaches-miss/">Read the post</a></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/journal-icefields-card.svg" width="600" height="400" alt="The Icefields Parkway in summer with a glacier ahead" loading="lazy"></figure>
          <div class="body"><div class="lab">Guide, Canadian Rockies</div><h3 class="card-title">Icefields Parkway Summer Drive: A Private Guide</h3><p>The stops that earn the time, the hours that avoid the crowds, and the honest 2026 status.</p><a class="more" href="/journal/icefields-parkway-summer-drive/">Read the guide</a></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/journal-saltspring-card.svg" width="600" height="400" alt="Market stalls under the trees in Centennial Park, Ganges, on Salt Spring Island" loading="lazy"></figure>
          <div class="body"><div class="lab">Guide, Gulf Islands</div><h3 class="card-title">Salt Spring Island Saturday Market: A Summer Guide</h3><p>Season dates, the make, bake, or grow rule, and how to build a Saturday around it.</p><a class="more" href="/journal/salt-spring-saturday-market-guide/">Read the guide</a></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">What we write about</div>
        <h2 class="section-title">The four kinds of guide you will find here</h2>
      </div>
      <div class="prose">
        <ul class="ticks">
          <li><strong>Season guides.</strong> What a region is genuinely like month by month, including the months we avoid and why. Jasper in September for the larches, Tofino in storm season, icewine in Niagara in January.</li>
          <li><strong>Crowd honesty.</strong> Which famous places earn their reputation, at which hours they stay quiet, and which ones we route around entirely.</li>
          <li><strong>Operational reality.</strong> Drive times between bases, where the services are, what wildfire season means for a summer plan, and why every outdoor day carries a fallback.</li>
          <li><strong>Segment reads.</strong> What the same region looks like for a family with a toddler, a retiree couple, and a leadership team, because they are three different trips.</li>
        </ul>
        <p>Every guide ends the same way our journeys begin: with an invitation to a conversation rather than a shopping cart.</p>
        <h2>How to use these guides</h2>
        <p>Read the one that matches your month, not the one that matches your wish list. Canadian travel is planned ahead of the season, so a September journey is chosen in winter, a storm season journey on the Pacific is chosen in autumn, and a wine journey on the lakeshore is chosen before the harvest. If the guide for your month says the region is wrong for your dates, believe it: we would rather move your region than defend your dates.</p>
        <p>When one of these guides sounds like your trip, the next step is a short conversation about the people travelling, the pace, and the season. That conversation is where the journey starts, and everything on this site is written to get you to it well informed.</p>
        <p>Start with the destinations themselves: the <a href="/destinations/tofino-private-tour/">Tofino private tour</a> page, the <a href="/destinations/jasper-private-tour/">Jasper private tour</a> page, or the full <a href="/destinations/">destinations index</a>.</p>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="callout">
        <div class="lab">Coming next</div>
        <p>A Clayoquot Sound guide to private boat days on the BC coast, a Lake Louise sunrise guide, an honest look at the Ontario lakeshore as a wine journey, and a piece on travelling Canada with a toddler that does not pretend the drives are short.</p>
      </div>
    </div>
  </section>
""",
)

# ---------------------------------------------------------------- Tofino storm season

TOFINO_POST = dict(
    path="journal/tofino-storm-season-guide/",
    title="Tofino Storm Season: A Private Guide to the Quiet Coast",
    desc="Tofino storm watching explained: the best months, the lodges that work in winter, the drive in, and what a private guide changes about the trip.",
    crumb=[("Home", "/"), ("Journal", "/journal/"), ("Tofino Storm Season", "/journal/tofino-storm-season-guide/")],
    og_image="/images/journal-tofino-hero.svg",
    og_type="article",
    date_line="Last updated 24 October 2026",
    hero=dict(
        eyebrow="BC coast, storm season",
        h1="Tofino in Storm Season: A Private Guide to the Quiet Coast",
        sub="By Kathy Hingan, Luxury Tours Canada. 21 October 2026. Eight minutes to read.",
        img="/images/journal-tofino-hero.svg",
        alt="Tofino storm watching: the Pacific breaking on the outer coast in winter",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <p>The Pacific arrives in sets. From the window of a Tofino lodge in January, you hear the next one before you see it, a low sound that starts somewhere out past the horizon and finishes against the rocks below the deck. Then the room goes quiet for twenty seconds, and the whole coast holds its breath, and it comes again.</p>
        <p>This is the season almost nobody books, and it is the one we recommend first to couples. July and August in Tofino are beautiful and busy, with the beach car parks full by ten in the morning. November to February is empty, cheaper, and considerably more dramatic. The trade is rain, and if you pack for rain, the trade is worth making.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-tofino-lead.svg" width="1400" height="800" alt="Winter swell breaking on the rocks near Tofino during storm watching season" loading="lazy">
          <figcaption>Chesterman Beach in January, mid-morning, and nobody in the frame.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="prose">
        <h2>Where does a private Tofino tour go in storm season?</h2>
        <p>Storm season changes the shape of a journey rather than cancelling it. The beach walks get shorter and much more deliberate. The private boat days move to the calmer windows, which the guide checks the evening before rather than the morning of, and the lodge becomes the destination rather than the base.</p>
        <p>What stays open: the rainforest trails, the harbour, the hot springs, and the long, slow lunches. What we build instead of a beach day is a morning at Hot Springs Cove, timed so the soak happens after the tour boats have gone, and an afternoon in the old-growth forest on Meares Island, where the cedars block the wind and the walk feels warmer than the forecast promised.</p>
      </div>
      <div class="grid g-2">
        <figure class="shot shot-card"><img src="/images/journal-tofino-pair-1.svg" width="600" height="400" alt="Rainforest trail on Meares Island near Tofino in winter" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/journal-tofino-pair-2.svg" width="600" height="400" alt="Hot Springs Cove soak in winter on the Tofino coast" loading="lazy"></figure>
      </div>
    </div>
  </section>

  <section class="cta" aria-label="Pull quote">
    <img src="/images/journal-tofino-quote.svg" width="1600" height="900" alt="Storm light on the Tofino shoreline at dusk" loading="lazy">
    <div class="veil"></div>
    <div class="inner">
      <blockquote>You can hear the set coming before you see it. Then the coast holds its breath, and it arrives.</blockquote>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <h2>When to go, and how to get there</h2>
        <p>Storm season runs November to February, with the biggest swell typically arriving in December and January. Spring brings the grey whale migration from March into April, and late spring and early autumn, May and June, September and October, are the best all-round windows on this coast, with active whales and thin crowds.</p>
        <p>The drive from Nanaimo takes three and a half to four hours, and it is one of the great coastal roads in the country. The alternative is a floatplane, which turns the transfer into the first experience of the trip. Either way, we plan the arrival so that the first night is not spent in a car.</p>
        <p class="small">One operational note worth having: boat and floatplane days are weather dependent in every season, so every itinerary we build on this coast carries a fallback day written in advance. That is not pessimism, it is how the coast works.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/journal-tofino-landscape.svg" width="1400" height="800" alt="Coastal road on the drive into Tofino in winter, rainforest on both sides" loading="lazy">
        <figcaption>The road into Tofino, three and a half hours from Nanaimo, and worth every minute.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For couples</div>
        <p>Book the room with the window and the tub, keep the schedule to one thing a day, and let the weather set the order. Storm season in Tofino is the most romantic month of the year on this coast, and the easiest time to be genuinely alone in it.</p>
      </div>
      <div class="callout">
        <div class="lab">For families</div>
        <p>Winter is fine for children who enjoy weather, with wetsuits and a guide on every beach day, and the reading age for the drama is probably six and up. The forest walks and the hot springs work in every season, and the distances are short.</p>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <h2>What a private guide changes about this season</h2>
        <p>Timing is everything here, and timing is exactly what a private guide buys you. The soak at Hot Springs Cove after the day boats leave. The beach hour when the rain pauses and the light comes through underneath the cloud. The boat window on the Thursday instead of the Wednesday, because that is when the swell drops.</p>
        <p>None of it is complicated, and none of it is available to a group on a fixed schedule. That is the whole difference between seeing this coast and being on it.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-tofino-closing.svg" width="1400" height="800" alt="Tofino harbour at dusk with fishing boats and lodge lights" loading="lazy">
          <figcaption>Harbour lights, the end of a storm-day, and dinner five minutes away.</figcaption>
        </figure>
        <p>Plan your own coastal journey with us, or read more about a <a href="/destinations/tofino-private-tour/">Tofino private tour</a> and the <a href="/destinations/salt-spring-island-private-tour/">Gulf Islands</a> that pair with it so well.</p>
      </div>
    </div>
  </section>
""",
    cta_band=("/images/journal-tofino-cta.svg", "Tofino storm season: the Pacific seen from a lodge window at dusk",
              "Begin Your Journey", "Tell us the month, and we will tell you honestly what the coast will do.", "Begin Your Journey"),
    faq=[
        ("What is the best month for Tofino storm watching?",
         "<p>December and January usually bring the biggest swell, with the season running November to February. If you want storm drama and reasonable odds of a dry walk in the same week, late November and early February are the sweet spot.</p>"),
        ("Can you still go whale watching in storm season?",
         "<p>Yes, in the calmer windows, and the guide picks the day rather than the calendar. Humpbacks feed offshore through autumn and into winter, and grey whales pass through from March to April.</p>"),
        ("Is Tofino too rainy in winter for a luxury trip?",
         "<p>It rains, and the lodges are built for it: fireplaces, deep baths, and windows facing the water. If your idea of a good day includes a storm, a book, and a soak, winter here beats summer comfortably. If it does not, come in May, June, September, or October instead.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_article(
        "Tofino in Storm Season: A Private Guide to the Quiet Coast",
        "Tofino storm watching explained: the best months, how to reach the coast, and what a private guide changes about a storm season journey.",
        "journal/tofino-storm-season-guide/", "/images/journal-tofino-hero.svg", PUBDATE, "Kathy Hingan")],
)

# ---------------------------------------------------------------- Jasper

JASPER_POST = dict(
    path="journal/jasper-what-the-banff-coaches-miss/",
    title="Private Luxury Tours in Jasper: What the Coaches Miss",
    desc="Luxury Jasper tours built around dark skies, quiet lakes, and the Icefields Parkway, plus an honest read on why Banff comes last on a Rockies journey.",
    crumb=[("Home", "/"), ("Journal", "/journal/"), ("Jasper and Banff", "/journal/jasper-what-the-banff-coaches-miss/")],
    og_image="/images/journal-jasper-hero.svg",
    og_type="article",
    date_line="Last updated 24 October 2026",
    hero=dict(
        eyebrow="Canadian Rockies",
        h1="Private Luxury Tours in Jasper: What the Banff Coaches Never Show You",
        sub="By Kathy Hingan, Luxury Tours Canada. 21 October 2026. Nine minutes to read.",
        img="/images/journal-jasper-hero.svg",
        alt="Luxury Jasper tour: Maligne Lake and the Canadian Rockies under a dark sky",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <p>At eleven at night in Jasper, standing on the shore of a lake an hour from the nearest streetlight, you can see the Milky Way as a structure rather than a smear. There is a bench, a guide, and a flask of something hot. No queue, no tripod forest, no coach idling behind you with its headlights on. Jasper holds one of the largest dark-sky preserves on earth, and almost nobody plans a holiday around it.</p>
        <p>That is the shape of the whole region. Banff and Lake Louise are the most photographed places in Canada, and in July they feel like it. Jasper, three hours north on the same parkway, is larger, quieter, and considerably darker, and it is where we open almost every Rockies journey we design.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-jasper-lead.svg" width="1400" height="800" alt="Maligne Lake at the quiet hour on a private luxury Jasper tour" loading="lazy">
          <figcaption>Maligne Lake, an hour before the day visitors arrive.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="prose">
        <h2>Why Jasper outperforms Banff for private travel</h2>
        <p>Three reasons, and none of them are about scenery. First, space: Jasper National Park is the largest in the Rockies, and the crowds concentrate in two or three places that are easy to avoid once you know the hours. Second, darkness: the dark-sky preserve is a genuinely rare asset, and a guided evening there is unlike anything available further south. Third, timing: because most visitors stay in Banff, the northern lakes and the northern stretches of the parkway stay quiet, even in August.</p>
        <p>Banff and Lake Louise still belong in a Rockies journey. They just belong at sunrise, in shoulder season, or on a route that bypasses the queues, and we tend to close with them rather than open there.</p>
      </div>
      <div class="grid g-2">
        <figure class="shot shot-card"><img src="/images/journal-jasper-pair-1.svg" width="600" height="400" alt="Dark sky evening with a guide in the Jasper Dark Sky Preserve" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/journal-jasper-pair-2.svg" width="600" height="400" alt="Canoe on a still lake in Jasper National Park at dawn" loading="lazy"></figure>
      </div>
    </div>
  </section>

  <section class="cta" aria-label="Pull quote">
    <img src="/images/journal-jasper-quote.svg" width="1600" height="900" alt="Night sky over a Rockies lake in Jasper" loading="lazy">
    <div class="veil"></div>
    <div class="inner">
      <blockquote>The sky here is a structure, not a smear. You need one bench and no streetlights.</blockquote>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <h2>When to go, and how to drive it</h2>
        <p>Late June to mid September is the classic window, with the lakes thawed, the roads open, and daylight running late into the evening. Mid September to early October is our own preference: the larches turn gold, the elk are in the valley, and the crowds thin out. Winter, December to March, brings aurora, frozen lakes, and temperatures between minus fifteen and minus twenty five, which is its own kind of trip and not for everyone.</p>
        <p>The practical rules matter more than the calendar. The Icefields Parkway runs 232 kilometres between Lake Louise and Jasper with very few services, so you fill the tank before you start, carry water, and treat the drive as the day rather than the transfer. Lake Louise sits at about 1,600 metres, so the first day at altitude is designed short and gentle. And April to May in the Rockies is snowmelt, mud, and closures, which is why we rarely build there.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-jasper-landscape.svg" width="1400" height="800" alt="The Icefields Parkway in autumn with golden larches and a glacier ahead" loading="lazy">
          <figcaption>The Icefields Parkway in late September, with the larches turning.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For independent travellers</div>
        <p>Jasper rewards the traveller who wants access and quiet rather than a checklist. The dark-sky evening, the canoe on still water, and the walk toward the Athabasca Glacier are the three things we build every northern journey around.</p>
      </div>
      <div class="callout">
        <div class="lab">For retirees and families</div>
        <p>No departure before half past eight, the parkway driven by private vehicle with short walks and long views, and wildlife viewed at distance with a briefing before every walk. Children over eight get the most from this region.</p>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <h2>What a private guide changes in Jasper</h2>
        <p>Two things, mostly: timing and honesty about the park. Timing gets you the lake before the boats, the wildlife pull-off at the right hour, and the dark-sky evening when the moon is out of the way. Honesty matters because some trails and services in the park were affected by the 2024 wildfire season, and the status of roads, walks, and facilities changes as recovery continues. We check the current position with Parks Canada before we quote anything, and we tell you plainly what is open rather than working from last year's notes.</p>
        <p>That combination is what makes a Jasper journey feel private even in high summer, and it is why the region leads our Rockies work rather than following it.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-jasper-closing.svg" width="1400" height="800" alt="Lodge window in Jasper at dusk with mountains behind" loading="lazy">
          <figcaption>The end of a Jasper day, with the peaks still lit.</figcaption>
        </figure>
        <p>Read more about a <a href="/destinations/jasper-private-tour/">Jasper private tour</a>, the <a href="/destinations/banff-yoho-private-tour/">Icefields Parkway and Yoho</a> that complete the region, or the <a href="/experiences/private-tours/">private journeys</a> we build for independent travellers.</p>
      </div>
    </div>
  </section>
""",
    cta_band=("/images/journal-jasper-cta.svg", "Evening light on the Canadian Rockies near Jasper",
              "Begin Your Journey", "Tell us the season, and we will build the Rockies around it.", "Begin Your Journey"),
    faq=[
        ("Is Jasper or Banff better for a private tour?",
         "<p>Jasper, for a private journey: bigger park, quieter roads, darker skies, and easier access to the viewpoints at the hours that matter. Banff and Lake Louise are best as the closing chapter of a Rockies trip, at sunrise or in shoulder season.</p>"),
        ("How long do you need in Jasper?",
         "<p>Three nights as a minimum, four to five to do it properly, with one of those evenings held for the dark sky and one full day for the parkway in each direction. Anything shorter turns a mountain park into a transfer.</p>"),
        ("Is Jasper still affected by the 2024 wildfire?",
         "<p>Parts of the park, including some trails and services, were affected, and recovery is ongoing. We confirm the current status of every road, walk, and facility with Parks Canada before quoting a journey, and we say clearly what is open at the time you travel.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_article(
        "Private Luxury Tours in Jasper: What the Banff Coaches Never Show You",
        "Luxury Jasper tours built around dark skies, quiet lakes, and the Icefields Parkway, with an honest read on why Banff belongs last on a private Rockies journey.",
        "journal/jasper-what-the-banff-coaches-miss/", "/images/journal-jasper-hero.svg", PUBDATE, "Kathy Hingan")],
)

# ---------------------------------------------------------------- Icefields Parkway summer (Nov 2026 draft, gated on Kathy approval)

ICEFIELDS_PUBDATE = "2026-11-07"  # planned publish; bump to the real date on approval

ICEFIELDS_POST = dict(
    path="journal/icefields-parkway-summer-drive/",
    title="Icefields Parkway Summer Drive: A Private Guide",
    desc="The Icefields Parkway summer drive, honestly: the stops that earn the time, the hours that avoid the crowds, and what is open after the 2024 wildfire.",
    crumb=[("Home", "/"), ("Journal", "/journal/"), ("Icefields Parkway Summer Drive", "/journal/icefields-parkway-summer-drive/")],
    og_image="/images/journal-icefields-hero.svg",
    og_type="article",
    date_line="Publishing November 2026",
    hero=dict(
        eyebrow="Canadian Rockies, summer",
        h1="The Icefields Parkway Summer Drive: A Private Guide",
        sub="By Kathy Hingan, Luxury Tours Canada. Publishing November 2026. Nine minutes to read.",
        img="/images/journal-icefields-hero.svg",
        alt="The Icefields Parkway in summer with a glacier above the valley",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <p>The parkway does something to time. You leave Lake Louise after breakfast, and twenty minutes later the Trans-Canada is behind you, the road narrows to two lanes of curves, and the day has already changed shape: glaciated peaks on both sides, the Bow River running turquoise beside you, and 232 kilometres of it ahead.</p>
        <p>Summer is when the parkway is at its fullest, and also when it is at its best. Mid-June to early September is peak season on this road, which means long daylight, wildflowers on the meadows, and pull-offs that fill by mid-morning. The drive rewards one thing above everything else, and that is an early start. Everything in this guide is written from that premise.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-icefields-lead.svg" width="1400" height="800" alt="Morning light on Bow Lake on the Icefields Parkway in July" loading="lazy">
          <figcaption>Bow Lake at eight in the morning, before the pull-off fills.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="prose">
        <h2>Where does a private Icefields Parkway summer drive stop?</h2>
        <p>The classic stops earn their time: Athabasca Falls, Sunwapta Falls, the Goats and Glaciers viewpoint, the Columbia Icefield, Bow Lake, Crowfoot Glacier, and the short climb to the Peyto Lake viewpoint. What a private day changes is the order and the hour. We run the road in the direction that keeps the low sun behind you, reach the waterfalls and the viewpoint before the tour coaches, and hold the Icefield for late morning, when the first wave has cleared.</p>
        <p>The road itself carries almost nothing: one fuel stop at Saskatchewan River Crossing, open with the season from early May to mid-October, and not much else between Lake Louise and Jasper. You start with a full tank, carry water, and treat the wildlife rules as absolute: bears on the roadside are watched from the car, at distance, with the engine running.</p>
      </div>
      <div class="grid g-2">
        <figure class="shot shot-card"><img src="/images/journal-icefields-pair-1.svg" width="600" height="400" alt="Athabasca Falls in early summer on the Icefields Parkway" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/journal-icefields-pair-2.svg" width="600" height="400" alt="Peyto Lake from the Bow Summit viewpoint in July" loading="lazy"></figure>
      </div>
    </div>
  </section>

  <section class="cta" aria-label="Pull quote">
    <img src="/images/journal-icefields-quote.svg" width="1600" height="900" alt="The Columbia Icefield seen from the parkway on a clear summer morning" loading="lazy">
    <div class="veil"></div>
    <div class="inner">
      <blockquote>The parkway is not a transfer between two places. Run well, it is the reason the journey exists.</blockquote>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <h2>When to go, and what the summer actually looks like</h2>
        <p>The full summer window runs from late June to early September, with July and August the most reliable months: every viewpoint open, every service running, and daylight that runs past ten in the evening around the solstice. June is quieter but holds snow at the high viewpoints into the month. September brings thinner crowds and cooler mornings, and it is the month we would choose for the drive itself.</p>
        <p>Two practical notes. Services on the road run with the season, so a June plan and a September plan need the fuel and food stops confirmed in advance. And the altitude is real: Lake Louise sits at about 1,600 metres, so the first day at height is designed short and gentle, exactly as on every Rockies journey we build.</p>
        <p class="small">One operational note worth having: road status on the parkway changes with weather in every season. We check Alberta 511 the morning of the drive, and every itinerary carries a fallback day written in advance.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/journal-icefields-landscape.svg" width="1400" height="800" alt="Summer evening light on the Sunwapta River along Highway 93" loading="lazy">
        <figcaption>Evening on the Sunwapta River, with the long light of a summer night.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For independent travellers</div>
        <p>The parkway rewards the traveller who wants the road itself: an early start, four or five real stops, and no schedule to defend. The ice rides and the skywalk at the Columbia Icefield run on a season of their own, typically May to mid-October, and they are worth the hours.</p>
      </div>
      <div class="callout">
        <div class="lab">For retirees and families</div>
        <p>No departure before half past eight, the road driven in short legs between the stops that have washrooms and level paths, and wildlife viewed from the car. Children over eight get the most from a full parkway day; younger children do better with the drive split across two days.</p>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <h2>What a private guide changes about the summer drive</h2>
        <p>Timing, direction, and honesty about what is open. Timing gets you Peyto Lake before the mid-morning wave and the Falls while the light is still on the lip. Direction keeps the sun behind you at the viewpoints that face south. And honesty matters this year more than most: the parkway and its landmarks sit outside the area burned in the 2024 Jasper wildfire, and the road is fully open, but recovery around Jasper is still a live picture, so every journey we quote is built on the current Parks Canada status rather than last year's notes.</p>
        <p>That is the difference between driving the road and being shown it.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-icefields-closing.svg" width="1400" height="800" alt="The road south from Jasper with early light on the peaks" loading="lazy">
          <figcaption>The end of a parkway day, with the peaks still lit.</figcaption>
        </figure>
        <p>Read more about the <a href="/destinations/banff-yoho-private-tour/">Icefields Parkway and Yoho</a> private journey, a <a href="/destinations/jasper-private-tour/">Jasper private tour</a>, or our field notes on <a href="/journal/jasper-what-the-banff-coaches-miss/">what the Banff coaches never show you</a>.</p>
      </div>
    </div>
  </section>
""",
    cta_band=("/images/journal-icefields-cta.svg", "Summer on the Icefields Parkway, glacier and valley in one frame",
              "Begin Your Journey", "Tell us when you are going, and we will tell you what the road will be like.", "Begin Your Journey"),
    faq=[
        ("Is the Icefields Parkway fully open in 2026?",
         "<p>Yes. The road is open year round, and the parkway and its landmarks sit outside the 2024 Jasper wildfire burn area. What is seasonal is everything on it: the fuel stop and food services run from early May to mid-October, and winter travel carries tire or chain rules from November to March. In storm weather we confirm the road with Alberta 511 before setting out.</p>"),
        ("How long should a summer day on the parkway take?",
         "<p>The full drive needs a day in each direction, done properly. We build it as two days with a night in Jasper, reach the waterfalls and viewpoints in the quiet hours, and treat the road itself as the experience rather than the transfer between Lake Louise and Jasper.</p>"),
        ("What is still closed after the 2024 wildfire?",
         "<p>The parkway itself is fully open, and so are the landmarks along it. Around Jasper, Maligne Canyon and the Cavell Road with its two trails are closed for the 2026 season, while trails such as the Valley of the Five Lakes have reopened. Status changes as recovery continues, so every journey is quoted on the current Parks Canada position, stated plainly before you travel.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_article(
        "Icefields Parkway Summer Drive: A Private Guide",
        "An honest private guide to the Icefields Parkway summer drive: the stops that earn the time, the hours that avoid the crowds, and the current status after the 2024 Jasper wildfire.",
        "journal/icefields-parkway-summer-drive/", "/images/journal-icefields-hero.svg", ICEFIELDS_PUBDATE, "Kathy Hingan")],
)

# ---------------------------------------------------------------- Salt Spring Saturday Market (Nov 2026 draft, gated on Kathy approval)

SALTSPRING_PUBDATE = "2026-11-14"  # planned publish; bump to the real date on approval

SALTSPRING_POST = dict(
    path="journal/salt-spring-saturday-market-guide/",
    title="Salt Spring Island Saturday Market: A Summer Guide",
    desc="The Salt Spring Island Saturday Market explained: season dates and hours, the make, bake, or grow rule, and how a private day builds around it.",
    crumb=[("Home", "/"), ("Journal", "/journal/"), ("Salt Spring Saturday Market", "/journal/salt-spring-saturday-market-guide/")],
    og_image="/images/journal-saltspring-hero.svg",
    og_type="article",
    date_line="Publishing November 2026",
    hero=dict(
        eyebrow="Gulf Islands, summer",
        h1="The Salt Spring Island Saturday Market: A Summer Guide",
        sub="By Kathy Hingan, Luxury Tours Canada. Publishing November 2026. Eight minutes to read.",
        img="/images/journal-saltspring-hero.svg",
        alt="The Salt Spring Island Saturday Market in Centennial Park, Ganges, in July",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <p>The Saturday market is the island's clock. By nine in the morning the park in the middle of Ganges is full: tables of vegetables still wet from the ground, bread in paper bags, cheese, honey, woodwork, paintings that came straight from the studio. Everything on the tables was made, baked, or grown by the person standing behind it, and that rule is the reason the market has run since the 1970s.</p>
        <p>Summer is the market at full strength. The season runs every Saturday from early April to the end of October, and from the last Saturday of June to the Labour Day weekend the stalls stay up an hour longer, until four. This guide is about making a market Saturday the anchor of an island day, because that is what the island itself does.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-saltspring-lead.svg" width="1400" height="800" alt="Market stalls under the trees in Centennial Park on a summer Saturday" loading="lazy">
          <figcaption>Centennial Park in July, stalls up and the morning still cool.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="prose">
        <h2>What makes the Salt Spring Island Saturday Market different?</h2>
        <p>The rule is the difference. Most markets allow resellers; this one does not. The make, bake, or grow standard means the jam, the glaze on the pottery, and the salad greens all come from the same hands you are buying from, and a question about any of it gets answered by the maker. For a visitor it is the fastest hour of local contact the island gives.</p>
        <p>The practical details matter. The market sits in Centennial Park in the village of Ganges, with parking tight on summer Saturdays, so we build the morning to arrive before nine and walk in from the harbour. Dogs stay out of the park by bylaw, which surprises visitors, and a daycare for them runs through the summer months. Bring a bag, and eat breakfast first: the baking goes early.</p>
      </div>
      <div class="grid g-2">
        <figure class="shot shot-card"><img src="/images/journal-saltspring-pair-1.svg" width="600" height="400" alt="A produce stall at the Salt Spring market with island vegetables" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/journal-saltspring-pair-2.svg" width="600" height="400" alt="Ganges harbour seen from the park after a morning at the market" loading="lazy"></figure>
      </div>
    </div>
  </section>

  <section class="cta" aria-label="Pull quote">
    <img src="/images/journal-saltspring-quote.svg" width="1600" height="900" alt="Morning shoppers in Centennial Park with the market at full swing" loading="lazy">
    <div class="veil"></div>
    <div class="inner">
      <blockquote>Everything sold in the park was made, baked, or grown by the hand that sells it.</blockquote>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <h2>When to go, and how a market Saturday fits a journey</h2>
        <p>The season runs from the first Saturday of April to the last of October, nine in the morning to three in the shoulder months and to four in high season. High season runs from the last Saturday of June to the Labour Day weekend. In December the market returns for the first three Saturdays, ten to three, which is a smaller, woodsmoke version of the same thing and worth knowing about if winter is your season on the coast.</p>
        <p>A market morning pairs naturally with the rest of the island: the studios and farms that open through the week, the viewpoint road up Mount Maxwell, a slow afternoon on the southern end at Ruckle Park, and a ferry home that leaves the day unhurried.</p>
        <p class="small">One operational note worth having: summer ferries to Salt Spring run on sailings that fill, so the day is built around the boat times first and the market hours second. That ordering is most of what a private plan buys you here.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/journal-saltspring-landscape.svg" width="1400" height="800" alt="The road south from Ganges with arbutus trees and the sea beyond" loading="lazy">
        <figcaption>The road south from Ganges, arbutus and sea, on an afternoon with no schedule.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For couples</div>
        <p>Arrive on the Friday, take the market slowly on Saturday morning, and give the afternoon to the vineyards and the viewpoint. The island is small, and a day without a schedule suits it.</p>
      </div>
      <div class="callout">
        <div class="lab">For families</div>
        <p>The market is genuinely good with children: room to move, food they will actually eat, and makers who will talk to them. Keep the morning to the park, swim in the afternoon, and let the ferry be the last event of the day rather than the race.</p>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="prose">
        <h2>What a private guide changes about a market day</h2>
        <p>Timing, mostly, and the day built around it. The ferry sailings, the parking, the hour the baking goes, the farms and studios that answer when you arrive: a private day chains these so the market is the anchor and not the queue. We build the day around the boat times, put the market first, and leave the afternoon open enough to follow whatever the makers point you toward.</p>
        <p>That is the difference between visiting the market and having a Salt Spring Saturday.</p>
        <figure class="shot shot-wide">
          <img src="/images/journal-saltspring-closing.svg" width="1400" height="800" alt="Ganges village in the late afternoon after the market crowds thin" loading="lazy">
          <figcaption>Ganges in the late afternoon, the market packed down and the village quiet again.</figcaption>
        </figure>
        <p>Plan your own <a href="/destinations/salt-spring-island-private-tour/">Salt Spring Island private tour</a>, see how the Gulf Islands pair with the outer coast in <a href="/journal/tofino-storm-season-guide/">Tofino in storm season</a>, or browse the full <a href="/destinations/">destinations index</a>.</p>
      </div>
    </div>
  </section>
""",
    cta_band=("/images/journal-saltspring-cta.svg", "A summer Saturday on Salt Spring Island, market morning and a slow afternoon",
              "Begin Your Journey", "Tell us your dates, and we will build the island Saturday around them.", "Begin Your Journey"),
    faq=[
        ("When does the Salt Spring Island Saturday Market run?",
         "<p>Every Saturday from the first Saturday of April to the last of October. Hours are nine to three in the shoulder months and nine to four in high season, from the last Saturday of June to the Labour Day weekend. The market also returns for the first three Saturdays of December, ten to three.</p>"),
        ("Can anything be bought at the market that was not made on the island?",
         "<p>No. The market has run on a make, bake, or grow rule since the 1970s: everything sold is made, baked, or grown by the vendor behind the table. That rule is why the produce, the baking, and the craft are all traceable to a person, and why the market is worth planning a morning around.</p>"),
        ("Is a market day worth building a journey around?",
         "<p>In summer, yes. Pair the morning in Ganges with the farms, studios, and viewpoints that open through the afternoon, and build the day around the ferry sailings rather than the market hours. With the boats timed first, the market becomes the anchor of the island day instead of a stop on it.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_article(
        "Salt Spring Island Saturday Market: A Summer Guide",
        "Season dates and hours for the Salt Spring Island Saturday Market, the make, bake, or grow rule, and how a private day on the island builds around it.",
        "journal/salt-spring-saturday-market-guide/", "/images/journal-saltspring-hero.svg", SALTSPRING_PUBDATE, "Kathy Hingan")],
)

ALL = [HUB, TOFINO_POST, JASPER_POST, ICEFIELDS_POST, SALTSPRING_POST]