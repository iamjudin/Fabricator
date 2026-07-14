# Field Notes: Tarsy Publication

Status: preparation material for Fabricator Publish; not a specification yet.
Captured 2026-07-14 from the local Tarsy plugin repository, installed plugin
state, pet package state, and the latest Tarsy pet-upgrade thread.

## Current Observations

- Canonical-looking plugin project: `/Users/iamjudin/Desktop/Plugins/Tarsy`.
  It is a Git repository with commits through
  `a4bac7e Simplify Tarsy to a single sarcasm style`.
- Installed local plugin entry is `tarsy@local-plugins`
  `0.1.0+codex.20260714195449`, but it points at
  `/Users/iamjudin/Desktop/Plugins/plugins/tarsy`, not the fuller
  `/Users/iamjudin/Desktop/Plugins/Tarsy` project.
- The two plugin bundles currently match byte-for-byte for `plugin.json` and
  `skills/tarsy/SKILL.md`, but the source-path mismatch is still a publication
  risk. Publishing must choose one canonical source and prove runtime tests use
  it.
- Tarsy has two release surfaces: the Codex plugin skill (`$tarsy`) and a
  companion pet package in `${CODEX_HOME:-$HOME/.codex}/pets/tarsy/`.
  Publication work should keep those surfaces separate unless the intended
  release explicitly bundles both.
- Current installed pet package has `spriteVersionNumber: 2` and
  `spritesheet-20260714-221026.webp`.
- The `Documents/Tars` project has uncommitted `assets/` and `docs/` and no
  commits on `main`; treat it as a pet-production scratch/project area, not
  automatically as the plugin release source.

## Comments and Thread Evidence

- Latest Tarsy-related thread:
  `019f5d91-4874-7732-8b05-61b9ad693d5f`, "Upgrade Tarsy pet directions".
- The thread was interrupted while upgrading the existing Tarsy pet to the v2
  look-direction contract. It validated the v1 atlas, produced QA artifacts,
  documented look mechanics, generated cardinal anchors, and then stopped during
  row-9 generation.
- The thread's key product comment: keep the robot body/baseline stable and read
  look direction through the screen face, eyes, brows, and slight head motion,
  not by rotating the whole sprite.
- `docs/tarsy-v2-gap-table.md` records the pre-upgrade gap state:
  row 8 `review` was a placeholder copied from `running`; rows 9 and 10 look
  directions were missing; row 5 `failed` had placeholder tail frames.
- The installed pet is already v2 after the gap table was written, so publish
  readiness requires fresh verification of the current installed atlas, not just
  reading the old gap table.

## Publish-Skill Lessons

- Before publication, identify the canonical release root and compare it with
  the installed runtime source path. Matching versions are not enough when the
  marketplace entry points at a duplicate path.
- Treat companion assets as their own release surface. A plugin can be
  publishable while a pet package still has unresolved visual QA, and the
  reverse can also be true.
- Publication readiness should ask for release evidence per surface:
  repository status, manifest version, validation, installed runtime path,
  runtime smoke, asset package manifest, asset dimensions/contract, and visual
  QA evidence when visuals are part of the release.
- Interrupted generation or QA threads are comments, not completion evidence.
  The publish workflow should read them, extract unresolved items, and require
  a current verification pass before declaring a release ready.
- If a public release will include a pet or other generated visual asset, the
  release checklist must include dimensions/format inspection and a visual
  contact-sheet or screenshot review, not only plugin manifest validation.

## Open Questions

- Is `/Users/iamjudin/Desktop/Plugins/Tarsy` the intended public repository,
  with `/Users/iamjudin/Desktop/Plugins/plugins/tarsy` only a local marketplace
  mirror, or should the marketplace source be moved before publication?
- Is the public Tarsy release meant to include only the sarcasm style plugin, or
  both the plugin and the Tarsy pet?
- Does the current installed v2 pet atlas fully resolve the old row-8/row-9/
  row-10 gaps, or does visual QA still need another pass?
