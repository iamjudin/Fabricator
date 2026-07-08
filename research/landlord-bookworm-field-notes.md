# Field Notes: Landlord and Bookworm

Status: preparation material for Fabricator; not a specification and not a
source of plugin architecture. Captured 2026-06-19 from the active project
threads, their current project state, and earlier implementation context.

## How to use these notes

- Treat official Codex/OpenAI documentation as the source for platform
  architecture and contracts.
- Treat Landlord and Bookworm as evidence from real work: useful for workflow
  design, failure modes, and validation, but not automatically reusable as
  architecture.
- Treat the earlier GPT Fabricator as a donor of interaction discipline only:
  root-cause thinking, careful revision flow, and preservation of user intent.
  Its archive-first packaging was a workaround for a manual ChatGPT workflow.
- Keep observation, inference, and future rule separate until Fabricator is
  designed deliberately.

## Product shape confirmed so far

- Fabricator is an extensible Codex plugin. Its first active focus is the
  Codex-plugin creation skill; other skills may be added as the work reveals a
  real need.
- A public publication skill is planned for later as a separate user-facing
  release workflow. Craft may still handle development-adjacent release
  mechanics for the plugin it is creating or maintaining, such as version
  metadata, local marketplace setup, cache-busted reinstall and smoke-test
  preparation. A future GPT skill is likewise a possible sibling and must not
  let GPT-era packaging or manual handoff constraints define the creation
  skill's architecture.
- Shared foundations are welcome only where they are genuinely platform-neutral
  (for example, revision discipline and preservation of user intent). Runtime
  workflow, validation, publishing, and file layout remain skill-specific.

## Shared working preferences observed

- Address the cause, not the cosmetic symptom. Locate where a rule is defined,
  applied, checked, and described before changing it.
- Do not immediately implement every issue uncovered during an external test.
  Capture emergent findings, finish the test, group the findings, then make a
  coherent change batch.
- Future work belongs in a backlog. Completed work belongs in Git history;
  backlog and changelog are different things.
- Make focused Git checkpoint commits after meaningful, validated stages.
  Experiments belong on a branch and are not merged without explicit approval.
- Preserve existing user intent and explicit constraints; model-added process
  must not quietly replace them.
- A Codex agent can work with the repository, test, validate, publish, and
  inspect Git directly. Handoff ZIPs, manifests, and deployment maps are not
  default daily-work artifacts.

## Landlord

### Working solution

- The workflow was reduced from a document chain to staged gates:
  chat-only first response and numbered questions; review canvas; grey coded
  wireframe; then either code iteration or a Figma path. The Figma path starts
  with variables, styles, components, and a style kit. Manual Figma edits are
  shown as a diff before code changes.
- A guard hook enforces the important order: no files on the first rough input;
  a wireframe requires the review canvas; Figma work requires a wireframe.
  Maintenance work is intentionally not blocked.
- Workflow behavior has targeted checks in addition to project validation
  (`_scripts/validate.sh` and hook tests).
- The maintenance workspace uses `_workflow/rules.md` and
  `_workflow/backlog.md`; its backlog explicitly holds external-test findings
  and archive-era cleanup decisions.

### Failures and lessons

- Plugin identity, marketplace configuration, and cache entries can outlive a
  path or display-name change. Duplicate UI entries and dangling hooks occurred
  after migration. Cache/config work needs explicit consent and an application
  restart may be required before judging the result.
- Old documentation templates and archive-era folders can continue to steer an
  agent after the live workflow changes. Remove or demote stale sources of
  truth rather than merely adding a newer document beside them.
- A project move must update all live references: Git client, Codex project,
  marketplace path, plugin runtime path, and any installed/cache identity.
- External testing produces useful emergent behavior. It should be recorded
  before it becomes a patch, otherwise local fixes obscure the pattern.

## Bookworm

### Working solution

- The plugin is deliberately narrow: EPUB/PDF input, a reader-facing Obsidian
  working note, local assets, and invisible internal quality checks.
- A small standard-library helper handles inspection, vault detection, and EPUB
  asset extraction. Real EPUB testing found malformed heading markup and led to
  a fallback rather than an assumption that all EPUB structure is clean.
