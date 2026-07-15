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
- Updating the public GitHub page is part of the definition of done for every
  public update. Do not stop at build, package, or runtime checks if README,
  changelog, release notes, About description, topics, install/update commands,
  or visible assets still describe the old release.
- User-facing public changes must flow through the canonical public repository.
  A local checkout, local marketplace, or installed cache can be useful
  diagnostic evidence, but it is not final public evidence by itself.
- When network access is available, verify raw public artifacts after push:
  at minimum the public `README.md` and package `.codex-plugin/plugin.json`.
  These catch "works locally" releases where the GitHub page or package source
  still exposes old instructions or metadata.
- Raw branch URLs can lag behind the pushed commit. If that happens, compare the
  remote SHA, GitHub API contents, and exact-commit raw URL. Report the
  propagation signal and keep checking the public marketplace/runtime source;
  do not silently ignore the mismatch.
- Treat stale visible assets as public-page failures. Icons, banners, pets,
  screenshots, and renamed media need explicit public checks when they are part
  of the package or README.
- Prefer updating GitHub page fields directly when available through trusted
  tooling. If a field requires manual UI work, mark release readiness as
  `Pending user/platform action` rather than silently skipping it.

## Runtime Evidence

- Publishing source code does not prove users run that version.
- Check repository state, marketplace clone, installed plugin cache, and fresh
  chat loaded skill path as separate layers.
- Check public repository presentation as a separate layer too. A correct
  installed plugin with a stale public page is not a complete public update.
- If README install/update commands changed, run a clean install smoke using an
  isolated `CODEX_HOME` or equivalent temporary runtime state. The smoke should
  execute the public instructions exactly as written.
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
