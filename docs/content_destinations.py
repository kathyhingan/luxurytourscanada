"""Destination content: the hub plus six destination pages.
One primary keyword per page, no keyword shared between pages.
"""

# ---------------------------------------------------------------- hub

HUB = dict(
    path="destinations/",
    title="Private Canada Tours | Destinations | Luxury Tours Canada",
    desc="Three regions for private Canada tours: the BC coast, the Rockies, and the Ontario lakeshore. Honest seasons, real drive times, eight guests maximum.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/")],
    og_image="/images/dest-hero.jpg",
    best_for=["Retirees", "Couples", "Independent travellers", "Corporate groups"],
    hero=dict(
        eyebrow="Three regions, four seasons",
        h1="Private Canada Tours: Three Regions That Deserve More Than a Week",
        sub="Canada is the second largest country on earth. We do not pretend to cover it in a fortnight. We build journeys in the three regions we know road by road, and we build them slowly.",
        img="/images/dest-hero.jpg",
        alt="Private Canada tours: a quiet highway through the Canadian Rockies at first light",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white" aria-label="Private Canada tour facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Regions</div><p class="small">Three we know personally: the BC coast, the Canadian Rockies, and the Ontario lakeshore, planned road by road</p></div>
        <div><div class="lab">Party size</div><p class="small">Eight guests maximum with one guide and one private vehicle from the first morning to the last</p></div>
        <div><div class="lab">Ideal stay</div><p class="small">Seven to fourteen nights for one region done properly, eighteen to twenty one to cross the country</p></div>
        <div><div class="lab">Planning window</div><p class="small">Summer journeys are planned between January and March, autumn trips in summer, winter journeys through autumn</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Why three regions">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The approach</div>
          <h2 class="section-title">Three regions, <em>known road by road.</em></h2>
          <p>Every private Canada tour we design begins with a region, not a package. Most of our journeys run through one of three areas: the BC coast around Tofino and Salt Spring Island, the Canadian Rockies from Jasper down to Banff and Yoho, and the Ontario lakeshore from Kingston to Essex County.</p>
          <p>Each region has its own season, its own roads, and its own way of rewarding a slower pace. We state drive times honestly, plan around wildfire season rather than hoping, and hold a second option for every outdoor day, because mountain weather turns by the hour.</p>
          <p>There is a seventh corner we add on request: Point Pelee and Essex County at the southernmost edge of mainland Canada, where the bird migration peaks in May and the monarchs pass through in September. Ask, and we will say plainly whether it fits your dates.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/dest-lakeshore.jpg" width="1400" height="800" alt="Lakeside vineyards on the Ontario lakeshore near Prince Edward County on a private Canada tour" loading="lazy">
          <figcaption>Wine harvest runs late September into October.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="The six destinations">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Where we go</div>
        <h2 class="section-title">Six destinations, <em>each built as a journey.</em></h2>
        <p class="lede">None of these is a day trip bolted onto a city stay. Each one anchors a journey of its own, and every page states the season, the drive times, and what we would skip.</p>
      </div>
      <div class="grid g-3">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-tofino.jpg" width="600" height="400" alt="Private boat in Clayoquot Sound near Tofino, British Columbia" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Tofino, British Columbia</h3>
            <p>Outer Clayoquot Sound by private boat, Hot Springs Cove timed away from the tour boats, whale and bear watching with a naturalist, and a storm season almost nobody sees.</p>
            <a class="more" href="/destinations/tofino-private-tour/">Tofino private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-saltspring.jpg" width="600" height="400" alt="Farm stand and vineyard on Salt Spring Island in the Gulf Islands, British Columbia" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Salt Spring Island, British Columbia</h3>
            <p>Thirty five minutes by floatplane from Vancouver. Farm tables, the Saturday market, Mount Maxwell, and warm lake swimming through summer.</p>
            <a class="more" href="/destinations/salt-spring-island-private-tour/">Salt Spring Island private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-jasper.jpg" width="600" height="400" alt="Maligne Lake in Jasper National Park at dawn on a private Jasper tour" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Jasper, Alberta</h3>
            <p>Larger and quieter than Banff, under one of the largest dark sky preserves on earth. Maligne Lake at the quiet hours, the Athabasca Glacier, and wildlife viewed at distance, always guide led.</p>
            <a class="more" href="/destinations/jasper-private-tour/">Jasper private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-banff.jpg" width="600" height="400" alt="Icefields Parkway private tour between Lake Louise and Jasper in the Canadian Rockies" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Banff and Yoho, Alberta and BC</h3>
            <p>Lake Louise at dawn or in shoulder season, Emerald Lake and Takakkaw Falls next door, and 232 kilometres of the Icefields Parkway.</p>
            <a class="more" href="/destinations/banff-yoho-private-tour/">Banff and Yoho private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-pec.jpg" width="600" height="400" alt="Sandbanks dunes and vineyard rows in Prince Edward County, Ontario" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Prince Edward County, Ontario</h3>
            <p>Canada's youngest serious wine region, the Sandbanks dunes, and a private Thousand Islands cruise out of the limestone waterfront at Kingston.</p>
            <a class="more" href="/destinations/prince-edward-county-private-tour/">Prince Edward County private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-notl.jpg" width="600" height="400" alt="Winery visit with the winemaker in Niagara-on-the-Lake, Ontario" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Niagara-on-the-Lake, Ontario</h3>
            <p>Winery visits with the winemaker still pouring, and icewine picked by hand in January on the coldest nights of the year.</p>
            <a class="more" href="/destinations/niagara-on-the-lake-private-tour/">Niagara-on-the-Lake private tour</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Who a private Canada tour suits">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">For every traveller</div>
        <h2 class="section-title">The same roads, <em>built around you.</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">&#128141;</span><div class="exp-title">Couples & Honeymoons</div><p class="exp-body">The BC coast and the lakeshore carry the romance: a soaking tub over the Pacific, farm tables that run late, and the quiet windows of June and September.</p><a href="/experiences/honeymoon-proposals/" class="exp-cta">Plan the quiet days</a></div>
        <div class="exp-card"><span class="exp-icon">&#128188;</span><div class="exp-title">Corporate Groups</div><p class="exp-body">Board level retreats out of Calgary and Banff, and two day escapes within three hours of Toronto on the lakeshore. One point of contact throughout.</p><a href="/experiences/corporate-mice/" class="exp-cta">Corporate retreats</a></div>
        <div class="exp-card"><span class="exp-icon">&#127807;</span><div class="exp-title">Retirees</div><p class="exp-body">No departure before half past eight, short drive days, the same guide throughout, and the walking stated honestly at every stop.</p><a href="/experiences/retirement-travel/" class="exp-cta">Retiree journeys</a></div>
        <div class="exp-card"><span class="exp-icon">&#129517;</span><div class="exp-title">Independent Travellers</div><p class="exp-body">Named places rather than scenery: the operator who runs the boat, the vineyard where the winemaker pours, and the access a coach cannot buy.</p><a href="/experiences/private-tours/" class="exp-cta">Private journeys</a></div>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Planning notes for a private Canada tour">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">When to go, <em>honestly.</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">The BC coast window</h3><p>May and June bring grey whales and quiet roads, September and October the clearest water, and November to February the storm watching season people plan a whole trip around. April is the month we rarely build.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The Rockies window</h3><p>Late June to early October for open roads and long light, with the golden larches in mid September. Parkway fuel and services run May to mid October, and winter builds here are aurora trips, not road trips.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The lakeshore window</h3><p>May to October, with the wine harvest late September into October and the Point Pelee migration in May. January is its own season: the icewine harvest in Niagara, picked at night below minus eight.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">How far ahead</h3><p>Summer Rockies journeys are planned between January and March, and the best tables and cabins book first. Autumn trips are booked in summer. Winter journeys, from storm season to icewine, are planned through autumn.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">How long to stay</h3><p>Seven to fourteen nights for one region done properly. A journey that crosses from the Pacific to the mountains and on to the lakeshore wants eighteen to twenty one nights, and rushing it wastes it.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Weather and wildfire</h3><p>Mountain weather turns by the hour, so every outdoor day carries a second option. Wildfire season is planned around rather than hoped away, and we say plainly when your dates land in the April mud weeks.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we design a private Canada tour">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design</div>
          <h2 class="section-title">Appointments first, <em>then the map.</em></h2>
          <p>A region is only as good as its specific days, so we design from the appointments outward: the boat that leaves the harbour before the fleet, the cellar where the winemaker still pours, the table that is yours for the afternoon. The map fills in around them, at drive times we have done ourselves.</p>
          <p>The whole lakeshore from Kingston to Essex County has been ridden on a bicycle rather than driven past, and the mountain roads are known in both directions, in the cold months as well as the warm ones. That is the standard every journey here is built to.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/dest-banff.jpg" width="1400" height="800" alt="Icefields Parkway at first light on a private Canada tour through the Rockies" loading="lazy">
          <figcaption>The parkway, at the hour the coaches have not reached yet.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="How the journeys are built">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">The other half</div>
      <h2 class="section-title">Destinations are <em>half the design.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Who is travelling decides the pace, the rooms, and the shape of every day. See how a journey changes for a honeymoon, a family, a retreat, or a retiree party, then tell us which shape is yours.</p>
      <a class="btn" href="/experiences/">How journeys are built around you</a>
    </div>
  </section>
""",
    cta_band=("/images/dest-hero.jpg",
              "Private Canada tours: a quiet highway through the Canadian Rockies at first light",
              "Ready to plan your region?",
              "Tell us what you are imagining. We will come back within 24 hours.",
              "Begin Your Journey"),
    faq=[
        ("What is the best time of year for a private Canada tour?",
         "<p>It depends on the region. The Rockies are best from late June to early October. The BC coast is at its finest in May and June and from September into October, with storm season from November to February. The Ontario lakeshore runs May to October, with icewine harvest in January. Tell us your month and we will tell you honestly which region suits it.</p>"),
        ("How long should a private Canada tour be?",
         "<p>Seven to fourteen days for one region done properly, and eighteen to twenty-one days for a shape that crosses from the Pacific to the mountains and on to the lakeshore. Distance is the product here, so a rushed Canada is a wasted one.</p>"),
        ("Do you design journeys across all of Canada?",
         "<p>We build journeys in the three regions we know personally: the BC coast, the Canadian Rockies, and the Ontario lakeshore. If your wish list sits outside those areas, we will say so and point you to someone better placed, rather than designing a journey we cannot stand behind.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_trip(
        "Private Canada Tours",
        "Bespoke private Canada tours across the BC coast, the Canadian Rockies, and the Ontario lakeshore, designed for a maximum of eight guests.",
        "Independent travellers, couples, families, retirees, corporate groups",
        "destinations/")],
)

# ---------------------------------------------------------------- Tofino

TOFINO = dict(
    path="destinations/tofino-private-tour/",
    title="Tofino Private Tour | Luxury BC Coast | Luxury Tours Canada",
    desc="Private Tofino tours built around the outer coast: Clayoquot Sound by private boat, Hot Springs Cove, whales and bears, and storm season. Maximum eight guests.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Tofino", "/destinations/tofino-private-tour/")],
    og_image="/images/tofino-hero.jpg",
    hero=dict(
        eyebrow="British Columbia, Pacific coast",
        h1="Tofino Private Tour: Where the Road Ends at the Pacific",
        sub="Storms you watch from a soaking tub, an old-growth island, and the outer waters of Clayoquot Sound reached by private boat while the beach car park fills up behind you.",
        img="/images/tofino-hero.jpg",
        alt="Tofino private tour: a private boat on the outer waters of Clayoquot Sound at first light",
        cta="Plan My Tofino Journey",
    ),
    best_for=["Couples", "Retirees", "Independent travellers", "Families with children over 6"],
    body="""
  <section class="band-white" aria-label="Tofino journey facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Best season</div><p class="small">May to June and September to October first, storm season November to February, July and August by honest plan only</p></div>
        <div><div class="lab">Getting there</div><p class="small">The Pacific Rim Highway from Nanaimo, or a floatplane straight into the harbour</p></div>
        <div><div class="lab">Ideal stay</div><p class="small">Three to five nights: two boat days, one land day, one weather day</p></div>
        <div><div class="lab">Character</div><p class="small">Wild coast, private boats, and the quietest hours on the sand</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Why Tofino for private travel">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The coast</div>
          <h2 class="section-title">Tofino has been <em>discovered.</em> The water has not.</h2>
          <p>In July and August the main beaches know it. So we do not build summer journeys around Chesterman Beach at midday. We build them around the hours and the waters that stay quiet: dawn, the shoulder seasons, and the outer reaches of Clayoquot Sound, reached by private boat with a naturalist who knows where the whales have been feeding that week.</p>
          <p>Every private Tofino tour we build starts on the water. What this coast does best is found in May and June, from September into October, and through the winter, when the Pacific puts on a show and almost nobody is there to see it. The road in from Nanaimo takes roughly three and a half to four hours, and it is one of the finest drives on the coast. A floatplane is the other way in, so the journey can begin above the water.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/tofino-landscape.jpg" width="1400" height="800" alt="Clayoquot Sound private boat tour passing a forested island on the Tofino coast" loading="lazy">
          <figcaption>Chesterman Beach before eight, when the sand still belongs to the shorebirds.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="What we build into a Tofino journey">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What we build into a <em>Tofino journey</em></h2>
        <p class="lede">Six hours of the coast most visitors never reach, timed to the tide and the light.</p>
      </div>
      <div class="hc-carousel" id="hcCarousel" tabindex="0" aria-label="Tofino experiences, scroll horizontally">
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/tofino-hotsprings.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">01</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Hot Springs Cove</span>
            <h3 class="hc-card-title">The soak after the boats leave</h3>
            <p class="hc-card-desc">A private water taxi out to the springs, timed so the boardwalk and the steam belong to you, and the open Pacific beyond.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/tofino-clayoquot.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">02</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Clayoquot Sound</span>
            <h3 class="hc-card-title">Whales and bears, private boat</h3>
            <p class="hc-card-desc">Grey whales, sea lions, and black bears turning rocks on the low tide line, with a naturalist guide and a vessel that goes where the larger boats cannot.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/tofino-meares.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">03</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Meares Island</span>
            <h3 class="hc-card-title">Old growth, guided</h3>
            <p class="hc-card-desc">A walk among cedars older than most countries, on an island protected by the people who live here. Mud boots provided, pace set by the forest.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/tofino-storm.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">04</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Storm season</span>
            <h3 class="hc-card-title">The Pacific at full volume</h3>
            <p class="hc-card-desc">From November to February the swell arrives in sets you can hear from the lodge. The room with the window, and the soaking tub, booked for exactly this.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/tofino-landscape.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">05</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The outer beaches</span>
            <h3 class="hc-card-title">Dawn, before the town wakes</h3>
            <p class="hc-card-desc">Chesterman and Cox Bay at first light, when the sand still belongs to the shorebirds and the swell is clean.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/tofino-mosaic-1.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">06</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Rainforest coast</span>
            <h3 class="hc-card-title">Where the road runs out</h3>
            <p class="hc-card-desc">Rainforest trails above open ocean at the end of the Pacific Rim Highway, where the map stops and the water starts.</p>
          </div>
        </div>
      </div>
      <p class="small" style="margin-top:12px">Drag the cards to browse the coast.</p>
    </div>
  </section>

  <section class="band-white" aria-label="Who a Tofino journey suits">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">For every traveller</div>
        <h2 class="section-title">The coast, <em>many ways</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">💍</span><div class="exp-title">Couples & Honeymoons</div><p class="exp-body">The room with the window, the tub, and nothing on the schedule until lunch. Winter storm season is the most romantic thing this coast does, and the easiest season to be alone in.</p><a href="/experiences/honeymoon-proposals/" class="exp-cta">Plan the moment</a></div>
        <div class="exp-card"><span class="exp-icon">🌿</span><div class="exp-title">Families</div><p class="exp-body">Pacific water is cold year round: wetsuits for any swimming, a guide on every beach day, and a fallback day already written before you fly. Best with children over six.</p><a href="/experiences/family-tours/" class="exp-cta">Family journeys</a></div>
        <div class="exp-card"><span class="exp-icon">🍁</span><div class="exp-title">Retirees</div><p class="exp-body">Unhurried boat days, a naturalist who sets the pace, and the drive in from Nanaimo broken into stops worth taking.</p><a href="/experiences/retirement-travel/" class="exp-cta">Retiree journeys</a></div>
        <div class="exp-card"><span class="exp-icon">🧭</span><div class="exp-title">Independent Travellers</div><p class="exp-body">You have seen the guidebook Tofino. We take you past it: the outer sound, the quiet hours, and the tide tables that decide everything.</p><a href="/experiences/private-tours/" class="exp-cta">Private journeys</a></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Planning notes for Tofino">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">What to know <em>before you go</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">Getting there</h3><p>The Pacific Rim Highway takes three and a half to four hours from Nanaimo and deserves a full day with stops. The other way in is a floatplane straight into the harbour.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Best season</h3><p>May and June bring grey whales, long evenings, and empty beaches. September and October bring the clearest light of the year and the whale watching most people miss.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The crowd problem</h3><p>July and August are the busy weeks on this coast, workable only with dawn starts and a boat in the outer waters. We plan them honestly or steer you to another window.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">How long</h3><p>Three to five nights. Two boat days, one land day, and one weather day, because boat and floatplane days here are weather dependent.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Storm season</h3><p>November to February: big swell, lodges built around the view, and the quietest the coast ever gets. Dress for rain and you will love it.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Getting around</h3><p>A private vehicle stays with you for the land days, and the boat days start from the harbour. Nothing depends on a shuttle timetable.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we design this journey">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Timed to the water, not the brochure</h2>
          <p>We build the boat days first, because the water decides everything else, and then shape the land days around the weather window. Your guide checks the marine forecast the evening before, and the fallback day is already written before you fly.</p>
          <p>Everything in the plan has been done here first: the soak at Hot Springs Cove after the boats leave, the walk on Meares Island at the hour the light comes through the canopy, the table at the end of the day where the fishing boats are still coming in.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/tofino-guide.jpg" width="1400" height="800" alt="Private guide scanning the water for whales on a Tofino boat day" loading="lazy">
          <figcaption>Wildlife is viewed at distance, guide-led, always.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Longer journeys">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">One coast, one journey</div>
      <h2 class="section-title">Tofino is rarely <em>the only stop.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Most of our guests pair this coast with the Rockies or the Gulf Islands. See how a private Canada journey is built, then tell us what your version looks like.</p>
      <a class="btn" href="/experiences/private-tours/">How private journeys work</a>
    </div>
  </section>
""",
    cta_band=("/images/tofino-storm.jpg",
              "Tofino private tour: winter swell arriving on the Pacific Rim coast",
              "Ready to see Tofino the right way?",
              "Tell us what you are imagining. We will come back within 24 hours.",
              "Begin Your Journey"),
    faq=[
        ("When is the best time for a private Tofino tour?",
         "<p>May and June, then September and October, then the storm season from November to February. July and August are the busiest weeks on this coast, and we work them only with dawn starts and a boat in the outer waters.</p>"),
        ("Can you see whales and bears on a private Tofino boat day?",
         "<p>Yes, with a naturalist guide and a private vessel, and always at a respectful distance. Grey whales pass through in spring, humpbacks feed offshore through the summer and autumn, and black bears work the low tide line in the sound. We time the boat day to the tide, not to a fixed departure.</p>"),
        ("Is Tofino worth visiting in winter?",
         "<p>For storm watching, yes, and it is the quietest the coast ever gets. Expect rain, big swell, and lodges built around the view. We book the room with the window and keep the walking short and the fire close.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_attraction(
        "Tofino, British Columbia, Canada",
        "Private luxury tours of Tofino and Clayoquot Sound on the west coast of Vancouver Island, including private boat days, Hot Springs Cove, and storm season.",
        "destinations/tofino-private-tour/", 49.1530, -125.7671, "/images/tofino-hero.jpg",
        ["Couples", "Retirees", "Independent travellers", "Families"])],
)

# ---------------------------------------------------------------- Salt Spring

SALTSPRING = dict(
    path="destinations/salt-spring-island-private-tour/",
    title="Salt Spring Island Private Tour | Luxury Tours Canada",
    desc="A Salt Spring Island private tour at an unhurried pace: farm tables, the Ganges market, Mount Maxwell, and floatplane transfers from Vancouver.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Salt Spring Island", "/destinations/salt-spring-island-private-tour/")],
    og_image="/images/saltspring-hero.jpg",
    hero=dict(
        eyebrow="British Columbia, Gulf Islands",
        h1="Salt Spring Island Private Tour: The Island That Still Runs on Farm Stands",
        sub="The largest of the Gulf Islands, thirty five minutes by floatplane from Vancouver, and a life measured in market mornings, orchard walks, and the view from Mount Maxwell.",
        img="/images/saltspring-hero.jpg",
        alt="Salt Spring Island private tour: a farm stand and orchard on the Gulf Islands waterfront",
        cta="Plan My Salt Spring Journey",
    ),
    best_for=["Retirees", "Couples", "Independent travellers"],
    body="""
  <section class="band-white" aria-label="Salt Spring journey facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Best season</div><p class="small">May to October for the market season, September and October for harvest and the empty roads</p></div>
        <div><div class="lab">Getting there</div><p class="small">Thirty five minutes by floatplane from Vancouver, or the ferry with the vehicle on deck</p></div>
        <div><div class="lab">Ideal stay</div><p class="small">Two to four nights, anchored on a Saturday market morning</p></div>
        <div><div class="lab">Character</div><p class="small">Farm stands, orchards, and the shortest drives in the Gulf Islands</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Why Salt Spring for private travel">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The island</div>
          <h2 class="section-title">The largest Gulf Island runs on <em>farm time.</em></h2>
          <p>Cheese, cider, lamb, lavender, and a Saturday market that has run on the Ganges waterfront for decades. The whole island is small enough to see properly in three days, and every drive runs minutes, not hours. It is the counterweight to everything busy about the west coast, and the leg of a journey where people finally stop checking the time.</p>
          <p>You arrive by floatplane from Vancouver or by ferry with the vehicle on deck, and the island does the rest. Our retirees call this the leg where they exhale. Our couples book it for the same reason, and autumn, when the stalls fill with harvest and the roads empty out, is the best of it.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/saltspring-landscape.jpg" width="1400" height="800" alt="Salt Spring Island farm and vineyard view over the southern Gulf Islands" loading="lazy">
          <figcaption>Mount Maxwell, late afternoon, looking south over the Gulf Islands.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="What we build into a Salt Spring journey">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What we build into a <em>Salt Spring journey</em></h2>
        <p class="lede">Three days, done slowly, timed to the market and the light.</p>
      </div>
      <div class="hc-carousel" id="hcCarousel" tabindex="0" aria-label="Salt Spring Island experiences, scroll horizontally">
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/saltspring-ganges.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">01</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Ganges village</span>
            <h3 class="hc-card-title">The Saturday market, early</h3>
            <p class="hc-card-desc">In with the guide before the crowd peaks: cheese, sourdough, and the jam stall that has been in the same hands for twenty years.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/saltspring-maxwell.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">02</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Mount Maxwell</span>
            <h3 class="hc-card-title">The lookout with the chairs</h3>
            <p class="hc-card-desc">A short walk on firm ground to the view across the southern Gulf Islands and out to the Pacific. The guide carries the folding chairs.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/saltspring-farm.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">03</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Farm tables</span>
            <h3 class="hc-card-title">Lunch where it was grown</h3>
            <p class="hc-card-desc">A table in sight of the fields, then a dairy or cidery on the way back. Producers who sell to the island first and visitors second.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/saltspring-cusheon.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">04</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Cusheon Lake</span>
            <h3 class="hc-card-title">The warm water swim</h3>
            <p class="hc-card-desc">The ocean here stays cold year round; this lake does not. A dock, a picnic, and an afternoon with nothing on it.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/saltspring-mosaic-1.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">05</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Orchards and cider</span>
            <h3 class="hc-card-title">Harvest, poured</h3>
            <p class="hc-card-desc">September and October bring the apple press and the smell of cider, on roads that empty out once the summer boats thin.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/saltspring-mosaic-2.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">06</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The arrival</span>
            <h3 class="hc-card-title">Thirty five minutes over the water</h3>
            <p class="hc-card-desc">A scheduled floatplane from Vancouver sets the island down below you before you land. It is the arrival we build first.</p>
          </div>
        </div>
      </div>
      <p class="small" style="margin-top:12px">Drag the cards to browse the island.</p>
    </div>
  </section>

  <section class="band-white" aria-label="Who a Salt Spring journey suits">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">For every traveller</div>
        <h2 class="section-title">The island, <em>many ways</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">💍</span><div class="exp-title">Couples & Honeymoons</div><p class="exp-body">Farm tables, cider, and the quietest roads in the Gulf Islands. Autumn is our pick: harvest stalls, long light, and the island to yourselves.</p><a href="/experiences/honeymoon-proposals/" class="exp-cta">Plan the slow days</a></div>
        <div class="exp-card"><span class="exp-icon">🌿</span><div class="exp-title">Families</div><p class="exp-body">Lake swimming at Cusheon in summer, farm gates, market pastries, and days short enough to stop while everyone is still happy.</p><a href="/experiences/family-tours/" class="exp-cta">Family journeys</a></div>
        <div class="exp-card"><span class="exp-icon">🍁</span><div class="exp-title">Retirees</div><p class="exp-body">Flat walking, short drives, and no departure before half past eight. The market walk is a kilometre on firm ground, with a bench every hundred metres.</p><a href="/experiences/retirement-travel/" class="exp-cta">Retiree journeys</a></div>
        <div class="exp-card"><span class="exp-icon">🧭</span><div class="exp-title">Independent Travellers</div><p class="exp-body">You have seen the ferry-queue version of Salt Spring. We build the private one: the market early, the producers the day boats miss, and the floatplane in.</p><a href="/experiences/private-tours/" class="exp-cta">Private journeys</a></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Planning notes for Salt Spring">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">What to know <em>before you go</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">Getting there</h3><p>A scheduled floatplane from Vancouver takes about thirty five minutes, or the ferry crosses with the private vehicle on deck. Either way, you land with the car and the guide already in place.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Best season</h3><p>May to October for the market season. September and October bring the harvest and the empty roads. Winter is quiet to the point of empty, and we build it only for guests who want exactly that.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The Saturday market</h3><p>Runs roughly April to October and sets the shape of the stay. We anchor one Saturday on it and plan the other days around it, never the reverse.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">How long</h3><p>Two to four nights. One market morning, one lake or orchard day, and one day with nothing booked, which on this island is the point.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Getting around</h3><p>One base, one private vehicle, the same guide throughout. Drives run minutes, so the days flex around weather and appetite instead of a timetable.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Pacing and care</h3><p>Flat ground, short walks, and no departure before half past eight. The nearest hospital is on the island, minutes from the harbour, and we note it in every itinerary.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we design this journey">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Built around a market morning</h2>
          <p>Island time is the point, so the Saturday market anchors the stay and everything else is planned around it. One base, one vehicle, the same guide from floatplane to farewell, and no day that starts before breakfast.</p>
          <p>Everything here has been done first: the market before the crowd, the chairs at the Maxwell lookout, the table where the food was grown in sight of the plates. If a producer sells to the island first and visitors second, that is where we eat.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/saltspring-guide.jpg" width="1400" height="800" alt="Guide and guests walking a farm road on Salt Spring Island" loading="lazy">
          <figcaption>A kilometre of market walk, and a bench every hundred metres.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Longer journeys">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">One island, one journey</div>
      <h2 class="section-title">Salt Spring is rarely <em>the only stop.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Most of our guests pair it with Tofino for a Gulf Islands and coast journey of seven to ten days, or with the Rockies for the shape that crosses from the Pacific to the peaks. See how a private Canada journey is built, then tell us what your version looks like.</p>
      <a class="btn" href="/experiences/private-tours/">How private journeys work</a>
    </div>
  </section>
""",
    cta_band=("/images/saltspring-landscape.jpg",
              "Salt Spring Island private tour: the view from Mount Maxwell over the southern Gulf Islands",
              "Ready to see Salt Spring the right way?",
              "Tell us what you are imagining. We will come back within 24 hours.",
              "Begin Your Journey"),

    faq=[
        ("How do you get to Salt Spring Island?",
         "<p>By scheduled floatplane from Vancouver, roughly thirty five minutes, or by ferry with the private vehicle on deck. The floatplane is the more memorable arrival and the one we build first for most journeys, because the island opens up below you before you land.</p>"),
        ("Is Salt Spring Island suited to travellers who prefer a slower pace?",
         "<p>It is the best leg in our portfolio for exactly that. Short drives, flat walking, one base, and a day that can be rearranged at breakfast without losing anything. We hold the same vehicle and the same guide for the whole stay.</p>"),
        ("What can we do on Salt Spring with children?",
         "<p>Farm visits, the market, lake swimming at Cusheon in summer, and short walks with a guide. Families do well here when the days stay short, because the island's distances make a relaxed rhythm easy to keep.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_attraction(
        "Salt Spring Island, British Columbia, Canada",
        "Private luxury tours of Salt Spring Island in the Gulf Islands, including the Ganges market, Mount Maxwell, farm and dairy visits, and floatplane arrivals.",
        "destinations/salt-spring-island-private-tour/", 48.8567, -123.4983, "/images/saltspring-hero.jpg",
        ["Retirees", "Couples", "Independent travellers"])],
)

# ---------------------------------------------------------------- Jasper

JASPER = dict(
    path="destinations/jasper-private-tour/",
    title="Jasper Private Tour | Luxury Canadian Rockies Journeys",
    desc="A Jasper private tour built around dark skies, quiet lakes, the Athabasca Glacier, and the Icefields Parkway, with wildlife at distance. Maximum eight guests.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Jasper", "/destinations/jasper-private-tour/")],
    og_image="/images/jasper-hero.jpg",
    hero=dict(
        eyebrow="Alberta, Canadian Rockies",
        h1="Jasper Private Tour: Dark Skies and Empty Switchbacks",
        sub="Larger, quieter, and darker than anywhere else in the Rockies. A glacier you can walk to before breakfast, elk on the roadside at dusk, and a night sky with nothing between you and it.",
        img="/images/jasper-hero.jpg",
        alt="Jasper private tour: Maligne Lake and the Canadian Rockies under a dark sky at dusk",
        cta="Plan My Jasper Journey",
    ),
    best_for=["Independent travellers", "Couples", "Retirees", "Families with children over 8"],
    body="""
  <section class="band-white" aria-label="Jasper journey facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Best season</div><p class="small">Late June to mid September for open roads, September for the golden larches, winter for dark skies and aurora</p></div>
        <div><div class="lab">Getting there</div><p class="small">Fly to Edmonton or Calgary, and the parkway drive belongs to the journey from the first kilometre</p></div>
        <div><div class="lab">Ideal stay</div><p class="small">Two to four nights in Jasper, with the parkway days built in at each end</p></div>
        <div><div class="lab">Character</div><p class="small">Dark skies, glacial water, and a park that is larger and quieter than Banff</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Why Jasper for private travel">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The park</div>
          <h2 class="section-title">The Rockies before <em>the crowds found them.</em></h2>
          <p>Jasper is larger than Banff, quieter in every season, and it holds one of the largest dark-sky preserves on the planet, which means a sky you will remember long after the photographs. The town is small, the wildlife is close to the road but never approached, and the pace of a day here is set by light rather than by a coach timetable.</p>
          <p>We lead with Jasper and work outward: the Icefields Parkway south to Lake Louise, Yoho beyond it, and Banff only in the quiet hours. Some trails and services were affected by the 2024 wildfire, so we confirm the current status of every road and walk with Parks Canada before we build, and we say plainly what is open.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/jasper-landscape.jpg" width="1400" height="800" alt="Icefields Parkway private tour looking south toward the Columbia Icefield in the Canadian Rockies" loading="lazy">
          <figcaption>Fill the tank at Jasper or Lake Louise. The parkway runs 232 kilometres with very few services.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="What we build into a Jasper journey">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What we build into a <em>Jasper journey</em></h2>
        <p class="lede">The quiet hours, the dark hours, and the drive between them.</p>
      </div>
      <div class="hc-carousel" id="hcCarousel" tabindex="0" aria-label="Jasper experiences, scroll horizontally">
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/jasper-maligne.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">01</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Maligne Lake</span>
            <h3 class="hc-card-title">The quiet hour on the water</h3>
            <p class="hc-card-desc">Maligne and Medicine Lake with a guide who knows when the day visitors come and go. A canoe on still water is the way to do it, not a seat on a cruise.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/jasper-darksky.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">02</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Dark Sky Preserve</span>
            <h3 class="hc-card-title">A sky with nothing between you and it</h3>
            <p class="hc-card-desc">An evening with a guide who knows where to stand, when the moon is out of the way, and which lake reflects the Milky Way best that week.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/jasper-glacier.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">03</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Columbia Icefield</span>
            <h3 class="hc-card-title">The ice you can walk to</h3>
            <p class="hc-card-desc">A guided walk toward the Athabasca Glacier on the Icefields Parkway, with the scale of the icefield in front of you the whole way.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/jasper-wildlife.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">04</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Wildlife</span>
            <h3 class="hc-card-title">Elk at the roadside at dusk</h3>
            <p class="hc-card-desc">Elk, bighorn sheep, black bears, and sometimes a grizzly on a distant slope. Viewed from the vehicle or a marked viewpoint, guide-led, always.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/jasper-mosaic-1.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">05</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Pyramid Lake</span>
            <h3 class="hc-card-title">The still-water morning</h3>
            <p class="hc-card-desc">A canoe out before breakfast while the peaks double themselves in the water, five minutes from the townsite and a world away from the parkway.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/jasper-mosaic-2.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">06</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The townsite</span>
            <h3 class="hc-card-title">A town the size of a village</h3>
            <p class="hc-card-desc">Walkable, small, and kept dark on purpose so the sky stays the main event. After dinner, the guide points out what the streetlights usually hide.</p>
          </div>
        </div>
      </div>
      <p class="small" style="margin-top:12px">Drag the cards to browse the park.</p>
    </div>
  </section>

  <section class="band-white" aria-label="Who a Jasper journey suits">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">For every traveller</div>
        <h2 class="section-title">The park, <em>many ways</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">💍</span><div class="exp-title">Couples & Honeymoons</div><p class="exp-body">A dark-sky evening for two, a canoe at the quiet hour, and the lodge at dusk. September is our pick: larches turning, elk in rut, and the roads thinning out.</p><a href="/experiences/honeymoon-proposals/" class="exp-cta">Plan the quiet days</a></div>
        <div class="exp-card"><span class="exp-icon">🌿</span><div class="exp-title">Families</div><p class="exp-body">Children over eight do best here. Canoeing replaces swimming, every walk starts with a wildlife briefing, and car seats are pre-sourced for every vehicle on the parkway.</p><a href="/experiences/family-tours/" class="exp-cta">Family journeys</a></div>
        <div class="exp-card"><span class="exp-icon">🍁</span><div class="exp-title">Retirees</div><p class="exp-body">The Icefields Parkway by private vehicle, with short walks and long views. No departure before half past eight, and an afternoon rest built into every day.</p><a href="/experiences/retirement-travel/" class="exp-cta">Retiree journeys</a></div>
        <div class="exp-card"><span class="exp-icon">🧭</span><div class="exp-title">Independent Travellers</div><p class="exp-body">You have seen what the coach queues do to the Rockies. We build the private version: the parkway in the quiet hours, the lake before the boats, and the sky after dark.</p><a href="/experiences/private-tours/" class="exp-cta">Private journeys</a></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Planning notes for Jasper">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">What to know <em>before you go</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">Getting there</h3><p>Fly to Edmonton or Calgary, and the drive belongs to the journey from the first kilometre. Your guide and private vehicle are with you from the airport, so the parkway is never a transfer, it is the point.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Best season</h3><p>Late June to mid September for open roads and long light, mid September to early October for golden larches and thin crowds. Winter brings aurora and frozen lakes, between minus fifteen and minus twenty five.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The Icefields Parkway</h3><p>232 kilometres between Lake Louise and Jasper with very few services. We fill the tank at Jasper or Lake Louise and carry what the day needs, because the next fuel stop can be an hour behind you.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Altitude and pacing</h3><p>Lake Louise sits near 1,600 metres and the passes climb higher. We build a gentle first day at altitude for every guest, and the itinerary states the walking honestly for each stop.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Wildfire recovery</h3><p>Parts of the park were affected by the 2024 wildfire, and some trails and services reopen on their own schedule. We confirm current status with Parks Canada before we build, and we say plainly what is open.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Pacing and care</h3><p>One base, one vehicle, the same guide throughout, and no departure before half past eight. The park keeps a health centre in the townsite, and travel medical insurance is essential in this country, so we say so in writing.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we design this journey">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Driven many times, not mapped once</h2>
          <p>The Icefields Parkway is among the great drives on the continent and one of the least forgiving if you have not done it. We drive it slowly, with a guide who has done it many times, and we plan the wildlife stops around light rather than around a schedule.</p>
          <p>Everything here has been done first: the lake before the boats, the chairs at the lookout, the sky from the shore of a lake that faces the right way. Where a wildfire or a weather system changes the plan, the fallback is already written: a different valley at the same hour, and a second location for any evening we have promised on the water or the ice.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/jasper-guide.jpg" width="1400" height="800" alt="Private guide pointing out a distant grizzly from a safe distance in Jasper" loading="lazy">
          <figcaption>The reaction to a first bear sighting tells us everything about a traveller.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Longer journeys">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">One park, one journey</div>
      <h2 class="section-title">Jasper is rarely <em>the only stop.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Most of our guests run the parkway south to Banff and Yoho for a full Rockies week, or pair the peaks with the Pacific and Tofino for the coast-and-mountains shape. See how a private Canada journey is built, then tell us what your version looks like.</p>
      <a class="btn" href="/experiences/private-tours/">How private journeys work</a>
    </div>
  </section>
""",
    cta_band=("/images/jasper-hero.jpg",
              "Jasper private tour: Maligne Lake and the Canadian Rockies at dusk under a dark sky",
              "Ready to see Jasper the right way?",
              "Tell us what you are imagining. We will come back within 24 hours.",
              "Begin Your Journey"),
    faq=[
        ("Is Jasper better than Banff for a private tour?",
         "<p>For a private tour, Jasper is the better base: larger, quieter, darker, and less crowded in every season. Banff and Lake Louise are worth your time at dawn, in shoulder season, or by routes that bypass the queues, and we usually close a Rockies journey with them rather than opening it there.</p>"),
        ("When should we visit Jasper National Park?",
         "<p>Late June to mid September for open roads and long light, or mid September to early October for golden larches and thinner crowds. Winter is beautiful and genuinely cold, between minus fifteen and minus twenty five, and it is best for guests who want aurora and frozen lakes.</p>"),
        ("Will we see bears on a Jasper private tour?",
         "<p>Often, and always at a distance. Wildlife is viewed guide-led from the vehicle or a marked viewpoint, never approached on foot, and every walk begins with a safety briefing. We will not promise a sighting, because it is a national park and not a zoo.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_attraction(
        "Jasper, Alberta, Canada",
        "Private luxury tours of Jasper National Park and the Jasper Dark Sky Preserve, including Maligne Lake, the Athabasca Glacier, and the Icefields Parkway.",
        "destinations/jasper-private-tour/", 52.8737, -118.0814, "/images/jasper-hero.jpg",
        ["Independent travellers", "Couples", "Retirees", "Families"])],
)

# ---------------------------------------------------------------- Banff and Yoho

BANFF = dict(
    path="destinations/banff-yoho-private-tour/",
    title="Icefields Parkway Private Tour | Banff and Yoho | Canada",
    desc="An Icefields Parkway private tour with Banff and Yoho in the quiet hours: Lake Louise at sunrise, Emerald Lake, and Takakkaw Falls. Private guide throughout.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Banff and Yoho", "/destinations/banff-yoho-private-tour/")],
    og_image="/images/banff-hero.jpg",
    hero=dict(
        eyebrow="Alberta and British Columbia",
        h1="Icefields Parkway Private Tour: Banff and Yoho in the Quiet Hours",
        sub="The lake at sunrise, before the day visitors arrive. A quieter valley next door. And 232 kilometres of parkway between two mountain towns, driven slowly.",
        img="/images/banff-hero.jpg",
        alt="Icefields Parkway private tour: Lake Louise at sunrise with the Victoria Glacier behind",
        cta="Plan My Rockies Journey",
    ),
    best_for=["Independent travellers", "Couples", "Retirees", "Families with children over 8", "Corporate groups"],
    body="""
  <section class="band-white" aria-label="Banff and Yoho journey facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Best season</div><p class="small">Mid September to early October for golden larches and thin crowds, late June to mid September for everything open, winter for frozen lakes and quiet roads</p></div>
        <div><div class="lab">Getting there</div><p class="small">Fly to Calgary, ninety minutes from the park gate, and the drive belongs to the journey from the first kilometre</p></div>
        <div><div class="lab">Ideal stay</div><p class="small">Three to five nights split between Banff, Lake Louise, and the quieter valley of Yoho</p></div>
        <div><div class="lab">Character</div><p class="small">The famous lakes at the right hour, a parkway built for slow driving, and a quieter valley next door</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Why Banff and Yoho for private travel">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The region</div>
          <h2 class="section-title">The famous lakes, <em>at the right hour.</em></h2>
          <p>Banff and Lake Louise are the most photographed places in Canada, and in July they feel like it. We do not refuse them. We take guests at dawn, in shoulder season, or by routes that bypass the queues, and we treat them as a chapter inside a Rockies journey rather than the whole book. The reward is the lake at sunrise with the mist still on it, and a shoreline with three walkers on it instead of three hundred.</p>
          <p>Yoho is the quieter neighbour, half an hour west, with Emerald Lake, Takakkaw Falls, and roads where you hear the river before you see it. Access rules around Lake Louise and Moraine Lake have changed materially in recent years, so we confirm the current system before every journey and build the day around it rather than around last year's instructions.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/banff-landscape.jpg" width="1400" height="800" alt="Banff luxury tour: the Bow Valley and the Icefields Parkway seen from a quiet viewpoint" loading="lazy">
          <figcaption>Lake Louise, twenty minutes after sunrise, when the day visitors are still in bed.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="What we build into a Banff and Yoho journey">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What we build into a <em>Rockies journey</em></h2>
        <p class="lede">The famous lakes at the right hour, and the quiet country between them.</p>
      </div>
      <div class="hc-carousel" id="hcCarousel" tabindex="0" aria-label="Banff and Yoho experiences, scroll horizontally">
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/banff-lakelouise.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">01</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Lake Louise</span>
            <h3 class="hc-card-title">The lake before the coaches</h3>
            <p class="hc-card-desc">A start before eight, the shore walk while the mist is still on the water, and coffee as the first coaches pull in behind us. Dawn is the whole point.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/banff-icefields.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">02</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Icefields Parkway</span>
            <h3 class="hc-card-title">232 kilometres, driven slowly</h3>
            <p class="hc-card-desc">Glacier, waterfall, and empty switchback between Lake Louise and Jasper, at your pace, with the fuel and food stops planned honestly.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/banff-yoho.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">03</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Yoho National Park</span>
            <h3 class="hc-card-title">The quieter valley next door</h3>
            <p class="hc-card-desc">Emerald Lake for an easy shore walk and a canoe, and roads where you hear the river long before you see it. Half an hour from Lake Louise, a world away in pace.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/banff-canoe.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">04</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">On the water</span>
            <h3 class="hc-card-title">A canoe instead of a swim</h3>
            <p class="hc-card-desc">Glacial lakes sit far too cold to swim, so the water activity is a canoe with a guide, on water that photographs badly at noon and beautifully at seven in the morning.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/banff-mosaic-1.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">05</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Takakkaw Falls</span>
            <h3 class="hc-card-title">The falls you can walk to</h3>
            <p class="hc-card-desc">One of the tallest waterfalls in Canada, and the walk from the car park to its base is short enough for almost every guest. We time it for the morning light.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/banff-mosaic-3.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">06</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Wildlife</span>
            <h3 class="hc-card-title">Bighorn at the roadside</h3>
            <p class="hc-card-desc">Bighorn sheep, elk, and sometimes a bear on a distant slope. Viewed from the vehicle or a marked viewpoint, guide-led, always at a distance.</p>
          </div>
        </div>
      </div>
      <p class="small" style="margin-top:12px">Drag the cards to browse the region.</p>
    </div>
  </section>

  <section class="band-white" aria-label="Who a Banff and Yoho journey suits">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">For every traveller</div>
        <h2 class="section-title">The Rockies, <em>at your pace</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">💍</span><div class="exp-title">Couples & Honeymoons</div><p class="exp-body">A canoe on Emerald Lake before the day boats, a sunrise shoreline with nobody on it, and the lodge fireplace after dark. September is our pick: golden larches, elk in the valley, and thinning roads.</p><a href="/experiences/honeymoon-proposals/" class="exp-cta">Plan the quiet days</a></div>
        <div class="exp-card"><span class="exp-icon">🌿</span><div class="exp-title">Families</div><p class="exp-body">Children over eight do best here. Wildlife briefings before every walk, car seats pre-sourced for the parkway, and canoeing instead of swimming, because the water is glacial.</p><a href="/experiences/family-tours/" class="exp-cta">Family journeys</a></div>
        <div class="exp-card"><span class="exp-icon">🍁</span><div class="exp-title">Retirees</div><p class="exp-body">The parkway by private vehicle, with short walks and long views. No departure before half past eight, an afternoon rest built into every day, and the drive broken by real meals.</p><a href="/experiences/retirement-travel/" class="exp-cta">Retiree journeys</a></div>
        <div class="exp-card"><span class="exp-icon">🧭</span><div class="exp-title">Independent Travellers</div><p class="exp-body">You have seen what the coach queues do to Lake Louise. We build the private version: the lake at dawn, the quieter valley after lunch, and the parkway when the coaches are somewhere else.</p><a href="/experiences/private-tours/" class="exp-cta">Private journeys</a></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Planning notes for Banff and Yoho">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">What to know <em>before you go</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">Getting there</h3><p>Fly to Calgary, and the park gate is ninety minutes west. Your guide and private vehicle are with you from the airport, so the parkway is never a transfer, it is the point.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Best season</h3><p>Mid September to early October for golden larches, elk, and room at every viewpoint. Late June to mid September for everything open and long light. Winter brings skiing, ice walks, and frozen lakes, with far fewer people on the parkway.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The Icefields Parkway</h3><p>232 kilometres between Lake Louise and Jasper with very few services. We fill the tank before we start and carry what the day needs, because the next fuel stop can be an hour behind you.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Access rules</h3><p>The Moraine Lake road closed to private vehicles in 2023, and parking at Lake Louise is managed. We confirm the current rules with Parks Canada before every journey and build the day around the system that exists, not the one from memory.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Altitude and pacing</h3><p>Lake Louise sits near 1,600 metres and the passes climb higher. We build a gentle first day at altitude for every guest, and the itinerary states the walking honestly for each stop.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Pacing and care</h3><p>One base, one vehicle, the same guide throughout, and no departure before half past eight. Banff has a hospital and the park keeps year-round warden coverage, and travel medical insurance is essential in this country, so we say so in writing.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we design this journey">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Checked before every journey, not assumed</h2>
          <p>The Rockies change their own rules: the Moraine Lake road, the parking systems at Lake Louise, the season dates for the Yoho falls road, and the recovery work still under way after the 2024 wildfire season. We check the current status of every road and walk with Parks Canada before we quote, and we design the day around what is true this month.</p>
          <p>Everything here has been done first: the lake before the boats, the viewpoint before the sun clears the ridge, the falls before the midday traffic. Where a rule or a weather system changes the plan, the fallback is already written: a different valley at the same hour, and a second location for any morning we have promised on the water.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/banff-guide.jpg" width="1400" height="800" alt="Guide setting up a sunrise viewpoint above Lake Louise for private guests" loading="lazy">
          <figcaption>Coffee at the lake, twenty minutes after sunrise.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Longer journeys">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">One region, one journey</div>
      <h2 class="section-title">Banff is rarely <em>the only stop.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Most of our guests run the parkway north to Jasper for a full Rockies week, or pair the peaks with the Pacific and Tofino for the coast-and-mountains shape. See how a private Canada journey is built, then tell us what your version looks like.</p>
      <a class="btn" href="/experiences/private-tours/">How private journeys work</a>
    </div>
  </section>
""",
    cta_band=("/images/banff-hero.jpg",
              "Icefields Parkway private tour: Lake Louise at sunrise with the Victoria Glacier behind",
              "Ready to see the Rockies the right way?",
              "Tell us what you are imagining. We will come back within 24 hours.",
              "Begin Your Journey"),
    faq=[
        ("What is the Icefields Parkway and how long does it take?",
         "<p>It is the 232 kilometre drive between Lake Louise and Jasper, one of the great mountain roads on earth. Driven straight through it takes about three and a half hours; done properly with stops at the glaciers, waterfalls, and viewpoints, it is a full day or two. We drive it slowly, and we fill the tank before we start, because services along it are very limited.</p>"),
        ("How do you avoid the crowds at Lake Louise and Moraine Lake?",
         "<p>Timing and access planning. We arrive at sunrise or in shoulder season, and we check the current road and parking rules before every journey, because they have changed in recent years. Where access is restricted, we build the day around the current system instead of a route that no longer works.</p>"),
        ("Is Yoho worth adding to a Banff journey?",
         "<p>Yoho is what Banff was before the world found it: Emerald Lake, Takakkaw Falls, and quiet roads, half an hour from Lake Louise. We include it in most Rockies journeys, and for guests who want the scenery without the volume, we lead with it.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_attraction(
        "Banff and Yoho National Parks, Canada",
        "Icefields Parkway private tours with Banff and Yoho National Parks, including Lake Louise at sunrise, Emerald Lake, Takakkaw Falls, and the Athabasca Glacier.",
        "destinations/banff-yoho-private-tour/", 51.1784, -115.5708, "/images/banff-hero.jpg",
        ["Independent travellers", "Couples", "Retirees", "Families", "Corporate groups"])],
)

# ---------------------------------------------------------------- Prince Edward County

PEC = dict(
    path="destinations/prince-edward-county-private-tour/",
    title="Prince Edward County Private Tour | Ontario Wine Country",
    desc="A Prince Edward County private tour with wine, farm tables, and the Sandbanks dunes, plus a private Thousand Islands cruise from Kingston. Flat, unhurried days.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Prince Edward County", "/destinations/prince-edward-county-private-tour/")],
    og_image="/images/pec-hero.jpg",
    hero=dict(
        eyebrow="Ontario, Lake Ontario and Lake Erie",
        h1="Prince Edward County Private Tour: Wine, Farm Tables, and Sandbanks Dunes",
        sub="Limestone towns, vineyards a bicycle ride apart, and a county where the food is grown within sight of the table. The road we know best, ridden end to end.",
        img="/images/pec-hero.jpg",
        alt="Prince Edward County private tour: a vineyard row and farm table in Ontario wine country",
        cta="Plan My Lakeshore Journey",
    ),
    best_for=["Retirees", "Couples", "Independent travellers", "Corporate groups"],
    body="""
  <section class="band-white" aria-label="Prince Edward County journey facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Best season</div><p class="small">September and October for harvest and colour in the same fortnight, May to October for lake days and long vineyard evenings</p></div>
        <div><div class="lab">Getting there</div><p class="small">Fly to Toronto. Kingston is about three hours east by road, and the county begins another ninety minutes along the same shore</p></div>
        <div><div class="lab">Ideal stay</div><p class="small">Three to four nights split between the limestone waterfront at Kingston and a village base inside the county</p></div>
        <div><div class="lab">Character</div><p class="small">Canada's youngest serious wine region, farm tables a bicycle ride apart, and the Sandbanks dunes where the lake behaves like a coast</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Why Prince Edward County for private travel">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The region</div>
          <h2 class="section-title">A county built on farm roads, <em>not on coach routes.</em></h2>
          <p>Almost no luxury operator sells southern Ontario as a journey, which is exactly why it belongs in ours. The county sits an hour and a half east of the heritage waterfront at Kingston, and it holds Canada's youngest serious wine region, farm tables that fill up on a Friday, and the Sandbanks dunes, where the lake behaves like a coast.</p>
          <p>The whole lakeshore from Kingston to Essex County has been ridden on a bicycle rather than driven past, and that changes what we recommend: the vineyard with the winemaker still pouring, the county road with the view, and the day built so nobody spends it in a car. Appointments do the work here the way they do in Niagara. The tasting with the person who made the wine, the table that is yours for the afternoon, and the dunes at the hour the day visitors have gone home.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/pec-landscape.jpg" width="1400" height="800" alt="Prince Edward County private tour: a vineyard row and farm table overlooking Lake Ontario in Ontario wine country" loading="lazy">
          <figcaption>Sandbanks dunes, late afternoon, when the day visitors have gone home.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="What we build into a Prince Edward County journey">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What we build into <em>a lakeshore journey</em></h2>
        <p class="lede">Two or three county days, one long farm table, and the water always in reach.</p>
      </div>
      <div class="hc-carousel" id="hcCarousel" tabindex="0" aria-label="Prince Edward County experiences, scroll horizontally">
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/pec-wine.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">01</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Cellar appointments</span>
            <h3 class="hc-card-title">Winemakers who still pour their own</h3>
            <p class="hc-card-desc">The county is small enough that the person who made the wine still sits down with you. We book those visits first, at hours the tasting rooms are quiet, and build the day around them.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/pec-dunes.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">02</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Sandbanks dunes</span>
            <h3 class="hc-card-title">A lake that behaves like a coast</h3>
            <p class="hc-card-desc">The dunes at the mouth of the bay hold water that runs clear and shallow for a hundred metres, warm enough to swim by August. We take them late, after the day visitors have gone home.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/pec-kingston.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">03</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Kingston and the islands</span>
            <h3 class="hc-card-title">Limestone streets and a private cruise</h3>
            <p class="hc-card-desc">The journey opens on the limestone waterfront and the old market square, then out on the water: a private Thousand Islands cruise with a story on every island. Toronto is the gateway.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/pec-bike.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">04</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The Waterfront Trail</span>
            <h3 class="hc-card-title">Flat kilometres by electric bicycle</h3>
            <p class="hc-card-desc">The shoreline trail is flat, quiet, and exactly the right speed for this region. Your guide rides beside you, and the vineyard stops sit close enough that nobody counts kilometres.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/pec-mosaic-2.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">05</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Farm tables</span>
            <h3 class="hc-card-title">Lunch within sight of the field</h3>
            <p class="hc-card-desc">The county grows what it serves. A long table on the farm, the menu set by the week's harvest, and nothing rushed: this is the meal guests remember from the whole journey.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/pec-mosaic-3.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">06</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The southern shore</span>
            <h3 class="hc-card-title">Point Pelee and the monarchs</h3>
            <p class="hc-card-desc">The mainland's southernmost point is a May destination for migrating birds and a September one for monarchs. The ferry timetable decides the day, so we check it before we build anything around it.</p>
          </div>
        </div>
      </div>
      <p class="small" style="margin-top:12px">Drag the cards to browse the region.</p>
    </div>
  </section>

  <section class="band-white" aria-label="Who a Prince Edward County journey suits">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">For every traveller</div>
        <h2 class="section-title">The lakeshore, <em>at your pace</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">&#128141;</span><div class="exp-title">Couples & Honeymoons</div><p class="exp-body">Wine afternoons that end with dinner on the farm, the dunes at the quiet hour, and the simplest romantic days in the portfolio. June and September are the two windows we recommend first.</p><a href="/experiences/honeymoon-proposals/" class="exp-cta">Plan the quiet days</a></div>
        <div class="exp-card"><span class="exp-icon">&#128188;</span><div class="exp-title">Corporate Groups</div><p class="exp-body">Three hours from Toronto makes this a two day retreat rather than a rush: the private cruise out of Kingston, a winery dinner in the county, and transport handled from the city.</p><a href="/experiences/corporate-mice/" class="exp-cta">Corporate retreats</a></div>
        <div class="exp-card"><span class="exp-icon">&#127807;</span><div class="exp-title">Retirees</div><p class="exp-body">Flat terrain, short drives, and no departure before half past eight. Two appointments a day rather than a circuit, an afternoon rest built in, and the cellar steps checked before we book them.</p><a href="/experiences/retirement-travel/" class="exp-cta">Retiree journeys</a></div>
        <div class="exp-card"><span class="exp-icon">&#129517;</span><div class="exp-title">Independent Travellers</div><p class="exp-body">You have seen what a coach party does to a tasting room. We build the private version: the winemaker, the quiet hour on the dunes, and a guide who has ridden every road we recommend.</p><a href="/experiences/private-tours/" class="exp-cta">Private journeys</a></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Planning notes for Prince Edward County">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">What to know <em>before you go</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">Getting there</h3><p>Fly to Toronto, and the lakeshore runs east from there: about three hours to Kingston by road, and the county another ninety minutes along the same shore. Your guide and private vehicle collect you at the airport, so the journey starts at the first vineyard view rather than at a rental counter.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Best season</h3><p>September and October bring the harvest and the colour within a fortnight of each other, the strongest window in the county. May and June are quiet and green, July and August belong to the dunes, and January pairs this region with the icewine harvest in Niagara for a winter journey.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The wine calendar</h3><p>The county pours its newest vintages through the autumn, and the small wineries run on appointments rather than walk-in bars. We check the current vintage calendar before we book anything, and we keep a second appointment in reserve for any day the first one shifts.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Appointments and tables</h3><p>Farm tables fill on summer Fridays and the winemaker visits book out through the harvest. We reserve both before we plan the rest, because the table and the tasting are the two things a schedule cannot bend around.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The bicycle days</h3><p>The Waterfront Trail rides flat from Kingston west through the county, and the electric versions make the vineyard stops effortless. We ride it in the morning when the county roads are quietest, with the day's vehicle carrying the tasting and the picnic.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Pacing and care</h3><p>A driver stays with the journey for its full length, which is what lets the days run at county speed. We recommend travel medical insurance for guests arriving from outside Canada and say so in writing, and the itinerary states the walking and riding at every stop honestly.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we design this journey">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">A lakeshore built for short drives</h2>
          <p>Ontario looks flat on a map and is anything but on a schedule, so we cluster the days: Kingston and the islands first, then the county, then Niagara if the journey asks for it. Nobody spends three hours in a vehicle to reach a vineyard.</p>
          <p>The whole road from Kingston to Essex has been ridden end to end, which is why we can tell you which town deserves two nights, which winery is worth an appointment, and which viewpoint is a photograph rather than an experience. We plan around the ferry timetable, the harvest dates, and the hour the dunes empty out.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/pec-guide.jpg" width="1400" height="800" alt="Guide and guests on bicycles beside the Waterfront Trail in Ontario" loading="lazy">
          <figcaption>Flat, quiet, and exactly the right speed for this shoreline.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Longer journeys">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">One region, one journey</div>
      <h2 class="section-title">Prince Edward County is rarely <em>the only stop.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Most of our guests pair it with Niagara-on-the-Lake for a lakeshore journey of seven to ten days, or run it as the quiet half of a trip that opens in Toronto. See how a private Canada journey is built, then tell us what your version looks like.</p>
      <a class="btn" href="/experiences/private-tours/">How private journeys work</a>
    </div>
  </section>
""",
    cta_band=("/images/pec-hero.jpg",
              "Prince Edward County private tour: a vineyard row and farm table in Ontario wine country",
              "Ready to plan a lakeshore journey?",
              "Tell us what you are imagining. We will come back within 24 hours.",
              "Begin Your Journey"),
    faq=[
        ("What is there to do in Prince Edward County?",
         "<p>Wine visits with the people who make it, farm tables, the Sandbanks dunes and the lake, and a county small enough to see by bicycle. Paired with Kingston, ninety minutes west, it becomes a proper journey with heritage, water, and food in it.</p>"),
        ("Is Prince Edward County good for a luxury Ontario wine tour?",
         "<p>It is the best-value wine region in the province for a private tour, and it is the one where winemakers will still sit down with you. Niagara-on-the-Lake has the older cellars and the icewine; the county has the appointments and the farm kitchens.</p>"),
        ("When is the best time for an Ontario lakeshore journey?",
         "<p>May to October, and September to October above all, when the harvest and the autumn colour overlap. Point Pelee is at its best in May for migrating birds and September for monarchs.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_attraction(
        "Prince Edward County, Ontario, Canada",
        "Private luxury tours of Prince Edward County wine country in Ontario, with the Sandbanks dunes, farm tables, and a private Thousand Islands cruise from Kingston.",
        "destinations/prince-edward-county-private-tour/", 44.0043, -77.1481, "/images/pec-hero.jpg",
        ["Retirees", "Couples", "Independent travellers", "Corporate groups"])],
)

# ---------------------------------------------------------------- Niagara-on-the-Lake

NOTL = dict(
    path="destinations/niagara-on-the-lake-private-tour/",
    title="Niagara-on-the-Lake Private Tour | Ontario Wine Journeys",
    desc="A Niagara-on-the-Lake private tour with cellar visits beside the winemaker, icewine in January, the heritage town, and a private driver for the day.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Niagara-on-the-Lake", "/destinations/niagara-on-the-lake-private-tour/")],
    og_image="/images/notl-hero.jpg",
    hero=dict(
        eyebrow="Ontario, Niagara wine country",
        h1="Niagara-on-the-Lake Private Tour: Winery Visits with the Winemaker",
        sub="Canada's oldest wine region, an hour and a half from Toronto, with cellars that will open a private tasting for the right appointment and icewine harvested on the coldest nights of January.",
        img="/images/notl-hero.jpg",
        alt="Niagara-on-the-Lake private tour: a winery cellar tasting beside the winemaker in Ontario",
        cta="Plan My Wine Journey",
    ),
    best_for=["Couples", "Retirees", "Independent travellers", "Corporate groups"],
    body="""
  <section class="band-white" aria-label="Niagara-on-the-Lake journey facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Best season</div><p class="small">Late September to mid October for harvest and colour, May to October for long evenings and the theatre season, January for the icewine harvest</p></div>
        <div><div class="lab">Getting there</div><p class="small">Fly to Toronto, about an hour and a half by road, and the drive down the Niagara Parkway is the first vineyard view of the journey</p></div>
        <div><div class="lab">Ideal stay</div><p class="small">Two to three nights in or beside the town, walking distance to the main street and the river</p></div>
        <div><div class="lab">Character</div><p class="small">Cellar appointments with the people who made the wine, a heritage town built for walking, and icewine picked at night in the cold</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Why Niagara-on-the-Lake for private travel">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The region</div>
          <h2 class="section-title">Cellars with real age, <em>at the mouth of the river.</em></h2>
          <p>This is the oldest wine region in the country, and it behaves like a European appellation: a heritage town where the Niagara River meets Lake Ontario, cellars with real age on them, and vines grown on the benches of the escarpment above. The town was the first capital of Upper Canada, and the main street still carries the stone of that period. The falls are twenty minutes away, which is close enough for a morning and far enough to leave behind by lunch.</p>
          <p>The difference a private journey makes here is appointments. The visit that stays with guests is the one with the person who made the wine, in a cellar rather than a tasting room, at an hour when the room is quiet. We book those first, build the day around them, and drive, so nobody at the table has to count glasses. Icewine is the other reason people come: picked by hand in the dark at temperatures below minus eight, and if your journey lands in January you can be there while the region runs on harvest.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/notl-landscape.jpg" width="1400" height="800" alt="Niagara-on-the-Lake private tour: vineyard rows above the Niagara River in autumn" loading="lazy">
          <figcaption>Vineyard rows above the river, in the week before harvest.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="What we build into a Niagara-on-the-Lake journey">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What we build into <em>a wine journey</em></h2>
        <p class="lede">Two or three cellar visits, one long lunch, and the river road between them.</p>
      </div>
      <div class="hc-carousel" id="hcCarousel" tabindex="0" aria-label="Niagara-on-the-Lake experiences, scroll horizontally">
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/notl-cellar.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">01</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Cellar appointments</span>
            <h3 class="hc-card-title">Two visits, not five</h3>
            <p class="hc-card-desc">Chosen for what you actually drink, each with the winemaker or the cellar master rather than a host reading from a card, and each booked at an hour the room is quiet.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/notl-icewine.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">02</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Icewine</span>
            <h3 class="hc-card-title">Picked at night, below minus eight</h3>
            <p class="hc-card-desc">The harvest happens when the weather allows, often around three in the morning. A winter journey here is built around that window and the festival weekends that follow it.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/notl-town.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">03</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The heritage town</span>
            <h3 class="hc-card-title">A main street built for walking</h3>
            <p class="hc-card-desc">Stone buildings from the town's years as the first capital of Upper Canada, a repertory theatre season, good coffee, and the river two blocks behind it.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/notl-dinner.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">04</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">A table at the winery</span>
            <h3 class="hc-card-title">Dinner where the wine was made</h3>
            <p class="hc-card-desc">A long table on the estate, the bottles from the cellars you walked through that afternoon, and the drive back handled so the evening can run as long as it wants to.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/notl-mosaic-1.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">05</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The river road</span>
            <h3 class="hc-card-title">The Niagara Parkway in winter</h3>
            <p class="hc-card-desc">The road along the river runs from the town to the falls, past orchards and vineyard blocks. In January it is quiet, cold, and the loveliest drive in the region.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/notl-guide.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">06</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">A driver for the day</span>
            <h3 class="hc-card-title">The day, driven for you</h3>
            <p class="hc-card-desc">One vehicle and the same guide from the moment we collect you in Toronto until the last stop. Nobody counts glasses, and nothing is rushed to make a shuttle.</p>
          </div>
        </div>
      </div>
      <p class="small" style="margin-top:12px">Drag the cards to browse the region.</p>
    </div>
  </section>

  <section class="band-white" aria-label="Who a Niagara-on-the-Lake journey suits">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">For every traveller</div>
        <h2 class="section-title">The wine country, <em>at your pace</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">&#128141;</span><div class="exp-title">Couples &amp; Honeymoons</div><p class="exp-body">An afternoon of cellar visits that ends with dinner on the estate, and the simplest romantic day in the portfolio. Late September and January are the two windows we recommend first.</p><a href="/experiences/honeymoon-proposals/" class="exp-cta">Plan the quiet days</a></div>
        <div class="exp-card"><span class="exp-icon">&#128188;</span><div class="exp-title">Corporate Groups</div><p class="exp-body">An hour and a half from Toronto makes this the easiest single day retreat we design: a private cellar visit, a tasting built around the team, dinner on the estate, and transport handled from the city.</p><a href="/experiences/corporate-mice/" class="exp-cta">Corporate retreats</a></div>
        <div class="exp-card"><span class="exp-icon">&#127807;</span><div class="exp-title">Retirees</div><p class="exp-body">Two appointments rather than a circuit, a long lunch with a view, and no early start. The walking is level in the town and the cellar steps are checked before we book them.</p><a href="/experiences/retirement-travel/" class="exp-cta">Retiree journeys</a></div>
        <div class="exp-card"><span class="exp-icon">&#129517;</span><div class="exp-title">Independent Travellers</div><p class="exp-body">You know what you drink and you have seen what a coach party does to a tasting room. We build the private version: the winemaker, the quiet hour, and the river road on the way home.</p><a href="/experiences/private-tours/" class="exp-cta">Private journeys</a></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Planning notes for Niagara-on-the-Lake">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">What to know <em>before you go</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">Getting there</h3><p>Fly to Toronto, and the region is about an hour and a half by road. Your guide and private vehicle collect you in the city, so the first vineyard view arrives before you have thought about the drive.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Best season</h3><p>Late September to mid October brings harvest, colour, and the quietest good weather of the year. May to October runs on long evenings and theatre. January is the region's other self, built on icewine.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The icewine window</h3><p>Icewine grapes are picked by hand at night when the temperature falls below minus eight. That can be December, January or February, and the growers decide on the day. We build a winter journey around a window rather than a date, and confirm the timing as it firms up.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Appointments</h3><p>Tasting rooms fill on weekends and through the harvest. The visit worth making is the appointment with a person rather than a pour, so we book two or three of those first and let the rest of the day fall around them.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The parkway and the falls</h3><p>The Niagara Parkway links the town to the falls in about twenty minutes. We drive it in the direction the light is best, take the falls early or late rather than at midday, and keep the route for the return trip when the day runs long.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Pacing and care</h3><p>A driver stays with you for the whole day, which is the point of doing this region privately. We recommend travel medical insurance for guests arriving from outside Canada and say so in writing, and the itinerary states the walking at every stop honestly.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we design this journey">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Appointments first, then the town</h2>
          <p>We book the cellar appointments before we plan anything else, because the visit that makes the day is the one with a person rather than a pour. From there the shape is simple: two visits, one long lunch, and the evening wherever the light is best. The town is a short walk at either end, and the falls are an easy decision once the cellar times are fixed.</p>
          <p>Harvest and festival dates move with the weather, so we check the current vintage and the growers' timing before every winter journey, and we keep a second appointment in reserve for any day the first one shifts. Everything here has been done first, in the cold as well as in the warm months: the cellar stairs, the table on the estate, and the river road in January.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/notl-guide.jpg" width="1400" height="800" alt="Driver and guide waiting outside a Niagara winery for private guests" loading="lazy">
          <figcaption>We drive, so nobody at the table has to count glasses.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Longer journeys">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">One region, one journey</div>
      <h2 class="section-title">Niagara-on-the-Lake is rarely <em>the only stop.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Most of our guests pair it with Prince Edward County for a lakeshore journey of seven to ten days, or run it as a single day at one end of a Rockies trip. See how a private Canada journey is built, then tell us what your version looks like.</p>
      <a class="btn" href="/experiences/private-tours/">How private journeys work</a>
    </div>
  </section>
""",
    cta_band=("/images/notl-hero.jpg",
              "Niagara-on-the-Lake private tour: a winery cellar tasting beside the winemaker in Ontario",
              "Ready to plan a wine journey?",
              "Tell us what you are imagining. We will come back within 24 hours.",
              "Begin Your Journey"),
    faq=[
        ("Do you drive between the wineries on a Niagara private tour?",
         "<p>Yes. A private vehicle and driver stay with you for the day, which is the whole point of doing this region privately: nobody at the table has to count glasses, and the schedule bends when a visit runs long.</p>"),
        ("When is icewine season in Niagara-on-the-Lake?",
         "<p>The harvest is in January, picked by hand at night when the temperature falls below minus eight. The festivals follow the harvest, so a winter journey here is built around that window and confirmed against the growers' timing.</p>"),
        ("How far is Niagara-on-the-Lake from Toronto?",
         "<p>About an hour and a half by road from the city, which makes it the easiest wine region in Canada to build into a journey, and the simplest day retreat for a corporate group.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_attraction(
        "Niagara-on-the-Lake, Ontario, Canada",
        "Private luxury wine tours of Niagara-on-the-Lake and the Niagara wine region, with cellar appointments, icewine in January, and a driver for the day.",
        "destinations/niagara-on-the-lake-private-tour/", 43.2537, -79.0709, "/images/notl-hero.jpg",
        ["Couples", "Retirees", "Independent travellers", "Corporate groups"])],
)

ALL = [HUB, TOFINO, SALTSPRING, JASPER, BANFF, PEC, NOTL]