# Changelog

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
