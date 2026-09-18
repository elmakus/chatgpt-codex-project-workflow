# Normal ChatGPT User Stop Contract

This policy-neutral contract controls **how normal ChatGPT reports a real workflow stop to the user**. It does not decide when a role stops; role/router state decides that first.

Read this module only when the current chat has exhausted all legal deterministic role transitions or has reached a real boundary.

## Response shape

Keep the user-facing response concise and human-oriented.

State:
1. **what happened** — the completed work, finding or blocker;
2. **what it means now** — current durable status/impact;
3. **what happens next** — either the exact smallest user action or that no user action is required.

Do not dump internal execution telemetry by default. Exact SHAs, branch/HEAD details, evidence paths, raw Task Board fields, long test inventories and internal bookkeeping stay in durable state unless the user asks or an exact value is materially needed for action/recovery/debugging.

## User action

When the workflow cannot continue without the user, include:

```text
USER ACTION REQUIRED: <smallest exact action>
```

Do not use this marker when no user action is actually required.

When approved scope is complete and no further action is required, say plainly:

```text
No action required.
```

## Fresh ChatGPT handoff

Whenever a fresh normal ChatGPT chat is required or recommended at the real stop, include a ready-to-copy prompt in the same response.

Generic shape:

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Kontynuuj: <exact concise continuation target>.
Durable start pointer: <implementation/TASK_BOARD.yaml | exact durable pointer>.
Odtwórz aktualny stan i wymagane authority/evidence z repo, a następnie wykonaj tylko legalny następny krok. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

For pending independent review, use:

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Kontynuuj: pending independent review dla <MXX-TYY | exact review target>.
Durable start pointer: implementation/TASK_BOARD.yaml.
Odtwórz exact review_subject, authority slice i evidence z repo, wykonaj niezależny review zgodnie z workflow i zapisz verdict/evidence w durable state. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

The branch is always included because it is a routing locator.

Do not duplicate review subject SHA, test counts/results, evidence prose, changed-file inventories or implementation summaries when durable state already contains them.

## No intermediate status stop

Do not use this contract merely because a role completed.

A role completion followed by a deterministic legal transition goes back through the policy router and continues in the same chat before any final user-facing status response.
