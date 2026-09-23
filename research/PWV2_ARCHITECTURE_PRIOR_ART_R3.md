# Research — PWv2.1 vs Orchestration Runtime prior-art split

Date: 2026-09-23
Research question: Re-evaluate pi-fabric, Laya/System One, Dagu, rpiv-todo and pi-extensible-workflows under the corrected architecture boundary where Project Workflow owns governance/policy and a separate rebuilt orchestration runtime owns worker execution.

## Durable continuation metadata — chatgpt_only

Research ID: pwv2-architecture-prior-art-r3
Status: consumed
Origin role: brainstorming
Origin subject: pwv2-architecture-prior-art@R3
Return target: brainstorming:pwv2-architecture-prior-art@R3
Return reconciliation: applied
Return reconciliation result: brainstorming/PWV2_ARCHITECTURE_PRIOR_ART_R3.md@blob:9ab28373a6a24441fdad7674b01a30b376370c44

## Why R3 exists

R1 and R2 investigated useful prior art correctly at the mechanism level, but part of the synthesis blurred two layers that are separate by design in the user's architecture:

1. **Project Workflow** governs project authority and legal lifecycle.
2. **codex_workflow-like runtime orchestration** executes bounded workers.

R3 does not rewrite R1/R2. It corrects the ownership model and reclassifies every candidate.

The working target names in this document are:
- **Project Workflow v2.1 / PWv2.1** for the next incremental governance/policy evolution;
- **Orchestration Runtime** for the provider-neutral full replacement of current `codex_workflow`.

"Orchestration Runtime" is a research label only. The final product name is not decided.

## Source snapshot and freshness check

### Previously researched upstreams

R3 rechecked the current `main` HEADs:

- `monotykamary/pi-fabric@0c742a021e229602626ca76b6db5e831f38cb258`
- `NandhaKishorM/laya@010bacef009c855ccba814b51f7c8e1d38ab5e3f`
- `snellingio/system-one@8ca10fd7dda8ad7db4b88af64b27e61452dd3716`
- `dagucloud/dagu@f8e5c27ce6d94e65bc72ce2c340e6775f2e99083`
- `juicesharp/rpiv-mono@d74b1c99830a565f3df3f37e0a36616d17ffc574`
- `vekexasia/pi-extensible-workflows@0c11e343cc3b36afcc702a334a0c47ce0b27d622`

These match the source revisions already inspected in R1/R2. Therefore R3 did not find a source-version reason to invalidate the earlier mechanism findings. The correction is architectural ownership.

### Current local architecture evidence

R3 also inspected:

- `elmakus/codex_workflow@018bcede6e0b5fe59c099a15e246d03cba02d9f6`
  - README
  - PROJECT.md
  - workflow_breakdown.md
- current `elmakus/pi-unraid` durable project material:
  - `feat/pi-unraid-bootstrap:PROJECT.md`
  - `decisions/PIB_ADR_004_WORKFLOW_ROLES.md`
  - `work/pi-extension-evaluation:research/PI_EXTENSION_EVALUATION_R1.md`

The current Pi project evidence explicitly separates Project Workflow authority roles from model/runtime identities and already warns that external orchestration must not silently become a second authority source.

## Correct architecture model

The revised model is not:

```text
Project Workflow
  -> interprets policy
  -> schedules all agents
  -> owns retries/worktrees/provider selection
```

It is:

```text
                 GOVERNANCE / POLICY
┌──────────────────────────────────────────────────────┐
│ Project Workflow v2.1                               │
│                                                      │
│ - canonical repo/Git authority                       │
│ - exact current subject/obligation                   │
│ - phase/role legality                                │
│ - accepted authority slice                           │
│ - evidence requirements                              │
│ - review freshness semantics                         │
│ - user-owned gates                                   │
│ - deterministic stop/transition validation           │
└──────────────────────┬───────────────────────────────┘
                       │ typed Execution Obligation
                       ▼
                 EXECUTION / ORCHESTRATION
┌──────────────────────────────────────────────────────┐
│ Orchestration Runtime                                │
│                                                      │
│ - launch worker/session                              │
│ - map role requirements to provider/model/resources  │
│ - deliver bounded context                            │
│ - fan-out/fan-in / pipeline                          │
│ - retry / timeout / concurrency / budget             │
│ - worktree/session isolation                         │
│ - runtime journal/replay                             │
│ - compact status and observability                   │
└──────────────────────┬───────────────────────────────┘
                       │ typed Execution Result
                       ▼
┌──────────────────────────────────────────────────────┐
│ Project Workflow v2.1                                │
│ - re-check canonical subject/head/preconditions      │
│ - validate evidence/result contract                  │
│ - persist the legal workflow transition in Git       │
└──────────────────────────────────────────────────────┘
```

The Orchestration Runtime may perform normal repository edits through an Executor role. What it must not do is independently decide that a Card, review subject, Research obligation, Definition, Planning gate or user-owned transition has legally advanced.

