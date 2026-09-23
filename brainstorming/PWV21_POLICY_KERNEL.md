# Brainstorm — PWv2.1 policy kernel

Date: 2026-09-23
Scope ID: pwv21-policy-kernel
Revision: R1
Status: tentative

## Goal

Explore a conservative PWv2.1 evolution that reduces repeated LLM interpretation of mechanical workflow state without turning Project Workflow into an orchestration engine or creating another source of project truth.

This is Brainstorming only. Nothing below is an accepted requirement, decision or implementation plan.

## Starting hypothesis

A useful mental model is:

```text
Git / repository durable state
        ↓
PWv2.1 stateless policy helpers
        ↓
exact legal obligation / validation result
        ↓
ChatGPT or Pi
        ↓
semantic role work
```

For Pi execution that uses subagents:

```text
Project Workflow
        ↓
typed Execution Obligation
        ↓
external orchestration-runtime
        ↓
worker(s)
        ↓
typed Execution Result
        ↓
Project Workflow
```

Project Workflow remains governance/policy. The separate `orchestration-runtime` remains execution/orchestration.

## Provenance / prior art

This Brainstorming starts from the prior-art synthesis on:

- `work/pwv2-architecture-prior-art-research`
- `research/PWV2_ARCHITECTURE_PRIOR_ART_R3.md`

and the transferred runtime findings in:

- `elmakus/orchestration-runtime`
- branch `work/orchestration-prior-art-findings`
- `research/ORCHESTRATION_RUNTIME_PRIOR_ART_R1.md`

Relevant prior-art families:
- `rpiv-todo`: dependency graph, cycle rejection, derived ready/blocked view;
- Dagu: deterministic workflow/state-machine execution patterns;
- `pi-fabric`: lazy capability discovery and code-mode mechanical composition;
- Laya/System One: bounded typed semantic classification with calibration caveats;
- `pi-extensible-workflows`: Pi-native worker/session/runtime orchestration.

The specific split proposed here is a synthesis for Project Workflow rather than a copy of one upstream architecture.

## Core constraint

PWv2.1 must preserve runtime interchangeability.

The desired property is:

```text
ChatGPT ↔ Pi
```

in the same way the project currently supports role continuation across:

```text
ChatGPT ↔ Codex
```

A fresh client/runtime must be able to reconstruct the exact legal continuation from repository state without access to another runtime's private session or database.

## Candidate PWv2.1 shape

### 1. Stateless validation layer

Possible commands/library operations:

```text
pw validate
pw graph
pw route
pw obligation
```

These are conceptual names only.

They should:
- read canonical repository state;
- return deterministic derived facts;
- have no daemon;
- have no mutable project database;
- not own worker sessions;
- not schedule subagents;
- not replace canonical Markdown/repository records.

### 2. `validate`

Candidate responsibility:
- manifest ↔ Task Board binding;
- stale/missing pointers;
- impossible status combinations;
- Research return/reconciliation invariants;
- review subject/state integrity;
- branch/workstream identity;
- canonical transition-record schema checks.

Potential value:
- fail earlier;
- reduce recovery ambiguity;
- make workflow regressions unit-testable.

Potential risk:
- duplicated behavior between Markdown contracts and code.

Open design question:
- whether code becomes normative for mechanical predicates or remains a validator generated/tested against Markdown contracts.

### 3. `graph`

Candidate responsibility:
- Task Card dependency existence;
- self-edge rejection;
- cycle detection;
- ready/blocked derivation;
- compact dependency view.

Prior-art source:
`rpiv-todo` mechanics, while rejecting its session-local persistence as project authority.

Potential value:
- deterministic readiness;
- less repeated LLM graph reasoning;
- compact human/agent progress view.

### 4. `route`

Candidate responsibility:
Given canonical durable state, compute the deterministic legal route when the route is fully mechanical.

Examples:
- pending REQUIRED/RECOMMENDED review → review;
- active Research obligation → research;
- green in-progress Card → post-review finalization;
- inconsistent bindings → recovery.

Non-goal:
Do not replace semantic/product/user decisions with code.

