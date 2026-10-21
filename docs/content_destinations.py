"""Destination content: the hub plus six destination pages.
One primary keyword per page, no keyword shared between pages.
"""

# ---------------------------------------------------------------- hub

HUB = dict(
    path="destinations/",
    title="Private Canada Tours | Destinations | Luxury Tours Canada",
    desc="Three regions for private Canada tours: the BC coast, the Rockies, and the Ontario lakeshore. Honest seasons, real drive times, eight guests maximum.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/")],
    og_image="/images/dest-clusters.svg",
    hero=dict(
        eyebrow="Three regions, four seasons",
        h1="Private Canada Tours: Three Regions That Deserve More Than a Week",
        sub="Canada is the second largest country on earth. We do not pretend to cover it in a fortnight. We build journeys in the three regions we know best, and we build them slowly.",
        img="/images/dest-hero.svg",
        alt="Private Canada tours: a quiet highway through the Canadian Rockies at first light",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <p>Every private Canada tour we design begins with a region, not a package. Most of our journeys run through one of three areas: the BC coast around Tofino and Salt Spring Island, the Canadian Rockies from Jasper down to Banff and Yoho, and the Ontario lakeshore from Kingston to Essex County.</p>
        <p>Each region has its own season, its own roads, and its own way of rewarding a slower pace. We state drive times honestly, plan around wildfire season rather than hoping, and hold a second option for every outdoor day, because mountain weather turns by the hour.</p>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Region one</div>
        <h2 class="section-title">The BC coast: Tofino and Salt Spring Island</h2>
        <p class="lede">Where the road ends at the Pacific. Storms you watch from a soaking tub, and an island that still runs on farm stands.</p>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-tofino.svg" width="600" height="400" alt="Private boat in Clayoquot Sound near Tofino, British Columbia" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Tofino, British Columbia</h3>
            <p>Outer Clayoquot Sound by private boat, Hot Springs Cove timed away from the tour boats, whale and bear watching with a naturalist, and a winter storm season almost nobody sees.</p>
            <a class="more" href="/destinations/tofino-private-tour/">Tofino private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-saltspring.svg" width="600" height="400" alt="Farm stand and vineyard on Salt Spring Island in the Gulf Islands, British Columbia" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Salt Spring Island, British Columbia</h3>
            <p>The largest of the Gulf Islands, reached by floatplane from Vancouver. Farm tables, a Saturday market, Mount Maxwell, and warm-lake swimming in summer.</p>
            <a class="more" href="/destinations/salt-spring-island-private-tour/">Salt Spring Island private tour</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Region two</div>
        <h2 class="section-title">The Rockies: Jasper, Banff, and Yoho</h2>
        <p class="lede">Jasper first. Dark skies, empty switchbacks, and a glacier you can walk to before breakfast.</p>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-jasper.svg" width="600" height="400" alt="Maligne Lake in Jasper National Park at dawn on a private Jasper tour" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Jasper, Alberta</h3>
            <p>Larger and quieter than Banff, under one of the largest dark-sky preserves on earth. Maligne Lake at the quiet hours, the Athabasca Glacier, and wildlife viewed at distance, always guide-led.</p>
            <a class="more" href="/destinations/jasper-private-tour/">Jasper private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-banff.svg" width="600" height="400" alt="Icefields Parkway private tour between Lake Louise and Jasper in the Canadian Rockies" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Banff and Yoho, Alberta and BC</h3>
            <p>Banff and Lake Louise at dawn, in shoulder season, or by routes that bypass the queues. Emerald Lake and Takakkaw Falls, the quieter neighbours, and 232 kilometres of the Icefields Parkway.</p>
            <a class="more" href="/destinations/banff-yoho-private-tour/">Banff and Yoho private tour</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">Region three</div>
          <h2 class="section-title">The Ontario lakeshore: Kingston to Essex</h2>
          <blockquote>Limestone towns, wine on the water, and the southernmost point in Canada. The road we know best, by bicycle.</blockquote>
          <p class="small" style="margin-top:14px">Almost no operator sells southern Ontario as a journey, which is exactly why it belongs in ours. The whole length of it has been ridden, not driven.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/dest-lakeshore.svg" width="1400" height="800" alt="Lakeside vineyards on the Ontario lakeshore near Prince Edward County" loading="lazy">
          <figcaption>Wine harvest runs late September into October.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Lakeshore destinations</div>
        <h2 class="section-title">Wine, history, and migrating birds</h2>
      </div>
      <div class="grid g-3">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-pec.svg" width="600" height="400" alt="Sandbanks dunes and vineyard rows in Prince Edward County, Ontario" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Prince Edward County</h3>
            <p>Wine, farm tables, and the Sandbanks dunes, an hour and a half from the heritage waterfront at Kingston.</p>
            <a class="more" href="/destinations/prince-edward-county-private-tour/">Prince Edward County private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-notl.svg" width="600" height="400" alt="Winery visit with the winemaker in Niagara-on-the-Lake, Ontario" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Niagara-on-the-Lake</h3>
            <p>Winery visits with the winemaker, and icewine in January, when the harvest happens on the coldest nights of the year.</p>
            <a class="more" href="/destinations/niagara-on-the-lake-private-tour/">Niagara-on-the-Lake private tour</a>
          </div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/dest-pelee.svg" width="600" height="400" alt="Monarch butterflies at Point Pelee National Park, the southernmost point of mainland Canada" loading="lazy"></figure>
          <div class="body">
            <h3 class="card-title">Point Pelee and Essex County</h3>
            <p>The southernmost point of mainland Canada: spring bird migration in May, monarchs in September, and Lake Erie wine country.</p>
            <a class="more" href="/experiences/private-tours/">Ask us to add it</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Practical</div>
        <h2 class="section-title">When to go, at a glance</h2>
      </div>
      <div class="prose">
        <p>Canadian travel is planned ahead of its season, and the seasons run opposite to the tropics. Peak planning for a summer Rockies journey happens between January and March. Autumn trips are booked in summer, and winter journeys, including storm season on the Pacific and aurora in the mountains, are planned through autumn.</p>
        <ul class="ticks">
          <li><strong>Summer, late June to mid September.</strong> Lakes thawed, mountain roads open, long light. Book early, this is the busiest window in the Rockies.</li>
          <li><strong>Autumn, mid September to early October.</strong> Golden larches in the Rockies, wine harvest on the lakeshore, and thinner crowds.</li>
          <li><strong>Winter, November to March.</strong> Pacific storm season, icewine in Niagara, frozen lakes and aurora in Jasper. Expect minus 15 to minus 25 Celsius in the mountains.</li>
          <li><strong>Shoulder, May to June.</strong> Grey whales along the BC coast and quiet roads almost everywhere.</li>
        </ul>
        <p class="small">April to May in the Rockies: snowmelt, mud, and closures. We rarely build there, and we will tell you plainly if your dates land in it.</p>
      </div>
    </div>
  </section>
""",
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
    og_image="/images/tofino-hero.svg",
    hero=dict(
        eyebrow="British Columbia, Pacific coast",
        h1="Tofino Private Tour: Where the Road Ends at the Pacific",
        sub="Storms you watch from a soaking tub, an old-growth island, and the outer waters of Clayoquot Sound reached by private boat while the beach car park fills up behind you.",
        img="/images/tofino-hero.svg",
        alt="Tofino private tour: a private boat on the outer waters of Clayoquot Sound at first light",
        cta="Plan My Tofino Journey",
    ),
    best_for=["Couples", "Retirees", "Independent travellers", "Families with children over 6"],
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <h2>Why Tofino for private travel</h2>
        <p>Tofino has been discovered, and in July and August the main beaches know it. So we do not build summer journeys around Chesterman Beach at midday. We build them around the hours and the waters that stay quiet: dawn, the shoulder seasons, and the outer reaches of Clayoquot Sound, reached by private boat with a naturalist who knows where the whales have been feeding that week.</p>
        <p>What Tofino does best is found in May and June, from September into October, and through the winter, when the Pacific puts on a show and almost nobody is there to see it. The road in from Nanaimo takes roughly three and a half to four hours, and it is one of the finest drives on the coast. A floatplane is the other way in, so the journey can begin above the water.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/tofino-landscape.svg" width="1400" height="800" alt="Clayoquot Sound private boat tour passing a forested island on the Tofino coast" loading="lazy">
        <figcaption>Chesterman Beach before eight, when the sand still belongs to the shorebirds.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What we build into a Tofino journey</h2>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/tofino-hotsprings.svg" width="600" height="400" alt="Hot Springs Cove near Tofino reached by private water taxi" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Hot Springs Cove by private boat</h3><p>A private water taxi out to the springs, timed so the soak happens after the tour boats have gone. Boardwalk, steam, and the open Pacific beyond.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/tofino-clayoquot.svg" width="600" height="400" alt="Whale watching from a private boat in Clayoquot Sound near Tofino" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Clayoquot Sound by private boat</h3><p>Whales, sea lions, and black bears turning rocks on the low tide line, with a naturalist guide and a vessel that goes where the larger boats cannot.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/tofino-meares.svg" width="600" height="400" alt="Old-growth forest walk on Meares Island near Tofino with a guide" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Meares Island old growth</h3><p>A guided walk among cedars older than most countries, on an island that was protected by the people who live here. Mud boots provided, pace set by the forest.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/tofino-storm.svg" width="600" height="400" alt="Winter storm watching on the Pacific Rim coast near Tofino" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Winter storm watching</h3><p>From November to February the swell arrives in sets you can hear from the lodge. We book the room with the window, and the soaking tub, for exactly this.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">The place in pictures</div>
        <h2 class="section-title">The coast at its quietest</h2>
      </div>
      <div class="grid g-2">
        <figure class="shot shot-mosaic"><img src="/images/tofino-mosaic-1.svg" width="800" height="1000" alt="Rainforest trail above the beach near Tofino" loading="lazy"></figure>
        <div class="grid">
          <figure class="shot shot-card"><img src="/images/tofino-mosaic-2.svg" width="600" height="400" alt="Floatplane arriving at Tofino harbour on the west coast of Vancouver Island" loading="lazy"></figure>
          <figure class="shot shot-card"><img src="/images/tofino-mosaic-3.svg" width="600" height="400" alt="Fishing boats at anchor in Tofino harbour at dusk" loading="lazy"></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">When to visit</div>
        <h2 class="section-title">Seasons on the west coast</h2>
      </div>
      <div class="prose">
        <p>May and June bring grey whales, long evenings, and empty beaches. September and October bring the clearest light of the year and the whale watching most people miss. November to February is storm season, which is a reason to go, not a reason to stay away, provided the room has the view and the fire. July and August are the busy months, workable only with dawn starts and a boat in the outer waters.</p>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><div class="lab">Summer</div><p>Long light and warm sand, at its best before nine in the morning. Book early, and let us take you out of the crowd by boat.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Autumn</div><p>Clear air, active whales, and few people. Our favourite window on this coast, and the one we recommend first for couples.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Winter</div><p>Storm watching, fireplaces, and the Pacific at full volume. Dress for rain and you will love it.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For couples</div>
        <p>The room with the window, the tub, and nothing on the schedule until lunch. Winter storm season is the most romantic thing this coast does, and it is the easiest season to be alone in.</p>
      </div>
      <div class="callout">
        <div class="lab">For families</div>
        <p>Pacific water is cold year round. Wetsuits for any swimming, and a guide on every beach day, because surf beaches carry rip currents. Boat and floatplane days are weather dependent, so every itinerary keeps a fallback day. Families with children over six do best here.</p>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Timed to the water, not the brochure</h2>
          <p>We build the boat days first, because the water decides everything else, and then shape the land days around the weather window. Your guide checks the marine forecast the evening before, and the fallback day is already written before you fly.</p>
          <p>Everything in the plan has been done here first: the soak at Hot Springs Cove after the boats leave, the walk on Meares Island at the hour the light comes through the canopy, the table at the end of the day where the fishing boats are still coming in.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/tofino-guide.svg" width="1400" height="800" alt="Private guide scanning the water for whales on a Tofino boat day" loading="lazy">
          <figcaption>Wildlife is viewed at distance, guide-led, always.</figcaption>
        </figure>
      </div>
    </div>
  </section>
""",
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
        "destinations/tofino-private-tour/", 49.1530, -125.7671, "/images/tofino-hero.svg",
        ["Couples", "Retirees", "Independent travellers", "Families"])],
)

