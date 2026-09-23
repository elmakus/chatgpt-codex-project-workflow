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

Challenge state: GREEN. The user selected PW-owned authority resolution: the kernel resolves/verifies every `must-open` source and hands OR/Paseo a complete authority bundle. OR transports/executes the package but does not decide which PW authority applies.

### Executable-policy scope

User choice accepted during Brainstorming: A2 / option 1B.
PWv2.1 should extend the existing executable router/kernel to compile exact deterministic obligations (role, subject, authority, prerequisites and completion/evidence contract) while keeping semantic role reasoning in Markdown/LLM and keeping orchestration mechanics outside Project Workflow.

Challenge state: GREEN. The main failure mode—an obligation that saves context by silently omitting applicable authority—is addressed by the hybrid obligation plus PW-owned authority-bundle resolution; OR/Paseo never substitutes its own authority selection.

### Additional accepted exploratory choices

The user accepted the following recommendations as a batch:

1. **Obligation fingerprint scope**
   - Fingerprint only the exact canonical inputs that materially determined the obligation.
   - Do not fingerprint the entire repository/commit merely for convenience.

2. **Obligation durability**
   - `Execution Obligation` remains derived/disposable rather than canonical durable project state.
   - Durable state retains only the canonical source state plus exact subject/fingerprint/result references needed for recovery and validation.

3. **Kernel mutation boundary**
   - PWv2.1 policy kernel remains read-only with respect to canonical project state for the 2.1 scope.
   - Kernel responsibilities are validation, routing, obligation compilation and result validation/reconciliation checks.
   - Canonical writes remain explicit coordinator/role actions governed by PW.

4. **2C-lite mechanical-policy representation**
   - Use a small versioned machine-readable registry containing stable rule IDs, precedence, outcomes, owners and named typed predicates.
   - Do not introduce arbitrary expression syntax or a general-purpose workflow DSL.

5. **PW ↔ orchestration-runtime contract**
   - Use versioned transport-neutral schemas for typed `Execution Obligation` and `Execution Result`.
   - JSON is the preferred interchange serialization.
   - Provider/model/session/Paseo/runtime telemetry stays outside canonical PW contract/state.

Challenge state: pending one bounded challenge for this accepted batch before the dependent choices are treated as stable exploratory state.

### Additional accepted exploratory choices — batch 2

The user accepted recommendations 6–9:

6. **Canonical mutation guard**
   - Kernel emits expected mutation preconditions/postconditions.
   - Coordinator/role performs the canonical write.
   - Kernel performs required readback + validation after the write.

7. **Deterministic obligation identity**
   - `obligation_id` should be content-derived/deterministic from rule/subject/fingerprint rather than random.

8. **2C-lite registry boundary**
   - Registry contains only mechanical rule metadata: stable `rule_id`, precedence, route/stop/recovery outcome, owner module and named typed predicates.
   - Predicate implementations remain in executable code; natural-language reasoning stays outside the registry.

9. **OR/Paseo retry boundary**
   - Runtime retries remain internal to orchestration-runtime/Paseo.
   - PW sees only semantic success/result or a real unresolved blocker; retry/session telemetry is not canonical PW state.

Challenge state: pending one bounded challenge for this accepted batch before all dependent choices are treated as stable exploratory state.

### Parallel Project Workflow Cards — reopened material choice

Current PWv2 has a one-Card invariant: at most one Project Workflow Card may be `in_progress` in a workstream.

PWv2.1 candidate direction requested by the user:
- permit multiple Cards in the same workstream to execute concurrently only when the accepted Plan/JIT decomposition explicitly marks them as parallel-safe;
- kernel must derive a bounded legal parallel set from canonical dependencies/authority and fail closed on overlap or uncertainty;
- OR/Paseo owns scheduling/execution of that legal set, not the legality decision;
- parallel Cards remain separate PW Cards with separate obligations/results/review subjects; runtime workers do not become Cards;
- avoid introducing a general scheduler or arbitrary lane machinery into PW.

Accepted exploratory choice: allow bounded plan-authorized parallel Cards, replacing the V2 one-Card invariant with a deterministic independence/parallel-set invariant.

Challenge state: GREEN. Parallelism is not inferred opportunistically by the kernel. Plan/JIT must explicitly declare a bounded parallel set plus the information needed to justify it; the kernel validates dependencies, declared write scopes, external effects and relevant overlap. Any uncertainty collapses the set back to serial execution.

### Parallel-card execution details

Accepted exploratory choices:

