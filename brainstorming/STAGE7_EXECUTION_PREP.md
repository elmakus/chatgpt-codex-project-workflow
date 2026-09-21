# Stage 7 Brainstorming — Execution Prep / JIT

Date: 2026-09-21
Scope: common-preexecution-core@R1
Status: active analysis
Production authority: none
Baseline: current main fixed-policy contracts

## Purpose

Analyze Execution Prep / JIT independently before Stage 8 Execution.

The goal is to separate:
- Project Workflow preparation semantics;
- project-level execution-safety constraints;
- runtime scheduling/delegation/concurrency mechanics.

## Current V1 comparison

### Shared semantic core

Both fixed policies intend Execution Prep to turn accepted authority and current predecessor evidence into bounded executable work.

Common semantics include:

- exact selected branch-isolated workstream;
- manifest-bound Task Board as mutable implementation state;
- Task Cards only when their contracts are currently knowable;
- durable JIT triggers instead of speculative placeholder Cards;
- exact authority slice;
- dependencies;
- included/excluded scope;
- acceptance;
- required tests/evidence/readback;
- external-write and authorization gates;
- independent-review requirement;
- OpenSpec classification where technical contract risk warrants it;
- incremental refinement only inside accepted authority;
- Research handoff/return when evidence is insufficient;
- qualified micro-fix materialization without inventing a Master Plan/milestone;
- automatic continuation into Execution when executable work exists and no real gate intervenes.

### ChatGPT-only V1 mechanics

ChatGPT-only additionally encodes serial-policy assumptions:

- exactly one next eligible Card becomes READY;
- bounded-parallel coordination fields are explicitly forbidden;
- concurrency is not representable in its active Task Board schema.

These are not different preparation semantics. They are consequences of the current runtime policy.

### Codex-only V1 mechanics

Codex-only adds a concrete parallel scheduler into Execution Prep:

- optional `parallel_safe`, `write_scope`, `exclusive_resources`;
- READY-set compatibility selection;
- batch ID;
- lane labels;
- frozen member list/order;
- integration base;
- runtime workspace-isolation capability check;
- batch members changed to `in_progress` before runtime launch;
- pre-launch stale-batch abandonment/recovery protocol.

The safety properties are relevant to Project Workflow, but the concrete batch/lane scheduling is runtime realization and should not make Execution Prep product-specific.

## Stage boundary with Execution

Target boundary:

```text
Execution Prep
-> contract work
-> prove Card readiness
-> persist READY set + project safety constraints
-> return to router

Execution
-> select actual execution set according to current capability
-> validate/freeze neutral active_execution
-> launch/perform work
```

Therefore Stage 7 should NOT:
- choose a concrete worker/subagent;
- create runtime lane identities;
- create product-specific batch IDs;
- query runtime merely to decide whether Cards are semantically READY;
- persist workspace paths;
- mark Cards active merely because a parallel-capable runtime exists;
- own launch-time stale-batch unwind.

Those belong to Stage 8 Execution / Recovery.

## READY semantics

Candidate common definition:

> READY means the Card is legally executable now from accepted project authority, dependency results, prerequisites, known scope/acceptance and authorization gates.

READY does NOT mean:
- the current runtime has chosen to execute it next;
- a worker has been assigned;
- enough concurrent worker slots exist;
- a worktree has been allocated.

Therefore more than one independent Card may be READY at the same time even when the current runtime can execute only one serially.

This matches the earlier Execution Prep parity evidence: runtime concurrency does not affect readiness.

## Card construction / JIT

Common Stage 7 should:

1. resolve exact accepted milestone/micro-fix authority;
2. initialize/reconcile the selected workstream Task Board when implementation state is first needed;
3. create only currently knowable Cards;
4. preserve exact authority refs and must-preserve constraints;
5. define bounded included/excluded scope;
6. define dependencies;
7. define acceptance and required verification;
8. record external-write/readback and authorization requirements;
9. classify independent review;
10. record JIT trigger instead of creating an unknowable future Card;
11. mark every currently legal Card READY according to semantic readiness, not runtime capacity.

Incremental JIT refinement may split/merge/reorder/refine only not-yet-started work inside accepted authority.

Stage 7 must not rewrite:
- a Card already in an active execution obligation;
- an immutable review subject;
- historical result/review evidence.

