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

### Storage-isolation problem to research

The permanent location is itself a design question and MUST be researched before promotion.

A parked future idea should not cause unrelated active work to observe its integration base or consumer branch moving merely because the parking record was updated. Even an unrelated documentation-only commit on a shared branch can force an active agent to fetch, compare, reconcile/rebase unpublished work, re-check freshness and prove that the remote movement does not affect its current obligation.

Therefore the future mechanism should aim to avoid:

- mutating `main` merely to record a future idea;
- mutating an active product/workstream branch merely to record out-of-scope future intent;
- creating false base/fingerprint drift for unrelated active agents;
- forcing unrelated workers to spend tool calls/context/tokens proving a parking-only change is harmless;
- turning the parking store into workflow authority or another mutable project-state source.

Research should compare at least:

- a dedicated metadata/future-candidates branch that active workstreams never use as their execution/integration base;
- GitHub Issue/Discussion or equivalent repository-side metadata;
- a separate repository or other project-level metadata store;
- any version-agnostic repository artifact that can be updated without perturbing active execution branches.

Selection criteria should include:

- durability and recoverability;
- discoverability at next-version intake;
- concurrent-write behavior;
- isolation from `main` and active workstream movement;
- low reconciliation/token overhead for unrelated agents;
- portability across ChatGPT/Pi/Paseo;
- simple promotion/defer/reject lifecycle;
- clear non-authoritative semantics.

Do not pre-select the final storage mechanism from this bootstrap file. The current `NEXT_VERSION_CANDIDATES.md` is only a temporary ledger.

### Research requirement before promotion

Research the storage/location question as its own bounded Research task before Definition, using real concurrent-workflow behavior as evidence. The outcome should explicitly decide where parked candidates live, how they are updated without disturbing active work, and how a new version discovers them deterministically.

The permanent location and exact schema should then be decided during that version's Brainstorming rather than overloading `#feature`.

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

`PWv2.3 = System-One integration, initially with Jev as primary provider`

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

### Initial provider strategy for PWv2.3

Preferred starting strategy:

- use hosted Jev as the initial primary/production evaluator;
- run Laya, Von and poorjev locally on Unraid in parallel shadow/benchmark mode;
- feed the same eligible PW decision traces to Jev and the local candidates;
- do not let shadow providers influence control flow while benchmarking;
- keep the Project Workflow integration provider-neutral so switching away from Jev does not require redesign.

The initial default should be to keep Jev while its quality, latency, availability and cumulative cost remain acceptable.

If Jev cost, availability, privacy or another operational constraint becomes material, use the accumulated PW-specific benchmark data to select the best local replacement rather than starting a new evaluation from scratch.

### Local benchmark deployment direction

The free candidates are expected to run locally.

Initial deployment target:

- Unraid CPU-only is acceptable for first benchmarking;
- Laya, Von and poorjev may run as separate local services/containers;
- GPU acceleration is optional, not a requirement for starting the benchmark;
- an existing NVIDIA GTX 1080 Ti may be evaluated later if CPU latency becomes a practical constraint, subject to compatibility with the then-current CUDA/PyTorch/runtime stack;
- do not make PW depend on the presence of that GPU.

### Candidate uses to evaluate in PWv2.3

Potentially useful decision classes include:

- triage of findings/evidence for materiality or likely owner;
- classification of JIT discoveries before normal PW routing;
- advisory semantic-risk scoring in addition to deterministic parallel-safety checks;
- ranking/selecting context or artifacts for progressive disclosure;
- cheap escalation decisions: answer locally vs escalate to a stronger agent/Research/reviewer;
- other small `Choice`, `Score` or yes/no decisions that can be measured against real outcomes.

Do not assume model routing or conversation compaction are the primary PW use cases. They may be evaluated, but available `pi-jev` evidence does not justify making compaction a core architectural dependency.

### Benchmark requirements

For each eligible PW decision, capture enough data to compare:

- actual/accepted PW outcome or later ground truth;
- provider answer;
- probabilities/confidence;
- abstention/escalation behavior where supported;
- latency;
- local CPU/GPU resource cost where applicable;
- Jev input-token usage and cumulative monetary cost;
- disagreement between providers.

At minimum, future evaluation should include:

- Jev as the primary/reference provider;
- Laya;
- Von;
- poorjev.

Laya, Von and poorjev are peer local candidates. Do not pre-select a local winner based only on generic public benchmarks.

### Evaluation before broader enforcement

Before expanding System-One influence beyond narrowly accepted advisory hooks:

1. build/replay a PW-specific evaluation corpus from real or representative Project Workflow traces;
2. compare providers on the actual PW decision classes;
3. measure at least accuracy, calibration/confidence quality, abstention/escalation behavior, false-negative risk, latency, resource cost and Jev monetary cost;
4. keep local alternatives in shadow mode long enough to obtain meaningful evidence;
5. only then decide whether Jev remains primary or whether a local provider should replace it.

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

## FUT-006 — Agent-facing `pw doctor` / `pw explain`

Status: `parked`
Target horizon: PWv2.2 candidate
Origin: user

### Intent

Investigate a read-only diagnostic/explanation interface that lets an agent mechanically inspect current Project Workflow state instead of repeatedly reconstructing it from several durable artifacts.

Potential outputs include:

- selected workstream and current obligation;
- exact reason/rule for the route;
- blockers and stale pointers/fingerprints;
- DAG ready/blocked frontier;
- due review/Research/user gates;
- bounded explanation for why a specific node is blocked or selected.

Primary consumer is the agent/runtime; human-readable output is a useful secondary UX.

### Research requirement before promotion

