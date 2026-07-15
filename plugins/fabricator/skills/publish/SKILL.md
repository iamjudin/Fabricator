---
name: publish
description: Prepare and verify a Codex plugin for public publication. Use after explicit invocation as $fabricator:publish, or when the user clearly says the plugin should be published publicly, released publicly, or prepared for a public marketplace/GitHub release. If publication intent is ambiguous, clarify public release versus local/pre-public work before using this skill.
---

# Publish

Prepare a Codex plugin for public release. Publish is a release workflow, not a
local maintenance shortcut. It turns an already useful plugin into a public
package with clear documentation, release evidence, and runtime verification.

Read `references/publication-principles.md` before changing release files or
declaring a release ready.

## Scope

Use Publish for public release preparation:

1. Public repository readiness.
2. Marketplace package layout.
3. README, changelog, license, contribution files, and GitHub metadata.
4. Release validation and CI.
5. Public install/update instructions.
6. Runtime evidence from marketplace, installed cache, and fresh-chat smoke.
7. Public GitHub page refresh for every public update.

Do not use Publish for ordinary local plugin creation, fixes, or pre-public
runtime update work. That is Craft unless the user clearly chooses public
publication.

## Start With Release Surfaces

1. Identify the canonical release root, plugin package root, marketplace root,
   installed runtime, and public marketplace clone when available.
2. Identify the release surfaces. The default surface is the Codex plugin
   package. Companion assets, pets, generated visual packages, docs sites, or
   binary artifacts are optional surfaces only when the project actually has
   them.
3. Check whether the user asked for public release or local/pre-public work. If
   ambiguous, ask one concise clarification before switching to Publish.
4. Verify current official Codex/OpenAI or GitHub facts when platform behavior
   matters and is not already proven in the project.

## Public Package Gates

For the Codex plugin package, verify:

1. `.agents/plugins/marketplace.json` has the intended marketplace name and
   points to the canonical `./plugins/<plugin-name>` package.
2. `plugins/<plugin-name>/.codex-plugin/plugin.json` has stable public metadata:
   name, version, description, license, keywords, interface text, icon/logo
   paths, and capabilities.
3. Every user-facing skill has concise routing and does not claim private or
   pre-public behavior as a public promise.
4. Package assets referenced by the manifest exist inside the package.
5. Validation scripts are executable and deterministic enough to run before
   every release.

## Repository Gates

Verify public repository presentation:

1. README answers what, why, install, use, update, development, license.
2. README commands match the actual package layout and marketplace name.
3. Visuals are used only when useful. A banner is optional, not mandatory.
4. `LICENSE`, `CHANGELOG.md`, and `CONTRIBUTING.md` exist when the project is
   meant for public use.
5. Issue/PR templates exist when the project accepts feedback or contribution.
6. CI runs the same meaningful validation as local release checks.
7. GitHub About/description/topics are listed as manual release evidence when
   they cannot be verified locally.
8. For every public update, refresh the public GitHub page before release:
   README-visible content, About description, topics, release notes, changelog,
   installation/update instructions, and any visible asset references affected
   by the change.
9. Do not treat build/runtime checks as sufficient release evidence if the
   public repository page still describes the old behavior.
10. For user-facing public changes, verify the canonical public repository, not
    only the local checkout or installed cache. Check the public GitHub page and
    raw public artifacts such as `README.md` and `.codex-plugin/plugin.json`
    after push/release when network access is available.
11. Check visible assets for stale references. If the public page, README,
    manifest, or package points at an old icon, banner, pet, screenshot, or
    renamed asset, the public update is not done.
12. If a raw branch URL lags behind the pushed commit, compare against the
    remote SHA, GitHub API contents, and exact-commit raw URL. Treat confirmed
    branch raw lag as propagation evidence to report, not as permission to skip
    public repository verification.

## Runtime Gates

Public release evidence must include both repository and Codex runtime layers:

1. Clean Git status and pushed branch/tag evidence when publishing remotely.
2. Local validation and official plugin validation.
3. Public GitHub page evidence: README/changelog/release notes plus About
   description/topics checked or explicitly marked pending user/platform action.
4. Marketplace add/upgrade evidence.
5. Installed plugin version and cache path.
6. Fresh-chat loaded skill path matching the intended installed version.
7. Smoke test of the public behavior, outside the plugin source repository when
   repository context could distort the result.
8. Clean install smoke evidence when public install/update instructions changed:
   use an isolated `CODEX_HOME` or equivalent temporary runtime state and run
   the README commands exactly as written.
9. If raw public branch artifacts are stale while the marketplace clone and
   exact commit are current, record that as a public artifact propagation
   signal and verify the installed marketplace source separately.

Local marketplace smoke can diagnose package shape, but it is not final public
release evidence. The final public gate must exercise the public repository or
public marketplace path that users are told to use.

If a chat preview points at an older or missing cache path, treat the smoke test
as stale runtime evidence, not product behavior.

## Output

Give a release readiness result:

- `Ready`: all required gates passed and only optional notes remain.
- `Blocked`: at least one release-critical gate failed.
- `Pending user/platform action`: the remaining step cannot be completed by the
  agent, such as setting GitHub topics, enabling 2FA, or final UI-only publish.

Do not call a release ready without evidence.
