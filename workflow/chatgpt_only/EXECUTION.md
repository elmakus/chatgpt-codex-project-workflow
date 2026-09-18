# ChatGPT-only Execution

Normal ChatGPT is the fixed executor for this route.

Read with:
- `workflow/chatgpt_only/STATE.md`;
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
10. Execute bounded scope.
11. Run required tests/checks and verify acceptance.
12. Perform material external readback/verification when meaningful.
13. Apply Definition of Done.
14. Persist exact result/tests/evidence pointers and mark Card done.
15. If a JIT trigger is now satisfied, run `EXECUTION_PREP.md` immediately when refinement is deterministic.
16. Continue with next READY Card automatically.
17. At review/close/strategic/user/runtime/end-of-scope boundary, route to the owning module.

Do not ask the user to choose among equivalent deterministic next Cards.

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
5. REQUIRED/RECOMMENDED independent review GREEN when review is a Card-completion requirement;
6. no hidden blocker/unassigned TODO inside accepted scope;
7. accepted result exists durably;
8. material external side effects/readback verified;
9. Task Board result state reconciled.

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

Routine GREEN Card is not a user stop.

Deterministic JIT prep is not a user stop.

GREEN milestone is not automatically a user stop; route through `CLOSE.md` and continue when its conditions permit.

Do not end a turn merely to announce work that this route can legally continue.
