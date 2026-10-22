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