If new evidence requires changing accepted product/system intent, route to Definition.
If Definition remains valid but strategy/milestone organization changes, route to Planning.
If evidence is missing, route to Research.

## Research return

The ChatGPT V1 contract contains the fuller explicit crash-safe Research return protocol, while Codex relies on the same policy-local Research lifecycle more compactly.

This is common semantic behavior and should survive V2:

- implementation/preparation Research pointer belongs to selected Task Board;
- completed Research remains pointed until the owning return reconciliation is durably applied;
- target mutation + `Return reconciliation: applied` + exact result refs are one durable transition;
- after that, consume/clear;
- crash after apply but before consume/clear performs consume/clear only, not Card reconstruction again.

## Micro-fix

Micro-fix semantics are effectively common.

Stage 7 may materialize:
- one bounded Card;
- `plan_revision/current_milestone: micro-fix`;
- no synthetic Master Plan/milestone entry;
- normal Card scope/acceptance/tests/review/evidence;
- workstream final-integration review requirement.

After materialization, ordinary common Execution/Review/Close semantics apply.

## Project-level concurrency safety

The important remaining Stage-7 design choice is not whether a runtime may parallelize; that is runtime capability.

The question is whether stable Card contracts should carry explicit project-level concurrency safety claims.

Evidence favors keeping an optional runtime-neutral safety contract because:
- Project Workflow owns dependencies and mutation/resource safety;
- another runtime must be able to decide legal concurrency from durable project state without previous-chat inference;
- write/resource conflicts are correctness properties, not worker-scheduling preferences;
- serial execution remains legal when the metadata is absent or concurrency cannot be realized.

Candidate semantic fields remain equivalent to:

```yaml
concurrency:
  safe: true
  write_scope:
    - <finite repository-relative mutation prefix>
  exclusive_resources:
    - <stable project-level resource token>
```

Exact field names are not yet important.

Rules:
- absent / false / incomplete proof => serial-only;
- planning may identify potential independent work, but Stage 7 is where current exact safety metadata is bound;
- metadata never names worker/model/session/worktree;
- runtime cannot widen these claims;
- actual simultaneous set selection happens in Stage 8.

## Pre-launch refresh

Codex V1 currently places `Refresh immediately before launch` inside Execution Prep.

For V2 this should move to Stage 8 because it is a property of the actual chosen execution set and exact launch boundary.

Stage 7 still works from current authoritative durable state, but it does not own the final launch-time revalidation.

## Proposed Stage 7 V2 output

A successful Execution Prep transition leaves:

- exact selected workstream / common Task Board;
- currently knowable stable Task Card contracts;
- JIT triggers for unknowable later work;
- semantic READY Cards;
- dependency and acceptance data;
- optional explicit concurrency-safety claims;
- exact review requirements;
- no runtime assignment;
- no concrete batch/lane/workspace identity;
- no `active_execution` yet.

Then it returns to the common router.

Stage 8 may choose one or more READY Cards and create the neutral durable `active_execution` obligation before actual execution.

## Resolved grilling decisions — concurrency safety

User accepted recommendations 1–5:

1. Stage 7 persists runtime-neutral concurrency-safety metadata; Stage 8 revalidates freshness/compatibility before actual concurrent execution rather than deriving safety from scratch.
2. If a Card lacks complete concurrency-safety proof, it remains serial-valid but is not eligible for concurrent execution. Runtime may not infer missing proof ad hoc.
3. Concurrency-safety claims belong in the stable Task Card contract, not mutable Task Board scheduling state.
4. Safety covers both repository mutation scope and shared/external resources through stable project-level claims/tokens.
5. Stage 7 marks every semantically executable Card READY. READY means executable-now, not selected-by-scheduler.

Resulting Stage-7 invariant:

> Execution Prep determines what work is legal and what concurrent combinations are project-safe in principle; Execution decides what subset to run now and how to realize it.

These choices are exploratory Brainstorming conclusions, not yet accepted Definition authority.

## Remaining Stage-7 questions

The remaining questions concern JIT mutation boundaries, authorization-sensitive readiness, and whether any preparation state besides stable Cards/JIT triggers is required before Stage 8.


## Grilling correction — preserve proven V1 behavior