11. **Parallelism declaration and validation**
   - Plan/JIT explicitly declares bounded parallel sets; kernel does not invent concurrency solely from dependency absence.
   - Kernel validates declared parallelism against dependencies, declared write scopes, external effects and relevant authority/scope overlap.
   - Uncertainty or overlap fails closed to serial execution.

12. **Write-scope ownership**
   - Plan/JIT defines each Card's declared `write_scope` when materializing/refining the Card.
   - Kernel validates and compares scopes; it does not author them.

13. **Conflict after concurrent execution**
   - Do not auto-merge semantic conflicts.
   - A result whose relevant base/state has been invalidated by a competing accepted result becomes stale/conflicted and must be reconciled/re-routed.

14. **Execution isolation**
   - OR/Paseo should realize parallel Cards in separate execution worktrees/branches or equivalent isolated environments.
   - PW stores only semantic Card/result identity, not runtime worktree topology.

15. **Parallel review**
   - Independent reviews may run concurrently when their exact review subjects are independent.
   - Milestone/final integration still requires an integrated compatibility/acceptance check across the combined result.

### Parallel-set lifecycle choices

Accepted exploratory choices:

16. **Parallel-set authority location**
   - Plan/JIT durably declares the `parallel_set` as execution intent/contract.
   - Task Board stores only current Card execution state, not a competing source of concurrency intent.

17. **Single active membership**
   - A Card belongs to at most one active parallel set at a time.
   - Later stages may place the same logical work into a new set only after the earlier set/stage is complete or reconciled.

18. **Partial launch**
   - A parallel set means Cards are permitted to overlap, not that they must start simultaneously.
   - A legal subset may start when Plan/JIT does not require synchronized start and remaining prerequisites stay valid.

19. **Localized blocking**
   - A blocked Card stops itself and dependent successors, not automatically all independent Cards in the set.
   - A whole-set stop occurs only when Plan/JIT declares a shared gate or kernel detects a shared invalidating conflict.

20. **Integrated compatibility obligation**
   - After parallel Card results are composed, PW emits a distinct integration/compatibility obligation for the combined result before downstream milestone/final progression.
   - This obligation validates cross-Card compatibility and accepted integration behavior; it is separate from individual Card reviews.

Challenge state: pending one bounded challenge for this accepted batch before all dependent concurrency choices are treated as stable exploratory state.

### Parallel-set safety choices

Accepted exploratory choices:

21. **Structured write scope**
   - Card `write_scope` should be machine-checkable: repository paths/globs plus named external resources/effect domains.
   - Free text may explain intent but cannot be the only basis for concurrency validation.

22. **Overlap override**
   - Overlapping write scopes serialize by default.
   - Plan/JIT may explicitly authorize a bounded `parallel_override` only with exact overlap scope and rationale.

23. **Integrated compatibility timing**
   - Run the combined compatibility obligation before the first downstream obligation that consumes results from more than one Card in the parallel set.
   - Do not force it after every individual Card completion.

24. **Relationship to individual review**
   - Integrated compatibility review/check does not normally replace individual Card review.
   - It may cover individual reviews only when the exact combined review subject demonstrably covers each Card's full acceptance surface and satisfies independence.

25. **Concurrency limit ownership**
   - PW defines only the finite legal `parallel_set`.
   - Actual simultaneous worker/Card execution count is runtime policy owned by OR/Paseo, subject to budget/capability limits.

Challenge state: pending one bounded challenge for this accepted batch before all dependent concurrency choices are treated as stable exploratory state.

### Kernel interface and portability choices

Accepted exploratory choices:

26. **Authority bundle form**
   - Use exact refs/hashes plus deterministic materialization of required authority.
   - LLM summaries may aid navigation but never substitute for authority.

27. **Obligation/result versioning**
   - Version the typed interchange contract with explicit schema versioning and fail closed on unsupported breaking versions.

28. **ChatGPT ↔ Pi parity source**
   - The 2C-lite machine-readable registry is the shared mechanical-policy source.
   - Python executes it; helper-less ChatGPT reads the same registry plus semantic Markdown rather than relying on a separately maintained router copy.

29. **Kernel output form**
   - Stable machine-readable JSON is the canonical interface.
   - Human-readable rendering is optional and non-authoritative.

30. **OR mutation boundary**
   - OR/Paseo never directly mutates canonical PW durable state as a result of Card execution.
   - OR returns typed `Execution Result`; PW/coordinator validates and performs the governed canonical write + readback.

Challenge state: pending one bounded challenge for this accepted batch before all dependent choices are treated as stable exploratory state.

