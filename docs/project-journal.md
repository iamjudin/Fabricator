# Project Journal

Compact journal of Fabricator's product decisions and useful project history.
This is not a chat log or a commit log. Keep only events that explain why the
project works the way it does, with evidence from files, commits, release notes,
or explicitly recorded field context.

## 2026-06-19 - Field evidence before architecture

Fabricator started from real plugin-maintenance evidence in Landlord and
Bookworm, not from an abstract framework. The early conclusion was that
Fabricator should be an extensible Codex plugin whose first practical focus is
Codex-plugin creation, while public publication should become a separate
workflow only when the need is real.

Important constraints came from failures in neighboring projects: establish the
real project root before generating files, keep hooks and caches scoped to the
target plugin, preserve user intent over generic agent process, and avoid
letting old archive-era docs remain active sources of truth.

Evidence:

- `research/landlord-bookworm-field-notes.md`
- `research/plugin-design-principles.md`

Article angle: Fabricator was shaped by production failures in small personal
plugins: wrong roots, stale caches, overbroad hooks, and documentation that kept
steering the agent after the workflow changed.

## 2026-07-03 - Craft proved accumulation before implementation

The Landlord battle test confirmed a key behavior for Craft: when the user is
collecting observations, Craft should capture and group evidence without
changing source. Implementation begins only after the user explicitly moves from
accumulation to action.

This also clarified the preferred repair pattern: do not patch a visible
symptom alone. Update the whole affected contract surface: active skill,
references, templates, tests/validators, docs, backlog state, runtime install,
and final smoke boundary when relevant.

Evidence:

- `research/landlord-bookworm-field-notes.md`
- Commits around the pre-public workflow series, including `5457e3c`,
  `e112649`, `5da308a`, `5ce08c2`, `ae1f39e`, and `5fb6196`

Article angle: Fabricator's "restraint" is product behavior. It exists because
agents that immediately patch every observation can destroy the signal before a
coherent fix is designed.

## 2026-07-14 - Publication became its own surface

Tarsy publication field notes showed that public release readiness is not one
surface. A plugin package and companion assets, such as a pet package, can have
different evidence requirements and different readiness states. The canonical
release root also matters: matching files are not enough when the installed
runtime points at a duplicate source path.

This prepared the split between Craft and Publish. Craft remains responsible
for local/pre-public development and runtime update mechanics. Publish owns
public repository presentation, marketplace evidence, tags, releases, and
public runtime smoke.

Evidence:

- `research/tarsy-publication-field-notes.md`
- `plugins/fabricator/skills/publish/SKILL.md`
- `plugins/fabricator/skills/publish/references/publication-principles.md`
- Commit `604a357` (`Record Tarsy publication field notes`)

Article angle: "Published" is not a Git push. For Codex plugins it is a chain
of repository, marketplace, installed cache, and fresh-chat runtime evidence.

## 2026-07-15 - Public Fabricator release and Publish hardening

Fabricator moved from pre-public/local plugin work into public release
preparation in `0.2.0`. The project gained public package metadata, README,
changelog, contribution files, CI expectations, release validation scripts, and
a dedicated Publish workflow.

Immediately after the public release, field evidence hardened the release
gates:

- `0.2.1` made public GitHub page refresh part of done.
- `0.2.2` added validation for manifest default prompt length and icon paths.
- `0.2.3` required raw public README/package checks and made local marketplace
  smoke diagnostic only.
- `0.2.4` updated the public README to reflect those release gates.
- `0.2.5` added diagnostics for raw branch propagation lag.

Evidence:

- `CHANGELOG.md`
- `README.md`
- `docs/release-checklist.md`
- `scripts/validate.sh`
- `scripts/validate-public.py`
- Tags `v0.2.0` through `v0.2.5`

Article angle: the first public release did not end the design work; it exposed
which parts of "release evidence" were previously invisible.

## 2026-07-15 - Watch was added for post-public learning

Fabricator `0.2.6` added Watch as the third workflow. The project decision was
to separate active development from passive post-public monitoring. Watch does
not implement fixes; it observes usage, classifies field signals, deduplicates
against a backlog, and routes findings to the plugin that owns the behavior.

The workflow also established that released child plugins should be able to own
their own monitoring contract and backlog. Fabricator receives
production-process findings only when there is a parent Fabricator project.

Evidence:

