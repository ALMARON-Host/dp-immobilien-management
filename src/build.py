"""
Statischer Seitengenerator für den Relaunch-Entwurf der dp immobilien management GmbH.

Aufruf:
    python src/build.py            -> baut nach ./site  (Links mit index.html, funktioniert auch per Doppelklick)
    python src/build.py --pretty   -> baut nach ./site  (saubere URLs mit "/" für den Live-Server)
    python src/build.py --pretty --noindex -> Vorschau für GitHub Pages (für Suchmaschinen gesperrt), siehe deploy.ps1

Inhalte liegen in src/pages/*.html. Jede Datei beginnt mit einem JSON-Kommentar:
    <!--meta {"path": "hausverwaltung", "title": "...", "description": "...", "nav": "hausverwaltung",
              "crumbs": [["Hausverwaltung", "/hausverwaltung"]]} -->
Links und Bilder werden in den Inhalten absolut geschrieben (href="/kontakt", src="/assets/img/...").
Der Generator rechnet sie in relative Pfade um.
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "site")
PRETTY = "--pretty" in sys.argv
NOINDEX = "--noindex" in sys.argv  # Vorschau (GitHub Pages): für Suchmaschinen gesperrt
SITE_URL = "https://www.dp-immobilien-management.de"

PORTAL = "https://zuhause.app/login"
TEL = "+4969403562400"
TEL_TXT = "069 / 4035624 - 00"
NOTFALL = "+4915129707877"
NOTFALL_TXT = "0151-29707877"
MAIL = "info@dp-immobilien-management.de"

ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>',
    "portal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
    "caret": '<svg class="nav__caret" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 3l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
}

# Hauptnavigation: (Schlüssel, Titel, Pfad, Unterpunkte[(Titel, Pfad, Untertitel)])
NAV = [
    ("ueber-uns", "Über uns", "/ueber-uns", [
        ("Firmenprofil", "/ueber-uns#profil", "Seit 1995 in Frankfurt"),
        ("Ihre 10 Vorteile mit dpi", "/ueber-uns#vorteile", "Was wir anders machen"),
        ("Das Team", "/ueber-uns#team", "Ihre Ansprechpartner"),
    ]),
    ("hausverwaltung", "Hausverwaltung", "/hausverwaltung", [
        ("Überblick Hausverwaltung", "/hausverwaltung", "Kaufmännisch & technisch"),
        ("WEG-Verwaltung", "/hausverwaltung/weg-verwaltung", "Unsere Kernkompetenz seit 1995"),
        ("Mietverwaltung", "/hausverwaltung/mietverwaltung", "Für Eigentümer von Mietobjekten"),
        ("Gewerbeverwaltung", "/hausverwaltung/gewerbeverwaltung", "Real Estate Asset Management"),
        ("Verwalterwechsel", "/hausverwaltung/verwalterwechsel", "So einfach wechseln Sie zu uns"),
    ]),
    ("vermittlung", "Immobilienvermittlung", "/immobilienvermittlung", [
        ("Überblick Vermittlung", "/immobilienvermittlung", "Vermietung und Verkauf"),
        ("Vermieten", "/immobilienvermittlung/wohnung-vermieten-frankfurt-am-main", "Wohnung oder Haus"),
        ("Verkaufen", "/immobilienvermittlung/immobilie-verkaufen", "Mit persönlicher Wertermittlung"),
    ]),
    ("referenzen", "Referenzen", "/referenzen", []),
    ("jobs", "Karriere", "/jobs", [
        ("Stellenangebote", "/jobs", "Werden Sie Teil des Teams"),
        ("Immobilienverwalter/in (m/w/d)", "/assets/docs/190814_Stellenanzeige-Stepstone.pdf", "Stellenanzeige als PDF"),
        ("Ausbildung", "/jobs/ausbildung", "Immobilienkauffrau/-mann"),
    ]),
    ("service", "Service", "/service/notfall", [
        ("Notfall & Schadensmeldung", "/service/notfall", "Rund um die Uhr erreichbar"),
        ("Häufige Fragen", "/service/faq", "Antworten für Eigentümer & Mieter"),
        ("Kundenportal", PORTAL, "Dokumente & Vorgänge online"),
    ]),
    ("kontakt", "Kontakt", "/kontakt", []),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def rel_prefix(path):
    depth = 0 if path == "" else path.count("/") + 1
    return "../" * depth


def resolve(url, prefix):
    """Rechnet einen absoluten Site-Link in einen relativen um."""
    if not url.startswith("/") or url.startswith("//"):
        return url
    frag = ""
    if "#" in url:
        url, frag = url.split("#", 1)
        frag = "#" + frag
    target = url.strip("/")
    if target.startswith("assets/") or re.search(r"\.[a-z0-9]{2,5}$", target):
        return prefix + target + frag
    if PRETTY:
        out = prefix + (target + "/" if target else "")
        return (out or "./") + frag
    return prefix + (target + "/" if target else "") + "index.html" + frag


def rewrite_links(html, prefix):
    return re.sub(r'(href|src|srcset|action)="(/[^"]*)"', lambda m: f'{m.group(1)}="{resolve(m.group(2), prefix)}"', html)


def nav_html(active, current_path):
    items = []
    for key, title, href, subs in NAV:
        is_active = key == active
        cls = "nav__link" + (" is-active" if is_active else "")
        if subs:
            sub = "".join(
                f'<li><a href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}'
                f'{" aria-current=\"page\"" if h.strip("/") == current_path else ""}>{esc(t)}<small>{esc(st)}</small></a></li>'
                for t, h, st in subs
            )
            items.append(
                f'<li class="nav__item nav__item--has-sub"><button type="button" class="{cls}" aria-expanded="false">{title}{ICON["caret"]}</button>'
                f'<ul class="nav__sub">{sub}</ul></li>'
            )
        else:
            cur = ' aria-current="page"' if href.strip("/") == current_path else ""
            items.append(f'<li class="nav__item"><a class="{cls}" href="{href}"{cur}>{title}</a></li>')
    extra = (f'<div class="nav__mobile-extra"><a class="btn" href="tel:{TEL}">{ICON["phone"]}{TEL_TXT}</a>'
             f'<a class="btn btn--ghost" href="{PORTAL}" target="_blank" rel="noopener">{ICON["portal"]}Kundenportal</a></div>')
    return f'<nav class="nav" id="hauptnavigation" aria-label="Hauptnavigation"><ul class="nav__list">{"".join(items)}</ul>{extra}</nav>'


def header_html(active, current_path):
    return f"""<a class="skip-link" href="#inhalt">Zum Inhalt springen</a>
