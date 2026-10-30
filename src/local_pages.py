# Erzeugt die regionalen Landingpages (Verkaufen, Verwaltung, Jobs) aus den Originaltexten.
import json, os

OUT = os.path.join(os.path.dirname(__file__), "pages")


def write(fn, meta, body):
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write("<!--meta " + json.dumps(meta, ensure_ascii=False) + " -->\n" + body)


def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ---------------- Immobilie verkaufen: Hanau / Bad Vilbel ----------------
SELL = [
    dict(fn="13-verkaufen-hanau.html", path="immobilie-verkaufen-hanau", city="Hanau",
         title="Immobilie verkaufen in Hanau | dp immobilien management",
         desc="Immobilie verkaufen in Hanau? dp immobilien management – Ihr zuverlässiger Partner für Haus und Wohnung in Hanau verkaufen. Jetzt beraten lassen!",
         eyebrow="Immobilie verkaufen · Hanau", intro_label="Im Bereich Immobilien unterstützen wir Sie gerne mit:",
         chips=["Kompetenz beim Verkauf von Häusern und Wohnungen", "Übernahme aller Verwaltungstätigkeiten", "Bei Bedarf Hausverwaltungstätigkeiten"],
         h1="Jetzt Ihre Immobilie verkaufen in Hanau!",
         lead=["Ihre Immobilie zu verkaufen in Hanau ist aktuell eine überaus lukrative Idee! Denn Hanau ist sowohl für Privatpersonen als auch Gewerbebetriebe eine der interessantesten Regionen in Deutschland! Wir sind Ihr Partner, wenn es um das Immobilie verkaufen in Hanau geht."],
         why_h="Wir stehen Ihnen zur Seite, wenn Sie Immobilie verkaufen wollen in und um Hanau",
         why=["Rundum-Service bei allen anstehenden Arbeiten", "Marketing für einen optimalen Verkauf", "Beste Kenntnisse der Region"],
         haus_h="Sie möchten Ihr Haus verkaufen in Hanau?",
         haus=["<b>Wenn Sie Ihr Haus verkaufen wollen und rund um Hanau in kürzester Zeit eine Auswahl potenzieller Kaufinteressenten vorliegen haben möchten, dann sind Sie bei uns an der richtigen Adresse!</b>",
               "Denn die professionelle und seriöse Immobilienvermittlung ist unser Metier. Wenn Sie Unterstützung benötigen, um Ihre Immobilie verkaufen zu können, sind wir in Hanau gerne für Sie da! Bei uns steht jeder Kunde ganz individuell im Vordergrund – und genauso individuell vermarkten wir Ihr Haus! Unsere Aufgabe ist es, Ihnen von Beginn an eine umfassende Dienstleistung anzubieten. Denn wir sind kein reines Maklerbüro, sondern vielmehr ein Generalunternehmen – spezialisiert auf die Komplettbetreuung von Eigentümern bei der Verwaltung oder wenn es darum geht, eine Immobilie verkaufen zu wollen in Hanau."],
         haus_btn="Jetzt Haus verkaufen!",
         whg_h="Oder möchten Sie eher eine Wohnung verkaufen in Hanau?",
         whg=["Natürlich steht Ihnen unser Service auch beim Thema Wohnung verkaufen in Hanau vollumfänglich zur Verfügung! Wie bei allen Immobilien ermitteln wir auch bei Wohnungen den marktgerechten Verkaufspreis, erstellen professionelle Exposés mit aussagekräftigen Fotos und präsentieren Ihre Wohnung in allen gängigen Online-Immobilienportalen! Auch die Auswahl von passenden Kaufinteressenten übernehmen wir gerne für Sie, wenn Sie Ihre Immobilie verkaufen wollen und in Hanau auf einen optimalen Verkaufspreis aus sind. Natürlich führen wir auch die anstehenden Besichtigungstermine in Ihrem Auftrag durch, organisieren Notartermine und sind an Ihrer Seite, wenn es an Beurkundungen und die Übergabe an den neuen Eigentümer geht.",
              'Übrigens: Nicht nur beim Immobilie verkaufen in Hanau können Sie auf uns zählen! Auch wenn Sie eine <a href="/immobilienvermittlung/wohnung-vermieten-frankfurt-am-main">Wohnung vermieten</a> möchten oder auf der Suche nach einer zuverlässigen <a href="/hausverwaltung">Hausverwaltung</a> sind, bieten wir Ihnen höchste Fachkompetenz und ein umfangreiches Portfolio an Leistungen!'],
         whg_btn="Immobilie verkaufen in Hanau!", img="wohnanlage-gruen"),
    dict(fn="14-verkaufen-bad-vilbel.html", path="immobilie-verkaufen-bad-vilbel", city="Bad Vilbel",
         title="Immobilie verkaufen in Bad Vilbel | dp immobilien management",
         desc="Immobilie verkaufen in Bad Vilbel? dp immobilien management – Ihr Partner für Haus und Wohnung in Bad Vilbel verkaufen. Jetzt beraten lassen!",
         eyebrow="Immobilie verkaufen · Bad Vilbel", intro_label="Rund um Bad Vilbel sind wir Ihr Profi für:",
         chips=["Immobilien vermitteln", "Haus verkaufen", "Wohnung verkaufen"],
         h1="Eine Immobilie verkaufen in Bad Vilbel: Zählen Sie auf unsere Expertise!",
         lead=["Wenn Sie eine Immobilie verkaufen wollen rund um Bad Vilbel, dann sind wir seit über 30 Jahren Ihr kompetenter Partner! Wir sind spezialisiert auf das Vermitteln von Immobilien in der Region – und wissen genau, wo wir die passenden Interessenten für Ihr Objekt finden.",
               "Eine Immobilie verkaufen in Bad Vilbel bedeutet: ein sicherlich lukratives Unterfangen! Denn Bad Vilbel ist seit einigen Jahren zu einer überaus beliebten Region geworden – sowohl für Privathaushalte als auch für Gewerbetreibende. Gerne möchten wir Sie dabei unterstützen, dass das Immobilien verkaufen in Bad Vilbel überzeugend reibungslos verläuft."],
         why_h="Warum dp immobilien management GmbH?",
         why=["Mehr als 30 Jahre Erfahrung in der Vermittlung von Immobilien", "Aus der Region – für die Region", "Umfangreiche Dienstleistungen im Bereich Immobilien"],
         haus_h="Wollen Sie Ihr Haus verkaufen in der Region Bad Vilbel?",
         haus=["<b>Wenn Sie Ihr Haus verkaufen wollen und rund um Bad Vilbel in kürzester Zeit eine überzeugende Auswahl an Kaufinteressenten zur Auswahl haben möchten, dann sind Sie bei der dp immobilien management GmbH an der richtigen Adresse!</b>",
               "Die professionelle, transparente und zuverlässige Immobilienvermittlung ist unser Metier. Wenn Sie Unterstützung benötigen, um Immobilien verkaufen zu können, sind wir in Bad Vilbel jederzeit persönlich für Sie da! Bei uns steht der Kunde immer im Vordergrund – und daher vermarkten wir Ihr Haus ganz individuell auf Sie und das Objekt zugeschnitten. Unsere Aufgabe ist es, Ihnen von Beginn an eine komplette Dienstleistungsauswahl bereitzustellen. Denn wir sind kein reines Maklerbüro, sondern vielmehr als Generalunternehmen aktiv – spezialisiert auf das Immobilien verkaufen wollen in Bad Vilbel."],
         haus_btn="Immobilien verkaufen in Bad Vilbel!",
         whg_h="Kontaktieren Sie uns, wenn Sie Ihre Wohnung verkaufen möchten in Bad Vilbel",
         whg=["Unsere Leistungspakete stehen Ihnen selbstverständlich auch beim Thema Wohnung verkaufen in Bad Vilbel uneingeschränkt zur Verfügung! Wie bei allen Immobilien, die wir im Auftrag unserer Kunden in Bad Vilbel verkaufen, ermitteln wir auch bei Wohnungen den marktgerechten Verkaufspreis. Wir erstellen professionelle, hochwertige Exposés mit ansprechenden Fotos und präsentieren Ihre Wohnung in allen gut sichtbaren Online-Immobilienportalen! Auch die Auswahl von zu Ihrer Wohnung passenden Kaufinteressenten übernehmen wir gerne für Sie, wenn Sie Ihre Immobilie verkaufen wollen und in Bad Vilbel auf einen optimalen Verkaufspreis setzen wollen. Auf Wunsch führen wir auch die anstehenden Besichtigungstermine in Ihrem Auftrag durch, organisieren für Sie alle wichtigen Notartermine und sind an Ihrer Seite, wenn es an Beurkundungen und die Übergabe an den neuen Eigentümer geht.",
              'Übrigens: Nicht nur beim Immobilie verkaufen in Bad Vilbel können Sie auf uns zählen! Auch wenn Sie eine <a href="/immobilienvermittlung/wohnung-vermieten-frankfurt-am-main">Wohnung vermieten</a> möchten oder auf der Suche nach einer zuverlässigen <a href="/hausverwaltung">Hausverwaltung</a> sind, bieten wir Ihnen leistungsstarke Fachkompetenz und ein begeisterndes Portfolio an Leistungen!'],
         whg_btn=None, img="fassade"),
]

