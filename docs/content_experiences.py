"""Experience and segment pages: hub plus five segment journeys.
Segment rules live in 02-AUDIENCES. Personal credibility is mandatory on the
families and retirees pages. Family travel language: "we have children ourselves",
never "our family travels alongside yours".
"""

# ---------------------------------------------------------------- hub

HUB = dict(
    path="experiences/",
    title="Private Guided Tours in Canada | Luxury Tours Canada",
    desc="Private guided tours Canada by segment: independent travellers, honeymoons and proposals, families, retirees, and corporate retreats, eight guests maximum.",
    crumb=[("Home", "/"), ("Experiences", "/experiences/")],
    og_image="/images/exp-private-hero.jpg",
    best_for=["Retirees", "Couples", "Independent travellers", "Corporate groups"],
    hero=dict(
        eyebrow="Eight kinds of traveller",
        h1="Private Guided Tours Canada, Built Around Who Is Travelling",
        sub="A honeymoon, a family with a six year old, and a leadership retreat are three different countries. We design each one from the brief, never from a template.",
        img="/images/exp-hero.jpg",
        alt="Private guided tours Canada: a guide and two guests on a quiet trail in the Canadian Rockies",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white" aria-label="Private guided tour facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Party size</div><p class="small">Eight guests maximum on every private journey, with corporate retreats running six to thirty</p></div>
        <div><div class="lab">Design basis</div><p class="small">Built from your brief and your dates, never from a template or a departure board</p></div>
        <div><div class="lab">Private throughout</div><p class="small">Private vehicles, private boats, and one guide from the first morning to the last</p></div>
        <div><div class="lab">First reply</div><p class="small">A written answer within 24 hours, including the honest word on your dates and season</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="How the segment shapes the journey">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The approach</div>
          <h2 class="section-title">The segment decides <em>everything.</em></h2>
          <p>The segment decides the pace, the properties, the operational detail, and what the journey is for. A retiree journey has no departure before half past eight. A family journey pre-sources child seats and briefs children on wildlife before every walk. A proposal gets a second location and a second time window, because mountain weather turns by the hour.</p>
          <p>Read the shape that sounds like your party below. If two of them do, that is normal, and we will design around both: the operational rules for the stricter of the two segments, applied throughout.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/exp-constant.jpg" width="1400" height="800" alt="Guide checking the marine forecast before a private boat day in British Columbia on a private guided tour in Canada" loading="lazy">
          <figcaption>Weather checked the evening before, not the morning of.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="The journey shapes">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">The shapes</div>
        <h2 class="section-title">Five journeys, <em>one standard.</em></h2>
        <p class="lede">Each shape below is its own page, with the operational detail spelled out: the departure rules, the room logic, and the way the days are built.</p>
      </div>
      <div class="grid g-3">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-independent.jpg" width="600" height="400" alt="Independent travellers on a quiet road in the Canadian Rockies" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Independent travellers</h3><p>Seasoned, well researched, and allergic to coaches. Access and exclusivity, with named places rather than scenery.</p><a class="more" href="/experiences/private-tours/">Private journeys</a></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-honeymoon.jpg" width="600" height="400" alt="Couple watching the Pacific from a soaking tub on a Canada honeymoon" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Honeymoons and proposals</h3><p>The moment handled completely, including a second location if the weather takes an interest. Discretion from the first email.</p><a class="more" href="/experiences/honeymoon-proposals/">Romance, planned</a></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-family.jpg" width="600" height="400" alt="Family with children on a guided walk in the Canadian Rockies" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Families with children</h3><p>Child seats pre-sourced, nap-timed drives, wildlife briefings, and cold-water rules taken seriously.</p><a class="more" href="/experiences/family-tours/">Family travel</a></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-retiree.jpg" width="600" height="400" alt="Retiree couple on the Icefields Parkway with a private vehicle and guide" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Retirees</h3><p>Unhurried days, honest altitude notes, the same guide throughout, and the trip you have been planning for decades finally done right.</p><a class="more" href="/experiences/retirement-travel/">Unhurried journeys</a></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-mice.jpg" width="600" height="400" alt="Leadership retreat group in a mountain lodge in Alberta" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Corporate and MICE</h3><p>Retreats for six to thirty with one point of contact, a fallback venue for every programme, and outcomes stated before experiences.</p><a class="more" href="/experiences/corporate-mice/">Retreats</a></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-more.jpg" width="600" height="400" alt="Notebook, map, and coffee on a table beside an itinerary" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Three more shapes</h3><p>Anniversaries and escapes, a safe gap year for an eighteen year old, and a yearly holiday where every single day earns its place. Ask us for the shape in writing.</p><a class="more" href="/#begin">Tell us your dates</a></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="What the segment changes">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">What the segment changes</div>
        <h2 class="section-title">Same country, <em>different rules.</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">Departure times</h3><p>Retiree journeys hold a half past eight floor. Family journeys bend around naps. Everyone else starts when the light is best, which in June can be very early.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Driving days</h3><p>The Rockies forgive a long drive and the parkway is the point of the day. The lakeshore never needs one. Family days are capped shorter, and retreat agendas keep transfers off them.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Activity level</h3><p>The walking is stated honestly at every stop, from the steps at a canyon to a flat vineyard morning, and altitude notes are given in advance, not discovered on the day.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Tables and rooms</h3><p>Honeymoons get the room and the table chosen first. Families get connecting rooms and early seatings. Retreats get one invoice and one point of contact.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Weather calls</h3><p>Every outdoor day carries a second option, and a proposal carries a second location and a second time window, because mountain weather turns by the hour.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Who plans what</h3><p>You tell us who is travelling and what the trip is for. We do the rest: the appointments, the permits, the child seats, the medical notes, and the plan B you should never need.</p></div></div>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="The constant across every journey">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">The constant</div>
          <h2 class="section-title">One rule, <em>every segment.</em></h2>
          <blockquote>Every client we serve is paying to not think about logistics.</blockquote>
          <p class="small" style="margin-top:14px">Our job is to make long roads and fast weather feel effortless, whether you are travelling with a toddler, a board of directors, or a ring in your pocket.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/exp-more.jpg" width="1400" height="800" alt="Journey planning notes and a map beside a coffee on a private guided tour in Canada" loading="lazy">
          <figcaption>One brief, one design, one point of contact.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Where the journeys go">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">The roads</div>
      <h2 class="section-title">The roads are <em>the other half.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Every journey above runs through one of three regions we know road by road: the BC coast, the Canadian Rockies, and the Ontario lakeshore. Choose the roads and we design the days around who is travelling.</p>
      <a class="btn" href="/destinations/">Explore the three regions</a>
    </div>
  </section>
""",
    cta_band=("/images/exp-hero.jpg",
              "Private guided tours Canada: a guide and two guests on a quiet trail in the Canadian Rockies",
              "Ready to plan your journey?",
              "Tell us what you are imagining. We will come back within 24 hours.",
              "Begin Your Journey"),
    faq=[
        ("How do you decide which shape of journey suits us?",
         "<p>By asking a handful of questions about who is travelling, the season, the pace, and what would make the trip worth it. Most parties land in one segment clearly. Some sit between two, usually independent traveller and professional on their yearly holiday, and we design for both.</p>"),
        ("Do you run group departures we can join?",
         "<p>No. Every journey is private to your party, with a maximum of eight guests. That is not a positioning statement, it is how the itinerary works: private vehicles, private boats, and days built around one group's pace.</p>"),
        ("Can you combine two segments in one journey?",
         "<p>Often, and it is usually families with retirees travelling together, or a corporate group extending into a private weekend. We design the operational rules for the stricter of the two segments and apply them throughout.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_trip(
        "Private Guided Tours in Canada",
        "Private guided tours in Canada designed around who is travelling: honeymoons and proposals, families, retirees, independent travellers, and corporate retreats, eight guests maximum.",
        "Independent travellers, couples, families, retirees, corporate groups",
        "experiences/")],
)

# ---------------------------------------------------------------- private tours

PRIVATE = dict(
    path="experiences/private-tours/",
    title="Private Tours Canada | Independent Luxury Journeys",
    desc="Private tours Canada for independent travellers: access where coaches cannot go, named places, not scenery, and routes from 27 years on the road.",
    crumb=[("Home", "/"), ("Experiences", "/experiences/"), ("Private Journeys", "/experiences/private-tours/")],
    og_image="/images/exp-private-hero.jpg",
    best_for=["Independent travellers", "Couples", "Retirees", "Families with teenagers"],
    hero=dict(
        eyebrow="Independent travellers",
        h1="Private Tours Canada: A Canada the Highway Does Not Show You",
        sub="You have done Banff once, or you know it from a hundred photographs, and you are not going to see it from a bus seat. Good. Neither are we.",
        img="/images/exp-private-hero.jpg",
        alt="Private tours Canada: an empty mountain road at dawn on a luxury Canada journey",
        cta="Plan My Private Journey",
    ),
body="""
  <section class="band-white" aria-label="Private tour facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Party size</div><p class="small">Eight guests maximum, with the vehicles and boats sized to your party and nobody else</p></div>
        <div><div class="lab">Design basis</div><p class="small">Built from your brief and your dates, never from a template or a departure board</p></div>
        <div><div class="lab">Access</div><p class="small">Routes, hours, and waters the coach groups cannot use, chosen for the season you travel</p></div>
        <div><div class="lab">First reply</div><p class="small">A written answer within 24 hours, including the honest word on your dates and season</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="How a private Canada journey is built">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The approach</div>
          <h2 class="section-title">What you are paying for is <em>access and judgement.</em></h2>
          <p>Independent travellers research deeply, dislike group tours, and find most travel marketing patronising. So here is the plain version: we go where the coaches cannot, we time the famous places for the hours nobody else uses, and we name the places instead of describing the scenery.</p>
          <p>The judgement is the part that cannot be booked anywhere else. Knowing that Tofino is at its best in the shoulder seasons and out on the water, that Jasper beats Banff for a private base, that the Icefields Parkway wants a full tank before it starts, and that the pull-off with the view is rarely the pull-off with the sign.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/exp-private-road.jpg" width="1400" height="800" alt="Empty mountain switchbacks at sunrise on a private Canada tour" loading="lazy">
          <figcaption>The road at six in the morning, and no one on it.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="What a private Canada journey holds">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">What a private journey <em>actually holds</em></h2>
        <p class="lede">Six things that separate a private Canada tour from the same road on a coach.</p>
      </div>
      <div class="hc-carousel" id="hcCarousel" tabindex="0" aria-label="Private Canada journey experiences, scroll horizontally">
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-private-dawn.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">01</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The quiet hours</span>
            <h3 class="hc-card-title">Famous places, before anyone arrives</h3>
            <p class="hc-card-desc">Lake Louise at sunrise, Maligne Lake before the day visitors, and the Pacific beaches before eight. The same places, at the hours that make the drive worth it.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-private-boat.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">02</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">Private waters</span>
            <h3 class="hc-card-title">The outer sound, your own boat</h3>
            <p class="hc-card-desc">A private vessel with a naturalist aboard, out past where the tour boats turn around, on the days the marine forecast allows it.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-private-expert.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">03</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The guide</span>
            <h3 class="hc-card-title">Someone who has done it many times</h3>
            <p class="hc-card-desc">Not a driver with a script. A guide who knows the road, the wildlife distances, the weather patterns, and when to change the plan.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/dest-banff.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">04</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The route</span>
            <h3 class="hc-card-title">Yoho instead of Banff</h3>
            <p class="hc-card-desc">The quiet valley rather than the busy one, the county road rather than the highway, and the ferry timing that keeps an island day unhurried.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/dest-lakeshore.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">05</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The lakeshore</span>
            <h3 class="hc-card-title">The Ontario back roads</h3>
            <p class="hc-card-desc">Vineyards, limestone towns, and the best table of the day found on a road with no coach on it.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/jasper-darksky.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">06</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">After dark</span>
            <h3 class="hc-card-title">Dark skies and the last light</h3>
            <p class="hc-card-desc">Jasper is a dark sky preserve. The evening after dinner becomes part of the route, with the scope set up and no light pollution between you and it.</p>
          </div>
        </div>
      </div>
      <p class="small" style="margin-top:12px">Drag the cards to browse the shapes.</p>
    </div>
  </section>

  <section class="band-white" aria-label="Where private Canada journeys run">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">The regions</div>
        <h2 class="section-title">Three regions, <em>known road by road</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">🌊</span><div class="exp-title">British Columbia coast</div><p class="exp-body">Clayoquot Sound, the Pacific Rim, and the Gulf Islands, with private boats and floatplane transfers between them.</p><a href="/destinations/tofino-private-tour/" class="exp-cta">Tofino</a></div>
        <div class="exp-card"><span class="exp-icon">🏔️</span><div class="exp-title">The Canadian Rockies</div><p class="exp-body">Jasper for a private base, Yoho for the quiet valley, and the Icefields Parkway driven at the hours it deserves.</p><a href="/destinations/banff-yoho-private-tour/" class="exp-cta">Banff and Yoho</a></div>
        <div class="exp-card"><span class="exp-icon">🍇</span><div class="exp-title">Ontario lakeshore</div><p class="exp-body">Niagara wine country, Prince Edward County, and the limestone towns, ridden on a bicycle before they were driven past.</p><a href="/destinations/prince-edward-county-private-tour/" class="exp-cta">The lakeshore</a></div>
        <div class="exp-card"><span class="exp-icon">🍁</span><div class="exp-title">Gulf Islands</div><p class="exp-body">Salt Spring and its neighbours, where the drives run minutes rather than hours and the market sets the rhythm of the week.</p><a href="/destinations/salt-spring-island-private-tour/" class="exp-cta">Salt Spring</a></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Planning notes for a private Canada tour">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">What to know <em>before you go</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">When to travel</h3><p>Late June to early October for the Rockies. May and June, then September and October, for the BC coast. May to October for the Ontario lakeshore. Tell us your month and we will tell you honestly which region suits it.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">How long</h3><p>Seven to fourteen days for one region done properly. Eighteen to twenty-one days to cross from the Pacific coast to the mountains and on to the lakeshore. A rushed Canada is a wasted one.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The vehicle</h3><p>A private vehicle with a guide, sized to the party, with child seats where they are needed. Coaches appear only if a corporate group explicitly asks for one.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Water days</h3><p>Boat and floatplane days are weather dependent. Your guide checks the marine forecast the evening before, and a fallback day is written into the plan before you fly.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The walking</h3><p>Activity is stated honestly at every stop, from the steps at a canyon to a flat vineyard morning, and altitude notes come in advance rather than on the day.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">What it includes</h3><p>Private transfers throughout, a dedicated guide, park passes and entrance fees, wildlife briefings before every walk, and a 24-hour contact for the whole journey.</p></div></div>
      </div>
      <div class="prose" style="margin-top:22px">
        <ul class="ticks">
          <li>All private ground transfers, airport to lodge and between destinations</li>
          <li>Domestic flights and floatplane transfers where the route calls for them</li>
          <li>Private boat, canoe, and crew on every water day</li>
          <li>Daily breakfast, plus the lunches and dinners noted in your itinerary</li>
          <li>National and provincial park passes and all entrance fees</li>
          <li>A single point of contact for changes, and a 24-hour line while you are in the country</li>
        </ul>
      </div>
      <p class="small">Not included: international flights, alcohol and room charges, personal shopping, activities added outside the plan, travel medical insurance, eTA fees where required, and gratuities.</p>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we design a private Canada journey">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we design this journey</div>
          <h2 class="section-title">The plan is written <em>around the hours that matter</em></h2>
          <p>We build the day around the two or three moments that make it worth the drive, then fill in around them: the boat that leaves the harbour before the fleet, the cellar where the winemaker still pours, the walk into the old growth at the hour the light comes through the canopy.</p>
          <p>Every one of those has been done here first, in the cold months as well as the warm ones, and in both directions. That is the standard the route is built to, and the reason a private journey here is shorter than it looks on paper and fuller than you expect on the day.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/exp-constant.jpg" width="1400" height="800" alt="Guide checking the marine forecast before a private boat day in British Columbia" loading="lazy">
          <figcaption>Weather checked the evening before, not the morning of.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Where the roads go">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">One country, a dozen roads</div>
      <h2 class="section-title">The regions decide <em>where the road goes.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Who is travelling decides the pace, the rooms, and the shape of every day. Choose the region first, then tell us who is coming and what the journey is for.</p>
      <a class="btn" href="/destinations/">Explore the three regions</a>
    </div>
  </section>
""",
    cta_band=("/images/exp-private-cta.jpg", "Private tours Canada: a mountain lake at dusk with a canoe at the shore",
              "Begin Your Journey", "Tell us what you are imagining. We will come back within 24 hours.", "Begin Your Journey"),
    faq=[
        ("What makes a private tour different from a small group tour?",
         "<p>The itinerary belongs to your party. There is no fixed departure, no other guests, and no schedule to fit around. Days start when you want them to, the route bends when something is worth staying for, and the vehicle and guide stay with you throughout.</p>"),
        ("Do you use coaches or vans for private tours in Canada?",
         "<p>Private vehicles with a guide, sized to the party, with child seats where they are needed. Coaches appear only if a corporate group explicitly wants one, and even then the days are built to avoid the places coaches queue.</p>"),
        ("Can you build a Canada tour around a specific interest, like wildlife or wine?",
         "<p>Yes, and it usually improves the journey. Wildlife shapes the Rockies and the BC coast. Wine shapes the Ontario lakeshore. Photography, hiking, and dark skies are all strong threads to pull through a route, and each one changes which months we recommend.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_trip(
        "Private Tours Canada for Independent Travellers",
        "Bespoke private tours of Canada for independent travellers, with access where coaches cannot go, quiet-hour timing at the famous places, and private guides throughout.",
        "Independent travellers", "experiences/private-tours/")],
)

# ---------------------------------------------------------------- honeymoon and proposals

HONEYMOON = dict(
    path="experiences/honeymoon-proposals/",
    title="Canada Honeymoon Luxury | Proposals and Honeymoons",
    desc="Canada honeymoon luxury and proposal planning: private lodges, quiet lakes at dawn, Pacific storms, and a second location if weather intervenes.",
    crumb=[("Home", "/"), ("Experiences", "/experiences/"), ("Honeymoons and Proposals", "/experiences/honeymoon-proposals/")],
    og_image="/images/exp-honeymoon-hero.jpg",
    best_for=["Honeymooners", "Proposal planners", "Couples", "Anniversaries"],
    hero=dict(
        eyebrow="Couples, proposals, and honeymoons",
        h1="Canada Honeymoon Luxury: The Trip You Will Retell for the Rest of Your Lives",
        sub="A private lodge, a lake at dawn with the mist still on it, and a storm coming in off the Pacific while you watch it from a soaking tub. And nobody has to plan a thing.",
        img="/images/exp-honeymoon-hero.jpg",
        alt="Canada honeymoon luxury: a couple watching the Pacific from the window of a private Tofino lodge",
        cta="Plan Our Journey",
    ),
    body="""
  <section class="band-white" aria-label="Canada honeymoon facts">
    <div class="wrap">
      <div class="grid g-4">
        <div><div class="lab">Party size</div><p class="small">Just the two of you, with one planner handling everything from the first call to the last transfer</p></div>
        <div><div class="lab">Design basis</div><p class="small">Built around the moment you are planning, a proposal or a honeymoon, never around a package</p></div>
        <div><div class="lab">The proposal</div><p class="small">Location, timing, photographer, decoy, and a second window, all rehearsed before you fly</p></div>
        <div><div class="lab">First reply</div><p class="small">A written answer within 24 hours, kept quietly to one of you</p></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="How we plan a Canada honeymoon">
    <div class="wrap">
      <div class="split">
        <div class="prose">
          <div class="lab eyebrow">The approach</div>
          <h2 class="section-title">Honeymoons and proposals run on <em>feeling first.</em></h2>
          <p>These are the two journeys where feeling comes first and logistics come second, and both are the happier for it. You tell us the moment you want, and we build the days around it: private lodges, quiet water, dinners at tables no one else is at, and the small logistics handled so completely that you never have to think about them.</p>
          <p>For proposal planners, everything runs quietly in the background. A hidden photographer, a private location, a decoy activity, and a second location and time window, because mountain weather turns by the hour and this moment does not get a second take.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/exp-honeymoon-lake.jpg" width="1400" height="800" alt="Maligne Lake at dawn on a Canada honeymoon, canoe at the shore in still water" loading="lazy">
          <figcaption>Maligne Lake before the day visitors, which is the whole point of going with us.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="What a Canada honeymoon actually holds">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Key experiences</div>
        <h2 class="section-title">Six things that make a Canada honeymoon <em>yours</em></h2>
        <p class="lede">What separates a honeymoon built for two from the same trip booked off a shelf.</p>
      </div>
      <div class="hc-carousel" id="hcCarousel" tabindex="0" aria-label="Canada honeymoon experiences, scroll horizontally">
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-honeymoon-photographer.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">01</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The proposal</span>
            <h3 class="hc-card-title">The moment, kept secret</h3>
            <p class="hc-card-desc">The photographer is placed before you arrive, the decoy activity is real, and the timing is rehearsed without the other person noticing a thing.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-honeymoon-strip-1.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">02</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The arrival</span>
            <h3 class="hc-card-title">A floatplane to the lodge</h3>
            <p class="hc-card-desc">Arrival by private floatplane or a quiet transfer, luggage handled, so the honeymoon starts calmly rather than at a carousel.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-honeymoon-weather.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">03</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The fallback</span>
            <h3 class="hc-card-title">A second location, a second window</h3>
            <p class="hc-card-desc">Every proposal, and every outdoor day, carries an alternative at the same hour. It is written before you travel, not improvised on the day.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-honeymoon-quiet.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">04</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The table</span>
            <h3 class="hc-card-title">Dinner where no one else is</h3>
            <p class="hc-card-desc">Private dining rather than the best table in the room, and lodges chosen for what you can see from the window at six in the morning.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-honeymoon-strip-2.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">05</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The coast</span>
            <h3 class="hc-card-title">Storm watching from the tub</h3>
            <p class="hc-card-desc">A Tofino room built for the weather, a soaking tub facing the Pacific, and the whole storm yours to watch while the fire stays lit.</p>
          </div>
        </div>
        <div class="hc-card">
          <div class="hc-card-img" style="background-image:url('/images/exp-honeymoon-strip-3.jpg')"></div>
          <div class="hc-card-base"></div>
          <div class="hc-card-num">06</div>
          <div class="hc-card-content">
            <span class="hc-card-tag">The morning</span>
            <h3 class="hc-card-title">Breakfast set for two</h3>
            <p class="hc-card-desc">Breakfast at your own table, at your own hour, before anyone else in the lodge is up and the lake is still holding the mist.</p>
          </div>
        </div>
      </div>
      <p class="small" style="margin-top:12px">Drag the cards to browse the shapes.</p>
    </div>
  </section>

  <section class="band-white" aria-label="Where a Canada honeymoon runs">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">The settings</div>
        <h2 class="section-title">Four settings, <em>each a different mood</em></h2>
      </div>
      <div class="exp-grid">
        <div class="exp-card"><span class="exp-icon">🌊</span><div class="exp-title">British Columbia coast</div><p class="exp-body">Tofino for the raw Pacific, the storms, and the room with the tub, with private boats and floatplane transfers between the islands.</p><a href="/destinations/tofino-private-tour/" class="exp-cta">Tofino</a></div>
        <div class="exp-card"><span class="exp-icon">🏔️</span><div class="exp-title">The Canadian Rockies</div><p class="exp-body">Jasper for dark skies and long mountain mornings, Banff and Yoho for the lakes at the hour before the day visitors arrive.</p><a href="/destinations/jasper-private-tour/" class="exp-cta">Jasper</a></div>
        <div class="exp-card"><span class="exp-icon">🍇</span><div class="exp-title">Ontario lakeshore</div><p class="exp-body">Niagara wine country and Prince Edward County, slow mornings, cellar tables, and limestone towns on a road with no coach on it.</p><a href="/destinations/prince-edward-county-private-tour/" class="exp-cta">The lakeshore</a></div>
        <div class="exp-card"><span class="exp-icon">🍁</span><div class="exp-title">Gulf Islands</div><p class="exp-body">Salt Spring and its neighbours, where the drives run minutes rather than hours and the market sets the rhythm of the week.</p><a href="/destinations/salt-spring-island-private-tour/" class="exp-cta">Salt Spring</a></div>
      </div>
    </div>
  </section>

  <section class="band-glacier" aria-label="Planning notes for a Canada honeymoon">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Planning notes</div>
        <h2 class="section-title">What to know <em>before you go</em></h2>
      </div>
      <div class="grid g-3">
        <div class="card"><div class="body"><h3 class="card-title">When to travel</h3><p>May and June, then September and October, for the BC coast and its storms. Late June to early October for the Rockies. Tell us your month and we will tell you honestly which setting pairs best with it.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">How long</h3><p>Five to eight days for a honeymoon in one region, done slowly. Ten to fourteen to pair the Pacific coast with the mountains. The trip should feel shorter than it is.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">Where to base</h3><p>Two bases at most, chosen so you unpack once and settle rather than move every night. A lodge with a view beats a list of towns ticked off.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The proposal</h3><p>One person plans it, correspondence stays discreet, and the photographer, location, and decoy activity are arranged before you land. Nothing about the day reads as staged.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The weather</h3><p>Mountain weather turns by the hour and the Pacific keeps its own forecast. Every outdoor day carries a fallback, and your planner watches the forecast the evening before, not the morning of.</p></div></div>
        <div class="card"><div class="body"><h3 class="card-title">The quiet</h3><p>No group departures, no shared boats, and a schedule that starts when you want it to. If you would rather stay in with the view, the day can be left empty on purpose.</p></div></div>
      </div>
      <div class="prose" style="margin-top:22px">
        <ul class="ticks">
          <li>Private transfers throughout, including the arrival, so the journey starts calmly</li>
          <li>A private boat day on the coast, or a canoe on a mountain lake, guide included</li>
          <li>The proposal setup on a proposal journey: location, timing, photographer, decoy, and the fallback</li>
          <li>Private dinners and one table arranged where the setting does the work</li>
          <li>Accommodation at the finest available property in each setting, confirmed after our call</li>
          <li>A single point of contact before you travel, and a 24-hour line while you are in the country</li>
        </ul>
      </div>
      <p class="small">Not included: international flights, alcohol outside arranged dinners, personal shopping, activities added outside the plan, travel medical insurance, and gratuities.</p>
    </div>
  </section>

  <section class="band-spruce on-dark" aria-label="How we keep a Canada honeymoon quiet">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">How we plan it</div>
          <h2 class="section-title">The details stay <em>out of your way</em></h2>
          <p>A honeymoon should not feel managed, even when it is. We build the day around the two or three moments that matter, then handle everything around them quietly: the transfer timed to your flight, the table held under one name, the boat booked before the harbour fills, and the weather watched from the evening before.</p>
          <p>For a proposal, that work happens weeks ahead and stays invisible. The location is checked at the same hour on the same day of the week in the same season, the photographer is positioned so the moment is captured without being seen, and every written fallback is rehearsed with you. Nothing is left to chance, and nothing about it feels arranged.</p>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/exp-constant.jpg" width="1400" height="800" alt="Planner checking the forecast the evening before a private water day on a Canada honeymoon" loading="lazy">
          <figcaption>Weather checked the evening before, not the morning of.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white" aria-label="Where the moments happen">
    <div class="wrap" style="text-align:center">
      <div class="lab eyebrow">One country, a dozen quiet corners</div>
      <h2 class="section-title">The setting decides <em>the mood of the trip.</em></h2>
      <p class="lede" style="max-width:640px;margin:0 auto 18px">Tofino for the raw Pacific, Salt Spring for slowness, the Rockies for dark skies and long mornings. Choose the setting first, then tell us the moment you are planning and who is in on it.</p>
      <a class="btn" href="/destinations/">Explore the regions</a>
    </div>
  </section>
""",
    cta_band=("/images/exp-honeymoon-cta.jpg", "Canada honeymoon luxury: a lodge window looking out over a mountain lake at dusk",
              "Begin Your Journey", "Tell us what you are imagining, and we will keep it quiet.", "Plan Our Journey"),
    faq=[
        ("Where in Canada is best for a honeymoon?",
         "<p>Tofino for the Pacific, the storms, and the room with the tub. Salt Spring Island for slowness and farm tables. Jasper for dark skies and mountain lodges. The best honeymoon pairs two of them, and the season decides which pair works.</p>"),
        ("Can you plan a surprise proposal without my partner finding out?",
         "<p>Yes, and it is a large part of what we do. The planning runs through one person, the correspondence is discreet, the photographer and location are arranged in advance, and the decoy activity is built so the day reads as an ordinary one right up to the moment.</p>"),
        ("What if the weather ruins the proposal location?",
         "<p>Every proposal we plan carries a second location and a second time window at the same hour, plus a written plan for what could go wrong. Mountain weather turns by the hour, so this is not pessimism, it is how a proposal gets made on the day you planned it.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_trip(
        "Canada Honeymoon and Proposal Journeys",
        "Private Canada honeymoon luxury journeys and proposal planning, with private lodges, quiet lakes, Pacific storm watching, and a second location for every proposal.",
        "Honeymooners and proposal planners", "experiences/honeymoon-proposals/")],
)

# ---------------------------------------------------------------- families

FAMILY = dict(
    path="experiences/family-tours/",
    title="Luxury Family Tour Canada | Travel With Kids Done Right",
    desc="A luxury family tour Canada families finish: child seats pre-sourced, nap-timed drives, wildlife briefings, and cold-water rules taken seriously.",
    crumb=[("Home", "/"), ("Experiences", "/experiences/"), ("Family Travel", "/experiences/family-tours/")],
    og_image="/images/exp-family-hero.jpg",
    hero=dict(
        eyebrow="Families with children",
        h1="Luxury Family Tours Canada: Travel With Kids, Done Right",
        sub="Car seats in every vehicle, drives timed around naps, wildlife briefings before every walk, and a beach plan that respects how cold the Pacific actually is.",
        img="/images/exp-family-hero.jpg",
        alt="Luxury family tour Canada: parents and children on a guided lakeside walk in the Canadian Rockies",
        cta="Plan A Family Journey",
    ),
    body="""
  <section class="band-deep on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">Why we understand family travel</div>
          <blockquote>We have children ourselves, so we know what it actually takes to cross this country with them: the logistics that fall apart, the schedules that do not survive contact with a six year old, and the moments that make all of it worth it.</blockquote>
          <p class="small" style="margin-top:14px">Our own family does not travel on client journeys. Local guides and vetted childminders look after the family-facing details on the ground, and every family journey is designed around that reality rather than around the version of family travel that looks good in a brochure.</p>
        </div>
        <figure class="shot shot-hero">
          <img src="/images/exp-family-portrait.jpg" width="800" height="1000" alt="Family with young children preparing for a guided walk in the Canadian Rockies" loading="lazy">
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">What we do differently</div>
        <h2 class="section-title">The things nobody else thinks about</h2>
      </div>
      <div class="grid g-3">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-family-carseat.jpg" width="600" height="400" alt="Child seat installed in a private vehicle on the Icefields Parkway" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Car seats, pre-sourced</h3><p>Child seats are required by law in Canada, and on a long drive they are essential. We confirm the right seats for each child before you land, in every vehicle.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-family-wildlife.jpg" width="600" height="400" alt="Guide briefing children before a wildlife walk in Jasper" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Wildlife briefings for children</h3><p>Short, clear, and repeated before every walk, so the wildlife stays at a distance and the children understand why. Bears are seen, never approached.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-family-water.jpg" width="600" height="400" alt="Guide supervised beach day with wetsuits on the BC coast" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Cold water, taken seriously</h3><p>Pacific and glacial water is cold year round. Wetsuits for any swimming, guide-supervised beach days only, and the lake rather than the ocean when the children want to stay in.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">By age</div>
        <h2 class="section-title">What works at each age</h2>
      </div>
      <div class="prose">
        <ul class="ticks">
          <li><strong>Toddlers, 0 to 3.</strong> Car seats, nap-timed drives, warm layers, and shallow beach play only. Salt Spring's short distances suit this stage better than the Rockies.</li>
          <li><strong>Young children, 4 to 8.</strong> Wildlife, canoeing, farm days on Salt Spring, and energy managed rather than spent. Long drives get stops built in.</li>
          <li><strong>Pre-teens, 9 to 14.</strong> Glacier walks, canoeing, and the cultural experiences they will actually remember. The Rockies open up properly at this age.</li>
        </ul>
      </div>
      <div class="grid g-3">
        <figure class="shot shot-card"><img src="/images/exp-family-strip-1.jpg" width="600" height="400" alt="Family canoeing on a Rockies lake with a guide" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/exp-family-strip-2.jpg" width="600" height="400" alt="Children at a Salt Spring Island farm stand" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/exp-family-strip-3.jpg" width="600" height="400" alt="Nap-timed drive with a stop at a mountain viewpoint" loading="lazy"></figure>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">What is included</div>
        <h2 class="section-title">Everything pre-sourced before you land</h2>
      </div>
      <ul class="ticks prose">
        <li>Child seats pre-sourced for every vehicle, and fitted before your arrival</li>
        <li>A cot, high chair, and carriers arranged at each property, confirmed in advance</li>
        <li>Wetsuits and child-sized safety equipment for water days</li>
        <li>Wildlife briefings for children before every walk</li>
        <li>Vetted childminder contacts at each destination, on request</li>
        <li>Private vehicles with nap-timed drives and stops built into every long leg</li>
        <li>A sick-day fallback written into the itinerary, because children are children</li>
        <li>A 24-hour contact for the whole journey</li>
      </ul>
      <p class="small">Not included: international flights, travel medical insurance (strongly recommended for every traveller), eTA fees where required, personal shopping, and gratuities.</p>
    </div>
  </section>
""",
    cta_band=("/images/exp-family-cta.jpg", "Family watching a mountain sunset from a lakeside lodge deck in Canada",
              "Begin Your Journey", "Tell us the ages and the season, and we will tell you honestly which region suits them.", "Plan A Family Journey"),
    faq=[
        ("What is the best Canada itinerary with a toddler?",
         "<p>Short distances, one base, and a gentle rhythm. Salt Spring Island and the Ontario lakeshore work better for toddlers than the Rockies, because the drives are fifteen minutes rather than three hours. If the Rockies are the dream, we build it around Jasper with nap-timed drives and a rest in the middle of each day.</p>"),
        ("Do you provide car seats for children in Canada?",
         "<p>Yes. Child seats are required by law, and we pre-source the correct seats for each child in every vehicle, fitted before you arrive. It is the first line of our pre-arrival checklist and not something you need to bring.</p>"),
        ("Is it safe to travel in bear country with children?",
         "<p>It is, with the right briefings. Wildlife is viewed at distance and guide-led, never approached, and every walk starts with a short briefing pitched at the children. Bear spray, group positioning, and route choice are the guide's job, and they are done every day.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_trip(
        "Luxury Family Tours Canada",
        "Private luxury family tours of Canada with child seats pre-sourced, nap-timed drives, wildlife briefings for children, and guide-supervised water days.",
        "Families with children", "experiences/family-tours/")],
)

# ---------------------------------------------------------------- retirees

RETIREE = dict(
    path="experiences/retirement-travel/",
    title="Retiree Travel Canada Luxury | Unhurried Journeys Canada",
    desc="Retiree travel Canada luxury, unhurried: no departures before 8:30am, honest altitude and medical notes, the same guide, and the trip you waited decades for.",
    crumb=[("Home", "/"), ("Experiences", "/experiences/"), ("Retiree Journeys", "/experiences/retirement-travel/")],
    og_image="/images/exp-retiree-hero.jpg",
    hero=dict(
        eyebrow="Retirees and senior travellers",
        h1="Retiree Travel Canada Luxury: The Trip You Have Been Planning for Decades",
        sub="No departure before half past eight. Long views, short walks, the same guide every day, and a pace that finally matches the way you want to travel.",
        img="/images/exp-retiree-hero.jpg",
        alt="Retiree travel Canada luxury: an unhurried private vehicle stop on the Icefields Parkway",
        cta="Plan My Retiree Journey",
    ),
    body="""
  <section class="band-deep on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">Why we design for this</div>
          <blockquote>We design journeys for retirees as a core part of what we do, and what we have learned is that this is rarely just a trip. It is often the one that has been imagined through working years.</blockquote>
          <p class="small" style="margin-top:14px">That changes how we plan it: the pace, the properties, the sequence, everything built around comfort, familiarity, and the complete absence of rushing.</p>
        </div>
        <figure class="shot shot-hero">
          <img src="/images/exp-retiree-portrait.jpg" width="800" height="1000" alt="Retired couple on a lodge deck overlooking a Canadian mountain lake" loading="lazy">
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">What we do differently</div>
        <h2 class="section-title">Pace is the whole design</h2>
      </div>
      <div class="grid g-3">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-retiree-morning.jpg" width="600" height="400" alt="Breakfast on a lodge terrace with a mountain view at half past eight" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">No departures before 8:30am</h3><p>Wildlife is best at dawn, so the outing moves to late afternoon or evening instead of an early start. Mornings belong to breakfast and the view.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-retiree-walk.jpg" width="600" height="400" alt="Short guided walk on firm ground with long views in the Canadian Rockies" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Short walks, long views</h3><p>Every itinerary states walking distance, terrain, and altitude for each day. The Icefields Parkway by private vehicle, with the walking kept optional.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-retiree-medical.jpg" width="600" height="400" alt="Guide reviewing a printed itinerary with guests at a lodge" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Medical notes in writing</h3><p>The nearest hospital or clinic is noted for every destination, altitude is stated honestly, and travel medical insurance is treated as essential, not optional.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">How it works</div>
        <h2 class="section-title">Three steps, taken slowly</h2>
      </div>
      <ol class="steps">
        <li><span class="num">1</span><div><strong>We talk about pace first.</strong> Walking distances, stairs, altitude, and how you like your mornings.</div></li>
        <li><span class="num">2</span><div><strong>We design around comfort.</strong> One base at a time, short drives, the same vehicle and guide, and an afternoon rest in most days.</div></li>
        <li><span class="num">3</span><div><strong>You travel unhurried.</strong> If any day needs to change, we change it. Nothing is fixed that does not have to be.</div></li>
      </ol>
      <div class="grid g-3">
        <figure class="shot shot-card"><img src="/images/exp-retiree-strip-1.jpg" width="600" height="400" alt="Private vehicle on the Icefields Parkway with a glacier viewpoint" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/exp-retiree-strip-2.jpg" width="600" height="400" alt="Garden and farm table lunch on Salt Spring Island" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/exp-retiree-strip-3.jpg" width="600" height="400" alt="Evening wildlife outing beside a quiet road in Jasper" loading="lazy"></figure>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">What is included</div>
        <h2 class="section-title">Designed for comfort, not compromise</h2>
      </div>
      <ul class="ticks prose">
        <li>Pace-adjusted scheduling: no departures before 8:30am, with an afternoon rest built in</li>
        <li>An accessibility briefing for each destination: walking distances, terrain, steps, and altitude</li>
        <li>Accommodation at the finest available property in each location, confirmed after our call</li>
        <li>The same vehicle and the same guide wherever the route allows</li>
        <li>Emergency medical contacts at every destination, and honest altitude notes</li>
        <li>Private transfers throughout, with luggage handled</li>
        <li>A 24-hour contact for the whole journey, and flexibility if a day needs to change</li>
      </ul>
      <p class="small">Not included: international flights, travel medical insurance (essential, and we will point you to providers), eTA fees where required, alcohol and room charges, and gratuities.</p>
    </div>
  </section>
""",
    cta_band=("/images/exp-retiree-cta.jpg", "Unhurried evening light over a Canadian mountain lake seen from a lodge",
              "Begin Your Journey", "Tell us the season and the pace, and we will design the days around both.", "Plan My Retiree Journey"),
    faq=[
        ("Do your Canada tours involve early starts?",
         "<p>No departures before half past eight, and we mean it. Where wildlife is better at dawn, we move the outing to late afternoon or evening rather than moving your alarm, which is a better wildlife hour anyway once the day visitors have gone.</p>"),
        ("How do you handle altitude and mobility in the Rockies?",
         "<p>We state altitude honestly, build a gentle first day, and keep the walking optional and short, with the vehicle close by. Lake Louise sits at about 1,600 metres, so the first day there is designed around a short walk and a long view. Every itinerary carries walking distances, terrain, and any steps for each day.</p>"),
        ("Is travel medical insurance really necessary for Canada?",
         "<p>Yes. Canada's public healthcare does not cover visitors, and treatment without insurance is expensive. We recommend it in every proposal and treat it as essential for retirees. We will point you to providers, though the policy is yours to choose.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_trip(
        "Retiree Travel Canada Luxury Journeys",
        "Private retiree luxury journeys in Canada with no departures before 8:30am, accessibility briefings, medical notes, and the same guide throughout.",
        "Retirees and senior travellers", "experiences/retirement-travel/")],
)

# ---------------------------------------------------------------- corporate and MICE

MICE = dict(
    path="experiences/corporate-mice/",
    title="Canada Corporate Retreat Luxury | MICE Canada Retreats",
    desc="Canada corporate retreat luxury for groups of six to thirty: private mountain and coastal retreats, one point of contact, and a fallback for every day.",
    crumb=[("Home", "/"), ("Experiences", "/experiences/"), ("Corporate and MICE", "/experiences/corporate-mice/")],
    og_image="/images/exp-mice-hero.jpg",
    hero=dict(
        eyebrow="Corporate and MICE",
        h1="Canada Corporate Retreat Luxury: Impressive, Seamless, Nothing Goes Wrong",
        sub="One point of contact from brief to debrief. Private mountain and coastal retreats for six to thirty, with a fallback venue for every programme day and a transport manifest for every transfer.",
        img="/images/exp-mice-hero.jpg",
        alt="Canada corporate retreat luxury: a leadership group meeting in a private mountain lodge",
        cta="Schedule A 30 Minute Brief",
    ),
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <p>When a leadership team travels, one fear runs underneath everything: something going wrong on the organiser's watch, in front of the chief executive or the client. So we start from the opposite end to a leisure journey and work outward from execution. One point of contact, one plan, and a written contingency for weather, closures, and wildfire smoke at every stage.</p>
        <p>What the group remembers afterwards is the part we do not compromise: a private dinner in a place no group has dined, a mountain morning that resets a room full of people, and a programme that leaves the team closer than any conference hotel could manage.</p>
      </div>
      <figure class="shot shot-wide">
        <img src="/images/exp-mice-lodge.jpg" width="1400" height="800" alt="Private mountain lodge prepared for a corporate retreat in the Canadian Rockies" loading="lazy">
        <figcaption>Banff and Lake Louise handle larger groups; Calgary is the gateway, ninety minutes from the park gate.</figcaption>
      </figure>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Programme overview</div>
        <h2 class="section-title">Three to five days, structured around outcomes</h2>
      </div>
      <div class="grid g-3">
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-mice-day1.jpg" width="600" height="400" alt="Team arriving at a private lodge by private transfer from Calgary" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Day one: arrival and reset</h3><p>Private transfers from Calgary, Vancouver, or Toronto, a briefing on the ground, and an evening that gets everyone out of the airport mindset.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-mice-day2.jpg" width="600" height="400" alt="Strategy session in a lodge with mountain views behind" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Day two: the work, in a room worth sitting in</h3><p>Morning sessions with AV support for hybrid attendees, an outdoor afternoon that changes the conversation, and dinner together.</p></div>
        </article>
        <article class="card">
          <figure class="shot shot-card"><img src="/images/exp-mice-day3.jpg" width="600" height="400" alt="Private dinner setting in a location no group has dined" loading="lazy"></figure>
          <div class="body"><h3 class="card-title">Day three: the thing they will talk about</h3><p>A private guided day, a dinner in a place no group has dined, and reflection built into the evening rather than left to the flight home.</p></div>
        </article>
      </div>
    </div>
  </section>

  <section class="band-spruce on-dark">
    <div class="wrap">
      <div class="split">
        <div>
          <div class="lab eyebrow">Logistics assurance</div>
          <h2 class="section-title">What the organiser needs in writing</h2>
          <ul class="ticks">
            <li>One point of contact from brief to debrief, reachable throughout</li>
            <li>A fallback venue and sequence for weather, closures, or wildfire smoke</li>
            <li>Airport-to-lodge private transfers from Calgary, Vancouver, or Toronto</li>
            <li>Transport manifests for every movement of the group</li>
            <li>AV support arranged for hybrid sessions, tested before the group arrives</li>
            <li>Multi-day mountain and coastal retreats for groups up to thirty</li>
          </ul>
        </div>
        <figure class="shot shot-wide">
          <img src="/images/exp-mice-logistics.jpg" width="1400" height="800" alt="Guide and organiser reviewing the transport manifest before the group departs" loading="lazy">
          <figcaption>Manifests, timings, and a second plan for every day.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">What this delivers</div>
        <h2 class="section-title">Outcomes, stated before experiences</h2>
      </div>
      <div class="prose">
        <p>Team cohesion earned in a canoe rather than a conference room. Leadership alignment reached over a long table at the end of a day that took everyone out of their inbox. And cultural capital: the retelling that raises how the team talks about where it works and who it works with. We will bring the value argument against Whistler, Aspen, or the Alps to the briefing, checked at the current exchange rate rather than asserted.</p>
      </div>
      <div class="grid g-3">
        <figure class="shot shot-card"><img src="/images/exp-mice-strip-1.jpg" width="600" height="400" alt="Guided canoe session for a corporate group in the Rockies" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/exp-mice-strip-2.jpg" width="600" height="400" alt="Private dinner table set for a corporate group in a heritage venue" loading="lazy"></figure>
        <figure class="shot shot-card"><img src="/images/exp-mice-strip-3.jpg" width="600" height="400" alt="Hybrid session with AV support in a mountain lodge" loading="lazy"></figure>
      </div>
    </div>
  </section>

  <section class="band-glacier">
    <div class="wrap">
      <div class="callout">
        <div class="lab">Investment</div>
        <p>Retreats of this scope are quoted per programme, after a short brief, because the variables are the group size, the season, and the properties. We will give you a range at the briefing and a precise figure once the shape is settled. No price grids, ever.</p>
      </div>
    </div>
  </section>
""",
    cta_band=("/images/exp-mice-cta.jpg", "Evening light on a private mountain lodge terrace set for a corporate dinner",
              "Schedule A 30 Minute Brief", "Tell us the group, the dates, and the outcome you need, and we will bring a programme.", "Schedule A 30 Minute Brief"),
    faq=[
        ("What group sizes can you handle for a corporate retreat in Canada?",
         "<p>Six to thirty guests, across multi-day mountain and coastal retreats. Banff and Lake Louise handle larger groups comfortably, and the BC coast suits smaller leadership groups where the point is space rather than scale.</p>"),
        ("What happens if weather or wildfire smoke disrupts the programme?",
         "<p>We write a fallback venue and a fallback sequence into every programme before you travel, so a disruption changes the plan rather than the outcome. Wildfire season runs July to September, and it is planned around rather than hoped away.</p>"),
        ("Do you support hybrid sessions for remote attendees?",
         "<p>Yes. AV support is arranged for hybrid sessions and tested before the group arrives. We will tell you plainly what the venue can and cannot do rather than promising a seamless link we have not verified.</p>"),
    ],
    extra_nodes=lambda sg: [sg.node_trip(
        "Canada Corporate Retreat and MICE Programmes",
        "Private corporate retreats and MICE programmes in Canada for six to thirty guests, with one point of contact, logistics assurance, and a fallback venue for every day.",
        "Corporate and MICE groups", "experiences/corporate-mice/")],
)

ALL = [HUB, PRIVATE, HONEYMOON, FAMILY, RETIREE, MICE]