<div class="topbar">
  <div class="wrap">
    <div class="topbar__group">
      <span data-office-status class="status-line"><span class="dot dot--off"></span><span data-status-text>Mo–Fr 9–12 Uhr, Di + Do 14–16 Uhr</span></span>
      <span class="topbar__hide-sm"><a href="tel:{TEL}">{TEL_TXT}</a></span>
      <span class="topbar__hide-sm"><a href="mailto:{MAIL}">{MAIL}</a></span>
    </div>
    <div class="topbar__group">
      <span class="topbar__emergency"><b>Notfall:</b> <a href="tel:{NOTFALL}">{NOTFALL_TXT}</a></span>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="dp immobilien management GmbH – Startseite">
      <img src="/assets/img/logos/dpi-logo.png" alt="dp immobilien management gmbh" width="310" height="260">
    </a>
    {nav_html(active, current_path)}
    <div class="header-actions">
      <button type="button" class="icon-btn theme-toggle" data-theme-toggle aria-label="Hell/Dunkel umschalten">{ICON["moon"]}</button>
      <a class="btn btn--ghost btn--sm btn--portal" href="{PORTAL}" target="_blank" rel="noopener">{ICON["portal"]}Kundenportal</a>
      <a class="btn btn--alert btn--sm btn--emergency" href="/service/notfall" aria-label="Notfall und Schadensmeldung">{ICON["alert"]}<span>Notfall</span></a>
      <button type="button" class="icon-btn menu-toggle" aria-controls="hauptnavigation" aria-expanded="false" aria-label="Menü öffnen">{ICON["menu"]}</button>
    </div>
  </div>
