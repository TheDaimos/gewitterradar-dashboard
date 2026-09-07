# Gewitterradar V4.05 – Installation (EN)

## Requirements

- Running Home Assistant installation.
- Blitzortung.org integration providing the required lightning/counter entities.
- Default counter used by the example: `sensor.home_lightning_counter`.

## Repository split

Public distribution is separated into:

- **Native Home Assistant Integration:** `TheDaimos/gewitterradar`
- **Dashboard/Card:** `TheDaimos/gewitterradar-dashboard`

V4.04 remains unchanged as the frozen regression baseline. V4.05 is the current stable Dashboard release.

HACS uses:

```text
/config/www/community/gewitterradar-dashboard/
/hacsfiles/gewitterradar-dashboard/
```

**Important for installations created before the repository rename:** Do not update or redownload the old HACS Dashboard entry `TheDaimos/gewitterradar`. That repository name now belongs to the native Home Assistant Integration. Instead, add `TheDaimos/gewitterradar-dashboard` as a custom **Dashboard** repository, install the current version there and first verify `/hacsfiles/gewitterradar-dashboard/gewitterradar.js`. Only then remove the stale old Dashboard entry/resource. See [`REPOSITORY_RENAME.md`](REPOSITORY_RENAME.md).

## HACS update channel

For normal installations and updates, use the default **Latest / newest version** offered by HACS. This is currently **V4.05**. Select an older fixed version only for an intentional rollback.

## Option A: Install or update through HACS

1. Add `TheDaimos/gewitterradar-dashboard` to HACS as a custom **Dashboard** repository if it is not already present.
2. Install the default **Latest / newest version**, or apply the offered update to V4.05.
3. HACS installs `gewitterradar.js`, the complete `assets/` directory and `app_gewitterradar_pkg.yaml` under `/config/www/community/gewitterradar-dashboard/`.
4. If the YAML helper package is used, copy `app_gewitterradar_pkg.yaml` to `/config/packages/app_gewitterradar_pkg.yaml`. Copying is recommended so the HACS staging copy remains available.
5. Perform a full Home Assistant restart after a package change.
6. Refresh the browser/Companion App cache if needed.

The HACS installation contains at least:

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

V4.05 uses **15 local visual assets** in total.

The Lovelace module URL is:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

### Why is the package still a manual step?

Gewitterradar is installed as a HACS **Dashboard repository**. HACS installs files under `/config/www/community/gewitterradar-dashboard/` but cannot deploy Home Assistant configuration directly into `/config/packages/`.

The maintained source is `home-assistant/app_gewitterradar_pkg.yaml`; `dist/app_gewitterradar_pkg.yaml` is the byte-identical HACS staging copy. CI verifies that both files match.

When packages are used, `configuration.yaml` must include:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

If that block already exists, do not add a second top-level `homeassistant:` key.

Existing `lightning_detection_*` helper IDs are intentionally preserved. The package distribution model is unchanged from V4.04.

## Option B: Manual installation

### 1. Copy JavaScript and assets

- Copy `gewitterradar-card-v4_05.js` to `/config/www/gewitterradar/gewitterradar-card-v4_05.js`.
- Copy the complete contents of `dist/assets/` to `/config/www/gewitterradar/assets/`.

### 2. Add the Lovelace resource

Register the card as a JavaScript module:

```text
/local/gewitterradar/gewitterradar-card-v4_05.js?v=4_05
```

### 3. Install the Home Assistant package

If the YAML helper package is used, copy `home-assistant/app_gewitterradar_pkg.yaml` to `/config/packages/app_gewitterradar_pkg.yaml`. The identical `dist/app_gewitterradar_pkg.yaml` can be used as an alternative. Then perform a full Home Assistant restart.

## Example Gewitterradar view

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

## Recorder protection recommended

Add this configuration to `configuration.yaml`:

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

If a `recorder:` block already exists, merge these entries into it instead of creating a second top-level key. The exclusion prevents long-term Recorder/History storage without disabling the live states used by Gewitterradar.

## First smoke test after V4.05

- HACS/the card reports `V4.05`.
- `/config/www/community/gewitterradar-dashboard/` contains `gewitterradar.js`, `app_gewitterradar_pkg.yaml` and all 15 files under `assets/`.
- The Lovelace resource points to `/hacsfiles/gewitterradar-dashboard/gewitterradar.js`.
- `lightning_detection_*` helpers are available when the YAML package is used.
- Card, radii, compass, Recent/history and KM/MI continue to work.
- On first start, **Über Gewitterradar** opens; afterwards it can be reopened through **Settings → Über Gewitterradar**.
- Focus/Escape, scrolling and the Recorder copy action behave correctly.
