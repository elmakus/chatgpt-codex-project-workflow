# Research — PWv2 architecture prior art R2: pi-extensible-workflows

Date: 2026-09-23
Research question: What mechanisms in pi-extensible-workflows are relevant to current PWv2, and do they materially change the candidate improvements identified in R1?

## Durable continuation metadata — chatgpt_only

Research ID: pwv2-architecture-prior-art-r2
Status: complete
Origin role: brainstorming
Origin subject: pwv2-architecture-prior-art@R2
Return target: brainstorming:pwv2-architecture-prior-art@R2
Return reconciliation: applied
Return reconciliation result: brainstorming/PWV2_ARCHITECTURE_PRIOR_ART_R2.md@blob:853b35f92d4393b755e8d02f30115268bd9bcb80

## Relationship to R1

This is a bounded R2 supplement to `research/PWV2_ARCHITECTURE_PRIOR_ART_R1.md`.

R1 remains immutable historical evidence for:
1. pi-fabric;
2. Laya / System One;
3. Dagu / deterministic state-machine orchestration;
4. rpiv-todo.

R2 adds the fifth requested prior-art source:
5. pi-extensible-workflows.

Unless explicitly changed below, R1 findings and candidate classifications remain in force as research evidence. Nothing in R1 or R2 is accepted requirements/decision/plan authority.

## Scope and hard constraints

Investigate `pi-extensible-workflows` against current PWv2, especially:
- Markdown/router interpretation load;
- context pressure and bounded role/subagent packages;
- deterministic/executable routing;
- tool/capability handling;
- workflow state, replay and interruption recovery;
- Task Card/dependency implications;
- structured handoffs/output validation;
- role isolation and fresh independent review.

Do not implement changes, design a complete PWv3, or alter accepted authority.

The current PWv2 authority constraints from R1 remain unchanged:
- WORKSTREAM.yaml, selected Task Board, Task Cards, canonical requirements/decisions/approved planning, review evidence and Git remain durable authority.
- Runtime journals, Pi session state, workflow snapshots, subagent records, Trajectory UI, worktree metadata or model aliases cannot become a second project authority.
- Current chatgpt_only execution semantics remain a constraint for present PWv2; adopting a multi-agent runtime for authoritative roles would itself be an architectural/product change, not an incremental implementation detail.
- Fresh independent review remains a hard semantic boundary.

## Source snapshot

Primary repository:
- https://github.com/vekexasia/pi-extensible-workflows
- inspected current main: `0c11e343cc3b36afcc702a334a0c47ce0b27d622`
- repository release commit message at inspection: `chore(release): 5.16.1`

Primary files inspected:
- README.md
- packages/core/skills/pi-extensible-workflows/SKILL.md
- docs/llm.md
- docs/developers.html
- docs/extensions.html
- docs/subagents.html
- packages/core/subagents/README.md
- packages/core/starter/review-loop.ts
- packages/core/starter/roles/developer.md
- packages/core/starter/roles/reviewer.md
- packages/core/starter/roles/researcher.md
- packages/core/src/host.ts
- packages/core/src/host-recovery.ts
- packages/core/src/types.ts
- relevant tests/search evidence for replay, snapshots, aliases and structured results.

Discovery source:
- public GitHub repository and README at https://github.com/vekexasia/pi-extensible-workflows.

## Direct answer

Yes: `pi-extensible-workflows` is materially relevant prior art for PWv2, and it strengthens R1 more than it changes R1.

It supplies a concrete Pi-native implementation of several mechanisms that R1 identified separately in pi-fabric and Dagu:
- deterministic JavaScript orchestration;
- parallel/pipeline control outside a single reasoning transcript;
- fresh agent sessions with explicit role/tool/context boundaries;
- structured result schemas;
- structural journaling and replay of completed operations;
- checkpoints/approvals;
- worktree isolation;
- on-demand workflow-function catalog discovery;
- compact cross-session status and recovery controls.

The most important R2 conclusion is:

> pi-extensible-workflows is a credible candidate **execution substrate** for a future PWv2 architectural refactor or PWv3 prototype, but it is not a replacement for PWv2's canonical router/authority model.

Its runtime journal can help resume execution, but Git-backed PWv2 state must remain sufficient to determine the legal project obligation. Its bundled `reviewLoop` is useful generic prior art, but it is not compatible with PWv2's fresh independent-review evidence boundary as-is.

