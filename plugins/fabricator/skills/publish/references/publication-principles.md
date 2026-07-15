# Publication Principles

Use these principles for every Fabricator Publish task.

## Naming

- Use English names in files, paths, manifests, docs, README, release notes, and
  marketplace metadata: `Fabricator`, `Craft`, and `Publish`.
- Russian names are only a chat convention with the user.
- Use lowercase ids for machine names: `fabricator`, `craft`, `publish`.

## Mode Selection

- Craft is the default for local and pre-public plugin work.
- Publish starts only when the user clearly chooses public publication.
- If the user says "publish", "release", "make public", or similar without a
  clear public/local distinction, ask whether they mean public release or local
  pre-public work.
- Do not silently turn local maintenance into a public release.

## Release Surfaces

- The default release surface is the Codex plugin package.
- Companion assets, pets, generated visual packages, binary artifacts, docs
  sites, or other side packages are optional surfaces. Include them only when
  the project actually has them or the user explicitly asks.
- Each surface needs its own evidence. A plugin can be ready while a companion
  asset is not, and the reverse can also be true.

## Repository Presentation

- README must explain what the plugin does, why it matters, installation,
  usage, update path, development validation, and license.
- Keep README public-facing. Do not expose internal development machinery
  unless it helps a public user or contributor.
- Visuals are useful when they show the product. A banner is optional.
- `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, issue templates, PR template,
  and CI are release readiness signals for public projects.
- GitHub About description, topics, website/social links, branch protection,
  and account security may require manual verification. Record them as pending
  user/platform evidence when the agent cannot inspect or change them.

## Runtime Evidence

- Publishing source code does not prove users run that version.
- Check repository state, marketplace clone, installed plugin cache, and fresh
  chat loaded skill path as separate layers.
- If reinstalling or upgrading keeps producing an old version, inspect the
  marketplace clone before blaming the plugin cache.
- A fresh chat that loads an old or missing skill path is stale runtime
  evidence and does not pass smoke testing.

## Release Result

- Release readiness must be explicit: `Ready`, `Blocked`, or
  `Pending user/platform action`.
- Name every blocker with a concrete recovery step.
- Do not claim public release completion until validation, package evidence,
  runtime smoke, and required external publication evidence are all present.
