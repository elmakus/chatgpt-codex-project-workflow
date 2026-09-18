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

## Explicit phase-promotion gate

When the selected policy route defines a user-owned phase promotion boundary, this contract only formats that stop; the policy route remains authoritative for when it applies.

For a Brainstorming → Project Definition promotion stop, keep it minimal:

```text
USER ACTION REQUIRED: choose one: continue brainstorming/research, or explicitly promote the current scope into Project Definition.
```

Do not imply that Definition or Planning has already started. Do not require a fresh chat solely for this gate.

## Fresh ChatGPT handoff

Whenever a fresh normal ChatGPT chat is required or recommended at the real stop, include a ready-to-copy prompt in the same response.

### Locator-only invariant

The fresh-session prompt is a **routing locator, not a task contract or session-scope boundary**.

Use the bounded forms below. Do not improvise a larger handoff by copying:
- review/audit checklists;
- prior findings or remediation proposals;
- acceptance/test inventories;
- implementation summaries;
- changed-file/diff inventories;
- SHAs already recoverable from durable state;
- GREEN/RED outcome branches or downstream workflow logic;
- previous-chat narrative.

The only allowed addition is the smallest non-durable user intent that cannot be recovered from repository authority.

If a nonstandard review/audit scope is materially required and cannot be reconstructed from existing durable authority, **persist that scope first** in the owning Task Card, review record, audit-scope artifact or other appropriate project file. When the selected route already has a canonical state pointer (for example Task Board), keep that canonical pointer and make its owning contract/state reference the durable scope artifact. Otherwise the handoff may point directly to the durable scope artifact. Never serialize the scope into the chat prompt.

The named entry target identifies only the first obligation to recover. After that role completes, the new chat returns to the selected policy router and continues deterministic authorized transitions until a real workflow stop.

### Generic shape

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Punkt wejścia: <exact concise continuation target>.
Durable start pointer: <implementation/TASK_BOARD.yaml | exact durable pointer>.
Odtwórz aktualny stan i wymagane authority/evidence z repo. Ten punkt wejścia jest tylko locator-em, nie granicą zakresu sesji. Po zakończeniu wskazanej roli wróć do policy routera i kontynuuj legalne deterministyczne przejścia aż do real workflow stop. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

The variants below format the handoff only. Canonical review-state ownership is defined by the selected policy route; this response contract does not create a second state source.

For pending implementation independent review, use the exact selected Task Board as the durable pointer. In legacy/default mode this is `implementation/TASK_BOARD.yaml`; in a branch-isolated workstream it is the exact manifest-selected workstream Task Board.

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Punkt wejścia: pending independent review dla <MXX-TYY | exact review target>.
Durable start pointer: <implementation/TASK_BOARD.yaml | implementation/workstreams/<id>/TASK_BOARD.yaml>.
Odtwórz exact review_subject, authority slice i evidence z repo, wykonaj niezależny review zgodnie z workflow i zapisz verdict/evidence w durable state. Wskazany review jest tylko pierwszą rolą tej sesji: po jej zakończeniu wróć do policy routera i kontynuuj aż do real workflow stop. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

For a pending branch-isolated **workstream final-integration review**, use the exact selected workstream manifest as the durable pointer because that manifest owns this distinct review lifecycle:

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact workstream branch>.
Punkt wejścia: pending independent final-integration review dla <workstream-id>.
Durable start pointer: implementation/workstreams/<id>/WORKSTREAM.yaml.
Odtwórz exact manifest review subject, workstream authority/acceptance surface i wymagane evidence z repo, wykonaj niezależny review zgodnie z workflow i zapisz verdict/evidence w manifest-owned review state. Wskazany review jest tylko pierwszą rolą tej sesji: po jej zakończeniu wróć do policy routera i kontynuuj aż do real workflow stop. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

For pending independent plan review, use:

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/planning branch>.
Punkt wejścia: pending independent plan review dla <plan revision>.
Durable start pointer: planning/reviews/<plan-revision>.md.
Odtwórz exact Review subject, approved Definition, canonical requirements/decisions i wymagane evidence z repo, wykonaj niezależny plan review zgodnie z workflow i zapisz verdict/evidence w tym review record. Wskazany review jest tylko pierwszą rolą tej sesji: po jej zakończeniu wróć do policy routera i kontynuuj aż do real workflow stop. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

The branch is always included because it is a routing locator.

## Context-hygiene fresh-chat handoff

When a policy-specific Context Health Gate returns `FRESH`, the current work is not blocked or failed. The current obligation is already complete and durable; the user only needs to start a clean chat for the next obligation.

Use:

```text
USER ACTION REQUIRED: start a fresh normal ChatGPT chat for context hygiene and paste the prompt below.
```

Then include:

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Punkt wejścia: <exact next legal obligation>.
Durable start pointer: <implementation/TASK_BOARD.yaml | exact durable pointer>.
Odtwórz aktualny stan i wymagane authority/evidence z repo. Ten punkt wejścia jest tylko locator-em, nie granicą zakresu sesji. Po zakończeniu wskazanej roli wróć do policy routera i kontynuuj legalne deterministyczne przejścia aż do real workflow stop. Ten handoff służy wyłącznie odświeżeniu kontekstu; nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

Keep the explanation short: the completed work is safely persisted and a clean context is preferable before the next obligation.

Do not mention guessed token counts, context-window percentages or internal budget estimates.

## No intermediate status stop

Do not use this contract merely because a role completed, because the role named by a fresh-session prompt completed, or because a GREEN/RED verdict was persisted.

A role completion followed by a deterministic legal transition goes back through the policy router and continues in the same chat before any final user-facing status response.
