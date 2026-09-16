# Gewitterradar V4.07.56 – Installation (DE)

## Voraussetzungen

- Laufende Home-Assistant-Installation.
- Blitzortung.org-Integration mit den benötigten Blitz-/Zählerentitäten.
- Für normale HACS-Nutzung: Repository `TheDaimos/gewitterradar-dashboard` als Typ **Dashboard**.

## HACS-Pfade

```text
/config/www/community/gewitterradar-dashboard/
/hacsfiles/gewitterradar-dashboard/
```

Die Modulressource lautet:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

## Installation über HACS

1. `TheDaimos/gewitterradar-dashboard` als benutzerdefiniertes Dashboard-Repository hinzufügen.
2. Gewitterradar installieren bzw. aktualisieren.
3. Unter **Einstellungen → Dashboards → Ressourcen** prüfen, dass `/hacsfiles/gewitterradar-dashboard/gewitterradar.js` als JavaScript-Modul geladen wird.
4. Eine Dashboard-View mit `type: custom:gewitterradar-card` anlegen.
5. Falls das YAML-Package genutzt wird, `app_gewitterradar_v4_07_pkg.yaml` aus dem HACS-Ordner nach `/config/packages/app_gewitterradar_v4_07_pkg.yaml` kopieren.
6. Nach einer Package-Änderung Home Assistant vollständig neu starten.

HACS kann Konfigurationsdateien nicht direkt nach `/config/packages/` installieren. Deshalb bleibt dieser Kopierschritt beim Dashboard-Package bewusst manuell.

Das historische `app_gewitterradar_v4_06_pkg.yaml` bleibt als Rückfall-/Migrationsdatei erhalten. Für V4.07 wird `app_gewitterradar_v4_07_pkg.yaml` verwendet.

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

Der Kartentyp ist:

```yaml
type: custom:gewitterradar-card
```

## Packages aktivieren

Falls Packages noch nicht eingebunden sind:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Wenn bereits ein `homeassistant:`-Block existiert, keinen zweiten Hauptschlüssel anlegen.

## Recorder-Schutz empfohlen

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

Bestehende `recorder:`-Konfiguration ergänzen, nicht doppelt anlegen.

## Prüfung nach Installation

- Karte zeigt V4.07.56.
- `gewitterradar.js` ist über `/hacsfiles/gewitterradar-dashboard/` geladen.
- `locales/about-locales.js` und der vollständige `assets/`-Ordner sind vorhanden.
- Bei Package-Nutzung liegt `app_gewitterradar_v4_07_pkg.yaml` unter `/config/packages/`.
- Karte, Radien, Kompass, Medaillon, Verlauf, Ortssuche und Hilfe funktionieren.
- Die 19 Sprachvarianten sowie die Diagnosewerkzeuge bleiben verfügbar.

## Repository-Umbenennung

Bei alten Installationen den veralteten HACS-Dashboard-Eintrag `TheDaimos/gewitterradar` nicht erneut laden. Zuerst `TheDaimos/gewitterradar-dashboard` sauber installieren und prüfen. Details: [`REPOSITORY_RENAME.md`](REPOSITORY_RENAME.md).