### User-facing behavior choices

Accepted exploratory choices:

31. **Automatic continuation**
   - PW continues automatically while the next legal obligation is deterministic and already authorized.
   - It stops only at real user/product/authorization/blocker boundaries.

32. **Agent-owned verification**
   - If uncertainty can be resolved by permitted research/readback/tools, PW resolves it without asking the user.
   - User questions are reserved for genuine user-owned decisions or unavailable required input.

33. **Human-facing output**
   - Normal user-facing responses stay concise: what happened, what it means, and what happens next.
   - obligation/result/fingerprint/internal telemetry remains in durable evidence or machine interfaces unless materially relevant.

34. **OR/Paseo visibility**
   - OR/Paseo remain implementation/runtime details during normal operation.
   - Surface them to the user only when a runtime-specific problem, decision or authorization makes them relevant.

35. **Automatic use of approved parallelism**
   - When accepted Plan/JIT already authorizes a legal parallel set, PW/OR may use it automatically without asking the user again.

Challenge state: pending one bounded challenge for this accepted batch before all dependent behavior choices are treated as stable exploratory state.

### Resilience and migration behavior choices

Accepted exploratory choices:

36. **OR/Paseo outage fallback**
   - If OR/Paseo is unavailable but the current obligation can be legally executed directly by ChatGPT, PW should continue without OR rather than block unnecessarily.

37. **Parallel-result conflict handling**
   - PW should attempt bounded safe reconciliation before escalating to the user.
   - User input is required only when the conflict becomes product/strategic/authorization-owned.

38. **Stale-result reuse**
   - A stale result is not automatically discarded.
   - PW first attempts safe reuse/rebase/reconciliation against current authority; repeat execution only when reuse cannot be proven safe.

39. **PWv2 -> PWv2.1 migration**
   - Prefer incremental migration at natural durable workflow boundaries rather than a flag-day cutover.
   - Existing PWv2 projects should remain recoverable during transition.

40. **Kernel/docs disagreement**
   - Fail closed on contradictory mechanical answers.
   - Do not guess which interpretation is intended; route to workflow recovery/fix before risky continuation.

Challenge state: pending one bounded challenge for this accepted batch before all dependent resilience/migration choices are treated as stable exploratory state.

### Runtime handoff and operational behavior choices

Accepted exploratory choices:

41. Independent workstreams may progress concurrently when they have no dependency/conflict.
42. A blocker in one independent workstream does not stop unrelated workstreams.
43. User-facing concurrency notices stay concise and Card/workstream-level.
44. If Cards prove not independent during execution, PW should collapse to safe serial continuation without user interruption when goal/authority do not change.
45. Workers must not silently repair out-of-scope findings; surface them for PW/JIT classification.
46. Tiny adjacent fixes may remain in-card only when clearly inside accepted goal/scope/risk.
47. Ordinary implementation defects found by review should route automatically through correction and re-review.
48. Review findings that challenge requirements/product authority route back to Definition/Brainstorming and user-owned decision when needed.
49. Research that invalidates planning strategy but not product intent routes automatically back to Planning.
50. Research that requires product-goal change routes to the user-owned decision boundary.
51. **Runtime handoff is user-directed, not auto-preferred.**
   - The user may tell the current Main/runtime to finish the current bounded obligation and produce the normal fresh-session locator prompt.
   - That same durable locator prompt may be opened in fresh ChatGPT or supplied to Paseo/OR.
   - PW semantics and legal continuation must be identical regardless of which runtime receives the handoff.
   - No canonical PW field selects a preferred runtime.
52. Worker-level telemetry remains non-canonical and is not part of normal PW progress reporting. Clarification pending only on how/where the user may optionally inspect OR/Paseo-native worker telemetry.
53. GREEN results from unaffected parallel Cards are preserved when another Card is RED.
54. Integrated compatibility failure should preserve valid Card results and create only bounded corrective integration work where possible.
55. Mandatory portability acceptance should include removing/ignoring OR/Paseo runtime state and proving that a fresh ChatGPT can reconstruct the same legal continuation from canonical repository state.

Challenge state: pending only for runtime-handoff/telemetry UX details; the remaining accepted choices are stable exploratory direction unless later evidence reopens them.

### Cross-runtime handoff choices

Accepted exploratory choices:

