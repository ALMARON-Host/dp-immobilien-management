# Erzeugt die FAQ-Seite inkl. strukturierter Daten (FAQPage) aus einer Liste.
import json, os, html
FAQ = [
 ("Für Eigentümer und Mieter", [
  ("Wann sind Sie telefonisch erreichbar?", "Sie erreichen uns Montag bis Freitag von 09.00 bis 12.00 Uhr sowie Dienstag und Donnerstag von 14.00 bis 16.00 Uhr unter 069 / 4035624 - 00."),
  ("Was mache ich bei einem Notfall außerhalb der Geschäftszeiten?", "In dringenden Notfällen erreichen Sie uns auch außerhalb der normalen Geschäftszeiten unter der Nummer 0151-29707877. Bei Gefahr für Leib und Leben wählen Sie bitte zuerst den Notruf 112."),
  ("Was finde ich im Kundenportal?", "Alle relevanten Objektdokumente wie Versicherungsrechnung, Energieausweis, Protokolle und Pläne stehen jederzeit zum Download bereit. Über das Vorgangsmanagement behalten Sie den Überblick über Ihre Anliegen. Den Login finden Sie unter zuhause.app."),
  ("Wie melde ich einen Schaden?", "Nutzen Sie unseren Schadensmelder auf der Seite Notfall & Schadensmeldung. Er zeigt Ihnen, ob Sie die Notfallnummer anrufen oder den Schaden über das Kundenportal melden sollten."),
 ]),
 ("Für Eigentümergemeinschaften und Vermieter", [
  ("In welchem Gebiet verwalten Sie Immobilien?", "Unser Tätigkeitsgebiet erstreckt sich von Bad Homburg im Norden bis Mörfelden-Walldorf / Dreieich im Süden und von Hanau im Osten bis Hofheim im Westen. Wir achten darauf, dass wir unsere Liegenschaften innerhalb von maximal einer Stunde erreichen können."),
  ("Welche Objektgrößen verwalten Sie?", "Im Bereich der WEG- und Mietverwaltung verwalten wir Objekte mit 3 bis 80 Einheiten (ohne Stellplätze). Darüber hinaus verwalten wir einige Geschäftshäuser sowie Gewerbeparks."),
  ("Sind unsere Verwaltungsbeiräte versichert?", "Ja. Wir haben eine Vermögensschadenshaftpflichtversicherung über 500.000 €, in der Beiräte (WEG) kostenlos mitversichert sind."),
  ("Wie läuft die Übernahme einer neuen Liegenschaft ab?", "Zu Beginn machen wir eine Objektbegehung und führen ein ausführliches Gespräch mit den Eigentümern bzw. dem Verwaltungsbeirat, um die individuellen Eigenschaften der Immobilie festzustellen und angestaute To-dos zu erfassen."),
  ("Mit welcher Software arbeiten Sie?", "Die Buchhaltung läuft über die cloudbasierte Software impower, die eine einfache und übersichtliche Belegprüfung ermöglicht. Kundenkommunikation und Vorgangsmanagement laufen über facilioo."),
  ("Ich bin bereits WEG-Kunde und möchte meine Wohnung verkaufen oder vermieten. Was muss ich vorbereiten?", "Nichts. Uns liegen bereits alle nötigen Unterlagen zu Ihrer Wohnung vor: Pläne, Energieausweis, Versicherungspolice usw."),
 ]),
 ("Karriere", [
  ("Bilden Sie aus?", "Ja. Wir sind seit 2017 Ausbildungsbetrieb der IHK Frankfurt und bilden Immobilienkaufleute (m/w/d) aus. Da wir für den eigenen Nachwuchs ausbilden, gibt es immer eine gute Chance auf Übernahme."),
 ]),
]
ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for _, qs in FAQ for q, a in qs]}
meta = {"path": "service/faq", "title": "Häufige Fragen | dp immobilien management", "description": "Antworten auf häufige Fragen zu Erreichbarkeit, Notfall, Kundenportal, Einzugsgebiet und Verwaltung durch die dp immobilien management GmbH.", "nav": "service", "crumbs": [["Service", "/service/notfall"], ["Häufige Fragen", "/service/faq"]], "jsonld": ld}
groups = ""
for title, qs in FAQ:
    items = "".join(f"<details><summary>{html.escape(q)}</summary><div><p>{html.escape(a)}</p></div></details>" for q, a in qs)
    groups += f'<div class="stack"><h2 style="font-size:var(--step-2)">{html.escape(title)}</h2><div class="faq">{items}</div></div>'
body = f"""
<section class="page-hero"><div class="wrap page-hero__grid page-hero__grid--solo"><div class="stack">{{{{breadcrumb}}}}<span class="eyebrow">Neu · Service</span><h1>Häufige Fragen</h1><p class="lead">Die wichtigsten Antworten für Eigentümer, Beiräte, Mieter und Bewerber. Ihre Frage ist nicht dabei? Rufen Sie uns an.</p></div></div></section>
<section class="section"><div class="wrap stack-lg" style="max-width:900px">{groups}</div></section>
{{{{> cta}}}}
"""
out = os.path.join(os.path.dirname(__file__), "pages", "09-faq.html")
open(out, "w", encoding="utf-8").write("<!--meta " + json.dumps(meta, ensure_ascii=False) + " -->\n" + body)
print("ok")
