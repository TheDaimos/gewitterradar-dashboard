# Repository rename and HACS migration

On 2026-09-06 the public Gewitterradar repositories were separated by role:

```text
TheDaimos/gewitterradar
→ native Home Assistant Integration

TheDaimos/gewitterradar-dashboard
→ Lovelace Dashboard/Card
```

The Dashboard repository was previously named `TheDaimos/gewitterradar`. Its repository identity and V4.04 release history were preserved by the GitHub rename, but the old repository name was subsequently reused for the native Integration. Do not use the old Dashboard repository URL for new Dashboard installations.

## Current HACS Dashboard repository

Add this repository to HACS as a custom repository of type **Dashboard**:

```text
https://github.com/TheDaimos/gewitterradar-dashboard
```

The native Integration is installed separately from:

```text
https://github.com/TheDaimos/gewitterradar
```

## Why the local HACS path changes

Current HACS derives a Dashboard repository's local directory and resource namespace from the repository's current full name. After the rename, the Dashboard therefore uses:

```text
/config/www/community/gewitterradar-dashboard/
/hacsfiles/gewitterradar-dashboard/
```

The current module resource is:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

The previous Dashboard path was:

```text
/config/www/community/gewitterradar/
/hacsfiles/gewitterradar/gewitterradar.js
```

That old `/hacsfiles/gewitterradar/` namespace must no longer be treated as the canonical Dashboard path because `TheDaimos/gewitterradar` is now the native Integration repository.

## Existing HACS installations

For a Dashboard installation created before the rename:

1. Refresh HACS metadata.
2. Confirm that the Dashboard repository resolves to `TheDaimos/gewitterradar-dashboard`.
3. Use **Redownload** for the installed Gewitterradar Dashboard once.
4. Confirm that `/config/www/community/gewitterradar-dashboard/` contains `gewitterradar.js`, `app_gewitterradar_pkg.yaml` and `assets/`.
5. In Home Assistant resource-storage mode, check **Settings → Dashboards → Resources** and confirm that the active resource uses `/hacsfiles/gewitterradar-dashboard/gewitterradar.js`.
6. If the old `/hacsfiles/gewitterradar/gewitterradar.js` resource is still present, remove that old resource only after the new resource has been confirmed working.
7. If Lovelace resources are managed in YAML, update the resource URL manually to `/hacsfiles/gewitterradar-dashboard/gewitterradar.js`.

A stale old local directory may remain after the repository rename. Do not use its presence as proof that the current Dashboard resource is correct; verify the active resource URL and the new HACS directory first.

## V4.04 remains frozen

This repository rename does not modify the frozen V4.04 application baseline, its JavaScript, helper package, PNG assets, tag, release target or `frozen/v4.04` backup branch. The rename changes repository addressing and current HACS local paths only.

The V4.04 release remains anchored to:

```text
Tag:    v4.04
Commit: 8ada0e06aef47627d31224b9e46d58de459fb24b
Backup: frozen/v4.04
```