</header>"""


def footer_html():
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/img/logos/dpi-logo-quer.png" alt="dp immobilien management gmbh" width="513" height="300" loading="lazy">
        <p>Cassellastr. 30-32 (Haus B)<br>60386 Frankfurt am Main</p>
        <p><a href="tel:{TEL}">{TEL_TXT}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
        <dl class="hours">
          <dt>Mo–Fr</dt><dd>09.00 – 12.00 Uhr</dd>
          <dt>Di + Do</dt><dd>14.00 – 16.00 Uhr</dd>
        </dl>
        <p>In dringenden Notfällen erreichen Sie uns auch außerhalb der normalen Geschäftszeiten unter der Nummer: <a href="tel:{NOTFALL}"><b>{NOTFALL_TXT}</b></a></p>
      </div>
      <div>
        <h2>Leistungen</h2>
        <ul>
          <li><a href="/hausverwaltung">Hausverwaltung</a></li>
          <li><a href="/hausverwaltung/weg-verwaltung">WEG-Verwaltung</a></li>
          <li><a href="/hausverwaltung/mietverwaltung">Mietverwaltung</a></li>
          <li><a href="/hausverwaltung/gewerbeverwaltung">Gewerbeverwaltung</a></li>
          <li><a href="/immobilienvermittlung/wohnung-vermieten-frankfurt-am-main">Vermieten</a></li>
          <li><a href="/immobilienvermittlung/immobilie-verkaufen">Verkaufen</a></li>
          <li><a href="/hausverwaltung/verwalterwechsel">Verwalterwechsel</a></li>
        </ul>
      </div>
      <div>
        <h2>Immobilienverwaltung</h2>
        <ul>
          <li><a href="/immobilienverwaltung-bad-vilbel">Immobilienverwaltung Bad Vilbel</a></li>
          <li><a href="/immobilienverwaltung-hanau">Immobilienverwaltung Hanau</a></li>
          <li><a href="/immobilienverwaltung-offenbach">Immobilienverwaltung Offenbach</a></li>
        </ul>
        <h2 style="margin-top:28px">Immobilie verkaufen</h2>
        <ul>
          <li><a href="/immobilie-verkaufen-hanau">Immobilie verkaufen Hanau</a></li>
          <li><a href="/immobilie-verkaufen-bad-vilbel">Immobilie verkaufen Bad Vilbel</a></li>
        </ul>
      </div>
      <div>
        <h2>Karriere</h2>
        <ul>
          <li><a href="/jobs/immobilienverwalter-frankfurt">Job Immobilienverwalter Frankfurt</a></li>
          <li><a href="/jobs/immobilienverwalter-bad-vilbel">Job Immobilienverwalter Bad Vilbel</a></li>
          <li><a href="/jobs/immobilienverwalter-hanau">Job Immobilienverwalter Hanau</a></li>
          <li><a href="/jobs/immobilienverwalter-offenbach">Job Immobilienverwalter Offenbach</a></li>
          <li><a href="/jobs/ausbildung">Ausbildung</a></li>
        </ul>
        <h2 style="margin-top:28px">Verbandsmitgliedschaften</h2>
        <div class="memberships">
          <img src="/assets/img/logos/vdiv-hessen.png" alt="Mitglied im Verband der Immobilienverwalter Hessen e.V." width="558" height="260" loading="lazy">
          <img src="/assets/img/logos/ivd.webp" alt="Mitglied im IVD" width="200" height="200" loading="lazy">
        </div>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> dp immobilien management GmbH</span>
      <ul>
        <li><a href="/kontakt">Kontakt</a></li>
        <li><a href="/impressum">Impressum</a></li>
        <li><a href="/datenschutz">Datenschutzerklärung</a></li>
        <li><a href="{PORTAL}" target="_blank" rel="noopener">Kundenportal</a></li>
      </ul>
    </div>
  </div>
</footer>
<nav class="action-bar" aria-label="Schnellzugriff">
  <a href="tel:{TEL}">{ICON["phone"]}Anrufen</a>
  <a href="{PORTAL}" target="_blank" rel="noopener">{ICON["portal"]}Portal</a>
  <a class="is-alert" href="/service/notfall">{ICON["alert"]}Notfall</a>
</nav>"""


ORG_JSONLD = {
    "@context": "https://schema.org",
    "@type": "RealEstateAgent",
    "name": "dp immobilien management GmbH",
    "url": SITE_URL,
    "logo": SITE_URL + "/assets/img/logos/dpi-logo.png",
    "telephone": "+49 69 403562400",
    "email": MAIL,
    "foundingDate": "1995",
    "address": {"@type": "PostalAddress", "streetAddress": "Cassellastr. 30-32 (Haus B)", "postalCode": "60386",
                "addressLocality": "Frankfurt am Main", "addressCountry": "DE"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "12:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday", "Thursday"], "opens": "14:00", "closes": "16:00"},
    ],
    "areaServed": ["Frankfurt am Main", "Bad Vilbel", "Hanau", "Offenbach", "Bad Homburg", "Hofheim", "Dreieich", "Mörfelden-Walldorf"],
    "memberOf": [{"@type": "Organization", "name": "Verband der Immobilienverwalter Hessen e.V."}, {"@type": "Organization", "name": "IVD"}],
}


