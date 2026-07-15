# Watch Principles

Use these principles for every Fabricator Watch task.

## Ownership

- Fabricator owns signals about the plugin production process: missing release
  gates, stale runtime checks, unclear Craft/Publish routing, public metadata
  failures, and monitoring setup gaps.
- Each child plugin owns signals about its own usage: wrong output, confusing
  user intent handling, missing docs, bad defaults, and domain-specific quality
  failures.
- Do not route every signal back to Fabricator. Users without a Fabricator
  project still need child plugins to observe themselves.

## Timing

- During active local development, Craft can inspect named test chats on demand.
- After publication, Watch handles passive monitoring because the user is no
  longer actively supervising every usage chat.
- Watch setup should be offered after Publish completes, not before release
  evidence is gathered.

## Evidence

- Prefer concrete thread evidence over impressions: source chat, date, plugin
  or skill invoked, observed symptom, expected behavior, and likely owner.
- Keep snippets short and paraphrase when the exact text is not needed.
- Do not store private or irrelevant conversation content in backlog entries.
- If a chat cannot be read, record the access limitation rather than inventing
  a signal.

## Automation

- A skill cannot wake itself. Passive monitoring needs a Codex automation,
  project rule, or external schedule.
- Ask the user how often to monitor after publication. Daily is the practical
  default when they want passive monitoring but do not choose a cadence.
- Prefer project-local monitoring for child plugins. Parent reporting is
  optional and should exist only when a parent Fabricator project is known.

## Backlog Shape

Use a simple backlog entry when the project has no stronger format:

```markdown
## Inbox

- [ ] <short finding>
  - Evidence: <date>, <chat or thread>, <brief symptom>
  - Owner: <Fabricator | plugin name>
  - Suggested next action: <Craft | Publish | Watch | docs | investigate>
```

Keep duplicates together. If a finding repeats, add the new evidence under the
existing item instead of creating a near-identical issue.