## 5. pi-extensible-workflows

### How the mechanism works

#### 5.1 Deterministic JavaScript workflow program

The model-facing workflow tool runs a named inline `script` or reviewed file-backed `scriptPath`.

The default pattern is:

```js
const reports = await parallel("research", {
  first: () => agent("Research the first target."),
  second: () => agent("Research the second target."),
});

return await agent(
  prompt("Summarize these reports:\n\n{reports}", { reports }),
);
```

The script can use:
- `agent(...)`;
- `parallel(name, tasks)`;
- `pipeline(name, items, stages)`;
- JavaScript branches and loops;
- `shell(...)` for host-side deterministic gates;
- registered workflow functions;
- `checkpoint(...)`;
- `withWorktree(...)`;
- budgets/retry/resume.

The sandboxed workflow JavaScript itself has no imports, filesystem, network, process or timers. Host operations occur through explicit workflow APIs, agents or `shell()`.

This is important for PWv2 because orchestration logic can execute without making every branch/loop an autoregressive Main-agent turn.

#### 5.2 Structural identity and journal replay

Direct `agent(...)` calls receive hidden source call-site identity. Calls from the same source site must not race outside `parallel`/`pipeline`; those combinators add stable structural keys.

Completed agent, shell, registered-function and checkpoint operations are journaled by structural identity. On `workflow_retry`:
- completed operations replay from the journal;
- incomplete operations execute;
- the retry becomes a linked child run.

A reviewed `scriptPath` file is captured at launch so later retry/resume uses the captured program rather than silently reading a changed file.

This is a practical durable-execution pattern similar in spirit to workflow engines, but embedded directly in Pi.

#### 5.3 Explicit agent-context isolation

The bundled skill states:

> Workflow run does not inherit any of the main agent context.

Each `agent(...)` call starts a separate agent session with an explicit prompt and options.

Options include:
- role;
- model;
- tools;
- skills;
- extensions;
- contextFiles;
- outputSchema;
- retries;
- timeout.

Roles provide defaults and per-call options may override them. `contextFiles` chooses which Pi context-file classes are loaded. Resource selectors can narrow tool/skill/extension surfaces.

This is directly relevant to PWv2 bounded role packages: a worker need not inherit the entire parent transcript.

#### 5.4 Resource/capability isolation

Role and call selectors use ordered Minimatch rules. A critical semantic is that candidate resources start enabled.

Therefore a list such as:

```yaml
tools: [read, grep]
```

is not necessarily a restrictive allowlist.

To restrict, use:

```yaml
tools: ["!*", read, grep]
```

The bundled reviewer role correctly uses:

```yaml
tools: ["!*", "read", "grep", "find", "ls"]
```

This can enforce a reviewer/read-only capability ceiling at the worker level.

The prepared launch is treated as immutable capability ceiling; setup hooks may narrow but cannot widen it.

#### 5.5 Structured outputs

`agent(..., { outputSchema })` requires a schema-valid final value.

Each workflow agent is expected to submit `workflow_result` exactly once. Schema-bound agents submit a value matching the requested schema. The runtime includes one repair prompt for invalid structured output.

This is close to the R1 structured-transition-envelope candidate: semantic work stays with the model, while transition-critical result shape can be mechanically checked.

#### 5.6 Workflow catalog discovery

The model-facing `workflow_catalog` call:
- returns a compact index of registered workflow functions and model aliases by default;
- accepts `{ name }` to load one entry in full.

The bundled skill explicitly recommends one compact catalog read and then full detail only for the function to be used.

This is analogous to the on-demand discovery principle identified in pi-fabric, although its scope is narrower: registered workflow functions/model aliases rather than a generic catalog for every Pi/MCP tool.

#### 5.7 Checkpoints / approvals

`checkpoint(input)` suspends for explicit approval/rejection.

Checkpoint prompts/context are bounded. Responses are journaled and replay after cold recovery.

The budget subsystem also models approval explicitly: relaxing exhausted limits produces `awaiting_approval` with a proposal ID; `workflow_respond` answers the exact proposal.

This is useful prior art for deterministic user/approval gates, but the existence of a runtime checkpoint does not itself define PWv2 authority. PWv2 must still decide from canonical policy which approval is required.

#### 5.8 Worktrees

`withWorktree(name, callback)` creates deterministic named worktree scopes from a clean launch HEAD and gives the callback a frozen `{ path, branch }`.