56. Prefer handoff at durable boundaries; if the user requests an earlier runtime switch, current runtime first persists a safe resumable state before handing off.
57. Use one runtime-neutral handoff/locator prompt for ChatGPT and OR/Paseo rather than separate prompt formats.
58. Handoff prompt stays locator-only: repo, branch/workstream, entry obligation and durable pointer; do not copy project history.
59. On continuation, current repository/Git state outranks any stale detail in the handoff prompt.
60. The user may switch ChatGPT ↔ OR/Paseo multiple times within one workstream.
61. Runtime switching does not mutate canonical Task Board semantics merely because the runtime changed.
62. Previous runtime identity is not canonical authority; retain it only as non-authoritative evidence when concretely useful.
63. After mid-Card runtime loss, fresh recovery checks for reusable durable/observable result before replay.
64. If execution completed but handoff/reconciliation was interrupted, recovery reuses valid result/evidence when provable.
65. **Superseded by 161-163.** OR may use bounded non-mutating helper lanes inside one Card, but the Card has one primary mutating Worker; multiple mutating owners require separate PW Cards.
66. OR must not erase the semantic boundaries of distinct PW Cards by merging them into one indistinguishable result.
67. **Single worker layer under OR/Main.** Workers may not directly spawn their own workers/subagents. A worker may request additional help from OR, and OR may start another sibling worker/helper within the same PW Card. Recursive/nested delegation is out of scope for the initial OR design.
68. **Superseded by 81/82/164.** Worker/reviewer model assignment is fixed by OR configuration; no silent mid-Card provider/model switching.
69. Provider/model failure is an OR runtime concern unless OR cannot complete the legal obligation and a real blocker remains.
70. A fresh runtime receiving the locator prompt should reconstruct and continue the exact legal obligation without asking the user what to do.

### Worker/review lifecycle corrections

User corrections reconcile PWv2.1 with already durable orchestration-runtime exploratory choices:

72. **Independent review coverage**
   - PWv2.1 should require an independent review for every Project Workflow Card and every Milestone.
   - OR does not invent this requirement; it executes the review obligation supplied by PW.
   - Challenge pending: this deliberately increases review cost/latency and should be retained only because the user values systematic verification over cheaper selective review.

81. **No automatic stronger-model escalation**
   - Normal worker/reviewer model assignment remains fixed according to OR configuration.
   - OR must not automatically upgrade to a stronger model because a Card looks difficult.
   - In an exceptional case where a stronger model appears genuinely necessary, Main may stop and ask the user for explicit approval.

82. **Fixed worker model is an invariant**
   - The configured worker model is fixed; no silent provider/model substitution or automatic mid-Card model switching.
   - If the configured model is unavailable or inadequate beyond normal repair/retry, OR fails closed or escalates to Main/user according to the runtime contract.

83. **One Card = one fresh Worker assignment**
   - A new PW Card gets a fresh Worker session/assignment.
   - The same Worker session persists through implementation and ordinary repair iterations for that same Card.
   - After that Card is terminal, the Worker is closed/archived; the next Card gets a new fresh Worker.
   - This preserves bounded context and prevents cross-Card contamination while avoiding needless rediscovery during repair loops.

### Worker operation choices 71-85

Accepted exploratory choices, reconciled with later corrections:

71. **Superseded by 161-163 for mutation.** OR may add bounded read-only/advisory helpers within a Card, but one Card has one primary mutating Worker.
72. Every PW Card and every Milestone requires independent review. Each new Card gets a fresh independent Reviewer assignment; each Milestone gets its own fresh independent Reviewer.
73. Implementing Worker may self-test but cannot satisfy its own formal independent review.
74. Reviewer for a Card starts only after an exact review subject/result is frozen; implementation and formal review of the same subject do not run concurrently.
75. OR may replace a struggling Worker without user input when scope/authority remain unchanged.
76. Duplicate competing mutating Workers for one Card are not allowed under 161-163. Comparative read-only/advisory lanes may be used when explicitly useful without creating competing mutation ownership.
77. Worker-proposed architecture changes outside Card scope return to PW rather than being accepted by OR.
78. Worker may choose among legally available tools/extensions/MCP capabilities inside its bounded assignment.
79. Missing tooling should first be handled within OR/runtime alternatives; escalate only a real unresolved blocker.
80. Concrete model identity is runtime detail, not PW canonical state.
81. No automatic stronger-model escalation; exceptional stronger-model use requires explicit user approval (later correction).
82. Worker/reviewer model assignment is fixed by OR configuration; no silent mid-Card model/provider switching (later correction).
83. One PW Card gets one fresh Worker assignment; the same Worker continues through ordinary repairs for that Card; next Card gets a fresh Worker (later correction).
84. Worker receives only the authority/context needed for its bounded Card, not the entire project/Plan by default.
85. OR/Main may hold broader coordination context than Workers, but may not become a second source of PW authority.

