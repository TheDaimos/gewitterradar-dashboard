# Global Project Defaults

This repository participates in the shared TheDaimos project-bootstrap model.

Canonical global defaults:

`TheDaimos/project-defaults`

Before substantial project work in a fresh ChatGPT/Codex session, load the current global defaults first, then this repository's own current guidance/state, then the shared dev-toolkit where applicable.

Preferred bootstrap mnemonics, fully equivalent:

> **Deimos**  
> **Daimos**

Equivalent standalone startup aliases include `start`, `starts`, `start repo`, `start project`, `load defaults`, and `check repo` as defined by the canonical defaults repository.

All bootstrap aliases are fail-closed: the current `TheDaimos/project-defaults/START_HERE.md` must actually be retrieved and followed before readiness is declared. Do not answer a standalone `Deimos`/`Daimos` from remembered context first.

## Binding Gewitterradar delivery rule

This repository is **not an independent Gewitterradar development source**.

`TheDaimos/gewitterradar` is the canonical Gewitterradar product repository and single source of truth for ongoing product development. The native Home Assistant integration and this Lovelace/dashboard package are only two delivery forms of the same product.

Unless the user explicitly limits a task to one delivery form, every Gewitterradar feature, UI, visual, behavior, setting, asset, regression fix or product-level change must apply to **both** delivery forms and must originate from the shared source state in `TheDaimos/gewitterradar`.

Future dashboard artifacts in this repository must therefore be generated or synchronized from `TheDaimos/gewitterradar`. Do not implement ordinary product changes only here. An explicitly requested emergency release-only change must be reconciled back into the canonical repository before the next normal release.

Existing frozen tags and shipped releases, including V4.05 and V4.06, remain immutable reference points and are not altered by this rule.

## Derived-repository branch lifecycle

Because this repository is a derived delivery target, its normal long-lived state should remain deliberately small:

- `main` contains the current derived Dashboard/HACS delivery state;
- published release tags `vX.XX` remain immutable;
- an explicit `frozen/vX.XX` may remain as the named rollback/release anchor;
- ordinary product feature development does not receive independent long-lived branches here.

Temporary audit, migration, release-preparation or delivery branches may be deleted after an explicit cleanup review once their relevant state is verified as fully integrated into `main` or preserved by the corresponding release/freeze anchor. A branch with unique divergent commits is retained until its contents have been consciously reviewed or archived; branch deletion is never performed merely for cosmetic tidiness.

Reusable development tooling belongs in `TheDaimos/home-assistant-dev-toolkit`; this production repository must not depend on either private shared repository at runtime.