# Brainstorming Grilling Requirements

Revision: `R1`
Status: `approved`
Updated: `2026-09-20`

## Goal / target state

Project Workflow Brainstorming can use a dependency-aware grilling method to expose and resolve material user/product/strategic decisions without creating a new workflow phase or authority layer. Lightweight Brainstorming remains lightweight, while ambiguous or decision-dependent scopes gain a structured frontier-based interview.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| BGR-REQ-001 | Grilling MUST remain an interaction method inside Brainstorming and MUST NOT become a separate workflow phase, intake kind, or authority layer. | MUST | `brainstorming-grilling@R1`; ADR-BGR-001 | accepted |
| BGR-REQ-002 | Brainstorming MUST automatically use grilling when unresolved user decisions depend on one another, the goal is materially ambiguous, or multiple materially different solution paths exist; it MUST NOT use a numeric question-count threshold. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-003 | Lightweight/simple Brainstorming MUST remain permitted without forcing the full grilling method. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-004 | A manual `#grill` directive MUST force grilling for the currently active Brainstorming scope only and MUST NOT create/recover a workstream or act as a new intake directive. | MUST | `brainstorming-grilling@R1`; ADR-BGR-001 | accepted |
| BGR-REQ-005 | Grilling MUST model material unresolved user decisions as a dependency-aware decision tree and compute the current frontier from decisions whose prerequisites are already settled. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-006 | Each frontier round MUST ask the currently independent material user decisions together, number the questions, and include an explicit assistant recommendation for each. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-007 | Facts the agent can establish through permitted research/tools MUST remain agent-owned work rather than questions delegated to the user; user-facing frontier questions SHOULD focus on genuine user/product/strategic decisions. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-008 | After each user round, the agent MUST incorporate the answers and recompute the decision tree/frontier before asking dependent questions. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-009 | The workflow MUST NOT require persistence of the full transient decision tree. Durable Brainstorming state MUST preserve accepted choices, unresolved material decisions, material dependency relations, and research needs sufficient for recovery. | MUST | `brainstorming-grilling@R1`; ADR-BGR-001 | accepted |
| BGR-REQ-010 | Normal grilling completion MUST require every material branch to be resolved or explicitly classified as deferred/non-blocking. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-011 | The user MUST be able to terminate grilling at any time through clear natural language such as “dobra, wystarczy”; the agent MUST stop asking further grilling questions rather than manufacture lower-value questions. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-012 | After user-requested termination, unresolved material blockers MUST keep Brainstorming open, while marginal/non-blocking items MAY be recorded as deferred without preventing `ready_for_definition`. | MUST | `brainstorming-grilling@R1` | accepted |
| BGR-REQ-013 | Grilling MUST preserve the existing Brainstorming → Project Definition promotion gate; accepted choices recorded during grilling are not canonical requirements/decisions until Definition reconciles them. | MUST | existing Brainstorming authority; `brainstorming-grilling@R1` | accepted |
| BGR-REQ-014 | `wait-what` / repitch behavior MUST remain outside this feature scope. | MUST | `brainstorming-grilling@R1` | accepted |

## Constraints

- Preserve existing Brainstorming/Research/Definition authority boundaries.
- Preserve `#feature` as feature workstream intake; `#grill` is not an Intake directive.
- Apply equivalent grilling semantics to policy-local Brainstorming routes where those routes own Brainstorming behavior, without importing execution-policy semantics between namespaces.
- Keep durable state concise enough to support progressive disclosure and fresh-session recovery.

## Non-goals

- Creating a standalone Grilling lifecycle phase.
- Creating a new workstream type for grilling.
- Persisting every node/branch of the transient decision tree.
- Implementing or localizing the upstream `wait-what` skill.
- Copying the upstream skill verbatim or depending on it at runtime.

## Global invariants

- Brainstorming remains non-authoritative until Project Definition promotes accepted intent.
- User/product/strategic choices remain user-owned.
- Researchable facts remain agent-owned work when they can be established through permitted tooling/evidence.
- Manual `#grill` changes interaction behavior only; it does not alter workstream identity or execution policy.
- A user-requested stop must not be overridden by an internal desire to exhaust the tree.

## External contracts / dependencies

- Inspired by Matt Pocock's public `grill-me` / `grilling` productivity skills, but no runtime dependency is required.
- Existing Project Workflow policy-local Brainstorming contracts remain the integration surface.

## Data integrity / idempotency / security constraints

- A repeated/manual `#grill` instruction for the same active scope must not create duplicate workstreams or duplicate Definition authority.
- Durable recovery must reconstruct material unresolved decisions without requiring the full previous chat transcript.

## Acceptance-level requirements

- A simple Brainstorming example can remain lightweight without triggering grilling.
- An ambiguous/dependency-heavy example triggers a frontier round with numbered decision questions and recommendations.
- A dependent question is not asked before its prerequisite decision is settled.
- Agent-findable facts are researched rather than asked back to the user.
- `#grill` during active Brainstorming forces the method without creating new Intake/workstream state.
- “Dobra, wystarczy” stops further grilling; remaining items are classified by materiality.
- A fresh chat can recover enough durable state to continue without a serialized full decision tree.
- Existing explicit promotion into Project Definition remains required.

## Definition completeness

Definition Complete = GREEN:
- target state and material MUST requirements are explicit;
- constraints, non-goals and invariants are captured;
- acceptance-level outcomes are sufficient for planning;
- the strategic integration decision is captured in ADR-BGR-001;
- no unresolved user/product choice remains that can materially alter the target definition.

## Downstream coverage

Planning must map these requirements to workflow-contract changes, tests, documentation/examples and branch-isolated execution packages.