- The project validates both its own behavior and the official plugin
  validator. A temporary local YAML shim was used only to unblock the official
  validator when its dependency was absent.
- Publishing involved local marketplace metadata, a cache-busting version,
  installation through the UI/deeplink, and a Git checkpoint.

### Failures and lessons

- Early scaffolding happened in the wrong temporary context and had to be moved
  to the actual project directory. Establish the live project root before
  generating files or configuring a marketplace.
- A Landlord hook affected Bookworm context and removed an unrelated backlog
  file. Cross-plugin hooks must be strictly scoped by project/runtime context;
  global-looking automation is a real isolation risk.
- Tooling gaps are not necessarily product failures: the official validator was
  correct, but its YAML dependency was missing. Preserve the original check and
  make the workaround narrow and temporary.
- Packaging and publishing have platform-specific facts. In this case the CLI
  did not support plugin installation; marketplace management was CLI-oriented
  while installation required the UI/deeplink.
- Generated JSON escaped a Russian display name. Validate user-visible metadata
  after mechanical versioning/publishing changes, not just parser validity.
- Reader output must not expose an internal agent work report. Product-facing
  content and internal quality process should stay separate.

### Public release lessons from Bookworm, 2026-07-06

- A public GitHub release does not automatically update the installed Codex
  plugin. In the Bookworm `0.1.5` case, GitHub `main`, tag and release were
  correct, but a clean new chat still used the locally installed `0.1.4`
  bundle because Codex had not refreshed the marketplace/plugin cache.
- A clean new chat resets conversation context, not installed plugin state.
  Public-release tests must verify the installed version, not only the release
  tag or the fact that the chat is new.
- Skill chips or deep links shown in chat text can contain stale cache paths
  such as an old `0.1.3` skill link. Treat those links as evidence to inspect,
  not as proof of the active runtime version. Check installed cache, plugin
  list, and observable behavior.
- For public plugins, the user may not have the `codex` CLI in the system
  `PATH`. Publish instructions should include the UI path or a clear fallback
  instead of assuming terminal access works.
- `Try in chat` launches the installed plugin version. It should not be
  presented as equivalent to "download the latest GitHub release now."
- The public README should explain what the plugin does for a person, not the
  internal development machinery. Bookworm's README improved after removing
  implementation details and keeping only the purpose, skills, installation,
  update and license.
- Public release evidence must include both repository evidence and Codex
  runtime evidence: pushed `main`, tag, GitHub Release, changelog/version,
  plugin validation, and a post-update check that Codex loads the intended
  version in a new chat.
- If the public release is followed by a hotfix, do not assume users are now on
  the hotfix. The update step is its own explicit workflow: marketplace upgrade
  or reinstall, then version verification.
- The root cause of the Bookworm `0.1.5` update failure was the marketplace
  clone, not only the installed plugin cache. Removing and reinstalling the
  plugin still reinstalled `0.1.3` because Codex copied from the stale local
  marketplace clone at `~/.codex/.tmp/marketplaces/bookworm`.
- The successful public-update sequence was: use **Upgrade marketplace** first
  to refresh the local marketplace clone, then use **Upgrade** on the plugin,
  then open a new chat and ask/check the loaded version. After marketplace
  upgrade, Bookworm's local marketplace clone moved to commit `7102b09` /
  `v0.1.5`, and `plugin.json` showed `0.1.5+codex.20260706164736`.
- If reinstalling a public plugin keeps returning an old version, inspect the
  marketplace clone revision/manifest before blaming the GitHub release or the
  plugin install step.

## Questions to carry into Fabricator design

- Which workflow stages deserve an enforceable hook, and which should remain
  guidance so maintenance is not accidentally blocked?
- How should a plugin declare its scope so hooks and automation cannot act on a
  neighboring project?
- What is the smallest official validation and publishing loop that gives a
  reliable release without reviving archive-first maintenance?
- How should Fabricator distinguish an observed local workaround from a
  reusable platform rule?
- Which user corrections are stable preferences: direct repeated corrections
  and explicit rules are candidates; one-off comments should remain context
  until corroborated.

## Fabricator Craft battle test in Landlord, 2026-07-03

### What happened

- Fabricator was invoked in the active Landlord maintenance project and used
  as a companion for external plugin testing rather than as a clean-room
  scaffold.
