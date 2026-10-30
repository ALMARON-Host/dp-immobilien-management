# dp immobilien management – Relaunch (Entwurf 1)

Neuaufbau von www.dp-immobilien-management.de: neues Design, dieselben Inhalte, alle Seiten übernommen.

**Vorschau:** https://almaron-host.github.io/dp-immobilien-management/ (für Suchmaschinen gesperrt)

## Bedienung

| Aufgabe | Befehl |
|---|---|
| Lokal bauen (per Doppelklick auf `site/index.html` ansehen) | `python src\build.py` |
| Vorschau online aktualisieren | `powershell -ExecutionPolicy Bypass -File .\deploy.ps1` |
| Live-Version für den Webserver | `python src\build.py --pretty` → Inhalt von `site/` hochladen |

Kein Node, kein Framework: nur Python 3 (Standardbibliothek). Die fertige Seite ist reines HTML/CSS/JS.

## Aufbau

```
src/pages/*.html        Inhalt jeder Seite (JSON-Kopf mit Pfad, Title, Description, Brotkrumen)
src/partials/*.html     Wiederkehrende Bausteine (Kontakt-Band, Karte, Bewertungs-Formular …)
src/build.py            Generator: Kopf, Navigation, Footer, relative Links, Sitemap, robots.txt, .htaccess
src/local_pages.py      Erzeugt die 9 Regionalseiten (Hanau, Bad Vilbel, Offenbach) aus den Originaltexten
src/faq.py              Erzeugt die FAQ-Seite inkl. strukturierter Daten
src/legal_pages.py      Übernimmt die Datenschutzerklärung aus dem Original-HTML
src/htaccess.txt        301-Weiterleitungen der alten Joomla-Adressen
assets/                 CSS, JS, Schriften (lokal, DSGVO), optimierte Bilder (WebP), PDFs
_quelle/                Originale: HTML, Texte, Bilder der alten Seite (nicht im Git)
```

## Seiten (29)

Alle 24 Seiten der alten Website plus 5 neue:

- Übernommen, gleiche URL: Start, Über uns, Hausverwaltung, WEG-, Miet-, Gewerbeverwaltung, Immobilienvermittlung, Vermieten, Verkaufen, Verkaufen Hanau/Bad Vilbel, Jobs, Ausbildung, Referenzen, Kontakt, Impressum, Datenschutz
- Übernommen, neue saubere URL (301 per `.htaccess`): Immobilienverwaltung Bad Vilbel/Hanau/Offenbach, Jobs Immobilienverwalter Frankfurt/Bad Vilbel/Hanau/Offenbach
- **Neu:** Verwalterwechsel, Angebotsanfrage (Assistent), Notfall & Schadensmeldung, Häufige Fragen, 404-Seite

## Neue Elemente

- Notfall-Button im Kopf + mobile Aktionsleiste (Anrufen / Portal / Notfall)
- Live-Anzeige „Jetzt erreichbar / Büro nicht besetzt“ nach Geschäftszeiten (Europe/Berlin)
- Schadensmelder: 3 Klicks zum richtigen Meldeweg (Notfallnummer, Kundenportal, 112 bei Gas)
- Zielgruppen-Einstieg auf der Startseite (WEG, Vermieter, Mieter, Verkäufer)
- Mehrstufige Angebotsanfrage und persönliche Wertermittlung statt Online-Rechner
- Vorher/Nachher-Regler für die Sanierungsprojekte, Filter für Referenzen
- Karte des Einzugsgebiets als eigene Grafik (kein Google Maps, kein Cookie-Banner nötig)
- Verwalterwechsel in 5 Schritten + Übergabe-Checkliste
- FAQ mit strukturierten Daten (Google), LocalBusiness-Daten, Sitemap
- Hell/Dunkel-Modus, Tastaturbedienung, sichtbarer Fokus, reduzierte Bewegung (Barrierefreiheit)
- Schriften lokal eingebunden (keine Google-Server), Bilder als WebP (~4 MB statt ~20 MB)

## Offene Punkte vor dem Livegang

1. **Zahlen widersprechen sich auf der alten Seite:** Über uns „rd. 80 Objekte / ca. 3.000 Einheiten“, Referenzen „rd. 40 Objekte / ca. 1.000 Einheiten“, Startseite „rund 40 Objekte“ (WEG). Bitte klären; im Entwurf wie im Original übernommen, Kennzahlenband nutzt die Über-uns-Werte.
2. **Formulare** (Kontakt, Angebot, Wertermittlung) senden noch nichts. Anbindung nötig (z. B. PHP-Mailer beim Hoster oder Formspree).
3. **Datenschutzerklärung** unverändert übernommen. Sie nennt u. a. Facebook und Google Analytics, die die neue Seite nicht nutzt. Neu fassen lassen (neue Formulare, Hosting, lokale Schriften).
4. **Impressum:** „§ 5 TMG“ auf „§ 5 DDG“ aktualisiert (TMG seit Mai 2024 ersetzt), Rest unverändert.
5. **Stellenanzeige-PDF** stammt von 2019 (`190814_Stellenanzeige-Stepstone.pdf`). Aktuell?
6. **Neue Texte prüfen lassen:** Verwalterwechsel, Notfall/Schadensmelder, FAQ, Angebots- und Bewertungsassistent, Zielgruppen-Kacheln.
7. **Kleine Korrekturen** gegenüber dem Original: Tippfehler (z. B. „technischne“, „Schadesfällen“, „Initiativebwerbungen“, „vermietenn“, „waren“→„wahren“), Hanau-Seite nannte versehentlich „Hausverwaltung Bad Vilbel“, Jobseiten nannten „dp Immobilien GmbH“ → „dp immobilien management GmbH“.
8. Daniel Budecker hat nur ein Platzhalterbild; Teamfotos ggf. aktualisieren.
9. Bildrechte der Stockfotos (Fotolia/Adobe Stock) für die neue Domain prüfen.

## Bewertungen (Stand 30.10.2026)

Eingebaut sind nur belegbare Angaben. Pflege in `src/partials/rating.html`, `testimonial.html`, `safety.html`.

| Quelle | Wert | Fundstelle |
|---|---|---|
| Google (über JACASA) | 4,7 / 5 bei 34 Bewertungen, aktualisiert 26.10.2026 | jacasa.de/hausverwaltung/dp-immobilien-management-frankfurt-am-main |
| ProvenExpert (Google-Import) | Google Maps 5,0 / 5 bei 32 Bewertungen (16.10.2026) | provenexpert.com/de-de/dp-immobilien-management-gmbh/ |
| ImmoScout24 | 1 veröffentlichte Bewertung, 5,0, Eigentümer:in, 11.07.2021 | immobilienscout24.de/anbieter/profil/dp-immobilien-management-gmbh |

Offen:
- Die Google-Werte unterscheiden sich je nach Portal (4,7 / 34 vs. 5,0 / 32). Vor Livegang im Google-Unternehmensprofil prüfen und Zahl anpassen.
- Weitere Zitate: Die Texte der Google-Rezensionen sind nur im Google-Profil einsehbar. Der Kunde kann die besten freigeben, dann ergänzen wir sie in `testimonial.html`.
- ImmoScout24 nennt als Erreichbarkeit Mo–Do 9–17 Uhr, Fr 9–13 Uhr, die alte Website dagegen Mo–Fr 9–12 Uhr und Di + Do 14–16 Uhr. Welche Zeiten gelten? (wichtig für die Live-Anzeige „Büro öffnet …“)