- `plugins/fabricator/skills/watch/SKILL.md`
- `plugins/fabricator/skills/watch/references/watch-principles.md`
- `docs/release-checklist.md`
- `CHANGELOG.md` entries for `0.2.6`
- Tag `v0.2.6`

Article angle: monitoring is not "more automation for its own sake"; it is a
small loop for converting real usage into durable backlog entries.

## 2026-07-15 to 2026-07-17 - Runtime staleness became a first-class defect

Several releases hardened Fabricator around stale runtime state:

- `0.2.7` updated public positioning for Watch.
- `0.2.8` removed internal development commands from the public README.
- `0.2.9` added recovery when a UI skill link points at a removed installed
  cache path.
- `0.2.10` added downstream-impact gates and stale automation-run detection.
- `0.2.11` added intent-based recovery for serialized Fabricator skill links
  and made Watch automation names target-specific.

The product conclusion is that source files, marketplace clones, installed
caches, hook registrations, already-open chats, and visible skill links are
separate runtime layers. A test result is not meaningful until the intended
build is proven.

Evidence:

- `plugins/fabricator/skills/craft/SKILL.md`
- `plugins/fabricator/skills/watch/SKILL.md`
- `docs/backlog.md`
- `CHANGELOG.md` entries for `0.2.7` through `0.2.11`
- Tags `v0.2.7` through `v0.2.11`

Article angle: stale state is not a rare edge case in plugin development; it is
one of the main product surfaces Fabricator has to manage.

## 2026-07-17 - Useful simplicity became an explicit project rule

After downstream-propagation work, the project added a constraint against
building systems too early. Fabricator should start with the smallest durable
mechanism that preserves the benefit: an existing checklist, backlog item,
Watch contract, or direct source fix. A dedicated registry or new automation is
worth adding only when repeated misses make it cheaper than manual discovery.

Evidence:

- `AGENTS.md`
- `docs/release-checklist.md`
- Commits `180801d` and `dd36b46`

Article angle: Fabricator is strict, but not maximalist. The interesting rule is
knowing when a checklist line is better product design than a new subsystem.

## 2026-07-20 - Craft widened to plugin-adjacent project surfaces

Fabricator `0.2.12` changed Craft from a plugin-only workflow into a
plugin-first workflow that can also handle project surfaces and mixed surfaces.
The new gate requires Craft to classify the surface before applying validation:
plugin surface, project surface, or mixed surface.

This release also added a project-start understanding gate after a field failure
where Craft implemented too early despite a request for analysis first. New
plugin or project work now starts by restating the task, outcome, boundaries,
assumptions, open questions, risks, and smallest next step. If the user asks for
analysis first, implementation must wait.

Evidence:

- `plugins/fabricator/skills/craft/SKILL.md`
- `plugins/fabricator/skills/craft/references/working-principles.md`
- `docs/backlog.md`
- `CHANGELOG.md` entry for `0.2.12`
- Commits `92359b9`, `8081fb1`, and `e46b0ac`
- Tag `v0.2.12`

Article angle: the project-start gate is a product lesson about consent and
scope, not just a planning nicety.

## 2026-07-20 - Current state snapshot

Current public version is `0.2.12+codex.20260720120000` in the plugin manifest.
The active product surface has three workflows:

- Craft: local/pre-public plugin and plugin-adjacent project creation or
  maintenance.
- Publish: public release preparation with repository, GitHub Release/tag,
  public page, marketplace, runtime, and fresh-chat evidence.
- Watch: post-public monitoring, field-note classification, and backlog intake.

The project has release validation scripts, a public release checklist, a
backlog with closed evidence-backed items, research field notes, and public docs.
There are no open backlog items at the time this journal entry was created.

Evidence:

- `plugins/fabricator/.codex-plugin/plugin.json`
- `README.md`
- `CHANGELOG.md`
- `docs/backlog.md`
- `docs/release-checklist.md`
- `scripts/validate.sh`
- `scripts/validate-public.py`

Useful future article threads:

- Why Codex plugin development needs runtime evidence beyond Git.
- How field failures became product rules without turning into bureaucracy.
- Craft/Publish/Watch as a lifecycle split: build, release, observe.
- The tension between strict release gates and useful simplicity.
- Why Fabricator treats stale links, caches, and already-open chats as product
  facts, not operator mistakes.