### Review/recovery choices 86-100

Accepted exploratory choices:

86. After Card review GREEN, PW continues automatically to the next legal Card without user confirmation.
87. When all Cards in a Milestone are ready, PW automatically launches Milestone review.
88. Card review RED enters automatic repair/re-review while the defect remains implementation-local and within accepted scope.
89. Repair loops are bounded; after the configured failure ceiling Main analyzes cause and escalates only when a real user-owned decision remains.
90. Milestone review findings should create only the bounded corrective work needed rather than rolling back an entire Milestone by default.
91. GREEN Milestone advances automatically to the next legal Milestone unless an explicit user gate exists.
92. PW may materialize missing Cards/JIT work that is necessary to realize the already accepted Plan without changing product goal/scope.
93. Work that expands product goal/scope requires return to a user-owned decision boundary.
94. Ordinary defects discovered in review remain repair work for the affected Card rather than automatically becoming separate Cards.
95. Milestone review is performed by a fresh independent Reviewer that did not implement or review the constituent Cards; Reviewer identity is not reused from any Card review in that Milestone.
96. **Fresh Milestone Reviewer must not receive prior Card-review opinions/verdict rationales by default.** It receives the canonical Milestone subject, accepted authority, relevant Card outputs/artifacts, and the raw/required test evidence needed to independently verify the Milestone. Prior review conclusions are not used as anchoring context; they may be consulted only through an explicit bounded investigation when a known issue requires it.
97. A GREEN verdict lacking required evidence is invalid and must fail closed.
98. A temporarily unexecutable required test does not become deferred GREEN unless the accepted Plan already defines an allowed alternate verification path.
99. Every User Stop should concisely state why PW stopped and the exact user input/authorization needed.
100. Fresh ChatGPT/Paseo after an arbitrary pause must be able to reconstruct and continue from repository state alone; this is a core PWv2.1 acceptance property.

### Fresh-review identity refinement

Accepted exploratory refinement, preserving the existing PWv2 semantic-independence rule:

- **Every new Card review subject gets a fresh independent Reviewer assignment.** A Reviewer from a different Card is not reused for the new Card.
- **Every Milestone review gets a fresh independent Reviewer assignment** that did not implement or review the constituent Cards.
- **Same-Card OR/Paseo repair loop:** when the Worker repairs its own Card after RED, the same Reviewer that previously reviewed that Card may recheck the repaired exact subject, provided that Reviewer did not materially produce/repair the new subject. This preserves reviewer continuity without violating independence.
- **ChatGPT-only corrective path:** a ChatGPT review context may participate in corrective implementation if the router legally returns it to corrective execution, but once that context materially repairs the subject it becomes ineligible to issue the next independent verdict on that repaired subject. The next review therefore requires a fresh independent context.
- The underlying invariant is subject-relative semantic independence, not provider/session naming: `produced_or_repaired(subject) => cannot_independently_review(subject)`.

PWv2 baseline verification: current `workflow/REVIEW.md` already states that a context which materially produced or repaired the exact subject cannot issue its independent verdict; changed reviewed subject/new verdict attempt is a new attempt.

### Review, reopening, recovery and stop UX choices 101-115

Accepted exploratory choices:

101. RED Card review should return concrete findings plus the evidence/conditions required for recheck.
102. The Worker repairing a RED Card sees the prior review findings for that same Card.
103. The same Reviewer rechecking the same Card may see its own prior RED findings and verify their correction, provided it did not materially repair the subject.
104. A fresh Reviewer for a new Card does not receive prior Card-review opinions by default; only subject-relevant canonical authority/evidence.
105. A previously GREEN Card may be reopened when new evidence genuinely invalidates its prior result/assumptions.
106. A reopened Card gets a fresh Worker assignment for the new repair cycle.
107. A reopened Card gets a fresh independent Reviewer assignment.
108. If an earlier defect may invalidate later Cards, PW marks affected downstream results potentially stale rather than assuming prior GREEN remains valid.
109. After repairing an earlier Card, PW determines which downstream Cards/tests/reviews require revalidation.
110. Revalidation is bounded to the actually invalidated acceptance surface; it does not imply redoing unaffected work from zero.
111. Successful automatic Recovery may be surfaced briefly to the user but should not create a stop.
112. If durable Plan/authority already selects the legal continuation, Recovery follows it without asking the user again.
113. If multiple legal continuations remain, PW may choose among purely technical equivalents; product/strategy differences return to the user.
114. **User Stop formatting is stop-type specific, not always an authorization phrase.**
   - Ordinary authorization stop: give the smallest explicit action, ideally a ready short phrase the user can approve.
   - Optional fresh-context handoff (for example Premium A/C): user may continue here, but the response must also include a ready-to-copy runtime-neutral `NEW CHAT START PROMPT`.
   - Mandatory fresh independent handoff (for example Premium B, or an independent-review boundary where the current context produced/repaired the exact subject and no internal qualifying reviewer exists): the legal next action is to start a fresh context/harness, and the response must include the ready-to-copy locator prompt.
   - End-of-scope or informational stop may require no authorization template at all.
