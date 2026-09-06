# Gewitterradar — Dashboard

**Gewitterradar** is a Home Assistant dashboard card for live lightning and thunderstorm visualization using data supplied by the Home Assistant Blitzortung.org integration.

Stable channel: **Latest** — currently **V4.04**

## Repository split

Gewitterradar is now distributed through two clearly separated public repositories:

- **Native Home Assistant Integration:** `TheDaimos/gewitterradar`
- **Dashboard/Card:** this repository, `TheDaimos/gewitterradar-dashboard`

The V4.04 Dashboard release remains frozen and functionally unchanged. The repository rename only separates the frontend/dashboard distribution from the native integration.

## Highlights

- Live lightning visualization
- Observation, storm and danger zones
- Stable cluster and individual-strike navigation
- Recent activity, KPI/status panels and 120-minute activity history
- Three compass designs with optional device orientation
- 19 selectable language variants
- Metric and imperial distance display
- Responsive layouts for phones, tablets, iPad and desktop

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

Do not add `TheDaimos/gewitterradar` as a Dashboard repository; that repository now contains the native Home Assistant Integration.

For a normal installation, use the default **newest / Latest** version offered by HACS. Do not deliberately select a fixed older version unless you need a rollback or a specific compatibility state. HACS checks the repository for newer releases and can then offer future Gewitterradar updates automatically.

With the current repository name, HACS installs the dashboard under `/config/www/community/gewitterradar-dashboard/` and exposes it through `/hacsfiles/gewitterradar-dashboard/`. The current module resource is therefore:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

HACS installs `gewitterradar.js`, the four required visual assets and a staged copy of `app_gewitterradar_pkg.yaml` below `/config/www/community/gewitterradar-dashboard/`.

The package still requires one manual step: copy or move

```text
/config/www/community/gewitterradar-dashboard/app_gewitterradar_pkg.yaml
```

to

```text
/config/packages/app_gewitterradar_pkg.yaml
```

and restart Home Assistant. This cannot be automated by the HACS Dashboard installation because HACS installs this repository only inside its own `/config/www/community/gewitterradar-dashboard/` directory and does not deploy configuration files into `/config/packages/`.

Installations created before the repository rename may still contain the old `/hacsfiles/gewitterradar/` resource or `/config/www/community/gewitterradar/` directory. **Do not Update or Redownload the stale old HACS Dashboard entry `TheDaimos/gewitterradar`**, because that repository name now belongs to the native Integration. Add and verify `TheDaimos/gewitterradar-dashboard` first, then clean up the stale old Dashboard entry/resource. Follow [the rename/migration note](docs/REPOSITORY_RENAME.md) for the safe order.

The canonical package source remains `home-assistant/app_gewitterradar_pkg.yaml`; V4.04 places a byte-identical convenience copy at `dist/app_gewitterradar_pkg.yaml` so HACS delivers it together with the card.

The JavaScript card is registered as:

```yaml
type: custom:gewitterradar-card
```

## Release

V4.04 is frozen as the current verified regression baseline at commit `8ada0e06aef47627d31224b9e46d58de459fb24b`. The `v4.04` tag and the backup branch `frozen/v4.04` are checked by CI against that exact commit. Future changes must use a new version instead of modifying V4.04 in place.

V4.04 keeps the working V4.03 HACS distribution model: the GitHub release publishes **zero custom release assets**, forcing current HACS to use the tagged `dist/` tree. V4.04 adds `dist/app_gewitterradar_pkg.yaml` to that tree, so users no longer need to download the helper package separately before installing it manually under `/config/packages/`.

Future stable Dashboard releases are explicitly published as GitHub **Latest** releases. At present GitHub `releases/latest` resolves to V4.04. See [Release policy](docs/RELEASE_POLICY.md).

Application behavior, helper IDs/defaults, layouts, lightning processing, compass behavior and the optimized PNG files remain unchanged.

See [V4.04 release notes](RELEASE_NOTES_V4_04.md), the [V4.04 HACS package-staging note](docs/HACS_V4_04_PACKAGE_STAGING.md), the [V4.01 asset verification report](docs/ASSET_OPTIMIZATION_V4_01.md) and [CHANGELOG.md](CHANGELOG.md).

## Data source

The live lightning data displayed by Gewitterradar is supplied through the Home Assistant Blitzortung.org integration. The number of simultaneously available lightning events depends on the integration configuration, including detection radius, time window and maximum number of lightning events.

## License

No software license has been selected for this repository yet. Until a license is added, the source remains subject to the default copyright rules applicable to the repository owner.
