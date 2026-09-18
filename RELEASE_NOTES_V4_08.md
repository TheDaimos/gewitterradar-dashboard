# Gewitterradar Dashboard V4.08 · 2026/09

V4.08 synchronisiert die Dashboard-/HACS-Auslieferung bytegenau mit dem öffentlichen kanonischen Gewitterradar V4.08.

## Neu in V4.08

- Cluster-Auflösungsprofile **Früh**, **Ausgewogen**, **Spät** und **Klassisch · V4.07.56**.
- Cluster-Navigation mit 5–3600 Sekunden oder **∞**.
- Zuverlässige Countdown-/Unendlich-Umschaltung auf Desktop und Touch ohne zusätzlichen Cluster-Sprung.
- Überarbeiteter Repository-/HACS-Auftritt mit absolut referenziertem Branding und bestehender Hero-Grafik.

## Installation

- HACS-Repository: `TheDaimos/gewitterradar-dashboard` als **Dashboard**.
- JavaScript-Modul: `/hacsfiles/gewitterradar-dashboard/gewitterradar.js`.
- Das bestehende V4.07-Package bleibt weiterhin die aktuelle Dashboard-Helferbasis und wird manuell nach `/config/packages/app_gewitterradar_v4_07_pkg.yaml` kopiert.
- V4.08.40 führte kein neues YAML-Helferpaket ein.

## Release-Identität

- Gewitterradar: **V4.08**
- Frontend: **2.028.645 Bytes**
- Frontend SHA256: `b75390652fae4aa98c77162fb207d97ece408ab617bbf107bcb0f3b9466a691f`
- Locale SHA256: `a57493b6291671696aeb87c267595e3ce5fede987546f702d7883ef6f07bd288`
- Kanonischer Produktcommit: `27da94e5043a365dbe8ea5c5e2224327165750fa`
- V4.07-Package SHA256: `1b705c5686e6a7be6dfb36717903df551d4f9f93787c39bd12bddf00aefae694`

Die Laufzeitdateien `dist/gewitterradar.js` und `dist/locales/about-locales.js` sind bytegleich mit der Dashboard-Ausleitung des kanonischen V4.08-Produktcommits.

Es werden keine benutzerdefinierten GitHub-Release-Artefakte veröffentlicht. HACS installiert weiterhin den vollständigen getaggten `dist/`-Stand.

Neue Produktentwicklung beginnt ausschließlich auf **V4.09.xx**.