# ---------------------------------------------------------------- Salt Spring

SALTSPRING = dict(
    path="destinations/salt-spring-island-private-tour/",
    title="Salt Spring Island Private Tour | Luxury Tours Canada",
    desc="A Salt Spring Island private tour at an unhurried pace: farm tables, the Ganges market, Mount Maxwell, and floatplane transfers from Vancouver.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Salt Spring Island", "/destinations/salt-spring-island-private-tour/")],
    og_image="/images/saltspring-hero.svg",
    hero=dict(
        eyebrow="British Columbia, Gulf Islands",
        h1="Salt Spring Island Private Tour: The Island That Still Runs on Farm Stands",
        sub="The largest of the Gulf Islands, thirty five minutes by floatplane from Vancouver, and a life measured in market mornings, orchard walks, and the view from Mount Maxwell.",
        img="/images/saltspring-hero.svg",
        alt="Salt Spring Island private tour: a farm stand and orchard on the Gulf Islands waterfront",
        cta="Plan My Salt Spring Journey",
    ),
    best_for=["Retirees", "Couples", "Independent travellers"],
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <h2>Why Salt Spring for private travel</h2>
        <p>Salt Spring is the counterweight to everything busy about the west coast. It is agricultural, quiet, and short of distances: the whole island is small enough to see properly in three days, at a pace that suits a journey where nobody wants to be rushed. Cheese, cider, lamb, lavender, and a Saturday market that has been running on the Ganges waterfront for decades.</p>
        <p>You arrive by floatplane from Vancouver, or by ferry with the vehicle on deck, and the island does the rest. Drives run fifteen minutes, not three hours. Our retirees tell us this is the leg where they finally exhale, and our couples book it for the same reason.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/saltspring-landscape.svg" width="1400" height="800" alt="Salt Spring Island farm and vineyard view over the southern Gulf Islands" loading="lazy">
        <figcaption>Mount Maxwell, late afternoon, looking south over the Gulf Islands.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">Three days, done slowly</h2>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/saltspring-ganges.svg" width="600" height="400" alt="The Saturday market at Ganges on Salt Spring Island" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">The Ganges market</h3><p>Cheese, sourdough, and a jam stall that has been in the same hands for twenty years. A flat kilometre of walking, benches every hundred metres, and nothing you have to buy.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/saltspring-maxwell.svg" width="600" height="400" alt="Mount Maxwell viewpoint on Salt Spring Island with folding chairs set up" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Mount Maxwell lookouts</h3><p>A short walk over firm ground to a view across the southern Gulf Islands and out to the Pacific. Our guide carries the folding chairs.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/saltspring-farm.svg" width="600" height="400" alt="Farm table lunch on Salt Spring Island with food grown in sight of the plates" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Farm tables and tastings</h3><p>Lunch where the food was grown in sight of the plates, then a dairy or cidery visit on the way back. Producers who sell to the island first and visitors second.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/saltspring-cusheon.svg" width="600" height="400" alt="Cusheon Lake on Salt Spring Island, warm enough for swimming in summer" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Cusheon Lake in summer</h3><p>The ocean here is cold; this lake is not. A warm-water swim in summer, with a dock, a picnic, and a book, is the whole afternoon.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="grid g-2">
        <figure class="shot shot-mosaic"><img src="/images/saltspring-mosaic-1.svg" width="800" height="1000" alt="Orchard walk on Salt Spring Island in autumn" loading="lazy"></figure>
        <div class="grid">
          <figure class="shot shot-card"><img src="/images/saltspring-mosaic-2.svg" width="600" height="400" alt="Floatplane landing on the water near Salt Spring Island" loading="lazy"></figure>
          <figure class="shot shot-card"><img src="/images/saltspring-mosaic-3.svg" width="600" height="400" alt="Farm gate and pasture on Salt Spring Island" loading="lazy"></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">When to visit</div>
        <h2 class="section-title">Best from May to October</h2>
      </div>
      <div class="prose">
        <p>The Saturday market runs roughly April to October, which sets the shape of an island journey. Late spring brings the orchards into leaf, summer brings lake swimming and long light, and September and October bring the harvest and the smell of cider. Winter is quiet to the point of empty, and we build it only for guests who want exactly that.</p>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><div class="lab">Summer</div><p>Warm lake swims, the market at its fullest, and long evenings on the water.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Autumn</div><p>Harvest, cider, and empty roads. Our pick for couples.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Winter</div><p>Grey herons, closed stalls, and the island to yourself.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For retirees</div>
        <p>Flat ground, short drives, and no departure before half past eight. The market walk is about a kilometre on firm surfaces, the viewpoint walk is under three hundred metres with a bench at the top, and the afternoon is yours. The nearest hospital is on the island, minutes from the harbour, and we note it in every itinerary.</p>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Built around a market morning</h2>
          <p>Island time is the point, so we anchor the stay on the Saturday market and build the rest of the days around it. One base, one vehicle, the same guide throughout, and no day that starts before you have had breakfast.</p>
          <p>Salt Spring pairs naturally with Tofino for a coast journey of seven to ten days, and with the Rockies for a signature shape that crosses the country from the Pacific to the peaks.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/saltspring-guide.svg" width="1400" height="800" alt="Guide and guests walking a farm road on Salt Spring Island" loading="lazy">
          <figcaption>A kilometre of market walk, and a bench every hundred metres.</figcaption>
        </figure>
      </div>
    </div>
  </section>
