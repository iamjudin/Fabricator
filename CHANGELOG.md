# Changelog

## [0.2.11] - 2026-07-17

- Craft now has an explicit intent-based recovery path for serialized
  Fabricator skill links that point at removed versioned installed-cache paths.
- Watch setup now requires target-specific automation names and checks for
  existing matching automations before creating a new recurring monitor.
- Closed the remaining Fabricator backlog items for stale skill-link recovery
  and ambiguous Watch automation names.

## [0.2.10] - 2026-07-17

- Added a downstream-impact gate for Fabricator releases that change shared
  Craft, Publish, Watch, runtime, or public-page standards.
- Publish now requires known Fabricator-made or Fabricator-maintained child
  plugin projects to receive the smallest durable propagation item when a shared
  standard changes.
- Watch now treats stale `inProgress` automation runs as monitoring evidence
  and asks scheduled monitor threads to archive themselves after completion
  when the platform supports it.
- Updated public release validation to require the downstream-impact checklist
  gate.

## [0.2.9] - 2026-07-15

- Added Craft recovery for stale UI skill-chip links that point to removed
  versioned installed-cache `SKILL.md` paths after Fabricator upgrades.
- Craft now resolves the current installed plugin cache before treating a
  missing linked skill path as unavailable.

## [0.2.8] - 2026-07-15

- Removed the public README Development block so the main GitHub page stays
  focused on users rather than internal validation commands.
- Updated Publish gates so contributor validation belongs in contributing docs,
  CI, or release checklists instead of being required on the main README page.

## [0.2.7] - 2026-07-15

- Updated README-visible public positioning so the GitHub page reflects the new
  Watch monitoring workflow.

## [0.2.6] - 2026-07-15

- Added Fabricator: Watch for post-public plugin monitoring and backlog intake.
- Made Publish ask after release whether passive monitoring should be enabled,
  how often it should run, and where usage and production-process findings
  should be routed.
- Added a Watch contract for child plugins so released plugins can monitor
  their own usage without depending on a Fabricator project.

## [0.2.5] - 2026-07-15

- Added a Publish diagnostic for raw branch URL propagation lag: compare remote
  SHA, GitHub API contents, and exact-commit raw URLs before reporting release
  evidence.

## [0.2.4] - 2026-07-15

- Updated README-visible public release behavior so the public GitHub page
  reflects the new raw public artifact, clean install, and local-diagnostic
  smoke gates added in 0.2.3.

## [0.2.3] - 2026-07-15

- Strengthened Publish gates from Tarsy field evidence: public releases now
  require raw public README/package checks, clean install smoke when public
  commands change, and stale visible-asset checks.
- Clarified that local marketplace smoke is diagnostic only and cannot be the
  final public release gate.

## [0.2.2] - 2026-07-15

- Shortened the manifest default prompt so Codex runtime accepts it instead of
  ignoring it during fresh-context startup.
- Added public validation for manifest default prompt length and icon paths so
  runtime loader warnings fail before release.

## [0.2.1] - 2026-07-15

- Made public GitHub page refresh a required Publish definition-of-done gate.
- Required Publish to verify README-visible content, changelog, release notes,
  GitHub About/topics, and install/update instructions for every public update.

## [0.2.0] - 2026-07-15

- Added Fabricator: Publish for public Codex plugin release preparation.
- Added public package metadata, icon paths, README, changelog, contribution
  files, CI, and release validation scripts.
- Clarified routing between local/pre-public Craft work and public Publish work.
- Kept English names in files and public metadata while allowing Russian names
  only in chat.

## [0.1.5] - 2026-07-09

- Strengthened Craft's pre-public runtime completion rules.
- Added blocked tool-route handling based on Landlord/Figma production testing.
