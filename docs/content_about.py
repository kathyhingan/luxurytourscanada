"""About page. Credibility without invented detail: the road-experience facts
come from the brand packet verbatim, and no first-hand claim is attributed to a
named person whose name has not been confirmed.
"""

ABOUT = dict(
    path="about/",
    title="About Luxury Tours Canada | 27 Years of Slow Travel",
    desc="About Luxury Tours Canada: private journeys designed by people who crossed the country slowly. No fixed packages, eight guests maximum, honest seasons.",
    crumb=[("Home", "/"), ("About", "/about/")],
    og_image="/images/about-hero.svg",
    hero=dict(
        eyebrow="About",
        h1="About Luxury Tours Canada: Built on 27 Years of Crossing It Slowly",
        sub="Thirteen provinces and territories, the longest coastline of any country on earth, and a designer who has crossed it six times with a thumb out, once on a bicycle.",
        img="/images/about-hero.svg",
        alt="About Luxury Tours Canada: the Trans-Canada Highway crossing the Rockies at dusk",
        cta="Begin Your Journey",
    ),
    body="""
  <section class="band-white">
    <div class="wrap">
      <div class="prose lede">
        <p>Luxury Tours Canada designs private, multi-destination journeys for a maximum of eight guests. No fixed packages, no group departures, and no two journeys alike. The company exists because of a simple observation: Canada rewards slow travel and punishes the other kind, and almost nobody sells it honestly.</p>
      </div>
    </div>
  </section>

  <section class="band-deep on-dark">
    <div class="wrap">
      <div class="split-wide">
        <div>
          <div class="lab eyebrow">The credibility</div>
          <blockquote>Six crossings of Canada by thumb, starting at sixteen on the Trans-Canada, and 700 kilometres by bicycle from Kingston to Essex. The road is the resume.</blockquote>
          <p class="small" style="margin-top:16px">The routes we sell are routes we know personally: the BC coast, Salt Spring Island, Tofino, Jasper, Banff, the Rockies, and the Ontario lakeshore from Kingston to Essex. Where we recommend something we have not done ourselves, we say so and we verify it before you travel.</p>
        </div>
        <figure class="shot shot-hero">
          <img src="/images/about-portrait.svg" width="800" height="1000" alt="The road-experience behind Luxury Tours Canada: a highway and a bicycle" loading="lazy">
        </figure>
      </div>
    </div>
  </section>

  <section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">How we work</div>
        <h2 class="section-title">What working with us looks like</h2>
      </div>
      <div class="prose">
        <p>Every journey begins with a conversation, and every journey is designed from a blank page. The first call sets the segment, the season, the pace, and the party; the itinerary that follows states drive times honestly, plans wildfire season rather than hoping about it, and carries a fallback for every outdoor day, because mountain weather turns by the hour.</p>
        <ul class="ticks">
          <li><strong>Private, always.</strong> Private vehicles, private boats, and a guide who stays with the journey.</li>
          <li><strong>Honest, deliberately.</strong> We will tell you Banff is crowded in July, that April in the Rockies is mud, and that the Pacific is cold in every month.</li>
          <li><strong>Small, by design.</strong> A maximum of eight guests per journey, because intimacy is the product.</li>
          <li><strong>Season first.</strong> Canadian travel is planned around its seasons, and we will move your region before we move your dates.</li>
        </ul>
        <h2>What we do not do</h2>
        <p>No group tours, no fixed packages, no price grids, and no hotel recommendation sections dressed up as guides. We do not publish prices because every journey is priced on what is actually in it, after a call, and we do not recommend specific properties in public because the right property depends on the party, the season, and the budget, not on a list.</p>
        <h2>Family travel, stated plainly</h2>
        <p>We have children ourselves, so we know what travelling with them actually takes. Our own family does not travel on client journeys: local guides and vetted childminders look after the family-facing details on the ground. Car seats are required by law and pre-sourced, wildlife briefings happen before every walk, and the cold-water rules on this coast are treated as the safety matters they are.</p>
        <h2>A new brand, honestly</h2>
        <p>Luxury Tours Canada is new, and we will not pretend otherwise with borrowed testimonials. What we can show you is specificity: itineraries with named places and real drive times, seasons described as they are, and operational detail that only comes from having done the trips. Our journeys also draw on years of designing private luxury travel in the Philippines for <a href="https://luxurytoursphilippines.com/">Arkipelago Luxury Tours Philippines</a>, our sister brand, where the same standard applies to a very different archipelago.</p>
        <p>If that is the kind of operator you want planning your Canada journey, the first step is a twenty minute conversation.</p>
      </div>
    </div>
  </section>
""",
    faq=[
        ("Who is behind Luxury Tours Canada?",
         "<p>A small team that has spent 27 years travelling Canada personally, from six crossings of the country by thumb to 700 kilometres by bicycle along the Ontario lakeshore, backed by years of designing private luxury journeys in the Philippines through our sister brand.</p>"),
        ("Why do you not publish prices?",
         "<p>Because there is no package to price. Every journey is designed around one party, and the cost depends on the season, the properties, and what is actually in the itinerary. We give you a range after a short call and a precise figure when the shape is settled.</p>"),
        ("Which parts of Canada do you cover?",
         "<p>The three regions we know personally: the BC coast around Tofino and Salt Spring Island, the Canadian Rockies from Jasper to Banff and Yoho, and the Ontario lakeshore from Kingston to Essex County. If your plans fall outside those regions, we will tell you plainly.</p>"),
    ],
)

ALL = [ABOUT]