## Responsibility boundary

| Concern | PWv2.1 | Orchestration Runtime | Interface |
|---|---|---|---|
| Canonical workstream/Card/review state | Owns | Reads only as supplied/authorized | Exact refs/hashes |
| Legal next phase/role | Owns | Must not infer/override | `obligation.role` |
| User-owned promotion/gate semantics | Owns | Displays/waits/returns response | gate id + response |
| Authority selection | Owns | Materializes/delivers | authority manifest |
| Model/provider choice | Constraint only when authority explicitly requires it | Owns normal resolution | capability/model requirements |
| Tool/resource mapping | Abstract policy/invariants | Owns concrete mapping | capability policy |
| Worker session lifecycle | No | Owns | freshness/continuation flag |
| Parallelism / fan-out | Defines whether work items are semantically independent if policy requires | Owns scheduling | bounded work items/dependencies |
| Retry | Defines when retry would violate authority/freshness | Owns runtime retry mechanics | retry class / idempotency metadata |
| Worktrees | Defines branch/workstream lifecycle constraints | Owns subordinate worktree mechanics | workspace policy |
| Result shape/evidence obligations | Owns semantics | Enforces transport/schema | result schema |
| Runtime journal | Never authority | Owns as optimization | optional trace ref |
| Project recovery | Must work from Git alone | Can accelerate when journal survives | canonical binding |
| Fresh independent review | Owns semantic evidence boundary | Owns fresh session/read-only enforcement | reviewer contract |
| Progress UI | Canonical facts source | Can render runtime/derived view | source refs |

## Current codex_workflow: legacy baseline, not target

The current fork already has several ideas worth preserving at the mechanism level:

### Preserve as concepts

1. **Bounded worker delegation**
   - workers receive role-owned packages instead of the entire Main context.
2. **Worker-runtime abstraction**
   - current `plus` and `muse-max` profiles prove that one semantic role can be backed by different runtimes.
3. **Independent Tester ownership**
   - executor and verifier are separate execution owners.
4. **Event-driven waiting**
   - normal coordination avoids status polling; rare material events can interrupt.
5. **Bounded result return**
   - workers return normal/final results to Main rather than sharing arbitrary sibling state.
6. **Role-specific capability intent**
   - read-only discovery/review roles and mutating executor roles are already conceptually distinct.

### Rebuild rather than preserve as architecture

1. **Codex-specific identity**
   - the replacement should not assume one provider/family.
2. **Fixed six-role topology in runtime core**
   - Project Workflow owns semantic role/obligation meaning. Runtime should accept a role contract rather than hard-code project governance.
3. **Hard-coded provider profiles**
   - generalize to adapters/capability profiles.
4. **Main as owner of project policy because runtime says so**
   - Main follows Project Workflow authority; the runtime merely executes current obligations.
5. **Runtime-owned project documentation/state as continuity mechanism**
   - useful runtime notes may exist, but repository Project Workflow state remains sufficient for recovery.
6. **Provider-specific session registry as project truth**
   - session registries remain ephemeral/non-authoritative execution state.

The rebuild can therefore reuse lessons without inheriting the existing product shape.

# Source-by-source re-evaluation

## 1. rpiv-todo

### Mechanism

Current `@juicesharp/rpiv-todo` exposes tasks with:
- `blockedBy` dependency edges;
- reverse derived `blocks`;
- validation that dependencies exist;
- self-edge rejection;
- tombstone handling;
- cycle detection before mutation;
- explicit status transitions;
- reconstruction after reload/compaction from session snapshots.

### PWv2.1 fit — strong

The dependency/cycle mechanics directly match Project Workflow's canonical Task Board/Card problem.

PWv2.1 can use a stateless derived validator that:
- reads selected WORKSTREAM + Task Board + Task Cards;
- verifies every dependency target;
- compares board/Card dependency declarations;
- rejects self-dependency and cycles;
- computes `ready`, `blocked`, and terminal sets;
- emits exact source refs.

This is policy/state validation, not agent orchestration.

### Orchestration Runtime fit — secondary

A runtime/UI can render a compact live working queue or use the derived ready set to schedule already-authorized independent work.

The runtime must not maintain a separate task graph that can disagree with the canonical board.

### Reject

Do not copy rpiv-todo's conversation/session snapshot persistence as project authority. Git-backed Project Workflow is stronger and cross-session/cross-host durable.

### Correct R1 ownership

- R1 L1 stays with PWv2.1.
- R1 P2 can become a derived UI/runtime view, but its data source remains PWv2.1.

## 2. pi-fabric

### Mechanism

Fabric supplies:
- one programmable `fabric_exec` surface;
- checked TypeScript or configured Python execution;
- branches, loops and fan-out outside the parent model transcript;
- generic capability namespaces;
- `tools.search`, `tools.describe`, `tools.call`;
- nested Pi/MCP/extension/provider calls;
- capability approvals/guardrails;
- bounded returned JSON while activity/tool details remain outside normal parent reasoning;
- bounded audit/projection traces;
- optional agent/workflow/mesh subsystems.

