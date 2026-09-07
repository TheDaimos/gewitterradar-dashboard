# Gewitterradar V4.05

V4.05 introduces the new premium **Über Gewitterradar** onboarding and information experience while preserving the proven live lightning, radius, Recent/history and Home Assistant package behavior from the V4.04 baseline.

## New: Über Gewitterradar

- New first-start onboarding dialog with a premium dark-night / gold-brass visual design.
- The dialog can be reopened at any time through **Einstellungen → Über Gewitterradar**.
- Dedicated introductory section for weather and lightning enthusiasts.
- Personal **Für Alkje** dedication with the accepted cinematic forest/sunset composition.
- Dynamic presentation of the configured observation, storm and danger radii instead of hard-coded values.
- Clear explanation of the three radius levels with the correct semantic colors: danger red, storm blue, observation gold.
- Thanks to **Blitzortung.org** and the volunteer station operators whose network/data form the basis of the lightning information used by Gewitterradar.
- Integrated Home Assistant Recorder recommendation, including the canonical `configuration.yaml` example and copy control.
- Collapsible overview of the settings/entities and their short purposes.

## Visual and responsive refinements

- New local branding, hero and dedication assets for the About experience.
- Expanded and refined compass/selector graphics plus the accepted trend medallion/arrow assets.
- Premium metallic section symbols and Recorder/database presentation.
- Responsive validation for desktop, iPad/tablet and Android portrait/landscape layouts.
- Focus, Escape, touch/click interaction, onboarding persistence, manual reopen and YAML copy behavior were regression-tested during the V4.05 development cycle.

## Compatibility

- Existing Gewitterradar helper IDs and the staged Home Assistant package remain compatible with the V4.04 installation model.
- The HACS Dashboard repository remains `TheDaimos/gewitterradar-dashboard` and the module resource remains:

  ```text
  /hacsfiles/gewitterradar-dashboard/gewitterradar.js
  ```

- Installations from before the repository rename must continue to follow the documented safe migration order and must not redownload the stale old Dashboard entry `TheDaimos/gewitterradar`.

## HACS distribution

V4.05 deliberately keeps the proven **zero custom GitHub release assets** model. HACS therefore installs the complete tagged `dist/` tree, including:

- `gewitterradar.js`
- the complete V4.05 `assets/` directory
- `app_gewitterradar_pkg.yaml`

The package still has to be copied manually from the HACS Dashboard directory to `/config/packages/app_gewitterradar_pkg.yaml` when the YAML helper package is used.

For normal installations and updates, use the default **Latest** version offered by HACS.
