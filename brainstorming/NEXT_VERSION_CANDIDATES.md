# Next Version Candidates

Date: `2026-09-25`
Status: `tentative`
Purpose: durable, non-authoritative parking lot for future Project Workflow ideas that are intentionally outside the scope of the currently active version.

> Nothing in this file is canonical requirement, design, ADR, plan, or implementation authority. Each candidate must pass through the normal Brainstorming → Project Definition → Planning lifecycle before implementation.

## FUT-001 — DAG-based execution orchestration

Status: `parked`
Target horizon: next Project Workflow version after the current version is completed
Origin: user

### Intent

Investigate DAG-based execution/orchestration so independent work can be represented by explicit dependencies and eligible work can proceed when its prerequisites are satisfied.

### Why parked

The current Project Workflow version must be completed first. This candidate must not expand the current version's implementation scope.

### Reconsideration topics

- durable execution graph / DAG state;
- dependency-aware scheduling;
- parallel execution of independent work;
- dynamic graph extension for JIT-discovered work;
- recovery/resume from persisted DAG state;
- integration with Task Cards, workstreams, review gates, Research and human authority;
- whether the graph should be dynamic/hierarchical rather than a single static DAG.

No implementation engine or external provider is selected by this note.

---

## FUT-002 — Domain-language layer for adaptive grilling

Status: `parked`
Target horizon: next Project Workflow version after the current version is completed
Origin: user

### Intent

Extend PW adaptive grilling with selected domain-modeling behavior inspired by upstream `grill-with-docs`, without replacing PW adaptive grilling or its authority model.

### Desired capabilities

- maintain a project `CONTEXT.md` as a pure domain glossary;
- identify vague, overloaded, conflicting, or duplicate terminology;
- establish canonical project terms and discouraged synonyms;
- cross-check stated domain behavior against the codebase;
- use concrete edge-case scenarios to sharpen boundaries between concepts;
- persist resolved terminology so later sessions do not have to rediscover it.

### Authority boundary

During Brainstorming:

- resolved terminology may update `CONTEXT.md`;
- architectural/product decisions remain exploratory choices only;
- Brainstorming must not create canonical ADRs or requirements through this layer.

Canonical promotion remains:

`Brainstorming → Project Definition → requirements/ + decisions/`

Do not replace PW adaptive grilling with upstream `grill-with-docs`. Reuse only the domain-modeling ideas that fit PW authority boundaries.

---

## FUT-003 — Permanent future-candidate parking lot

Status: `parked`
Target horizon: next Project Workflow version after the current version is completed
Origin: user

### Intent

Make a future-candidate parking lot a permanent Project Workflow capability.

The purpose is to distinguish:

- `#feature`: work intended to enter the active managed-change lifecycle now;
- parked candidate: potentially valuable future work intentionally excluded from the current version/scope.

### Required semantics to define in the next version

Adding a parked candidate should not by itself create a workstream, branch, Project Definition, Planning artifact, OpenSpec change, Task Card, or implementation authority.

At the start of a new Project Workflow version / major iteration, unresolved parked candidates must be read back and each explicitly classified as:

- `promoted` — enters normal Brainstorming/Definition for the new version;
- `deferred` — remains parked for a later horizon;
- `rejected` / `superseded` — no longer pursued, with a short reason.

The permanent location and exact schema should be decided during that version's Brainstorming. A likely direction is a dedicated roadmap/future-candidates artifact rather than overloading `#feature`.

---

## FUT-004 — Premium handoff may satisfy the target premium gate

Status: `parked`
Target horizon: next Project Workflow version after the current version is completed
Origin: user

### Intent

Investigate whether an explicit user choice to follow a generated Premium A/C fresh-context handoff should itself be sufficient durable evidence of selecting that handoff, so the receiving context can satisfy the matching premium gate and continue deterministically without asking for a second equivalent confirmation.

### Observed UX problem

Current semantics keep the handoff and gate authorization separate. This can produce a redundant sequence:

`Premium stop → user chooses generated fresh-context handoff → receiving context reconstructs the same due gate → receiving context asks the user to confirm again → continuation`

The extra confirmation is logically consistent with the current contract, but creates avoidable friction after the user has already deliberately chosen the generated handoff.

### Reconsideration topics

- whether launching/using an exact generated premium handoff can be treated as explicit authorization for that exact gate subject;
- how to bind such authorization to the exact premium gate, planning cycle, subject and handoff so stale/copied prompts cannot authorize unrelated work;
- whether the semantics should differ between optional Premium A/C handoffs and mandatory fresh-independent Premium B;
- preserving locator-only handoffs without smuggling workflow policy or mutable session identity into them;
- ensuring REQ-style auto-continuation semantics apply immediately after handoff authorization, with no duplicate user stop;
- regression coverage for stale handoffs, replayed prompts, wrong cycle/subject and intentional user cancellation.

### Why parked

PWv2.1 currently defines premium handoff selection and premium-gate satisfaction as separate actions. This candidate records a future UX/authority-model improvement only and must not alter the current PWv2.1 scope or semantics.

---

## Next-version intake rule

When the next Project Workflow version is started:

1. Read every unresolved candidate in this file before completing initial Brainstorming.
2. Re-evaluate each candidate against the then-current architecture and evidence.
3. Explicitly classify each as `promoted`, `deferred`, or `rejected/superseded`.
4. Promote accepted intent through normal Project Definition.
5. Do not implement directly from this file.