def page(meta, body, fragment=False):
    path = meta["path"]
    prefix = rel_prefix(path)
    crumbs = meta.get("crumbs")
    crumb_html = ""
    if crumbs:
        lis = '<li><a href="/">Start</a></li>' + "".join(
            f'<li><a href="{h}">{esc(t)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{esc(t)}</li>'
            for i, (t, h) in enumerate(crumbs)
        )
        crumb_html = f'<nav class="breadcrumb" aria-label="Brotkrumen"><ol>{lis}</ol></nav>'
    body = body.replace("{{breadcrumb}}", crumb_html)
    body = expand_partials(body)
    jsonld = ""
    if meta.get("org_jsonld"):
        jsonld += f'<script type="application/ld+json">{json.dumps(ORG_JSONLD, ensure_ascii=False)}</script>'
    if meta.get("jsonld"):
        jsonld += f'<script type="application/ld+json">{json.dumps(meta["jsonld"], ensure_ascii=False)}</script>'
    canonical = SITE_URL + "/" + (path + ("" if path == "" else ""))
    head = f"""<title>{esc(meta["title"])}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{esc(meta.get("description", ""))}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(meta["title"])}">
<meta property="og:description" content="{esc(meta.get("description", ""))}">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:image" content="{SITE_URL}/assets/img/hero.webp">
<meta name="theme-color" content="#b1116d">
{"<meta name=\"robots\" content=\"noindex, nofollow\">" if NOINDEX else ""}
<link rel="icon" href="/assets/img/logos/dpi-logo.png">
<link rel="preload" href="/assets/fonts/Manrope.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/BricolageGrotesque.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css">
<script>try{{var t=localStorage.getItem("dpi-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{jsonld}"""
    content = f"""{header_html(meta.get("nav", ""), path)}
<main id="inhalt">
{body}
</main>
{footer_html()}
<script src="/assets/js/main.js" defer></script>"""
    if fragment:
        # Variante für die Online-Vorschau: ohne doctype/html/head/body (wird dort automatisch ergänzt)
        html = head + "\n" + content
    else:
        html = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{content}
</body>
</html>"""
    return rewrite_links(html, prefix)


PARTIALS = {}


def load_partials():
    pdir = os.path.join(SRC, "partials")
    if not os.path.isdir(pdir):
        return
    for f in os.listdir(pdir):
        if f.endswith(".html"):
            PARTIALS[f[:-5]] = open(os.path.join(pdir, f), encoding="utf-8").read()


def expand_partials(html):
    for _ in range(3):
        html = re.sub(r"\{\{>\s*([\w-]+)\s*\}\}", lambda m: PARTIALS.get(m.group(1), f"<!-- fehlt: {m.group(1)} -->"), html)
    return html


def read_page(fn):
    raw = open(fn, encoding="utf-8").read()
    m = re.match(r"\s*<!--meta\s+(\{.*?\})\s*-->", raw, re.S)
    if not m:
        raise SystemExit(f"Keine Metadaten in {fn}")
    return json.loads(m.group(1)), raw[m.end():]


def main():
    load_partials()
    os.makedirs(OUT, exist_ok=True)
    for entry in os.listdir(OUT):  # Inhalt leeren (Ordner selbst bleiben lassen)
        e = os.path.join(OUT, entry)
        shutil.rmtree(e) if os.path.isdir(e) else os.remove(e)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    pages = []
    for fn in sorted(os.listdir(os.path.join(SRC, "pages"))):
        if not fn.endswith(".html"):
            continue
        meta, body = read_page(os.path.join(SRC, "pages", fn))
        pages.append(meta)
        if meta["path"] == "404":
            target = os.path.join(OUT, "404.html")
            meta = dict(meta, path="")
        else:
            d = os.path.join(OUT, *meta["path"].split("/")) if meta["path"] else OUT
            os.makedirs(d, exist_ok=True)
            target = os.path.join(d, "index.html")
        open(target, "w", encoding="utf-8").write(page(meta, body, fragment=("--artifact" in sys.argv and meta["path"] == "" and target.endswith("index.html") and os.path.dirname(target) == OUT)))
    # Sitemap
    urls = "".join(f"<url><loc>{SITE_URL}/{p['path'] + '/' if p['path'] else ''}</loc></url>" for p in pages if p["path"] != "404")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    shutil.copy(os.path.join(SRC, "htaccess.txt"), os.path.join(OUT, ".htaccess"))
    print(f"{len(pages)} Seiten gebaut -> {OUT} ({'saubere URLs' if PRETTY else 'Datei-Links'})")


if __name__ == "__main__":
    main()
