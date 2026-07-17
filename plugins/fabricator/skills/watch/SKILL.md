---
name: watch
description: Set up or run post-public monitoring for a Codex plugin. Use after explicit invocation as $fabricator:watch, after Publish completes and the user wants passive monitoring, or when the user asks to collect plugin usage signals, field notes, backlog items, or daily monitoring from Codex chats.
---

# Watch

Observe released Codex plugins in use and turn field signals into durable
backlog entries. Watch is an operations workflow, not a development shortcut:
it monitors usage, classifies evidence, and routes findings to the plugin that
owns the behavior.

Read `references/watch-principles.md` before creating monitoring prompts,
automation proposals, or backlog entries.

## Scope

Use Watch after a plugin is public or otherwise released enough that the user is
no longer actively inspecting every test chat by hand.

Watch has two routes:

1. Production-process monitoring: chats where Fabricator is used to create or
   publish a plugin. Findings about Fabricator's workflow belong in the
   Fabricator project backlog.
2. Plugin-usage monitoring: chats where a released child plugin is used without
   Fabricator. Findings about that plugin belong in that plugin's own project
   backlog.

Do not assume every user has a Fabricator project. Child plugins must be able to
own their own Watch layer and backlog.

## Setup Contract

When enabling Watch for a plugin project, create or update a lightweight
observability contract:

- `docs/backlog.md` for durable backlog intake when no backlog exists.
- `docs/field-notes.md` for dated monitoring observations when useful.
- `.fabricator/watch.json` when the project accepts local metadata files.

The contract should capture:

- Plugin id and public display name.
- Project root and backlog paths.
- Automation display name and target label. Names must be unique and
  target-specific, for example `<Plugin> weekly <purpose> (<target scope>)`.
- Thread search queries and aliases.
- Whether Fabricator production-process signals should be reported to a parent
  Fabricator project.
- Whether plugin-usage signals are reported only to the plugin's own project.
- Monitoring cadence and status: active, paused, or disabled.
- Privacy or exclusion rules for chats that should not be inspected.

Keep machine-facing names in English. Local-language names are allowed only as
user-facing aliases for finding chats.

## After Publish

After a public release is ready and runtime smoke has passed, ask the user
whether they want passive monitoring for this plugin project.

Ask only the decisions that belong to the user:

1. Whether to monitor this plugin after publication.
2. How often to monitor: daily, weekly, or a custom cadence.
3. Which projects or chat patterns count as plugin usage.
4. Whether production-process findings should also be reported to a parent
   Fabricator backlog when a parent project exists.

If the user declines, record Watch as disabled or skipped. Do not create a
monitor silently.

If the user enables monitoring and automation tools are available, propose or
create the recurring automation using the platform automation mechanism. Before
creating a new automation, inspect existing automations with the same visible
name, plugin id, or target path and update the matching automation instead of
creating a duplicate. Use a display name that includes the plugin, cadence,
monitor purpose, and target scope so parent-project and child-project monitors
cannot look identical in the UI. Prefer a daily cadence when the user says
"regularly" or "passively" without a specific interval, but still state the
chosen cadence.

## Daily Run

For each scheduled run:

1. Identify relevant recent chats using the configured thread queries.
2. Check previous automation runs for stale `inProgress` state before
   interpreting current monitor health. Report stale runs separately from
   active work, with start time and project target when available.
3. Read enough thread context to classify signals, not entire conversations by
   default.
4. Separate Fabricator production-process signals from child-plugin usage
   signals.
5. Deduplicate against the existing backlog.
6. Add concise backlog items with evidence: date, source chat, symptom,
   affected workflow, and suggested next action.
7. Report a digest to the native project thread when configured.
8. When running as a scheduled automation and the platform supports it, archive
   the completed monitor thread after the final digest is produced.

Do not implement fixes during Watch unless the user explicitly switches to
Craft or Publish. Watch can recommend that a finding is ready for Craft or
Publish.

## Output

Give a monitoring result:

- `No signal`: checked the configured sources and found no new actionable item.
- `Backlog updated`: added or updated backlog entries with evidence.
- `Needs setup`: monitoring cannot run until the contract, cadence, or target
  projects are known.
- `Blocked`: required thread access, project access, or automation tools are
  unavailable.

Never claim passive monitoring is active unless a schedule or equivalent
project rule is actually configured.
