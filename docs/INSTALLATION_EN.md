# Gewitterradar V4.07.56 – Installation (EN)

This guide covers the **Dashboard/Lovelace delivery** of Gewitterradar from `TheDaimos/gewitterradar-dashboard`.

## Requirements

- a running Home Assistant installation;
- the Blitzortung.org integration as the source of live lightning data;
- HACS for the normal installation path;
- access to `/config/`, because the Gewitterradar package must be copied manually into `/config/packages/`.

## 1. Install Gewitterradar through HACS

1. Add `https://github.com/TheDaimos/gewitterradar-dashboard` to HACS as a custom repository of type **Dashboard**.
2. Install or update **Gewitterradar**.
3. Under **Settings → Dashboards → Resources**, verify that the following resource is loaded as a **JavaScript module**:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

The corresponding files are normally stored under:

```text
/config/www/community/gewitterradar-dashboard/
```

## 2. Activate the V4.07 package manually

HACS Dashboard repositories cannot deploy configuration files directly into `/config/packages/`. This step is therefore intentionally manual.

Copy:

```text
/config/www/community/gewitterradar-dashboard/app_gewitterradar_v4_07_pkg.yaml
```

to:

```text
/config/packages/app_gewitterradar_v4_07_pkg.yaml
```

If Home Assistant packages are not enabled yet, add this to `configuration.yaml`:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

If a top-level `homeassistant:` block already exists, merge the setting into that block. **Do not create a second top-level `homeassistant:` key.**

Then perform a full Home Assistant restart.

### Important when upgrading from V4.06

V4.07 uses only:

```text
app_gewitterradar_v4_07_pkg.yaml
```

The historical `app_gewitterradar_v4_06_pkg.yaml` remains available only for rollback and migration reference.

**Never load the V4.06 and V4.07 packages at the same time.** Both intentionally define the same `lightning_detection_*` helpers.

Canonical V4.07 package checksum:

```text
SHA256: 1b705c5686e6a7be6dfb36717903df551d4f9f93787c39bd12bddf00aefae694
```

## 3. Create the Gewitterradar Dashboard View

The HACS download installs the card and its assets, but it does **not** create a Dashboard View automatically.

### Through the Home Assistant UI

1. Open the desired Dashboard.
2. Choose **Edit dashboard**.
3. Create a new View named **Gewitterradar**.
4. Use the **Panel / one card** View type.
5. Optionally set the icon to `mdi:weather-lightning`.
6. Add a **Manual card**.
7. Enter this card configuration:

```yaml
type: custom:gewitterradar-card
```

That is the complete minimal configuration. The V4.07 package provides the required Gewitterradar helpers.

### Complete YAML example

```yaml
views:
  - title: Gewitterradar
    path: gewitterradar
    icon: mdi:weather-lightning
    type: panel
    cards:
      - type: custom:gewitterradar-card
```

If the Blitzortung counter on the system is not named `sensor.home_lightning_counter`, it can be specified explicitly:

```yaml
type: custom:gewitterradar-card
counter_entity: sensor.YOUR_LIGHTNING_COUNTER
```

## 4. Link the worldwide reference location to Blitzortung

The V4.07 package provides its own reference tracker:

```text
device_tracker.gewitterradar_dashboard
```

Select this tracker once in the Blitzortung.org integration as its **Location entity**.

After that, location changes are made in Gewitterradar. The package updates the Gewitterradar tracker, while Blitzortung.org remains responsible for the data region, re-subscription and update latency.

Gewitterradar does not modify foreign Config Entries and does not write directly to Home Assistant `.storage`.

## 5. Recorder protection – strongly recommended

Gewitterradar processes short-lived lightning entities. During high lightning activity, a very large number of state changes can occur. The following Recorder exclusion is therefore recommended:

```yaml
recorder:
  exclude:
    entity_globs:
      - "geo_location.lightning_strike*"
      - "sensor.*_lightning_distance"
      - "sensor.*_lightning_azimuth"
      - "sensor.*_lightning_counter"
```

Merge these entries into an existing `recorder:` configuration and **do not create a second top-level `recorder:` key**.

The live states remain available to Gewitterradar. Existing historical data is not removed automatically.

See also [`RECORDER.md`](RECORDER.md).

## 6. Remove old resources

Only one Gewitterradar JavaScript resource may be active:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

Do not load historical or test resources such as

```text
/hacsfiles/gewitterradar/gewitterradar.js
```

in parallel.

After changing resources, reload the browser completely; use a hard reload if the frontend cache remains stale.

## 7. Verification after installation

Verify the following:

- Gewitterradar reports **V4.07.56**;
- `/hacsfiles/gewitterradar-dashboard/gewitterradar.js` is the only active Gewitterradar resource;
- `assets/` and `locales/about-locales.js` exist in the HACS directory;
- `/config/packages/app_gewitterradar_v4_07_pkg.yaml` is active;
- the V4.06 package is not loaded in parallel;
- the map and radii are displayed;
- live lightning or the available 120-minute history appears;
- compass, medallion and history work;
- worldwide place search and direct coordinate input work;
- `device_tracker.gewitterradar_dashboard` changes coordinates when the reference location changes;
- Blitzortung.org uses that tracker as its Location entity;
- the Help/Notes area including the Recorder guidance is available.

## 8. Repository rename / older installations

For older installations, do not load the stale Dashboard repository entry `TheDaimos/gewitterradar` in parallel. The Dashboard delivery uses `TheDaimos/gewitterradar-dashboard`.

Before switching, verify and replace old JavaScript resources and the active V4.06 package cleanly.

Details: [`REPOSITORY_RENAME.md`](REPOSITORY_RENAME.md)
