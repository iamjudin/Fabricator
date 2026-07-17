# Backlog

## Inbox

## Bugs

- [ ] Handle missing explicit Fabricator skill cache paths more gracefully
  - Evidence: July 15, 2026, thread `019f678f-5de4-7e32-aae7-06af8ccfcd01` (`$fabricator:craft Проаналиируй соседний чат...`), explicit `fabricator:craft` cache path `.../fabricator/0.2.7+codex.20260715192701/...` was missing, so the skill could not be applied directly in a fresh task.
  - Owner: Fabricator
  - Suggested next action: Craft/docs fallback so named Fabricator invocation or missing-path guidance still routes correctly after cache turnover.

## Workflow gaps

## Runtime and release

## Public page

## Watch

- [ ] Make Watch automation names and targets unambiguous across parent/plugin projects
  - Evidence: July 15, 2026, thread `019f6751-b22c-7b00-b288-21667922f784` (`Проверить Bookworm на стандарты`), two `Daily Bookworm quality review` automations existed with the same visible title but different targets (`/Users/iamjudin/Desktop/Plugins/Bookworm` and `/Users/iamjudin/Desktop/Brain`), which made the active monitor unclear until one duplicate was removed.
  - Owner: Fabricator
  - Suggested next action: Watch setup should require target-specific naming or a recorded target label when creating child-plugin monitors.

- [x] Detect and report stale automation runs
  - Evidence: July 17, 2026, current Fabricator thread: scheduled task UI showed `Bookworm runtime drift monitor` stuck `In progress` since `2026-07-17 11:16:48 MSK`, and an older `Fabricator daily Watch` run stuck `In progress` since `2026-07-16 20:24:13 MSK`, even though a newer Fabricator Watch run completed.
  - Owner: Fabricator
  - Suggested next action: Watch should check previous automation runs for stale `inProgress` state, distinguish stale runs from active work, report the finding, and archive completed monitor threads when possible.
  - Released in: Fabricator `0.2.10`.
