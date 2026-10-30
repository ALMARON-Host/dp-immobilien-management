/* dp immobilien management – Relaunch-Entwurf */
(function () {
  "use strict";
  var root = document.documentElement;

  /* ---------- Hell/Dunkel ---------- */
  var THEME_KEY = "dpi-theme";
  function storedTheme() { try { return localStorage.getItem(THEME_KEY); } catch (e) { return null; } }
  function applyTheme(t) {
    if (t === "light" || t === "dark") root.setAttribute("data-theme", t); else root.removeAttribute("data-theme");
  }
  applyTheme(storedTheme());
  function isDark() {
    var t = root.getAttribute("data-theme");
    if (t) return t === "dark";
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }
  document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var next = isDark() ? "light" : "dark";
      applyTheme(next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
      btn.setAttribute("aria-label", next === "dark" ? "Helles Design aktivieren" : "Dunkles Design aktivieren");
    });
  });

  /* ---------- Navigation ---------- */
  var nav = document.querySelector(".nav");
  var toggle = document.querySelector(".menu-toggle");
  var header = document.querySelector(".site-header");
  var ICON_MENU = toggle ? toggle.innerHTML : "";
  var ICON_CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';
  function setMenu(open) {
    if (!nav || !toggle) return;
    nav.classList.toggle("is-open", open);
    document.body.classList.toggle("nav-open", open);
    // Position erst nach dem Umschalten messen, damit das Menü direkt unter der Kopfzeile ansetzt
    if (open && header) nav.style.setProperty("--nav-top", Math.max(0, header.getBoundingClientRect().bottom) + "px");
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Menü schließen" : "Menü öffnen");
    toggle.innerHTML = open ? ICON_CLOSE : ICON_MENU;
  }
  if (nav && toggle) {
    toggle.addEventListener("click", function () { setMenu(!nav.classList.contains("is-open")); });
    // Menü schließen, sobald ein Link angetippt wird (auch Sprungmarken auf derselben Seite)
    nav.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
    window.addEventListener("resize", function () { if (window.innerWidth > 980) setMenu(false); });
  }
  document.querySelectorAll(".nav__item--has-sub > .nav__link").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width: 980px)").matches || btn.tagName === "BUTTON") {
        e.preventDefault();
        var item = btn.parentElement;
        var open = item.classList.toggle("is-open");
        btn.setAttribute("aria-expanded", String(open));
      }
    });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    document.querySelectorAll(".nav__item.is-open").forEach(function (i) { i.classList.remove("is-open"); });
    if (nav && nav.classList.contains("is-open")) { setMenu(false); toggle.focus(); }
  });

  /* ---------- Erreichbarkeit live (Europe/Berlin) ---------- */
  // Mo–Fr 09–12 Uhr, zusätzlich Di + Do 14–16 Uhr
  function berlinNow() {
    try {
      var parts = new Intl.DateTimeFormat("de-DE", { timeZone: "Europe/Berlin", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false }).formatToParts(new Date());
      var o = {}; parts.forEach(function (p) { o[p.type] = p.value; });
      var days = { "So": 0, "Mo": 1, "Di": 2, "Mi": 3, "Do": 4, "Fr": 5, "Sa": 6 };
      return { day: days[o.weekday.replace(".", "")], min: parseInt(o.hour, 10) * 60 + parseInt(o.minute, 10) };
    } catch (e) { var d = new Date(); return { day: d.getDay(), min: d.getHours() * 60 + d.getMinutes() }; }
  }
  function officeOpen() {
    var n = berlinNow();
    if (n.day < 1 || n.day > 5) return false;
    if (n.min >= 540 && n.min < 720) return true;
    if ((n.day === 2 || n.day === 4) && n.min >= 840 && n.min < 960) return true;
    return false;
  }
  var open = officeOpen();
  document.querySelectorAll("[data-office-status]").forEach(function (el) {
    var dot = el.querySelector(".dot");
    var txt = el.querySelector("[data-status-text]");
    if (dot) dot.classList.toggle("dot--off", !open);
    if (txt) txt.textContent = open ? "Jetzt telefonisch erreichbar" : "Büro derzeit nicht besetzt";
  });

  /* ---------- Vorher/Nachher ---------- */
  document.querySelectorAll(".ba__frame").forEach(function (frame) {
    var range = frame.querySelector(".ba__range");
    if (!range) return;
    function set() { frame.style.setProperty("--pos", range.value + "%"); }
    range.addEventListener("input", set); set();
  });

  /* ---------- Referenzen-Filter ---------- */
  var filter = document.querySelector("[data-ref-filter]");
  if (filter) {
    filter.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      filter.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      var cat = b.getAttribute("data-cat");
      document.querySelectorAll("[data-ref-group]").forEach(function (g) {
        g.hidden = !(cat === "alle" || g.getAttribute("data-ref-group") === cat);
      });
    });
  }

  /* ---------- Assistenten (mehrstufig) ---------- */
  document.querySelectorAll("[data-wizard]").forEach(function (wiz) {
    var steps = Array.prototype.slice.call(wiz.querySelectorAll(".wizard__step"));
    var bar = wiz.querySelector(".wizard__progress");
    var back = wiz.querySelector("[data-back]");
    var next = wiz.querySelector("[data-next]");
    var nav = wiz.querySelector(".wizard__nav");
    var i = 0;
    if (bar) { bar.innerHTML = steps.map(function () { return "<span></span>"; }).join(""); }
    function show() {
      steps.forEach(function (s, k) { s.hidden = k !== i; });
      if (bar) Array.prototype.forEach.call(bar.children, function (s, k) { s.classList.toggle("is-done", k <= i); });
      if (back) back.hidden = i === 0;
      var fin = steps[i].hasAttribute("data-final") || i === steps.length - 1;
      if (next) next.hidden = fin;
      var focusable = steps[i].querySelector("legend, h3");
      if (focusable && wiz.dataset.started) { focusable.setAttribute("tabindex", "-1"); focusable.focus({ preventScroll: false }); }
    }
    function valid() {
      var s = steps[i];
      var required = s.querySelectorAll("[required]");
      for (var k = 0; k < required.length; k++) { if (!required[k].checkValidity()) { required[k].reportValidity(); return false; } }
      var radios = s.querySelectorAll("input[type=radio]");
      if (radios.length && !s.querySelector("input[type=radio]:checked")) {
        var msg = s.querySelector("[data-hint]"); if (msg) msg.hidden = false; return false;
      }
      return true;
    }
    if (next) next.addEventListener("click", function () {
      if (!valid()) return;
      wiz.dataset.started = "1";
      // Schadensmelder: Notfall springt direkt zum Notfall-Ergebnis
      var jump = steps[i].querySelector("input[type=radio]:checked[data-goto]");
      if (jump) { var target = wiz.querySelector("#" + jump.getAttribute("data-goto")); if (target) { i = steps.indexOf(target); show(); return; } }
      var skipTo = steps.slice(i + 1).findIndex(function (s) { return !s.hasAttribute("data-only-via-jump"); });
      i = i + 1 + (skipTo < 0 ? 0 : skipTo);
      show();
    });
    if (back) back.addEventListener("click", function () { i = 0; wiz.dataset.started = "1"; show(); });
    wiz.addEventListener("change", function (e) {
      var h = steps[i].querySelector("[data-hint]"); if (h) h.hidden = true;
      // Ergebnis-Text füllen
      if (e.target.name && wiz.querySelector("[data-echo='" + e.target.name + "']")) {
        wiz.querySelectorAll("[data-echo='" + e.target.name + "']").forEach(function (el) { el.textContent = e.target.getAttribute("data-label") || e.target.value; });
      }
    });
    show();
  });

  /* ---------- Formulare (Entwurf: kein Versand) ---------- */
  document.querySelectorAll("form[data-demo]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var ok = form.querySelector(".form-success");
      if (ok) { ok.hidden = false; ok.setAttribute("tabindex", "-1"); ok.focus(); }
    });
  });

  /* ---------- Jahr im Footer ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