Separate parallel branches can receive separate worktrees. Retried/recovered operations reuse the enclosing scope.

This is relevant to isolated parallel workers, but PWv2's managed workstream branch remains the project-lifecycle identity. Internal runtime worktrees cannot replace WORKSTREAM.yaml/branch lifecycle.

#### 5.9 Runtime status and recovery

`workflow_status({ runId })` returns a compact cross-session run summary without transcripts.

Recovery primitives distinguish:
- per-agent same-run retry;
- workflow retry of failed persisted run;
- resume of budget-exhausted run;
- new run with `parentRunId` only for borrowing named worktrees.

The recovery API accepts an `expectedState` so recovery fails instead of acting on a runtime state that changed after inspection.

This is good compare-and-act prior art, but `expectedState` protects the workflow runtime state, not the PWv2 canonical subject/branch/head. A PWv2 integration would additionally need a canonical subject/head guard.

### What PWv2 problem it could solve

#### Main-transcript context pressure

Strong fit.

Worker transcripts, tool use and intermediate reasoning live in child agent sessions rather than Main. The parent workflow receives only explicit agent results and the final returned value.

This directly attacks:
- intermediate subagent/tool transcript growth;
- unrelated parent-history leakage;
- multi-role context contamination.

#### Bounded context package for role/subagent

Strong fit as a delivery mechanism.

PWv2 already knows what a bounded role needs conceptually:
- exact authority slice;
- Card/review subject;
- accepted dependency results;
- required checks/evidence.

pi-extensible-workflows can enforce the runtime boundary through:
- one fresh session per `agent(...)`;
- role prompt;
- `contextFiles`;
- tool/skill/extension selectors;
- structured prompt/result flow.

What it does **not** provide is a PWv2-aware compiler that knows which canonical repository sections must be included. That remains the hard part of R1 Candidate A2.

#### Deterministic orchestration

Strong fit as substrate, incomplete as policy.

The JavaScript workflow is deterministic enough to control sequencing, fan-out, retry and checkpoints. A versioned reviewed `scriptPath` or registered workflow function can avoid repeatedly asking Main to improvise the same orchestration.

However, an LLM-authored inline script is not itself an authoritative translation of ROUTER.md. If used for PWv2 routing, policy logic must be versioned/reviewed and tested against canonical contracts.

#### Recovery after interruption

Strong operational fit, but secondary authority only.

Structural journal replay is more sophisticated than merely restarting a subagent. It avoids rerunning completed operations when runtime state is intact.

PWv2 already has stronger project recovery: Git state answers what project obligation is current. The workflow journal can answer a narrower question: which runtime operations for that obligation already completed.

Correct layering would be:

```text
canonical Git state
  -> legal PWv2 obligation
  -> exact runtime workflow instance / expected subject
  -> runtime journal optimization
```

Never:

```text
workflow journal
  -> decide what PWv2 obligation is current
```

#### Structured handoffs

Strong fit.

`outputSchema` can enforce fields for worker results, review findings, evidence references or transition-envelope metadata.

It reduces malformed handoffs but not semantic errors. A schema-valid wrong result remains wrong.

#### Capability discovery

Moderate fit.

`workflow_catalog` validates the R1 on-demand-discovery principle. It is useful for workflow extensions/functions and aliases, but it does not subsume pi-fabric's broader generic action search/describe surface.

#### Role isolation

Strong fit.

Separate native sessions plus restrictive role resource selectors can produce much cleaner executor/reviewer boundaries than a long parent transcript.

#### Fresh independent review

Partially compatible, but **the bundled reviewLoop is not sufficient**.

Every `agent(...)` reviewer invocation is a separate session, which is good.

But `packages/core/starter/review-loop.ts` explicitly passes the reviewer:
- original task;
- previous review findings;
- developer summary.

PWv2's fresh independent reviewer contract intentionally excludes previous implementation-chat narrative as review evidence and requires recovery from exact canonical subject/authority/evidence.

Therefore the generic `reviewLoop` must not be used as PWv2 REQUIRED/RECOMMENDED independent review as-is.

A PWv2-compatible custom workflow could instead launch a fresh reviewer session with only:
- exact immutable review subject;
- Card/milestone contract;
- same canonical authority slice used by implementation;
- exact evidence/readback required by the review contract;
- restricted read-only tools;
- no persistent agent handle;
- no developer narrative unless it is itself canonical evidence.

