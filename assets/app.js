/* arslankayainsaat.com — kütüphane yok, tek dosya (dehaiskele app.js'ten sadeleştirildi). */
(function () {
  "use strict";
  var ham = document.getElementById("hamburger"), menu = document.getElementById("menu");
  function kapat() {
    menu.classList.remove("acik");
    ham.setAttribute("aria-expanded", "false");
    ham.setAttribute("aria-label", "Menüyü aç");
    document.body.classList.remove("menu-acik");
  }
  if (ham && menu) {
    ham.addEventListener("click", function () {
      var acik = menu.classList.toggle("acik");
      ham.setAttribute("aria-expanded", acik ? "true" : "false");
      ham.setAttribute("aria-label", acik ? "Menüyü kapat" : "Menüyü aç");
      document.body.classList.toggle("menu-acik", acik);
    });
    menu.addEventListener("click", function (o) { if (o.target.tagName === "A") kapat(); });
    document.addEventListener("keydown", function (o) {
      if (o.key === "Escape" && menu.classList.contains("acik")) { kapat(); ham.focus(); }
    });
  }

  var hb = document.querySelector(".hb");
  if (hb) requestAnimationFrame(function () { hb.classList.add("ac"); });

  /* Ortaya çıkış — ⚠️ güvenlik ağı şart: gözlemci tetiklenmezse içerik gizli kalıyordu. */
  var gel = document.querySelectorAll(".gel");
  if (gel.length) {
    if ("IntersectionObserver" in window) {
      var goz = new IntersectionObserver(function (g) {
        g.forEach(function (x) {
          if (!x.isIntersecting) return;
          var k = x.target.parentNode, n = 0;
          if (k) n = Array.prototype.indexOf.call(k.querySelectorAll(":scope > .gel"), x.target);
          x.target.style.transitionDelay = Math.min(n, 6) * 55 + "ms";
          x.target.classList.add("gorundu");
          goz.unobserve(x.target);
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.02 });
      gel.forEach(function (x) { goz.observe(x); });
      setTimeout(function () {
        gel.forEach(function (x) {
          if (!x.classList.contains("gorundu") && x.getBoundingClientRect().top < innerHeight * 1.5)
            x.classList.add("gorundu");
        });
      }, 2500);
    } else gel.forEach(function (x) { x.classList.add("gorundu"); });
  }

  /* Kaydırınca üst menü kompakt — histerezisli (90/40px). */
  var durum = false, bekle = false;
  addEventListener("scroll", function () {
    if (bekle) return; bekle = true;
    requestAnimationFrame(function () {
      var y = scrollY;
      if (!durum && y > 90) { durum = true; document.body.classList.add("kaydi"); }
      else if (durum && y < 40) { durum = false; document.body.classList.remove("kaydi"); }
      bekle = false;
    });
  }, { passive: true });
})();

/* Hero arka planı: Ken Burns'ü görünmezken durdur + masaüstünde fare derinliği.
   ⚠️ Yalnız .hero-fon-kat'a --px/--py yazar; img'deki CSS animasyonuna DOKUNMAZ. */
(function () {
  "use strict";
  var hero = document.getElementById("heroKb");
  if (!hero || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var gorunur = true;
  function esitle() { hero.classList.toggle("is-paused", !(gorunur && !document.hidden)); }
  if ("IntersectionObserver" in window)
    new IntersectionObserver(function (g) { gorunur = g[0].isIntersecting; esitle(); }).observe(hero);
  document.addEventListener("visibilitychange", esitle);

  if (!matchMedia("(hover:hover) and (min-width:1001px)").matches) return;
  var kat = hero.querySelector(".hero-fon-kat"), raf = null, x = 0, y = 0;
  if (!kat) return;
  hero.addEventListener("pointermove", function (o) {
    var r = hero.getBoundingClientRect();
    x = (o.clientX - r.left) / r.width - 0.5;
    y = (o.clientY - r.top) / r.height - 0.5;
    if (!raf) raf = requestAnimationFrame(function () {
      kat.style.setProperty("--px", (-x * 18).toFixed(1) + "px");
      kat.style.setProperty("--py", (-y * 12).toFixed(1) + "px");
      raf = null;
    });
  }, { passive: true });
  hero.addEventListener("pointerleave", function () {
    kat.style.setProperty("--px", "0px"); kat.style.setProperty("--py", "0px");
  });
})();
