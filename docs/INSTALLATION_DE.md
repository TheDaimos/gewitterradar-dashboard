# Gewitterradar V4.05 – Installation (DE)

## Voraussetzungen

- Laufende Home-Assistant-Installation.
- Blitzortung.org-Integration mit den benötigten Blitz-/Zählerentitäten.
- Standard-Zähler der Beispielkonfiguration: `sensor.home_lightning_counter`.

## Repository-Aufteilung

Die öffentliche Verteilung ist getrennt:

- **Native Home-Assistant-Integration:** `TheDaimos/gewitterradar`
- **Dashboard/Card:** `TheDaimos/gewitterradar-dashboard`

V4.04 bleibt als eingefrorene Regression-Basis unverändert erhalten. V4.05 ist das aktuelle stabile Dashboard-Release.

HACS verwendet für das Dashboard:

```text
/config/www/community/gewitterradar-dashboard/
/hacsfiles/gewitterradar-dashboard/
```

**Wichtig für Installationen von vor der Repository-Umbenennung:** Den alten HACS-Dashboard-Eintrag `TheDaimos/gewitterradar` nicht aktualisieren und nicht neu herunterladen. Dieser Repository-Name gehört inzwischen zur nativen Home-Assistant-Integration. Stattdessen `TheDaimos/gewitterradar-dashboard` als benutzerdefiniertes **Dashboard**-Repository hinzufügen, dort die aktuelle Version installieren und zuerst `/hacsfiles/gewitterradar-dashboard/gewitterradar.js` prüfen. Erst danach den alten Dashboard-Eintrag bzw. die alte Ressource entfernen. Siehe [`REPOSITORY_RENAME.md`](REPOSITORY_RENAME.md).

## HACS-Updatekanal

Für normale Installationen und Updates die standardmäßig angebotene **Latest / neueste Version** verwenden. Aktuell ist dies **V4.05**. Eine ältere feste Version nur für einen bewussten Rückschritt auswählen.

## Variante A: Installation oder Update über HACS

1. `TheDaimos/gewitterradar-dashboard` in HACS als benutzerdefiniertes Repository vom Typ **Dashboard** hinzufügen, falls noch nicht vorhanden.
2. Gewitterradar als **Latest / neueste Version** installieren bzw. das angebotene Update auf V4.05 durchführen.
3. HACS installiert `gewitterradar.js`, den vollständigen Ordner `assets/` und `app_gewitterradar_pkg.yaml` nach `/config/www/community/gewitterradar-dashboard/`.
4. Wenn das YAML-Helper-Package verwendet wird, `app_gewitterradar_pkg.yaml` nach `/config/packages/app_gewitterradar_pkg.yaml` kopieren. Kopieren wird empfohlen, damit die HACS-Ausgangsdatei erhalten bleibt.
5. Nach einer Package-Änderung Home Assistant vollständig neu starten.
6. Browser-/Companion-App-Cache bei Bedarf neu laden.

Die HACS-Struktur enthält mindestens:

```text
/config/www/community/gewitterradar-dashboard/
├── app_gewitterradar_pkg.yaml
├── gewitterradar.js
└── assets/
    ├── gewitterradar-about-dedication-v4.webp
    ├── gewitterradar-about-hero-v2.webp
    ├── gewitterradar-brand-icon.png
    ├── gewitterradar-compass-frame-v1.png … v5.png
    ├── gewitterradar-compass-selector-frame-v1.png … v5.png
    ├── gewitterradar-trend-arrow.png
    └── gewitterradar-trend-medallion.png
```

V4.05 verwendet insgesamt **15 lokale Grafik-Assets**.

Die Lovelace-Moduladresse lautet:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

### Warum bleibt das Package ein manueller Schritt?

Gewitterradar ist in HACS als **Dashboard-Repository** eingebunden. HACS installiert dessen Dateien nach `/config/www/community/gewitterradar-dashboard/`, darf aber keine Home-Assistant-Konfigurationsdatei direkt nach `/config/packages/` deployen.

Die gepflegte Originaldatei ist `home-assistant/app_gewitterradar_pkg.yaml`; `dist/app_gewitterradar_pkg.yaml` ist die byte-identische HACS-Kopie. Die CI prüft diese Gleichheit.

In `configuration.yaml` muss bei Nutzung von Packages die Einbindung vorhanden sein:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Wenn der Block bereits existiert, keinen zweiten `homeassistant:`-Hauptschlüssel anlegen.

Die bestehenden Helper-IDs `lightning_detection_*` bleiben bewusst erhalten. Das Package-Verteilungsmodell ist gegenüber V4.04 unverändert.

## Variante B: Manuelle Installation

### 1. JavaScript und Assets kopieren

- `gewitterradar-card-v4_05.js` nach `/config/www/gewitterradar/gewitterradar-card-v4_05.js` kopieren.
- Den vollständigen Inhalt von `dist/assets/` nach `/config/www/gewitterradar/assets/` kopieren.

### 2. Lovelace-Ressource eintragen

Als JavaScript-Modul:

```text
/local/gewitterradar/gewitterradar-card-v4_05.js?v=4_05
```

### 3. Home-Assistant-Package installieren

Falls das YAML-Helper-Package verwendet wird, `home-assistant/app_gewitterradar_pkg.yaml` nach `/config/packages/app_gewitterradar_pkg.yaml` kopieren. Alternativ kann die identische Datei `dist/app_gewitterradar_pkg.yaml` verwendet werden. Danach Home Assistant vollständig neu starten.

## Gewitterradar-View – Beispiel

```yaml
title: Gewitterradar
path: gewitterradar
icon: mdi:weather-lightning
type: panel
cards:
  - type: vertical-stack
    cards:
      - type: custom:gewitterradar-card
        counter_entity: sensor.home_lightning_counter
        radius_entity: input_number.lightning_detection_observation_radius
        compass_mode_entity: input_boolean.lightning_detection_compass_nearest_strike
```

## Recorder-Schutz empfohlen

Diese Konfiguration gehört in `configuration.yaml`:

```yaml
recorder:
  exclude:
    entity_globs:
      - "geo_location.lightning_strike*"
    entities:
      - sensor.home_lightning_distance
      - sensor.home_lightning_azimuth
      - sensor.home_lightning_counter
```

Wenn bereits ein `recorder:`-Block existiert, die Einträge dort ergänzen und keinen zweiten Hauptschlüssel anlegen. Der Ausschluss verhindert die dauerhafte Recorder-/History-Speicherung, ohne die Live-Zustände für Gewitterradar abzuschalten.

## Ersttest nach V4.05

- HACS bzw. die Karte zeigt `V4.05`.
- `/config/www/community/gewitterradar-dashboard/` enthält `gewitterradar.js`, `app_gewitterradar_pkg.yaml` und alle 15 Dateien unter `assets/`.
- Die Lovelace-Ressource zeigt auf `/hacsfiles/gewitterradar-dashboard/gewitterradar.js`.
- Die `lightning_detection_*`-Helfer sind verfügbar, sofern das YAML-Package verwendet wird.
- Karte, Radien, Kompass, Recent-/Verlaufsbereich und KM/MI funktionieren weiterhin.
- Beim ersten Start erscheint **Über Gewitterradar**; anschließend lässt sich der Dialog über **Einstellungen → Über Gewitterradar** erneut öffnen.
- Fokus/Escape, Scrollen und die Kopierfunktion im Recorder-Hinweis verhalten sich korrekt.