### What PWv2 already solves another way

PWv2 already has:
- durable Git-backed workstream identity;
- canonical execution/review state;
- exact research/review subjects;
- workstream branches;
- explicit user/review stops;
- recovery from repository state;
- bounded Task Card authority slices;
- fresh independent-review semantics.

pi-extensible-workflows adds runtime machinery around those concepts. It should not replace them.

### Is it a real improvement or only complexity?

#### Real improvement

It is real improvement prior art for:
- bounded child contexts;
- parallel role execution;
- deterministic call structure;
- structured worker output;
- runtime replay;
- Pi-native worktree/session management;
- compact runtime inspection;
- concrete role capability restriction.

Unlike generic Dagu prior art, this is directly designed for Pi and therefore lowers prototype cost if PWv2/PWv3 later targets Pi-native orchestration.

#### Added complexity

It becomes harmful if:
- its journal/run records become required project state;
- an inline LLM-generated workflow script becomes de facto policy router;
- runtime worktrees compete with PWv2 branch/workstream lifecycle;
- bundled reviewLoop is mistaken for PWv2 independence;
- resume replays an old snapshot after canonical PWv2 authority has changed;
- generic roles/settings silently drift outside the reviewed Project Workflow revision.

## Context usage impact

### Positive

Potentially high reduction.

1. Child agents do not inherit Main context.
2. Each role can receive a small prompt and selected context files.
3. Main does not need every child transcript.
4. Agent results can be schema-bounded.
5. Parallel branches do not require one Main inference per branch transition.
6. Catalog detail is loaded on demand.
7. Compact status is available without transcripts.

This is probably more directly useful for PWv2 role/subagent context than Dagu because it owns the actual Pi child-agent session boundary.

### Remaining context risks

- Explicitly interpolating large child results into a summarizer can still create large context.
- A badly designed role may load global/project/cwd context files unnecessarily.
- A tool-restricted child may still read too much repository content.
- Persistent `agent.create` handles intentionally retain prior turns and should not be used where fresh role context is required.
- The Main agent still has to decide/build the workflow unless orchestration is versioned.

## Determinism / recoverability impact

### Positive

- structural call identity;
- stable parallel/pipeline keys;
- launch-captured scriptPath content;
- frozen/captured settings/roles for executed calls;
- journal replay of completed operations;
- expectedState guard for retry/resume;
- typed run/error states;
- explicit checkpoints;
- deterministic resource preflight;
- fail-closed unknown role/model/resource behavior.

### Important non-determinism / change semantics

Dynamic model aliases are intentionally resolved again on resume and the runtime records drift warnings. Therefore "resume" is not necessarily bit-identical model execution for future incomplete calls.

Roles/functions not yet reached may also be captured later according to current availability rules.

For PWv2, the exact Project Workflow revision, workstream subject and canonical branch/head must remain the stronger compatibility guard.

### Recoverability boundary

If the pi-extensible-workflows local run store disappears, its fine-grained replay optimization disappears. PWv2 must still be recoverable from Git by constructing a new runtime execution for the canonical current obligation.

This means a future integration should be tested with destructive runtime-state deletion.

## Role isolation / independent review impact

### Executor / bounded worker isolation

Strongly positive:
- separate sessions;
- no inherited Main transcript;
- explicit role prompt;
- restricted tools;
- selected context files;
- optional worktree;
- schema-bound output.

### Reviewer isolation

Potentially strongly positive with a custom PWv2 workflow.

The runtime can start a genuinely separate reviewer agent session and can restrict it to read/search tools.

But freshness is a **policy package property**, not merely "different agent ID".

A reviewer that receives developer summary/history is session-separate but not evidence-clean under PWv2's current review contract.

### Persistent handles

`agent.create` intentionally keeps one agent transcript across turns. This is valuable for iterative authors, but should be excluded from PWv2 independent-review launches.

## New failure modes

### F1 — runtime journal becomes second authority

A run ID or journal state could accidentally be treated as proof of project completion.

Mitigation:
Canonical WORKSTREAM/Task Board/Card/review state always wins. Runtime state is cache/evidence only.

### F2 — stale workflow resume after canonical state changed

A captured script/snapshot may continue correctly according to its runtime contract while the project branch/authority has advanced.

