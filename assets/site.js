/* Luxury Tours Canada. Shared behaviours: nav drawer, FAQ accordions, quote form.
   The form posts natively to the Apps Script web app through the hidden iframe sink,
   the same pattern the LTP stack uses, so the payload survives without CORS work. */

function toggleMenu(){
  var d = document.getElementById('navDrawer');
  var b = document.getElementById('navToggle');
  if(!d || !b) return;
  var open = d.classList.toggle('open');
  b.setAttribute('aria-expanded', open ? 'true' : 'false');
  b.textContent = open ? 'Close' : 'Menu';
}

/* One FAQ open at a time */
document.addEventListener('DOMContentLoaded', function(){
  var items = document.querySelectorAll('.faq details');
  items.forEach(function(d){
    d.addEventListener('toggle', function(){
      if(d.open){ items.forEach(function(o){ if(o !== d) o.open = false; }); }
    });
  });

  /* Stamp the form: page slug and timestamp travel with every submission.
     Phone normalization, the LTP pattern: a leading + makes Google Sheets
     treat the value as a formula and drop it, so a leading + becomes 00
     and the number saves as plain text. */
  var form = document.getElementById('journeyForm');
  if(form){
    form.addEventListener('submit', function(){
      var ph = document.getElementById('fieldPhone');
      if(ph && ph.value.indexOf('+') === 0){
        ph.value = '00' + ph.value.slice(1);
      }
      var ts = document.getElementById('formTimestamp');
      var pg = document.getElementById('formPage');
      if(ts) ts.value = new Date().toISOString();
      if(pg && !pg.value) pg.value = location.pathname;
      var ok = document.getElementById('formOk');
      if(ok){
        setTimeout(function(){
          ok.classList.add('show');
          form.reset();
        }, 500);
      }
    });
  }
});

/* Reveal on scroll, disabled for reduced motion */
(function(){
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var els = document.querySelectorAll('.reveal');
  if(!els.length || !('IntersectionObserver' in window)){
    els.forEach(function(e){ e.classList.add('visible'); });
    return;
  }
  var ro = new IntersectionObserver(function(entries){
    entries.forEach(function(en){ if(en.isIntersecting) en.target.classList.add('visible'); });
  }, {threshold:.12});
  els.forEach(function(e){ ro.observe(e); });
})();