If a transition genuinely depends on judgment or user authority, the result should be an explicit semantic/user gate rather than a guessed route.

### 5. `obligation`

Candidate responsibility:
Produce a small derived semantic execution manifest for the current role.

Conceptual shape:

```text
identity:
  workflow revision
  workstream
  subject
  branch / expected state

role:
  exact semantic role
  freshness / continuation requirement

authority:
  exact canonical refs
  hashes / immutable source refs where useful

policy:
  mutation class
  abstract capability constraints
  workspace constraints

completion:
  checks
  evidence requirements
  result contract
```

The package is derived/disposable.

Canonical source always wins.

## What should remain LLM-owned

Likely examples:
- Brainstorming;
- product/strategic judgment;
- Project Definition synthesis;
- Strategic Planning;
- implementation reasoning;
- Research synthesis;
- independent review reasoning;
- RED classification when evidence requires semantic interpretation;
- deciding whether a new issue is substantively the same problem when deterministic identity cannot establish it.

PWv2.1 should not attempt to turn all workflow work into a deterministic state machine.

## What should remain outside PWv2.1

The separate orchestration-runtime should own:
- subagent scheduling;
- provider/model selection;
- worker session lifecycle;
- context transport;
- fan-out/fan-in;
- retry mechanics;
- worktrees used as subordinate execution sandboxes;
- runtime journal;
- budgets/timeouts/concurrency;
- runtime observability;
- concrete Pi tools/extensions/MCP wiring.

PW may constrain these semantically but should not implement their mechanics.

## Interchangeability model

A key acceptance idea for future Definition:

### ChatGPT-only path

```text
Git state
  ↓
PWv2.1 route/validation
  ↓
ChatGPT performs role
  ↓
canonical Git update
```

No orchestration-runtime required.

### Pi path

```text
Git state
  ↓
PWv2.1 route/obligation
  ↓
Pi
  ↓
orchestration-runtime if subagents are useful
  ↓
canonical result/evidence
  ↓
Project Workflow persistence
```

### Runtime handoff

A project can move:

```text
ChatGPT → Pi → ChatGPT
```

without transferring private runtime history.

The only required handoff is canonical repository state.

## Expected real-world benefits

### Fewer mechanical workflow mistakes

Examples:
- missing higher-priority review;
- starting a blocked Card;
- following a stale Research pointer;
- accepting a result for an obsolete subject;
- inconsistent branch/workstream binding.

### Lower context cost

Models need less repeated Router/contract reading for facts that code can derive mechanically.

This does not mean eliminating Markdown contracts; the target is to avoid using LLM reasoning as a calculator for deterministic state.

### Better cross-runtime consistency

ChatGPT and Pi can receive the same derived legal obligation instead of independently interpreting every router condition.

### Better testability

Mechanical policy behavior can have ordinary fixtures/property tests:

```text
given durable state X
expect route Y
```

and malformed-state cases can be tested without invoking a model.

### Better orchestration boundary

Pi's orchestration runtime can consume an exact obligation instead of becoming responsible for discovering Project Workflow authority.

## Complexity risks

### Risk 1 — Two implementations of the policy

If Markdown and code independently encode the same rules, they can drift.

Possible mitigation candidates to brainstorm:
- one generated from the other;
- executable predicates with Markdown as normative explanation backed by contract tests;
- code remains shadow/validation-only for v2.1;
- a smaller machine-readable transition table shared by docs and code.

No choice yet.

### Risk 2 — "Stateless helper" grows into a workflow platform

Guardrail hypothesis:
- no database;
- no daemon;
- no scheduler;
- no worker/session ownership;
- no hidden mutable project state.

### Risk 3 — Obligation compiler omits authority

A smaller context is useful only if it is lossless with respect to applicable constraints.

Need a fail-closed design with exact source refs/hashes and expandable omitted sources.

### Risk 4 — Breaking ChatGPT portability

If normal ChatGPT must run a Pi-only extension or a local daemon to understand Project Workflow, portability is lost.

Candidate constraint:
the executable core should be portable as a simple repository tool/library, while Markdown contracts remain sufficient for a capable runtime to recover manually if the helper is unavailable.