115. After the user supplies the required authorization/input, PW reruns the router and continues until the next real workflow stop.

Baseline note: this matches current PWv2 `workflow/USER_STOP.md`, which distinguishes ordinary user-action stops from optional Premium A/C fresh handoffs and mandatory Premium B fresh independent handoff.

### Milestone and final-integration review choices 116-130

Accepted exploratory choices:

116. Milestone-review corrections should route back to clearly identified existing Cards or bounded new Cards rather than unstructured global repair.
117. A Milestone review may cause a new Card to be materialized when the missing work is still within the accepted Plan.
118. If the discovered work changes product goal/scope, PW stops at the appropriate user-owned authority boundary.
119. Repairing one Card after Milestone review does not automatically force re-review of every Card; only materially affected Cards are revalidated.
120. The same Milestone Reviewer may recheck the repaired Milestone if that Reviewer did not materially produce/repair the changed subject.
121. If the Milestone Reviewer materially repairs the subject, it loses eligibility to issue the next independent verdict; a fresh Reviewer is required.
122. Final integration review of the completed workstream is a separate fresh independent review beyond Card and Milestone reviews.
123. Final integration Reviewer receives the exact final subject, authority and raw/relevant evidence, not prior GREEN opinions as anchoring context.
124. Final integration review may invalidate an earlier GREEN Card/Milestone when new evidence shows a real defect.
125. Final integration RED routes automatically to bounded corrective work when product goal/scope remain unchanged.
126. PW must mechanically enforce reviewer freshness/semantic independence rather than relying on prompt convention alone.
127. If the current runtime cannot provide a qualifying fresh Reviewer, PW produces the required fresh-context locator handoff.
128. Switching ChatGPT ↔ Paseo does not change review requirements or acceptance semantics.
129. Out-of-scope-looking review findings are classified rather than blindly discarded: blocker, needed in-scope work, or true out-of-scope note.
130. Workstream close is permitted only after GREEN final integration review and all required acceptance evidence are satisfied.

### PWv2 -> PWv2.1 migration choices 131-145

Accepted exploratory choices:

131. PWv2.1 should continue active PWv2 workstreams without a manual migration ceremony when legacy durable state is unambiguous and safely interpretable.
132. Ambiguous legacy state must fail closed to Recovery rather than be guessed.
133. An active PWv2 Card may continue under PWv2.1 only after validating that its authority, subject and evidence can be bound unambiguously to the new contract.
134. Migration is lazy/on-entry at natural workstream boundaries rather than a flag-day migration of every repository.
135. Historical PWv2 GREEN remains valid when its exact subject/evidence still proves the accepted result; do not re-review without cause.
136. A historical GREEN that lacks newly required evidence is not retroactively RED; route to bounded revalidation when that evidence becomes material.
137. New review semantics apply to continued active work, but do not automatically reopen correctly closed historical stages.
138. Missing historical Milestone review is backfilled only when that Milestone remains material to the active continuation path, not as blanket retroactive cleanup.
139. PWv2.1 may mechanically add missing durable fields when their values are uniquely derivable from existing canonical state.
140. A new durable field whose value requires semantic interpretation or a user decision cannot be invented; route to Recovery or the owning user gate.
141. Preserve historical records and apply minimal migration rather than rewriting project history into a new format.
142. Valid old-format results should be normalized/adapted into the new contract rather than rejected solely for serialization/version age.
143. Safe mechanical migration should not itself create a user stop.
144. Contradictions among legacy manifest/Task Board/Git state must not be resolved by probability or convenience; fail closed to Recovery.
145. Migration acceptance must include real PWv2 workstreams in multiple lifecycle states and prove correct PWv2.1 continuation/recovery.

Challenge state: migration batch accepted; adversarial validation still required before Definition promotion.

### Adversarial closure batch 146-160