Discovery does not grant permission. Every invocation still goes through normal registry/authorization checks.

### PWv2.1 fit — small

Fabric is not a Project Workflow policy mechanism.

PWv2.1 may benefit indirectly if a policy validator/research tool uses code-mode for mechanical evidence collection, but that is an implementation substrate, not a governance feature.

### Orchestration Runtime fit — strong

Two Fabric patterns belong naturally in the runtime layer:

#### Dynamic capability discovery

Expose a small capability index, search, load exact schema/details only when needed, then call. This avoids permanently injecting every MCP/plugin schema.

#### Code-mode composition

Mechanical read/search/filter/fan-out work can happen in one bounded program and return only:
- structured facts;
- exact evidence refs;
- explicit partial/failure information.

This is especially useful for bounded Research, inspection and tool-heavy worker roles.

### Interface fit

Stable evidence references from runtime-composed work can flow back through the Execution Result envelope.

PW does not need the nested transcript; it needs verifiable evidence refs and a declared result.

### Reject

Do not adopt Fabric mesh/shared-task/state as Project Workflow authority.

If another runtime such as pi-extensible-workflows owns worker orchestration, Fabric's multi-agent/workflow layer should not automatically become a second scheduler. It may be constrained to tool composition/capability routing or omitted.

### Correct R1 ownership

- R1 L2 moves from "PWv2 low-risk" to Orchestration Runtime.
- R1 L3 moves to Orchestration Runtime.
- R1 P3 becomes an Orchestration Runtime substrate concern.
- R1 R1 remains rejected as authority.

## 3. Laya / System One

### Mechanism

System One-style runtimes answer constrained typed questions without normal free-text generation:
- `choice`;
- `score`;
- `noul` / boolean probability.

System One Lite keeps logits only for allowed answer codes. It explicitly warns that returned probability mass/confidence is not a calibrated probability of correctness and recommends thresholds based on representative labeled data.

Laya adds specialized typed-decision checkpoints/router behavior and reports calibration-oriented metrics, but current benchmark material still shows calibration quality depends on checkpoint/domain and temperature fitting.

### PWv2.1 fit — deliberately weak

Finite Project Workflow transition predicates should be deterministic code, not probabilistic classification.

A classifier must not decide:
- whether Definition is complete;
- whether user promotion is authorized;
- whether review is legally required;
- whether RED can be ignored;
- whether a Card is terminal;
- what the canonical next route is when durable state already determines it.

### Orchestration Runtime fit — optional/advisory

A calibrated classifier can be useful for bounded **non-authoritative** runtime choices, for example:
- choose among pre-approved tool/capability classes;
- pick a cheap versus strong worker profile;
- classify a raw tool result into a predeclared evidence bucket;
- decide whether to escalate a worker to a stronger model;
- rank candidate tools before full schema loading.

The legal action set must already be bounded by PW/runtime policy.

Low confidence/OOD/unsupported input escalates to a reasoning worker.

### Interface fit

If PW explicitly requests a semantic classification obligation, the runtime can return:
- selected label;
- full distribution;
- model/checkpoint identity;
- calibration version;
- abstain/escalation status.

The classification is evidence, not a transition.

### Reject

- classifier as authoritative PW router;
- confidence threshold as proof of correctness/safety;
- uncalibrated "0.9" treated as 90% correctness.

### Correct R1 ownership

R1 P1 moves primarily to optional Orchestration Runtime/advisory infrastructure, not PW core.

## 4. Dagu

### Mechanism

Dagu provides deterministic DAG execution with:
- explicit `depends`;
- step and DAG retry policies;
- harness steps for AI/CLI workers including Pi;
- structured `output_schema` validation;
- human tasks and approval gates;
- push-back/rewind;
- sub-DAGs;
- durable run inspection/retry.

Its Pi harness can set provider/model/thinking/tool allowlists and can disable context-file discovery.

### PWv2.1 fit — pattern only

The useful PW lesson is **deterministic policy evaluation**, not "put Project Workflow in Dagu."

Finite transition conditions in ROUTER/state contracts can be implemented/tested as code/state-machine logic.

That policy evaluator should:
- read canonical repo state;
- emit one legal obligation/stop or an explicit semantic/user gate;
- own no runtime worker history;
- persist no alternate project state.

### Orchestration Runtime fit — strong prior art

Dagu's natural home is runtime execution:
- dependency scheduling;
- retries;
- step timeouts;
- validated worker result shape;
- approval wait transport;
- fan-out/sub-workflows;
- inspection and replay.

However a Pi-native runtime may make external Dagu deployment unnecessary.

### Interface fit

Dagu reinforces several boundary contracts:
- output schema validation;
- explicit dependency edge;
- explicit approval/gate id;
- retryability/failure state;
- bounded prior output reference rather than blindly inlining huge logs.

