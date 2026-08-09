/* =============================================================================
   Delivery 360° — Rodrigo Barros
   ~5KB, sem dependência, módulo ES com defer implícito.
   Regra da casa: nada anima se o usuário pediu menos movimento, e nada de
   efeito de ponteiro em tela de toque (gasta bateria e não agrega).
   ============================================================================= */

const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const finePointer  = matchMedia('(hover: hover) and (pointer: fine)').matches;
const $  = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

/* ---------------------------------------------------------------------------
   1. Reveal no scroll — um único observer para a página inteira
--------------------------------------------------------------------------- */
const revealables = $$('[data-reveal]');
if (reduceMotion || !('IntersectionObserver' in window)) {
  revealables.forEach(el => el.setAttribute('data-in', ''));
} else {
  const io = new IntersectionObserver((entries, obs) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      e.target.setAttribute('data-in', '');
      obs.unobserve(e.target);
    }
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
  revealables.forEach(el => io.observe(el));
}

/* ---------------------------------------------------------------------------
   2. Contadores — animam uma vez, ao entrar na tela
--------------------------------------------------------------------------- */
const counters = $$('[data-count]');
if (counters.length) {
  const run = el => {
    const target = Number(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    if (reduceMotion) { el.textContent = target + suffix; return; }
    const dur = 1100;
    const t0 = performance.now();
    const tick = now => {
      const p = Math.min((now - t0) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);           // easeOutCubic
      el.textContent = Math.round(target * eased) + (p === 1 ? suffix : '');
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries, obs) => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        run(e.target);
        obs.unobserve(e.target);
      }
    }, { threshold: 0.5 });
    counters.forEach(el => io.observe(el));
  } else {
    counters.forEach(run);
  }
}

/* ---------------------------------------------------------------------------
   3. Checklist de sintomas — micro-compromisso: quem marca, se reconhece
--------------------------------------------------------------------------- */
const checkWrap  = $('[data-check]');
const checkScore = $('[data-check-score]');
if (checkWrap && checkScore) {
  const boxes = $$('input[type="checkbox"]', checkWrap);
  const update = () => {
    const n = boxes.filter(b => b.checked).length;
    checkScore.textContent = n === 0
      ? ''
      : `Você marcou ${n} de ${boxes.length}. O problema não é você — e a gente resolve isso abaixo.`;
  };
  checkWrap.addEventListener('change', update);
  update();
}

/* ---------------------------------------------------------------------------
   4. Header “grudado” + CTA fixa no mobile
      Um sentinel invisível evita listener de scroll (melhor INP)
--------------------------------------------------------------------------- */
const header = $('.header');
const dock   = $('[data-dock]');

if ('IntersectionObserver' in window) {
  const sentinel = document.createElement('div');
  sentinel.style.cssText = 'position:absolute;top:0;left:0;width:1px;height:80vh;pointer-events:none';
  document.body.prepend(sentinel);

  const io = new IntersectionObserver(([e]) => {
    const passed = !e.isIntersecting;
    if (header) header.toggleAttribute('data-stuck', passed);
    if (dock) {
      dock.toggleAttribute('data-show', passed);
      dock.setAttribute('aria-hidden', String(!passed));
      const cta = $('a', dock);
      if (cta) cta.tabIndex = passed ? 0 : -1;
    }
  }, { threshold: 0 });
  io.observe(sentinel);
}

/* ---------------------------------------------------------------------------
   5. Risco da ancoragem de valor (R$ 1.500)
--------------------------------------------------------------------------- */
const strike = $('[data-strike]');
if (strike && 'IntersectionObserver' in window) {
  const io = new IntersectionObserver(([e], obs) => {
    if (!e.isIntersecting) return;
    e.target.setAttribute('data-in', '');
    obs.disconnect();
  }, { threshold: 0.9 });
  io.observe(strike);
}

/* ---------------------------------------------------------------------------
   6. Tilt 3D nos cartões + parallax da capa
      Um único rAF por frame, coordenadas lidas do evento (zero layout thrash)
--------------------------------------------------------------------------- */
if (finePointer && !reduceMotion) {
  const MAX = 7; // graus — acima disso vira enjoo, não sofisticação

  for (const card of $$('[data-tilt]')) {
    let raf = 0, rx = 0, ry = 0;
    const apply = () => {
      raf = 0;
      card.style.transform = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-4px)`;
    };
    card.addEventListener('pointermove', ev => {
      const r = card.getBoundingClientRect();
      ry = ((ev.clientX - r.left) / r.width - 0.5) * (MAX * 2);
      rx = (0.5 - (ev.clientY - r.top) / r.height) * (MAX * 2);
      if (!raf) raf = requestAnimationFrame(apply);
    });
    card.addEventListener('pointerleave', () => {
      if (raf) { cancelAnimationFrame(raf); raf = 0; }
      card.style.transform = '';
    });
  }

  // Capa: segue o ponteiro pela página inteira, bem sutil
  const cover = $('[data-cover]');
  const glare = $('[data-glare]');
  if (cover) {
    let raf = 0, x = 0, y = 0;
    const apply = () => {
      raf = 0;
      cover.style.setProperty('--ry', `${-15 + x * 12}deg`);
      cover.style.setProperty('--rx', `${7 - y * 10}deg`);
      if (glare) glare.style.transform = `translateX(${-30 + x * 60}%)`;
    };
    addEventListener('pointermove', ev => {
      x = ev.clientX / innerWidth - 0.5;
      y = ev.clientY / innerHeight - 0.5;
      if (!raf) raf = requestAnimationFrame(apply);
    }, { passive: true });
  }
}

/* ---------------------------------------------------------------------------
   7. Teste A/B de headline sem ferramenta externa
      ?h=a → Escala e autoridade | ?h=b → Antes e depois | padrão → principal
--------------------------------------------------------------------------- */
const variant = new URLSearchParams(location.search).get('h');
if (variant === 'a' || variant === 'b') {
  const h1 = $('#h1');
  const hi = h1 && $('.hi', h1);
  const lo = h1 && $('.lo', h1);
  const top = h1 && h1.dataset[`hl${variant.toUpperCase()}Lo`];
  const main = h1 && h1.dataset[`hl${variant.toUpperCase()}`];
  if (hi && lo && top && main) { lo.textContent = top; hi.textContent = main; }
}

/* ---------------------------------------------------------------------------
   8. Ano do rodapé
--------------------------------------------------------------------------- */
const year = $('[data-year]');
if (year) year.textContent = new Date().getFullYear();
