# Plugin Design Principles

Status: working principles distilled from the completed Bookworm work and
Landlord observations on 2026-06-24. They are design criteria for Fabricator,
not a substitute for current official Codex documentation.

## Product and skill boundaries

1. Give every skill one clear job and state what it must not do. Bookworm's
   `Refine` restores and normalizes source material; `Enrich` adds a clearly
   separated external layer. Fabricator may gain further skills, but its
   current focus is the Codex-plugin creation skill.
2. Do not let an implementation workflow leak into the product workflow. A
   user-facing skill must not create specs, plans, commits, worktrees, or ask
   the user to choose agents unless that is the skill's actual job.
3. Preserve the user's intent over generic agent conventions. Repeated direct
   corrections and explicit constraints are stronger than convenient defaults.
4. Keep a single current source of truth for active rules. Retire, demote, or
   clearly label archive-era material so it cannot quietly steer runtime work.

## User data and interaction

5. Treat user data as staged work when the operation affects user-owned
   material: inspect and prepare a temporary result, show the meaningful
   outcome, then write, replace, move, or delete only after explicit
   confirmation. This is a safety pattern, not a universal interaction rule.
6. Use the user's language and expected tone consistently. In this workspace,
   speak Russian on "ты": friendly, direct, and professional. Small mismatches in
   address or terminology are real product defects when the skill is used in a
   personal knowledge space.
7. Keep product output reader-facing. Internal checks, method notes, runtime
   details, and agent self-reports belong in logs or final status, not inside
   the user artifact.
8. Preserve provenance. Never invent citations or links; distinguish verified
   sources, unresolved references, and new external material visibly.

## Runtime correctness and isolation

9. Establish the real project root, target scope, and writable destination
   before generating files or changing configuration. The user may provide only
   the main project folder; organize the remaining Codex-appropriate structure
   independently.
10. Scope hooks, automations, caches, and cleanup to their own plugin and
    project. A plugin must not affect a neighboring project merely because the
    host application shares a context or marketplace.
11. Test user-facing skills outside their source repository when the repository
    context could trigger development behavior. Runtime context is part of the
    product contract.
12. Build for imperfect inputs and changing environment state: malformed source
    structure, missing dependencies, vanished directories, iCloud paths, and
    stale candidates need explicit, truthful handling rather than empty output
    or guesses.
13. Use temporary run directories for intermediate artifacts. Clean them only
    after the confirmed handoff and verification, never before.

## Validation and learning

14. Test observable behavior, not only instruction text. A contract test should
    prove the generated TOC works, a file remains untouched, an offer appears
    in every correct success branch, or a prohibited side effect does not occur.
15. Turn each reproduced field failure into a focused regression test before or
    alongside the fix. Hotfixes should close the exact branch that failed.
16. When the user supplies a test-chat link, analyze it and record the findings
    first. Do not implement them until the user explicitly approves taking the
    findings into work.
17. During external tests, record emergent findings first; finish the run,
    group related work, then implement a coherent batch. Keep future work in a
    backlog and completed work in Git history.
18. When technical difficulty arises, look first to current official sources.
    Prefer narrow, reversible workarounds for missing tooling and keep the
    original official check intact. A workaround must not redefine the product
    contract.

## Method integrity and change control

19. Before implementation, derive one compact canonical core for the plugin:
    purpose, main scenarios, stages, artifacts, terms, constraints, and
    transitions. Skills, tests, and any references must agree with this core.
20. Separate the user's established method from the agent's proposed
    improvement. Never merge an agent-added enhancement into the method
    silently.
21. For every important rule, identify where it is defined, applied, and
    tested. Critical rules must live in active skill/runtime instructions and
    tests where appropriate, not only in optional reference material.
22. Do not shorten away working mechanics. Remove repetition or secondary
    explanation first; retain necessary constraints, stages, and verifiable
    conditions.
23. Assess the change surface before editing. Distinguish a local correction
    from a cross-layer change, and inspect all affected rules, code, tests, and
    documentation in the latter case.
24. Do not widen the agreed scope silently. When a requested fix requires a
    broader change, explain the consequence and obtain a decision before
    making the additional change.
