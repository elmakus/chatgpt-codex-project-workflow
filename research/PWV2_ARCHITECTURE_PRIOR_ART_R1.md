# Research — PWv2 architecture prior art

Date: 2026-09-23
Research question: Which mechanisms from pi-fabric, Laya/System One, Dagu-style deterministic workflow/state-machine orchestration, and rpiv-todo could materially improve the current PWv2 while preserving its existing durable authority model?

## Durable continuation metadata — chatgpt_only

Research ID: pwv2-architecture-prior-art-r1
Status: complete
Origin role: brainstorming
Origin subject: pwv2-architecture-prior-art@R1
Return target: brainstorming:pwv2-architecture-prior-art@R1
Return reconciliation: applied
Return reconciliation result: brainstorming/PWV2_ARCHITECTURE_PRIOR_ART_R1.md@blob:718586457e74f419de9285155f77ec4d5b3e6163

## Scope and hard constraints

This research investigates only the four user-specified prior-art areas and compares them against current PWv2. It does not implement changes, does not design a complete PWv3, and does not promote findings into accepted requirements, decisions or planning.

The existing PWv2 authority model is a hard constraint:
- WORKSTREAM.yaml remains canonical for workstream identity and pre-execution routing pointers.
- The selected Task Board remains canonical mutable Card/milestone execution state.
- Task Cards remain stable bounded work-package contracts.
- requirements/, decisions/, approved planning, review evidence and Git remain canonical durable authority.
- Session memory, UI state, classifier output, an external workflow engine, Fabric state, or a derived graph/cache must never become an independent authority source.

## Source snapshot

### Current PWv2 baseline

Repository base inspected: elmakus/chatgpt-codex-project-workflow main@7aa7512ead67a86256089d1af0171e2e655e700d.

