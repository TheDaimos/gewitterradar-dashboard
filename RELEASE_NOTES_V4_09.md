# Gewitterradar Dashboard V4.09 · 2026/09

V4.09 synchronisiert die Dashboard-/HACS-Auslieferung bytegenau mit dem öffentlichen kanonischen Gewitterradar V4.09.

## Neu in V4.09

- Kartenansichten Standard, Groß und Vollbild mit geräte-/browserbezogener Standardansicht.
- Separates Gewitter-Kartenfenster mit aktuell gewählter Karte und Kompass.
- Im Vollbild unabhängig ein-/ausblendbare und frei verschiebbare Instrumente für Kompass und Medaillon.
- Frei bewegliche Standort-Pille mit adaptivem, responsivem Standortmenü.
- Cluster-Auflösung und Cluster-Navigation unter Kartendarstellung.
- Finaler viewportbasierter Touch-Scrollbereich für Radien.
- Einheitliche ×-Löschschaltflächen für Bezeichnung, Breitengrad und Längengrad.
- Kartenansicht und Hilfe über den vollständigen Produktumfang von 19 Sprachvarianten synchronisiert.
- Geschützte Medaillon-Diagnose auf das produktive trend-icon begrenzt, damit das zusätzliche Vollbild-Medaillon die Kalibrierung nicht verfälschen kann.

## Installation

- HACS-Repository: TheDaimos/gewitterradar-dashboard als Dashboard.
- JavaScript-Modul: /hacsfiles/gewitterradar-dashboard/gewitterradar.js.
- Das bestehende V4.07-Package bleibt weiterhin die aktuelle Dashboard-Helferbasis und wird manuell nach /config/packages/app_gewitterradar_v4_07_pkg.yaml kopiert.
- V4.09 führt kein neues YAML-Helferpaket ein.

## Release-Identität

- Gewitterradar: V4.09
- Frontend: 2.238.824 Bytes
- Frontend SHA256: c9f01617d3a19519ecc44f84a7bf71aa3056dee57245af860becd893c652fce2
- Locale SHA256: dc6506291dd4cfe75e3b9c829fb42f21062511fb574d335af438e6c42711802e
- Kanonischer Produktcommit: a6a5b68ebc289f04217bc5abb55c46422dce4e4c
- V4.07-Package SHA256: 1b705c5686e6a7be6dfb36717903df551d4f9f93787c39bd12bddf00aefae694

Die Laufzeitdateien dist/gewitterradar.js und dist/locales/about-locales.js sind bytegleich mit der Dashboard-Ausleitung des kanonischen V4.09-Produktcommits.

Es werden keine benutzerdefinierten GitHub-Release-Artefakte veröffentlicht. HACS installiert weiterhin den vollständigen getaggten dist/-Stand.