Research this candidate independently before Definition. Determine overlap with the existing router/state-contract tooling, expected context/token savings, failure modes, stable explanation schema, and whether a single `doctor` surface plus machine-readable output is preferable to multiple commands.

---

## FUT-007 — Atomic canonical transition applier

Status: `parked`
Target horizon: PWv2.2 candidate
Origin: user

### Intent

Investigate applying logically related canonical Project Workflow state changes as one validated transition rather than a sequence of partially durable mutations.

Candidate shape:

`expected current state/hashes → proposed transition → validate complete resulting state → one durable Git commit → readback/verification`

The mechanism should fail closed if preconditions changed or the resulting state violates invariants.

### Research requirement before promotion

Research this candidate independently before Definition. Evaluate transaction boundaries, optimistic concurrency/fingerprint strategy, Git commit semantics, rollback/failure behavior, interaction with parallel DAG completion, and which transitions are safe to automate without creating a second state authority.

---

## FUT-008 — DAG crash/recovery simulation and property testing

Status: `parked`
Target horizon: PWv2.2 candidate
Origin: user
Dependency: FUT-001 DAG-based execution orchestration

### Intent

Investigate a dedicated test harness that generates or replays DAG workflow states and deliberately injects interruption/crash boundaries to prove deterministic recovery from canonical repository state.

Scenarios should include interruption around:

- node launch;
- returned-but-not-yet-reconciled result;
- review freeze/verdict/finalization;
- parallel node completion and integration;
- dynamic/JIT graph extension;
- atomic transition boundaries;
- stale-result and dependency changes.

Core properties include no duplicate execution solely due to runtime loss, no illegal dependency advance, no lost valid result, no invalid GREEN, no unrecoverable deadlock, and deterministic next-obligation reconstruction.

### Research requirement before promotion

Research this candidate independently before Definition. Compare example-based replay, generated state-machine/property testing, fault injection, model checking/state-space approaches, and realistic scope so the harness gives high confidence without becoming a second workflow implementation.

---

## FUT-009 — Lightweight non-authoritative execution trace / replay

Status: `parked`
Target horizon: PWv2.2 candidate, only if complexity/runtime cost remains low
Origin: user

### Intent

Investigate a lightweight non-authoritative trace of mechanical workflow decisions for debugging, regression replay, observability and future PWv2.3 System-One evaluation.

Possible trace fields include:

- obligation/subject identity;
- canonical input fingerprint;
- matched mechanical rule IDs;
- DAG frontier and selected node(s);
- transition/result classification;
- next obligation;
- timing/cost metadata where useful.

Canonical Git/project state remains the only workflow authority. Trace loss must not impair recovery or legality.

### Scope constraint

Adopt only if the implementation does not materially complicate Project Workflow, increase agent context load, or create a maintenance-heavy parallel state system.

### Research requirement before promotion

Research this candidate independently before Definition. Quantify storage/runtime/context overhead, retention strategy, privacy/sensitive-data boundaries, usefulness for regression replay and Jev/Laya/Von/poorjev benchmarking, and whether derived-on-demand traces can replace persistent logging.

---

## FUT-010 — DAG-node context compiler

Status: `parked`
Target horizon: PWv2.2 candidate
Origin: user
Dependency: FUT-001 DAG-based execution orchestration

### Intent

Investigate mechanically compiling the smallest lossless authority/context package needed by one executable DAG node.

The compiler may resolve:

- exact requirements/decisions applicable to the node;
- dependency results and immutable bindings;
- code/write scope;
- tests/evidence/readback obligations;
- must-open sources;
- exclusions and authorization boundaries.

The compiler must derive from canonical PW authority and references; it must not invent scope or become a new authority layer.

Expected benefits to validate are lower worker context/token cost, less irrelevant project-history loading, reduced cross-node contamination and more reproducible worker inputs.

### Research requirement before promotion

Research this candidate independently before Definition. Measure losslessness, context-size reduction, derivation/fingerprint rules, interaction with dynamic DAG changes, caching/content-addressing opportunities, and failure behavior when required authority cannot be resolved.

---

## FUT-011 — Requirement-to-evidence traceability graph

Status: `parked`
Target horizon: PWv2.2 candidate subject to scope; may defer if DAG scope becomes too large
Origin: user

### Intent

Investigate a provenance/traceability graph distinct from the execution DAG.

The execution DAG answers `what depends on what to execute`.

The traceability graph should answer `why does this work exist and what evidence proves the accepted requirement/decision is satisfied`.

Potential relations include:

`requirement → decision/ADR → milestone/Card → implementation/result → tests/evidence → review attempt/verdict`

Potential uses:

- detect accepted requirements without implementation/evidence coverage;
- detect Cards/results without clear authority coverage;
- support Final Integration coverage checks;
- perform impact analysis when a requirement/decision changes;
- identify potentially stale downstream tests/reviews/evidence after authority changes.

### Research requirement before promotion

Research this candidate independently before Definition. Determine the minimum useful graph, source-of-truth ownership, whether edges can be derived rather than manually maintained, how stale coverage is detected, and whether the value justifies inclusion in PWv2.2 versus deferral to a later version.


---

## Next-version intake rule

When the next Project Workflow version is started:

1. Read every unresolved candidate in this file before completing initial Brainstorming.
2. Re-evaluate each candidate against the then-current architecture and evidence.
3. Where a candidate declares a Research requirement, investigate that candidate as its own bounded Research question before promotion; do not treat acceptance of one candidate as evidence for another merely because they are architecturally related.
4. Explicitly classify each candidate as `promoted`, `deferred`, or `rejected/superseded`.
5. Promote accepted intent through normal Project Definition.
6. Do not implement directly from this file.
