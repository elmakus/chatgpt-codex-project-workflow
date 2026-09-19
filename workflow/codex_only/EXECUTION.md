# Codex-only Execution

> M03 contract. This namespace remains non-routable from root policy routing until M04.

## Fixed project coordinator

Codex Main is the fixed Project Workflow execution coordinator for `codex_only`.

Project Workflow defines Card authority, durable state, acceptance, review attempts, bounded batch/lane semantics and continuation boundaries. `codex_workflow` owns concrete worker realization, model/profile/reasoning selection, invocation, waiting, worker lifecycle, resume/replacement and runtime concurrency.

Codex Main alone writes shared Task Board/integration state.

## Execution priority

Before selecting new work:

1. recover inconsistent durable state;
2. resolve pending/in-progress Review, except a frozen `pending` review for an integrated member of the current unresolved batch, which remains deferred until that batch closes;
3. resolve implementation-owned Research;
4. resolve RED correction;
5. finalize GREEN reviewed Cards;
6. recover/continue an existing current parallel batch;
7. recover other in-progress/blocked serial work;
8. only then select new READY work or ask Execution Prep to freeze a compatible batch.

Runtime liveness never outranks a durable project verdict/result.

## Serial execution

When no current parallel batch applies, ordinary serial execution remains valid:

1. choose one deterministic READY Card with complete dependencies;
2. persist `in_progress` and semantic `implementation_owner_role` when applicable;
3. run Refresh Gate against exact current authority/source/evidence;
4. execute the bounded Card through runtime;
5. persist exact result/tests/evidence through Main;
6. freeze REQUIRED/RECOMMENDED review for the exact result, or finalize when review does not apply;
7. return to the router after the durable Card boundary.

No capability inventory or policy switching is performed.

## Bounded parallel execution

A current batch is executable only when it was frozen by `EXECUTION_PREP.md` and still satisfies `STATE.md`.

### Launch

For a `prepared` batch:

1. reverify exact current branch state against `integration_base`, allowing only expected Main-owned batch-control bookkeeping committed after that implementation base;
2. reverify dependencies, Card contracts, scope/resource compatibility and reserved shared-state exclusions;
3. require runtime proof that every concurrent local mutation has a separate worktree/equivalent isolated mutable workspace;
4. if any safety fact is stale, return to the explicit pre-launch abandonment transition in `RECOVERY.md#Prepared`; do not partially launch;
5. only while every member remains `prepared`, Main transitions the batch to `running` and member states to `in_progress`;
6. runtime realizes the finite frozen member set concurrently.

Do not persist concrete worker/session/worktree identity. Do not add newly READY Cards to the running batch.

### Worker-lane contract

Each runtime lane receives:

- one exact Card contract/authority slice;
- the frozen `integration_base`;
- the Card's bounded `write_scope`;
- required tests/evidence/readback;
- prohibition on modifying live selected Task Board, workstream manifest or shared integration bookkeeping.

The lane returns to Main:

- exact result commit/ref derivable from the frozen base;
- required Card evidence/tests;
- any bounded failure/blocker.

A worker never writes shared project coordination state directly.

### Persist returned result

When runtime returns a member result, Main verifies that the result/evidence refers to that exact batch/member/base and then writes only project state:

- member `state: returned`;
- exact `result_commit`;
- exact durable evidence pointer.

Returned state does not mean integrated/accepted.

A runtime replacement for an unchanged member does not create a new batch/lane. If `result_commit` is already durable, never rerun the lane merely because runtime state disappeared.

## Main-owned validation and deterministic integration

Returned members are integrated sequentially in the batch's frozen member order. Before the first returned member is applied, Main persists the batch state as `integrating`; recovery may reconcile that bookkeeping transition when Git integration is already durable.

For the next returned member:

1. derive exact `integration_base..result_commit` changes;
2. verify every mutation lies within the Card's normalized `write_scope`;
3. verify no live selected Task Board, workstream manifest or shared integration bookkeeping was mutated by the lane;
4. verify required Card tests/evidence and accepted authority;
5. verify the current shared workstream head contains only already-integrated earlier members/authorized Main bookkeeping relative to the batch base; no post-review production correction can appear here because formal member review is deferred while this batch is unresolved;
6. perform the smallest normal Git reconciliation needed to apply the result in frozen order;
7. verify the integrated state/readback;
8. Main records exact `integrated_commit`, reconciles the Card `result_commit` to that shared-branch implementation result and persists tests/evidence.

Scope escape is fail-closed: preserve the returned result/evidence, mark the affected member/batch blocked, and route Recovery. Do not widen the Card scope silently.

A material textual/semantic integration conflict or other post-launch member failure is also fail-closed. Preserve every returned/integrated result; do not rerun successful members or improvise another integration order.

### Post-launch blocked batch reconciliation

Recovery of a launched batch uses one of two explicit shapes.

**Bounded same-member retry** is legal only when the affected Card can be corrected without changing its accepted authority, frozen `integration_base`, member order, `write_scope` or `exclusive_resources`. Main first preserves the failed result/ref and blocker evidence durably. It then clears that member's active `result_commit` slot while transitioning only that member `blocked -> in_progress`, keeps the same batch/lane/base, and resumes the batch as `running` when no prefix is integrated or `integrating` when an integrated prefix already exists. Runtime re-realizes only that member from the original frozen base. A corrected return repopulates the member's active `result_commit` after the prior failed result is recoverable from evidence, then passes the ordinary validation/integration path in frozen order. Successful siblings are never rerun.

