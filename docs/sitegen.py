"""Luxury Tours Canada site generator.

Shell (nav, footer, head, FAQ, schema) extracted once from the approved homepage.
Content modules supply title, meta, hero, body HTML and FAQ pairs; this module
renders the page, and builds FAQPage JSON-LD from the SAME strings that render
visibly, so markup and schema can never drift apart.

Run:  python3 docs/build_all.py   (from the repo root)
"""

import json, os, html

SITE = "https://luxurytourscanada.com"
BRAND = "Luxury Tours Canada"
FORM_ACTION = "https://script.google.com/macros/s/AKfycbwRYj-L08AOiqzyHD7jX8lJhyFTPxzXseriRz0046zeA5ySPXPGwLdQ_vShRWoGwCzf/exec"


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- head

def head(title, desc, path, og_type="website", og_image="/images/home-hero.jpg", jsonld=None):
    """path like 'destinations/tofino-private-tour/' ('' for home)."""
    url = SITE + "/" + path
    graph = json.dumps(jsonld or [], indent=2)
    return f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
<!-- 1. Analytics: NEW IDs for this site, never the Arkipelago IDs -->
<!-- Google Analytics: [GA ID TBD] -->
<!-- Microsoft Clarity: [CLARITY ID TBD] -->
<!-- 2. Favicon -->
<link rel="icon" type="image/svg+xml" href="/favicon.jpg">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<!-- 3. SEO -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:site_name" content="{BRAND}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}{og_image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{graph}
</script>
</head>"""


# ---------------------------------------------------------------- shell

NAV_ITEMS = [
    ("Destinations", "/destinations/"),
    ("Experiences", "/experiences/"),
    ("Journal", "/journal/"),
    ("About", "/about/"),
]


def header():
    links = "\n      ".join(f'<a href="{h}">{t}</a>' for t, h in NAV_ITEMS)
    return f"""<a class="skip" href="#main">Skip to content</a>

<header class="site-head">
  <div class="bar">
    <a class="wordmark" href="/">LUXURY TOURS CANADA<span>Private Journeys, Coast to Coast</span></a>
    <nav class="site-nav" aria-label="Main">
      {links}
      <a class="btn btn-sm" href="/#begin">Begin Your Journey</a>
    </nav>
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="navDrawer" onclick="toggleMenu()">Menu</button>
  </div>
  <div class="drawer" id="navDrawer">
    <a href="/destinations/">Destinations</a>
    <a href="/experiences/">Experiences</a>
    <a href="/journal/">Journal</a>
    <a href="/about/">About</a>
    <a href="/#begin">Begin Your Journey</a>
  </div>
</header>"""



JOURNEY_FORM = """<section class="band-white" id="begin" aria-label="Begin your journey">
  <div class="wrap" style="max-width:860px">
    <div class="section-head" style="text-align:center">
      <div class="lab eyebrow">Start here</div>
      <h2 class="section-title">Begin Your Journey</h2>
      <p class="lede" style="max-width:640px;margin:0 auto 6px">Every Luxury Tours Canada journey begins with a conversation. No commitment, no package pricing, no two journeys alike.</p>
    </div>
    <div class="form-wrap">
      <div class="promise-item"><span class="promise-dot"></span><span>We respond within 24 hours, always.</span></div>
      <div class="promise-item"><span class="promise-dot"></span><span>Every inquiry is read and answered personally.</span></div>
      <div class="promise-item"><span class="promise-dot"></span><span>No fixed packages and no price grids. Ever.</span></div>
      <iframe name="formSink" style="display:none" aria-hidden="true" tabindex="-1" title="Form submission target"></iframe>
      <form id="journeyForm" action="{FORM_ACTION}" method="POST" target="formSink" onsubmit="submitForm(event)" style="margin-top:18px">
        <input type="hidden" name="source" value="ltc-page">
        <input type="hidden" name="page" id="formPage">
        <input type="hidden" name="timestamp" id="formTimestamp">
        <input type="hidden" name="quiz_who" id="quizWho" value="">
        <input type="hidden" name="quiz_draw" id="quizDraw" value="">
        <input type="hidden" name="quiz_pace" id="quizPace" value="">
        <input type="hidden" name="quiz_dest" id="quizDest" value="">
        <input type="hidden" name="quiz_luxury" id="quizLuxury" value="">
        <input type="hidden" name="quiz_archetype" id="quizArchetype" value="">
        <div class="form-group">
          <label class="f-label" for="fieldName">Your name</label>
          <input class="form-input" type="text" id="fieldName" name="name" placeholder="First and last name" required>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="f-label" for="fieldEmail">Email address</label>
            <input class="form-input" type="email" id="fieldEmail" name="email" placeholder="your@email.com" required>
          </div>
          <div class="form-group">
            <label class="f-label" for="fieldType">Journey type</label>
            <select class="form-select" id="fieldType" name="journey_type">
              <option value="">Select...</option>
              <option>Private Journey</option>
              <option>Honeymoon</option>
              <option>Engagement Proposal</option>
              <option>Family with Children</option>
              <option>Retiree Journey</option>
              <option>Corporate / MICE</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label class="f-label" for="fieldPhone">Phone number</label>
          <input class="form-input" type="tel" id="fieldPhone" name="phone" placeholder="Any country, include the country code" pattern="[+0-9][0-9 ()\-.]{{6,}}" title="Enter your full number with country code, for example +1 604 555 0142" inputmode="tel" required>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="f-label" for="fieldDates">Approximate dates</label>
            <input class="form-input" type="text" id="fieldDates" name="dates" placeholder="For example, September 2027">
          </div>
          <div class="form-group">
            <label class="f-label" for="fieldGroup">Group size</label>
            <input class="form-input" type="text" id="fieldGroup" name="group_size" placeholder="For example, 2 adults, 1 child aged 6">
          </div>
        </div>
        <div class="form-group">
          <label class="f-label" for="fieldMessage">Tell us what you are imagining</label>
          <textarea class="form-input" id="fieldMessage" name="message" placeholder="Destinations, pace, what matters most, anything on your mind..."></textarea>
        </div>
        <button class="btn" type="submit" id="formSubmitBtn">Request My Journey Consultation</button>
        <p class="form-note">We respond within 24 hours. Every inquiry is handled personally.</p>
        <div class="form-ok" id="formOk" role="status"><strong>Received.</strong> Thank you. We will come back to you within 24 hours, personally.</div>
      </form>
    </div>
  </div>
</section>
"""

FOOTER = JOURNEY_FORM + """<footer class="site-foot">
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="brandline">LUXURY TOURS CANADA</div>
        <p style="margin-top:10px;font-size:16px">Private journeys, coast to coast. Bespoke, multi-destination luxury travel across Canada, designed by people who have crossed it the slow way.</p>
      </div>
      <div>
        <div class="lab">Destinations</div>
        <ul>
          <li><a href="/destinations/tofino-private-tour/">Tofino</a></li>
          <li><a href="/destinations/salt-spring-island-private-tour/">Salt Spring Island</a></li>
          <li><a href="/destinations/jasper-private-tour/">Jasper</a></li>
          <li><a href="/destinations/banff-yoho-private-tour/">Banff and Yoho</a></li>
          <li><a href="/destinations/prince-edward-county-private-tour/">Prince Edward County</a></li>
          <li><a href="/destinations/niagara-on-the-lake-private-tour/">Niagara-on-the-Lake</a></li>
        </ul>
      </div>
      <div>
        <div class="lab">Experiences</div>
        <ul>
          <li><a href="/experiences/private-tours/">Private Journeys</a></li>
          <li><a href="/experiences/honeymoon-proposals/">Honeymoons and Proposals</a></li>
          <li><a href="/experiences/family-tours/">Family Travel</a></li>
          <li><a href="/experiences/retirement-travel/">Retiree Journeys</a></li>
          <li><a href="/experiences/corporate-mice/">Corporate and MICE</a></li>
        </ul>
      </div>
      <div>
        <div class="lab">Company</div>
        <ul>
          <li><a href="/about/">About</a></li>
          <li><a href="/journal/">Journal</a></li>
          <li><a href="/#begin">Begin Your Journey</a></li>
        </ul>
      </div>
    </div>
    <div class="bottom">&copy; 2026 Luxury Tours Canada. All rights reserved.</div>
  </div>
</footer>

<script src="/assets/site.js"></script>"""


# ---------------------------------------------------------------- pieces

def crumbs(trail):
    """trail: list of (name, href). Last item is the current page."""
    parts = []
    for i, (name, href) in enumerate(trail):
        if i == len(trail) - 1:
            parts.append(f'<span aria-current="page">{esc(name)}</span>')
        else:
            parts.append(f'<a href="{href}">{esc(name)}</a>')
    joined = " &rsaquo; ".join(parts)
    return f"""<nav class="crumbs" aria-label="Breadcrumb"><div class="inner lab">{joined}</div></nav>"""


def hero(eyebrow, h1, sub, img, alt, cta_text="Begin Your Journey", cta_href="/#begin", short=False, eager=True):
    eager_attr = ' fetchpriority="high"' if eager else ' loading="lazy"'
    cls = "hero hero-short" if short else "hero"
    cta = f'<p><a class="btn" href="{cta_href}">{esc(cta_text)}</a></p>' if cta_text else ""
    return f"""<section class="{cls}" aria-label="Introduction">
    <img src="{img}" width="1600" height="900" alt="{esc(alt)}"{eager_attr}>
    <div class="veil"></div>
    <div class="inner">
      <div class="lab eyebrow">{esc(eyebrow)}</div>
      <h1>{h1}</h1>
      <p class="sub">{sub}</p>
      {cta}
    </div>
  </section>"""


def bestfor(chips, label="Best for"):
    inner = "".join(f'<span class="chip lab">{esc(c)}</span>' for c in chips)
    return f"""<section class="bestfor"><div class="wrap"><div class="lab">{esc(label)}</div><div class="chips">{inner}</div></div></section>"""


def shot(img, w, h, alt, caption=None, cls="shot-wide", lazy=True):
    lazy_attr = ' loading="lazy"' if lazy else ""
    cap = f"<figcaption>{esc(caption)}</figcaption>" if caption else ""
    return f"""<figure class="shot {cls}">
    <img src="{img}" width="{w}" height="{h}" alt="{esc(alt)}"{lazy_attr}>
    {cap}
  </figure>"""


def cta_band(img, alt, heading="Begin Your Journey", line="Tell us what you are imagining. We will come back within 24 hours.", btn="Begin Your Journey"):
    return f"""<section class="cta" aria-label="Closing invitation">
    <img src="{img}" width="1600" height="900" alt="{esc(alt)}" loading="lazy">
    <div class="veil"></div>
    <div class="inner">
      <h2>{esc(heading)}</h2>
      <p>{esc(line)}</p>
      <p><a class="btn" href="/#begin">{esc(btn)}</a></p>
    </div>
  </section>"""


def faq_block(pairs):
    """pairs: list of (question, answer_html). Renders accessible accordions.
    The same strings are used for FAQPage schema by faq_schema()."""
    items = []
    for i, (q, a) in enumerate(pairs):
        open_attr = " open" if i == 0 else ""
        items.append(f"""<details class="faqitem"{open_attr}>
      <summary>{esc(q)}</summary>
      <div class="ans">{a}</div>
    </details>""")
    body = "\n    ".join(items)
    return f"""<section class="band-white">
    <div class="wrap">
      <div class="section-head">
        <div class="lab eyebrow">Questions we are asked</div>
        <h2 class="section-title">Frequently asked questions</h2>
      </div>
      <div class="faq">
    {body}
      </div>
    </div>
  </section>"""


# ---------------------------------------------------------------- schema

def node_agency():
    return {
        "@type": "TouristAgency",
        "@id": SITE + "/#organization",
        "name": BRAND,
        "url": SITE,
        "logo": SITE + "/images/logo.png",
        "description": "Bespoke luxury tours and private guided journeys across Canada, from the BC coast to the Rockies and the Ontario lakeshore.",
        "areaServed": {"@type": "Country", "name": "Canada"},
        "priceRange": "$$$",
    }


def node_breadcrumb(trail):
    items = []
    for i, (name, href) in enumerate(trail):
        items.append({"@type": "ListItem", "position": i + 1, "name": name,
                      "item": (SITE + href) if href else SITE + "/"})
    return {"@type": "BreadcrumbList", "itemListElement": items}


def node_attraction(name, desc, path, lat, lng, image, tourist_types):
    return {
        "@type": "TouristAttraction",
        "name": name,
        "description": desc,
        "url": SITE + "/" + path,
        "image": SITE + image,
        "touristType": tourist_types,
        "geo": {"@type": "GeoCoordinates", "latitude": str(lat), "longitude": str(lng)},
        "containedInPlace": {"@type": "Country", "name": "Canada"},
    }


def node_trip(name, desc, tourist_type, path):
    return {
        "@type": "TouristTrip",
        "name": name,
        "description": desc,
        "url": SITE + "/" + path,
        "provider": {"@id": SITE + "/#organization"},
        "touristType": tourist_type,
        "offers": {"@type": "Offer", "priceCurrency": "USD",
                   "description": "Custom pricing: contact for a personalised quote"},
    }


def node_article(headline, desc, path, image, date_published, author_name):
    return {
        "@type": "Article",
        "headline": headline,
        "description": desc,
        "image": SITE + image,
        "datePublished": date_published,
        "dateModified": date_published,
        "url": SITE + "/" + path,
        "author": {"@type": "Person", "name": author_name,
                   "url": SITE + "/about/"},
        "publisher": {"@type": "Organization", "name": BRAND, "url": SITE,
                      "logo": {"@type": "ImageObject", "url": SITE + "/images/logo.png"}},
    }


def node_faq(pairs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": _strip_html(a)}}
            for q, a in pairs
        ],
    }


def _strip_html(s):
    import re
    return re.sub(r"<[^>]+>", "", s).strip()


def graph(*nodes):
    out = [{"@context": "https://schema.org"}]
    out.extend(n for n in nodes if n)
    return out


# ---------------------------------------------------------------- page

def page(path, title, desc, crumb_trail, hero_html, body_html, faq_pairs=None,
         extra_nodes=None, og_type="website", og_image="/images/home-hero.jpg",
         with_breadcrumb_schema=True, date_line=None):
    """Render a full page. path: 'destinations/x/' (folder with index.html)."""
    nodes = [node_agency()]
    if with_breadcrumb_schema and crumb_trail:
        nodes.append(node_breadcrumb(crumb_trail))
    for n in (extra_nodes or []):
        nodes.append(n)
    if faq_pairs:
        nodes.append(node_faq(faq_pairs))

    date_html = f'<div class="crumbs"><div class="inner lab">{esc(date_line)}</div></div>' if date_line else ""
    html_out = "\n".join([
        head(title, desc, path, og_type=og_type, og_image=og_image,
             jsonld=graph(*nodes)),
        "<body>",
        header(),
        crumbs(crumb_trail) if crumb_trail else "",
        '<main id="main">',
        hero_html,
        body_html,
        faq_block(faq_pairs) if faq_pairs else "",
        date_html,
        "</main>",
        FOOTER,
        "</body>",
        "</html>",
    ])
    target = os.path.join(path, "index.html") if path else "index.html"
    os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(html_out)
    return target