# Brainstorm — Decision-tree grilling in Project Workflow

Date: `2026-09-20`
Scope ID: `brainstorming-grilling`
Revision: `R1`
Status: `ready_for_definition`

## Problem / goal

Strengthen Project Workflow Brainstorming so the agent systematically exposes unresolved product/design decisions instead of stopping after a shallow question set or silently choosing downstream branches.

The inspiration is Matt Pocock's `grill-me` / `grilling` pair:
- https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me
- https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling

This scope is about the underlying interviewing method, not copying the upstream skill verbatim.

## Current understanding

### Verified facts

- Our ChatGPT-only and Codex-only Brainstorming contracts already require clarification of problem/current state/target state/constraints, separation of facts/decisions/assumptions, identification of open questions/research needs, and delayed architecture freeze.
- They do not currently define a decision-tree model, dependency-aware question frontier, or round-by-round recomputation of unresolved decisions.
- Upstream `grill-me` is intentionally a tiny user-invoked wrapper. Its body only invokes the separate `grilling` skill.
- Upstream `grilling` contains the real behavior: design tree, current frontier, whole-frontier rounds, numbered questions, a recommended answer per question, agent-owned fact finding, user-owned decisions, and completion only when the frontier is empty.
- Upstream separates invocation policy from reusable behavior: `grill-me` has implicit invocation disabled while `grilling` remains model-reachable.
- Upstream `wait-what` is a separate explicitly invoked repitch tool. It asks the agent to re-explain the prior message with missing context, ASD-STE100 Simplified Technical English, and project ubiquitous language from `CONTEXT.md`.

### Existing accepted decisions

- Brainstorming is exploratory and must not become accepted requirement/decision authority.
- User-owned promotion into Project Definition remains a separate gate.
- Facts/research should be obtained by the agent when available; product/strategic decisions belong to the user.
- Project Workflow should preserve progressive disclosure and avoid unnecessary duplicate machinery.

### Explicit user/product choices from this exploration

- Grilling is **not** a new workflow phase. It is a mechanism inside Brainstorming.
- Use the decision-tree/frontier method conditionally rather than for every trivial Brainstorming session.
- Automatically enter grilling when there are dependent user decisions, material ambiguity in the goal, or multiple meaningfully different solution paths. Do not use a numeric question threshold.
- Provide an explicit manual `#grill` control that forces grilling for the currently active Brainstorming scope only. It does not create a workstream and is not a new intake kind.
- Every frontier decision question should include the assistant's recommended answer.
- Facts that the agent can establish itself are the agent's responsibility; frontier questions presented to the user should focus on genuine user/product/strategic decisions.
- Do not persist the full working decision tree by default. Persist only the durable choices, unresolved decisions, material dependency relations, and research needs required to recover the Brainstorming state.
- Normal grilling completion requires all material branches to be resolved or explicitly classified as deferred/non-blocking.
- The user may explicitly stop grilling at any time with natural language such as “dobra, wystarczy”. The agent must stop instead of continuing low-value questioning. Remaining items are then classified: material blockers keep Brainstorming open; low-value/non-blocking items are recorded as deferred and do not prevent readiness.
- `wait-what` is outside this feature's scope. The user may separately adapt/install it as a Polish-language skill.

## Chosen direction

Integrate grilling semantics into the existing Brainstorming working method:

1. Keep one Brainstorming lifecycle. Grilling is an interaction method inside it, never a separate phase or authority layer.
2. Use lightweight Brainstorming for simple scopes.
3. Switch to decision-tree/frontier grilling when unresolved choices depend on one another, the goal is materially ambiguous, or multiple substantial solution paths exist.
4. Allow the user to force the method with `#grill` for the current Brainstorming scope.
5. Model unresolved decisions as a dependency-aware decision tree.
6. Compute the current **frontier**: unresolved user decisions whose prerequisites are already settled.
7. Resolve agent-findable facts without asking the user to research them.
8. Ask the whole currently independent frontier in one round.
9. Number every user decision question and include an explicit recommended answer.
10. Incorporate the user's answers, recompute the tree/frontier, and repeat only while material unresolved branches remain.
11. Persist concise durable outcomes rather than the full transient tree.
12. Stop automatically when all material branches are resolved or explicitly deferred/non-blocking.
13. Stop immediately when the user says the grilling is enough. Do not manufacture increasingly marginal questions merely to empty an internally generated tree.
14. After a user stop, classify any remainder by materiality. A real unresolved product/strategic blocker keeps Brainstorming open; merely marginal/non-blocking items may be deferred without preventing readiness for Definition.
15. Keep Brainstorming exploratory; accepted choices are recorded for later reconciliation by Project Definition.

## Alternatives rejected or narrowed

### Mandatory grilling for all Brainstorming

Rejected in favor of conditional use because trivial or obvious feature discovery should remain lightweight.

### Separate Grilling workflow phase

Rejected. The mechanism belongs inside Brainstorming and must not create another lifecycle or authority layer.

### `#grill` as intake/workstream creation

Rejected. `#feature` remains the feature-entry mechanism; `#grill` only changes the interaction mode of an already active Brainstorming scope.

### Persist the complete decision tree

Rejected as unnecessary durable telemetry. The tree is working state; durable records retain only the information required for recovery and later Definition.

### Include `wait-what` in this feature

Rejected from this scope. It is a separate communication/repitch capability rather than Brainstorming lifecycle behavior.

## Research needed

No blocking research identified.

## Open questions

No material product questions remain for this scope.

## Outcome of this session

- Tentative conclusions: conditional decision-tree/frontier grilling inside Brainstorming, explicit `#grill` force control, recommendation with every decision question, agent-owned fact finding, concise durable state, and a user-controlled early-stop escape hatch.
- Explicit user/product choices to promote through Project Definition: all choices in the section above.
- Research still needed: none blocking.
- Open questions: none material.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `user_authorized`
- Definition promotion subject: `brainstorming-grilling@R1`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`. This exact scope/revision was explicitly promoted by the user.
