# Gewitterradar — Dashboard

**Gewitterradar** is a Home Assistant dashboard card for live lightning and thunderstorm visualization using data supplied by the Home Assistant Blitzortung.org integration.

Stable channel: **Latest** — currently **V4.05**

## Repository role

For users and development there is one product: **Gewitterradar**. The native Home Assistant Integration and the Dashboard/Card are two delivery forms of the same project.

Current public delivery repositories:

- **Canonical product / native Home Assistant Integration:** `TheDaimos/gewitterradar`
- **Derived Dashboard/Card delivery:** this repository, `TheDaimos/gewitterradar-dashboard`

The V4.04 Dashboard release remains frozen as the verified regression baseline. V4.05 is a new release and does not modify the V4.04 tag or frozen backup branch.

## Highlights

- Live lightning visualization
- Observation, storm and danger zones
- Stable cluster and individual-strike navigation
- Recent activity, KPI/status panels and 120-minute activity history
- Multiple calibrated compass designs with optional device orientation
- 19 selectable language variants
- Metric and imperial distance display
- Responsive layouts for phones, tablets, iPad and desktop
- Premium first-start **Über Gewitterradar** onboarding, re-openable from Settings
- Dynamic radius explanation, Blitzortung.org acknowledgement and Recorder guidance

## Requirements

- Home Assistant
- Blitzortung.org integration with the required lightning/counter entities

## Installation

See:

- [Installation – Deutsch](docs/INSTALLATION_DE.md)
- [Installation – English](docs/INSTALLATION_EN.md)
- [Repository rename / HACS migration](docs/REPOSITORY_RENAME.md)
- [Home Assistant Recorder recommendation](docs/RECORDER.md)

Gewitterradar can be installed as a custom **Dashboard** repository in HACS:

```text
https://github.com/TheDaimos/gewitterradar-dashboard
```

Do not add `TheDaimos/gewitterradar` as a Dashboard repository; that repository contains the canonical Gewitterradar product and native Home Assistant Integration.

For a normal installation, use the default **newest / Latest** version offered by HACS. Do not deliberately select a fixed older version unless you need a rollback or a specific compatibility state. HACS checks the repository for newer releases and can offer future Gewitterradar updates automatically.

With the current repository name, HACS installs the dashboard under `/config/www/community/gewitterradar-dashboard/` and exposes it through `/hacsfiles/gewitterradar-dashboard/`. The module resource is:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

V4.05 installs `gewitterradar.js`, the complete required `assets/` directory and a staged copy of `app_gewitterradar_pkg.yaml` below `/config/www/community/gewitterradar-dashboard/`.

## Nach dem HACS-Download: Gewitterradar-View anlegen

**Wichtig:** Der HACS-Download installiert die Karte und ihre Assets, legt aber keine Home-Assistant-Dashboard-View für dich an. Nach der Installation muss Gewitterradar einmal in einem Dashboard eingebunden werden.

Prüfe zuerst unter **Einstellungen → Dashboards → Ressourcen**, dass diese Modulressource vorhanden ist:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

Lege danach eine neue View an bzw. bearbeite dein gewünschtes Dashboard im YAML-Modus. Ein vollständiges Beispiel ist:

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

Der eigentliche Kartentyp ist:

```yaml
type: custom:gewitterradar-card
```

Die drei Beispiel-Entity-IDs oben entsprechen der bisherigen Package-/Legacy-Konfiguration. Bei einer Installation mit der nativen Gewitterradar-Integration werden die gemeinsame Frontend-/Konfigurationsanbindung und eine vereinfachte Neunutzer-Einrichtung im Rahmen der laufenden Produktkonvergenz vereinheitlicht. Bis diese gemeinsame Auslieferung veröffentlicht ist, gilt die vollständige Installationsanleitung unter [`docs/INSTALLATION_DE.md`](docs/INSTALLATION_DE.md).

The package still requires one manual step when the YAML helper package is used: copy

```text
/config/www/community/gewitterradar-dashboard/app_gewitterradar_pkg.yaml
```

to

```text
/config/packages/app_gewitterradar_pkg.yaml
```

and restart Home Assistant. HACS Dashboard repositories cannot deploy configuration files directly into `/config/packages/`.

Installations created before the repository rename may still contain the old `/hacsfiles/gewitterradar/` resource or `/config/www/community/gewitterradar/` directory. **Do not Update or Redownload the stale old HACS Dashboard entry `TheDaimos/gewitterradar`**, because that repository name now belongs to the canonical Gewitterradar product/native Integration. Add and verify `TheDaimos/gewitterradar-dashboard` first, then clean up the stale old Dashboard entry/resource. Follow [the rename/migration note](docs/REPOSITORY_RENAME.md) for the safe order.

The canonical package source remains `home-assistant/app_gewitterradar_pkg.yaml`; `dist/app_gewitterradar_pkg.yaml` is a byte-identical convenience copy delivered by HACS together with the card.

## Release

V4.04 remains frozen at commit `8ada0e06aef47627d31224b9e46d58de459fb24b`. The `v4.04` tag and `frozen/v4.04` backup branch are checked by CI against that exact commit.

V4.05 promotes the accepted About/Onboarding and visual refinement work to the stable channel. It retains the proven HACS distribution rule: the GitHub release publishes **zero custom release assets**, forcing HACS to install the complete tagged `dist/` tree rather than an incomplete standalone release asset.

Stable Dashboard releases are published as GitHub **Latest** releases. See [Release policy](docs/RELEASE_POLICY.md).

See [V4.05 release notes](RELEASE_NOTES_V4_05.md), [CHANGELOG.md](CHANGELOG.md), and the [V4.04 HACS package-staging note](docs/HACS_V4_04_PACKAGE_STAGING.md) for the unchanged package-delivery model.

## Data source

The live lightning data displayed by Gewitterradar is supplied through the Home Assistant Blitzortung.org integration. The number of simultaneously available lightning events depends on the integration configuration, including detection radius, time window and maximum number of lightning events.

## License

No software license has been selected for this repository yet. Until a license is added, the source remains subject to the default copyright rules applicable to the repository owner.
