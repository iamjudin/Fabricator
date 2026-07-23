# Fabricator Agent Rules

## Useful Simplicity

- Optimize for end-user benefit, not process complexity. Before adding a
  registry, monitor, checklist, automation, abstraction, or cross-project rule,
  compare the practical value against the extra moving parts and failure modes.
- Prefer the simplest durable mechanism that preserves the benefit. If a rule
  can be captured as a small backlog item, checklist line, or one clear
  instruction, do that before adding a new system.
- Treat complexity and fragility as product costs. A solution is not better
  merely because it is more complete; it is better only when the added structure
  pays for itself in less manual work, fewer repeated mistakes, or clearer
  release evidence.
- For downstream propagation, start with impact classification and the smallest
  durable update: existing release checklist, backlog item, Watch contract, or
  direct source fix. Do not create a dedicated downstream registry until the
  number of active child projects or repeated misses make the registry clearly
  cheaper than manual discovery.

## Project Workspace Hygiene

- If a project has a folder, project work belongs inside that folder by
  default: source edits, generated assets, previews, scratch outputs, logs, and
  run artifacts should use project-owned paths.
- Use global temporary directories such as `/private/tmp` only for genuinely
  throwaway helper scripts, sandbox-required intermediates, or artifacts that
  cannot safely live in the project. Prefer project-specific names and clean
  them up before handoff when they are no longer needed.
- If an artifact must remain outside the project, record why, where it lives,
  and who owns cleanup. Do not let global temp become hidden project storage.

## Context Moves

- When continuing work after a context move, restart with a compact handoff
  anchor instead of a generic greeting. State the last accepted conclusion, the
  project it belongs to, and the next practical action.
- If the current work would benefit from a fresh runtime context, say so
  directly and explain why. For plugin development, a fresh chat is especially
  appropriate after install/update verification because already-open chats can
  retain older skill or hook state.
- Use this startup shape when it fits:
  `Подхвати последний вывод: <conclusion>. <next action>.`
- For Fabricator's current pre-public plugin development rule, the handoff
  anchor is:
  `Подхвати последний вывод: pre-public plugin dev workflow = hard-clean + UI install, CLI reinstall только диагностика. Запиши в Fabricator.`
