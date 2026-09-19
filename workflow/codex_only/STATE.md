# Codex-only State Contract

> M03 contract. This namespace remains non-routable from root policy routing until M04.

## Project-state ownership

The canonical Task Board selected by the current project/workstream context is the sole mutable Card/milestone execution-state record. A branch-isolated board is trusted only after manifest identity/branch binding succeeds.

Codex Main is the sole writer of shared Project Workflow Task Board and integration state. Executor/Tester workers return bounded results/evidence to Main; they do not become independent project-state writers.

Runtime worker identity and lifecycle are not Project Workflow state.

## Card and milestone lifecycle

Serial execution remains valid by default.

Normal Card lifecycle is:

```text
planned -> ready -> in_progress -> done
                     \-> blocked
```

`superseded` requires accepted authority. Reviewable Cards remain non-terminal until the current REQUIRED/RECOMMENDED review attempt is GREEN.

Multiple `in_progress` Cards are legal only in one of two bounded states: (1) every such Card is a member of the selected Task Board's exact current parallel batch and that batch satisfies the M03 invariants below; or (2) `current_batch` has just been cleared after one batch reached a closed durable boundary — either `complete` or terminally reconciled `blocked` — and every remaining `in_progress` Card is an integrated member of that same closed batch with an outstanding REQUIRED/RECOMMENDED review, finalization or RED-correction obligation. The second state is a post-batch review drain: it authorizes only those review/finalization/correction transitions, not unrelated new implementation, until those Cards leave `in_progress`.

## Semantic implementation provenance

A reviewable implementation records:

```yaml
implementation_owner_role: executor
```

This is a Project Workflow role slot, not a runtime worker identity.

For a reviewable Card, the field lives on that Card. For a reviewable milestone/checkpoint subject, the milestone records the same field as aggregate production provenance. Runtime may resume/replace concrete realizations without changing semantic owner state.

Do not persist worker/session/model/profile/invocation/lease identifiers or resume protocol in Project Workflow state.

## M03 Card safety metadata

Stable Card authority may define:

```yaml
parallel_safe: true
write_scope:
  - "workflow/codex_only/EXECUTION.md"
exclusive_resources: []
```

Absence of these fields is equivalent to serial-only behavior.

Parallel eligibility requires `parallel_safe: true` plus current JIT proof under `EXECUTION_PREP.md`. The metadata never authorizes concurrent execution by itself.

## Parallel batch state

The Task Board may omit parallel state or use:

```yaml
parallel: null
```

Both mean no active/history ledger has been initialized and serial execution remains valid.

When bounded parallelism is used:

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

Batch states:

```text
prepared -> running -> integrating -> complete
                           \-> blocked
```

Member states:

```text
prepared -> in_progress -> returned -> integrated
                    \-----------------> blocked
```

Recovery-only retry edges exist only for the bounded post-launch rule below: an affected member may move `blocked -> in_progress` after its failed result is preserved and active result slot cleared, and its batch may move `blocked -> running | integrating` according to whether an integrated prefix already exists. These edges do not reopen terminally reconciled blocked history.

### Batch invariants

- `current_batch` is null or identifies exactly one unresolved active batch entry; completed batches and reconciled historical `blocked` batches may remain in history with no current pointer;
- batch IDs are stable and never reused;
- membership, member order, lane labels and `integration_base` are immutable after launch;
- membership is finite/frozen; an existing batch is never dynamically refilled;
- every member names exactly one Card that was READY/dependency-complete when frozen;
- every member Card contract was explicitly `parallel_safe: true` and passed the same current JIT safety proof;
- all member `write_scope` claims are pairwise disjoint and all `exclusive_resources` pairwise non-conflicting;
- the exact `integration_base` is recoverable Git/project state, not a runtime session locator;
- lane labels are project-local semantic provenance only;
- `result_commit` is the returned lane result; `integrated_commit` is the immutable exact shared-workstream result produced by that batch member's original Main integration; a later post-batch review repair may advance the Card's current result but MUST NOT rewrite this historical batch ref;
- terminal/returned result refs require durable evidence sufficient for their state;
- a `blocked` batch/member requires durable evidence for the blocker or reconciled abandonment outcome;
- a pre-launch prepared-batch abandonment is legal only while every member is still `prepared`, no member has a durable result/integrated ref and no member entered runtime-active state; its batch/member history becomes `blocked`, its affected Card statuses are reconciled back to legal READY/serial state, and only then may `current_batch` be cleared;
- once any member left `prepared`, the pre-launch unwind is forbidden; recover the actual running/returned/integrated state instead of resetting Cards;
- a post-launch `blocked` current batch has exactly two bounded recovery shapes: retry only the affected member under the unchanged frozen contract, or terminally reconcile the launched batch into blocked history;
- same-member retry is legal only when the Card authority, `integration_base`, frozen member order, `write_scope` and `exclusive_resources` remain valid and the correction is bounded to that member; Main first preserves the prior failed result/ref and failure evidence durably, then clears the member's active `result_commit` slot as part of `blocked -> in_progress`; the corrected return repopulates it on `returned` under the same batch/lane/base while successful siblings are never rerun;
- terminal post-launch reconciliation may clear `current_batch` only after runtime-active lanes are quiesced/reconciled, every integrated member/ref remains immutable history, every non-integrated member history entry is durably set to `blocked` while preserving any returned result/evidence, and every corresponding Card is moved out of batch-owned `in_progress` into `blocked` with exact blocker/result/evidence linkage; batch evidence must identify this as terminal post-launch reconciliation; reviewable integrated members may remain `in_progress` only as the resulting post-batch review drain;
- live Task Board, workstream manifest and shared integration bookkeeping remain reserved Main-owned state;
- concrete worker/worktree/session identity never appears as required batch state;
- completed batch entries remain durable history; a later batch gets a new stable ID;
- when a reviewable member is integrated, Main freezes the ordinary M02 exact subject immediately, but while that batch remains `current_batch` the attempt stays `pending` and formal Tester dispatch is deferred;
- an integrated member of the current unresolved batch MUST NOT have its review attempt enter `in_progress | red | green`; batch integration/closure owns continuation first.