### Reject

Dagu DAG/run DB/history must not decide Project Workflow authority or be required to recover the project.

### Correct R1 ownership

- R1 A1 remains a PWv2.1 policy-evaluator candidate, but is **not** a worker orchestrator.
- R1 A3 moves to Orchestration Runtime.
- Dagu itself becomes external prior art rather than a proposed PW engine.

## 5. pi-extensible-workflows

### Mechanism

Current pi-extensible-workflows supplies a Pi-native deterministic JavaScript workflow runtime with:
- separate `agent(...)` sessions;
- no automatic inheritance of Main agent context;
- roles;
- provider/model aliases;
- tool/skill/extension selectors;
- `contextFiles`;
- `parallel` and `pipeline`;
- registered workflow functions;
- `outputSchema`;
- exactly-one structured `workflow_result`;
- checkpoints;
- budgets;
- worktrees;
- structural call-site identity;
- journal replay of completed operations;
- retry/resume;
- compact status/Trajectory observability;
- compact `workflow_catalog` discovery.

It is directly designed for Pi and overlaps heavily with the runtime responsibilities the replacement codex_workflow needs.

### PWv2.1 fit — almost none directly

PWv2.1 should not absorb its scheduler/journal.

The relevant PW idea is only that a worker-runtime can technically enforce the contracts PW emits.

### Orchestration Runtime fit — strongest source

This is the strongest concrete substrate candidate found in R1-R3.

It already solves much of the low-level runtime work that a rebuild would otherwise need:
- create Pi child sessions;
- isolate context;
- map roles/resources;
- fan out work;
- validate result shape;
- manage runtime retry/replay;
- create subordinate worktrees;
- collect checkpoints;
- inspect runs;
- bound concurrency/budgets.

Therefore the future architecture decision should compare at least:

#### Option A — build on/wrap pi-extensible-workflows

Create a thin Project-Workflow-aware adapter that:
1. receives a typed Execution Obligation;
2. maps abstract role/capability requirements to a runtime role;
3. launches fresh/continuation agents as requested;
4. returns a typed Execution Result;
5. never treats piewf journal state as project authority.

#### Option B — implement a smaller Pi-native role runtime

Use direct Pi subagent primitives and build only the required scheduling/result/retry layer.

The source-level research does not choose between A and B.

### Fresh review caveat

The bundled `reviewLoop` is **not** equivalent to PW independent review.

It passes developer summaries and previous review findings into reviewer iterations. PW fresh review requires:
- a new reviewer execution/session when the policy demands freshness;
- canonical review subject;
- canonical authority;
- independently inspectable evidence;
- no contaminated implementation-chat narrative unless that narrative is itself accepted evidence.

A custom runtime workflow can enforce this; the bundled generic loop should not be used as-is.

### Runtime journal caveat

Journal replay is an optimization.

A future integration must prove:
- deleting the entire piewf run store does not prevent project recovery;
- a stale persisted run cannot resume after canonical subject/head changed;
- external side effects are idempotent/read back because a crash after effect but before journaling can duplicate them.

### Correct R2 ownership

- R2 A4 moves from "PWv2 architectural refactor" to **Orchestration Runtime candidate/substrate**.
- R2 R6/R7/R8/R9 remain valid rejects.

# Corrected candidate portfolio

## A. PWv2.1 candidates

### PW1 — Canonical dependency graph validator

Problem:
Task Card/Task Board dependencies are canonical but currently require repeated interpretation and lack one dedicated cycle/consistency engine.

Mechanism:
Stateless graph validator over selected workstream/board/cards.

Checks:
- missing IDs;
- Card/board disagreement;
- self edges;
- cycles;
- dependency terminality;
- ready/blocked derivation.

Benefit:
Deterministic readiness and earlier impossible-plan detection.

Authority impact:
None if derived from canonical state.

Context impact:
Small-to-medium reduction.

Complexity:
Low-to-medium.

Validation:
Historical workstreams plus synthetic malformed/cyclic fixtures; byte-identical derived output after cache deletion.

### PW2 — Shadow deterministic policy evaluator

Problem:
Many router choices are finite predicates over durable state.

Mechanism:
Read-only executable evaluator computes:
- exact legal obligation;
- real stop;
- inconsistent/recovery state;
- explicit semantic/user gate when deterministic evaluation cannot finish.

It never schedules a worker.

Benefit:
Find Markdown ambiguity and build a transition corpus.

Authority impact:
None in shadow mode.

Context impact:
No immediate production saving; enables later reduction.

Complexity:
Medium.

Validation:
Replay historical transition commits and fuzz invalid state. Every disagreement with current contracts must be explained.

### PW3 — Executable policy kernel for finite transitions

Problem:
Repeated LLM interpretation of deterministic router conditions costs context and permits inconsistent readings.

Mechanism:
Promote proven PW2 logic into versioned Project Workflow policy code.

