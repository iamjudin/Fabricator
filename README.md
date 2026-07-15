# Fabricator

Fabricator helps create, maintain, publish, and observe reliable Codex plugins.

It has three workflows:

- **Craft** creates and maintains local or pre-public Codex plugins.
- **Publish** prepares public plugin releases with package, repository, and
  runtime evidence.
- **Watch** sets up and runs post-public monitoring so released plugins can
  collect usage signals into their own backlog.

Fabricator is strict about runtime state because Codex plugins can look updated
in source while an old cache or old chat keeps running something else. Charming,
if your hobby is debugging ghosts.

## Features

- Build Codex plugin workflows from an idea or an existing project.
- Maintain skills, hooks, marketplace setup, validation, and local runtime
  installation.
- Separate accumulation of findings from implementation work.
- Verify installed cache, version, and fresh-chat loaded skill paths before
  judging test results.
- Prepare public releases with README, license, changelog, CI, marketplace,
  runtime, and fresh-chat evidence.
- Keep the public GitHub page current during every public update, including
  README-visible behavior, changelog, release notes, About/topics, and
  install/update instructions.
- Treat local marketplace smoke as diagnostic for public releases; final public
  evidence checks the public repository, raw README/package metadata, clean
  install instructions when they change, and visible asset references.
- Ask after publication whether a released plugin project should be monitored,
  how often, and where usage findings should be routed.

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

Use Watch for post-public monitoring setup or backlog intake:

```text
$fabricator:watch
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

## Development

Validate the repository from the root:

```bash
scripts/validate.sh
git diff --check
```

The plugin package lives in `plugins/fabricator`.

## Contributing

Issues and pull requests are welcome for bug reports, documentation fixes,
workflow improvements, and validation hardening. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Fabricator is source-available under the [PolyForm Noncommercial 1.0.0](LICENSE)
license. It is free to use, modify, and redistribute for noncommercial purposes.
