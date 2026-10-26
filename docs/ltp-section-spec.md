# LTP Page Section Architecture - Extraction Spec for the LTC Rebuild

Source of truth: `arkipelago` repo (read-only), 11 pages extracted 2026-10-27.
Purpose: Kathy wants every LTC page restructured to match this architecture. This
document is the input for that rebuild. Order and component completeness are
authoritative; prose is deliberately minimal.

Conventions used below: headings are VERBATIM (markup abbreviations noted:
`<br>` line breaks, `<em>`/`<span class="accent">` emphasis inside headings).
"reveal" = `.reveal` / `.reveal-delay-1..3` classes animated by IntersectionObserver.

---

## 1. index.html (homepage, 1341 lines)

### Ordered skeleton

1. `<nav id="nav">` - fixed top nav, transparent over hero, gains `.scrolled` bg at scrollY>80.
   - Logo block: "ARKIPELAGO" + sub "Luxury Tours Philippines".
   - 5 dropdown `<li class="nav-item-dropdown">` groups + plain links: Destinations (11 sub-links), Tour Types (14 sub-links + "All Tour Types"), Experiences (Day Tours, Private Journeys, Honeymoons & Proposals, Family Tours, Retiree Journeys, Corporate & MICE + 4 indented "↳" corporate sub-pages), "Find My Journey" (/#quiz), Journal, Explorer Map, Our Philosophy (dropdown: Our Philosophy, Our Commitment).
   - CTA stack: 2 buttons - "Begin Your Journey" (outline, onclick → /#begin) and "For Filipino Joiners" (gold fill, → /arkipelago-weekends/).
   - Hamburger (3 spans) for mobile.
2. `<div id="navDrawer" class="nav-drawer">` - fullscreen mobile drawer mirroring the nav with "↳" sub-items (indented, smaller, lower opacity) + 2 full-width drawer CTAs ("Begin Your Journey →", gold "For Filipino Joiners →"). Toggle locks body scroll.
3. `<section class="hero">` - split hero.
   - Left: eyebrow "Bespoke Multi-Destination Journeys"; H1 `The Philippines,<br>as it was always<br>meant to be <em>experienced.</em>`; subtitle paragraph; 2 actions (`.btn-primary` "Begin Your Journey" → scrollToForm(); `.btn-ghost` "Explore destinations" → #destinations).
   - Right: branded inline SVG Philippines map (grid pattern, gold island paths, glowing destination dots with uppercase labels PALAWAN/BATANES/BAGUIO/SIARGAO/BOHOL/BUKIDNON/VIGAN/P. GALERA, footer text "7,641 ISLANDS · PHILIPPINE ARCHIPELAGO").
   - Decorative vertical text "Arkipelago Luxury Tours · Est. 2025"; scroll indicator (line + "Scroll").
4. `<section class="quiz-section" id="quiz">` - 5-step interactive quiz. FULL DETAIL BELOW.
5. `<section style="background:var(--navy)">` (philosophy band) - label "Our Philosophy"; H2 `Every client we serve is paying to <em>not think about logistics.</em>`; 2 body paragraphs. Right column: 4-stat grid (`.phil-stat`): "7,641 Islands in the Philippine Archipelago", "8 Maximum guests per private journey", "100% Custom, no two journeys are identical", "30+ Years of personal journeys across the Philippines, deeply personal, deeply local".
6. `<section class="how-it-works" id="how-it-works">` - label "How It Works"; H2 `Four steps. One journey.<br>Everything handled.`; subtitle. 4 numbered `.hiw-step` cards: 01 "Tell Us What You're Imagining", 02 "We Respond Within 24 Hours", 03 "We Design Your Journey", 04 "Your Journey Is Confirmed" (each: num + label + body). CTA row: btn-primary "Begin Your Journey" + note "No commitment until you say so. Every inquiry handled personally."
7. `<section class="destinations" id="destinations">` - section-header (label "Where We Take You", H2 "The Destinations", "View all →" link). Horizontal card carousel `.hc-carousel` of 14 `.hc-card` link cards (bg image, number, region tag, h3 title, desc): 01 El Nido, 02 Coron, 03 Port Barton, 04 Palawan, 05 Batanes, 06 Vigan, 07 Ilocos, 08 Baguio, 09 Sagada, 10 Puerto Galera, 11 Bohol, 12 Cebu, 13 Bukidnon Highlands, 14 Siargao. Prev/next arrow buttons + JS-generated dot indicators; touch swipe + mouse drag.
8. `<section class="experiences" id="experiences">` - section-header (label "Who We Design For", H2 "Every Journey, Entirely Yours"). 5 `.exp-card` grid cards (emoji icon, title, body, CTA link): Private Journeys / Honeymoons & Proposals / Families with Children / Retiree Journeys / Corporate & MICE.
9. `<section class="quote-section">` - visually-hidden H2 "Why Choose Arkipelago for Private Guided Tours Philippines" (SEO); quote mark; 3-line pull quote `We don't sell the Philippines.<br>We give you access to the version of it<br>that <em>most people never see.</em>`; attribution "– Arkipelago, Founded 2025".
10. `<section class="journey-cta" id="begin">` - two-column CTA + form (full detail in Forms section). Left: label "Start Here", H2 "Begin Your Journey", body, 4 `.promise-item` rows with dots. Right: hidden iframe `formSink` + `#journeyForm`.
11. `<footer>` - 4 columns. Col 1 brand: "ARKIPELAGO" / "Luxury Tours Philippines" / tagline "Curated. Sovereign. Unforgettable." Col 2 "Experiences" (6 links). Col 3 "Destinations" (11 links). Col 4 "Arkipelago" (Explorer Map, Arkipelago Weekends, Our Philosophy, Journal, Begin Your Journey → scrollToForm). Footer bottom: "© 2026 Arkipelago Luxury Tours Philippines. All rights reserved." + coordinates "9°30′N 118°30′E · Philippine Archipelago".

### Homepage quiz (5 questions) - complete

Structure: `.quiz-eyebrow` "Find Your Journey"; `.quiz-title` H2 "What kind of traveller are you?"; `.quiz-subtitle` "Five questions. Enough for us to begin imagining your journey before you even write to us."; progress bar of 5 segments (`#qp0..#qp4`, states active/done); 5 `.quiz-step` panels (`#step0..#step4`, only one `.active`); result panel `#quizResult` (`.active` when shown).

Each option: `<div class="quiz-option" data-value="X" onclick="sel(this,STEP)">` containing emoji `.opt-icon`, `.opt-label`, `.opt-desc`. Selecting highlights it, stores `A[step]=data-value`, enables Continue.

Step 1 (step0) - "This journey, <span>who is it for?</span>" (1 of 5; no Back button):
- solo - 🧳 "Just me" / "A solo journey on my own terms"
- couple - 💑 "Me and my partner" / "Honeymoon, anniversary, or simply the two of us"
- family - 👨‍👩‍👧‍👦 "Family with children" / "We travel together, kids (and sometimes pets) included"
- retire - 🌺 "Retirement journey" / "The trip I've been planning for decades, finally taken right"
- corporate - 🏛️ "My team or company" / "Corporate retreat, MICE, or incentive travel"

Step 2 (step1) - "What draws you to <span>the Philippines</span> above anywhere else?" (2 of 5):
- nature - 🌊 "The natural world" / "Islands, ocean, wildlife, somewhere truly untouched"
- culture - 🏛️ "Culture & heritage" / "History, food, local life, I travel to understand a place"
- romance - 🌅 "Romance & beauty" / "I want somewhere that takes my breath away"
- adventure - 🤿 "Adventure & activity" / "Diving, surfing, hiking, I want to be active"
- slow - 🌿 "Rest & restoration" / "I've earned this. I want to do nothing, beautifully"

Step 3 (step2) - "How long are you imagining, and <span>what pace feels right</span>?" (3 of 5):
- short - ⚡ "4–6 days, well-packed" / "Limited time, but I want to see a lot"
- balanced - 🗓️ "7–10 days, balanced" / "A mix of exploring and breathing"
- long - 🌙 "11–14 days, unhurried" / "I want to settle in. No rushing."
- extended - 🗺️ "Two weeks or more" / "I want to genuinely explore the archipelago"

Step 4 (step3) - "Which part of the Philippines <span>calls to you</span> most?" (4 of 5):
- palawan - 🏝️ "Palawan, Coron & Port Barton" / "Shipwrecks, karst lakes, the Palawan nobody talks about"
- visayas - 🐋 "Bohol, Cebu & Siargao" / "Whale sharks, chocolate hills, island life"
- north - 🌾 "Batanes, Baguio & Vigan" / "Cool highlands, heritage, the other Philippines"
- mindanao - 🏔️ "Bukidnon & Mindanao" / "Highland plateaus, tribal culture, the undiscovered south"
- multi - ✈️ "Show me everything" / "I want a journey that spans the whole archipelago"

Step 5 (step4) - "When you think of <span>luxury</span>, what does it actually mean to you?" (5 of 5; final button "See My Journey →" calls showResult()):
- privacy - 🔒 "Total privacy" / "No other guests. Just us and the place."
- service - 🤍 "Flawless service" / "Every need anticipated before I think to ask"
- access - 🗝️ "Access to the unreachable" / "Places money can't simply buy, you need to know someone"
- comfort - 🛏️ "Exceptional comfort" / "The finest rooms, the best beds, nothing roughing it"

Result panel: `#rBadge` badge, `<h3 class="result-title" id="rTitle">`, `#rDesc` paragraph, CTA row ("Begin This Journey" → scrollToForm(); "Retake the quiz" → restartQuiz()).

Archetype decision (showResult):
```
type = 'explorer' (default)
if who==='corporate' → 'corporate'
else if who==='family' → 'family'
else if who==='retire' → 'retire'
else if who==='couple' and draw in {romance,slow} → 'romance'
else if draw==='culture' → 'heritage'
else if draw==='adventure' → 'explorer'
```
Six archetypes (badge / title / desc template / seg):
- romance - "Honeymoon & Proposal Journey" - "You deserve a moment that stops time." - seg "Honeymoon"
- family - "Family Journey" - "Luxury travel that works for every member of your family." - seg "Family with Children"
- retire - "Retiree Journey" - "The journey you've been planning for decades. Finally, done right." - seg "Retiree Journey"
- corporate - "Corporate & MICE Journey" - "A retreat your team will talk about for years." - seg "Corporate / MICE"
- heritage - "Cultural Heritage Journey" - "The Philippines most travellers never understand." - seg "Private Journey"
- explorer - "Private Discovery Journey" - "The Philippines no travel guide has ever shown you." - seg "Private Journey"

Each desc is a sentence template interpolating `paceMap` (short→"4–6 days", balanced→"7–10 days", long→"11–14 days", extended→"2+ weeks"), `destMap` (palawan→"Coron & Port Barton, Palawan", visayas→"Bohol, Cebu & Siargao", north→"Northern Philippines", mindanao→"Bukidnon & Mindanao", multi→"a multi-island journey"), `luxMap` (privacy→"total privacy", service→"flawless service", access→"exclusive access", comfort→"exceptional comfort").

Quiz state → form hidden fields (showResult tail):
- `#quizWho` (name=quiz_who) ← whoLabels: solo→"Just me (solo)", couple→"Me and my partner", family→"Family with children", retire→"Retirement journey", corporate→"Team / corporate"
- `#quizDraw` (quiz_draw) ← drawLabels: nature→"The natural world", culture→"Culture & heritage", romance→"Romance & beauty", adventure→"Adventure & activity", slow→"Rest & restoration"
- `#quizPace` (quiz_pace) ← paceLabels: short→"4–6 days, well-packed", balanced→"7–10 days, balanced", long→"11–14 days, unhurried", extended→"Two weeks or more"
- `#quizDest` (quiz_dest) ← destLabels: palawan→"Coron & Port Barton, Palawan", visayas→"Bohol, Cebu & Siargao", north→"Batanes, Baguio & Vigan", mindanao→"Bukidnon & Mindanao", multi→"Show me everything (multi-island)"
- `#quizLuxury` (quiz_luxury) ← luxLabels: privacy→"Total privacy", service→"Flawless service", access→"Access to the unreachable", comfort→"Exceptional comfort"
- `#quizArchetype` (quiz_archetype) ← r.badge (the archetype badge string)
- Additionally the visible `journeyTypeSelect` is pre-selected to `r.seg` by matching option text.
- `restartQuiz()` nulls `A`, clears all six hidden fields, resets steps/progress/selections.

Navigation behavior: `nxt()`/`prv()` swap `.active` between `#stepN` panels and between `#qpN` progress segments, then smooth-scroll `#quiz` into view. State array `const A=[null,null,null,null,null]`.

### Homepage form fields (#journeyForm, posts to Apps Script /exec via target="formSink")
Hidden: quiz_who, quiz_draw, quiz_pace, quiz_dest, quiz_luxury, quiz_archetype, source="arkipelago-homepage", timestamp (#formTimestamp, ISO string stamped at submit), page (#formPage, window.location.href).
Visible: name (required), email (required), journey_type select (Select… / Private Journey / Honeymoon / Engagement Proposal / Family with Children / Retiree Journey / Corporate / MICE), phone (required, pattern `[+0-9][0-9 ()\-.]{6,}`, leading "+" normalized to "00" client-side), dates ("Approximate Dates", e.g. March 2026), group_size ("e.g. 2 adults, 1 child"), message textarea.
Submit button "Request My Journey Consultation"; note "We respond within 24 hours. Every inquiry is handled personally."; JS validates name/email/phone + 7–15 phone digits, then hides form and injects a success block ("✓ / Your journey begins. / Thank you, {name}…") after 1.5s.

---

## 2. experiences/private-tours/index.html (1390 lines)

No breadcrumb on this page. Same nav + drawer as homepage.

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer` - identical site-wide furniture (see §1 items 1-2).
2. `<section class="hero">` - eyebrow "Private Guided Tours Philippines"; H1 `The Philippines<br>no travel guide<br>has ever <em>shown you.</em>`; subtitle; 2 actions (`.btn-primary` "Find My Journey Type" → scrollToQuiz(), `.btn-ghost` "Begin planning" → #begin). Below: `.hero-stats` band of 4 stats (7,641 islands / 8 max guests / 100% custom / 30+ years).
3. `<section class="cred-strip">` - two-column credibility. Left: label "Who This Is For"; H2 `You've been to Bali.<br>You've done the Maldives.<br>You want <em>something real.</em>`; 2 paragraphs. Right: `.differentiator-list` of 4 items (icon + title + body): 🧭 "No fixed routes", ⛵ "Private everything", 🗺️ "Access that isn't advertised", 📞 "One conversation to start".
4. `<section class="quiz-section" id="journey-finder">` - 4-question variant quiz. FULL DETAIL BELOW.
5. `<section class="journeys-section" id="journey-types">` - section-header (label "The Journeys We Design", H2 "Five ways to experience the Philippines privately"). 6 `.journey-card` cards (number, type line, h3 name, desc, 2 meta chips duration+destinations, CTA button "Design this journey" → scrollToForm()): 01 The Water Journey (7–12 days), 02 The Discovery Journey (9–14), 03 The Cultural Heritage Journey (8–12), 04 The Private Escape (5–9), 05 The Complete Archipelago (14–21), "?" "Tell us what you're imagining" (visually distinct gold-tint variant).
6. `<section class="how-section">` - label "The Process"; H2 "From first message to first morning"; subtitle "Four steps. No commitment until you're ready."; 4 `.hiw-step` (01 "You Tell Us What You're Imagining", 02 "We Have a Conversation", 03 "We Design Your Journey", 04 "You Arrive. Everything Is Ready."); CTA btn-primary "Begin Your Journey" + note "No commitment. No package pricing. Just a conversation."
7. `<section class="dest-strip">` - section-header (label "Where We Take You", H2 "Eight destinations. None of them overcrowded."). 8 `.dest-item` text cards (region, name, tagline, no images): Coron & Port Barton, Batanes, Siargao, Bohol & Cebu, Baguio & Sagada, Bukidnon Highlands, Puerto Galera, Vigan & Ilocos. Closing `.dest-note` paragraph on El Nido positioning ("We don't take clients to El Nido as a primary base…").
8. `<section class="quote-section" aria-hidden="true">` - quote `We go where the group boats don't.<br>That's not a selling point.<br>It's just <em>how we travel.</em>` + attribution "– Arkipelago, Founded 2025".
9. `<section class="faq-section">` - label "Questions"; H2 "Frequently asked"; 6 `<details class="faq-item">` accordions (summary `.faq-q` + `.faq-a`): differentiator vs other operators, solo travellers, destinations off the tourist trail, cost (no price grids), how far in advance, best time of year. ONLY page in this set using native `<details>` FAQ.
10. `<section class="journey-cta" id="begin">` - same layout as homepage CTA (label "Start Here", H2 "Begin Your Journey", body, 4 promise items, formSink iframe, #journeyForm).
11. `<footer>` - identical to homepage footer (tagline "Curated. Sovereign. Unforgettable.", 4 cols, © + coords).

### Private-tours quiz (4 questions) - complete

Eyebrow "Journey Type Finder"; H2 "What kind of journey are you imagining?"; subtitle "Four questions. We'll tell you which journey archetype fits, and which corners of the Philippines we'd design it around."; 4 progress segments; 4 steps; state `const A=[null,null,null,null]` (draw, pace, dest, luxury - NO "who" question).

Step 1 (step0) - "What draws you to <span>the Philippines</span> above anywhere else?" (1 of 4; 6 options, no Back):
- water - 🤿 "The water" / "Diving, snorkelling, open ocean, I want to be in it, on it, under it"
- discovery - 🗺️ "The undiscovered" / "Places that don't appear in any guide. Access that requires knowing someone who knows someone."
- culture - 🏛️ "Deep culture & history" / "I travel to understand a place. Colonial layers, living traditions, the stories behind what I'm looking at."
- escape - 🌿 "Complete escape" / "I want to disappear. Somewhere beautiful, private, and completely unreachable by the kind of person who books package tours."
- adventure - ⛰️ "Adventure & the wild" / "Hiking, wildlife, remote highland terrain, the Philippines that surprises people who expected only beaches."
- multi - ✈️ "All of it" / "I want the full range, islands to highlands, colonial cities to uninhabited atolls. Show me the whole archipelago."

Step 2 (step1) - "How do you like to <span>move through a place</span>?" (2 of 4):
- packed - ⚡ "Well-packed, 4–7 days" / "I have limited time. I want to see a lot. I'll sleep on the plane."
- balanced - 🗓️ "Balanced, 8–11 days" / "Enough to settle in, explore properly, and not feel like I'm rushing."
- deep - 🌙 "Deep immersion, 12–14 days" / "I want to understand a place, not just pass through it. Fewer destinations, more depth."
- extended - 🗺️ "Extended journey, 2+ weeks" / "I'm here to genuinely explore the archipelago. Take me across it."

Step 3 (step2) - "Which destination <span>calls to you most</span>?" (3 of 4; `.quiz-options.three-col` grid variant):
- palawan - 🏝️ "Palawan" / "Coron, Port Barton, the Palawan that hasn't been overrun"
- batanes - 🌾 "Batanes" / "The northernmost Philippines, stone houses, rolling hills, a coast like nothing else"
- siargao - 🌊 "Siargao" / "The island behind the surf photos, mangroves, private outer islands, extraordinary light"
- visayas - 🐋 "Bohol & Cebu" / "Chocolate Hills, whale sharks, colonial history, the Central Visayas at its richest"
- north - 🏔️ "Northern Luzon" / "Baguio, Sagada, the Banaue rice terraces, the highland Philippines most visitors never reach"
- open - 🧭 "Surprise me" / "I'd rather you recommended based on what I've told you. I trust the expertise."

Step 4 (step3) - "When you imagine <span>the perfect private journey</span>, what matters most?" (4 of 4; final "See My Journey →"):
- access - 🔑 "Access to the unreachable" / "I want to go where other people simply can't. The doors that only open with the right contacts."
- privacy - 🏖️ "Complete privacy" / "No other guests. No crowds. The beach, the boat, the island, entirely mine."
- expertise - 🧠 "Deep local expertise" / "A guide who can actually tell me what I'm looking at. Someone who has been coming here for years."
- sovereign - ✍️ "Complete control over my itinerary" / "I want the flexibility to change the plan at any point. Nothing fixed until I say so."

Result: two-column `.result-card`. Left: `#rBadge`, `<h3 class="result-archetype" id="rArchetype">` (multiline archetype statement, last line wrapped in `<em>` by JS), `#rTagline`, label "Journeys we'd design for this" + `#rDestinations` destination pills, CTA row ("Begin Planning This Journey" → scrollToForm(), "Start again" → restartQuiz()). Right: label "What we'd build in" + `#rHighlights` (dot + text rows).

Archetype decision (showResult):
```
type = 'discovery' (default)
draw water→water, culture→culture, escape→escape, adventure→adventure, multi→archipelago, discovery→discovery
Refinements: if luxury==='privacy' and draw!=='water' → 'escape'
             if luxury==='access' and draw==='discovery' → 'discovery'
             if draw==='multi' or (dest==='open' and pace==='extended') → 'archipelago'
```
Six archetypes, each with badge / archetype statement / tagline (interpolating paceLabels: packed→"4–7 days", balanced→"8–11 days", deep→"12–14 days", extended→"2+ weeks") / destinations[] / highlights[]:
- water - "The Water Journey" - "Diving, snorkelling,\nand open ocean."
- discovery - "The Discovery Journey" - "The Philippines\nno one else goes to."
- culture - "The Cultural Heritage Journey" - "The Philippines\nyou travel to understand."
- escape - "The Private Escape" - "Somewhere beautiful.\nCompletely unreachable."
- adventure - "The Adventure Journey" - "The Philippines\nthat surprises everyone."
- archipelago - "The Complete Archipelago" - "The full range.\nNo destination repeated."

Quiz state → form hidden fields (showResult tail):
- `#quizDraw` (quiz_draw) ← drawLabels: water→"The water & diving", discovery→"The undiscovered", culture→"Deep culture & history", escape→"Complete escape", adventure→"Adventure & the wild", multi→"All of it"
- `#quizPace` (quiz_pace) ← paceLabels (above)
- `#quizDest` (quiz_dest) ← destLabels: palawan→"Coron & Port Barton, Palawan", batanes→"Batanes", siargao→"Siargao", visayas→"Bohol & Cebu", north→"Northern Luzon", open→"Open to recommendation"
- `#quizLuxury` (quiz_luxury) ← luxLabels: access→"Access to the unreachable", privacy→"Complete privacy", expertise→"Deep local expertise", sovereign→"Complete itinerary control"
- `#quizArchetype` (quiz_archetype) ← r.badge
- `journeyTypeSelect` pre-selected via typeMap: water→"Private Journey, Water & Diving", discovery→"Private Journey, Discovery", culture→"Private Journey, Cultural Heritage", escape→"Private Journey, Private Escape", adventure→"Private Journey, Discovery", archipelago→"Private Journey, Complete Archipelago"
- NO quiz_who field on this page (4 answers only).

### Form fields (#journeyForm)
Hidden: quiz_draw, quiz_pace, quiz_dest, quiz_luxury, quiz_archetype, source="arkipelago-private-journeys", timestamp, page.
Visible: name, email, journey_type select (Select… / Private Journey, Water & Diving / Private Journey, Discovery / Private Journey, Cultural Heritage / Private Journey, Private Escape / Private Journey, Complete Archipelago / Not sure yet, let's talk), phone, dates, group_size ("e.g. 2 adults"), message. Submit "Request My Journey Consultation". Same validation + success-block pattern as homepage.

---

## 3. experiences/honeymoon-proposals/index.html (843 lines)

No quiz on this page. Nav + drawer identical.

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer`.
2. `<div class="breadcrumb">` - "Home › Experiences › Honeymoons & Proposals" (span separators, current page as plain text).
3. `<section class="hero">` - eyebrow "Couples · Honeymooners · Proposal Planners"; H1 `The Philippines,<br>designed for <em>the two of you.</em>`; `.hero-sub` paragraph; 2 actions (`.btn-primary` "Begin Your Journey" → #begin, `.btn-ghost` "Planning a proposal?" → #proposal).
4. `<div class="segment-strip">` - 2 clickable `.segment-tab` jump links (scrollIntoView): "For couples / Honeymoon Journeys" → #honeymoon; "Planning something special? / Proposal Planning" → #proposal.
5. `<section class="section" id="honeymoon">` - split layout. Left: label "Honeymoon Journeys", H2 `Hand it over.<br>We'll handle <em>everything.</em>`, 3 body paragraphs. Right: 4 `.feeling-card` cards (emoji icon + title + body): 🏝 "Private vessels only", 🌅 "Sunrise access", 🏡 "Private accommodation", 🍽 "Dinners worth remembering".
6. `<div class="pull-quote">` - quote "The water is the same colour as the Maldives. The privacy is comparable. But the <em>stories</em> you come home with, those are not." + attribution "Arkipelago, on why couples choose the Philippines".
7. `<section class="section section-dark">` (destinations) - label "Where we take couples"; H2 `The most <em>romantic</em> corners of the archipelago`; body paragraph; 3 `.dest-card` cards (region, name, body, `.dest-tag` duration chip): Coron & Port Barton "7–10 days recommended", Siargao "5–8 days recommended", Amanpulo "3–7 nights standalone" (Amanpulo body cites "From USD 1,200/night" - LTP is not price-free).
8. `<section class="section" id="proposal">` - label "Proposal Planning"; H2 `She won't suspect<br><em>a thing.</em>`; body paragraph; `.proposal-wrap` panel: eyebrow "How we handle it", title "The Proposal, from first conversation to the moment itself", body, 6 `.proposal-step` cards (Step 01 "Location & timing", Step 02 "The decoy", Step 03 "The photographer", Step 04 "The contingency", Step 05 "After the yes", Step 06 "The honeymoon"), `.proposal-note` "Every proposal we have planned has worked. We treat the logistics with the same seriousness you treat the question."
9. `<section class="section-warm section">` (inclusions) - label "What's included"; H2 "Every journey includes"; 8 `.include-item` dot rows (transfers, private vessel, domestic flights, dedicated guide, finest accommodation, entrance fees/permits, 24/7 contact, proposal-specific: photographer/decoy/contingency/setup); bordered exclusion note (international flights, alcohol, shopping, gratuities not included; travel insurance recommended).
10. `<section class="section section-dark">` (FAQ) - label "Common questions"; H2 "Things couples ask us"; 5 STATIC `.faq-item` divs (`.faq-q` + `.faq-a`, no `<details>`, no JS): surprise proposal, vs Maldives/Bali, private villas/overwater, somewhere no one else goes, how far in advance.
11. `<section class="cta-section" id="begin">` - left: label "Begin your journey"; H2 "Every journey begins with a conversation."; 2 body paragraphs (second one italic confidentiality line); `.cta-promise` "24-hour response guaranteed". Right: formSink iframe + `#journeyForm`.
12. `<footer>` - 4 cols; brand tagline "The Philippines, as it was always meant to be experienced."; col order Destinations / Experiences / Arkipelago ("Begin a Journey" → /#begin); footer bottom © line only, NO coordinates.

### Form fields (#journeyForm)
Hidden: source="arkipelago-honeymoon-proposals", segment="couples", timestamp, page. No quiz fields.
Visible: name ("Your name", "First name"), email, phone (same pattern/normalization), occasion select (name=journey_type; Select one / Honeymoon / Surprise proposal / Anniversary / Proposal + Honeymoon / Romantic getaway - these options carry value attrs), timing (name=dates, "e.g. March 2026, or 'flexible'"), message textarea. Submit "Send My Enquiry →"; note "No packages. No price lists. Just a conversation."; separate `.form-success` div toggled visible by JS after 1.5s ("Thank you. We'll be in touch within 24 hours…").

---

## 4. experiences/family-tours/index.html (1694 lines)

Light theme page (teal/coral, Nunito/Lora) - own inline CSS, not the navy/gold palette.

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer` (same furniture, navy palette).
2. `<div class="breadcrumb">` - "Home › Experiences › Family Tours".
3. `<header class="hero">` - eyebrow "Families · Children of all ages · Pets welcome"; H1 `The Philippines,<br>for families who <span class="accent">refuse to stay home.</span>`; `.hero-lead` paragraph; actions (`.btn-coral` "Start Planning" → #begin, `.btn-ghost` "What makes us different →" → #what-we-do); `.hero-stats` 3 stats (4mo "Youngest we've travelled with (our own daughters)", 8 max guests, 100% custom); decorative island/palm/sun inline SVG illustration.
4. Wave SVG divider band (navy → white).
5. `<div class="tab-strip">` - 7 sticky scroll-spy `.tab-item` buttons: "What We Do"(what-we-do), "By Age"(ages), "Pets Welcome"(pets), "Destinations"(destinations), "What's Included"(inclusions), "Questions"(faq), "Start Planning"(begin). JS scroll helper (-80px offset) + scroll-spy toggles .active.
6. `<section class="cred-block">` - eyebrow "Why we actually understand families"; `.cred-quote` (""We have children ourselves. We started travelling with our daughters when they were <span class="accent">just 4 months old.</span>…"); 3 body paragraphs; `.cred-photo-wrap` (Loboc River family photo + `.photo-caption`).
7. `<section class="section" id="what-we-do">` - eyebrow "The Arkipelago family difference"; H2 `We've thought of what <span class="accent">you haven't yet.</span>`; lead; 6 `.diff-card` (icon + title + body): 🛏 "Pre-arrival sourcing", ⛵ "Safe on the water", 🗓 "Flex built into every day", 👩‍⚕️ "Medical preparedness", 🏊 "Water conditions briefed", 🙋 "Childminder contacts".
8. `<section class="section section--sand" id="ages">` - eyebrow "We design for every age"; H2 `Your children's ages <span class="accent">change everything.</span> Good.`; lead; 4 `.age-card` cards with colored `.age-badge` chips: "0 – 18 months / Babies & Infants", "18mo – 4 years / Toddlers", "5 – 11 years / Young Children", "12+ years / Pre-teens & Teens".
9. `<div class="pull-quote">` - "Finally, someone who gets it. We don't want to choose between having children and having extraordinary experiences." + cite "What every family client tells us, usually within the first five minutes".
10. `<section class="pets-block" id="pets">` - eyebrow "Your whole family travels" (teal); `.pets-headline` `Your dog or cat<br>comes too.`; 2 paragraphs | pet photo (el-nido-kayak-dog.jpg) + `.pets-list` 7 bullet items (pet-friendly accommodation verified, private transport, vet contact, staff briefing, food/medication sourcing, restrictions noted, genuinely suitable villa).
11. `<section class="section section--navy-mid" id="destinations">` - eyebrow "Where we take families"; H2 `The destinations that <span class="accent">work for everyone.</span>`; lead; 4 `.dest-card` (region, name, body, `.dest-ages` line): Bohol & Cebu "Best from: all ages, including infants · 7–10 days", Puerto Galera "Best from: all ages · 3–5 days", Coron, Palawan "Best from: 8 years+ · 6–9 days", Baguio & Sagada "Best from: 8 years+ · 5–7 days"; centered note + `.btn-coral` "Discuss Your Family's Journey" → #begin.
12. `<section class="section section--coral-light">` (how it works) - eyebrow "How it works"; H2 `From first message to <span class="accent">last transfer home.</span>`; lead; 5 `.step` rows (01 "Tell us about your family", 02 "A conversation, not a questionnaire", 03 "We build the itinerary from scratch", 04 "We refine it together", 05 "We're with you until you're home").
13. `<section class="section" id="inclusions">` - eyebrow "What's included"; H2 `Every family journey <span class="accent">includes.</span>`; lead; 12 `.inc-item` rows (✦ icon + bold lead-in + body: private transfers/car seats, private vessel/child PFDs, domestic flights, child-engaging guide, baby & child gear, family accommodation, water condition briefing, paediatrician contacts, flexible daily scheduling, childminder referrals, pet logistics, 24/7 contact); `.excl-note` exclusions paragraph.
14. `<section class="section section--sand" id="faq">` - eyebrow "Common questions"; H2 `Things family clients <span class="accent">ask us.</span>`; 6 static `.faq-item` divs (baby/infant trips, pets, sick child mid-trip, boat safety, best destinations, pre-arrival sourcing list).
15. `<section class="contact-section" id="begin">` - eyebrow "Start planning"; H2 (inline-styled Nunito) `Tell us about your family.<br>We'll handle everything else.`; body paragraph; formSink iframe + form.
16. `<footer class="site-footer">` - brand tagline "The Philippines, as it was always meant to be experienced."; Destinations / Experiences / Arkipelago cols ("Start Planning" → #begin); footer bottom single © line.

### Form fields (#journeyForm)
Hidden: timestamp, page, segment="Family", source="family-tours-page". No quiz fields.
Visible: name, email, phone, children (text "Children's ages", "e.g. 8 months, 3 years, 7 years"), pets select (Select one / No pets travelling / Yes, dog / Yes, cat / Yes, dog and cat / Other), timing select (name=dates: Within the next 3 months / 3–6 months from now / 6–12 months from now / More than a year away / Flexible, just exploring), message textarea. Submit `.btn-submit` "Send Our Family's Enquiry →"; note "24-hour response guaranteed · No packages · No price lists · Just a conversation"; `.form-success` div. JS: phone "+"→"00", timestamp/page stamps, disable button "Sending…", success after 1.5s. Reveal observer gated at `window.innerWidth >= 641`.

---

## 5. experiences/retirement-travel/index.html (1878 lines)

Gold/sand theme variant.

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer`.
2. `<div class="breadcrumb">` - "Home › Experiences › Retiree Journeys".
3. `<header class="hero">` - eyebrow "Retirees · Milestone Journeys · Bucket List Travel"; H1 `The Philippines,<br>taken at <em>exactly your pace.</em>`; `.hero-lead`; actions (`.btn-gold` "Begin Your Journey" → #begin, `.btn-ghost` "See our destinations →" → #destinations); `.hero-stats` 3 stats (30+ years, 8 max guests, 24h response guarantee); ornamental compass SVG (`.hero-ornament`, desktop only, arc text "ARKIPELAGO · LUXURY TOURS PHILIPPINES").
4. `<div class="tab-strip">` - 5 tabs: "The Journey"(what-we-do), "Destinations"(destinations), "What's Included"(inclusions), "Common Questions"(faq), "Begin Planning"(begin). Scroll helper + scroll-spy.
5. `<section class="credibility" id="credibility">` - eyebrow "Why we understand retirees"; `.credibility-quote` (""We've been planning journeys for retirees for years… <em>we do best.</em>""); 3 body paragraphs.
6. `<section class="section" id="what-we-do">` - eyebrow "The Arkipelago difference"; H2 `What retiree journeys<br>actually look like <em>with us.</em>`; lead; 6 `.diff-card`: 🌅 "No early starts" (nothing before 8:30am), 🧭 "Expert, unhurried guides", 🏡 "Finest accommodation, always", 🗺 "Fewer destinations, more depth", 🚗 "Accessible by design", 🏥 "Medical preparedness".
7. `<div class="pull-quote">` - "Not slower, <em>deeper.</em> That is the pace of a retiree journey done right." + cite "Arkipelago, on what unhurried travel actually means".
8. `<section class="section section--sand">` (process) - eyebrow "The process"; H2 `How your journey <em>comes together.</em>`; lead; 5 `.step`: 01 "Tell us what you're imagining", 02 "A conversation, not a questionnaire", 03 "We design your journey from scratch", 04 "We refine it together", 05 "We handle everything until you're home".
9. `<section class="section section--navy-mid" id="destinations">` - eyebrow "Where we take retirees"; H2 `The destinations that reward <em>patience.</em>`; lead; 4 `.dest-card` with `.dest-tag`: Vigan & Ilocos "7–10 days recommended", Bohol & Cebu "7–10 days recommended", Coron & Port Barton "7–10 days recommended", Batanes "5–7 days recommended"; note (Baguio & Sagada, Bukidnon, North Luzon routes) + `.btn-gold` "Discuss Your Destinations" → #begin.
10. `<section class="section">` (signature journeys) - eyebrow "Signature journeys"; H2 `Journeys other retirees <em>have loved.</em>`; lead ("not fixed packages… starting points for a conversation"); 3 arrow `.step` rows: "The North Heritage Journey" (Baguio → Sagada → Vigan, 7–10 days), "The Classic South" (Coron → Bohol → Cebu, 10–14 days), "The Discovery Journey" (Batanes → Siargao, 10 days); framed sample-itinerary note ("Here's what a 10-day North Heritage journey can look like…").
11. `<section class="section section--sand" id="inclusions">` - eyebrow "What's included"; H2 `Every journey <em>includes.</em>`; lead; 10 `.inc-item` rows (transfers, domestic flights, private vessel, expert guide, finest accommodation, daily breakfast + selected meals, entrance fees/permits, accessibility briefing, medical preparedness documentation, 24/7 contact); `.exclusions-note`.
12. `<section class="section" id="faq">` - eyebrow "Common questions"; H2 `Things retirees <em>ask us.</em>`; 6 static `.faq-item` divs (mobility considerations, pace, guides, medical preparedness, recommended destinations, planning horizon 6–12 months).
13. `<section class="contact-section" id="begin">` - eyebrow "Begin your journey"; H2 "Every journey begins with a conversation."; body; formSink iframe + form.
14. `<footer class="site-footer">` - same pattern as family (tagline "The Philippines, as it was always meant to be experienced.", 4 cols, © only).

### Form fields (#journeyForm)
Hidden: timestamp, page, segment="Retiree", source="retiree-journeys-page". No quiz fields.
Visible: name, email, phone, occasion select (name=journey_type: Bucket list journey / Milestone birthday or anniversary / Post-retirement dream trip / OFW homecoming journey / Long-planned Philippines return / Other), timing select (name=dates, same 5 options as family), travellers select (name=group_size: Just me (solo) / 2 (couple or friends) / 3–4 / 5–8), message textarea. Submit "Send My Enquiry →"; note "24-hour response guaranteed · No packages · No price lists · Just a conversation"; `.form-success`.

---

## 6. experiences/corporate-mice/index.html (1711 lines)

Gold/sand theme variant. Form id differs: `#briefForm`.

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer`.
2. `<div class="breadcrumb">` - "Home › Experiences › Corporate & MICE".
3. `<header class="hero">` - eyebrow "Corporate Retreats · MICE · Incentive Travel · Leadership Offsites"; H1 `Impressive.<br>Seamless.<br><em>Something no one has done before.</em>`; `.hero-lead`; actions (`.btn-gold` "Submit a Corporate Brief" → #brief, `.btn-outline` "What we deliver →" → #what-we-deliver); `.hero-stats` 3 stats (30 "Maximum pax per private journey", 1 "Point of contact from brief to debrief", 24h response guarantee); `.hero-panel` outcomes box: label "What this delivers", title "The outcomes your leadership team is actually looking for", 7-item bullet list.
4. `<div class="tab-strip">` - 7 tabs: "What We Deliver"(what-we-deliver), "Featured Client"(daryl), "Experiences"(experiences), "vs Maldives"(compare), "Destinations"(destinations), "Logistics"(logistics), "Submit Brief"(brief). Scroll helper + scroll-spy.
5. `<section class="section" id="what-we-deliver">` - eyebrow "The Arkipelago corporate difference"; H2 `One call. One brief.<br><em>Everything handled.</em>`; lead; 6 `.deliver-card` numbered 01–06: "One point of contact", "Zero ambiguity in the brief", "Contingency as standard", "Private. Always.", "Structured + experiential", "The comparison argument".
6. `<section class="daryl-block" id="daryl">` - featured client testimonial block. Left: eyebrow "Featured client"; large quote (genuine remoteness, cultural weight…); attribution "Daryl Urbanski - Fractional CMO · Founder, Best Business Coach · Singapore & Australia". Right `.daryl-profile`: eyebrow "About Daryl", photo, name, title ("Fractional CMO · 20+ years building B2B revenue systems across APAC"), 2-paragraph bio (mentions Michael E. Gerber / The E-Myth), 4 `.daryl-result` stats ($1.6M front-end revenue 9 months Neurogym, $500K automated sales E-Myth, 106% repeat purchase lift, 20+ years APAC).
7. `<div class="pull-quote">` - "I need this to be impressive, seamless, and something no one has done before, and I cannot afford for anything to go wrong." + cite "What every corporate decision-maker tells us, and what we design every retreat around".
8. `<section class="section section--warm" id="experiences">` - eyebrow "What's possible"; H2 `Retreat experiences that <em>actually deliver.</em>`; lead with 4 inline links to the corporate sub-pages (one-day executive intensive, two-day bootcamp, three-day executive war room, five-day installation retreat); 6 `.exp-card`: 🏝 "Private Island Buyout", 🍽 "Gala Dinner on the Beach", 🤿 "Diving & Wreck Experiences", 🛶 "Island-Hopping & Water Days", 🎣 "Cultural Immersions", 🏔 "Highland Retreat Option".
9. `<section class="section section--sand" id="compare">` - eyebrow "The business case"; H2 `Philippines vs Maldives<br>for corporate retreats.`; lead "The CFO will ask. Here is the answer, with the numbers behind it."; 3-column `.compare-table` (Criteria / Maldives / Fiji / Philippines, Arkipelago) with 8 rows, `.tick`/`.cross` cell classes (cost per person, flight from Singapore, visa, cultural experience, activity variety, private island access, multi-day variety, "We haven't done this before").
10. `<section class="section section--navy" id="destinations">` - eyebrow "Where we take corporate groups"; H2 `Four destinations.<br><em>One extraordinary programme.</em>`; lead; 4 `.dest-card` with `.dest-tag` "Best for" lines: Coron & the Calamian Islands (senior leadership · island buyouts · 4–6 days), Siargao (leadership teams of 6–14 · 3–5 days), Puerto Galera (Manila-based teams · 2–4 days), Vigan & Ilocos Heritage Route (cultural programmes · senior retreats · 5–7 days).
11. `<section class="section" id="how-it-works">` - eyebrow "The process"; H2 `From brief to <em>debrief.</em>`; lead; 5 `.step`: 01 "Submit your brief", 02 "A 30-minute briefing call", 03 "We build the programme", 04 "You review and approve", 05 "On-ground execution".
12. `<section class="section section--navy" id="logistics">` - eyebrow "Logistics assurance"; H2 `Everything documented.<br><em>Nothing left to chance.</em>`; lead; 8 `.log-card`: ✈️ "Airport transfers", 🏨 "Accommodation", 📡 "AV & connectivity", 🩺 "Medical preparedness", ⛵ "Vessels & transport", 🍽 "Catering & dietary", 🌧 "Weather contingency", 📞 "Single point of contact".
13. `<section class="section section--warm" id="faq">` - eyebrow "Common questions"; H2 `What corporate clients <em>ask us.</em>`; 5 static `.faq-item` divs (group sizes 6–30, vs Maldives/Bali, hybrid/AV support, point of contact during retreat, best destinations).
14. `<section class="contact-section" id="brief">` - eyebrow "Submit a corporate brief"; H2 `Tell us what you need.<br>We'll tell you what's possible.`; body; formSink iframe + `#briefForm`.
15. `<footer class="site-footer">` - 4 cols; Arkipelago col last link "Submit a Brief" → #brief; © only.

### Form fields (#briefForm - note the different id)
Hidden: timestamp, page, segment="Corporate-MICE", source="corporate-mice-page". No quiz fields.
Visible: name, work email ("you@company.com"), company, phone, group_size select (6–10 people / 11–20 people / 21–30 people / 30+ people), dates text ("e.g. Q3 2025 or July 10–15"), retreat type select (name=journey_type: Leadership offsite / Incentive travel / Client entertainment / Team milestone trip / Full company offsite / MICE, conference + experience / Other), budget select (USD 3,000–5,000 / 5,000–8,000 / 8,000–12,000 / 12,000–15,000 / 15,000+ per person / To be determined), message textarea (labelled "Programme objectives and any specific requirements"). Submit "Submit Corporate Brief →"; note "24-hour response guaranteed · All briefs handled in confidence · No commitment until you approve the programme"; `.form-success` "Brief received…".

---

## 7. destinations/el-nido/index.html (741 lines)

Destination page template. No quiz, no form on page (CTAs link to /#begin).

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer`.
2. `<nav class="breadcrumb" aria-label="Breadcrumb">` - `.breadcrumb-inner`: Home `<span class="sep">–</span>` Destinations (→ /destinations/) `<span class="sep">–</span>` `<span class="current">El Nido, Palawan</span>`.
3. `<section class="hero">` - `.hero-bg` + `.hero-latline` (decorative latitude line); eyebrow "Northern Palawan · Bacuit Archipelago"; H1 `El Nido,<br><em>the right way</em>`; subtitle; `.hero-meta` 4 fact items (strong label + value): "Best Season Nov – May", "Airport Lio (ENI) via AirSWIFT", "Ideal Stay 4 – 7 nights", "Character Dramatic · Iconic · Private".
4. `<section class="section intro">` - `.intro-grid` split: left label "The Archipelago", H2 `Worth every<br><em>photograph, done right</em>`, 3 paragraphs (crowding problem → private solution); right `.intro-image` (Big Lagoon photo + 3-line caption "Big Lagoon / Miniloc Island, Bacuit Bay / Best before 8am").
5. `<section class="personal-band">` - eyebrow "A Note From Arkipelago"; `.personal-quote` (""El Nido is overcrowded. We recommend it anyway – because the <em>solution is not to go elsewhere,</em> it is to go differently.""); 2 `.personal-body` paragraphs with named accommodation picks (Charlie's El Nido at Lio Beach; Los Cabanos sunset dinner).
6. `<section class="section highlights">` - label "Signature Experiences"; H2 `What El Nido<br><em>actually is</em>`; `.hc-carousel` of 8 `.hc-card` (num + tag + h3 + desc, bg images): 01 Big Lagoon, 02 Small Lagoon, 03 Secret Lagoon, 04 Nacpan Beach, 05 Payong-Payong Sandbar, 06 Cudugnon Cave, 07 Lio Beach, 08 Las Cabanas at Dusk. Arrows + JS dots (same carousel JS as homepage).
7. `<section class="experience-strip">` - label "For Every Traveller"; H2 `El Nido's<br><em>many faces</em>`; 6 `.exp-item` rows (icon + title + desc): Couples & Honeymooners, Independent Travellers, Families, Photographers, Retirees, Corporate Groups.
8. `<section class="section practical">` - label "Planning Notes"; H2 `What to know<br><em>before you go</em>`; 6 `.prac-card` (`.prac-title` + `.prac-text`): Getting There, Best Season, The Crowd Problem, How Long, Where to Stay (names Charlie's El Nido), Getting Around.
9. `<section class="section">` (day-tour cross-link, centered) - label "One day, not one week?"; H2 `El Nido,<br><em>as a private day tour</em>`; body; `.btn-gold` "See the private day tour" → /day-tours/el-nido-bacuit-bay-day/.
10. `<section class="cta-band">` - H2 `Ready to see El Nido<br><em>the right way?</em>`; body; dual CTA: `.btn-gold` "Start Planning" → /#begin, `.btn-outline` "Explore Coron" → /destinations/coron/.
11. `<footer>` - homepage-style footer (tagline "Curated. Sovereign. Unforgettable.", 4 cols, © + coords).

---

## 8. destinations/coron/index.html (1231 lines)

Same template as El Nido with these differences:

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer`.
2. `<nav class="breadcrumb">` - Home – Destinations – `<span class="current">Coron, Palawan</span>`.
3. `<section class="hero">` - eyebrow "Northern Palawan · Calamian Islands"; H1 `Coron,<br><em>Untamed</em>`; subtitle; `.hero-meta`: "Best Season Nov – May", "From Manila ~1 hr by air", "Ideal Stay 4 – 7 nights", "Character Wild · Historic · Remote".
4. `<section class="section intro">` - label "The Island"; H2 `A different Palawan<br><em>entirely</em>`; 3 paragraphs (El Nido vs Coron contrast, Tagbanua ancestral domain / UNESCO Tentative List, Busuanga logistics) | intro-image (Twin Lagoon photo + caption "Twin Lagoon / Coron Island, Palawan / Sacred Tagbanua domain").
5. NO personal band on Coron (El Nido only).
6. `<section class="section highlights">` - label "Signature Experiences"; H2 `What Coron does<br><em>differently</em>`; 9-card carousel: 01 Kayangan Lake, 02 Twin Lagoon, 03 WWII Wreck Diving, 04 Barracuda Lake, 05 Malcapuya Island, 06 Calauit Safari Park, 07 Mount Tapyas, 08 Siete Pecados, 09 Private Island-Hopping.
7. `<section class="experience-strip">` - H2 `Coron's many<br><em>personalities</em>`; 6 exp-items: Divers & Wreck Hunters, Island-Hopping Purists, History Seekers, Nature & Wildlife, Couples & Honeymooners, Families.
8. `<section class="section practical">` - 6 prac-cards: Getting There, Best Season, Cultural Notes (Tagbanua/fees), How Long, Getting Around, A Word on Crowds.
9. `<section class="section">` day-tour cross-link - H2 `Coron,<br><em>as a private day tour</em>` → /day-tours/coron-island-ultimate-day/.
10. `<section class="cta-band">` - H2 `Ready to explore<br><em>Coron?</em>`; dual CTA: "Start Planning" → /#begin, "Coron vs El Nido" → /journal/coron-vs-el-nido/.
11. `<footer>` - homepage-style + coords.

---

## 9. about/index.html (572 lines)

Story-led page. No form, no quiz.

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer`.
2. `<div class="breadcrumb">` - "Home › About".
3. `<section class="about-hero">` - eyebrow "The People Behind the Journey"; H1 `Born here.<br>Raised on the road.<br>Obsessed with the <em>version of it</em><br>most people never find.`; `.about-hero-sub` paragraph.
4. `<section style="background:var(--navy)">` (origin) - `.origin` split. Left: label "Our Story"; H2 `This is not a business<br>that started with a <em>business plan.</em>`; 4 first-person paragraphs (signed implicitly "My name is Kathy"). Right `.origin-aside`: family photo + caption ("Loboc River, Bohol, with the family"); `.pull-block` quote; 5 `.coord-card` fact cards: "Founded / 2025, Philippines", "Personal journeys across the archipelago / 30+ years", "Family background / Logistics, nationwide", "Maximum guests per private journey / 8, always", "Fixed packages available / None. Not one."
5. `<section class="different">` - label "What Makes Us Different"; H2 `We've been there.<br>That changes everything.`; intro; 3 numbered `.diff-card`: 01 "Grown Up in These Islands", 02 "Tested by Every Kind of Journey", 03 "Nothing Is Fixed".
6. `<section class="credibility">` - label "Why This Matters"; H2 `We've planned journeys for people<br>in every situation you can <em>imagine.</em>`; 4 `.cred-item` (icon + title + body): 👨‍👩‍👧‍👦 "Families with Children", 🐾 "Families Travelling with Pets", 💍 "Proposals & Honeymoons", 🌺 "Retirees".
7. `<section class="promise">` - label "Our Commitment"; H2 `Every journey begins<br>with a <em>conversation.</em>`; 2 paragraphs (second links "A Seedling for Every Day" → /sustainability/); `.btn-primary` "Begin Your Journey" → /#begin + italic reassurance line "No commitment. Every inquiry answered personally within 24 hours."
8. `<footer>` - homepage-style + coords.

---

## 10. journal/index.html (1027 lines)

JS-driven index. No static post cards in HTML.

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer`.
2. `<div class="breadcrumb">` - "Home › Journal".
3. `<header class="journal-hero">` - eyebrow "The Journal"; H1 `Dispatches from the <em>archipelago</em>`; `.journal-hero-desc` ("Destination intelligence, private guides, and the stories behind the journeys – written by people who have actually been there.").
4. `<div class="filter-bar" id="filterBar" role="navigation">` - 9 `.filter-btn` buttons with data-filter: all ("All"), palawan, batanes, bohol ("Bohol & Cebu"), siargao, ilocos ("Ilocos & Vigan"), families, couples, retirees.
5. `<section class="journal-grid-wrap">` - `.grid-meta`: `#postCount` ("Loading guides…" until JS fills "N Guides") + RSS link to /feed.xml with inline SVG icon. `#postGrid` (role="list") with a loading state; JS fetches /posts.json, sorts by date desc, renders `.post-card` articles: "Latest" featured badge on first card in All view, image (eager on first, lazy on rest; letter placeholder if no image), category eyebrow, h2 title link, excerpt, footer row (date · read time, "Read" arrow link).
6. `<section class="journal-cta">` - H2 `Ready to stop reading and <em>start going?</em>`; line "Every journey begins with a conversation. Tell us what you're imagining."; `.btn-gold` "Begin Your Journey" → /#begin.
7. `<footer class="site-footer">` - 4 cols (tagline "Curated. Sovereign. Unforgettable."), footer bottom © + coords.

JS furniture: FILTER_MAP keyword matching against post category/segment (palawan: ['palawan','coron','port barton','el nido'], batanes, bohol: ['bohol','cebu'], siargao, ilocos: ['ilocos','vigan'], families: ['famil'], couples: ['couple','honeymoon','proposal','romantic'], retirees: ['retir','senior']); staggered card reveal (80ms setTimeout); escHtml sanitizer for injected content.

---

## 11. journal/luxury-solo-travel-philippines/index.html (528 lines)

Journal post template. No form (CTA links to homepage form). Uses absolute URLs (https://luxurytoursphilippines.com/...) - older template variant.

### Ordered skeleton

1. `<nav id="nav">` + `#navDrawer`.
2. `<header class="post-hero">` - `.post-hero-bg`; eyebrow "Insight · Solo Travel Philippines"; H1 `Luxury Solo Travel in the Philippines: <em>Mountains First, Then the Sea</em>`; `.post-meta` "By Kathy Hingan · October 1, 2026 · 12 min read".
3. `<div class="breadcrumb">` - Home › Journal › Luxury Solo Travel Philippines. NOTE in source: "moved after hero, no background, per Kathy's review" - on posts the breadcrumb sits BELOW the hero.
4. `<article class="post-wrap">` #1 - 3 lede paragraphs; `<h2>` "Why the Mountains Come First"; 3 paragraphs.
5. `<div class="img-wide">` #1 - full-bleed image + `.img-caption` (Sierra Madre foothills).
6. `<article class="post-wrap">` #2 - `<h2>` "The Journey, Day by Day"; 6 paragraphs with bold day lead-ins (Day 1 Manila to the foot of the Sierra Madre … Day 6 Tamaraw Falls).
7. `<article class="post-wrap">` #3 - `.pull-quote` ("Anyone can put a hot bath in an itinerary. Putting it where it belongs is <em>the difference.</em>"); `<h2>` "Choose How You'll Close the Journey"; 3 option paragraphs (Option one: Boracay, getting there like a local / Option two: Boracay, private throughout / Option three: El Nido replaces Boracay); `.segment-callout` (`.sc-label` "For Solo Travellers" + paragraph).
8. `<div class="img-wide">` #2 - El Nido sandbar image + caption.
9. `<article class="post-wrap">` #4 - `<h2>` "A Food Trip, Done Right" (3 paragraphs); `<h2>` "Is the Philippines Safe for Solo Travellers?" (3 paragraphs); `<h2>` "The Practicalities That Determine Whether It Works" (4 bold-led paragraphs: When to go / How long / Getting there / Dietary needs); `<h2>` "What This Journey Is Really About" (2 paragraphs); `.faq-section`: `<h2>` "Frequently Asked Questions" + 3 static `.faq-item` (safety, vegetarian solo travel, how many days); `.post-cta` (h3 "Tell us when you'd like to disappear." + line + `.btn-gold` "Begin Your Journey" → https://luxurytoursphilippines.com/#begin); italic "Related reading:" line with 3 links (2 journal posts + 1 destination page).
10. `<div class="img-wide">` #3 - closing sunset image.
11. `<footer class="site-footer">` - `.footer-brand-block` (tagline "The Philippines, as it was always meant to be experienced."); 3 `.footer-col` (Destinations 5 links → all to /#destinations; Experiences 5; Arkipelago 3: Our Philosophy, Journal, "Begin a Journey"); footer bottom © only.

---

## Page-level furniture (site-wide patterns)

- **Nav**: one structure reused everywhere (3 hover-dropdown groups, 3 plain links, Our Philosophy dropdown, dual CTA stack, hamburger). Byte-identical on the main pages; about/journal share a near-identical variant; the solo post variant uses absolute URLs. LTC note: LTC nav will have its own IA, but copy the PATTERN (dropdown groups + dual CTA + drawer mirror).
- **Mobile drawer**: fullscreen `#navDrawer`, mirrors every nav link with "↳" sub-items, 2 stacked CTA links, body-scroll lock on open.
- **Sold-out banner**: DORMANT on every analyzed page - CSS rules (`.soldout-banner`, slides in below nav at scrollY>300) and JS (`arkiBannerTop`/`arkiBannerSync`) ship on all pages, but no `#soldoutBanner` div exists in any body, so the JS no-ops (`if(!b) return`). If LTC wants this pattern, the markup must be added deliberately.
- **Cursor JS**: custom gold dot + trailing ring (`#cursor`/`#cursorRing`, pointer:fine only, requestAnimationFrame easing) on homepage, private-tours, about. NOTE ONLY: LTC will NOT copy this.
- **Reveal animations**: `.reveal` (+ `.reveal-delay-1..3`) → `.visible` via IntersectionObserver, thresholds .05–.12; family/retirement/corporate gate the observer at `window.innerWidth >= 641` (mobile renders without animation); journal cards stagger via setTimeout in JS.
- **Footer**: 4-column layout everywhere. Two tagline variants: "Curated. Sovereign. Unforgettable." (homepage, private-tours, el-nido, coron, about, journal index) vs "The Philippines, as it was always meant to be experienced." (honeymoon, family, retirement, corporate, solo post). Coordinates line "9°30′N 118°30′E · Philippine Archipelago" present on homepage/private-tours/el-nido/coron/about/journal index; absent on the segment pages and the solo post. Col 4 last link varies: "Begin Your Journey" (→ scrollToForm or /#begin), "Start Planning", "Submit a Brief" (corporate, → #brief).
- **Forms**: every form posts natively (method=POST, target="formSink" hidden iframe) to the same Apps Script /exec URL. Universal JS: phone leading "+" → "00" normalization, `formTimestamp` ISO stamp, `formPage` = window.location.href, button disable + "Sending…" + success block/`.form-success` div after 1.5s delay. Form ids: `journeyForm` everywhere except corporate (`briefForm`). Per-page hidden tagging: `source` (arkipelago-homepage / arkipelago-private-journeys / arkipelago-honeymoon-proposals / family-tours-page / retiree-journeys-page / corporate-mice-page) and `segment` (couples / Family / Retiree / Corporate-MICE; absent on homepage and private-tours).
- **FAQ**: two mechanisms - native `<details class="faq-item">` accordions (private-tours only) vs static `.faq-item` divs (all other pages, no toggle JS). LTC brand gate requires FAQ JSON-LD pairing; LTP ships none of that here.
- **Carousels**: `.hc-carousel` + JS-built dots + arrows + touch swipe + mouse drag, used on homepage destinations and both destination pages (14 / 8 / 9 cards).
- **Tab strips**: sticky scroll-spy `.tab-strip` on family (7 tabs), retirement (5), corporate (7); smooth scroll with -80px offset; `sections` array drives active state. Private-tours and honeymoon instead use hero buttons / segment-strip jump links.

## Cross-page patterns summary

Constant across all 11 pages:
- Fixed nav + drawer pair, nav-scroll state, dormant sold-out banner scaffold, reveal animation system, 4-column footer with © 2026 line.
- Single H1 per page, one eyebrow line above it, eyebrow/H1/lead hierarchy in every hero.
- Form capture via hidden-iframe POST + phone normalization + timestamp/page stamps (where a form exists).
- Emoji-icon card grids for scannable differentiators; text-first destination cards with region labels and duration chips; numbered process steps (4–5 steps, "01" style numerals).
- CTA discipline: every page's conversion path ends at a form section (id="begin" or id="brief") or links to /#begin; secondary CTAs cross-link to sibling pages (destination→destination, destination→day tour, corporate→sub-pages).

Page-type-specific:
- **Homepage**: quiz + destinations carousel + full how-it-works + quote band; 6 hidden quiz fields.
- **Experience pages** (private-tours, honeymoon, family, retirement, corporate): breadcrumb → hero (with hero-stats) → credibility block → differentiation grid → pull-quote → destinations grid → numbered process → inclusions/exclusions → FAQ → form. Variations: private-tours leads with its own 4-question quiz and has no tab strip; honeymoon has segment strip + 6-step proposal panel and no quiz; family adds ages grid + pets block + 7-tab strip; retirement adds signature journeys + compass ornament; corporate adds featured-client block, comparison table, logistics grid, budget field.
- **Destination pages** (el-nido, coron): breadcrumb → hero with 4-up hero-meta facts → intro split with captioned image → highlights carousel → per-traveller-type strip → 6 practical cards → day-tour cross-link → dual-CTA band. No forms, no quiz.
- **About**: hero → origin story with coord-cards → 3-item differentiator grid → credibility grid → commitment/CTA band. No form.
- **Journal index**: hero → filter bar → JS-rendered card grid from /posts.json + RSS → CTA strip.
- **Journal post**: post-hero (category eyebrow, H1, byline) → breadcrumb below hero → alternating article/img-wide bands with inline pull-quote, segment callout, FAQ block, post-CTA, related reading. No form.
- **Quiz presence**: homepage (5 questions incl. "who") and private-tours (4 questions, no "who") only. Quiz answers feed hidden fields with human-readable labels + archetype badge; result panel pre-selects the visible journey_type select.
