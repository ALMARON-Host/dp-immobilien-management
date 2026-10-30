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
  if (storedTheme()) applyTheme(storedTheme());
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
  // ZENTRALE STELLE für die Telefonzeiten. Wochentag: 1 = Montag … 5 = Freitag. Zeiten in Minuten ab 0 Uhr.
  var OFFICE_HOURS = {
    1: [[540, 720]],              // Mo 09:00–12:00
    2: [[540, 720], [840, 960]],  // Di 09:00–12:00, 14:00–16:00
    3: [[540, 720]],              // Mi 09:00–12:00
    4: [[540, 720], [840, 960]],  // Do 09:00–12:00, 14:00–16:00
    5: [[540, 720]]               // Fr 09:00–12:00
  };
  var WEEKDAYS = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"];

  // Aktuelles Datum und Uhrzeit in Frankfurt (unabhängig davon, wo der Besucher ist)
  function berlinNow() {
    try {
      var parts = new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Berlin", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hour12: false }).formatToParts(new Date());
      var o = {}; parts.forEach(function (p) { o[p.type] = p.value; });
      return { y: +o.year, m: +o.month, d: +o.day, min: (+o.hour % 24) * 60 + +o.minute };
    } catch (e) { var n = new Date(); return { y: n.getFullYear(), m: n.getMonth() + 1, d: n.getDate(), min: n.getHours() * 60 + n.getMinutes() }; }
  }

  // Gesetzliche Feiertage in Hessen
  function easterSunday(y) {
    var a = y % 19, b = Math.floor(y / 100), c = y % 100, d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25),
        g = Math.floor((b - f + 1) / 3), h = (19 * a + b - d - g + 15) % 30, i = Math.floor(c / 4), k = c % 4,
        l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451),
        month = Math.floor((h + l - 7 * m + 114) / 31), day = ((h + l - 7 * m + 114) % 31) + 1;
    return Date.UTC(y, month - 1, day);
  }
  var holidayCache = {};
  function isHoliday(t) {
    var dt = new Date(t), y = dt.getUTCFullYear();
    if (!holidayCache[y]) {
      var e = easterSunday(y), DAY = 86400000;
      holidayCache[y] = [Date.UTC(y, 0, 1), e - 2 * DAY, e + DAY, Date.UTC(y, 4, 1), e + 39 * DAY, e + 50 * DAY,
                         e + 60 * DAY, Date.UTC(y, 9, 3), Date.UTC(y, 11, 25), Date.UTC(y, 11, 26)];
    }
    return holidayCache[y].indexOf(t) !== -1;
  }

  function hhmm(min) { return Math.floor(min / 60) + ":" + ("0" + (min % 60)).slice(-2) + " Uhr"; }

  // Ermittelt: geöffnet (bis wann) oder nächste Öffnung (wann)
  function officeStatus() {
    var n = berlinNow(), today = Date.UTC(n.y, n.m - 1, n.d), DAY = 86400000;
    for (var i = 0; i < 21; i++) {
      var t = today + i * DAY, wd = new Date(t).getUTCDay(), slots = OFFICE_HOURS[wd] || [];
      if (isHoliday(t)) continue;
      for (var s = 0; s < slots.length; s++) {
        var start = slots[s][0], end = slots[s][1];
        if (i === 0 && n.min >= end) continue;
        if (i === 0 && n.min >= start) return { open: true, until: end };
        return { open: false, dayOffset: i, weekday: wd, start: start, minutesUntil: i === 0 ? start - n.min : null, holidayToday: isHoliday(today) };
      }
    }
    return { open: false };
  }

  function statusText(st) {
    if (st.open) return "Jetzt telefonisch erreichbar – bis " + hhmm(st.until);
    if (st.start == null) return "Telefonzeiten: Mo–Fr 9–12 Uhr";
    if (st.minutesUntil != null && st.minutesUntil <= 60) return "Büro öffnet in " + st.minutesUntil + " Min.";
    var when = st.dayOffset === 0 ? "heute" : st.dayOffset === 1 ? "morgen" : "am " + WEEKDAYS[st.weekday];
    return (st.holidayToday ? "Heute Feiertag – " : "") + "Büro öffnet " + when + " um " + hhmm(st.start);
  }

  function renderStatus() {
    var st = officeStatus();
    var soon = !st.open && st.minutesUntil != null && st.minutesUntil <= 60;
    document.querySelectorAll("[data-office-status]").forEach(function (el) {
      var dot = el.querySelector(".dot");
      var txt = el.querySelector("[data-status-text]");
      if (dot) { dot.classList.toggle("dot--off", !st.open && !soon); dot.classList.toggle("dot--soon", soon); }
      if (txt) txt.textContent = statusText(st);
    });
  }
  renderStatus();
  setInterval(renderStatus, 60000); // jede Minute aktualisieren

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
