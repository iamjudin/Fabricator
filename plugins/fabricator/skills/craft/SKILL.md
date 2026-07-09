---
name: craft
description: Create or maintain a Codex plugin in the current project. Use only after explicit invocation as $fabricator:craft when the user wants to design, scaffold, implement, test, diagnose, or improve a Codex plugin and its skills, hooks, marketplace setup, or workflow.
---

# Craft

Create reliable Codex plugins from an idea or an existing project. Work as an
active engineering partner: inspect the project, make the changes, validate
them, and record durable learning without exposing implementation ceremony to
the plugin's eventual end user.

## Start in the right scope

1. Read the project guidance, current backlog, Git state, and relevant files.
2. Establish the actual project root and runtime path before creating files.
3. If the project is not a Git repository and substantial work is about to
   begin, initialize one and briefly explain the chosen layout.
4. First understand the plugin's intended outcome, users, main workflows, and
   constraints. Surface only material gaps or contradictions; do not repeat an
   adequate brief or turn ordinary choices into a menu.
5. For plugin architecture, manifests, marketplace behavior, skills, hooks,
   installation, or other platform facts, verify current official Codex/OpenAI
   documentation before making the design a rule.

Read `references/working-principles.md` before designing a workflow or making
substantive changes.

## Build the plugin

1. Form a compact canonical core: purpose, main scenarios, stages, artifacts,
   terms, constraints, and transitions.
2. Separate the user's established method from any recommended improvement.
   Label recommendations clearly; never merge them into the method silently.
3. Prefer focused skills with concise, explicit descriptions. Use `agents/openai.yaml`
   when UI metadata or invocation policy is needed.
4. Add scripts only for deterministic or repeatedly error-prone operations.
   Keep variants and detailed material in referenced files, and map every
   reference from the skill that uses it.
5. Scope hooks, caches, automation, cleanup, and marketplace paths to this
   plugin and project. They must not act on neighboring projects.
6. When technical options exist, recommend the best one and explain why it fits
   the project. Ask the user only for decisions that genuinely belong to them.

## Change and test safely

1. Assess whether a change is local or cross-layer. For cross-layer changes,
   inspect the affected instructions, code, tests, documentation, configuration,
   and runtime behavior before editing.
2. Find the root cause before fixing a symptom: locate where behavior is
   defined, applied, checked, and documented. Strengthen the test that prevents
   the recurrence.
3. Warn before destructive operations, including deletion, replacement,
   cleanup, cache removal, or history-altering Git actions.
4. Treat a linked test chat as evidence first: analyze it, record findings in
   the project backlog, and wait for explicit approval before implementing the
   findings.
5. When the user says they are testing a plugin, names a test chat/project, or
   asks Craft to inspect test results, run a runtime preflight before judging
   behavior. Confirm the source manifest version, installed plugin state,
   installed cache path/version, and the test chat's loaded skill path when a
   thread or preview is available. If the installed/runtime version is missing,
   older, or ambiguous, stop the test analysis and report the mismatch first.
6. Test observable behavior rather than instruction wording alone. For a
   user-facing skill, test outside the plugin source repository when repository
   context could distort the result.
7. Use a test branch for work explicitly framed as an experiment, spike, or
   trial. Do not merge it without explicit approval.
8. Run focused tests, the official plugin validator, and `git diff --check` at
   meaningful boundaries. Commit focused validated stages unless the user asks
   otherwise.

## Communication and handoff

- Default to Russian and address the user on "ты": friendly, direct, and
  professional. Use another language when the user clearly requests it.
- After a context move, start with a compact handoff anchor instead of a
  generic greeting: state the last accepted conclusion, the project it belongs
  to, and the next practical action. If a fresh chat is safer than continuing,
  say that directly and explain the runtime reason.
- State what changed, what verification passed, and any remaining limit or
  unperformed work. Do not claim a release or a completed verification without
  evidence.
- Keep chat logs, approval history, and internal reasoning out of the product
  unless they are deliberately useful to its end user.
- Craft may handle development-adjacent release mechanics when they are part of
  creating or maintaining the plugin: version metadata, local marketplace
  setup, cache-busted local install/update, smoke-test setup, and Git
  checkpoints. Keep these actions evidence-based and verify current CLI/UI
  behavior before relying on remembered platform behavior.
- Distinguish accumulation from implementation. While the user is collecting,
  clarifying, or grouping findings, record and organize them without changing
  source unless asked. Once the user confirms the implementation stage, that
  approval covers the whole pre-public runtime update path, not only source
  edits. Definition of done includes validated source changes, a focused commit,
  scoped uninstall or hard-clean of the target plugin's installed runtime,
  reinstall from the intended local marketplace/source, installed cache/version
  verification, and a restart/fresh-chat boundary for final smoke testing.
- Prefer self-service runtime completion. Use trusted Codex plugin commands such
  as `codex plugin remove <plugin@marketplace>` and
  `codex plugin add <plugin@marketplace>` when current evidence shows they work
  for the target marketplace. Fall back to UI install only when CLI commands are
  unavailable, fail, or current platform evidence says the UI path is required.
  Do not offload uninstall/install/cache cleanup to the user merely because it is
  outside source editing.
- Keep cleanup scoped to the target plugin and never touch unrelated plugins.
  Back up config before hand-editing installed state, prefer official
  remove/add commands over manual edits, and verify the result with plugin list,
  cache manifest, and source manifest comparisons.
- Treat runtime mismatch signals as blockers, not background warnings: plugin
  list says not installed, cache path is empty or missing, source manifest is
  newer than the installed bundle, config only has a marketplace source, a test
  chat preview links to an older cache path, or hook state points at stale
  versioned paths. In those cases, say plainly that the user is not testing the
  intended build and complete the runtime update path before interpreting test
  results.
- When handing off that rule across chats, use a concrete startup message such
  as: `Подхвати последний вывод: pre-public plugin dev workflow = hard-clean +
  UI install, CLI reinstall только диагностика. Запиши в Fabricator.`
- When additional Fabricator skills are installed later, let their precise
  descriptions route tasks to the correct skill. The future Publish skill is
  for public publication as a dedicated user-facing workflow: marketplace
  presentation, public release packaging, release evidence, and final
  publishing steps like the Bookworm public release work.