""",
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
        "destinations/salt-spring-island-private-tour/", 48.8567, -123.4983, "/images/saltspring-hero.svg",
        ["Retirees", "Couples", "Independent travellers"])],
)

# ---------------------------------------------------------------- Jasper

JASPER = dict(
    path="destinations/jasper-private-tour/",
    title="Jasper Private Tour | Luxury Canadian Rockies Journeys",
    desc="A Jasper private tour built around dark skies, quiet lakes, the Athabasca Glacier, and the Icefields Parkway, with wildlife at distance. Maximum eight guests.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Jasper", "/destinations/jasper-private-tour/")],
    og_image="/images/jasper-hero.svg",
    hero=dict(
        eyebrow="Alberta, Canadian Rockies",
        h1="Jasper Private Tour: Dark Skies and Empty Switchbacks",
        sub="Larger, quieter, and darker than anywhere else in the Rockies. A glacier you can walk to before breakfast, elk on the roadside at dusk, and a night sky with nothing between you and it.",
        img="/images/jasper-hero.svg",
        alt="Jasper private tour: Maligne Lake and the Canadian Rockies under a dark sky at dusk",
        cta="Plan My Jasper Journey",
    ),
    best_for=["Independent travellers", "Couples", "Retirees", "Families with children over 8"],
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <h2>Why Jasper for private travel</h2>
        <p>Jasper is the Rockies before the crowds found them. It is larger than Banff, quieter in every season, and it holds one of the largest dark-sky preserves in the world, which means a sky you will remember more than any photograph. The town is small, the wildlife is close to the road but never approached, and the pace of a day here is set by light rather than by a coach timetable.</p>
        <p>We lead with Jasper and work outward: the Icefields Parkway south to Lake Louise, Yoho beyond it, and Banff only in the quiet hours. Some trails and services in the park were affected by the 2024 wildfire, so we confirm the current status of every road and walk with Parks Canada before we build, and we say plainly what is open.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/jasper-landscape.svg" width="1400" height="800" alt="Icefields Parkway private tour looking south toward the Columbia Icefield in the Canadian Rockies" loading="lazy">
        <figcaption>Fill the tank at Jasper or Lake Louise. The parkway runs 232 kilometres with very few services.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What a Jasper journey holds</h2>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/jasper-maligne.svg" width="600" height="400" alt="Maligne Lake in Jasper National Park at the quiet hour before day visitors arrive" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Maligne Lake at the quiet hours</h3><p>Maligne and Medicine Lake with a guide who knows when the day visitors come and go. A canoe on still water is the way to do it, not a seat on a cruise.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/jasper-darksky.svg" width="600" height="400" alt="Dark sky viewing in the Jasper Dark Sky Preserve with a guide" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Jasper Dark Sky Preserve</h3><p>An evening with a guide who knows where to stand, when the moon is out of the way, and which lake reflects the Milky Way best that week.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/jasper-glacier.svg" width="600" height="400" alt="Guided walk toward the Athabasca Glacier on the Icefields Parkway" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">The Athabasca Glacier</h3><p>A guided walk toward the ice on the Icefields Parkway, with the scale of the Columbia Icefield in front of you the whole way.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/jasper-wildlife.svg" width="600" height="400" alt="Elk beside the road near Jasper, viewed at distance with a guide" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Wildlife, at distance</h3><p>Elk, bighorn sheep, black bears, and if you are lucky a grizzly on a distant slope. Viewed from the vehicle or a marked viewpoint, guide-led, always.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="grid g-2">
        <figure class="shot shot-mosaic"><img src="/images/jasper-mosaic-1.svg" width="800" height="1000" alt="Canoe on a still Rockies lake in Jasper National Park" loading="lazy"></figure>
        <div class="grid">
          <figure class="shot shot-card"><img src="/images/jasper-mosaic-2.svg" width="600" height="400" alt="Mountain lodge in Jasper at dusk with the peaks behind" loading="lazy"></figure>
          <figure class="shot shot-card"><img src="/images/jasper-mosaic-3.svg" width="600" height="400" alt="Elk grazing on a Jasper roadside meadow in autumn" loading="lazy"></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">When to visit</div>
        <h2 class="section-title">Long light, golden larches, and real cold</h2>
      </div>
      <div class="prose">
        <p>Late June to mid September is the classic window: lakes thawed, roads open, daylight until late. Mid September to early October is the connoisseur's window, when the larches turn gold and the crowds thin out. Winter, December to March, brings skiing, frozen lakes, and aurora, with temperatures between minus fifteen and minus twenty five. April and May are for mud, snowmelt, and closures, and we rarely build there.</p>
        <p>Lake Louise sits at about 1,600 metres, so we build a gentle first day at altitude for every guest, and state the climb honestly in the itinerary.</p>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><div class="lab">Summer</div><p>Long light and open roads. Book early, this is the Rockies at their busiest.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Autumn</div><p>Golden larches, elk in rut, and thin crowds. Our preferred window for a Rockies journey.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Winter</div><p>Frozen lakes, dark skies, and aurora. Dress for minus twenty and the valley is yours.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For families</div>
        <p>Children over eight do best here. Canoeing replaces swimming, because glacial lakes are far too cold for a dip, and every walk starts with a wildlife briefing. Car seats are required by law and are pre-sourced for every vehicle on the parkway.</p>
      </div>
      <div class="callout">
        <div class="lab">For retirees</div>
        <p>The Icefields Parkway by private vehicle, with short walks and long views. No departure before half past eight, an afternoon rest built in, and a late-afternoon wildlife outing in place of a dawn start. Travel medical insurance is essential in this country, and we say so in writing.</p>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Driven many times, not mapped once</h2>
          <p>The Icefields Parkway is among the great drives on the planet and one of the least forgiving if you have not done it: 232 kilometres between Lake Louise and Jasper with very few services. We drive it slowly, with a guide who has done it many times, and we plan the wildlife stops around light rather than around a schedule.</p>
          <p>Where a wildfire or a weather system changes the plan, the fallback is already written: a different valley at the same hour, and a second location for any evening we have promised on the water or the ice.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/jasper-guide.svg" width="1400" height="800" alt="Private guide pointing out a distant grizzly from a safe distance in Jasper" loading="lazy">
          <figcaption>The reaction to a first bear sighting tells us everything about a traveller.</figcaption>
        </figure>
      </div>
    </div>
  </section>
""",
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
        "destinations/jasper-private-tour/", 52.8737, -118.0814, "/images/jasper-hero.svg",
        ["Independent travellers", "Couples", "Retirees", "Families"])],
)

