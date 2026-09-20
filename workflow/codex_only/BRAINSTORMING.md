# Codex-only Brainstorming

This policy-local module owns Brainstorming transitions after `execution_policy: codex_only` is selected.

## Goal

Explore the problem space without accidentally converting possibilities into requirements or decisions.

## Canonical location

Project brainstorming lives in `brainstorming/`.

Use `templates/BRAINSTORM.md` for substantial sessions and `templates/OPEN_QUESTIONS.md` for unresolved questions when those templates are useful.

## Non-negotiable distinction

**BRAINSTORMING != DECISION.**

Brainstorming may contain:
- ideas;
- alternatives;
- hypotheses;
- experiments;
- pros/cons;
- assumptions to verify;
- rejected or merely considered directions.

Nothing in `brainstorming/` becomes authoritative merely because it was written down or discussed repeatedly.

When the user explicitly accepts an individual choice during exploration, preserve it in the active brainstorming record as an explicit user/product choice to be reconciled by Project Definition later. Acceptance of one choice does **not** by itself authorize leaving Brainstorming when the selected policy owns a separate phase-promotion gate. Do not make Brainstorming a second requirements/planning writer.

Do not rewrite history to make old brainstorming look settled.

## Working method

1. Clarify the problem, current state, target state and constraints.
2. Separate known facts, user decisions, assumptions and implementation-time choices.
3. Identify open questions and research needs.
4. Compare options only at the level justified by current evidence.
5. Delay freezing architecture until adequate verification exists.
6. Persist useful tentative work in the project repository so chat length is not project memory.

Read only already accepted requirements/decisions and source/project context that actually constrain the exploration. Do not load implementation-state machinery unless the question depends on current execution state.

## Durable active scope

Once exploration is durable managed-change state, an exact selected Codex-only workstream manifest already exists under the branch-first entry contract. Create/reconcile the exact brainstorming record first, then set manifest `routing.exploratory_scope` to that repository-relative record path in the same durable transition when practical. The record owns `Scope ID`, `Revision`, status and Definition-promotion fields; the manifest is locator-only.

A fresh coordinator context recovers the active exploratory scope from selected manifest `routing.exploratory_scope`, validates that locator through `WORKSTREAMS.md`, then reads only the pointed record. Never mirror this locator into root `PROJECT.md`. A missing/mismatched locator for otherwise-live exploratory state is Recovery, not permission to guess another record.

## Exit conditions

Move to Research when claims require verification.

Before yielding, create one exact obligation under `workflow/codex_only/RESEARCH.md#Durable record contract` with Origin role `brainstorming`, exact exploratory `<scope-id>@<revision>`, Return target `brainstorming:<scope-id>@<revision>`, reconciliation pending, and set the selected workstream manifest `routing.research_obligation` to that exact record. Persist the record + locator before returning to the router.

When that record becomes complete for this Brainstorming subject, use `workflow/codex_only/RESEARCH.md#Final Return-target protocol`. The target mutation is the exact exploratory-record reconciliation. Persist it together with `Return reconciliation: applied` + exact result ref; only then consume/clear. Recovery from applied+complete must not reapply findings or create another brainstorming revision.

When enough facts and accepted choices exist to formalize authoritative requirements/decisions and target state, Brainstorming may become **ready for Project Definition**.

Readiness is not itself authority to leave the exploratory phase. The selected policy route owns the promotion boundary. If that route requires explicit user promotion, persist the ready state and stop until the user authorizes Project Definition.

Do not treat research completion, repeated agreement in discussion, or the assistant's confidence that the idea is mature as implicit phase-promotion authority.

Do not create canonical requirements/decisions, a Master Plan, implementation Task Cards or detailed OpenSpec merely because ideas are becoming concrete.