Mitigation:
Bind every authoritative workflow launch/recovery to exact workstream ID, branch, canonical subject and expected Git head/authority revision. Fail closed when those no longer match.

### F3 — replay duplicates external side effects

The docs explicitly warn that a host crash after an external side effect but before journaling can cause the action to run again.

Mitigation:
Use workflow operations for verification/idempotent work by default; every external mutation needs PWv2 readback/idempotency semantics. Never infer exactly-once.

### F4 — resource selector misunderstanding

Positive selectors are additive unless the set is first cleared with `!*`.

Mitigation:
PWv2 role templates must use explicit deny-all-then-allow patterns and validate effective resources with doctor/preflight.

### F5 — generic reviewLoop violates evidence-clean review

Separate session does not equal independent PWv2 review when developer summaries/previous review are injected.

Mitigation:
Do not use reviewLoop for REQUIRED/RECOMMENDED PWv2 review. Build a custom fresh-review function that reconstructs only canonical authority/evidence.

### F6 — generated inline workflow becomes transient policy

The Main agent can generate JavaScript on the fly. That is appropriate for task-specific orchestration, not authoritative policy routing.

Mitigation:
Policy-grade orchestration must be a reviewed/versioned `scriptPath`, registered function, or deterministic repo CLI with tests.

### F7 — worktree lifecycle collision

Runtime-owned worktree branches can be confused with PWv2 managed workstream branches.

Mitigation:
Treat runtime worktrees as subordinate execution sandboxes only. Workstream identity remains manifest branch. Define explicit merge/result rules before allowing write-capable workers.

### F8 — schema-valid semantic error

outputSchema validates shape, not correctness or authority compliance.

Mitigation:
Keep normal semantic review/acceptance.

### F9 — persistent agent handle contaminates role freshness

An `agent.create` handle carries transcript between turns.

Mitigation:
Disallow persistent handles for reviewer/other fresh-boundary roles.

### F10 — runtime configuration drift

Roles/settings/extensions/model aliases may change independently of project workflow unless pinned/captured.

Mitigation:
For policy-grade use, capture/version relevant runtime role/config artifacts with the workstream/workflow revision and record resolved runtime identity in evidence.

## Comparison against R1 sources

| Mechanism | pi-fabric | Dagu | rpiv-todo | pi-extensible-workflows | R2 interpretation |
|---|---|---|---|---|---|
| Code-mode branches/loops/fan-out outside Main | Strong | DAG-oriented | No | Strong JavaScript workflow DSL | Confirms code-mode orchestration is practical in Pi itself |
| On-demand capability discovery | Broad action search/describe | Not central | No | Compact workflow_catalog + detail | Strengthens principle, but pi-fabric remains broader |
| Child role context isolation | Agent/runtime dependent | Worker boundary | No | Explicit separate Pi agent sessions, no Main-context inheritance | Strong new concrete evidence for A2 |
| Tool/resource restriction per role | Capability registry | Worker config | No | Role/call selectors, immutable capability ceiling | Strong fit for bounded role packages |
| Structured result validation | Typed tool schemas | output_schema | Typed todo tool | agent outputSchema + workflow_result | Strong direct Pi-native fit for L4 |
| Deterministic execution identity | Tool program/trace | DAG step IDs | task IDs | call-site + structural path + occurrence journal | Strong fit for replay |
| Retry without rerunning completed work | Partial runtime mechanisms | Durable workflow semantics | No | Journal replay completed / execute incomplete | Strong new concrete evidence for A3 |
| Approval gate | Permission/host mechanisms | human/approval steps | No | checkpoint + proposal response | Strong fit as execution gate, not authority |
| Worktree isolation | Available in agents | git.worktree action | No | withWorktree / subagent worktree | Directly relevant to Pi implementation workers |
| Project authority model | Fabric-local runtime state | Engine state | Todo state | Workflow journal/snapshot | None should replace PWv2 Git authority |
| Fresh independent review as PWv2 defines it | Must be custom | Must be custom | N/A | Possible with custom fresh agent package; bundled reviewLoop is not sufficient | Freshness remains PWv2-owned |

## Does R2 change the R1 candidate list?

Mostly it strengthens and refines it.

### R1 Candidate L2 — On-demand capability discovery

**Status after R2: unchanged, strengthened.**

pi-extensible-workflows independently uses compact catalog index + named detail. This supports the idea that demand-driven schema/detail loading is useful.