Accepted exploratory choices and challenge resolutions:

146. Parallel sibling results are revalidated against relevant changed inputs before acceptance; affected results become stale/revalidation-bound rather than blindly integrated.
147. A result completed against an older workstream state is accepted only after proving intervening commits did not invalidate its relevant preconditions.
148. Handoff prompts are locators only; current canonical Git state always outranks stale prompt narrative.
149. Loss of all OR/Paseo sessions/state must not prevent project recovery from canonical repository/PW state.
150. Unknown external side-effect completion after crash requires readback/reconciliation before any retry; no blind duplicate effect.
151. A reviewer contaminated by Worker transcript/context does not satisfy a fresh-independent-review requirement; launch a clean reviewer.
152. Any post-GREEN mutation changes the exact subject; if the prior Reviewer made that mutation it also becomes ineligible to independently verdict the new subject.
153. Fresh Milestone review should not be anchored by prior Card GREEN verdicts; provide current subject/authority/raw evidence instead.
154. Mechanical-kernel versus semantic-document contradiction routes to workflow Recovery; never silently choose one interpretation.
155. Helper/router unavailability must not block legal continuation when canonical repo contracts are sufficient; fresh ChatGPT can reconstruct manually.
156. Helper/manual route disagreement is a parity/contract defect, not an ignorable mismatch; repair workflow before risky continuation.
157. Ambiguous migration blocks only the dependent path; independent workstreams/Cards may continue.
158. Valid sibling results in a parallel set are preserved when another sibling blocks/fails unless a dependency/invalidation reaches them.
159. Final integration incompatibility creates bounded integration correction first; constituent Cards are reopened only when evidence assigns the defect to them.
160. Definition readiness requires the destructive recovery thought-test: discard chat memory, OR state and helper cache, then prove canonical Git alone identifies the exact legal continuation.

Challenge outcome: GREEN for the major stale-state, runtime-loss, reviewer-freshness, migration-locality, integration and helper-parity failure classes covered by this batch. Remaining Brainstorming work is limited to final policy-registry parity details and synthesis/cleanup unless a new contradiction is found.

### Policy-kernel closure batch 161-175

Accepted exploratory choices:

161. **One Card = one primary mutating Worker.** OR must not fan one PW Card/Execution Obligation out across multiple concurrent mutating Workers. If implementation is materially parallelizable, Planning/JIT should model the independent mutation units as separate Cards in an authorized parallel set.
162. The Card Worker may request bounded read-only/advisory help (for example Scout/Researcher/test investigation) through OR. Helpers do not become additional mutating owners of the Card.
163. Earlier exploratory allowance for multiple mutating Workers inside one Card is superseded. A Card that genuinely needs multiple independently mutating owners should be split into Cards rather than hidden inside runtime fan-out.
164. Fixed worker-model resolution remains fail-closed: no silent fallback to another model/provider.
165. Helper-less ChatGPT must reconstruct the legal route from canonical repository contracts rather than escalating merely because confidence is lower; only an actual contradiction/ambiguity is Recovery.
166. Mechanical policy must not be independently duplicated in machine registry and prose condition trees. Mechanical facts/rules need one canonical representation with checked/documented semantic projection.
167. Changes to a mechanical rule must have tests/contract checks that detect stale human-facing documentation or references where mechanically verifiable.
168. Markdown changes that contradict mechanically checkable policy must be caught before merge where feasible; otherwise parity tests must fail closed at runtime/recovery.
169. Do not move all Project Workflow semantics into a general YAML/TOML workflow DSL. The machine-readable layer remains deliberately small and mechanical.
170. Rules requiring semantic interpretation of intent/product meaning remain owned by the appropriate LLM role/module, not the deterministic kernel.
171. Acceptance testing must compare representative canonical repo states across executable helper and helper-less fresh ChatGPT and require the same legal next obligation/stop.
172. Parity fixtures must include RED/recovery, fresh-review boundaries, parallel Cards, migration from PWv2 and other high-risk states.
173. A PWv2.1 feature that is only recoverable/understandable through the Python helper and cannot be reconstructed from canonical contracts is rejected.
174. Serialization/file-format details of the small policy registry are implementation choices for Definition/Planning unless they change user-visible semantics or authority.
175. After this batch, Brainstorming should move to a bounded completion audit/final challenge pass rather than another broad grilling cycle.

