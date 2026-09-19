# Codex-only Execution

> M02 contract. This namespace remains non-routable from root policy routing until M04.

## Fixed project coordinator

Codex Main is the fixed Project Workflow execution coordinator for `codex_only`.

Project Workflow defines Card authority, durable state, acceptance, review attempts and continuation boundaries. `codex_workflow` owns concrete worker realization, model/profile/reasoning selection, invocation, waiting, worker lifecycle, resume/replacement and runtime concurrency.

Codex Main alone writes shared Task Board/integration state.

## Serial M02 execution loop

1. Resolve the exact project/workstream state context and canonical Task Board.
2. Recover existing inconsistent/review/Research/RED/in-progress obligations before selecting new work.
3. Select one authority-valid READY Card whose dependencies are complete.
4. Persist start state and semantic `implementation_owner_role` for the production obligation.
5. Run the state/contract Refresh Gate against current repository/runtime evidence.
6. Execute the bounded Card through the runtime. For reviewable production implementation the owning project role is `executor`; concrete worker identity is runtime-owned.
7. Persist exact implementation result/tests/evidence through Codex Main.
8. If review is REQUIRED/RECOMMENDED, freeze a new exact review attempt under `STATE.md`/`REVIEW.md`; do not mark the Card terminal.
9. Obtain the independent Tester through runtime orchestration and let Review run to a durable verdict.
10. GREEN returns here for post-review finalization. RED returns here only after the router classifies bounded owning-Executor correction.
11. Return through the policy router after each durable project obligation; deterministic authorized continuation is not a user/normal-ChatGPT stop.

Fixed-policy execution does not run a capability inventory or switch execution policy because a capability might be needed.

## Production owner

`implementation_owner_role` is project provenance, not runtime identity.

For ordinary reviewable implementation:

```yaml
implementation_owner_role: executor
```

If runtime cannot safely resume the previous concrete Executor, `codex_workflow` may fail closed to a replacement that realizes the same project role. The Task Board does not store that worker/session transition.

Codex Main may perform coordination/integration/bookkeeping without becoming the production owner merely because it writes shared state.

## Review boundary

After implementation of subject S1:

1. Main verifies the exact persisted result and evidence.
2. Main appends R01 `pending` for S1 and points `current_attempt` to R01.
3. Runtime supplies an independent Tester.
4. Main marks R01 `in_progress`.
5. Tester performs the full review and returns verdict/evidence without repairing production.
6. Main persists GREEN/RED.

Under `codex_only`, this formal review does not require returning to the user or a fresh normal-ChatGPT session solely for independence.

## Post-review finalization

When the current REQUIRED/RECOMMENDED attempt is GREEN:

- verify result being finalized is still exactly the GREEN subject;
- verify required acceptance/tests/evidence;
- keep prior attempts/evidence unchanged;
- mark the Card terminal only when all Definition-of-Done conditions are satisfied;
- return to the router before selecting later work.

If production changed after GREEN, the verdict does not cover the changed subject. Freeze a new exact attempt when review still applies.

## RED correction

Execution after RED is legal only when the router selected bounded production correction from that exact RED evidence.

- keep the RED attempt/evidence immutable;
- Main routes the correction to the Card's `implementation_owner_role: executor`;
- Tester/reviewer does not repair production;
- owning Executor produces the correction;
- Main persists corrected result/tests/evidence;
- append a new pending review attempt for the corrected exact subject;
- the next review is a full applicable review;
- do not select unrelated READY work while this non-terminal RED obligation exists.

If the correction requires plan/Definition/Research/user authority, return to the router rather than silently expanding execution authority.

## Recovery-aware result freeze

If a crash occurs after corrected implementation is durable but before Main appends the new attempt, recovery verifies the exact corrected result and appends the missing attempt once. It does not rerun production repair merely to recreate project-state bookkeeping.

If a reviewer runtime disappears during an unchanged attempt, keep the same attempt and let runtime resume/replace the Tester. Runtime replacement alone never freezes a new subject.

## Research

Implementation-triggered evidence gaps use the Task Board `research_obligation` pointer and an exact durable Research record. Research is evidence, not authority.

On return, reconcile only the affected durable obligation. Preserve all review attempt history.

## Definition of Done

A Card may become `done` only when:

1. bounded scope/acceptance are satisfied;
2. required tests/checks are GREEN or an authorized exception exists;
3. relevant OpenSpec is coherent;
4. REQUIRED/RECOMMENDED current review attempt is GREEN;
5. finalized result still equals the GREEN subject;
6. result/evidence/readback is durable;
7. shared Task Board state is reconciled by Main.

## M03 boundary

This M02 loop is serial. M03 introduces bounded compatible Card sets, project lane provenance and workspace isolation while preserving Main-only shared-state writes and the M02 review-attempt lifecycle.
