# Codex-only Execution Preparation

> M03 contract. This namespace remains non-routable from root policy routing until M04.

## Ownership

Execution Prep converts approved milestone authority and current predecessor evidence into bounded executable Task Cards and, when current evidence permits, one finite compatible parallel batch for Codex Main.

Codex Main owns all selected Task Board mutations. Runtime worker selection/lifecycle and concrete worktree paths are not Project Workflow state.

## Preparation invariants

- Decompose only work whose contract is currently knowable; use durable JIT triggers instead of speculative placeholder Cards.
- Preserve exact requirements, accepted decisions, milestone outcomes, exclusions and authorization gates in every Card authority slice.
- Fixed `codex_only` execution does not run an executor-selection/capability policy switch.
- Serial execution is always the safe/default shape.
- Planning-level parallel candidates are hints only.
- A stable Card may opt in with `parallel_safe`, `write_scope`, `exclusive_resources`; absence/false opt-in is serial.
- Codex Main remains the sole writer of shared Task Board/integration state.
- Runtime worker/session/model/profile/invocation/resume identity is never Task Card/batch schema.

## Card decomposition

For each currently knowable Card:

1. record stable ID/title/milestone and exact dependencies;
2. record exact authority slice and every implementation-shaping must-preserve constraint;
3. define bounded included/excluded scope, outcome and acceptance;
4. define required tests/evidence/readback and authorization gates;
5. classify REQUIRED/RECOMMENDED/none review;
6. create/reconcile JIT OpenSpec when technical contract risk warrants it;
7. set optional parallel metadata only when its write/resource boundary is knowable now;
8. mark the next executable Card(s) READY only after dependencies/prerequisites are satisfied.

A Card that cannot yet be contracted stays behind a durable JIT trigger rather than becoming a placeholder.

## Current-state parallel eligibility

Parallel evaluation occurs immediately before launch, not during Planning.

### Normalize eligible Card metadata

For every READY Card considered:

- require `parallel_safe: true`;
- require non-empty finite `write_scope`;
- normalize every write claim as a repository-relative path prefix;
- reject absolute paths, parent traversal and wildcard/glob claims for parallel eligibility;
- treat `.` as whole-repository ownership;
- treat scopes as conflicting when equal or when one is an ancestor prefix of another on a path-segment boundary;
- compare `exclusive_resources` by exact stable token equality;
- reject any scope that delegates the live selected Task Board, selected workstream manifest or shared integration bookkeeping to a lane;
- verify every dependency is terminal/accepted.

Metadata invalid for parallelism does not by itself invalidate the Card; execute that Card serially when otherwise READY.

### Build one deterministic compatible set

1. Read READY Cards in canonical Task Board order.
2. Consider only Cards that passed individual eligibility.
3. Start an empty set and greedily append a candidate only when its normalized write scope and exclusive resources are compatible with every already-selected member.
4. Resolve one exact current Git integration base for the whole candidate set.
5. Ask runtime to establish that every concurrent local mutation can use a separate worktree/equivalent isolated mutable workspace. Persist no concrete workspace path/worker identity.
6. Verify each member can return an exact result from that base for Main-owned reconciliation.
7. If fewer than two members remain, do not create a batch; select deterministic serial execution.
8. Otherwise freeze exactly that finite member list and order. Do not refill the batch when other Cards later become READY.

This is bounded ready-set selection, not a generic scheduler.

## Freeze batch state

Append the next stable batch ID and assign stable lane labels in frozen member order:

```yaml
parallel:
  current_batch: B01
  batches:
    - id: B01
      state: prepared
      integration_base: "<exact-git-commit>"
      members:
        - card_id: M01-T01
          lane: L01
          state: prepared
          result_commit: null
          integrated_commit: null
          evidence: null
```

Then:

- set every member Card `execution_status: in_progress`;
- persist semantic `implementation_owner_role: executor` when the Card is reviewable/production-owned;
- keep non-member READY Cards unchanged;
- persist this Main-owned state before runtime launch.

Batch/lane labels are project provenance only; they never identify a concrete worker.

## Refresh immediately before launch

After freezing but before changing a member to runtime-active, re-read only state capable of invalidating safety:

- current branch/HEAD versus frozen integration base;
- member Card authority/contracts;
- dependency terminal state;
- normalized write/resource compatibility;
- reserved shared-state exclusions;
- runtime ability to provide isolated mutable workspaces.

If the base or safety proof became stale before launch:

- do not start the stale batch;
- preserve/dissolve its durable prepared evidence according to Recovery;
- either form a new batch from current truth or fall back serially.

Do not silently mutate membership/base on an already-launched batch.

## RED corrective preparation

Milestone RED from M02 review still routes here to reopen/create exact bounded corrective Card(s). Such correction is serial unless it independently satisfies the same M03 current-state batch gate; do not infer parallel safety merely from disjoint RED findings.

## Research

If execution preparation lacks evidence needed to classify exact Card scope/safety, use the policy-local implementation-owned Research pointer/return protocol. Research does not itself authorize parallelism.

## Review boundary

Execution Prep never performs the Card review. If implementation later produces a REQUIRED/RECOMMENDED reviewable subject, `EXECUTION.md` freezes the exact integrated result under the M02 review model.

## M04 boundary

M04 reconciles the complete lifecycle/intake/micro-fix/Close preparation route before root activation. M03 does not cut over root routing.