The code:
- reads canonical Git-backed state;
- produces an Execution Obligation or Stop;
- does not launch agents;
- does not store project state outside Git.

Markdown becomes human-readable specification/docs backed by contract tests, not a second behavior implementation.

Benefit:
Large reduction in router interpretation and stronger invalid-state rejection.

Authority impact:
High Project Workflow refactor, but no authority-model change.

Context impact:
Potentially high.

Complexity:
High.

Validation:
Shadow equivalence corpus, property/fuzz tests, crash/recovery from repo, contract parity checks.

### PW4 — Canonical transition-record schema validation

Problem:
Research/review/handoff records contain transition-critical fields that can be malformed even when prose looks reasonable.

Mechanism:
Validate exact subjects, pointers, review states, return targets/reconciliation, branch bindings and impossible combinations.

Benefit:
Fail closed earlier; simpler recovery.

Authority impact:
Low if schema validates existing canonical records.

Context impact:
Small direct, high reliability benefit.

Complexity:
Low-to-medium.

Validation:
Current history + malformed fixture suite.

### PW5 — Execution Obligation compiler

Problem:
Runtime must not infer canonical authority/role semantics from broad repository context.

Mechanism:
Given the legal current obligation, PW emits a small **semantic manifest**, not an agent prompt.

Suggested fields:
- `workflow_revision`;
- `workstream_id`;
- `subject`;
- `branch`;
- `expected_head` / state digest;
- `role`;
- `authority_refs` + content hashes/commit refs;
- dependency-result refs;
- required checks/evidence;
- freshness/continuation requirement;
- abstract mutation/capability policy;
- workspace constraints;
- expected result schema identifier;
- user-gate/review invariants if applicable.

Benefit:
Prevents runtime from becoming a hidden authority selector.

Authority impact:
Medium because omission correctness matters; manifest is derived/disposable.

Context impact:
High indirect reduction.

Complexity:
Medium-high.

Validation:
Compare full manual authority reconstruction against compiled manifests across historical Execution/Research/Review/Planning cases. Mutate source after compile and require stale-manifest rejection.

### PW6 — Returned-result canonical precondition validator

Problem:
A worker may finish after branch/head/subject changed.

Mechanism:
Before accepting any result, re-read canonical state and verify:
- same obligation subject;
- compatible branch/head or explicitly permitted descendant;
- same workflow/policy revision compatibility;
- same authority refs/digests;
- no higher-priority obligation appeared.

Benefit:
Prevents stale runtime completion from advancing workflow.

Authority impact:
Strengthens existing authority.

Context impact:
Small.

Complexity:
Medium.

Validation:
Inject concurrent commits, RED review arrival, user-gate changes and runtime resumes.

### PW7 — Repository-derived ready/progress view

Problem:
Humans/agents need a compact view of current/blocked/ready work.

Mechanism:
Generate from canonical board/cards on demand; no mutable UI state.

Benefit:
Less rereading, good recovery UX.

Authority impact:
None.

Context impact:
Small-medium.

Complexity:
Medium host/UI dependent.

Validation:
Delete UI/cache and reproduce identical view from Git.

## B. Orchestration Runtime candidates

### OR1 — Provider-neutral role runtime

Problem:
Current codex_workflow is tied to Codex/Muse-specific profiles while future execution should not make provider identity part of Project Workflow semantics.

Mechanism:
Adapter interface:
- role/capability requirements in;
- resolved provider/model/thinking/runtime out;
- model/provider mapping configured independently of PW unless canonical project authority explicitly pins one.

Benefit:
One orchestration layer across providers/models.

Authority impact:
None if mapping is execution configuration.

Context impact:
Neutral directly.

Complexity:
Medium-high.

Validation:
Same Execution Obligation across at least two adapters; equivalent result contract and capability enforcement.

### OR2 — Fresh/continuation worker session primitive

Problem:
Different roles require either hard freshness or deliberate continuation.

Mechanism:
Explicit session mode:
- `fresh`;
- `continue(session_ref)` only when obligation permits it.

Default fresh for independent reviewer.

Benefit:
Technical enforcement of role isolation.

Authority impact:
None; obeys PW contract.

Context impact:
High positive.

Complexity:
Medium; pi-extensible-workflows already supplies much of it.

Validation:
Prove reviewer cannot see executor transcript/session; prove continuation retains only when authorized.

### OR3 — Bounded context materializer/transport

Problem:
PW can identify canonical refs but runtime must turn them into a worker-usable context without loading the parent transcript.

Mechanism:
Resolve PW manifest refs, verify hashes, deliver:
- exact excerpts/files;
- stable source refs;
- role instructions;
- omitted-but-expandable manifest.

Runtime cannot choose different authority.

Benefit:
Very high context reduction.

Authority impact:
Medium implementation risk if materialization omits or mutates canonical inputs.

Complexity:
High.

Validation:
Full-context vs bounded-context replay; constraint-miss rate is primary metric, not token reduction.

