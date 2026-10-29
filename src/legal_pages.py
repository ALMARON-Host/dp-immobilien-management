# Übernimmt Datenschutzerklärung aus dem Original-HTML (bereinigt) und erzeugt Impressum + 404.
import os, re, json, html
from html.parser import HTMLParser
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_quelle", "html-original", "datenschutz.html")
OUT = os.path.join(ROOT, "src", "pages")
ALLOWED = {"h2", "h3", "h4", "h5", "p", "ul", "ol", "li", "a", "strong", "b", "em", "br"}
MAP = {"h1": None, "h5": "h4", "b": "strong"}

class Clean(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.out = []; s.skip = 0; s.stack = []
    def handle_starttag(s, t, a):
        if t in ("script", "style", "noscript", "svg", "img"):
            if t != "img": s.skip += 1
            return
        if s.skip: return
        t2 = MAP.get(t, t)
        if t2 is None or t2 not in ALLOWED: return
        if t2 == "a":
            href = dict(a).get("href", "")
            href = re.sub(r"^(https?://www\.dp-immobilien-management\.de)?/images/", "/assets/docs/", href)
            ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
            s.out.append(f'<a href="{html.escape(href)}"{ext}>')
        else:
            s.out.append(f"<{t2}>" if t2 != "br" else "<br>")
    def handle_endtag(s, t):
        if t in ("script", "style", "noscript", "svg"): s.skip -= 1; return
        if s.skip: return
        t2 = MAP.get(t, t)
        if t2 and t2 in ALLOWED and t2 != "br": s.out.append(f"</{t2}>")
    def handle_data(s, d):
        if not s.skip: s.out.append(html.escape(d, quote=False))

raw = open(SRC, encoding="utf-8").read()
start = raw.find("Datenschutzerkl", raw.find("<h1"))
start = raw.rfind("<h1", 0, start)
end = raw.find("Sie haben Fragen?", start)
if end < 0: end = raw.find("Sprechen Sie uns an", start)
c = Clean(); c.feed(raw[start:end])
body = "".join(c.out)
body = re.sub(r"<(p|li|h2|h3|h4|strong)>\s*</\1>", "", body)
body = re.sub(r"\s+", " ", body)
body = re.sub(r"Diese E-Mail-Adresse ist vor Spambots geschützt! Zur Anzeige muss JavaScript eingeschaltet sein!", '<a href="mailto:info@dp-immobilien-management.de">info@dp-immobilien-management.de</a>', body)
body = body.replace("</p>", "</p>\n").replace("</h2>", "</h2>\n").replace("</h3>", "</h3>\n")
body = re.sub(r"<h4>\s*(\d+\.\s.*?)</h4>", lambda m: "<h2>" + m.group(1) + "</h2>", body)
body = re.sub(r"<h4>(.*?)</h4>", lambda m: "<h3>" + m.group(1) + "</h3>", body)
body = re.sub(r"^\s*Datenschutzerklärung\s*", "", body)
# Inhaltsverzeichnis aus h2/h3
heads = re.findall(r"<h([23])>(.*?)</h\1>", body)
toc, n = [], 0
def anchor(m):
    global n
    n += 1
    return f'<h{m.group(1)} id="ds-{n}">{m.group(2)}</h{m.group(1)}>'
body = re.sub(r"<h([23])>(.*?)</h\1>", anchor, body)
toc = "".join(f'<a href="#ds-{i+1}">{re.sub("<.*?>","",h[1])}</a>' for i, h in enumerate(heads) if h[0] == "2")

meta = {"path": "datenschutz", "title": "Datenschutzerklärung | dp immobilien management", "description": "Datenschutzerklärung der dp immobilien management GmbH", "nav": "", "crumbs": [["Datenschutz", "/datenschutz"]]}
page = f"""<section class="page-hero"><div class="wrap page-hero__grid page-hero__grid--solo"><div class="stack">{{{{breadcrumb}}}}<h1>Datenschutzerklärung</h1></div></div></section>
<section class="section"><div class="wrap">
<p class="note" style="margin-bottom:32px">Entwurfshinweis: Text unverändert von der bisherigen Website übernommen. Vor dem Livegang an die neue Website anpassen (z. B. lokal eingebundene Schriften, neue Formulare, Hosting).</p>
<div class="with-toc"><nav class="toc" aria-label="Inhalt">{toc}</nav><div class="prose">{body}</div></div></div></section>"""
open(os.path.join(OUT, "27-datenschutz.html"), "w", encoding="utf-8").write("<!--meta " + json.dumps(meta, ensure_ascii=False) + " -->\n" + page)
print("Datenschutz:", len(body), "Zeichen,", len(heads), "Überschriften; PDF-Links im Original:", raw.count("Datenschutzhinweise-"))
