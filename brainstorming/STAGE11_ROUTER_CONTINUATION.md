# Stage 11 Brainstorming — Router / Automatic Continuation / Human Stops

Date: 2026-09-22
Scope: common-preexecution-core@R1
Status: resolved
Production authority: none
Baseline: current main ChatGPT-only/Codex-only routers + common user-stop contract + resolved Stages 1-10

## Purpose

Define one common continuation/router behavior after each durable workflow boundary.

Target property:

> Continue automatically whenever the next legal obligation is deterministic and already authorized. Stop only for a real human-owned boundary or the explicit premium-model handoff boundaries accepted in this Brainstorming.

The router chooses semantic obligations. Runtime-specific worker/session/context realization must not become a second project state machine.

## Common routing priority

Candidate high-level ordering:

1. recover authoritative durable state before routing when context/runtime may be stale;
2. preserve/recover the exact currently active obligation before selecting unrelated work;
3. satisfy pending Research/review/correction/finalization obligations before later implementation;
4. honor explicit accepted human authorization/product-decision gates;
5. honor the deliberate premium-model handoff stops;
6. otherwise select the next deterministic approved obligation;
7. end only when approved scope is complete and no further authorized obligation exists.

Exact low-level ordering remains module-specific; this stage defines the cross-stage policy.

## Automatic continuation

Ordinary durable boundaries are not user stops:
- Intake completion when next route is already authorized;
- Research completion when exact Return target exists;
- Definition completion when no premium handoff boundary applies;
- GREEN review when deterministic continuation is legal;
- bounded RED correction when authority is sufficient;
- Card completion;
- milestone Close;
- Recovery completion;
- publication/readback success.

The same context may continue across semantic roles when independence rules permit it.

Runtime replacement is allowed at durable boundaries without changing project semantics.

## Real human-owned stops

A normal human stop exists only when something genuinely requires user authority/input, including:
- unresolved product/system choice;
- explicit accepted authorization gate;
- missing credential/access/input that cannot be remediated by the runtime;
- end of approved scope where starting additional work would widen authority;
- explicit user request to stop/review before proceeding.

Do not stop merely because:
- a role/module ended;
- a worker/reviewer completed;
- a milestone completed;
- deployment/live-write is occurring without an explicit accepted authorization gate;
- current context could be cleaner;
- another runtime/model might also be capable.

## Premium-model hard stops — deliberate exception

The user explicitly requires three human-facing hard stops around the highest-leverage planning block:

### Premium stop A — Definition -> Strategic Planning

After Project Definition is complete and durable, before Strategic Planning:
- hard stop;
- tell the user that the next stage should use the best currently available model;
- do not begin Planning automatically.

### Premium stop B — Strategic Planning -> Independent Plan Review

After the exact Master Plan subject is frozen:
- hard stop;
- planner MUST NOT realize Stage-6 Plan Review through an internal subagent/worker;
- instruct the user to use a fresh independent context with the best currently available model.

### Premium stop C — approved Plan -> Execution Prep

After independent Plan Review is GREEN and the reviewed plan revision is durably approved:
- hard stop;
- tell the user that the highest-leverage planning/review block is complete;
- recommend switching to a lighter/cheaper model;
- do not automatically enter Execution Prep from the premium reviewer context.

These are intentional workflow/product-experience boundaries, not consequences of capability absence.

## Independence interaction

A context may cross role boundaries automatically unless the next obligation requires independence from work that context materially produced/repaired.

Implementation review remains capability-first:
- if a qualifying independent reviewer can be realized internally, use it;
- otherwise persist the same obligation and hand off to a fresh independent context.

Stage-6 Plan Review is the explicit exception above: user-mediated fresh top-model context is mandatory by design.

## Recovery and routing

Recovery does not end with a status report.

After durable state is coherent:
- rerun the common router;
- continue into the exact pending obligation when authorized;
- do not ask the user to say "continue" merely because Recovery succeeded.

If a crash occurs at a premium hard-stop boundary:
- durable state must make that boundary reconstructible;
- Recovery/router must re-present the required premium handoff rather than skipping it.

## Context health

Current ChatGPT-only contains context-health/fresh-session mechanics that Codex does not treat as project semantics.

Target V2 direction:
- context health is surface/runtime hygiene, not Project Workflow authority;
- it may recommend moving to a fresh context at a safe durable boundary;
- it must not create a semantic project stop by itself unless the surface genuinely cannot safely continue;
- premium stops A/B/C are separate explicit workflow gates and must not be conflated with context-health recommendations.

## End of approved scope

When the current managed workstream/project scope is durably complete:
- do not invent a new milestone/workstream;
- persist terminal truth;
- report completion;
- this is a real workflow end, not an invitation to autonomously widen scope.

If another already-approved milestone exists, that is not end of scope and continuation is automatic.

## Current open material questions

1. Should premium stops A/B/C outrank every otherwise-deterministic automatic continuation route, including Recovery resumption?
2. At end of approved scope, should the workflow simply report completion and stop, rather than asking "what next?" or proposing new work as part of Project Workflow?
3. Should context-health/fresh-chat guidance be strictly advisory at safe durable boundaries, with no Project Workflow hard stop unless continuation is technically unsafe?
4. After any ordinary Recovery, GREEN review, Card close or milestone close, should the router continue automatically without a user-facing checkpoint whenever the next obligation is already authorized?

These are Brainstorming questions, not accepted Definition decisions.


## Grilling decisions — stop precedence and context health

User accepted:

1. Premium hard stops A/B/C outrank otherwise-deterministic automatic continuation, including Recovery resumption. If Recovery reconstructs one of those exact boundaries, it re-presents the required premium-model handoff rather than routing past it.
2. At true end of approved scope, Project Workflow reports durable completion and stops. It does not ask "what next?" as a workflow requirement and does not invent another milestone/workstream.
3. Context Health / fresh-chat lifecycle is removed from V2 Project Workflow. The user reports it was not useful in practice and ordinary ChatGPT chat replacement already happens often enough. V2 therefore does not carry a common Context Health project mechanism or hard stop.
4. After ordinary Recovery, GREEN review, Card finalization or milestone Close, the router continues automatically whenever the next obligation is deterministic and already authorized.

Consequences:
- premium A/B/C are explicit exceptional workflow stops;
- normal chat/session replacement is handled by durable recovery, not a Context Health phase;
- no semantic project state is added for chat length/context hygiene.


## Stage 11 completion audit

Resolved:
- premium hard stops A/B/C outrank ordinary automatic continuation, including Recovery;
- end of approved scope is a real terminal stop and does not invite autonomous scope expansion;
- Context Health is removed from V2 Project Workflow rather than generalized;
- ordinary Recovery/review/Card/milestone boundaries continue automatically when the next obligation is deterministic and already authorized;
- runtime/session replacement is recovered from durable state rather than represented as project lifecycle;
- Stage-6 Plan Review remains the deliberate fresh-best-model exception to capability-first internal review realization.

No remaining Stage-11 semantic decision is open.

Stage 11 is resolved at Brainstorming level.
