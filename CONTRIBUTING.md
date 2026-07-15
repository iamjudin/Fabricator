# Contributing

Thanks for helping improve Fabricator.

## Good Contributions

- Bug reports with the plugin version, installed cache path, and reproduction
  steps.
- Documentation fixes for install, update, release, or runtime verification.
- Workflow improvements that preserve the separation between Craft and Publish.
- Validation scripts that make release evidence more reliable.

## Local Validation

Run from the repository root:

```bash
scripts/validate.sh
git diff --check
```

## Pull Requests

Keep pull requests focused. Include:

- what changed;
- why it changed;
- validation that passed;
- any remaining runtime or release risk.

Use English names in files, paths, manifests, docs, release notes, and
marketplace metadata: `Fabricator`, `Craft`, and `Publish`.