Supersession note:
- Earlier choices 65 and 71 that could be read as permitting several mutating Workers inside one Card are superseded by 161-163. OR may still use bounded non-mutating helpers inside a Card.
- Earlier choice 68 permitting runtime model/provider switching is superseded by the later fixed-model choices 81/82/164: no silent model/provider substitution.
- Issue `chatgpt-codex-project-workflow#56` is resolved by rejecting internal mutating fan-out within a single Card; legal mutation parallelism is represented as multiple PW Cards in an explicitly authorized parallel set.

Challenge outcome: GREEN for the remaining policy-kernel portability/parity direction, subject to final completion audit.

### Completion audit — final unresolved material questions

The bounded completion audit found six remaining material questions. They are intentionally limited to contradictions/simplifications that could still change Definition:

176. Whether parallel integrated compatibility may ever replace mandatory per-Card independent review.
177. Whether `parallel_override` should exist for overlapping mutating write scopes or overlapping mutation should always serialize.
178. Whether optional worker-level telemetry UX should be fully deferred to orchestration-runtime and removed from PWv2.1 scope.
179. Final challenge of the mandatory review stack: every Card + every Milestone + final workstream integration review despite added cost/latency.
180. Whether fresh-review obligations may be satisfied automatically by a new internal independent OR/Paseo reviewer without a user stop.
181. Whether every executable mechanical predicate must have a canonical human-readable contract sufficient for helper-less recovery, so no legal routing semantics exist only in Python code.

A small additional synthesis issue is already non-product: stale "challenge pending" labels and historical decision-tree text must be reconciled after these questions; no user choice is required for that cleanup.


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


### Execution Result contract

User choice accepted during Brainstorming: C / typed semantic `Execution Result`.

The runtime return should contain only Project-Workflow-relevant semantic result data, such as:
- exact obligation/subject binding;
- result subject/status;
- changed artifacts or exact result refs;
- tests/evidence/readback outcomes;
- blocker or semantic outcome needed for PW continuation.

It should not make provider/model/worker/session/retry/worktree/Paseo telemetry canonical PW state.

Challenge state: GREEN. The user accepted exact obligation binding plus a fingerprint of the canonical derivation inputs/current relevant Git state. PW must validate freshness before accepting the result; stale results cannot be accepted blindly and must be re-routed/reconciled against current canonical state.

### Result freshness / stale-result protection

Stable exploratory choice: bind each typed `Execution Result` to the exact obligation identity plus a fingerprint of the canonical inputs that determined that obligation. Before accepting a result, PW verifies the current relevant canonical state against that fingerprint. A mismatch is stale and requires re-derivation/reconciliation rather than blind acceptance.

### Authority-bundle ownership

Stable exploratory choice: PW owns authority resolution and bundle construction.
- PW kernel determines the applicable authority, validates exact refs/hashes and materializes the bounded safe subset plus every required `must-open` source into the handoff package.
- OR/Paseo receives and transports the already-resolved package to workers.
- OR/Paseo must not infer, add, drop or reinterpret which Project Workflow authority applies.
- This keeps authority selection in PW while allowing OR/Paseo to own delivery, execution topology and runtime mechanics.

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

Brainstorming is now in closure-oriented grilling. Most user-visible behavior, review/recovery semantics, runtime handoff, concurrency, and PW↔OR boundaries have accepted exploratory direction.

Remaining material fronts:

1. **Mechanical policy truth / 2C-lite parity.**
   - Freeze how the small machine-readable mechanical registry, Python predicates and semantic Markdown remain mutually consistent without creating a workflow DSL.
   - Prove helper-less ChatGPT can reconstruct the same legal route.

2. **Adversarial challenge closure.**
   - Run bounded failure challenges against the accepted batches that are still marked challenge-pending, especially parallel-set lifecycle, mechanical-policy drift, mutation/readback, runtime handoff and review cost/freshness.

3. **Migration and compatibility edge cases.**
   - Confirm PWv2 -> PWv2.1 transition behavior for active workstreams, reopened Cards, stale results and mixed old/new durable records.

4. **Small operator/UX details.**
   - Optional OR/Paseo worker telemetry visibility and a few real-stop/handoff edge cases that do not alter authority.

5. **Definition readiness synthesis.**
   - Reconcile duplicate/superseded brainstorming notes, mark stable exploratory choices, identify explicit rejects/open questions, and determine whether any Research is still required.

Expected remaining grilling should be a small number of focused batches, not another full architecture discovery cycle.

These remain Brainstorming questions, not requirements/decisions.

## Definition promotion

- Definition promotion authorization: pending
- Definition promotion subject: none

Do not enter Project Definition until the user explicitly authorizes promotion of this exact scope/revision.