/* ---- Journey finder quiz (LTP pattern, Canada options) ---- */
const A=[null,null,null,null,null];
function sel(el,step){
  el.closest('.quiz-options').querySelectorAll('.quiz-option').forEach(o=>o.classList.remove('selected'));
  el.classList.add('selected');
  A[step]=el.dataset.value;
  document.getElementById('next'+step).disabled=false;
}
function nxt(cur){
  document.getElementById('step'+cur).classList.remove('active');
  document.getElementById('step'+(cur+1)).classList.add('active');
  document.getElementById('qp'+cur).classList.remove('active');
  document.getElementById('qp'+cur).classList.add('done');
  const np=document.getElementById('qp'+(cur+1));
  if(np){np.classList.remove('done');np.classList.add('active')}
  const q=document.getElementById('quiz');
  if(q)q.scrollIntoView({behavior:'smooth',block:'start'});
}
function prv(cur){
  document.getElementById('step'+cur).classList.remove('active');
  document.getElementById('step'+(cur-1)).classList.add('active');
  document.getElementById('qp'+(cur-1)).classList.remove('done');
  document.getElementById('qp'+(cur-1)).classList.add('active');
  document.getElementById('qp'+cur).classList.remove('active','done');
  const q=document.getElementById('quiz');
  if(q)q.scrollIntoView({behavior:'smooth',block:'start'});
}
function showResult(){
  document.querySelectorAll('.quiz-step').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.qp').forEach(s=>{s.classList.remove('active');s.classList.add('done')});
  const[who,draw,pace,dest,luxury]=A;
  let type='explorer';
  if(who==='corporate')type='corporate';
  else if(who==='family')type='family';
  else if(who==='retire')type='retire';
  else if(who==='couple'&&(draw==='romance'||draw==='slow'))type='romance';
  else if(draw==='culture')type='heritage';
  else if(draw==='adventure')type='explorer';
  const paceMap={'short':'4 to 6 days','balanced':'7 to 10 days','long':'11 to 14 days','extended':'2+ weeks'};
  const destMap={'coast':'Tofino & Salt Spring Island, BC','rockies':'Jasper, Banff & Yoho','lakeshore':'Prince Edward County & Niagara-on-the-Lake','multi':'a coast-to-coast journey'};
  const luxMap={'privacy':'total privacy','service':'flawless service','access':'exclusive access','comfort':'exceptional comfort'};
  const pl=paceMap[pace]||'';const dl=destMap[dest]||'Canada';const ll=luxMap[luxury]||'an extraordinary experience';
  const M={
    romance:{badge:'Honeymoon & Proposal Journey',title:"You deserve a moment that stops time.",desc:`A ${pl} journey through ${dl}, built around ${ll} and complete romance. Whether it is a proposal at sunrise on Lake Louise or a storm watched from a soaking tub in Tofino, we design the days that become the story you tell for the rest of your lives.`,seg:'Honeymoon'},
    family:{badge:'Family Journey',title:"Luxury travel that works for every member of your family.",desc:`A ${pl} journey through ${dl} designed around the real complexity of travelling with children. Cold-water rules, wildlife briefings, flexible pacing with ${ll}, and destinations chosen with your children's ages in mind, not against them.`,seg:'Family with Children'},
    retire:{badge:'Retiree Journey',title:"The journey you've been planning for decades. Finally, done right.",desc:`A ${pl} journey through ${dl}, unhurried, deeply comfortable, and built entirely around ${ll}. No departures before 8:30am, honest altitude notes, expert guides, the finest rooms. No one rushing you anywhere. Just Canada, at its most generous pace.`,seg:'Retiree Journey'},
    corporate:{badge:'Corporate & MICE Journey',title:"A retreat your team will talk about for years.",desc:`A private ${pl} experience for your group through ${dl}. We provide ${ll}, mountain and coastal venues, meaningful team experiences, and a fallback plan for every programme day. You focus on your people.`,seg:'Corporate / MICE'},
    heritage:{badge:'Cultural Heritage Journey',title:"The Canada most travellers never understand.",desc:`A ${pl} journey through ${dl} for the traveller who wants to understand a place, not just pass through it. Limestone towns, vineyards and their winemakers, heritage Kingston, cool-climate wine in January, all with ${ll}.`,seg:'Private Journey'},
    explorer:{badge:'Private Discovery Journey',title:"The Canada no travel guide has ever shown you.",desc:`A ${pl} private journey through ${dl}, no groups, no fixed routes, no places everyone else goes. We provide ${ll} and build your itinerary from scratch, using access most visitors never have.`,seg:'Private Journey'}
  };
  const r=M[type];
  document.getElementById('rBadge').textContent=r.badge;
  document.getElementById('rTitle').textContent=r.title;
  document.getElementById('rDesc').textContent=r.desc;
  const s=document.getElementById('fieldType');
  if(s){for(let i=0;i<s.options.length;i++){if(s.options[i].text===r.seg){s.selectedIndex=i;break}}}
  const whoLabels={solo:'Just me (solo)',couple:'Me and my partner',family:'Family with children',retire:'Retirement journey',corporate:'Team / corporate'};
  const drawLabels={nature:'The natural world',culture:'Culture and heritage',romance:'Romance and beauty',adventure:'Adventure and activity',slow:'Rest and restoration'};
  const paceLabels={short:'4 to 6 days, well-packed',balanced:'7 to 10 days, balanced',long:'11 to 14 days, unhurried',extended:'Two weeks or more'};
  const destLabels={coast:'Tofino & Salt Spring Island, BC',rockies:'Jasper, Banff & Yoho',lakeshore:'Prince Edward County & Niagara-on-the-Lake',multi:'Show me everything (coast to coast)'};
  const luxLabels={privacy:'Total privacy',service:'Flawless service',access:'Access to the unreachable',comfort:'Exceptional comfort'};
  const setv=(id,v)=>{const el=document.getElementById(id);if(el)el.value=v||''};
  setv('quizWho',whoLabels[who]);
  setv('quizDraw',drawLabels[draw]);
  setv('quizPace',paceLabels[pace]);
  setv('quizDest',destLabels[dest]);
  setv('quizLuxury',luxLabels[luxury]);
  setv('quizArchetype',r.badge);
  document.getElementById('quizResult').classList.add('active');
  document.getElementById('quiz').scrollIntoView({behavior:'smooth',block:'start'});
}
function restartQuiz(){
  A.fill(null);
  ['quizWho','quizDraw','quizPace','quizDest','quizLuxury','quizArchetype'].forEach(id=>{const el=document.getElementById(id);if(el)el.value='';});
  document.getElementById('quizResult').classList.remove('active');
  document.querySelectorAll('.quiz-step').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.quiz-option').forEach(o=>o.classList.remove('selected'));
  document.querySelectorAll('.quiz-btn-next').forEach(b=>b.disabled=true);
  document.querySelectorAll('.qp').forEach((s,i)=>{s.classList.remove('done','active');if(i===0)s.classList.add('active')});
  document.getElementById('step0').classList.add('active');
  document.getElementById('quiz').scrollIntoView({behavior:'smooth',block:'start'});
}

