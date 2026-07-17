# Release Checklist

Use this before tagging a public Fabricator release.

## Package

- Confirm `.agents/plugins/marketplace.json` has marketplace name `fabricator`.
- Confirm the marketplace entry points to `./plugins/fabricator`.
- Confirm `plugins/fabricator/.codex-plugin/plugin.json` has the release
  version, English public metadata, and icon paths.
- Confirm `plugins/fabricator/assets/icon_fab.png` is present and referenced.
- Confirm `craft` and `publish` skills are both present.

## Repository

- Confirm `README.md` explains what, why, install, use, update, and license
  without a main-page internal development command block.
- Confirm `README.md` visible content matches the release being published.
- Confirm `CHANGELOG.md` includes the release entry before tagging.
- Confirm `LICENSE`, `CHANGELOG.md`, and `CONTRIBUTING.md` are current.
- Confirm issue and PR templates are present.
- Confirm CI runs `scripts/validate.sh`.
- Confirm GitHub About description and topics match the release.
- Confirm GitHub Release notes match the release and do not describe an older
  public behavior.
- Confirm install/update commands on the public page are still correct.
- After push/release, confirm raw public `README.md` and package
  `.codex-plugin/plugin.json` match the released version and instructions.
- If raw branch URLs lag, compare remote SHA, GitHub API contents, and
  exact-commit raw URLs; report propagation evidence rather than skipping the
  public artifact check.
- Confirm public visible asset references are current: icon, logo, banner,
  pet, screenshots, or renamed media when present.

## Downstream Impact

- Classify the release as Fabricator-only or shared-standard.
- If the release changes a shared Craft, Publish, Watch, release, runtime, or
  public-page standard, find known Fabricator-made or Fabricator-maintained
  child plugin projects from local plugin workspaces, `.fabricator` metadata,
  Watch contracts, backlogs, release notes, and recent field evidence.
- For each affected child project, apply the smallest durable propagation:
  source/checklist update, Watch contract update, release note, or backlog
  item.
- If a child project is unavailable or outside the current write scope, record
  the pending propagation item with project, affected rule, owner, and next
  action before release readiness is declared.
- Include downstream propagation evidence in the release result.

## Validation

Run from the repository root:

```bash
scripts/validate.sh
git diff --check
```

## Local Diagnostic Smoke

```bash
codex plugin marketplace add /Users/iamjudin/Desktop/Plugins/Fabricator
codex plugin add fabricator@fabricator
```

This checks local package shape only. Do not treat local marketplace smoke as
final public release evidence.

Start a new Codex chat and confirm:

- `$fabricator:craft` loads Craft from the intended installed version.
- `$fabricator:publish` loads Publish from the intended installed version.
- ambiguous publishing language asks whether the user means public release or
  local/pre-public work.

## Public Smoke

After pushing the public repository:

```bash
codex plugin marketplace add iamjudin/Fabricator
```

Then install or upgrade Fabricator in Plugins, start a new chat, and confirm the
fresh-chat loaded skill path matches the released version.

If README install/update commands changed, also run a clean install smoke with
an isolated `CODEX_HOME` or equivalent temporary runtime state and execute the
public README commands exactly as written.

## Public Page Done

A public update is not done until the GitHub repository page is current:

- README-visible behavior is current.
- Changelog entry is current.
- GitHub Release notes are current.
- About description and topics are current or explicitly marked pending
  user/platform action.
- Install/update instructions are current.
- Raw public README and package plugin manifest are current.
- Any raw branch propagation lag is explained with API/exact-commit evidence.
- Public visible asset references are current.

## Post-Public Watch

- After release readiness and runtime smoke pass, ask whether passive monitoring
  should be enabled for this plugin project.
- Ask for monitoring cadence: daily, weekly, or custom.
- Ask which projects or chat patterns count as plugin usage.
- Ask whether Fabricator production-process findings should report to a parent
  Fabricator backlog when a parent project exists.
- If enabled, configure or propose the recurring monitor with the platform
  automation mechanism. If declined, record Watch as disabled/skipped.