### Risk 5 — Premature executable router

Moving too much Router logic to code in one step could make PW harder to evolve.

Candidate migration:
```text
validate
→ graph
→ shadow route
→ measured parity
→ selective executable route
→ obligation compiler
```

## Candidate migration sequence

1. Add read-only `validate`.
2. Add read-only dependency `graph`.
3. Build `route --shadow`; current Router remains authoritative.
4. Replay historical workstream transition states and classify disagreements.
5. Only promote proven finite predicates to executable policy.
6. Add derived `obligation`.
7. Integrate the external orchestration-runtime through that contract.
8. Repeatedly test ChatGPT-only operation with the orchestration layer entirely absent.

## Strong invariant candidate

A future acceptance test could be:

> Delete all orchestration-runtime/session state. Open the project from a fresh ChatGPT session. Project Workflow must still identify the correct canonical continuation from Git alone.

A second invariant:

> Switch from ChatGPT to Pi or Pi to ChatGPT at any durable workflow boundary. Both must derive the same legal current obligation from the repository.

## Baseline correction from the actual PWv2 implementation

The initial hypothesis above predated direct inspection of the current target implementation in `elmakus/project_workflow_v2`.

Established implementation facts from current PWv2:
- PWv2 already has one canonical semantic `workflow/` tree;
- `tools/router.py` is already the production runtime-neutral obligation selector;
- `tools/state_contract.py` already provides executable validation for the durable state envelope;
- ChatGPT bootstrap points to canonical `workflow/ROUTER.md` in the workflow repository;
- Codex bootstrap points to the bundled copy of the same canonical `workflow/` tree;
- runtime/model/session/worker identity is deliberately non-canonical;
- the executable router already handles many deterministic route/stop/recovery transitions through the lifecycle.

Therefore PWv2.1 does **not** start from “Markdown router only -> shadow executable router”.
The material question is now where to stop extending the existing executable obligation selector and which mechanical predicates should remain in executable contracts versus semantic Markdown/LLM modules.

The earlier candidate migration sequence remains historical brainstorming context, not the current implementation baseline.

## Environment assumption: Paseo

User clarified that the intended agent backend will always be Paseo.

Current architectural interpretation:
- `orchestration-runtime` is the separate orchestration layer that owns worker/subagent execution mechanics;
- Paseo is the expected backend/infrastructure used by `orchestration-runtime`, not a replacement for that layer;
- Project Workflow owns governance, legal obligations, authority and durable workflow transitions;
- `orchestration-runtime` owns concrete orchestration such as worker realization, provider/model selection, sessions, retries, fan-out/fan-in and worktree/runtime mechanics, potentially through Paseo;
- do not duplicate those mechanics inside Project Workflow;
- neither OR nor Paseo daemon/session/runtime state may become canonical Project Workflow authority;
- keep PW obligations/runtime contracts semantically portable so ChatGPT can still reconstruct project legality from repository state without needing OR/Paseo private state.

This assumption may justify a thinner PW ↔ runtime interface and fewer hypothetical portability layers, while preserving repository-based authority interchangeability.

## Accepted exploratory choices

### Runtime portability / helper dependency

User choice accepted during Brainstorming:
- prefer/use the executable helper/reference implementation when available;
- do **not** make that helper a prerequisite for reconstructing the legal continuation;
- canonical repository state plus portable workflow contracts must remain sufficient for a fresh capable runtime to recover without private runtime/session state.

Challenge state: GREEN. The user reconfirmed this choice after the bounded failure-mode challenge that a helper-preferred path can silently drift from helper-less recovery unless parity is continuously tested.

### Execution Obligation depth

User choice accepted during Brainstorming: C3 / hybrid obligation.
The obligation should carry exact role/subject, exact authority refs/hashes, mechanically safe constraints, prerequisites, completion/test/evidence contract, bounded deterministic materialization, and an explicit `must-open` set for authority that cannot be safely substituted by the compiled view.

The obligation remains derived/disposable and never becomes project authority.

Challenge state: pending. Main failure mode to resolve: a worker may ignore `must-open` and act on an incomplete compiled view.

