# ChatGPT-only Project Definition

This policy-local module owns Definition transitions after `execution_policy: chatgpt_only` is selected.

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
- relevant verified research/evidence;
- existing accepted requirements and decisions when redefining an active project;
- current project/source/external baseline only when it materially constrains the definition.

Do not load implementation-state machinery merely to define a new project unless active-state compatibility is itself part of the definition.

## Authority distinctions

Keep verified facts/external constraints, accepted requirements, accepted strategic decisions and open questions separate. Definition may formalize unambiguous consequences of accepted intent and verified hard constraints, but must not invent user/product choices.

## Definition workflow

1. Recover current accepted goal and existing Definition authority.
2. Read only relevant brainstorming/research/evidence.
3. Separate facts, explicit user choices, requirements, strategic decisions and unresolved questions.
4. Draft/reconcile canonical requirements.
5. Create/reconcile accepted decision records for material strategic choices.
6. Preserve constraints, non-goals, invariants, external contracts and acceptance-level outcomes.
7. Check for contradictions.
8. Resolve or surface every question that can materially alter planning.
9. Mark canonical requirements `approved` only when Definition Complete passes.
10. Return to the selected policy router.

## Definition Complete gate

Definition is ready for planning only when goal/target state, MUST requirements, boundaries, invariants, acceptance outcomes and required strategic choices are explicit; material Research uncertainty is resolved/non-blocking; no unresolved user/product choice can change milestone architecture; and canonical requirements are coherent and approved.

## Route transitions

When more evidence is required, persist the exact open question/evidence need and create one exact obligation under `workflow/chatgpt_only/RESEARCH.md#Durable record contract` with Origin role `project_definition`, exact Definition subject, Return target `project_definition:<exact subject>`, and reconciliation pending. Use `PROJECT.md → Active research obligation` for pre-execution Definition; use Task Board `research_obligation` for active implementation/recovery Definition. Persist record + owning pointer before yielding.

When that record becomes complete for this Definition subject, use `workflow/chatgpt_only/RESEARCH.md#Final Return-target protocol`. Reconcile findings into requirements/decisions/open questions and persist those target mutations together with `Return reconciliation: applied` + exact result refs. Only then consume/clear. Recovery from applied+complete must not repeat Definition mutation.

When broader option generation/comparison is needed, return to Brainstorming.

When user/product authority is required, persist the smallest exact decision question and stop for that authority.

When Definition Complete is GREEN, persist requirements/decisions/pointers and return to the policy router; Planning is the normal next role when needed.

## Redefinition during active work

If new evidence changes accepted requirements, strategic decisions, global invariants, external behavior or authorization boundaries, stop affected downstream work and return to Definition. If Definition remains valid and only milestone/execution strategy must change, return to Planning instead.

