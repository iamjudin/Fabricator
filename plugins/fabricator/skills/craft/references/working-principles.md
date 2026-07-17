# Working Principles

Use these principles for every Fabricator Craft task.

Use English names in files, paths, manifests, docs, README, release notes, and
marketplace metadata: `Fabricator`, `Craft`, and `Publish`. Russian names are
only a chat convention with the user.

## Method integrity

- Maintain one canonical core for the current plugin. Its active skills, tests,
  scripts, and documentation must agree with it.
- For each critical rule, know where it is defined, applied, and tested. Do not
  leave it only in optional reference material.
- Do not remove working mechanics merely to make instructions shorter. Remove
  repetition and secondary explanation first.
- Do not widen agreed scope silently. Explain the required wider change and its
  consequence before making it.
- If required source material is unreadable or incomplete, do not reconstruct
  it from memory. State what is missing and request a usable source.
- After a change, check that previously agreed behavior, rules, files, and
  tests have not been unintentionally lost.

## Project practice

- The user may give only the main project folder. Choose the remaining
  Codex-appropriate organization independently and explain meaningful choices.
- When continuing after a context move, begin from a compact handoff anchor:
  the last accepted conclusion, the project it belongs to, and the next
  practical action. Recommend a fresh chat when runtime state matters, such as
  after plugin install/update verification or when old skill/hook context may
  still be loaded.
- Use the project's backlog for future work and Git history for completed work.
  Mention overlap with an existing backlog item before starting related work.
- Record external materials compactly: distinguish material that affected the
  result from material merely reviewed or not used.
- Use current official sources when platform behavior or a technical obstacle
  is uncertain. Keep any workaround narrow, reversible, and separate from the
  product contract.
- If a plugin uses lifecycle hooks, design the hook command and the update
  workflow as one contract. Avoid direct fragile versioned installed-cache paths
  where a cachebuster can leave the active thread pointing at a removed bundle;
  prefer a stable wrapper or other cache-resilient route, add validation so the
  fragile path cannot return, and warn before updating hook-bearing plugins from
  a thread that may already hold the old hook registration.
- Treat plugin maintenance as two modes. In accumulation mode, the user is
  gathering findings, screenshots, comments, research, and corrections; record,
  group, and preserve them without changing source unless explicitly asked.
  In implementation mode, the user has approved turning accumulated findings
  into product changes; the accepted scope is the complete
  implementation-to-runtime path unless explicitly narrowed. Do not stop at
  source edits, validation, or a Git commit when the change is meant to be
  tested as an installed Codex plugin.
- Definition of done for a pre-public plugin update includes: validated source
  changes, focused checkpoint commit, scoped uninstall or hard-clean of the
  target installed runtime, reinstall from the intended local marketplace/source,
  installed-version/path verification, cache manifest comparison against source,
  and a restart/fresh-chat boundary for final smoke testing.
- A source-only fix is not done when the user's expected surface is the installed
  plugin. Do not end with "source updated", "source committed", or "cache still
  needs reinstall" as the final state unless the user explicitly narrowed the
  task to source only. Continue through cachebuster/reinstall/runtime preflight
  yourself; if the only remaining step is an unavoidable Codex restart or fresh
  chat, name the exact boundary and treat final smoke as pending that boundary.
- If the user says they are publishing, releasing, making the plugin public, or
  similar, determine the intended mode before changing workflow. Public release
  belongs to Publish. Local/pre-public update and testing remain Craft by
  default. If the wording is ambiguous, ask one concise clarification.
- Prefer doing uninstall/install yourself with trusted Codex plugin commands
  such as `codex plugin remove <plugin@marketplace>` and
  `codex plugin add <plugin@marketplace>` when current evidence shows they work.
  Use UI install only as a fallback when commands are unavailable or fail, and
  do not ask the user to do manual uninstall/install/cache work while an agent
  path is available.
- Keep runtime cleanup narrowly scoped. Remove only the target plugin's installed
  state/cache/stale tails, preserve marketplace source unless intentionally
  changing it, back up config before any manual config edit, and never touch
  neighboring plugins as part of a target plugin update.
- Before evaluating any external test chat, verify that the test is running the
  intended build. This applies whenever the user says they are testing, points
  to a named plugin/test chat/project, or asks whether a result reflects the
  latest work. Check the source `.codex-plugin/plugin.json` version, plugin
  list/install state when available, installed cache path/version, active config
  plugin entry, hook-state paths for hook-bearing plugins, and the loaded skill
  path shown by a fresh chat preview or thread evidence.
- Stop the test and report a runtime mismatch if any signal says the build is
  not current: the plugin is not installed, only the marketplace source remains
  in config, cache is empty, installed version is older than source, the test
  chat uses an old skill/cache path, hook state points at a stale versioned
  bundle, or the evidence cannot prove which build is active. Do not analyze
  behavioral failures as product defects until the version being tested is
  known.
- When a runtime mismatch is found, provide the next concrete recovery action:
  scoped uninstall/hard-clean for the target plugin, reinstall from the intended
  local marketplace/source, installed-version/path verification, restart Codex
  when needed, then a fresh test chat. Prefer self-service commands first; leave
  a manual UI instruction only when no verified agent path remains.
- A UI-inserted skill chip may be serialized as a markdown link to a specific
  versioned cache path. If that linked `SKILL.md` path no longer exists after a
  plugin upgrade, treat the link as stale runtime evidence, not proof that the
  skill is unavailable. Resolve the latest installed plugin via `codex plugin
  list`, current cache directories, or the marketplace clone, and load the same
  skill from the current installed version before continuing.
- For explicit Fabricator invocations with missing serialized paths, recover by
  intent before giving up: visible skill label, plugin id and skill id, current
  installed marketplace clone, cache manifest, and source project skill file
  when available. Record the stale path as evidence and continue with the
  newest proven Fabricator instructions.
- Treat tool-route blocks as first-class production signals. If a workflow
  promises a route through Figma, browser, GitHub, or another connector, and a
  hook/guard/state machine blocks that route, inspect the blocking condition
  before continuing. Decide whether it is an intended gate, a stale runtime
  artifact, a missing marker, or a false positive. A false positive requires a
  source fix, regression test, documentation/backlog update, reinstall/runtime
  verification for plugin work, and a renewed smoke attempt or explicit
  "pending restart/fresh chat" boundary.

## User-facing quality

- Keep output oriented to the plugin user, not an agent's internal process.
- Use the note/chat language for structure, headings, labels, field names and
  generic wording. Translate foreign terms when the local equivalent is
  established and reads naturally; keep originals for product/framework/source/
  brand/publication names, acronyms, professional terms that are more natural
  in the original, or cases where translation is artificial.
- Never invent sources, links, behavior claims, or verification results.
- Check consistency across active instructions, code, tests, documentation,
  configuration, and observed runtime behavior before calling work complete.