If correction cannot remain inside that frozen member contract, Main performs **terminal post-launch reconciliation** rather than mutating the batch contract. Main quiesces/reconciles every runtime-active member, preserves all returned/integrated refs and blocker evidence, sets every non-integrated member history entry to `blocked` while retaining any returned result/evidence, moves every corresponding Card out of batch-owned `in_progress` into durable `blocked` state with exact batch/member/result/evidence linkage, records terminal-reconciliation evidence on the batch, leaves the batch as immutable `blocked` history, and only then clears `current_batch`. Integrated reviewable Cards may remain `in_progress` as the bounded post-batch review drain; that drain resolves before the now-serial blocked Cards or unrelated work. A preserved non-integrated returned result may later be reused only after serial Recovery revalidates it against current authority/head; otherwise only that affected Card is re-executed.

Neither path may reset launched Cards to READY or use the prepared-batch abandonment transition.

After successful member integration:

- set the member `state: integrated`;
- if that Card has REQUIRED/RECOMMENDED review, freeze the ordinary M02 exact review subject on the integrated Card result as `pending`, but do **not** dispatch a Tester while this batch remains current;
- if review does not apply, keep the Card's exact integrated result durable; terminal Card finalization may occur without changing batch history;
- return through the router, where this exact current batch continues before any deferred member review.

Pending member reviews therefore do not interleave production correction into an unresolved batch. Remaining returned lane results stay durable and are integrated in the frozen order without replay.

When all members are integrated, set batch `state: complete` and `current_batch: null`. Preserve the completed batch entry as recovery history. Only after that durable closure does the router dispatch frozen member reviews, deterministically in canonical Task Board order when more than one is pending.

## Production owner and review boundary

`implementation_owner_role: executor` remains semantic project provenance, not a lane/worker identity.

Parallel execution does not weaken M02 review rules:

1. review is frozen only after the exact Main-integrated Card result is durable;
2. one immutable integrated subject belongs to one review attempt;
3. while that Card belongs to `current_batch`, the frozen attempt remains `pending` and Tester dispatch is deferred until the batch is complete/current-null;
4. Tester is independent from the implementation owner for that subject and does not repair production;
5. RED returns through Main to the owning Executor role only after batch closure;
6. corrected implementation is a new review subject/attempt;
7. prior attempt evidence and historical batch `result_commit` / `integrated_commit` remain immutable.

A later unrelated integration commit does not rewrite an already-frozen historical Card result/subject. A later post-batch RED repair may advance the Card's current result, but it does not rewrite the completed batch member's original integration provenance.

## Post-review finalization

When the current REQUIRED/RECOMMENDED attempt is GREEN:

- verify the Card result pointer still identifies the exact GREEN subject;
- verify acceptance/tests/evidence;
- keep prior attempts/evidence unchanged;
- mark the Card `done`;
- return to the router.

Under the M03 batch rule, formal review is never already in progress for a member of an unresolved current batch. If recovery finds that state, route Recovery before finalization.

## RED correction

RED outranks continuing unrelated batch work.

- preserve RED attempt/evidence;
- Card-owned bounded correction returns through Main to that Card's `implementation_owner_role: executor`;
- milestone RED routes through Execution Prep to exact bounded corrective Cards;
- Tester does not repair production;
- corrected Card result is persisted by Main and receives a new review attempt;
- for a Card that originated in a completed batch, correction is serial/post-batch and MUST NOT overwrite the historical member `result_commit` or `integrated_commit`; the prior batch-subject attempt preserves the lineage;
- already-returned/integrated sibling batch results remain durable and are not replayed.

A correction is not automatically parallel-safe merely because the original Card was a batch member. Re-evaluate any new concurrency at JIT.

## Recovery-aware execution

For current batch recovery use `RECOVERY.md`. In particular:

- `prepared`: revalidate before launch;
- `in_progress` without durable result: runtime may resume/replace realization;
- `returned`: validate/integrate once, never rerun;
- partial integration: continue the next frozen member in order;
- `blocked`: classify exact evidence;
- `complete`: no batch execution remains.

## Research

Implementation-triggered evidence gaps use one Task Board `research_obligation` and exact Research record. Research evidence never becomes a second scheduler or lane state store.

## Definition of Done

A Card may become `done` only when:

1. bounded scope/acceptance are satisfied;
2. required tests/checks are GREEN or an authorized exception exists;
3. relevant OpenSpec is coherent;
4. if executed through a batch, its returned diff passed scope/reserved-state validation and exact integrated result is durable;
5. REQUIRED/RECOMMENDED current review attempt is GREEN when applicable;
6. finalized Card result still equals the reviewed subject when review applies;
7. result/evidence/readback is durable;
8. shared Task Board state is reconciled by Main.

## M04 boundary

M03 supplies bounded Card execution/integration mechanics only. M04 reconciles complete lifecycle routing, final workstream integration/Close and root cutover.
