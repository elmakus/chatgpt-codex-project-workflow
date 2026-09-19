# Design — codex_only M03 bounded parallel safety

## Card safety contract

Parallel execution is opt-in. A stable Card may declare:

```yaml
parallel_safe: false
write_scope: []
exclusive_resources: []
```

Absent fields are equivalent to `parallel_safe: false` and remain valid serial behavior.

For `parallel_safe: true`:

- `write_scope` is a non-empty finite list of normalized repository-relative path prefixes covering every repository mutation, including lane-owned evidence;
- absolute paths, parent traversal and globs are invalid for parallel eligibility;
- scopes conflict when equal or when one is an ancestor of the other on a path-segment boundary; `.` claims the whole repository;
- `exclusive_resources` is a finite list of stable semantic tokens; exact token equality conflicts;
- the live selected Task Board, workstream manifest and shared integration bookkeeping are Main-owned reserved state and cannot be delegated through a lane scope.

These fields permit JIT evaluation; they never guarantee concurrency by themselves.

## Deterministic JIT compatible set

Execution Prep evaluates current READY Cards in canonical Task Board order. A Card joins the compatible set only when:

1. all dependencies are complete;
2. `parallel_safe: true`;
3. its write scope is valid and bounded;
4. its write scope is disjoint from every selected member;
5. its exclusive resources do not conflict with every selected member;
6. runtime can provide a separate mutable worktree/equivalent workspace for every concurrent local mutation;
7. all members can start from one exact current Git integration base and return an exact result that Main can reconcile.

Selection is a deterministic greedy pass in Task Board order. Membership and integration order are frozen before launch and never refilled. Fewer than two compatible members means serial execution.

Failure of parallel eligibility does not block an otherwise READY Card; it falls back to serial execution.

## Durable batch model

Serial/no-batch state may use:

```yaml
parallel: null
```

A frozen batch uses:

```yaml
parallel:
  current_batch: B01
  batches:
    - id: B01
      state: prepared
      integration_base: "<exact-git-commit>"
      evidence: null
      members:
        - card_id: M03-T01
          lane: L01
          state: prepared
          result_commit: null
          integrated_commit: null
          evidence: null
```

Batch states are `prepared | running | integrating | complete | blocked`.
Member states are `prepared | in_progress | returned | integrated | blocked`.

Batch IDs and lane IDs are stable project-local labels, not concrete runtime identities. Completed batch entries and reconciled blocked/abandoned entries remain durable history. `current_batch` becomes null after the batch is complete or its blocked outcome is reconciled. Reviewable integrated members may then remain `in_progress` only as one bounded post-batch review drain from the same closed `complete` or terminally reconciled `blocked` batch; that drain resolves before unrelated new implementation. A later batch gets a new ID rather than refilling an old batch.

## Runtime boundary and workspace isolation

Before parallel members become `in_progress`, runtime must establish isolated mutable workspaces. Project Workflow stores no concrete workspace path, worker/session identity or lease.

Each lane receives one Card plus the frozen integration base, must not mutate reserved shared coordination state, and returns an exact result commit plus evidence to Main.

Runtime may replace a concrete worker while the project keeps the same batch/member identity. A member with no durable returned result may be resumed/re-realized; a durable returned result is never replayed because runtime state was lost.

## Main-owned validation and integration

For each returned member, Main verifies:

- an exact base-to-result diff can be derived from the frozen integration base;
- every repository mutation is within the Card write scope;
- reserved shared coordination state was not mutated;
- required Card evidence/tests are present;
- integration into current workstream state remains inside accepted authority.

Scope escape is a fail-closed blocker and is never silently widened.

Main transitions the batch to `integrating` before applying the first returned member, then integrates returned members sequentially in frozen member order. It records the lane result under `result_commit`, the shared-branch result under immutable historical `integrated_commit`, and the integrated commit as the Card implementation result. Reviewable Cards freeze the ordinary M02 exact subject on that integrated result, but the attempt remains `pending` and Tester dispatch is deferred while this exact batch is unresolved. After every member is integrated, Main marks the batch complete/current-null; only then are frozen member reviews dispatched in canonical Task Board order.

If a later review is RED, owning-Executor correction is post-batch. The Card's current result/new review attempt may advance, but the completed batch member's original `result_commit` / `integrated_commit` and original batch-subject attempt remain immutable lineage.

A material integration conflict preserves returned results/evidence and routes Recovery/current authority. Successful lanes are not rerun and integration order is not improvised.

## Post-launch blocked reconciliation

After any member has left `prepared`, the pre-launch abandonment/reset transition is permanently unavailable. A post-launch blocked batch has exactly two recovery shapes:

1. **same-member retry** — allowed only when the affected Card's accepted authority, frozen integration base/order, write scope and exclusive resources remain unchanged. Main preserves the failed result/ref plus blocker evidence, clears the active member result slot while transitioning only the affected member back to `in_progress`, keeps the same batch/lane/base, and re-realizes it from the original base. A corrected return repopulates the active member result pointer only after the prior failed result remains durably recoverable. Integrated/returned siblings are never replayed.
2. **terminal launched-batch reconciliation** — when the correction cannot stay inside the frozen member contract, Main quiesces/reconciles active lanes, preserves all returned/integrated refs, sets every non-integrated member history entry plus corresponding Card to durable `blocked` with exact evidence linkage, records terminal-reconciliation evidence, keeps the batch as immutable blocked history, and only then clears `current_batch`. Integrated reviewable members become the normal post-batch review drain; non-integrated blocked Cards resume later under serial Recovery.

Neither shape widens scope, changes frozen order/base, or discards successful results.

## Recovery

Recovery reconstructs from repository state only:

- batch/member state;
- exact integration base;
- returned result/evidence refs;
- integrated refs;
- Card/review state.

At durable boundaries:

- `prepared`: revalidate base/safety before launch; Main-only batch-control commits after the frozen implementation base are allowed, but any implementation/safety drift invalidates the proof. If stale while every member is still prepared and result-free, persist blocked abandonment evidence, restore batch-owned Card statuses to READY, then clear `current_batch`; never reuse that batch ID. If any member became runtime-active, this pre-launch unwind is forbidden;
- `in_progress` without result: runtime may resume/replace the same project member;
- `returned`: do not rerun; validate/integrate once;
- partial integration: preserve integrated members and continue next frozen member in order; frozen pending reviews for those integrated members remain deferred until batch closure;
- `blocked`: recover exact evidence and classify the smallest correction/fallback;
- `complete`: no batch work remains; Card review/finalization proceeds normally.

## M02 preservation

Parallelism changes dispatch/integration only. M02 immutable review attempts, Tester non-repair, owning-Executor correction, Main-only shared-state writes and runtime-identity prohibition remain authoritative.