However, its catalog is workflow-function/model-alias specific. pi-fabric remains stronger prior art for generic tool/MCP capability discovery.

### R1 Candidate L3 — Read-only code-mode tool composition with bounded return

**Status after R2: unchanged, strengthened.**

pi-extensible-workflows demonstrates Pi-native JavaScript composition, but its primary composition is orchestration over agents/functions rather than pi-fabric's generic nested tool program.

The safest low-risk experiment remains read-only/bounded. Write-capable workflow operations retain replay/idempotency risks.

### R1 Candidate L4 — Structured transition-envelope validation

**Status after R2: unchanged, strongly strengthened.**

`outputSchema` plus exactly-one `workflow_result` is a direct implementation pattern for schema-valid worker handoffs.

PWv2 should still keep transition-critical envelopes canonical/derived from repository state rather than only in runtime output.

### R1 Candidate A1 — Executable deterministic router

**Status after R2: unchanged, implementation path clarified.**

pi-extensible-workflows could host an executable router, but the router logic must be reviewed/versioned. An on-the-fly generated workflow script is not acceptable authority.

A cleaner prototype would be:
- deterministic PWv2 router CLI/function reads canonical repository state;
- pi-extensible-workflows calls it through a registered function or bounded shell gate;
- returned legal obligation selects the next bounded worker;
- authoritative transition is committed to canonical repo state.

### R1 Candidate A2 — Deterministic bounded role-context package compiler

**Status after R2: strengthened materially.**

pi-extensible-workflows already solves the **delivery boundary**:
- new agent session;
- no Main context inheritance;
- explicit role;
- explicit contextFiles;
- explicit tools/skills/extensions;
- structured output.

What remains unsolved is **package correctness**:
- selecting every necessary canonical authority constraint;
- hashing/pinning those sources;
- proving no material constraint was omitted.

Therefore A2 remains a real architectural refactor, but no longer requires inventing a child-agent runtime from scratch in a Pi deployment.

### R1 Candidate A3 — Deterministic orchestrator around bounded LLM workers

**Status after R2: substantially strengthened and made concrete.**

Dagu proved the architecture class. pi-extensible-workflows proves a close Pi-native implementation already exists.

If future authority permits Pi-native multi-agent orchestration, the first experiment should evaluate adapting this runtime rather than building a scheduler from scratch.

Still required:
- canonical Git state remains sole project authority;
- exact PWv2 route/subject guards;
- custom review-boundary semantics;
- idempotency/readback contracts;
- runtime-state deletion recovery test;
- version pinning / compatibility checks.

### R1 Candidate P3 — Tool-composition/runtime profile as first-class execution substrate

**Status after R2: strengthened and narrowed.**

R2 suggests splitting P3 into two concepts if later promoted:
1. generic nested tool composition/capability discovery — pi-fabric prior art;
2. Pi-native bounded multi-agent orchestration/replay — pi-extensible-workflows prior art.

They solve related but different context problems.

## New candidate introduced by R2

### PWv2 — architectural refactor

#### Candidate A4 — Pi-native bounded worker substrate using pi-extensible-workflows

Problem:
PWv2 has durable role/authority semantics but normal execution still assumes one ChatGPT conversation interprets routes/contracts and accumulates context. A future Pi-hosted workflow needs bounded worker sessions, role resources, structured results, replay and operational recovery.

Proposed mechanism:
Evaluate pi-extensible-workflows as the worker/orchestration substrate, while keeping PWv2 policy and canonical state outside it:
- versioned deterministic router/package compiler in the Project Workflow repo;
- launch one fresh `agent(...)` per bounded role;
- explicit role/contextFiles/resource selectors;
- outputSchema for transition-critical worker results;
- structural workflow journal only as runtime cache;
- canonical workstream/Task Board mutations in Git;
- custom PWv2 review workflow rather than bundled reviewLoop.

Expected benefit:
Avoid building Pi session spawning, concurrency, role selection, tool restriction, worktree handling, structured outputs, journal/replay and inspection from scratch. Potentially large context reduction and stronger operational determinism.

Authority impact:
High architectural impact. Safe only if runtime journal/snapshots/run IDs are non-authoritative and every legal obligation can be recovered from repo alone.

Context impact:
High positive potential: child agents do not inherit Main context and can receive narrow resources/context files.

