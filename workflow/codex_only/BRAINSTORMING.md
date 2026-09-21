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

## Adaptive grilling interaction method

Adaptive grilling is the default interaction method inside every Brainstorming scope. It is **not** a separate workflow phase, Intake kind, workstream kind or authority layer, and no entry route or manual operator directive controls whether it applies.

Depth is proportional to the expected decision value of another sensible round. A genuinely simple scope may finish after one short user round when the completion audit finds no further material decision value. Do not manufacture low-value questions merely to increase depth, and do not use a fixed minimum/maximum question count or round count. Having enough information to implement is **not** by itself a Brainstorming completion condition.

### Decision surface, tree and frontier

During Brainstorming:

1. Model material unresolved **user/product/strategic decisions** as a transient dependency-aware decision tree.
2. Search the relevant decision surface with adaptive internal lenses such as goal/non-goals, user/UX, scope, architecture/interfaces, data/state, dependencies, failure/edge cases, migration/backward compatibility, security/operations and acceptance. Use only lenses that are relevant; do not turn them into a rigid user-facing checklist.
3. Keep agent-findable facts agent-owned. Establish them through permitted tools/evidence or the applicable Research route instead of delegating research to the user.
4. Compute the current **frontier** from material unresolved decisions whose prerequisites are already settled.
5. Select a coherent thematic batch from that frontier. Split a large frontier into digestible groups rather than dumping it at once. Number each material decision question and include an explicit assistant recommendation for it.
6. Incorporate the user's answers as exploratory accepted choices. Give each material settled choice one bounded adversarial/counterfactual challenge before treating it as stable exploratory state.
7. After every user round, Research reconciliation, challenge result or material reopening, recompute the decision tree/frontier before exposing dependent questions or declaring completion.
8. Continue while another sensible round has meaningful expected value for changing scope, UX, architecture, constraints, acceptance or important edge cases.

### Challenge stability and reopening

Once a material choice has received its bounded challenge, do not repeatedly reopen it merely to prolong exploration.

Reopen that choice only when materially new evidence, contradiction or changed context undermines it. Recompute any dependent branches/frontier when a choice reopens.

### Durable state and recovery

The full transient decision tree is working state and is not required durable authority.

Persist only enough Brainstorming state for fresh-session recovery:
- accepted exploratory choices;
- unresolved material decisions;
- material dependency relations between those decisions;
- challenge/reopening state when needed to avoid duplicate challenge churn;
- research needs/evidence obligations.

This durable state remains exploratory and must not become a second requirements/decision authority or a persisted conversation transcript.

### Completion and user-requested stop

Before normal completion, perform a bounded completion audit across the relevant decision surface and one final challenge/discovery pass. Completion is allowed only when another sensible round has low expected value for changing material scope, UX, architecture, constraints, acceptance or important edge cases.

A clear natural-language user stop such as “dobra, wystarczy” halts new Brainstorming questions immediately. Do not manufacture lower-value follow-ups after that stop. Then classify the unresolved remainder:
- unresolved material product/strategic blockers keep the exploratory scope tentative and prevent it from being treated as ready to leave Brainstorming;
- marginal/non-blocking items may be recorded as deferred.

Stopping questions does not authorize a downstream phase transition and does not bypass the active route's existing promotion/authority boundary.

## Exit conditions

Move to Research when claims require verification.

Before yielding, create one exact obligation under `workflow/codex_only/RESEARCH.md#Durable record contract` with Origin role `brainstorming`, exact exploratory `<scope-id>@<revision>`, Return target `brainstorming:<scope-id>@<revision>`, reconciliation pending, and set the selected workstream manifest `routing.research_obligation` to that exact record. Persist the record + locator before returning to the router.

When that record becomes complete for this Brainstorming subject, use `workflow/codex_only/RESEARCH.md#Final Return-target protocol`. The target mutation is the exact exploratory-record reconciliation. Persist it together with `Return reconciliation: applied` + exact result ref; only then consume/clear. Recovery from applied+complete must not reapply findings or create another brainstorming revision.

When enough facts and accepted choices exist to formalize authoritative requirements/decisions and target state, Brainstorming may become **ready for Project Definition**.

Readiness is not itself authority to leave the exploratory phase. The selected policy route owns the promotion boundary. If that route requires explicit user promotion, persist the ready state and stop until the user authorizes Project Definition.

Do not treat research completion, repeated agreement in discussion, or the assistant's confidence that the idea is mature as implicit phase-promotion authority.

Do not create canonical requirements/decisions, a Master Plan, implementation Task Cards or detailed OpenSpec merely because ideas are becoming concrete.
