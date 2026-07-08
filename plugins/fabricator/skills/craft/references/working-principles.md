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