Implementation complexity:
Medium-to-high for a prototype because much runtime machinery already exists; high for production-grade PWv2 compatibility because canonical routing/package/review semantics must be integrated and validated.

Required validation experiment:
1. Build a disposable shadow workflow for one existing historical Card lifecycle.
2. Version/pin the workflow function and exact PWv2 commit.
3. Compile an executor package from canonical Card/authority state.
4. Launch a bounded executor worker and structured result.
5. Persist result through existing canonical PWv2 state.
6. Launch a **separate custom reviewer** from canonical subject/authority/evidence only.
7. Inject crash before and after every journal/Git boundary.
8. Delete all pi-extensible-workflows runtime state and prove project recovery from Git alone.
9. Restore runtime state but advance canonical Git subject; prove stale resume fails closed.
10. Inject non-idempotent external-write scenario; prove retry cannot silently duplicate it.
11. Compare context/token footprint and missed-constraint rate against current full-context workflow.

Success criteria:
- no second authority;
- no review-boundary contamination;
- deterministic legal route equivalence;
- material context reduction;
- recovery survives runtime-state deletion.

## Reject / no material benefit additions

### R6 — Bundled reviewLoop as PWv2 REQUIRED/RECOMMENDED review

Problem:
Generic reviewLoop passes developer summary and previous review findings into the next reviewer.

Proposed mechanism:
Do not use it as the PWv2 independent-review gate.

Expected benefit:
The generic loop is convenient, but convenience does not satisfy evidence-clean fresh review.

Authority impact:
Would weaken the existing review contract if treated as equivalent.

Context impact:
Could be efficient but imports implementation narrative.

Implementation complexity:
No value in forcing compatibility; a custom review function is simpler/clearer.

Required validation experiment:
None for direct adoption. Any custom replacement must prove reviewer input contains only canonical subject/authority/evidence plus independently gathered inspection.

### R7 — Workflow journal / run ID as PWv2 recovery authority

Problem:
Journal replay is attractive enough to become de facto state.

Proposed mechanism:
Reject. Use it only as runtime optimization.

Expected benefit:
No project-authority benefit beyond existing Git recovery.

Authority impact:
Would create split brain.

Context impact:
Neutral.

Implementation complexity:
Unnecessary.

Required validation experiment:
Destructive runtime-state deletion must remain a mandatory test for any future substrate prototype.

### R8 — LLM-authored inline workflow script as authoritative router

Problem:
The model can write a workflow script dynamically.

Proposed mechanism:
Reject for policy routing. Authoritative transition logic must be versioned/reviewed/tested.

Expected benefit:
Fast prototyping only.

Authority impact:
Unacceptable transient policy source.

Context impact:
Potentially low, but correctness is the priority.

Implementation complexity:
Low to prototype, high hidden correctness risk.

Required validation experiment:
Not appropriate as final architecture; use only shadow experimentation.

### R9 — Persistent agent handle for independent review

Problem:
Persistent handles preserve one agent's transcript across turns.

Proposed mechanism:
Do not use `agent.create` for fresh-review roles.

Expected benefit:
None for independent review.

Authority impact:
Can violate freshness/evidence isolation.

Context impact:
Retains context intentionally.

Implementation complexity:
Avoid.

Required validation experiment:
Fresh reviewer tests should assert a new agent session and absence of prior implementation/review narrative.

## Updated candidate classification summary

### PWv2 — low-risk incremental

R2 adds no new standalone low-risk feature that should be implemented merely because this package exists.

It **strengthens** existing R1 low-risk candidates:
- L2 on-demand capability discovery;
- L3 read-only bounded code-mode composition;
- L4 structured transition-envelope validation.

Using the full multi-agent runtime for authoritative current chatgpt_only roles would not be low-risk because it changes executor/session semantics.

### PWv2 — architectural refactor

R2 materially strengthens:
- A1 executable deterministic router;
- A2 deterministic bounded role-context package compiler;
- A3 deterministic orchestrator around bounded LLM workers.

R2 adds:
- A4 Pi-native bounded worker substrate using pi-extensible-workflows.

Of all prior art in R1/R2, pi-extensible-workflows is the closest concrete implementation candidate for A3/A4 in a Pi-hosted future.

### PWv3 prior art

Still relevant as a broader architecture source if PWv2 intentionally avoids changing current chatgpt_only executor semantics.

