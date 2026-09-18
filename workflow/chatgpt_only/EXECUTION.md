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
5. If Task Board `research_obligation` exists:
   - `Status: active | blocked` → return to the router before selecting later work;
   - `Status: complete` whose exact `Return target` is **not** this Execution obligation → return to the router;
   - `Status: complete` whose exact `Return target` **is** this Execution obligation → do not bounce back to the router; perform **Completed Research return into Execution** below before selecting later work.
6. If the current non-terminal Card has `review_state: red`, this Execution route is legal only when the router selected bounded L1/L2 corrective work from that exact RED evidence. Continue correction of that affected Card/subject; do not select an unrelated READY Card. If that classification has not been established or is contradictory, return to the router/Recovery.
7. If an existing `in_progress` Card has `review_state: green` for its exact persisted implementation subject, perform **Post-review Card finalization** below before selecting new work.
8. Only when no active RED correction exists, select exactly one deterministic READY Card whose dependencies are done.
9. Read its exact milestone/Card authority slice.
10. Persist start transition from `STATE.md`.
11. Run Refresh Gate.
12. Reconcile OpenSpec JIT only when current Card requires it.
13. Execute bounded scope.
14. Run required tests/checks and verify acceptance.
15. Perform material external readback/verification when meaningful.
16. Persist exact implementation result/tests/evidence pointers before any terminal state transition.
17. If the Card requires/recommends independent review and the exact current subject is not already GREEN, keep the Card non-terminal, activate the Review boundary below, persist `review_state: pending`, and stop for a fresh reviewer.
18. Otherwise apply Definition of Done and mark the Card `done`.
19. The current execution-role obligation ends at the durable Card boundary.
20. Persist the terminal Card/result state and return to the router before starting any next Card.
21. The router performs its context-health trigger check, then:
   - selects execution preparation when a JIT trigger is satisfied;
   - selects execution again when another READY Card is legal;
   - selects review/close/strategic/recovery/user-stop handling when that state owns the next obligation.

Do not ask the user to choose among equivalent deterministic next Cards.

## Post-review Card finalization

A Card-level REQUIRED/RECOMMENDED review is a **precondition for terminal `done`**, not a review of an already-terminal Card.

When the router returns an `in_progress` Card with `review_state: green`:

1. recover the exact `review_subject`, review evidence and persisted implementation result;
2. verify that the implementation/result being finalized is still exactly the subject that received GREEN;
3. verify all remaining Definition of Done conditions;
4. if no implementation/behavioral change occurred after the GREEN subject, set `execution_status: done` and persist terminal result state;
5. return to the router before selecting later work.

Do not re-run implementation merely because review completed.

If the implementation/result changed after the GREEN subject, that verdict does not cover the new subject. Keep the Card non-terminal, freeze the changed subject and create the next REQUIRED/RECOMMENDED review attempt before `done`.

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

If evidence exceeds current L1/L2 authority, stop affected work and return to the router for classification: Planning when Project Definition remains valid but milestone/plan strategy must change, Project Definition when accepted requirements/strategic decisions/global target-state authority must change, or Research when more evidence is required first. Do not convert plan-only replanning into a user stop.

## Completed Research return into Execution

When Task Board `research_obligation` points to a record with `Status: complete` and exact `Return target: execution:<subject>` for the current affected durable subject, this Execution route is the **final owning Return target**.

1. Verify Task Board still points to that exact record and that its Origin/Return subjects match the affected Card/review/blocker state.
2. Recover current durable implementation/result/review state before changing anything.
3. If the required correction/reconciliation is already durably persisted, do **not** repeat it. A matching downstream `pending | in_progress | green | red` review state for the corrected exact subject is downstream evidence that the old Research-return correction has already crossed its review boundary; it does not reactivate the old correction.
4. Otherwise perform only the bounded correction/reconciliation authorized by that Return target, then persist exact result/tests/evidence.
5. When REQUIRED/RECOMMENDED review still applies, freeze the corrected exact subject as the next `review_state: pending` boundary before considering the Research return consumed.
6. After the corrective result **and any required new pending review boundary** are durable, set the Research record to `Status: consumed` and clear Task Board `research_obligation`. Prefer one durable repository transition for the pending-review boundary plus Research consume/clear so a crash cannot expose one without the other.
7. If a crash nevertheless leaves the correction or pending review durable while the Research record is still `complete` and pointed, re-entry here is consumption/reconciliation only: prove the durable result, perform only the missing consume/clear transition, and do not redo implementation.
8. Return to the router. If this chat created the new REQUIRED/RECOMMENDED pending subject, the normal fresh-review independence stop applies after the consume/clear transition.

A completed Research return must never produce `ROUTER → EXECUTION → ROUTER` without either performing the owned reconciliation or proving it was already durably performed.

## Implementation → Research handoff

When execution/recovery needs Research before it can classify or continue affected work, persist the continuation **before** yielding the execution role:

1. create one exact research record with `Status: active`, `Origin role: execution_resolution`, an exact durable Card/review/blocker subject as `Origin subject`, and `Return target: execution_resolution:<same exact affected subject>`;
2. set Task Board `research_obligation` to that record; do not use `PROJECT.md → Active research obligation` for implementation-triggered Research;
3. keep the affected Card non-terminal and preserve its exact implementation/review/blocker state; mark it `blocked` when the evidence gap itself prevents further Card progress;
4. return to the router, which routes the active obligation to Research;
5. when Research becomes `complete`, keep the Task Board pointer in place and return through the router to the exact `execution_resolution` target;
6. `execution_resolution` classifies the findings and durably refines the record's Return target to the exact final owning role/subject while keeping `Status: complete` and the Task Board pointer;
7. that final target performs its correction/reconciliation; only after the result is durably persisted does it set Research to `consumed` and clear Task Board `research_obligation`.

The research record owns lifecycle Status, Origin and Return target; Task Board stores only the implementation-owned pointer. If this Execution route is the final Return target of a completed Research obligation, follow **Completed Research return into Execution** above. Keep the pointer until the corrective result and, when required, the new `review_state: pending` boundary are durable; then consume/clear it without replaying already-persisted correction work.

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
- persist exact implementation/result/test/evidence pointers but keep the Card `execution_status` non-terminal (normally `in_progress`);
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