### Executable-policy scope

User choice accepted during Brainstorming: A2 / option 1B.
PWv2.1 should extend the existing executable router/kernel to compile exact deterministic obligations (role, subject, authority, prerequisites and completion/evidence contract) while keeping semantic role reasoning in Markdown/LLM and keeping orchestration mechanics outside Project Workflow.

Challenge state: pending one bounded adversarial challenge before treating this choice as stable exploratory state.

## Current decision tree

### A. Executable-policy scope

A1. keep the current PWv2 boundary: executable validation + deterministic obligation selection; semantic role procedures stay Markdown/LLM  
A2. selectively move additional proven finite predicates from semantic modules into the existing executable router/contracts while keeping the router an obligation selector  
A3. broaden the executable layer into a substantially more complete workflow state machine

Current recommendation:
A2, conservatively. PWv2 already proves the executable-router pattern; PWv2.1 should extend it only for predicates that are mechanically derivable from canonical state and fail closed on semantic/user gates.

### B. Source-of-truth relation between Markdown and code

B1. Markdown normative, code validator/helper  
B2. executable predicates normative for mechanical behavior, Markdown specification/docs  
B3. shared machine-readable transition contract generates/tests both

This is likely the most important complexity decision.

### C. Obligation package depth

C1. refs-only package; role opens sources itself  
C2. exact excerpts/materialized package with hashes  
C3. hybrid refs + bounded materialization + expandable sources

### D. Runtime portability

Exploratory choice accepted, challenge pending:
- canonical Git/workflow contracts remain sufficient for recovery;
- executable helper/reference implementation is preferred when available but not a mandatory runtime dependency;
- no client-private helper/session state may become project authority.


### Canonical mechanical-policy representation

User inclination: 2C, not yet frozen.

Analysis against the actual PWv2 implementation:
- a full declarative rewrite of the entire router would likely create a custom workflow DSL because many current predicates involve exact-subject binding, stale-state checks, read-set validation, reconciliation and fail-closed recovery;
- a narrower 2C is promising: a small canonical machine-readable registry for finite mechanical policy facts/rules, stable rule IDs, route/stop kinds, precedence and owner-module mapping;
- Python should evaluate reusable typed predicates and produce route/obligation outputs from that registry rather than duplicating policy values in prose;
- Markdown semantic modules should reference/explain the same rule IDs and remain authoritative for semantic role behavior, not restate executable condition trees;
- generated/contract-tested documentation views are acceptable, but the registry must not grow into a general workflow programming language.

Current recommendation: pursue 2C-lite rather than a full data-driven router DSL. New machinery is acceptable when it measurably removes duplicated policy interpretation and improves parity/testability.

### E. PW ↔ orchestration boundary

E1. simple role + refs contract  
E2. typed Execution Obligation/Result contract  
E3. richer capability/workspace/retry semantics in the interface

## Current frontier for continued Brainstorming

The first material decisions to explore are:

1. **How far beyond the current `tools/router.py` boundary should PWv2.1 go?**  
   Current recommendation: selectively executable finite predicates only; the router decides the next legal obligation/stop/recovery boundary, not how semantic roles perform their work.

2. **How should current executable mechanical contracts and Markdown semantic contracts relate so they cannot materially drift?**  
   Current recommendation: first evaluate the existing PWv2 pattern (executable mechanical contract + semantic Markdown + contract tests) before introducing a new transition DSL/table. Add a machine-readable policy table only if it removes more duplication than complexity it creates.

3. **Runtime portability helper dependency.**  
   Stable exploratory choice: helper/reference implementation preferred, but canonical repository/workflow state must remain independently recoverable. Helper-less parity must be continuously testable.

4. **Execution Obligation depth.**  
   Accepted exploratory choice: C3 hybrid refs + bounded deterministic materialization + explicit `must-open` authority. Challenge pending on whether `must-open` must be technically enforced before execution.

These are Brainstorming questions, not decisions.

## Definition promotion

- Definition promotion authorization: pending
- Definition promotion subject: none

Do not enter Project Definition until the user explicitly authorizes promotion of this exact scope/revision.