### OR4 — Structured result transport

Problem:
Free-form worker prose is hard to validate and compose.

Mechanism:
Output schemas + exactly one terminal result envelope.

Benefit:
Deterministic fan-in, clearer failures and smaller parent context.

Authority impact:
None; schema correctness is not semantic correctness.

Complexity:
Low-medium if piewf substrate.

Validation:
Malformed/partial/oversized result cases; repair behavior; evidence-ref integrity.

### OR5 — Fan-out / fan-in / pipeline scheduler

Problem:
Independent role work should not require serial Main turns.

Mechanism:
Parallel keyed work items, ordered pipelines, dependency-aware scheduling.

Runtime receives already-authorized work items; it does not invent Project Workflow phases.

Benefit:
Latency/context savings.

Authority impact:
Low if semantic independence is declared by policy/input.

Complexity:
Medium.

Validation:
Parallel independent reads/research lanes and isolated mutating worktrees; deterministic result association.

### OR6 — Lazy capability discovery

Problem:
Large plugin/MCP/tool schema surfaces consume context.

Mechanism:
Compact index → search → describe → call; preserve authorization separately.

Benefit:
Potentially large tool-schema context reduction.

Authority impact:
None.

Complexity:
Low-medium with existing Pi/MCP/Fabric primitives.

Validation:
A/B full-schema vs lazy discovery on real tasks; ambiguous names and missing capability tests.

### OR7 — Code-mode mechanical composition

Problem:
Tool-heavy loops/search/filter steps create transcript bloat.

Mechanism:
Checked code-mode block executes nested read/search/tool calls and returns compact structured result/evidence refs.

Benefit:
Large context/round-trip reduction.

Authority impact:
None when effects remain capability-gated.

Complexity:
Medium.

Validation:
Read-only first; partial failure, cancellation, oversized result and evidence retention tests.

### OR8 — Runtime journal/replay

Problem:
A runtime crash should not require repeating every completed worker/tool operation.

Mechanism:
Structural operation identity and replay completed operations; execute only incomplete operations.

Binding must include the canonical Execution Obligation digest.

Benefit:
Operational resilience.

Authority impact:
High risk if mistaken for project state; safe only as cache.

Complexity:
Medium-high.

Validation:
Delete runtime state and recover project from Git; stale manifest blocks resume; crash around side effects.

### OR9 — Worktree isolation and mutation ownership

Problem:
Parallel mutating workers can collide.

Mechanism:
Named subordinate worktrees; one mutation owner per path/scope; explicit integration back to the workstream branch.

Benefit:
Safe parallelism.

Authority impact:
Runtime worktree is subordinate; selected PW workstream branch remains lifecycle identity.

Complexity:
Medium.

Validation:
Concurrent disjoint edits, conflicting edits, cleanup failure, stale base and aborted run.

### OR10 — Event-driven lifecycle and observability

Problem:
Polling wastes context/runtime and obscures state.

Mechanism:
Durable execution IDs, terminal event delivery, rare material event channel, compact inspect/status, Gantt/trajectory optional UI.

Benefit:
Lower chatter and easier operational debugging.

Authority impact:
None.

Complexity:
Medium.

Validation:
Long-running worker, crash, cancellation, duplicate completion suppression, restart.

### OR11 — Budgets / timeout / recursion / concurrency guards

Problem:
Agent/runtime fan-out can run away.

Mechanism:
Per-run limits and hard ceilings; child capability inheritance must be narrowing or explicit.

Benefit:
Operational safety/cost control.

Authority impact:
None.

Complexity:
Medium.

Validation:
Limit races, cancellation, max-depth, queued/parallel workers and budget exhaustion.

### OR12 — Optional calibrated typed decision helper

Problem:
Some runtime choices are semantic but too small for a large reasoning worker.

Mechanism:
Laya/System-One-style typed choice/score/boolean under closed labels with abstain/escalation.

Allowed examples:
- tool shortlist;
- worker profile tier suggestion;
- evidence bucket;
- escalation recommendation.

Forbidden:
- canonical PW route;
- approval authority;
- review verdict acceptance.

Benefit:
Potential latency/cost improvement.

Authority impact:
Low if advisory.

Complexity:
Medium-high because calibration lifecycle is required.

Validation:
Real labeled runtime corpus; accuracy/confusion/Brier/ECE/OOD/option-order drift; explicit abstain.

### OR13 — Derived runtime/working-queue UX

Problem:
Operator needs visibility across runtime jobs without reading full transcripts.

Mechanism:
Combine PW-derived obligation/ready data with non-authoritative runtime status.

Benefit:
Good Pi/Paseo/TUI UX.

Authority impact:
None if clearly labeled derived/runtime.

Complexity:
Medium.

Validation:
Restart/cache deletion; no UI mutation path can advance canonical PW state.

## C. Shared interface-contract candidates

### IF1 — Typed Execution Obligation