Primary current contracts inspected:
- PROJECT.md
- CHATGPT.md
- workflow/CONTEXT_ROUTING.md
- workflow/common/AUTHORITY.md
- workflow/common/RESEARCH.md
- workflow/chatgpt_only/ROUTER.md
- workflow/chatgpt_only/WORKSTREAMS.md
- workflow/chatgpt_only/INTAKE.md
- workflow/chatgpt_only/BRAINSTORMING.md
- workflow/chatgpt_only/RESEARCH.md
- workflow/chatgpt_only/STATE.md
- workflow/chatgpt_only/TASK_CARDS.md
- workflow/chatgpt_only/TASK_CARD_TEMPLATE.md
- workflow/chatgpt_only/WORKSTREAM_TASK_BOARD_TEMPLATE.yaml
- workflow/chatgpt_only/REVIEW.md
- workflow/chatgpt_only/EXECUTION.md
- workflow/chatgpt_only/CONTEXT_HEALTH.md
- docs/audits/CHATGPT_ONLY_ROLE_TRANSITION_REVIEW_STATE_MACHINE.md
- representative implementation/workstreams/*/TASK_BOARD.yaml records
- repository test/tree inventory.

Size observation at the inspected base:
- ROUTER.md: 352 lines / 29,838 chars.
- WORKSTREAMS.md: 461 lines / 34,784 chars.
- STATE.md: 274 lines / 15,591 chars.
- TASK_CARDS.md: 105 lines / 4,182 chars.
- RESEARCH.md: 104 lines / 7,936 chars.
- REVIEW.md: 120 lines / 9,021 chars.
- CONTEXT_HEALTH.md: 94 lines / 5,565 chars.
- EXECUTION.md: 195 lines / 14,410 chars.

These files are not all supposed to be loaded at once; PWv2 already uses progressive disclosure. The numbers matter because legal routing still depends on repeated interpretation of substantial Markdown modules and exact durable records.

### Prior-art repositories / docs pinned during research

pi-fabric:
- repository: https://github.com/monotykamary/pi-fabric
- inspected main: 0c742a021e229602626ca76b6db5e831f38cb258
- key sources: README.md, docs/providers.md, docs/architecture.md, docs/configuration.md, docs/compaction.md, docs/audit-trace.md, skillsets/typescript/fabric-exec/SKILL.md.

Laya / System One:
- Laya: https://github.com/NandhaKishorM/laya
- inspected main: 010bacef009c855ccba814b51f7c8e1d38ab5e3f
- System One Lite: https://github.com/snellingio/system-one
- inspected main: 8ca10fd7dda8ad7db4b88af64b27e61452dd3716
- key sources: Laya README/router/tests/calibration material; System One README, docs/how-it-works.md, docs/confidence.md and API docs.
- calibration caveat source used as secondary evidence: https://huggingface.co/convaiinnovations/laya/discussions/3. This is an external evaluation/discussion, not upstream authority, and is treated only as a warning that project-specific calibration must be measured rather than assumed.

Dagu:
- engine: https://github.com/dagucloud/dagu
- inspected main: f8e5c27ce6d94e65bc72ce2c340e6775f2e99083
- docs: https://github.com/dagucloud/docs
- inspected main: 8e1412bd057fcbc754c5c7eb141ebae2f9dd29d1
- key sources: dependency/runtime plan implementation, YAML specification, Durable Execution, Approval, Human Tasks, Sub-DAGs, Harness output_schema docs, build-workflow dependency validation.

rpiv-todo:
- current monorepo: https://github.com/juicesharp/rpiv-mono
- inspected main: d74b1c99830a565f3df3f37e0a36616d17ffc574
- archived original: https://github.com/juicesharp/rpiv-todo
- key sources: packages/rpiv-todo/docs/tool-schema.md and overlay.md.

## Current PWv2 baseline findings

PWv2 already solves several problems that the prior-art projects solve in other ways:

1. Durable recovery is repository-first. Exact workstream/branch identity, research pointers, review subject/evidence, Card state and result refs survive a session boundary. A fresh chat can reconstruct legal work from Git-backed state.
2. Progressive disclosure exists. The router directs the agent to the smallest relevant role module and exact durable records instead of treating the whole repository as prompt context.
3. Role isolation is explicit. Task Cards carry bounded authority slices. Required/recommended independent review is a real fresh-chat boundary; an implementing chat cannot review its own reviewed subject.
4. Task dependencies already exist semantically. Task Cards have Dependencies and selected Task Boards have depends_on entries; readiness requires dependencies complete.
5. The gap is executable enforcement. The current repo contains Markdown routers/contracts plus contract tests, but no executable chatgpt_only router/state-transition implementation that deterministically computes every next role from canonical durable state.
6. The dependency model is not currently a first-class validated graph. Existing contracts specify dependencies/readiness, but the inspected current tree does not expose a dedicated cycle detector/topological ready-queue validator for Task Board/Card dependencies.
7. Recovery is deterministic at the durable-state level but the reconstruction/routing step is still interpreted by the LLM. This is a different problem from persistence itself.
8. Context pressure is reduced by progressive disclosure, but repeated router/contract reads and large raw tool results can still consume main-model context.

## 1. pi-fabric

### How the mechanism works

pi-fabric exposes one programmable model-facing tool, fabric_exec. The model writes a checked TypeScript program (or configured Python kernel) that invokes Pi core tools, MCP tools, captured extension tools and Fabric providers through a host bridge. Branches, loops, Promise.all fan-out and data-flow happen inside the guest program. Only the program's returned value needs to enter the main model context; nested activity remains separately observable/auditable.

Capability discovery is demand-driven:
- known actions can use concise direct provider proxies;
- extension names can be exposed as a names-only roster;
- tools.search finds likely action refs;
- tools.describe returns the full action descriptor/schema;
- tools.call invokes a discovered/computed ref;
- discovery does not grant permission; each call still passes normal registry/approval/lifecycle checks.

Fabric also bounds/projection-manages nested results and traces. Its docs distinguish rich live/audit detail from bounded durable trace projections, and its compaction layer preserves structured facts/addresses while allowing arbitrary old prose/tool-output bodies to disappear from the inline model view.

Important non-adoption boundary: Fabric's agent runtime, actors, workflows, mesh and durable coordination are outside the useful minimum here. PWv2 already has its own authority/lifecycle model; importing those as workflow authority would create a competing state system.

### Which PWv2 problem it could solve

- Large model-facing tool schema surfaces.
- Repeated model round-trips for search/read/filter/reduce sequences.
- Huge intermediate outputs entering the primary transcript.
- Fan-out research/tool work that is mechanically composable.
- Bounded role workers needing only a small capability surface.

### What PWv2 already does instead

PWv2 already performs workflow-level progressive disclosure: route first, then read only the role module and exact authority records. It also persists durable evidence outside session memory. That helps workflow context but does not solve runtime tool-schema sprawl or intermediate tool-result growth inside a role.

### Real improvement or added complexity

Real improvement if adopted narrowly as a runtime/execution primitive:
- on-demand tool discovery is directly useful;
- read-only code-mode composition can materially reduce transcript/tool-roundtrip pressure;
- typed schemas/checking reduce argument-shape errors.

Full Fabric orchestration would mainly add complexity and duplicate PWv2 authority.

### Context usage impact

Potentially strong reduction. A names-only capability roster plus search/describe avoids injecting every tool schema. Multi-call code mode lets raw search/read results be filtered/aggregated inside the guest and returns only a bounded product to Main.

The saving is not automatic: a Fabric program can still return too much data, and rich traces/audits still exist. PWv2 would need an explicit rule that only the bounded role result/evidence references cross back into the reasoning context unless expansion is needed.

### Determinism / recoverability impact

Positive for call-shape determinism because the program is type/schema checked before execution. Negative or neutral for workflow recovery unless carefully bounded: imperative code can make partial side effects, Promise.all is not a transaction, and runtime traces are not PWv2 authority.

Safe fit requires: Fabric/runtime state is disposable; any durable workflow transition/result still gets committed to canonical repo files before the router advances.

### Role isolation / independent review impact

Can improve role isolation by exposing only an allowlisted capability surface to a bounded worker. It must not replace the fresh independent reviewer boundary. A reviewer may use the same runtime mechanism, but it must start from its canonical fresh review package and not inherit implementation narrative/runtime-private state.

### New failure modes

- Partial completion of fan-out where sibling calls have side effects.
- Hidden or over-compressed intermediate evidence causing a false conclusion.
- Stale/discovered ref or schema mismatch.
- Over-broad capability allowlist.
- Sandbox/native escape configuration risk.
- Treating runtime trace, agent memory or mesh state as durable workflow authority.
- Main context loses evidence needed by a reviewer if only an opaque summary survives.

### Fit

- On-demand capability search/describe: PWv2 low-risk incremental candidate.
- Read-only/code-mode tool composition with bounded returned output: PWv2 low-risk incremental experiment.
- General executable tool-composition layer for write-heavy roles: PWv2 architectural refactor.
- Fabric agents/workflows/mesh as authority: reject.

## 2. Laya / System One

### How the mechanism works

The shared idea is non-free-form typed judgment over a closed answer space.

System One Lite gives the clearest mechanical description:
1. Format state, instructions and allowed answers.
2. Encode allowed answers as answer tokens/codes.
3. Run the model to a fixed answer position without generating text.
4. Keep logits for valid answer codes only and apply softmax.
5. Map the resulting probability distribution back to declared labels.

Choice returns the top label plus probabilities. Score returns a probability distribution over ordered levels and a probability-weighted numeric score. Noul returns a yes probability.

System One Lite's Choice/Score confidence is a concentration statistic:
confidence = (max_probability - 1/n) / (1 - 1/n).
It measures how peaked the permitted distribution is, not probability of correctness.

Laya uses encoder checkpoints for typed choice/score/noul decisions in a single forward pass and has a Router that selects an appropriate checkpoint per request using explicit model/task/language signals and detection/default rules. Laya's training/materials emphasize proper scoring rules and post-hoc calibration. Its own reported typed-decisions benchmark still has non-zero ECE, and its base checkpoints are substantially weaker on the same benchmark. A recent independent zero-shot evaluation reports severe confidence miscalibration and option-order sensitivity on its suite. That secondary result is not a universal verdict, but it makes one engineering rule unavoidable: PWv2 cannot treat model confidence as calibrated until measured on its own labeled routing/classification distribution.

### Which PWv2 problem it could solve

- Cheap bounded classification where the legal answer set is already known.
- Evidence relevance/severity buckets.
- Tool/model selection among a prevalidated legal set.
- Deciding whether bounded work should escalate to a larger semantic model.
- Potentially reducing expensive-model context by turning a large-but-bounded classification input into a tiny typed result.

### What PWv2 already does instead

Today the normal reasoning model interprets the router/contracts and classifies semantic situations itself. Deterministic hard conditions exist in prose, but semantic classification and hard routing are not separated into distinct runtime layers.

### Real improvement or added complexity

A real improvement only for narrow semantic judgments with closed labels and strong fallbacks. It is not a safe replacement for the authoritative router.

A small classifier would be overengineering when:
- the decision is already fully deterministic from durable fields;
- the input is small enough that the current role model must read it anyway;
- a wrong answer could skip an authority/review/user gate;
- no labeled project-specific evaluation set exists.

### Context usage impact

Potentially positive when the classifier can consume a bounded payload directly and return a few probabilities without injecting the raw material into the main role model. It gives little or no context benefit if Main must first read/interpret the same material to construct the question.

### Determinism / recoverability impact

Output format is more deterministic than free-form generation, but semantic correctness remains probabilistic. Recovery is safe only if the classifier result is disposable/recorded as evidence, while the durable route remains reconstructible from canonical repo state.

For hard workflow transitions, classifier output must be validated against deterministic legal-transition constraints. Low confidence, malformed input, OOD state or model failure must fail closed to the larger model/manual semantic path, never to an automatic authority-changing action.

### Role isolation / independent review impact

Useful inside a role for bounded triage. Unsafe if used to:
- issue a review verdict,
- waive or create an independent-review boundary,
- decide that implementation may change accepted authority,
- decide a user/product approval is unnecessary.

Fresh independent review must remain a separately instantiated reviewer over the exact canonical review subject.

### New failure modes

- Confidence mistaken for correctness probability.
- Calibration drift after model/checkpoint/question changes.
- Option-order sensitivity.
- Closed label set omits the correct/unknown class.
- OOD input appears highly confident.
- Long state exceeds model context window.
- Classifier and authoritative router disagree.
- Threshold tuned on synthetic or unrepresentative data.
- Silent model/version change alters routing.

### Fit

- Bounded advisory classification and model/tool escalation experiments: PWv3 prior art, with a possible PWv2 shadow-mode experiment.
- Classifier as authoritative PWv2 router: reject.
- Confidence-only auto-waiver of review/user/authority gates: reject.

## 3. Dagu and deterministic workflow/state-machine patterns

### How the mechanism works

Dagu compiles declarative workflow steps and depends edges into an execution plan. Ready steps are selected from dependency state; graph execution naturally permits fan-out. Current Dagu explicitly checks acyclicity; its runtime implementation uses Kahn's algorithm for cycle detection.

Relevant mechanisms:
- explicit dependency DAG and deterministic ready-state computation;
- step retries and whole-DAG retries with separate semantics;
- sub-DAG composition and persisted child runs;
- human tasks and post-step approval gates that enter a Waiting state;
- structured output_schema: stdout must decode as JSON and match an inline JSON Schema or the step fails before publishing downstream outputs;
- harness.run can execute coding-agent CLIs as bounded workflow steps;
- persisted run history/status enables inspect/retry/resume behavior;
- parallel child runs and bounded concurrency.

Dagu also has AI-oriented decision/agent features, but those are not necessary for the prior-art value here. The key pattern is deterministic orchestration around bounded LLM workers.

### Which PWv2 problem it could solve

- Repeated LLM interpretation of ROUTER.md and lifecycle contracts.
- Deterministic next-obligation selection.
- Explicit state-transition validation.
- Crash/restart continuation without asking a model to re-derive obvious finite-state transitions.
- Structured role handoffs with schema validation.
- Retry semantics and explicit approval barriers.
- Dependency/cycle enforcement.

### What PWv2 already does instead

PWv2 already has:
- one policy router as conceptual transition owner;
- canonical durable workstream/Task Board/review/research pointers;
- exact route/return targets;
- fresh review gates;
- fail-closed recovery semantics.

The difference is execution: PWv2's current transition rules are primarily Markdown interpreted by the model. Dagu turns equivalent finite parts into executable state-machine/DAG behavior.

### Real improvement or added complexity

This is the largest plausible architectural improvement in the research, but it is not low-risk.

A deterministic executable router could remove a large class of repeated interpretation and stale-context failures. However, PWv2 has semantic branches that cannot be reduced safely to simple status fields without either:
- retaining a semantic LLM classifier/role for those branches, or
- redesigning the state schema so the needed facts are explicit.

Blindly translating ROUTER.md into another workflow engine would create two implementations of the same policy and increase drift risk.

### Context usage impact

Potentially very large reduction. If a deterministic router reads canonical records and emits one exact next obligation plus a bounded role context package, the role model no longer needs to repeatedly ingest/interpret the full policy router and unrelated lifecycle modules.

The benefit depends on one-source discipline: if the agent must also re-read the Markdown router to verify the executable router every time, context use becomes worse, not better.

### Determinism / recoverability impact

Strongly positive if:
- the executable transition logic is versioned with the workflow;
- it consumes canonical repository state;
- every durable state mutation remains in canonical files/Git;
- its own database/history is treated only as a cache/log;
- it fails closed on unknown/invalid states;
- crash-injection proves restart from repository state alone.

Potentially negative if engine-local status becomes necessary to know the next legal step.

### Role isolation / independent review impact

Can improve isolation: the orchestrator can launch a bounded worker with only the exact Card/authority slice and can enforce a fresh process/session for independent review.

It must not infer reviewer freshness merely from a different step name. Freshness must remain an explicit PWv2 contract and be enforced as a session boundary. Review outputs should be schema-validated but still semantic reviewer judgments, not deterministic engine verdicts.

### New failure modes

- Split-brain between Markdown contract and executable router.
- Version skew between repo workflow ref and installed router binary.
- Engine DB/cache becomes de facto authority.
- Retry repeats a non-idempotent external write.
- Transition implementation omits a rare legal gate.
- Schema-valid but semantically wrong LLM handoff.
- State migration bugs.
- Deadlock from malformed dependencies.
- Automatic routing crosses a user/authority gate because semantic facts were under-modeled.

### Fit

- Read-only/shadow deterministic validation of current state/transitions: PWv2 low-risk incremental candidate.
- Executable router plus bounded role-package compiler: PWv2 architectural refactor.
- External Dagu-like engine owning orchestration while repository remains authority: PWv3 prior art / prototype, not a direct PWv2 default.
- External engine state as workflow authority: reject.

## 4. rpiv-todo

### How the mechanism works

rpiv-todo has a small explicit task state machine and typed mutation API. Each task may carry blockedBy IDs. Before a mutation is accepted it validates:
- dependency exists;
- dependency is not tombstoned;
- no self-dependency;
- adding the edge does not close a cycle.

It keeps deleted tasks as tombstones so historical dependency references remain resolvable. Reverse blocks edges are derived from other tasks' blockedBy sets.

Its persistence model is session-branch replay, not a database/file: every successful tool result contains a complete snapshot in details; lifecycle handlers walk the active branch and restore the last snapshot. Therefore reload/compaction can rebuild task state.

The overlay is explicitly derived UI. It groups status, shows dependency markers, truncates completed work before unfinished work, and is rebuilt from restored task state.

### Which PWv2 problem it could solve

- Task Card dependency cycles are not currently enforced by a dedicated graph validator.
- Ready work can require repeated interpretation of depends_on and Card state.
- A compact live view of ready/blocked/current work could reduce repeated state scans.
- Reload recovery could benefit from an explicitly derived queue view.

### What PWv2 already does instead

PWv2 already has stronger durable persistence than rpiv-todo: canonical Task Boards/Cards in Git plus exact workstream pointers. Therefore branch replay is not a missing capability and should not be copied as primary persistence.

PWv2 also already has dependencies semantically and readiness rules. The missing piece is executable graph validation/derivation.

### Real improvement or added complexity

Explicit dependency graph validation is a real, low-complexity improvement if implemented as a derived validator over existing canonical fields.

A separate todo store would be pure duplication and a dangerous second authority source.

### Context usage impact

Positive if the router/role can consume a small derived view such as:
- current card;
- ready cards;
- blocked cards with unsatisfied dependencies;
- cycle/invalid-edge diagnostics.

The model should be able to expand to canonical Task Board/Card records when needed. The compact queue is a view, not authority.

### Determinism / recoverability impact

Positive. Cycle detection and topological/readiness computation are deterministic. Recovery can recompute the same queue from Git-backed canonical state after every reload, so no extra persistence is required.

### Role isolation / independent review impact

Mostly neutral to positive. A derived queue can route execution without leaking unrelated work. Review readiness must still honor review_state/review_subject and fresh-session rules; dependency graph readiness cannot mark a reviewed Card done or waive review.

### New failure modes

- Derived graph parser disagrees with Task Card/Task Board fields.
- Duplicate dependency declaration locations drift.
- UI/cache is accidentally treated as state.
- A cycle validator checks only Task Board and misses a conflicting Task Card contract.
- Tombstone/superseded semantics are translated incorrectly into PWv2.
- Auto-selection of a ready Card bypasses a higher-priority router gate.

### Fit

- Dependency graph validator, cycle detection and derived ready queue: PWv2 low-risk incremental.
- Live progress surface derived from canonical state: optional PWv2/PWv3 UX prior art.
- rpiv branch-replay persistence as PWv2 state: reject.
- separate todo store: reject.

## Comparative table

| Prior art | Core mechanism | PWv2 overlap today | Material gap it addresses | Context impact | Determinism / recovery | Role isolation / review | Primary new risk | Best fit |
|---|---|---|---|---|---|---|---|---|
| pi-fabric code mode | One typed programmable tool runs nested branches/loops/fan-out and returns a bounded result | PWv2 already does workflow progressive disclosure, not nested-tool transcript isolation | Intermediate tool-output growth and repeated tool round-trips | High potential reduction | Better call-shape validation; workflow recovery unchanged unless results are committed | Good with strict per-role allowlists; cannot replace fresh review | Partial side effects / opaque compression | Low-risk read-only experiment; larger write-capable refactor |
| pi-fabric discovery | Names/catalog/search/describe then call | No equivalent PWv2-level tool schema router | Avoid loading every capability schema | High when tool surface is large | Neutral-positive; discovery is non-authoritative | Good | Stale/misranked discovery or over-broad tool set | PWv2 low-risk incremental |
| Laya/System One | Closed-set typed probabilistic choice/score/boolean without free-form generation | Main LLM currently performs semantic classification | Cheap bounded triage/escalation | Medium to high when Main can avoid raw input | Output shape deterministic, correctness probabilistic | Safe only inside roles/advisory; never reviewer freshness/verdict | Miscalibration/OOD/option sensitivity | PWv3 prior art; PWv2 shadow experiment |
| Dagu/state machine | Executable DAG/state transitions, retries, schemas, waiting/approval gates | PWv2 already defines durable states/router/gates in Markdown | Remove repeated interpretation of finite transitions | Very high potential | Strong if repo remains sole state; poor if engine state becomes required | Can enforce bounded workers/fresh reviewer launch | Split-brain/version skew/retry side effects | PWv2 architectural refactor / PWv3 prototype |
| rpiv-todo graph | blockedBy graph, pre-mutation cycle checks, derived reverse edges | PWv2 already records dependencies/readiness | Missing executable cycle/readiness validation | Low-medium reduction via compact ready queue | Strong positive, easy recomputation | Neutral-positive | Derived cache becomes authority or declaration drift | PWv2 low-risk incremental |
| rpiv-todo branch replay | Last complete snapshot reconstructed from session branch | PWv2 already has Git-backed canonical durable state | No material missing problem | No useful core benefit | Weaker than repo authority for PWv2 | Neutral | Creates second state source | Reject |

## Cross-cutting conclusions

### Markdown volume and repeated router interpretation

PWv2's progressive disclosure is directionally correct, but it still asks the LLM to interpret a substantial Markdown transition system. The highest-value architectural direction is not "less durable state"; it is separating:
- deterministic facts/transitions that code can compute;
- semantic judgments that require a model;
- authority-bearing records that remain in Git.

The safest first step is a shadow validator, not an authoritative executable router.

### Bounded context packages

PWv2 already has the raw ingredients: exact authority slices, Card contracts, review subjects, Research return targets and workstream pointers. A deterministic package builder could compile the exact files/sections needed for one role and include source hashes/refs. It would be a derived view only. This is a larger change than a linter because omission of an authority constraint would be a serious failure.

### Large intermediate tool outputs

pi-fabric's code-mode pattern is directly useful: perform mechanical read/search/filter/fan-out outside Main reasoning and return a bounded result with stable evidence pointers. For PWv2, the first experiment should be read-only. Write-capable batching requires transaction/idempotency analysis.

### Capability discovery

Search/describe-on-demand is a clean fit because it reduces context without changing project authority. Capability discovery should affect what tool schema is loaded, not what project operation is authorized.

### Recovery after interruption

PWv2 already solves the durable-state part well. The remaining opportunity is deterministic route reconstruction from that state. Do not replace Git recovery with session replay, engine DB state, todo snapshots or classifier memory.

### Task dependencies and cycle detection

This is the clearest missing executable invariant. The current Task Board already has depends_on; Task Cards also carry Dependencies. A validator can cross-check those canonical declarations, reject missing/self/cyclic edges and derive ready/blocked views without inventing a new state store.

### Structured handoffs

Dagu-style output_schema suggests validating role-result envelopes mechanically. The useful target is not forcing all semantic evidence into JSON; it is validating the transition-critical fields: subject/ref, result/evidence path, tests/checks summary, review state, return target and explicit next-router input. Narrative evidence can remain Markdown.

### Small models for bounded classification

Use only when the legal answer set is closed and a wrong result cannot silently cross a hard authority/review/user gate. Confidence thresholds must be fitted and audited on a PWv2-specific labeled set; confidence concentration alone is insufficient. A safe architecture is "classifier proposes; deterministic legal-set validator constrains; larger semantic model handles low-confidence/OOD/material cases."

### Fresh independent reviewer boundary

None of the prior art justifies weakening it. A deterministic orchestrator can make freshness easier to enforce, but reviewer identity/session separation remains an explicit PWv2 rule. Classifier decisions and prior worker context must not satisfy the independent-review obligation.

## Candidate improvements to evaluate

The following are research candidates only. None is approved for implementation.

### PWv2 — low-risk incremental

#### Candidate L1 — Task dependency graph validator and derived ready queue

Problem:
Task dependencies exist in Task Cards/Task Board but lack a dedicated executable graph/cycle validator and compact deterministic ready view.

Proposed mechanism:
Build a stateless validator that reads the selected WORKSTREAM.yaml, Task Board and referenced Task Cards; checks dependency IDs, self-edges, Card/board agreement, cycles and status/readiness invariants; emits a derived ready/blocked graph. Never persist a separate task database.

Expected benefit:
Earlier detection of impossible plans, less repeated LLM reasoning over dependency state, deterministic queue recovery after restart.

Authority impact:
None if read-only/derived. Canonical Task Board/Cards remain authoritative.

Context impact:
Small-to-medium reduction by presenting a compact ready/blocked summary with exact refs.

Implementation complexity:
Low to medium.

Required validation experiment:
Run in shadow mode across every current workstream plus synthetic missing-edge, self-edge, multi-node-cycle, superseded/deleted-equivalent and stale-status fixtures. Verify deterministic identical output after reload and ensure every reported edge points back to canonical records.

#### Candidate L2 — On-demand capability discovery for role tools

Problem:
Large tool/plugin schema surfaces consume context even when most actions are irrelevant.

Proposed mechanism:
Adopt the pi-fabric-style names/search/describe/call pattern or an equivalent Pi-native mechanism: expose a compact capability index, load full schemas only for selected actions, and preserve normal authorization separately.

Expected benefit:
Lower prompt/schema overhead and fewer guessed tool arguments.

Authority impact:
None. Tool discovery never grants project authority.

Context impact:
Potentially high when many MCP/plugins are available.

Implementation complexity:
Low to medium if the host already supports discovery; otherwise medium.

Required validation experiment:
A/B the same representative Research/Execution tasks with full schemas vs compact discovery. Measure model input tokens, schema lookup count, failed calls, latency and task correctness. Include ambiguous names and stale/missing capability cases.

#### Candidate L3 — Read-only code-mode tool composition with bounded return

Problem:
Search/read/filter/fan-out sequences put large intermediate outputs and many tool turns into Main context.

Proposed mechanism:
Allow a bounded read-only code-mode invocation to perform multiple independent reads/searches/loops and return only a small structured result plus exact evidence refs. No project/external writes in the first experiment.

Expected benefit:
Lower transcript growth, fewer model round-trips, better parallelism for mechanical evidence gathering.

Authority impact:
None when read-only and evidence refs remain canonical.

Context impact:
Potentially high reduction for research/audit roles.

Implementation complexity:
Medium.

Required validation experiment:
Replay several historical research/review evidence-gathering tasks. Compare context growth, missed evidence, reproducibility and result correctness. Inject one failed branch and one oversized tool result; verify failure is visible and not silently summarized away.

#### Candidate L4 — Structured transition-envelope validation

Problem:
Role handoffs/evidence are structured by convention but transition-critical fields can still be omitted or malformed in Markdown.

Proposed mechanism:
Define a small machine-validated envelope for transition-critical metadata only: exact subject/ref, result/evidence pointer, checks summary, review state, research return target/reconciliation and declared next-router input. Narrative evidence remains in current canonical Markdown files.

Expected benefit:
Fail earlier on malformed durable handoffs and reduce recovery ambiguity.

Authority impact:
Low if the envelope is embedded in or deterministically derived from the existing canonical record, not a duplicate file that can drift.

Context impact:
Small direct reduction; meaningful recovery benefit.

Implementation complexity:
Low to medium.

Required validation experiment:
Validate current historical handoffs/research/review records in compatibility mode, then inject missing/wrong subject, stale ref, bad return target and impossible state combinations. Confirm failures are precise and no valid historical record is silently reinterpreted.

#### Candidate L5 — Shadow deterministic router/state validator

Problem:
Many next-role conditions are finite and already encoded in durable state, but the LLM repeatedly interprets Markdown.

Proposed mechanism:
A read-only executable checker computes the legal next-role set and stop conditions from canonical state and compares its answer with the normal Markdown-router path. It cannot mutate state or select a role authoritatively.

Expected benefit:
Finds ambiguities before an architectural refactor and produces empirical coverage of which router decisions are truly deterministic.

Authority impact:
None in shadow mode.

Context impact:
No immediate production saving; enables evidence for later reduction.

Implementation complexity:
Medium.

Required validation experiment:
Replay historical workstream states at known transition commits and compare checker output with recorded next roles/stops. Fuzz malformed manifests/boards. Every disagreement must be classified as checker bug, Markdown ambiguity, or genuinely semantic branch.

### PWv2 — architectural refactor

#### Candidate A1 — Executable deterministic router for finite transitions

Problem:
Substantial Markdown is repeatedly interpreted for transitions that are often mechanical.

Proposed mechanism:
Move finite transition predicates into a versioned executable state machine that reads canonical repo state and emits one legal next obligation or an explicit semantic-decision request. Keep Git-backed workflow records as the only durable authority. Markdown becomes specification/explanation generated from or tested against the executable transition contract, not a second independently maintained behavior definition.

Expected benefit:
Large reduction in route ambiguity/context reads; stronger invalid-state rejection; simpler crash recovery.

Authority impact:
High architectural impact but can preserve the existing authority model if the executable router itself is versioned workflow policy and never owns project state.

Context impact:
Potentially very high reduction.

Implementation complexity:
High.

Required validation experiment:
Before any cutover, build a complete transition corpus from historical durable states, property/fuzz tests for invalid states, and a model-checkable transition table. Run old and new routers in shadow mode and require explained equivalence for every covered state. Crash after each transition boundary and prove recovery from repo alone.

#### Candidate A2 — Deterministic bounded role-context package compiler

Problem:
Even with route selection, each role may repeatedly read several contracts and authority records to reconstruct the same bounded package.

Proposed mechanism:
Given an exact canonical obligation, compile a transient package containing the role contract, exact authority excerpts/refs, Card/subject, accepted dependency results and required checks. Include source hashes/commit refs and a manifest of omitted-but-expandable sources.

Expected benefit:
Major context reduction and less authority omission.

Authority impact:
Medium-high risk: the package must remain derived and disposable. Canonical source always wins.

Context impact:
Very high potential reduction for executor/reviewer/subagent roles.

Implementation complexity:
High because safe omission is harder than summarization.

Required validation experiment:
Replay implementation and independent-review cases with full current reads versus compiled packages. Measure context and, more importantly, missed constraints/changed decisions. Mutate a canonical source after package creation and require stale-package rejection via hashes.

#### Candidate A3 — Deterministic orchestrator around bounded LLM workers

Problem:
Retries, sequencing, approval waits and resume behavior still require repeated role/router interpretation.

Proposed mechanism:
Use a Dagu-like state-machine/DAG runtime to launch bounded Pi/LLM workers, validate structured outputs, enforce idempotent retry policy and session-fresh reviewer launches. The engine is stateless/rebuildable with respect to project authority; every authoritative transition is committed to repo.

Expected benefit:
Operational determinism, explicit retry semantics, crash-resume and smaller worker prompts.

Authority impact:
High. Strict anti-second-authority design is mandatory.

Context impact:
High reduction at worker level.

Implementation complexity:
Very high.

Required validation experiment:
Prototype on a disposable workflow mirror. Delete the orchestrator's local DB/cache between every step and prove it can reconstruct from repo. Inject crashes before/after Git writes, duplicate retries, malformed worker JSON, stale branch heads and review boundaries. No irreversible write may be retried without an idempotency/readback contract.

### PWv3 prior art

#### Candidate P1 — Typed semantic decision primitive with calibrated escalation

Problem:
Some bounded semantic classifications do not justify a large autoregressive reasoning model but are not deterministic enough for rules.

Proposed mechanism:
A System One/Laya-style choice/score/boolean primitive over closed labels. It may suggest evidence class, tool/model choice, or escalation. The legal action set is deterministically constrained; unknown/OOD/low-confidence routes to a larger semantic model. No authority-changing gate can depend solely on it.

Expected benefit:
Lower cost/latency and smaller main-model context for high-volume bounded classifications.

Authority impact:
Low if advisory; unacceptable if authoritative.

Context impact:
Potentially medium-high where classifier directly consumes raw bounded input.

Implementation complexity:
Medium for a prototype, high for trustworthy calibration lifecycle.

Required validation experiment:
Create a PWv2-specific labeled corpus from real historical bounded decisions. Evaluate accuracy, confusion matrix, Brier/ECE, option-order sensitivity, OOD behavior and calibration drift by model version. Choose thresholds only from held-out data and evaluate cost-weighted false-auto-route versus escalation. Include an explicit unknown/abstain path.

#### Candidate P2 — Repository-derived live progress/graph UX

Problem:
Humans and agents can spend effort rereading Task Board state to understand current/blocked/ready work.

Proposed mechanism:
An rpiv-todo-like overlay generated on demand from canonical workstream/Task Board/Card state. No mutations are stored in the overlay; refresh/reload recomputes the same view from Git.

Expected benefit:
Faster situational awareness without changing workflow semantics.

Authority impact:
None if strictly read-only/derived.

Context impact:
Indirect positive: agents could be given the same compact derived graph.

Implementation complexity:
Medium and host-specific.

Required validation experiment:
Render all current workstreams, restart with all UI/cache state deleted, recompute and compare. Attempt UI-side mutations and ensure they cannot change canonical workflow state.

#### Candidate P3 — Tool-composition/runtime profile as a first-class execution substrate

Problem:
Future PW versions may want bounded role workers with tiny tool surfaces and mechanical fan-out outside the reasoning transcript.

Proposed mechanism:
Treat the pi-fabric code-mode/capability-discovery pattern as a runtime substrate specification: typed invocation, on-demand schema discovery, bounded nested output, explicit capability allowlists, and stable evidence references. Do not inherit Fabric's workflow/mesh authority model.

Expected benefit:
A cleaner separation between reasoning context and mechanical tool execution.

Authority impact:
None conceptually, but runtime security/capability policy becomes an architectural concern.

Context impact:
High potential.

Implementation complexity:
High for a general substrate.

Required validation experiment:
Benchmark representative PW workloads across direct tools vs composed runtime; audit side effects, cancellation, partial fan-out, evidence retention, reviewer visibility and capability least privilege.

### Reject / no material benefit

#### Candidate R1 — Fabric agents/workflows/mesh as PWv2 authority

Problem:
Would duplicate capabilities PWv2 already owns in Git/workstreams.

Proposed mechanism:
Not recommended: do not move lifecycle/coordination authority into Fabric mesh/actors/workflows.

Expected benefit:
No material benefit relative to authority risk.

Authority impact:
Unacceptable second source of truth.

Context impact:
Could reduce some transcript traffic, but at the cost of hidden state.

Implementation complexity:
High.

Required validation experiment:
None unless a future PWv3 explicitly reopens the authority model.

#### Candidate R2 — rpiv-todo branch replay or separate todo database as canonical task state

Problem:
PWv2 already has stronger canonical persistence.

Proposed mechanism:
Do not adopt as authority. At most derive a UI/queue from Task Board/Cards.

Expected benefit:
None for core durability.

Authority impact:
Would create split state.

Context impact:
No necessary benefit.

Implementation complexity:
Unnecessary.

Required validation experiment:
None.

#### Candidate R3 — Small classifier as the authoritative policy router

Problem:
The router includes hard authority/review/user gates and rare semantic conditions.

Proposed mechanism:
Do not let Laya/System One or another classifier directly select/waive those transitions.

Expected benefit:
Potential speed is outweighed by correctness risk.

Authority impact:
Unacceptable if a probabilistic result can bypass canonical policy.

Context impact:
Could reduce context, but unsafely.

Implementation complexity:
Medium plus ongoing calibration burden.

Required validation experiment:
Not appropriate as an authority path. Only the bounded advisory experiment P1 is justified.

#### Candidate R4 — Confidence threshold as proof of safety/correctness

Problem:
Typed-model confidence is easy to misread as calibrated correctness.

Proposed mechanism:
Do not use raw confidence as a hard review/user-write/authority gate.

Expected benefit:
None without domain calibration; false assurance is harmful.

Authority impact:
Can silently bypass gates.

Context impact:
Minimal.

Implementation complexity:
Low but misleading.

Required validation experiment:
If confidence is ever used operationally, calibration on held-out PWv2 data is mandatory as described in P1.

#### Candidate R5 — External orchestrator database/history as required recovery state

Problem:
Would undermine current repo-first recoverability.

Proposed mechanism:
Do not make Dagu or any other engine-local state necessary to know the legal next workflow obligation.

Expected benefit:
Operational convenience does not outweigh authority split.

Authority impact:
Unacceptable second authority.

Context impact:
Could simplify prompts, but at a structural cost.

Implementation complexity:
High.

Required validation experiment:
Any future orchestrator prototype must pass the destructive test: erase its local runtime state and recover correctly from Git alone.

## Overall research conclusion

The strongest immediate opportunities are not a wholesale workflow-engine replacement.

1. PWv2 already has the right durable authority and fresh-review model. Preserve them.
2. Add determinism first where facts are already explicit: dependency/cycle validation, state/handoff validation, and shadow route checks.
3. Reduce context at the runtime boundary: on-demand tool schema discovery and read-only code-mode composition are promising because they do not need new project authority.
4. Treat an executable router/context-package compiler as a real architectural refactor, not a helper script casually added beside ROUTER.md. The central design risk is split policy authority.
5. Treat System One/Laya-style typed classification as a bounded semantic primitive only. It is suitable for proposals, triage and escalation after domain calibration, not for waiving hard workflow gates.
6. rpiv-todo's graph/cycle ideas transfer cleanly; its persistence model does not.
7. Dagu's key prior art is the separation of deterministic orchestration from bounded workers plus schema-validated outputs and explicit waiting/approval states. Adopting the pattern is more relevant than adopting Dagu's state as authority.
8. The fresh independent reviewer boundary remains unchanged under every viable candidate.

No candidate is approved by this research. Any adoption decision belongs to a future normal Project Definition / Planning route.