for s in SELL:
    meta = {"path": s["path"], "title": s["title"], "description": s["desc"], "nav": "vermittlung",
            "crumbs": [["Immobilienvermittlung", "/immobilienvermittlung"], [f"Immobilie verkaufen {s['city']}", "/" + s["path"]]]}
    chips = "".join(f'<span class="chip">{c}</span>' for c in s["chips"])
    lead = "".join(f'<p class="lead">{p}</p>' for p in s["lead"])
    haus = "".join(f"<p>{p}</p>" for p in s["haus"])
    whg = "".join(f"<p>{p}</p>" for p in s["whg"])
    whg_btn = f'<div class="btn-row"><a class="btn" href="#bewertung">{s["whg_btn"]}</a></div>' if s["whg_btn"] else ""
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div class="stack">
      {{{{breadcrumb}}}}
      <span class="eyebrow">{s["eyebrow"]}</span>
      <h1>{s["h1"]}</h1>
      {lead}
      <div class="btn-row"><a class="btn" href="#bewertung">Jetzt beraten lassen!</a><a class="btn btn--ghost" href="tel:+4969403562400">069 / 4035624 - 00</a></div>
      <p class="muted" style="font-size:.9rem">{s["intro_label"]}</p>
      <div class="chips">{chips}</div>
    </div>
    <img class="page-hero__img" src="/assets/img/{s["img"]}.webp" alt="Wohnimmobilie in der Region {s["city"]}" width="1600" height="1066">
  </div>
