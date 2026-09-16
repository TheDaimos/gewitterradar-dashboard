# Gewitterradar V4.07.56 – Installation (EN)

## Requirements

- Running Home Assistant installation.
- Blitzortung.org integration providing the required lightning/counter entities.
- For normal HACS use: repository `TheDaimos/gewitterradar-dashboard` added as a **Dashboard** repository.

## HACS paths

```text
/config/www/community/gewitterradar-dashboard/
/hacsfiles/gewitterradar-dashboard/
```

The module resource is:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

## Install through HACS

1. Add `TheDaimos/gewitterradar-dashboard` as a custom Dashboard repository.
2. Install or update Gewitterradar.
3. Under **Settings → Dashboards → Resources**, verify that `/hacsfiles/gewitterradar-dashboard/gewitterradar.js` is loaded as a JavaScript module.
4. Create a Dashboard View using `type: custom:gewitterradar-card`.
5. When the YAML package is used, copy `app_gewitterradar_v4_07_pkg.yaml` from the HACS directory to `/config/packages/app_gewitterradar_v4_07_pkg.yaml`.
6. Perform a full Home Assistant restart after a package change.

HACS Dashboard repositories cannot deploy configuration files directly into `/config/packages/`, therefore that copy step remains manual.

The historical `app_gewitterradar_v4_06_pkg.yaml` remains available for rollback/migration. V4.07 uses `app_gewitterradar_v4_07_pkg.yaml`.

## Example Dashboard View

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

The card type is:

```yaml
type: custom:gewitterradar-card
```

## Enable packages

If packages are not already enabled:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

If a top-level `homeassistant:` block already exists, merge the setting instead of adding a second key.

## Recorder protection recommended

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

Merge these entries into an existing `recorder:` configuration instead of creating a duplicate block.

## Verification after installation

- The card reports V4.07.56.
- `gewitterradar.js` is loaded from `/hacsfiles/gewitterradar-dashboard/`.
- `locales/about-locales.js` and the complete `assets/` directory are present.
- When the YAML package is used, `app_gewitterradar_v4_07_pkg.yaml` exists under `/config/packages/`.
- Map, radii, compass, medallion, history, worldwide location search and Help work as expected.
- All 19 language variants and the protected diagnostic tools remain available.

## Repository rename

For old installations, do not redownload the stale Dashboard entry `TheDaimos/gewitterradar`. First install and verify `TheDaimos/gewitterradar-dashboard`. Details: [`REPOSITORY_RENAME.md`](REPOSITORY_RENAME.md).
