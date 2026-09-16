# Gewitterradar — Dashboard

**Gewitterradar** is a Home Assistant dashboard card for live lightning and thunderstorm visualization using data supplied by the Home Assistant Blitzortung.org integration.

Stable public release: **V4.06**  
Current prepared Dashboard candidate: **V4.07.56**

## Repository role

For users and development there is one product: **Gewitterradar**. The native Home Assistant Integration and the Dashboard/Card are two delivery forms of the same project.

- Canonical product repository: `TheDaimos/gewitterradar`
- Derived Dashboard/HACS delivery: `TheDaimos/gewitterradar-dashboard`

Ordinary product development takes place only in the canonical repository. This repository is synchronized from the accepted canonical state.

The V4.07.56 Dashboard candidate is derived from canonical commit:

`3c7817162f9619837f3be8d2048a79cdb04ca8bb`

Accepted payload identities:

- `dist/gewitterradar.js` — SHA256 `249485f4bcf68c9b23b821cae9b507030ae09cff5a56f7e28d3d7f3b02eb4a1a`
- `dist/locales/about-locales.js` — SHA256 `997c4fe9b357935888fdb7bedc43cdd17f105b97241a000324891cea575dd436`
- `dist/app_gewitterradar_v4_07_pkg.yaml` — SHA256 `1b705c5686e6a7be6dfb36717903df551d4f9f93787c39bd12bddf00aefae694`

## Highlights

- Live lightning visualization
- Observation, storm and danger zones
- Cluster and individual-strike modes
- Recent activity, KPI/status panels and 120-minute activity history
- Multiple calibrated compass designs and trend medallion
- Worldwide place/postcode search plus direct coordinates
- 15 languages plus 4 German dialect variants = 19 variants
- Full Help & Notes and Recorder guidance
- Responsive layouts for phones, tablets, iPad and desktop
- Protected V4.07.56 diagnostics including virtual storm cells, EXTREM and medallion states

## Requirements

- Home Assistant
- Blitzortung.org integration with the required lightning/counter entities

## Installation

Gewitterradar can be added as a custom **Dashboard** repository in HACS:

```text
https://github.com/TheDaimos/gewitterradar-dashboard
```

The module resource is:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

The HACS Dashboard download installs the card and its assets, but it does not create a Dashboard View automatically.

A minimal example is:

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

The actual card type is:

```yaml
type: custom:gewitterradar-card
```

When the YAML helper package is used, copy:

```text
/config/www/community/gewitterradar-dashboard/app_gewitterradar_v4_07_pkg.yaml
```

to:

```text
/config/packages/app_gewitterradar_v4_07_pkg.yaml
```

and restart Home Assistant. HACS Dashboard repositories cannot deploy configuration files directly into `/config/packages/`.

The historical V4.06 package remains in the repository for rollback/migration purposes. New V4.07 installations use `app_gewitterradar_v4_07_pkg.yaml`.

Detailed instructions:

- [Installation – Deutsch](docs/INSTALLATION_DE.md)
- [Installation – English](docs/INSTALLATION_EN.md)
- [Repository rename / HACS migration](docs/REPOSITORY_RENAME.md)
- [Recorder recommendation](docs/RECORDER.md)

## Release model

Published tags and frozen release branches remain immutable. V4.05 and V4.06 are not rewritten by the V4.07.56 preparation.

V4.07.56 is prepared from the exact accepted canonical Gewitterradar state and is validated independently in this derived repository before public release.

The GitHub/HACS release continues to publish **no custom release assets**, so HACS installs the complete tagged `dist/` tree rather than an incomplete standalone asset.

See [V4.07.56 release notes](RELEASE_NOTES_V4_07_56.md) and [CHANGELOG.md](CHANGELOG.md).

## Data source

Live lightning data is supplied through the Home Assistant Blitzortung.org integration. The number of simultaneously available lightning events depends on that integration's configuration, including detection radius, time window and maximum event count.

## License

No software license has been selected for this derived repository yet. Until a license is added, the source remains subject to the default copyright rules applicable to the repository owner.
