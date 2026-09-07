# Release policy

## Frozen V4.04 baseline

Gewitterradar V4.04 is the first release that combines the verified HACS `dist/` installation path with the staged Home Assistant package. It remains the frozen regression baseline.

The approved V4.04 release anchor is:

```text
Tag:    v4.04
Commit: 8ada0e06aef47627d31224b9e46d58de459fb24b
Backup: frozen/v4.04
```

The tag, its release target and the frozen backup branch must continue to resolve to this exact commit. CI checks all three anchors. Existing stable releases must not be retagged, rebuilt in place or silently replaced. Functional or packaging changes start a new version.

## V4.05 stable release

V4.05 is the current stable Dashboard release. It promotes the accepted About/Onboarding and visual refinement work while preserving the V4.04 HACS/package distribution model.

The release workflow creates a new `v4.05` tag and `frozen/v4.05` backup branch at the exact validated release commit and publishes V4.05 as GitHub **Latest**. V4.05 also publishes zero custom GitHub release assets, so HACS installs the complete tagged `dist/` tree containing `gewitterradar.js`, `assets/` and `app_gewitterradar_pkg.yaml`.

## Latest release policy

Normal HACS installations should use the newest/default version offered by HACS rather than deliberately selecting a fixed historical version. In documentation this channel is called **Latest**.

Every stable Gewitterradar release must:

- use a new version tag instead of changing an existing stable tag;
- be published as the GitHub **Latest** release;
- preserve the zero-custom-release-asset HACS distribution model unless a future HACS implementation is deliberately revalidated;
- pass the complete distribution, package, asset and HACS validation before publication;
- update release notes and the changelog;
- retain a frozen backup branch for the published release commit.

HACS checks repository metadata for newer versions and offers updates when a newer stable release is published. Users who use the default newest version therefore remain on the normal update path. Selecting an older version should be reserved for an intentional rollback or compatibility requirement.

## GitHub immutable releases

GitHub supports repository-level immutable releases. When enabled, future published release tags and release assets cannot be changed after publication. Existing releases are not retroactively converted.

For V4.04, the fixed commit SHA, `v4.04` tag, `frozen/v4.04` backup branch and CI anchor checks provide the regression guard. V4.05 follows the same fixed-anchor principle with its own version tag and frozen backup branch. Existing stable tags must never be moved to a newer commit.