- The first useful behavior was restraint: when the user said to accumulate
  knowledge, Fabricator did not edit code or backlog and treated the signal as
  an observation.
- When the user explicitly asked whether the observations were being captured,
  Fabricator added focused backlog items and committed them separately.
- After more evidence from chat screenshots and a Figma file audit, Fabricator
  grouped the findings into one implementation batch instead of applying
  one-off cosmetic fixes.
- The resulting Landlord changes updated the runtime skill, references,
  canvas template, test protocol, validator, README, deployment map and backlog
  status. This is a good example of fixing the rule across definition,
  application, documentation and checks.
- The final reinstall step updated a cache-busted version and confirmed
  installation with the available CLI, then summarized the next smoke-test
  route for a fresh chat.
- The follow-up Landlord decision at that time made CLI cachebuster/reinstall
  the main local update behavior: verify `codex plugin list`, the installed
  cache version/path, and test in a new chat. Later pre-public evidence
  superseded this as the default rule; see the later note below.
- A later reinstall attempt exposed a separate hook layer: explicit invocation
  through `$landlord` or the menu governs when the skill workflow activates,
  but an already-registered lifecycle hook can still fire on `PreToolUse` or
  `Stop` from a stale installed cache path. In that case the fix is not a
  skill-invocation rule; it is an install/cache registration recovery.
- A later dev-safe update fix exposed a more specific root cause: `hooks.json`
  commands that expand to a versioned installed-cache path can keep pointing at
  a removed bundle inside an already loaded thread after a cachebuster update.
  Landlord addressed this with a fail-open wrapper, a validator that rejects
  direct fragile hook paths, and an explicit rule to update hook-bearing plugins
  from an external terminal or a fresh Codex session rather than from the
  currently hooked thread.
- Later pre-public plugin development evidence superseded the earlier
  CLI-first reinstall habit: the reliable development workflow is hard-clean
  stale installed/cache/marketplace tails for the target plugin, install through
  the Codex UI, then verify in a fresh chat. CLI reinstall is useful as
  diagnostics for stale state and path/version evidence, but should not be the
  trusted install/update path before public release unless current platform
  evidence proves otherwise.

### What worked well

- Evidence-first behavior matched the desired workflow: observe, classify,
  capture, then implement after the user clearly moved from observation to
  action.
- Backlog and Git were used correctly: future observations went to backlog,
  completed work moved to Done, and focused commits recorded each stage.
- Root-cause framing was good. The Figma problem was not treated as a visual
  screenshot issue; Fabricator inspected the actual Figma structure and found
  duplicate styles, missing components, tiny frame heights and overflow-based
  layout.
- The implementation reached the validation layer by adding explicit
  `_scripts/validate.sh` checks for the new Landlord workflow contracts.
- Communication stayed direct and useful: Fabricator stated what it was doing,
  why it was safe, and what had not been verified.

### Risks and lessons for Fabricator

- Do not collapse all publication-like work into one bucket. Craft should
  handle local development release mechanics when they are necessary to test or
  maintain the plugin. The later Publish skill is for public publication as a
  dedicated workflow, like the Bookworm marketplace/public-release work.
- The implementation batch was large enough to be useful, but Craft should
  continue naming scope before edits so the user can stop or narrow a batch
  before product files change.
- Local CLI behavior changed from earlier expectations during this run, but
  later pre-public evidence narrowed the rule again: use CLI reinstall for
  diagnosis and path/version evidence, while the reliable development update is
  hard-clean plus UI install followed by a fresh-chat smoke test.
- Menu-based or `$`-based activation does not by itself prove hooks are
  isolated. Fabricator should treat lifecycle hook registration, installed
  cache files, marketplace metadata, and skill invocation as distinct runtime
  layers when diagnosing plugin behavior.
- For plugins with lifecycle hooks, Fabricator should design the hook command
  and update workflow together. Prefer a stable wrapper or other cache-resilient
  command path, validate that fragile versioned cache paths cannot return, and
  warn the user before updating a hook plugin from a thread that may already
  hold the old hook registration.
- The best observed pattern is not "always make a huge patch"; it is
  "collect enough related evidence, then patch the whole contract surface that
  defines the behavior."