It is particularly useful for:
- explicit role/session boundary;
- journal/replay runtime;
- worktree sandbox coordination;
- compact execution observability;
- checkpoints;
- result schemas.

### Reject / no material benefit

R2 adds explicit rejects:
- bundled reviewLoop as PWv2 independent-review gate;
- workflow runtime state as project authority;
- ad-hoc generated workflow JS as policy authority;
- persistent agent handles for fresh review.

## Updated five-source comparison

| Prior art | Strongest contribution to PWv2 research | Context benefit | Determinism/recovery benefit | Authority risk | Best research fit |
|---|---|---:|---:|---:|---|
| pi-fabric | Generic typed code-mode tool composition + on-demand action discovery | Very high | Medium | Medium if runtime state leaks into authority | Low-risk runtime experiments / PWv3 substrate |
| Laya / System One | Cheap typed probabilistic semantic decisions | Medium-high in narrow cases | Output-shape high, semantic correctness probabilistic | High if used for hard gates | PWv3 bounded classifier prior art |
| Dagu | Deterministic DAG/state-machine orchestration around bounded workers | Very high potential | Very high | High if engine state becomes authority | PWv2 architectural refactor / PWv3 |
| rpiv-todo | Explicit blockedBy graph, cycle detection, derived ready view | Low-medium | High | Low if derived only | PWv2 low-risk incremental |
| pi-extensible-workflows | Pi-native deterministic multi-agent workflow runtime with bounded sessions + journal replay | Very high | High operationally | High if journal/scripts become policy/state authority | PWv2 architectural refactor / concrete Pi prototype |

## Interaction with fresh independent reviewer boundary

This source provides useful mechanisms but does not change the R1 conclusion.

PWv2 freshness requires both:
1. a fresh reviewer execution/session;
2. an evidence-clean bounded package reconstructed from canonical state.

pi-extensible-workflows solves (1) well with a new `agent(...)` session.

It can help enforce (2) using:
- a custom reviewer role;
- `tools: ["!*", "read", "grep", "find", "ls"]`;
- minimal `contextFiles`;
- exact prompt containing canonical subject/authority/evidence refs;
- `outputSchema` for findings/verdict envelope.

But the built-in reviewLoop intentionally supplies implementation summaries and review history. Therefore it is generic implementation-review automation, not PWv2 independent review.

## Required anti-second-authority rules for any future prototype

If this source is ever evaluated beyond research, require all of the following:

1. Git-backed PWv2 state is sufficient to determine the current legal obligation without any workflow run ID.
2. Every runtime run is bound to exact workstream ID, branch, Project Workflow revision and canonical subject/head.
3. Runtime resume fails closed when that canonical binding changed.
4. Runtime result never marks a Card/review/milestone terminal by itself.
5. Canonical state transition is a separate repository mutation/readback.
6. Runtime journal loss cannot make project recovery impossible.
7. Worktree branch/path is execution metadata only.
8. A fresh reviewer gets a new agent session and canonical package only.
9. Persistent handles are forbidden for fresh-boundary roles.
10. External mutations use explicit idempotency/readback contracts.
11. Policy-grade scripts/functions are reviewed/versioned; ad-hoc scripts are not authority.
12. Trajectory/UI/status output is observability only.

## Overall R2 conclusion

pi-extensible-workflows is one of the most relevant prior-art sources for a future Pi-hosted PWv2/PWv3 because it directly demonstrates that several desired properties can coexist:

- deterministic programmatic orchestration;
- multiple bounded agent sessions;
- explicit context/resource restrictions;
- structured output;
- parallel/pipeline execution;
- replay/resume;
- checkpoints;
- worktrees;
- compact inspection.

It does **not** make PWv2's durable authority model obsolete. In fact, its own journal/snapshot semantics make the separation more important.

R2 changes the practical implementation outlook more than the conceptual architecture:

- R1 said "a deterministic orchestrator around bounded workers may be valuable."
- R2 says "there is already a mature Pi-native runtime that could be evaluated for that role instead of building the worker/orchestration layer from zero."

The hardest unsolved PWv2 pieces remain:
- canonical executable policy/router semantics;
- correct bounded authority-package compilation;
- exact compatibility binding between runtime snapshot and canonical project subject;
- fresh independent-review package semantics.

No candidate is approved by R2. Any adoption/prototype decision belongs to a future normal Project Definition / Planning route.