This is the core boundary.

PW owns generation; runtime owns consumption.

Minimum conceptual fields:

```text
identity:
  workflow_revision
  workstream_id
  obligation_id
  subject

canonical_precondition:
  branch
  expected_head/state_digest

role:
  semantic_role
  freshness: fresh | continuation
  continuation_ref?: ...

authority:
  exact refs + hashes/commit refs
  dependency results

policy:
  mutation class
  capability constraints
  workspace constraints
  review/evidence invariants

completion:
  required checks
  evidence requirements
  result schema id
```

Do not put provider-specific implementation details here unless accepted project authority explicitly requires them.

### IF2 — Typed Execution Result

Runtime returns facts, not a new route.

Suggested conceptual fields:

```text
execution_id
obligation_digest
status: completed | failed | cancelled | blocked | stale
result_payload
evidence_refs
check_results
mutation_summary
resulting_commit/head if any
runtime_failure_code if any
runtime_trace_ref optional
resolved_runtime metadata optional/non-authoritative
```

PW decides what that result means for the lifecycle.

### IF3 — Fresh independent-review contract

PW semantic requirements:
- exact review subject;
- canonical authority slice;
- canonical evidence requirements;
- no implementer narrative unless canonical;
- fresh reviewer required.

Runtime enforcement:
- new session/process;
- no inherited executor transcript;
- no persistent handle reuse;
- read-only/minimum capabilities unless the review contract permits otherwise;
- result schema for verdict/findings/evidence.

Both halves are necessary.

### IF4 — Abstract capability policy

PW should express **what is permitted**, not necessarily Pi tool names.

Example concepts:
- repository read-only;
- repository mutation;
- Git commit allowed/forbidden;
- network allowed/forbidden;
- external side effects allowed/forbidden;
- secret access class;
- user interaction allowed/required.

Runtime maps these to concrete Pi tools/extensions/MCP permissions.

This keeps PW provider/tool-implementation neutral.

### IF5 — Canonical stale-binding handshake

Before launch/resume:
runtime verifies the supplied branch/head/obligation digest still exists.

Before accepting result:
PW rechecks canonical state.

Both directions fail closed.

### IF6 — User/checkpoint gate handshake

PW decides:
- a gate is legally required;
- exact subject;
- what response types are allowed.

Runtime:
- pauses;
- renders/collects response;
- returns `gate_id + response`.

Only PW persistence makes that response part of canonical workflow state.

### IF7 — Runtime failure taxonomy

Runtime should report stable bounded failure facts such as:
- `retryable_provider_failure`;
- `timeout`;
- `cancelled`;
- `capability_missing`;
- `permission_denied`;
- `budget_exhausted`;
- `workspace_conflict`;
- `schema_invalid`;
- `stale_precondition`;
- `side_effect_uncertain`.

Runtime must not translate those directly into arbitrary Project Workflow route changes.

PW policy classifies the next legal obligation.

# What should not be in PWv2.1

The corrected research explicitly removes these from PW core:

- provider/model routing logic;
- native subagent scheduling;
- process/session management;
- worker retry loops;
- fan-out/fan-in implementation;
- runtime journal;
- runtime worktree allocation;
- MCP/tool schema search implementation;
- runtime budgets/concurrency;
- live agent UI;
- persistent worker sessions.

PW may impose semantic constraints on any of them, but should not implement their mechanics.

# What should not be in the Orchestration Runtime

The runtime must not own:

- canonical workstream/Card/milestone status;
- Project Definition readiness;
- accepted requirements/decisions;
- legal phase transition;
- whether a user promotion gate is satisfied;
- whether a RED review is superseded/ignorable;
- authority-slice selection by inference;
- final workflow acceptance;
- a second durable task board;
- project recovery that requires runtime DB/journal.

# Corrections to R1/R2 candidate ownership

| Previous candidate | R3 classification |
|---|---|
| L1 Task dependency graph validator | PWv2.1 |
| L2 On-demand capability discovery | Orchestration Runtime |
| L3 Read-only code-mode composition | Orchestration Runtime |
| L4 Structured transition envelope | PWv2.1 + Interface |
| L5 Shadow deterministic router | PWv2.1 |
| A1 Executable deterministic router | PWv2.1, renamed conceptually to policy evaluator/kernel; **not scheduler** |
| A2 Bounded role-context package compiler | Split: PW authority/obligation manifest + Runtime materialization/transport |
| A3 Deterministic orchestrator around workers | Orchestration Runtime |
| P1 Typed semantic decision primitive | Optional Orchestration Runtime advisor |
| P2 Repository-derived progress graph | PW-derived data + optional runtime/UI presentation |
| P3 Tool-composition/runtime substrate | Orchestration Runtime |
| R1 Fabric workflow/mesh as PW authority | Still reject |
| R2 rpiv task persistence as canonical state | Still reject |
| R3 small classifier as authoritative router | Still reject |
| R4 confidence as proof | Still reject |
| R5 external orchestrator history required for recovery | Still reject |
| R2 A4 piewf bounded worker substrate | Orchestration Runtime, not PW refactor |
| R2 bundled reviewLoop for PW review | Still reject |
| R2 runtime journal as PW recovery authority | Still reject |
| R2 ad-hoc workflow JS as policy authority | Still reject |
| R2 persistent handle for independent review | Still reject |