# ---------------------------------------------------------------- Banff and Yoho

BANFF = dict(
    path="destinations/banff-yoho-private-tour/",
    title="Icefields Parkway Private Tour | Banff and Yoho | Canada",
    desc="An Icefields Parkway private tour with Banff and Yoho in the quiet hours: Lake Louise at sunrise, Emerald Lake, and Takakkaw Falls. Private guide throughout.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Banff and Yoho", "/destinations/banff-yoho-private-tour/")],
    og_image="/images/banff-hero.svg",
    hero=dict(
        eyebrow="Alberta and British Columbia",
        h1="Icefields Parkway Private Tour: Banff and Yoho in the Quiet Hours",
        sub="The lake at sunrise, before the day visitors arrive. A quieter valley next door. And 232 kilometres of parkway between two mountain towns, driven slowly.",
        img="/images/banff-hero.svg",
        alt="Icefields Parkway private tour: Lake Louise at sunrise with the Victoria Glacier behind",
        cta="Plan My Rockies Journey",
    ),
    best_for=["Independent travellers", "Couples", "Retirees", "Families with children over 8", "Corporate groups"],
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <h2>Why Banff and Yoho, done this way</h2>
        <p>Banff and Lake Louise are the most photographed places in Canada, and in July they feel like it. We do not refuse them. We take guests at dawn, in shoulder season, or by routes that bypass the queues, and we treat them as a chapter inside a Rockies journey rather than the whole book. The reward is the lake at sunrise with the mist still on it, and a car park with three vehicles in it instead of three hundred.</p>
        <p>Yoho National Park is the quieter neighbour, thirty minutes away, with Emerald Lake and Takakkaw Falls. Road and parking rules around Lake Louise and Moraine Lake have changed in recent years, so we confirm access before every journey and build the day around the current system rather than last year's instructions.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/banff-landscape.svg" width="1400" height="800" alt="Banff luxury tour: the Bow Valley and the Icefields Parkway seen from a quiet viewpoint" loading="lazy">
        <figcaption>Lake Louise, twenty minutes after sunrise, when the day visitors are still in bed.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">The parkway and the quiet valleys</h2>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/banff-lakelouise.svg" width="600" height="400" alt="Lake Louise at sunrise on a private Banff tour before the day visitors arrive" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Lake Louise at sunrise</h3><p>We leave before eight, take the walk along the shore, and are drinking coffee while the first coaches pull in behind us.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/banff-icefields.svg" width="600" height="400" alt="Icefields Parkway private tour vehicle stopped at a glacier viewpoint" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Icefields Parkway by private vehicle</h3><p>232 kilometres of glacier, waterfall, and empty switchback between Lake Louise and Jasper, at your pace, with the fuel and food stops planned honestly.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/banff-yoho.svg" width="600" height="400" alt="Emerald Lake in Yoho National Park on a private Rockies journey" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Yoho: Emerald Lake and Takakkaw Falls</h3><p>The neighbour Banff forgets. Emerald Lake for an easy walk and a canoe, Takakkaw Falls for a short stroll to the base of the water.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/banff-canoe.svg" width="600" height="400" alt="Canoeing on a glacial lake in the Canadian Rockies with a guide" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">A canoe instead of a swim</h3><p>Glacial lakes are far too cold to swim, so the water activity is a canoe, with a guide, on a lake that photographs badly and feels extraordinary.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="grid g-2">
        <figure class="shot shot-mosaic"><img src="/images/banff-mosaic-1.svg" width="800" height="1000" alt="Yoho National Park waterfall beside the road on a private Rockies tour" loading="lazy"></figure>
        <div class="grid">
          <figure class="shot shot-card"><img src="/images/banff-mosaic-2.svg" width="600" height="400" alt="Mountain lodge fireplace in Banff after a day on the parkway" loading="lazy"></figure>
          <figure class="shot shot-card"><img src="/images/banff-mosaic-3.svg" width="600" height="400" alt="Bighorn sheep on the roadside in the Canadian Rockies, viewed at distance" loading="lazy"></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">When to visit</div>
        <h2 class="section-title">Shoulder season is the secret</h2>
      </div>
      <div class="prose">
        <p>Mid September to early October is when this region is at its best for private travel: golden larches, elk in the valley, and room at every viewpoint. Late June to mid September is the classic window with everything open. Winter, December to March, brings skiing and frozen lakes, and the access rules for Lake Louise and Moraine Lake change with the season, so we confirm them before we build.</p>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><div class="lab">Summer</div><p>Everything open, everything busy. We work the early hours and the quiet valleys.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Autumn</div><p>Larches, elk, and space at the viewpoints. Our recommendation for this region.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Winter</div><p>Skiing, ice walks, and frozen lakes, with far fewer people on the parkway.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For corporate groups</div>
        <p>Banff and Lake Louise handle larger groups well, and Calgary is the gateway, ninety minutes from the park gate. Retreats of six to thirty stay here comfortably, with a fallback venue for every programme day. For the retreat structure, see our corporate journeys page.</p>
      </div>
      <div class="callout">
        <div class="lab">For families</div>
        <p>Children over eight get the most from this region. Wildlife briefings before every walk, car seats pre-sourced for the parkway, and canoeing rather than swimming, because the water is glacial.</p>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Access rules checked before every journey</h2>
          <p>Lake Louise and Moraine Lake access has changed materially in recent years, and so has the status of some trails after the 2024 wildfire season. We check the current rules with Parks Canada before we quote, and we design the day around them rather than around habit.</p>
          <p>The result is a region that feels private even in August: the lake at dawn, the quieter valley after lunch, and the parkway at the hours when the coaches are somewhere else.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/banff-guide.svg" width="1400" height="800" alt="Guide setting up a sunrise viewpoint above Lake Louise for private guests" loading="lazy">
          <figcaption>Coffee at the lake, twenty minutes after sunrise.</figcaption>
        </figure>
      </div>
    </div>
  </section>
