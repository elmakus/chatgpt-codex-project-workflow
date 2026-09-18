# Project Definition

## Goal

Convert explored ideas and verified evidence into the **accepted product/system definition** that planning is allowed to organize for execution.

Definition answers:

- what must become true;
- what must remain true;
- what is explicitly out of scope;
- which strategic/high-level choices are already accepted;
- which unresolved questions still require evidence or user/product authority.

Definition does **not** own milestone sequencing, Task Card decomposition or implementation execution.

## Canonical outputs

Do not create a separate definition summary merely to restate authority.

Persist accepted definition into the existing canonical artifacts:

- product/system requirements, constraints, non-goals, invariants and acceptance-level outcomes → `requirements/`;
- accepted strategic/high-level choices and their rationale/consequences → `decisions/`;
- unresolved questions that still matter → `brainstorming/OPEN_QUESTIONS.md` or the project's canonical equivalent;
- material high-level authority pointers/status → `PROJECT.md` only when appropriate.

Use `templates/REQUIREMENTS.md` and `templates/DECISION.md` when useful.

## Entry boundary

Project Definition may begin only after the selected policy route's entry conditions are satisfied.

If the selected route requires explicit user promotion from exploratory Brainstorming, Definition must verify the exact promotion subject/revision required by that route instead of inferring authorization from brainstorming maturity, research completion or the existence of tentative conclusions.

Once Definition has been explicitly authorized for the current definition scope, ordinary Research ↔ Definition evidence loops do not require repeated promotion unless the work deliberately returns to open-ended Brainstorming and reopens that scope.

## Inputs

Read only what is needed to establish accepted intent:

- project `PROJECT.md`;
- user/product goal and explicit choices;
- relevant brainstorming conclusions;
- the exact completed active-research record when returning from Research to this Definition subject;
- relevant verified research/evidence;
- existing accepted requirements and decisions when redefining an active project;
- current project/source/external baseline only when it materially constrains the definition.

Do not load implementation-state machinery merely to define a new project unless active-state compatibility is itself part of the definition.

## Authority distinctions

Keep these categories separate:

### Verified fact / external constraint

A fact supported by evidence may constrain the definition. Preserve provenance.

A verified hard environmental/technical/legal constraint may be recorded as a requirement constraint without pretending it is a user preference.

### Accepted requirement

A requirement expresses accepted product/system intent: behavior, target state, invariant, constraint, non-goal or acceptance-level outcome.

The definition role may formalize unambiguous consequences of explicit accepted intent and verified hard constraints. It must not invent a product preference, risk tolerance or external behavior choice that requires user/product authority.

### Accepted decision

A decision records an accepted strategic/high-level HOW when choosing among alternatives materially shapes architecture, product/system behavior, compatibility, data model, security, migration or another downstream implementation choice.

Record material rationale and rejected alternatives when their omission could cause a later role to choose differently.

### Open question

If evidence or user/product authority is still required and the answer can materially change the target definition, keep it explicitly unresolved.

Do not hide it in planning as an implementation detail.

## Definition workflow

1. Recover the current accepted goal and any existing definition authority.
2. Read only relevant brainstorming/research/evidence. When `PROJECT.md → Active research obligation` points to a `complete` record whose Return target is this Definition subject, treat reconciliation of that record as the current obligation.
3. Separate facts, explicit user choices, requirements, strategic decisions and unresolved questions.
4. Draft/reconcile canonical requirements.
5. Create/reconcile accepted decision records for material strategic choices.
6. Preserve constraints, non-goals, invariants, external contracts and acceptance-level outcomes.
7. Check for contradictions between new definition, existing accepted authority and verified hard constraints.
8. Resolve or surface every unresolved question that can materially alter planning.
9. Mark canonical requirements `approved` only when the Definition Complete gate below passes.
10. Return to the policy router.

Do not create milestones or Task Cards merely because the target is now clear.

## Definition Complete gate

Definition is ready for planning only when all applicable conditions hold:

- goal/target state is explicit enough to plan;
- material MUST requirements are identifiable;
- non-goals/scope boundaries are explicit where omission could cause scope drift;
- global invariants and hard external constraints are captured;
- acceptance-level outcomes are defined enough to judge eventual success;
- every strategic/high-level choice that must be frozen before planning is accepted in `decisions/`;
- relevant research uncertainty is either resolved or explicitly proven non-blocking for planning;
- no unresolved user/product choice can materially change milestone architecture or project outcome;
- canonical requirements are internally coherent and marked `approved`.

## Route transitions

Definition is a bounded role.

When more evidence is required:
- persist the exact open question/evidence need;
- create/activate one exact research record with `Status: active`, `Origin role: project_definition`, the exact current Definition subject/revision as `Origin subject`, and `Return target: project_definition:<exact subject>`;
- for pre-execution Definition, set `PROJECT.md → Active research obligation` to that exact record before yielding the role;
- return to the router;
- route to Research.

When returning from a `complete` Research record:
- reconcile its verified findings into requirements/decisions/open questions as appropriate;
- persist that Definition reconciliation first;
- then set the research record to `consumed` and clear `PROJECT.md → Active research obligation`;
- only then continue the remaining Definition obligation.

When the problem space itself needs more option generation/comparison:
- return to the router;
- route to Brainstorming.

When an unresolved strategic/product choice requires user authority:
- persist the smallest exact decision question and relevant alternatives/evidence;
- this is a real user stop;
- do not let Planning silently choose.

When Definition Complete is GREEN:
- persist requirements/decisions/pointers;
- return to the router;
- Planning is the next normal role when a plan is required.

## Redefinition during active work

If execution/research reveals evidence that changes accepted requirements, strategic/high-level decisions, global product/system invariants, product/external behavior or an authorization boundary:

1. stop affected downstream work;
2. route to Definition for the changed product/system authority;
3. preserve provenance from the triggering evidence/blocker;
4. after Definition is accepted, route to Planning when the existing Master Plan is no longer valid;
5. otherwise return to the appropriate downstream role after reconciling affected contracts.

If accepted Project Definition remains valid and only milestone structure/order/outcome or execution strategy must change, route to Planning rather than reopening Definition.

Do not rewrite completed historical evidence merely because authority evolved.