If a batch cannot meet these invariants, fail closed to Recovery/serial fallback rather than guessing.

## Review block

For Card/milestone review, Task Board owns:

```yaml
review:
  requirement: REQUIRED
  current_attempt: R01
  attempts:
    - id: R01
      state: pending
      subject: "<exact-immutable-subject>"
      reviewer_role: tester
      evidence: null
```

The stable Card/milestone contract remains authority for review requirement. The Task Board records the resolved requirement for recovery.

Attempt invariants remain:

- attempt IDs are stable and never reused;
- one attempt covers one immutable subject;
- `current_attempt` points to an existing attempt when non-null;
- at most one attempt in an owning review block is non-terminal;
- prior attempts are append-only;
- GREEN/RED requires durable evidence;
- `reviewer_role: tester` is semantic project provenance;
- `in_progress` requires runtime proof of reviewer independence from the exact implementation owner;
- changed implementation after RED appends a new attempt;
- reviewer replacement for an unchanged subject does not create a new attempt.

A reviewable parallel Card freezes its review subject only after Main has integrated that Card's returned result and persisted the exact integrated Card result. Parallel lane result identity does not replace the M02 review subject. If the Card belongs to the current unresolved batch, the exact attempt is frozen as `pending` but reviewer dispatch is deferred until that batch is `complete` and `current_batch: null`.

After the batch closes, normal M02 review may produce RED. A later owning-Executor correction is outside the completed batch: it advances the Card's current result and creates a new review attempt, while the completed batch member's original `result_commit` / `integrated_commit` and the original batch-subject review attempt remain immutable lineage.

The manifest-owned workstream final-integration review remains distinct and is reconciled in M04.

## RED -> repair -> recheck

Card RED returns through Main to the Card's `implementation_owner_role`. Milestone RED routes through Execution Prep to exact bounded corrective Card(s). Tester never repairs production.

A corrected reviewable result is a new exact subject/attempt and prior RED/GREEN evidence remains unchanged. Runtime replacement remains transparent project-wise.

## Recovery integrity

Treat as inconsistent and recover before unrelated work:

- invalid/missing review attempt pointers or terminal evidence;
- active reviewable subject lacking semantic implementation owner;
- Task Board GREEN subject/result mismatch;
- runtime-only identity used as required project authority;
- worker acting as competing Task Board writer;
- more than one `in_progress` Card without either one valid current parallel batch covering all of them or one exact post-batch review-drain set from the same closed `complete` or terminally reconciled `blocked` batch, in which every such Card is an integrated member with an outstanding review/finalization/RED-correction obligation;
- clearing/abandoning a prepared batch while any member Card remains `in_progress` solely because that batch froze it;
- using the pre-launch unwind after any member entered runtime-active state or acquired a returned/integrated result;
- clearing a post-launch blocked batch while runtime-active work is unresolved or while any non-integrated member Card remains batch-owned `in_progress` rather than durably reconciled to `blocked`;
- retrying a post-launch blocked member after its frozen authority/base/scope/resource contract changed, or replacing its failed result pointer without preserving the prior failed result/evidence lineage;
- active batch member/order/base mutation after launch;
- duplicate/reused batch IDs or lane labels inside one batch;
- active batch member not matching a Card/current lifecycle state;
- returned/integrated member missing required result/evidence;
- integrated member missing immutable provenance to its original Main-integrated Card result / original batch-subject review attempt; a later post-batch RED repair may legitimately make the current Card result differ from the historical member `integrated_commit` when that append-only review/correction lineage is exact;
- an integrated member of `current_batch` whose review attempt has already entered `in_progress | red | green`; formal review must remain deferred while that batch is unresolved;
- more than one non-complete batch pointed as current.

A corrected implementation or returned lane result already durable before a partial Main write is reconciled exactly once; recovery never reruns work merely to recreate bookkeeping.

## Implementation-owned Research

Task Board `research_obligation` remains the single implementation/recovery Research pointer. Research lifecycle/Origin/Return target lives in the pointed record. Parallel state does not create separate research schedulers.

## M04 boundary

M03 defines bounded compatible Card dispatch/integration only. M04 reconciles full Intake/Brainstorming/Research/Definition/Planning/Micro-fix/Close routing, stacked-workstream integration, final target refresh and root cutover.