</section>
<section class="section">
  <div class="wrap split split--top">
    <div class="stack">
      <span class="eyebrow">Haus verkaufen</span>
      <h2>{s["haus_h"]}</h2>
      {haus}
      <div class="btn-row"><a class="btn" href="#bewertung">{s["haus_btn"]}</a></div>
    </div>
    <div class="panel stack">
      <h2 style="font-size:var(--step-2)">{s["why_h"]}</h2>
      {checklist(s["why"])}
    </div>
  </div>
</section>
<section class="section section--surface">
  <div class="wrap split split--reverse">
    <div class="stack">
      <span class="eyebrow">Wohnung verkaufen</span>
      <h2>{s["whg_h"]}</h2>
      {whg}
      {whg_btn}
    </div>
    <img class="split__img reveal" src="/assets/img/schluessel-haus.webp" alt="Hausmodell mit Schlüssel" width="1600" height="1000" loading="lazy">
  </div>
</section>
{{{{> bewertung}}}}
{{{{> testimonial}}}}
{{{{> cta}}}}
"""
    write(s["fn"], meta, body)


# ---------------- Immobilienverwaltung: Bad Vilbel / Hanau / Offenbach ----------------
MGMT = [
    dict(fn="15-verwaltung-bad-vilbel.html", path="immobilienverwaltung-bad-vilbel", city="Bad Vilbel",
         title="Immobilienverwaltung Bad Vilbel | dp immobilien management",
         desc="Professionelle Haus- und Mietverwaltung in Bad Vilbel. Wählen Sie die dp immobilien management GmbH für Ihre Immobilien.",
         h1="Immobilienverwaltung Bad Vilbel – Ihr Vertrauen, unsere Verantwortung",
         lead=["Willkommen bei der dp immobilien management GmbH – Ihrem erfahrenen Partner für umfassende Immobilienverwaltung in Bad Vilbel. Mit einem tief verwurzelten Verständnis für die lokalen Immobilienmärkte bieten wir eine maßgeschneiderte Verwaltungslösung, die sicherstellt, dass Ihre Immobilien nicht nur erhalten, sondern in ihrem Wert gesteigert werden."],
         blocks=[("Hausverwaltung in Bad Vilbel, die Sie verstehen", "Unser Ziel ist es, Ihnen als Eigentümer das Leben leichter zu machen. Unsere Hausverwaltung Bad Vilbel ist darauf ausgelegt, Ihre Bedürfnisse zu erkennen und zu erfüllen. Dies bedeutet eine transparente Kommunikation und Berichterstattung sowie eine effiziente Bewirtschaftung Ihrer Immobilien."),
                 ("Mietverwaltung in Bad Vilbel mit Weitsicht", "Die Mietverwaltung Bad Vilbel beinhaltet mehr als nur das Sammeln von Mieten und das Verwalten von Nebenkostenabrechnungen. Wir sehen unsere Aufgabe darin, das Wohl Ihrer Mieter zu sichern und somit die Basis für eine langfristige Werterhaltung Ihrer Immobilien zu schaffen."),
                 ("Klare Kosten, transparente Hausverwaltung im Raum Bad Vilbel", "Wir glauben an Klarheit, speziell wenn es um die Kosten der Hausverwaltung in Bad Vilbel geht. Keine versteckten Gebühren, keine unerwarteten Kosten. Bei uns wissen Sie genau, was Sie für Ihr Geld erhalten – eine Leistung, die sich rechnet."),
                 ("Ihr Haus und Ihre Immobilienverwaltung in Bad Vilbel ist in guten Händen", "Jedes Haus ist so einzigartig wie seine Bewohner. Deshalb kümmern wir uns individuell und mit größtem Engagement darum, Ihre Immobilie zu verwalten in Bad Vilbel. Unser Fachwissen garantiert Ihnen eine professionelle Verwaltung, die den Wert Ihrer Liegenschaft erhöht.")],
         outro="Mit der dp immobilien management GmbH wählen Sie einen Partner, der die Vision Ihres Zuhauses teilt. Wir sind stolz darauf, unseren Kunden nicht nur exzellente Dienstleistungen zu bieten, sondern auch eine Partnerschaft auf Vertrauensbasis zu erleben. Kontaktieren Sie uns noch heute, um zu erfahren, wie wir Sie unterstützen können.",
         img="fassade"),
    dict(fn="16-verwaltung-hanau.html", path="immobilienverwaltung-hanau", city="Hanau",
         title="Immobilienverwaltung Hanau | dp immobilien management",
         desc="Ihre Experten für Immobilien- und Hausverwaltung in Hanau. Kompetent, transparent und persönlich – dp immobilien management GmbH.",
         h1="Immobilienverwaltung Hanau – Ihr Vertrauenspartner dp immobilien management GmbH",
         lead=["Die dp immobilien management GmbH steht für kompetente Betreuung rund um Ihre Immobilie in Hanau und Umgebung. Falls Sie auf der Suche nach einem zuverlässigen Partner sind, der mit fachlicher Expertise und persönlichem Engagement Ihre Immobilien verwaltet, sind Sie bei uns genau richtig.",
               "Hier sind die Gründe, warum wir die ideale Wahl für Ihr Immobilienmanagement sind."],
         blocks=[("Hausverwaltung in Hanau – professionell und persönlich", "Unser Ziel ist es, Ihnen als Eigentümer das Leben leichter zu machen. Unsere Hausverwaltung in Hanau ist darauf ausgelegt, Ihre Bedürfnisse zu erkennen und zu erfüllen. Dies bedeutet eine transparente Kommunikation und Berichterstattung sowie eine effiziente Bewirtschaftung Ihrer Immobilien."),
                 ("Mietverwaltung Hanau – effizient und transparent", "Die Mietverwaltung ist das A und O für die Werterhaltung Ihrer Immobilieninvestition. Unsere erfahrenen Fachkräfte sorgen für eine lückenlose Mietverwaltung, stellen die Rentabilität Ihrer Immobilien sicher und stehen Ihnen bei allen Fragen zur Seite."),
                 ("Kosten Hausverwaltung im Raum Hanau – faire und klare Kalkulation", "Wir verstehen, dass die Kostentransparenz bei der Auswahl des Immobilienverwalters eine entscheidende Rolle spielt. Deshalb bieten wir Ihnen faire und nachvollziehbare Preise für die Verwaltung Ihrer Häuser und Wohnanlagen an."),
                 ("Haus verwalten Hanau – wir behalten alles im Blick", "Das Verwalten eines Hauses erfordert ständige Aufmerksamkeit und ein umfassendes Verständnis aller relevanten Prozesse. Unsere Experten stellen sicher, dass sich Ihre Immobilien in Top-Zustand befinden und alle rechtlichen sowie finanziellen Angelegenheiten effizient gemanagt werden.")],
         outro="Indem Sie sich für die dp immobilien management GmbH entscheiden, setzen Sie auf eine nachhaltige Wertsteigerung Ihrer Immobilien. Unser Team arbeitet Hand in Hand mit Eigentümern, um sicherzustellen, dass Ihre Erwartungen nicht nur erfüllt, sondern übertroffen werden.",
         img="wohnanlage-gruen"),
    dict(fn="17-verwaltung-offenbach.html", path="immobilienverwaltung-offenbach", city="Offenbach",
         title="Immobilienverwaltung Offenbach | dp immobilien management",
         desc="Professionelle Hausverwaltung in Offenbach – dp immobilien management GmbH. Ihr Eigentum optimal betreut.",
         h1="dp immobilien management GmbH – Ihr Partner für Immobilienverwaltung in Offenbach",
         lead=["Willkommen bei der dp immobilien management GmbH, Ihrem Experten für Immobilienverwaltung in Offenbach. Mit unserer langjährigen Erfahrung in der Haus- und Mietverwaltung bieten wir maßgeschneiderte Lösungen, die Ihre Erwartungen nicht nur erfüllen, sondern übertreffen."],
         blocks=[("Unser Angebot – Hausverwaltung Offenbach", "In Offenbach und Umgebung vertrauen Immobilienbesitzer auf die dp immobilien management GmbH, wenn es um die fachgerechte Verwaltung ihrer Wohnobjekte geht. Wir verstehen die Einzigartigkeit jeder Immobilie und sorgen mit unserer Expertise dafür, dass Ihre Immobilien optimal betreut werden."),
                 ("Mietverwaltung Offenbach – Ihre Rendite im Blick", "Unser Service umfasst nicht nur die klassische Hausverwaltung, sondern auch die sorgfältige Mietverwaltung. Wir übernehmen für Sie die Mieterkorrespondenz, die Betriebskostenabrechnung sowie die Sicherstellung der Instandhaltung Ihrer Immobilien."),
                 ("Kosten Hausverwaltung Offenbach – Transparenz und Fairness", "Die dp immobilien management GmbH steht für transparente und faire Kostenstrukturen in Offenbach. Wissen Sie stets, wofür Sie zahlen und welche Leistungen Sie für Ihr Geld erhalten."),
                 ("Ihr Haus in guten Händen – Haus verwalten Offenbach", "Mit dem Rundum-sorglos-Paket der dp immobilien management GmbH können Sie sich entspannt zurücklehnen. Wir kümmern uns um alle Angelegenheiten rund um die Verwaltung Ihrer Immobilie.")],
         outro="Als dp immobilien management GmbH stellen wir Ihnen nicht nur herausragende Immobilienverwaltungsdienste zur Verfügung, sondern auch eine Partnerschaft, auf die Sie sich verlassen können. Kontaktieren Sie uns, und erfahren Sie, wie wir auch Ihre Immobilien in Offenbach professionell verwalten können. Unsere Experten sind bereit, Ihnen die Last der Immobilienverwaltung abzunehmen und den Wert Ihrer Investition zu maximieren.",
         img="strasse"),
]

for m in MGMT:
    meta = {"path": m["path"], "title": m["title"], "description": m["desc"], "nav": "hausverwaltung",
            "crumbs": [["Hausverwaltung", "/hausverwaltung"], [f"Immobilienverwaltung {m['city']}", "/" + m["path"]]]}
    lead = "".join(f'<p class="lead">{p}</p>' for p in m["lead"])
    blocks = "".join(f'<div class="stack reveal"><h2 style="font-size:var(--step-2)">{h}</h2><p>{t}</p></div>' for h, t in m["blocks"])
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div class="stack">
      {{{{breadcrumb}}}}
      <span class="eyebrow">Hausverwaltung ist Vertrauenssache · {m["city"]}</span>
      <h1>{m["h1"]}</h1>
      {lead}
      <div class="btn-row"><a class="btn" href="/kontakt">Jetzt Kontakt aufnehmen</a><a class="btn btn--ghost" href="/angebot">Angebot anfragen</a></div>
    </div>
    <img class="page-hero__img" src="/assets/img/{m["img"]}.webp" alt="Wohnimmobilie in {m["city"]}" width="1600" height="1066">
  </div>
</section>
<section class="section">
  <div class="wrap split split--top">
    <div class="stack">
      <span class="eyebrow">30 Jahre Erfahrung im Umgang mit Immobilien</span>
      <h2>Ihre Vorteile durch unsere Immobilienverwaltung in {m["city"]}:</h2>
    </div>
    <div class="panel">{{{{> local-advantages}}}}</div>
  </div>
</section>
<section class="section section--surface">
  <div class="wrap stack-lg">
    <div class="grid-2">{blocks}</div>
    <p class="lead measure" style="color:var(--ink)">{m["outro"]}</p>
  </div>
</section>
{{{{> safety}}}}
{{{{> services3}}}}
{{{{> cta}}}}
"""
    write(m["fn"], meta, body)


