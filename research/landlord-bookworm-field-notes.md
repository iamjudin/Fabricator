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
- The follow-up Landlord decision made this the main local update behavior:
  after a confirmed CLI cachebuster/reinstall, do not press the UI install
  plus again. Verify `codex plugin list`, the installed cache version/path, and
  test in a new chat. Do not clean cache or installation tails without explicit
  approval.

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
- Local CLI behavior changed from earlier expectations: `codex plugin add`
  was available in this run, while earlier notes said UI install was required.
  Fabricator should verify current tool behavior at the moment of use and not
  rely on stale platform assumptions.
- A successful CLI reinstall changes the next user instruction: the right
  smoke-test step is a new chat/thread, not another UI install click.
- The best observed pattern is not "always make a huge patch"; it is
  "collect enough related evidence, then patch the whole contract surface that
  defines the behavior."