25. If a required input is unreadable or incomplete, do not reconstruct it
    from memory or guesswork. State the boundary and request a usable source or
    the minimum missing clarification.
26. Reuse established context. Ask only questions that expose a genuine gap or
    contradiction; do not ask the user to repeat an adequate brief.
27. Do not turn technical alternatives into a menu by default. Choose and
    recommend a path when the evidence permits; ask only when the decision is
    genuinely the user's.
28. After a change, explicitly check for unintended losses of previously
    agreed behavior, rules, files, or tests.
29. Keep conversational logs, approval history, and internal reasoning out of
    the product unless they are deliberately useful to its end user.
30. For external materials, distinguish what materially influenced the result,
    what was merely reviewed, and what was not used. Keep this provenance
    compact and relevant.
31. Final validation checks consistency across all active layers: instructions,
    code, tests, documentation, configuration, and observed runtime behavior.
32. Final status reports distinguish completed and verified work from planned
    work, known limits, and work not performed.

## Publishing and maintenance

33. Work locally during development, but do not treat all publication-like
    mechanics as outside Craft. Craft may handle version metadata, local
    marketplace setup, cache-busted local install/reinstall, smoke-test setup
    and Git checkpoints when they are part of creating or maintaining the
    plugin. The future publication skill is for public release as a distinct
    user-facing workflow.
34. Treat repository, remote Git host, marketplace, installed cache, and active
    chat as distinct layers. Publishing source code does not prove users run the
    new version; already-open chats can retain the older skill context.
35. For public releases, verify both sides: repository evidence (`main`, tag,
    GitHub Release, changelog/version) and Codex runtime evidence (marketplace
    refresh, plugin upgrade/reinstall, installed cache version/path, and a
    new-chat smoke test). A clean new chat does not update the installed plugin
    by itself, and `Try in chat` runs the installed version, not necessarily the
    latest GitHub release.
36. When updating a public plugin, refresh the marketplace layer before judging
    the plugin install layer. If reinstalling the plugin still returns an old
    version, inspect the local marketplace clone revision and manifest; a stale
    marketplace clone can reinstall the old plugin even after remove/reinstall.
37. Make public documentation explain the outcome and primary actions, not the
    development machinery. Keep installation/update instructions short and
    correct for the current platform. Include a UI-friendly update path when
    the `codex` CLI may not be available in the user's terminal `PATH`.
38. For local development reinstall, prefer the current supported path:
    cache-bust the version, reinstall through the available CLI/UI mechanism,
    verify the installed plugin list and cache version/path, then test in a new
    chat so fresh runtime context is loaded. Do not ask the user to click the
    UI install/add control again after a confirmed CLI reinstall. Clean stale
    cache/config tails only after explicit approval or a demonstrated stale
    cache problem, and never touch unrelated plugins.
39. Create a Git repository before substantial work if the project is not
    connected to one. Explain the chosen setup briefly, commit validated
    milestones independently, and use a test branch for explicit experiments.
40. Find the root cause before changing symptoms: identify where a behavior is
    defined, applied, checked, and documented.
41. When presenting technical options, state the recommended choice and why it
    best fits the current Codex project.
42. Warn before destructive changes, including deletion, replacement, cleanup,
    cache removal, or history-altering Git operations.

## Fabricator implications to verify later

- The creation skill should produce a testable runtime contract, an isolated
  scope, a Git-backed project when appropriate, and only the documentation
  needed for current maintenance.
- Because Fabricator is intended for public installation, the creation skill
  must carry these behavioral rules inside its own instructions rather than
  relying on a user's local Codex setup:
  - find the root cause before applying cosmetic fixes;
  - when presenting technical options, recommend one and explain why it fits;
  - communicate in Russian on "ты", in a friendly and professional tone.
- Public publication comes later as its own skill and should be capable of
  direct Git and marketplace work, while making release evidence explicit
  rather than reviving ZIP-first handoffs. Craft still owns local
  development-release mechanics needed to test and maintain the plugin.
- Final architecture, manifest details, validation commands, and install/update
  mechanics must be checked against current official Codex documentation before
  they become Fabricator rules.