# ---------------- Jobs: Frankfurt / Bad Vilbel / Hanau / Offenbach ----------------
JOBS = [
    dict(fn="20-job-frankfurt.html", path="jobs/immobilienverwalter-frankfurt", city="Frankfurt",
         title="Immobilienverwalter Jobs Frankfurt | dp immobilien management",
         desc="Top-Jobs in der Immobilienverwaltung – jetzt bei der dp immobilien management GmbH in Frankfurt bewerben.",
         h1="Karriere bei dp immobilien – Immobilienverwalter Jobs in Frankfurt am Main", intro=[],
         sections=[("Hausverwaltung Jobs Frankfurt am Main – Werden Sie Teil unseres Teams", ["Sie haben eine Leidenschaft für die Immobilienbranche und möchten Ihre Karriere auf das nächste Level bringen? Die dp immobilien management GmbH sucht engagierte Talente, die ihre Expertise in der Hausverwaltung in Frankfurt einbringen möchten. Mit einem starken Fokus auf professionelle Entwicklung und einem dynamischen Arbeitsumfeld bieten wir vielfältige Chancen für Ihre berufliche Entfaltung."]),
                   ("Stellenangebot Hausverwaltung Frankfurt am Main – Unsere Erwartungen", ["Bei der dp immobilien management GmbH erwarten wir Exzellenz, Einsatzbereitschaft und den Willen zur ständigen Weiterentwicklung. Wir sind auf der Suche nach Teamspielern, die den Wert von Immobilien erkennen und respektieren und die Erwartungen unserer Kunden nicht nur erfüllen, sondern übertreffen."]),
                   ("Stellenangebot Immobilienverwaltung in Frankfurt am Main – Das bieten wir", ["Treten Sie ein in eine Welt, in der Ihre Arbeit geschätzt wird und Sie täglich dazu beitragen können, die Landschaft der Immobilienverwaltung zu gestalten. Wir bieten attraktive Benefits, marktgerechte Vergütung und die Möglichkeit, an spannenden Projekten in Frankfurt und Umgebung zu arbeiten."])]),
    dict(fn="21-job-bad-vilbel.html", path="jobs/immobilienverwalter-bad-vilbel", city="Bad Vilbel",
         title="Jobs Immobilienverwalter Bad Vilbel | dp immobilien management",
         desc="Starten Sie Ihre Karriere in der Immobilienverwaltung bei der dp immobilien management GmbH – auch für Bewerber aus Bad Vilbel.",
         h1="Karriere bei dp immobilien – Jobs als Immobilienverwalter in Bad Vilbel", intro=[],
         sections=[("Hausverwaltung Jobs Bad Vilbel", ["Die dp immobilien management GmbH ist ein renommiertes Unternehmen mit Sitz in der pulsierenden Metropole Frankfurt am Main. Wir sind stolz darauf, eine der führenden Adressen für professionelle Immobilienverwaltung in der Region zu sein. Unser Team aus erfahrenen Spezialisten widmet sich mit Leidenschaft der Verwaltung und Betreuung verschiedener Immobilienobjekte.", "Ihre Karriere in der Immobilienbranche kann hier bei uns neue Höhen erreichen. Sind Sie bereit für eine neue Herausforderung und möchten Teil eines dynamischen und erfolgreichen Teams werden? Dann sollten Sie sich unsere aktuellen Stellenangebote genauer anschauen!"]),
                   ("Stellenangebot Hausverwaltung Bad Vilbel", ["Bei der dp immobilien management GmbH bieten wir Ihnen nicht nur einen Job, sondern eine Karriereperspektive. Unsere Mitarbeiter genießen vielseitige Aufgabenfelder in einem zukunftsorientierten Arbeitsumfeld. Wir legen Wert auf individuelle Weiterbildung und bieten attraktive Arbeitsbedingungen.", "Bei uns finden Sie flache Hierarchien und ein kollegiales Miteinander. Wir wissen, dass unsere Mitarbeiter unser größtes Kapital sind, und fördern daher den Dialog und Austausch innerhalb des Teams."]),
                   ("Stellenangebot Immobilienverwaltung Bad Vilbel", ["Unsere Stellenangebote richten sich an Persönlichkeiten, die sowohl fachlich als auch menschlich in unser Unternehmen passen. Organisationstalent, Kommunikationsfähigkeit und eine selbstständige Arbeitsweise sind uns ebenso wichtig wie branchenspezifische Kenntnisse. Erfahrungen in der Immobilienverwaltung sind vorteilhaft, aber auch Quereinsteiger mit der richtigen Einstellung und der Willenskraft zum Lernen haben bei uns Chancen. Ein ausgeprägtes Dienstleistungsverständnis und eine hohe Kundenorientierung sind für uns unerlässlich."]),
                   ("Werden Sie Teil der dp immobilien management GmbH", ["Wir suchen Menschen, die mit ihrem Engagement und ihrem Know-how zur dp immobilien management GmbH beitragen und mit uns wachsen wollen. Wenn Sie eine Karriere in der Immobilienverwaltung anstreben und Sie die Stelle anspricht, freuen wir uns über Ihre aussagekräftige Bewerbung."])]),
    dict(fn="22-job-hanau.html", path="jobs/immobilienverwalter-hanau", city="Hanau",
         title="Jobs Immobilienverwalter Hanau | dp immobilien management",
         desc="Starten Sie Ihre Karriere in der Immobilienverwaltung mit den Jobangeboten der dp immobilien management GmbH – auch für Bewerber aus Hanau.",
         h1="Stellenangebote Immobilienverwaltung Hanau bei dp immobilien",
         intro=["Willkommen auf der Karriereseite der dp immobilien management GmbH in Frankfurt am Main, dem Ort, an dem Ihre berufliche Zukunft in der Immobilienbranche Gestalt annimmt. Wenn Sie ambitioniert, engagiert und bereit sind, in der dynamischen Welt der Immobilienverwaltung Fuß zu fassen, dann bieten wir Ihnen die Möglichkeit, sich mit uns weiterzuentwickeln und zugleich unser starkes Team in Hanau zu unterstützen."],
         sections=[("Jobs Immobilienverwalter in Hanau – Beginnen Sie Ihre Karriere bei uns", ["Die dp immobilien management GmbH ist auf der Suche nach talentierten Fachkräften, die Spaß daran haben, die Immobilien unserer Kunden fachgerecht zu verwalten und zu betreuen. Unsere Immobilienverwalter-Jobs in Hanau bieten vielfältige Herausforderungen und Entwicklungsmöglichkeiten in einem professionellen Arbeitsumfeld."]),
                   ("Hausverwaltung Jobs Hanau – Werden Sie Teil eines starken Teams", ["Als Teil unseres Teams haben Sie die Chance, die Hausverwaltung aus unterschiedlichen Perspektiven kennenzulernen. Unsere Hausverwaltung-Jobs in Hanau sind zugeschnitten auf Proaktivität, Serviceorientierung und Teamgeist. Wir schätzen die individuelle Entwicklung jedes Mitarbeiters und bieten Schulungen und Weiterbildungsmöglichkeiten."]),
                   ("Stellenangebot Hausverwaltung – Ihre Chance auf professionelles Wachstum in Hanau", ["Unser Stellenangebot in der Hausverwaltung in Hanau umfasst die gesamte Bandbreite der Immobilienbetreuung – von der technischen und kaufmännischen Verwaltung bis hin zum Objektmanagement. Wenn Sie in einer Branche mit hohem Wachstumspotenzial durchstarten möchten, freuen wir uns auf Ihre Bewerbung."]),
                   ("Stellenangebot Immobilienverwaltung Hanau – Entdecken Sie Ihre Möglichkeiten", ["In Hanau bieten wir spannende Perspektiven für alle, die in der Immobilienverwaltung tätig werden möchten. Bei der dp immobilien management GmbH erwartet Sie ein berufliches Umfeld, in dem Sie Ihre Leidenschaft für Immobilien voll ausleben können. Alle offenen Stellen und die dazu passenden Anforderungsprofile finden Sie auf unserer Karriereseite."])]),
    dict(fn="23-job-offenbach.html", path="jobs/immobilienverwalter-offenbach", city="Offenbach",
         title="Jobs Immobilienverwalter Offenbach | dp immobilien management",
         desc="Entdecken Sie bei der dp immobilien management GmbH Ihre neue Karriere im Bereich Immobilienverwaltung – auch für Bewerber aus Offenbach.",
         h1="Karriere bei dp immobilien – Jobs Immobilienverwalter Offenbach",
         intro=["Willkommen auf der Karriereseite der dp immobilien management GmbH, dem Experten im Bereich Immobilienverwaltung mit Sitz im Herzen von Frankfurt am Main. Sie möchten Teil unseres dynamischen Teams werden und Ihre Fähigkeiten in die professionelle Verwaltung und Betreuung von Immobilien einbringen? Entdecken Sie spannende Karrieremöglichkeiten und entfalten Sie Ihr volles Potenzial mit uns!"],
         sections=[("Stellenangebot Hausverwaltung Offenbach", ["Bei der dp immobilien management GmbH verbinden wir traditionelle Werte mit modernen Managementmethoden. Wir sind ständig auf der Suche nach motivierten Fachkräften, die unsere Leidenschaft für Immobilien teilen und unseren Kunden erstklassige Dienstleistungen bieten möchten. Informieren Sie sich über unsere aktuellen Stellenangebote in der Hausverwaltung in und um Offenbach."]),
                   ("Was wir bieten", ["__LIST__Interessante Aufgaben und Projekte in der Immobilienverwaltung|Attraktive Arbeitsbedingungen und leistungsgerechte Vergütung|Persönliche und fachliche Weiterbildungsangebote|Ein dynamisches, unterstützendes Team|Moderne Arbeitsplätze in zentraler Lage"]),
                   ("Bewerbungsprozess", ["Möchten Sie mehr über den Bewerbungsprozess erfahren und ein Teil unseres Teams werden? Senden Sie uns Ihre aussagekräftigen Unterlagen zu und beginnen Sie ein neues Kapitel Ihrer Karriere bei der dp immobilien management GmbH!"]),
                   ("Stellenangebot Immobilienverwaltung Offenbach", ["Unser Team ist das Fundament unseres Erfolgs. Wir investieren nicht nur in Immobilien, sondern vor allem in Menschen. Werden Sie Teil unserer Erfolgsgeschichte und gestalten Sie die Zukunft der Immobilienverwaltung aktiv mit. Unsere Stellenangebote in der Immobilienverwaltung richten sich an erfahrene Experten und ambitionierte Einsteiger."]),
                   ("Ihre Karrierechance in der Immobilienbranche in Offenbach", ["Die dp immobilien management GmbH steht für vielfältige Entwicklungsmöglichkeiten und individuelle Förderung. Als fortschrittlicher Arbeitgeber bieten wir zahlreiche Weiterbildungskurse und Zertifizierungsprogramme an. Starten Sie Ihre Karriere in der Immobilienverwaltung bei uns und profitieren Sie von einer Kultur, die Initiative und Engagement wertschätzt."]),
                   ("Werden Sie Teil unseres Teams!", ["Wir freuen uns auf neue Kollegen, die mit Engagement und Innovationskraft unsere Vision einer serviceorientierten Immobilienverwaltung teilen. Finden Sie heraus, wie Sie mit Ihren Fähigkeiten und Ihrer Persönlichkeit unser Team bereichern können. Wir bieten eine offene und kollegiale Arbeitsatmosphäre, in der jede Meinung zählt."])]),
]


