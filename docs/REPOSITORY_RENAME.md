# Repository rename and HACS migration

On 2026-09-06 the public Gewitterradar repositories were separated by role:

```text
TheDaimos/gewitterradar
→ native Home Assistant Integration

TheDaimos/gewitterradar-dashboard
→ Lovelace Dashboard/Card
```

The Dashboard repository was previously named `TheDaimos/gewitterradar`. Its repository identity and V4.04 release history were preserved by the GitHub rename, but the old repository name was subsequently reused for the native Integration. Do not use the old Dashboard repository URL for new Dashboard installations.

## Important HACS rename collision

This is not a normal repository rename from HACS's point of view.

The old Dashboard repository name `TheDaimos/gewitterradar` now points to a different, valid repository: the native Home Assistant Integration. A stale HACS Dashboard entry that still uses the old repository name can therefore no longer be relied on to discover the Dashboard rename automatically.

**Do not use Update or Redownload on a stale pre-rename Dashboard entry that still identifies itself as `TheDaimos/gewitterradar`.** Doing so can make HACS inspect the new native Integration repository instead of the renamed Dashboard repository.

The safe migration is to install the renamed Dashboard repository under its new name first, verify the new resource, and only then remove the stale old Dashboard entry/resource.

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

## Existing HACS installations created before the rename

Use this order for an existing Dashboard installation that was created while the Dashboard repository was still named `TheDaimos/gewitterradar`:

1. **Do not Update or Redownload the stale old Dashboard entry.**
2. Add `https://github.com/TheDaimos/gewitterradar-dashboard` to HACS as a new custom repository of type **Dashboard**.
3. Install the Dashboard from this new repository. For the current stable line, use the default Latest version, V4.04.
4. Confirm that `/config/www/community/gewitterradar-dashboard/` contains at least `gewitterradar.js`, `app_gewitterradar_pkg.yaml` and `assets/`.
5. In Home Assistant resource-storage mode, check **Settings → Dashboards → Resources** and confirm that the active module resource uses `/hacsfiles/gewitterradar-dashboard/gewitterradar.js`.
6. If Lovelace resources are managed in YAML, update the resource URL manually to `/hacsfiles/gewitterradar-dashboard/gewitterradar.js`.
7. Reload the Dashboard/browser or Companion App and verify that Gewitterradar loads correctly from the new resource path.
8. Only after the new Dashboard installation has been confirmed working, remove the stale old Dashboard repository entry/resource that still refers to `/hacsfiles/gewitterradar/`.
9. A stale local directory `/config/www/community/gewitterradar/` may remain. Remove it only after the new Dashboard path has been verified and only if it is no longer required by any other manually maintained resource.

The already installed Home Assistant package at `/config/packages/app_gewitterradar_pkg.yaml` is not renamed by this repository migration. If it is already the expected V4.04 package, it can remain in place.

If HACS does not allow the renamed Dashboard repository to be added while the stale old custom-repository registration exists, remove only that stale HACS custom-repository registration first. Do not use Redownload on it. Then add `TheDaimos/gewitterradar-dashboard` and continue with the verification steps above.

## V4.04 remains frozen

This repository rename does not modify the frozen V4.04 application baseline, its JavaScript, helper package, PNG assets, tag, release target or `frozen/v4.04` backup branch. The rename changes repository addressing and current HACS local paths only.

The V4.04 release remains anchored to:

```text
Tag:    v4.04
Commit: 8ada0e06aef47627d31224b9e46d58de459fb24b
Backup: frozen/v4.04
```