function scrollToForm(){
  const f=document.getElementById('begin');
  if(f)f.scrollIntoView({behavior:'smooth',block:'start'});
  const d=document.getElementById('navDrawer');
  if(d&&d.classList.contains('open')&&typeof toggleMenu==='function')toggleMenu();
}

/* Destination carousel: dots + drag + snap, homepage */
(function(){
  const carousel=document.getElementById('hcCarousel');
  if(!carousel)return;
  let isDown=false,startScrollLeft=0,startPageX=0;
  carousel.addEventListener('mousedown',e=>{isDown=true;startScrollLeft=carousel.scrollLeft;startPageX=e.pageX;carousel.style.userSelect='none';});
  window.addEventListener('mouseup',()=>{isDown=false;carousel.style.userSelect='';});
  carousel.addEventListener('mousemove',e=>{if(!isDown)return;e.preventDefault();carousel.scrollLeft=startScrollLeft-(e.pageX-startPageX);});
})();

/* Form: same native-POST sink pattern, with validation and success state (LTP submitForm) */
function submitForm(e){
  const btn=document.getElementById('formSubmitBtn');
  const form=document.getElementById('journeyForm');
  const name=document.getElementById('fieldName').value.trim();
  const email=document.getElementById('fieldEmail').value.trim();
  const phone=document.getElementById('fieldPhone').value.trim();
  const note=document.getElementById('formOk');
  if(!name||!email||!phone){e.preventDefault();return}
  const phoneDigits=phone.replace(/[^\d]/g,'');
  if(phoneDigits.length<7||phoneDigits.length>15){
    e.preventDefault();
    if(note){note.innerHTML='<strong>One more thing.</strong> Please enter a valid phone number including your country code, for example +1 604 555 0142.';note.style.display='block'}
    return;
  }
  document.getElementById('fieldPhone').value=phone.charAt(0)==='+'?'00'+phone.slice(1):phone;
  const ts=document.getElementById('formTimestamp');
  const pg=document.getElementById('formPage');
  if(ts)ts.value=new Date().toISOString();
  if(pg&&!pg.value)pg.value=location.pathname;
  btn.textContent='Sending...';
  btn.disabled=true;
  setTimeout(()=>{
    form.style.display='none';
    const wrap=form.parentElement;
    wrap.innerHTML=`<div style="text-align:center;padding:60px 24px"><div style="font-family:'Cormorant Garamond',serif;font-size:48px;color:var(--amber);margin-bottom:16px">✓</div><h3 style="font-family:'Cormorant Garamond',serif;font-size:32px;font-weight:300;color:var(--spruce);margin:0 0 16px">Your journey begins.</h3><p style="font-family:'EB Garamond',serif;font-size:18px;color:var(--slate);line-height:1.75;max-width:400px;margin:0 auto">Thank you, ${name}. We have received your inquiry and will be in touch within 24 hours with our initial thoughts for your journey.</p></div>`;
  },1500);
}