""",
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
        "destinations/banff-yoho-private-tour/", 51.1784, -115.5708, "/images/banff-hero.svg",
        ["Independent travellers", "Couples", "Retirees", "Families", "Corporate groups"])],
)

# ---------------------------------------------------------------- Prince Edward County

PEC = dict(
    path="destinations/prince-edward-county-private-tour/",
    title="Prince Edward County Private Tour | Ontario Wine Country",
    desc="A Prince Edward County private tour with wine, farm tables, and the Sandbanks dunes, plus a private Thousand Islands cruise from Kingston. Flat, unhurried days.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Prince Edward County", "/destinations/prince-edward-county-private-tour/")],
    og_image="/images/pec-hero.svg",
    hero=dict(
        eyebrow="Ontario, Lake Ontario and Lake Erie",
        h1="Prince Edward County Private Tour: Wine, Farm Tables, and Sandbanks Dunes",
        sub="Limestone towns, vineyards a bicycle ride apart, and a county where the food is grown within sight of the table. The road we know best, ridden end to end.",
        img="/images/pec-hero.svg",
        alt="Prince Edward County private tour: a vineyard row and farm table in Ontario wine country",
        cta="Plan My Lakeshore Journey",
    ),
    best_for=["Retirees", "Couples", "Independent travellers", "Corporate groups"],
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <h2>Why Prince Edward County for private travel</h2>
        <p>Almost no luxury operator sells southern Ontario as a journey, which is exactly why it belongs in ours. The county sits an hour and a half east of the heritage waterfront at Kingston, and it holds Canada's youngest serious wine region, farm tables that fill up on a Friday, and the Sandbanks dunes, where the lake behaves like a coast.</p>
        <p>The whole lakeshore from Kingston to Essex County has been ridden on a bicycle rather than driven past, and that changes what we recommend: the vineyard with the winemaker still pouring, the county road with the view, and the day built so nobody spends it in a car.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/pec-landscape.svg" width="1400" height="800" alt="Vineyard and farm table overlooking Lake Ontario in Prince Edward County" loading="lazy">
        <figcaption>Sandbanks dunes, late afternoon, when the day visitors have gone home.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">Wine, water, history, and a bicycle</h2>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/pec-kingston.svg" width="600" height="400" alt="Limestone waterfront at Kingston, Ontario, with a private Thousand Islands cruise departing" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Kingston and the Thousand Islands</h3><p>The limestone waterfront, the old market square, and a private cruise out among islands with a story on every one. Toronto is the gateway.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/pec-wine.svg" width="600" height="400" alt="Winery visit with the winemaker in Prince Edward County wine country" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Wineries with the winemaker</h3><p>Not a tasting room queue. We book the visit where the person who made the wine talks you through it, in a county small enough that they still can.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/pec-dunes.svg" width="600" height="400" alt="Sandbanks dunes in Prince Edward County beside Lake Ontario" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Sandbanks dunes</h3><p>A provincial park where the lake runs clear and shallow for a hundred metres, warm enough to swim by August, with dunes behind it.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/pec-bike.svg" width="600" height="400" alt="Guests on electric bicycles beside the guide on the Waterfront Trail in Ontario" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">The Waterfront Trail by electric bicycle</h3><p>Flat, quiet, and exactly the right speed for this shoreline. Your guide rides beside you, and the vineyard stops are all within reach.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="grid g-2">
        <figure class="shot shot-mosaic"><img src="/images/pec-mosaic-1.svg" width="800" height="1000" alt="Heritage limestone building in Kingston, Ontario, on a private lakeshore tour" loading="lazy"></figure>
        <div class="grid">
          <figure class="shot shot-card"><img src="/images/pec-mosaic-2.svg" width="600" height="400" alt="Farm table lunch in Prince Edward County with regional produce" loading="lazy"></figure>
          <figure class="shot shot-card"><img src="/images/pec-mosaic-3.svg" width="600" height="400" alt="Monarch butterflies resting in Point Pelee National Park in autumn" loading="lazy"></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">When to visit</div>
        <h2 class="section-title">May to October, with harvest in the middle</h2>
      </div>
      <div class="prose">
        <p>May starts the season with the vineyards in leaf and the lake still cold. September and October are the best months, with the wine harvest and the autumn colour arriving within a fortnight of each other. January brings icewine in Niagara, which pairs naturally with this region for a winter journey. Point Pelee, the southernmost point of mainland Canada, is a May destination for migrating birds and a September one for monarchs, and the Pelee Island ferry is seasonal, so we check the timetable before building a day around it.</p>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><div class="lab">Summer</div><p>Lake swimming at the dunes, long vineyard evenings, and the county at its fullest.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Autumn</div><p>Harvest and colour in the same fortnight. The best time to be here.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Winter</div><p>Icewine in Niagara, quiet county roads, and fires in heritage inns.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For retirees</div>
        <p>Flat terrain, short drives, and the strongest cultural content in our portfolio: history in Kingston, wine and food in the county, and a lakeshore that can be seen properly without a long day in the vehicle. No departure before half past eight, and an afternoon rest built into every day.</p>
      </div>
      <div class="callout">
        <div class="lab">For couples</div>
        <p>This is the leg where we plan the long lunch and leave the evening open. Prince Edward County works for couples who want wine, water, and a table that is theirs rather than a tasting bar.</p>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">A lakeshore built for short drives</h2>
          <p>Ontario looks flat on a map and is anything but on a schedule, so we cluster the days: Kingston and the islands, then the county, then Niagara if the journey asks for it. Nobody spends three hours in the vehicle to reach a vineyard.</p>
          <p>The whole road from Kingston to Essex has been ridden end to end, which is why we can tell you which town deserves two nights, which winery is worth an appointment, and which viewpoint is a photograph rather than an experience.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/pec-guide.svg" width="1400" height="800" alt="Guide and guests on bicycles beside the Waterfront Trail in Ontario" loading="lazy">
          <figcaption>Flat, quiet, and exactly the right speed for this shoreline.</figcaption>
        </figure>
      </div>
    </div>
  </section>
""",
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
        "destinations/prince-edward-county-private-tour/", 44.0043, -77.1481, "/images/pec-hero.svg",
        ["Retirees", "Couples", "Independent travellers", "Corporate groups"])],
)

