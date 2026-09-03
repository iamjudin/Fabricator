# Fabricator

Fabricator helps create, maintain, publish, and review reliable Codex plugins.

It has two workflows:

- **Craft** creates and maintains local or pre-public Codex plugins.
- **Publish** prepares public plugin releases with package, repository, and
  runtime evidence.

Fabricator is strict about runtime state because Codex plugins can look updated
in source while an old cache or old chat keeps running something else. Charming,
if your hobby is debugging ghosts.

## Features

- Build Codex plugin workflows and plugin-adjacent project surfaces from an
  idea or an existing project.
- Classify whether the current work is a plugin surface, project surface, or
  mixed surface before applying gates.
- Start new projects with an understanding gate: outcome, boundaries,
  assumptions, open questions, risks, and the smallest next step.
- Keep project artifacts in project-owned paths by default and treat global
  temp as throwaway-only.
- Maintain skills, hooks, marketplace setup, validation, and local runtime
  installation.
- Check GitHub remote/auth readiness before remote creation, push, tag, or
  release, and stop at a clear user-action boundary when auth is missing.
- Separate accumulation of findings from implementation work.
- Verify installed cache, version, and fresh-chat loaded skill paths before
  judging test results.
- Recover current Fabricator instructions when an old UI skill link points at a
  removed installed-cache path.
- Prepare public releases with README, license, changelog, CI, marketplace,
  GitHub Release/tag, runtime, and fresh-chat evidence.
- Keep the public GitHub page current during every public update, including
  README-visible behavior, changelog, release notes, About/topics, and
  install/update instructions.
- Treat local marketplace smoke as diagnostic for public releases; final public
  evidence checks the public repository, raw README/package metadata, clean
  install instructions when they change, and visible asset references.
- When Fabricator changes a shared production standard, check downstream child
  plugin projects and propagate the smallest durable update or backlog item.
- Keep post-release learning manual: inspect named chats when the user points
  at a concrete issue, then route findings to the owning backlog.

## Install

Add the marketplace from GitHub:

```bash
codex plugin marketplace add iamjudin/Fabricator
```

Then open Plugins in Codex, find **Fabricator**, click Add, and start a new
chat.

Use Craft for local creation and maintenance:

```text
$fabricator:craft
```

Use Publish for public release preparation:

```text
$fabricator:publish
```

If you say that you are publishing without making public/local intent clear,
Fabricator should ask whether this is a public release or continued local
pre-public work. Local work stays with Craft by default.

## Update

Upgrade the marketplace snapshot:

```bash
codex plugin marketplace upgrade fabricator
```

Then upgrade or reinstall Fabricator in Plugins and start a new chat.

## Contributing

Issues and pull requests are welcome for bug reports, documentation fixes,
workflow improvements, and validation hardening. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Fabricator is source-available under the [PolyForm Noncommercial 1.0.0](LICENSE)
license. It is free to use, modify, and redistribute for noncommercial purposes.
