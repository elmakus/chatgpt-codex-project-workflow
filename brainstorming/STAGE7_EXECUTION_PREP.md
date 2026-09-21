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

## Open material question

Should V2 retain explicit optional Card-level concurrency safety metadata as common project state, or require Stage 8/runtime to derive safety from the ordinary Card scope each time?

Recommendation: retain explicit optional safety metadata. It is project correctness evidence, supports cross-runtime takeover, and does not force concurrency.