def para(p):
    if p.startswith("__LIST__"):
        return checklist(p[8:].split("|"))
    return f"<p>{p}</p>"


for j in JOBS:
    meta = {"path": j["path"], "title": j["title"], "description": j["desc"], "nav": "jobs",
            "crumbs": [["Karriere", "/jobs"], [f"Immobilienverwalter {j['city']}", "/" + j["path"]]]}
    intro = "".join(f'<p class="lead">{p}</p>' for p in j["intro"])
    secs = "".join(f'<div class="stack"><h2 style="font-size:var(--step-2)">{h}</h2>{"".join(para(p) for p in ps)}</div>' for h, ps in j["sections"])
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div class="stack">
      {{{{breadcrumb}}}}
      <span class="eyebrow">Jobs bei dp immobilien management</span>
      <h1>{j["h1"]}</h1>
      {intro}
      <div class="btn-row"><a class="btn" href="mailto:info@dp-immobilien-management.de?subject=Bewerbung">Jetzt E-Mail schreiben</a></div>
    </div>
    <img class="page-hero__img" src="/assets/img/teamwork.webp" alt="Zusammenarbeit im Team" width="1600" height="1092">
  </div>
</section>
<section class="section">
  <div class="wrap grid-2" style="grid-template-columns:minmax(0,1.3fr) minmax(0,0.9fr);align-items:start">
    <div class="stack-lg">{secs}
      <div class="btn-row"><a class="btn" href="mailto:info@dp-immobilien-management.de?subject=Bewerbung">Jetzt E-Mail schreiben</a></div>
    </div>
    {{{{> jobcontact}}}}
  </div>
</section>
"""
    write(j["fn"], meta, body)

print("ok")
