# ChatGPT-only Execution

Normal ChatGPT is the fixed executor for this route.

Read with:
- `workflow/chatgpt_only/STATE.md`;
- `workflow/chatgpt_only/DELEGATED_WORKERS.md` only when the active Card declares delegated workers;
- Task Board;
- current milestone/Card;
- exact Card authority slice;
- only source/runtime/evidence needed by current scope.

## Deterministic execution loop

1. Establish exact project repository, active branch, HEAD and relevant runtime/external baseline.
2. Read Task Board.
3. Recover existing `in_progress` or `blocked` obligation before selecting new work.
4. If a REQUIRED/RECOMMENDED review is `pending|in_progress`, return to the router so it selects `REVIEW.md` before later dependent implementation.
5. Select exactly one deterministic READY Card whose dependencies are done.
6. Read its exact milestone/Card authority slice.
7. Persist start transition from `STATE.md`.
8. Run Refresh Gate.
9. Reconcile OpenSpec JIT only when current Card requires it.
10. If the Card declares delegated workers, apply `DELEGATED_WORKERS.md` at each concrete worker step: invoke the project-defined profile, await completion, validate the normalized result and keep raw transcript/log detail outside normal main context.
11. Execute the remaining bounded scope owned directly by ChatGPT.
12. Run required tests/checks and verify acceptance.
13. Perform material external readback/verification when meaningful.
14. Apply Definition of Done.
15. Persist exact result/tests/evidence pointers and mark Card done.
16. The current execution-role obligation ends at the durable Card boundary.
17. Persist the completed Card/result state and return to the router before starting any next Card.
18. The router performs its context-health trigger check, then:
   - selects execution preparation when a JIT trigger is satisfied;
   - selects execution again when another READY Card is legal;
   - selects review/close/strategic/recovery/user-stop handling when that state owns the next obligation.

Do not ask the user to choose among equivalent deterministic next Cards.

A delegated worker is not another Task Card executor. ChatGPT remains accountable for the active Card, acceptance, state transitions, review boundaries and user/live authorization gates.

## Refresh Gate

Before implementation compare only state that can affect current Card:
- exact branch/HEAD + relevant runtime/external state;
- Task Board Card/milestone pointers;
- milestone + Card contracts;
- exact requirements/accepted decisions/plan constraints in authority slice;
- required dependency results;
- relevant actual source/interfaces;
- required tests/evidence/readback/review obligations;
- relevant OpenSpec only when referenced/required.

Read prior handoff only when it materially supplies current predecessor truth or recovery.

Refresh Gate is not a tool/capability inventory.

Local implementation-detail drift inside accepted authority may be reconciled.

If evidence requires changing requirements, frozen architecture/decisions, global invariants, milestone outcome/behavior contract or explicit authorization boundary, stop affected execution for strategic resolution.

## Runtime-operation rule

Do not inventory or describe available tools before work.

Attempt each concrete required operation with actual runtime.

Ordinary local remediation is implementation detail when permitted. If a required operation still cannot proceed:
- persist exact blocker;
- mark Card blocked when contract cannot be met;
- request only smallest user input/access/authorization actually required.

Do not stop merely because some capability might be needed later.

Do not treat an isolated local test as proof of a materially different external/production environment.

For a declared delegated-worker step, profile/runtime availability is discovered at the concrete invocation point, not through speculative preflight. If the required worker cannot be invoked/awaited, use the same exact-blocker rule; do not silently perform the delegated task inline.

## Scope / authority

Preserve every implementation-shaping constraint in exact authority slice.

Implement only included scope. Do not smuggle unrelated cleanup or architecture changes into current Card.

Actual source/runtime informs implementation but does not silently rewrite accepted strategic authority.

## OpenSpec

When required, read `workflow/common/OPENSPEC.md`, reconcile actual change JIT, then verify implemented behavior against it.

Do not load OpenSpec merely because project supports it.

## External writes

For material external mutation, use meaningful persisted-state verification when available:

```text
WRITE → READBACK → VERIFY EXPECTED STATE → EVIDENCE
```

Explicit deployment/live-write authorization remains a hard stop.

## Definition of Done

Card may become `done` only when all applicable conditions hold:
1. included scope complete and excluded scope not silently expanded;
2. acceptance satisfied;
3. required tests/checks GREEN or authorized baseline exception exists;
4. applicable OpenSpec consistent;
5. every required delegated-worker step, when present, completed with a valid normalized result or an explicitly accepted exception; worker success alone does not replace Card tests/acceptance;
6. REQUIRED/RECOMMENDED independent review GREEN when review is a Card-completion requirement;
7. no hidden blocker/unassigned TODO inside accepted scope;
8. accepted result exists durably;
9. material external side effects/readback verified;
10. Task Board result state reconciled.

## Review boundary

When this chat implements a subject requiring/recommending independent review:
- freeze exact subject and implementation/test evidence;
- set `review_state: pending`;
- persist durable state;
- commit/push the durable handoff state when possible;
- **stop before issuing verdict**;
- this is a real stop: use root `CHATGPT.md#Real-stop-response-contract`, clearly mark `USER ACTION REQUIRED:`, and include the ready-to-copy branch-aware fresh-review prompt from `REVIEW.md`.

This is a real independence stop.

## Automatic continuation

Routine GREEN Card is not a user stop. It returns to the router, which may immediately select the next execution obligation after the context-health check.

Deterministic JIT prep is not a user stop.

GREEN milestone is not automatically a user stop; route through `CLOSE.md` and continue when its conditions permit.

Do not end a turn merely to announce work that this route can legally continue.