# ---------------------------------------------------------------- Niagara-on-the-Lake

NOTL = dict(
    path="destinations/niagara-on-the-lake-private-tour/",
    title="Niagara-on-the-Lake Private Tour | Ontario Wine Journeys",
    desc="A Niagara-on-the-Lake private tour with cellar visits beside the winemaker, icewine in January, the heritage town, and a private driver for the day.",
    crumb=[("Home", "/"), ("Destinations", "/destinations/"), ("Niagara-on-the-Lake", "/destinations/niagara-on-the-lake-private-tour/")],
    og_image="/images/notl-hero.svg",
    hero=dict(
        eyebrow="Ontario, Niagara wine country",
        h1="Niagara-on-the-Lake Private Tour: Winery Visits with the Winemaker",
        sub="Canada's oldest wine region, an hour from Toronto, with cellars that will open a private tasting for the right appointment and icewine harvested on the coldest nights of January.",
        img="/images/notl-hero.svg",
        alt="Niagara-on-the-Lake private tour: a winery cellar tasting beside the winemaker in Ontario",
        cta="Plan My Wine Journey",
    ),
    best_for=["Couples", "Retirees", "Independent travellers", "Corporate groups"],
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <h2>Why Niagara-on-the-Lake for private travel</h2>
        <p>This is the oldest wine region in the country, and it behaves like a European appellation: a heritage town at the mouth of the Niagara River, cellars with real age on them, and a winter harvest that exists nowhere else in Canada. Icewine is picked at night, by hand, at temperatures below minus eight, and if your journey is in January you can be there for it.</p>
        <p>The difference a private tour makes here is appointments. We book the visits where the person who made the wine takes you through it, at the times the tasting rooms are quiet, and we drive, so nobody at the table has to count glasses.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/notl-landscape.svg" width="1400" height="800" alt="Luxury Ontario wine tour: vineyard rows above the Niagara River in autumn" loading="lazy">
        <figcaption>Icewine is picked by hand at night, below minus eight degrees.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">A wine day with a driver, and a winter one to remember</h2>
      </div>
      <div class="grid g-2">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/notl-cellar.svg" width="600" height="400" alt="Private cellar tasting with a winemaker in Niagara-on-the-Lake" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Cellar appointments</h3><p>Two or three visits rather than five, chosen for what you actually drink, each with the winemaker or the cellar master rather than a host reading a card.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/notl-icewine.svg" width="600" height="400" alt="Icewine harvest at night in the Niagara wine region of Ontario" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Icewine in January</h3><p>The harvest happens when the temperature allows, often at three in the morning. We plan a winter journey around that window and the festivals that follow it.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/notl-town.svg" width="600" height="400" alt="Heritage main street of Niagara-on-the-Lake, Ontario" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">The heritage town</h3><p>A main street built for walking, with a theatre season, good coffee, and the river two blocks behind it. Toronto is an hour away.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/notl-dinner.svg" width="600" height="400" alt="Private dinner table at a Niagara winery restaurant" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">A table at the winery</h3><p>Dinner on the estate where the wine was made, then the drive back handled, so the evening can run as long as it wants to.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="grid g-2">
        <figure class="shot shot-mosaic"><img src="/images/notl-mosaic-1.svg" width="800" height="1000" alt="Niagara River and vineyard in winter on a private Ontario wine journey" loading="lazy"></figure>
        <div class="grid">
          <figure class="shot shot-card"><img src="/images/notl-mosaic-2.svg" width="600" height="400" alt="Wine barrels in a Niagara cellar" loading="lazy"></figure>
          <figure class="shot shot-card"><img src="/images/notl-mosaic-3.svg" width="600" height="400" alt="Heritage houses on a Niagara-on-the-Lake street" loading="lazy"></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">When to visit</div>
        <h2 class="section-title">Two seasons, two different journeys</h2>
      </div>
      <div class="prose">
        <p>From May to October the region runs on warm evenings, vineyard walks, and theatre. January is its other self: icewine harvest, festival weekends, and cellars that feel like the right place to be in the cold. Between the two, late September and early October bring the harvest and the autumn colour, which is the quietest good weather of the year.</p>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><div class="lab">Summer</div><p>Vineyard walks, long dinners, and the river at its best. Book the good tables early.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Autumn</div><p>Harvest, colour, and space. The connoisseur's window for a wine journey.</p></div></div>
        <div class="card"><div class="body"><div class="lab">Winter</div><p>Icewine, festivals, and cellars. The only place in Canada to be in January.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="callout">
        <div class="lab">For couples</div>
        <p>A wine day, a long lunch, and an evening on the estate. Niagara-on-the-Lake is where we build the simplest romantic day in the portfolio, and the one guests most often ask to repeat.</p>
      </div>
      <div class="callout">
        <div class="lab">For corporate groups</div>
        <p>An hour from Toronto, which makes this the easiest single day retreat we design: a private cellar visit, a tasting for the team, and dinner on the estate, with transport handled from the city.</p>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">Appointments first, then the town</h2>
          <p>We book the cellar appointments before we plan anything else, because the visit that makes the day is the one with a person rather than a pour. From there the shape is simple: two visits, one long lunch, and the evening wherever the light is best.</p>
          <p>Niagara pairs naturally with Prince Edward County for a lakeshore journey of seven to ten days, and with the Rockies for guests who want wine and mountains in the same trip.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/notl-guide.svg" width="1400" height="800" alt="Driver-guide waiting outside a Niagara winery for private guests" loading="lazy">
          <figcaption>We drive, so nobody at the table has to count glasses.</figcaption>
        </figure>
      </div>
    </div>
  </section>
""",
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
        "destinations/niagara-on-the-lake-private-tour/", 43.2537, -79.0709, "/images/notl-hero.svg",
        ["Couples", "Retirees", "Independent travellers", "Corporate groups"])],
)

ALL = [HUB, TOFINO, SALTSPRING, JASPER, BANFF, PEC, NOTL]