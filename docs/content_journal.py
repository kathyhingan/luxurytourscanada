"""Journal hub and two seed posts. Blog template: 07-SKILL-PAGE-DESIGN Template 2.
Posts are written from the planning and operations angle, so the byline rule
(road-experience pieces carry the road author's name) is respected while the
road author's name is still to be confirmed.
"""

PUBDATE = "2026-10-21"

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
        <p>A September guide to the Rockies for the golden larches, an honest look at the Ontario lakeshore as a wine journey, and a piece on travelling Canada with a toddler that does not pretend the drives are short.</p>
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
    date_line="Last updated 21 October 2026",
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
    date_line="Last updated 21 October 2026",
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

ALL = [HUB, TOFINO_POST, JASPER_POST]