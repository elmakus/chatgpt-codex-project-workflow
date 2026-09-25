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

## FUT-005 — System-One / typed decision layer after DAG

Status: `parked`
Target horizon: primarily PWv2.3; PWv2.2 should prepare compatible seams and evaluation data
Origin: user
Dependency: evaluate after / on top of FUT-001 DAG-based execution orchestration

### Intent

Investigate adding a fast, typed, confidence-aware System-One decision layer to Project Workflow after the DAG execution model is established.

The intended role is not to replace Project Workflow authority, deterministic gates, review verdicts or dependency logic. It is an advisory/triage layer for small semantic decisions where a cheap structured evaluator may reduce expensive agent reasoning or improve routing of attention.

### Versioning direction

Preferred sequencing:

`PWv2.2 = DAG first, System-One-aware architecture only`

`PWv2.3 = evaluate and potentially integrate the System-One layer`

Do not couple first-time DAG implementation and first-time probabilistic decision enforcement into the same rollout unless later Research produces strong evidence that the two cannot be separated cleanly.

PWv2.2 SHOULD nevertheless consider the future layer while defining the DAG so that PWv2.3 does not require avoidable architectural rework.

### PWv2.2 preparation to investigate

During DAG Brainstorming / Project Definition, consider whether to provide:

- a provider-neutral `DecisionEvaluator` seam for typed semantic questions;
- optional decision-hook points around DAG node completion, finding classification, JIT/dynamic-node discovery and other clearly bounded advisory decisions;
- separation between deterministic DAG/control-plane authority and probabilistic evaluator output;
- telemetry/evaluation traces sufficient to replay real PW decisions later;
- durable outcome labels where already naturally available, such as review result, Research escalation, JIT promotion/discard, parallel success/conflict or later correction;
- an explicit disabled/no-op mode so the DAG does not depend on a System-One provider in PWv2.2.

These are preparation candidates, not an instruction to ship a System-One model in PWv2.2.

### Candidate uses to evaluate in PWv2.3

Potentially useful decision classes include:

- triage of findings/evidence for materiality or likely owner;
- classification of JIT discoveries before normal PW routing;
- advisory semantic-risk scoring in addition to deterministic parallel-safety checks;
- ranking/selecting context or artifacts for progressive disclosure;
- cheap escalation decisions: answer locally vs escalate to a stronger agent/Research/reviewer;
- other small `Choice`, `Score` or yes/no decisions that can be measured against real outcomes.

Do not assume model routing or conversation compaction are the primary PW use cases. They may be evaluated, but available `pi-jev` evidence does not justify making compaction a core architectural dependency.

### Provider-neutral evaluation

Do not bind PW to Jev or any one open implementation.

At minimum, future evaluation should treat these as first-class candidates:

- Laya;
- Von;
- poorjev.

Hosted Jev may be included as a reference/baseline when available, but the future architecture should remain usable with free/local providers.

Laya is not a fallback-only candidate. Its Jev-compatible typed-decision interface and local/open deployment make it a peer candidate; known weaknesses on high-cardinality classification must be evaluated against actual PW decision shapes rather than assumed to disqualify it.

### Evaluation before enforcement

Before any System-One output influences Project Workflow control flow:

1. build/replay a PW-specific evaluation corpus from real or representative Project Workflow traces;
2. compare candidate providers on the actual PW decision classes;
3. measure at least accuracy, calibration/confidence quality, abstention/escalation behavior, false-negative risk, latency and local resource cost;
4. run the selected evaluator in shadow mode against normal PW decisions;
5. only then decide which advisory decisions, if any, may influence routing.

Do not select a provider based only on generic support-ticket/classification benchmarks.

### Authority boundary

The System-One layer must not become canonical authority for:

- user authorization;
- Project Definition promotion;
- requirement/ADR acceptance;
- GREEN/RED formal review verdicts;
- hard DAG dependency satisfaction;
- destructive-operation authorization;
- canonical shared-state mutation.

Those remain governed by deterministic PW contracts and the existing human/reviewer authority model.


---

## Next-version intake rule

When the next Project Workflow version is started:

1. Read every unresolved candidate in this file before completing initial Brainstorming.
2. Re-evaluate each candidate against the then-current architecture and evidence.
3. Explicitly classify each as `promoted`, `deferred`, or `rejected/superseded`.
4. Promote accepted intent through normal Project Definition.
5. Do not implement directly from this file.
