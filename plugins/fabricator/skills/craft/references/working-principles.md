# Working Principles

Use these principles for every Fabricator Craft task.

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
- For pre-public plugin development, use hard-clean plus Codex UI install as
  the default runtime update workflow. Use CLI reinstall to diagnose installed
  state, marketplace/cache paths, and stale tails, not as the trusted user-facing
  update path unless current platform evidence proves otherwise.
- Do not wait for a separate user push to perform that runtime update stage
  after validated source changes have been approved for pre-public testing.
  A plugin update is not done at source commit if its intended evidence includes
  installed runtime behavior. Continue through scoped hard-clean, UI install
  handoff, installed-version/path verification, and fresh-chat smoke testing.
  If the current chat cannot complete the UI action itself, give the exact UI
  action required and report the stage as blocked/incomplete rather than done.
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
  scoped hard-clean for the target plugin, Codex UI install from the intended
  local marketplace/source, installed-version/path verification, then a fresh
  test chat. Keep CLI reinstall/add as diagnostics unless current platform
  evidence says it is the trusted install path.

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
