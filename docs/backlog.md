# Backlog

## Inbox

## Bugs

- [x] Handle missing explicit Fabricator skill cache paths more gracefully
  - Evidence: July 15, 2026, thread `019f678f-5de4-7e32-aae7-06af8ccfcd01` (`$fabricator:craft Проаналиируй соседний чат...`), explicit `fabricator:craft` cache path `.../fabricator/0.2.7+codex.20260715192701/...` was missing, so the skill could not be applied directly in a fresh task.
  - Owner: Fabricator
  - Suggested next action: Craft/docs fallback so named Fabricator invocation or missing-path guidance still routes correctly after cache turnover.
  - Released in: Fabricator `0.2.11`.

## Workflow gaps

- [ ] Require project-start understanding gate before Craft implementation
  - Evidence: July 20, 2026, thread `019f7c5a-504c-7333-ac34-c1d6f1757e54` (`Спроектировать плагин для публикаций`): the user explicitly asked for analysis before implementation and one plugin concept, but Craft proceeded to create a project scaffold, multiple files, backlog entries, and a checkpoint commit before approval.
  - Owner: Fabricator
  - Suggested next action: Craft should start every new plugin/project with a required understanding gate: restate the task, desired outcome, scope boundaries, what it will not do yet, assumptions, open questions, risks, and the smallest proposed next step. Phrases such as "сперва анализ", "потом реализация", "сначала расскажи как понял", and "не делай пока" make this a hard stop: wait for explicit implementation approval before editing files, scaffolding, or committing.

## Runtime and release

- [ ] Treat GitHub Release/tag as required public release evidence
  - Evidence: July 19, 2026, screenshot from a plugin publication chat: the repository was pushed and installable, but no GitHub tag/release was created, leaving GitHub showing no published releases even though the plugin was described as public.
  - Owner: Fabricator
  - Suggested next action: Publish should distinguish repository publication from a complete GitHub Release, require tag creation, tag push, GitHub Release notes, and post-release public smoke before saying the release is done.

## Public page

## Watch

- [x] Make Watch automation names and targets unambiguous across parent/plugin projects
  - Evidence: July 15, 2026, thread `019f6751-b22c-7b00-b288-21667922f784` (`Проверить Bookworm на стандарты`), two `Daily Bookworm quality review` automations existed with the same visible title but different targets (`/Users/iamjudin/Desktop/Plugins/Bookworm` and `/Users/iamjudin/Desktop/Brain`), which made the active monitor unclear until one duplicate was removed.
  - Owner: Fabricator
  - Suggested next action: Watch setup should require target-specific naming or a recorded target label when creating child-plugin monitors.
  - Released in: Fabricator `0.2.11`.

- [x] Detect and report stale automation runs
  - Evidence: July 17, 2026, current Fabricator thread: scheduled task UI showed `Bookworm runtime drift monitor` stuck `In progress` since `2026-07-17 11:16:48 MSK`, and an older `Fabricator daily Watch` run stuck `In progress` since `2026-07-16 20:24:13 MSK`, even though a newer Fabricator Watch run completed.
  - Owner: Fabricator
  - Suggested next action: Watch should check previous automation runs for stale `inProgress` state, distinguish stale runs from active work, report the finding, and archive completed monitor threads when possible.
  - Released in: Fabricator `0.2.10`.