# Naming implications

The current name `codex_workflow` carries two misleading implications for the rebuilt layer:

1. **Codex-specific** — the future runtime should be able to map a semantic role to multiple providers/runtimes.
2. **Workflow authority** — Project Workflow already owns governance/lifecycle semantics.

A future naming decision should probably prefer a term such as:
- `Pi Role Runtime`;
- `Project Role Runtime`;
- `Pi Agent Runtime`;
- another provider-neutral "runtime/orchestrator" name.

`Pi Role Runtime` is the clearest descriptive research candidate because it says what the layer does without claiming Project Workflow authority. This is not an accepted naming decision.

# Recommended evaluation sequence for a future Definition

This research does not authorize implementation, but if the user later promotes the architecture, the lowest-risk sequence is:

1. **PW2 shadow policy evaluator**
   - no runtime change;
   - measure deterministic route coverage.
2. **PW dependency/state validators**
   - graph/cycle + transition schema.
3. **Define IF1/IF2 typed obligation/result contract**
   - no new scheduler yet.
4. **Prototype runtime adapter with one role**
   - fresh read-only Research/Explorer is safest.
5. **Prototype independent reviewer**
   - prove zero executor transcript inheritance.
6. **Prototype bounded Executor**
   - one worktree, structured result, canonical stale guard.
7. **Evaluate pi-extensible-workflows substrate versus minimal native Pi runtime**
   - same IF1/IF2 contract so substrate can be swapped.
8. **Add fan-out/retry/journal only after single-role boundary is proven.**
9. **Delete runtime state repeatedly**
   - project must remain recoverable from Git.
10. **Only then consider optional Fabric code-mode or Laya/System One optimization.**

This sequence deliberately validates the boundary before optimizing runtime complexity.

# Validation matrix

| Experiment | Must prove |
|---|---|
| PW shadow evaluator replay | legal route parity with current contracts |
| Graph validator synthetic cycles | deterministic fail-closed dependency behavior |
| Obligation compiler replay | no missing authority constraints |
| Stale result injection | old worker result cannot advance new canonical subject |
| Fresh reviewer | no executor transcript/history in reviewer input/session |
| Runtime state deletion | project recovery from Git alone |
| Runtime resume after Git advance | stale resume fails closed |
| Worktree parallelism | no cross-worker mutation collision |
| Structured result corruption | schema/transport failure is explicit |
| External side effect crash | no claim of exactly-once; uncertainty/readback surfaced |
| Capability selector audit | abstract policy maps to effective least privilege |
| Provider swap | same obligation semantics across runtime adapters |
| Fabric code-mode A/B | context reduction without hidden evidence loss |
| System-One helper eval | calibrated benefit versus simple rules/reasoning fallback |

# Overall conclusion

The corrected R3 architecture is simpler than the R1/R2 synthesis:

## Project Workflow v2.1 should become a better **policy kernel**, not an orchestrator.

Its best improvements are:
- deterministic state/route validation;
- dependency graph validation;
- structured canonical records;
- exact Execution Obligation generation;
- stale-result rejection;
- derived compact views.

## The replacement for codex_workflow should become a provider-neutral **role execution runtime**.

Its best mechanisms are:
- fresh isolated Pi sessions;
- bounded context transport;
- provider/model/tool mapping;
- fan-out/fan-in;
- lazy capability discovery;
- code-mode mechanical work;
- structured outputs;
- runtime retry/journal;
- worktrees;
- budgets/timeouts;
- observability.

## pi-extensible-workflows is the strongest concrete substrate candidate.

It should be evaluated as a way to avoid rebuilding Pi-native session/orchestration mechanics from zero, not adopted as Project Workflow authority.

## Dagu validates the execution-engine architecture but is less naturally embedded than piewf.

It remains strong prior art for deterministic scheduling/retry/approval/output validation.

## pi-fabric is mainly a tool-runtime optimization.

Its strongest fit is lazy capability discovery and bounded code-mode composition, potentially underneath/alongside the Orchestration Runtime.

## rpiv-todo gives the clearest direct PWv2.1 improvement.

Copy its graph/cycle/derived-view ideas, not its persistence model.

## Laya/System One is optional optimization, not foundational architecture.

Do not introduce it until a real high-volume bounded classification problem exists and a domain-specific labeled calibration set is available.

The most important design rule is now explicit:

> **Project Workflow decides what is legally required. Orchestration Runtime decides how to execute that exact obligation. Runtime results are evidence/input back to Project Workflow, never a second source of project truth.**
