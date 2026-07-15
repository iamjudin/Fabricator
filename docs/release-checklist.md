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

- Confirm `README.md` explains what, why, install, use, update, development,
  and license.
- Confirm `LICENSE`, `CHANGELOG.md`, and `CONTRIBUTING.md` are current.
- Confirm issue and PR templates are present.
- Confirm CI runs `scripts/validate.sh`.
- Confirm GitHub About description and topics are set manually before final
  public launch.

## Validation

Run from the repository root:

```bash
scripts/validate.sh
git diff --check
```

## Local Smoke

```bash
codex plugin marketplace add /Users/iamjudin/Desktop/Plugins/Fabricator
codex plugin add fabricator@fabricator
```

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