The user clarified that V2 is primarily a merge of two already-working fixed-policy branches, especially preserving the behavior that works well in `chatgpt_only`. The goal is not to redesign every lifecycle into a larger generic framework.

This adds a conservative-merger rule for Stage 7:

> Prefer the smallest common contract that preserves proven ChatGPT-only behavior and adds only the runtime-neutral capability needed to absorb Codex-only behavior.

### Future work whose exact Card is not knowable yet

Current `chatgpt_only` already distinguishes:

- **planned work package / durable JIT trigger** — we know future work will be needed, but its exact executable Card depends materially on predecessor evidence;
- **real Task Card** — scope is bounded enough to contract now.

Therefore V2 should preserve this behavior:

- if future work is known conceptually but its exact scope depends materially on predecessor results, keep the planned work package/JIT trigger;
- after the predecessor result is durable, Execution Prep materializes or substantially reshapes the real Card from that evidence;
- do not create a vague executable placeholder merely to reserve an ID;
- if the Card is already sufficiently knowable now but merely waits for a dependency, it may exist before the dependency completes and becomes READY later.

So the trigger preserves **that something remains to be done**, while the later JIT pass owns the exact Card shape.

### READY and deployment/live writes

The user does not want a default human-approval gate merely because work performs deployment or a live write.

Target rule:

- deployment/live-write nature by itself does **not** make a Card non-READY;
- a Card is blocked from READY only when accepted project authority explicitly requires an approval/authorization that has not yet been satisfied, or when concrete required access/input is missing;
- Project Workflow must not invent an extra user-confirmation gate solely from operation category;
- external readback/verification requirements still remain part of the Card contract.

This preserves authorization semantics where explicitly required without adding unnecessary user stops.

### Grilling decisions currently settled

- concurrency safety metadata: explicit optional runtime-neutral Card-contract metadata;
- incomplete concurrency proof: serial-only, not invalid;
- safety metadata belongs to stable Card contract;
- safety covers repository mutation + shared/external resources;
- all semantically executable Cards may be READY at once;
- future-but-not-yet-contractable work is represented by planned work package/JIT trigger, not vague placeholder Card;
- READY is not blocked merely because work is deployment/live-write;
- missing facts route to Research;
- micro-fix reuses the same Execution Prep semantics in a smaller shape.


## Grilling decision — front-load knowable decomposition

User clarified the intended operating model:

- Strategic Planning is expected to be authored by a stronger planning model/runtime.
- Later orchestration/JIT continuation may use a different, lighter coordinating model/runtime.
- The workflow should therefore preserve as much useful planning/decomposition work as can be known reliably up front, rather than intentionally deferring easy-to-specify work to later JIT.

Stage-7 direction:

1. Planning should express the full milestone/workstream structure and planned work packages as far as they are meaningfully knowable.
2. Execution Prep should materialize **all currently well-defined useful Task Cards**, not only the immediately next Card.
3. A Card that is already bounded enough to specify may exist in `planned` even if its dependencies are not yet complete.
4. When those dependencies become satisfied, the Card may become `ready` without requiring re-planning.
5. Only work whose exact executable scope genuinely depends on predecessor evidence remains as a durable planned-work/JIT trigger instead of a speculative Card.
6. Later orchestration may split/merge/reorder/refine only not-yet-started Cards inside accepted authority when new evidence makes that useful.
7. The objective is to front-load high-quality reasoning without freezing details that are genuinely unknowable.

This preserves the existing ChatGPT-only planned-work/JIT model while making explicit that JIT is a precision mechanism, not a reason to defer work that the planner can already specify well.


## Grilling decisions — state boundary before Execution

User accepted:

- no extra Card lifecycle state between `ready` and `in_progress` merely for preparation; do not add `prepared` to ordinary Card status;
- Stage 8 must refresh/revalidate current repository/dependency truth immediately before actual execution selection/start;
- if that refresh materially invalidates Card scope/readiness/safety, route back to JIT/Recovery rather than launching stale work;
- if nothing material changed, execution proceeds without ceremony.

This keeps the ordinary Card lifecycle small:

`planned -> ready -> in_progress -> done/blocked`

with review-related non-terminal behavior handled by the review contract rather than another preparation status.
