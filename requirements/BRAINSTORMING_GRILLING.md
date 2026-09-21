# Brainstorming Grilling Requirements

Revision: `R2`
Status: `approved`
Updated: `2026-09-21`
Supersedes revision: `R1` — conditional/manual grilling semantics replaced by adaptive grilling as the default Brainstorming interaction method.

## Goal / target state

Every Project Workflow Brainstorming scope uses one adaptive, dependency-aware grilling method by default, regardless of entry path or execution-policy route. The method must explore material user/product/strategic decisions deeply enough to reduce downstream rework without manufacturing low-value questions or relying on a manual `#grill` trigger.

Depth is proportional to remaining decision value: a simple scope may finish after one short round, while a complex scope may legitimately require many rounds.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| BGR-REQ-001 | Grilling MUST remain an interaction method inside Brainstorming and MUST NOT become a separate workflow phase, intake kind, workstream kind, or authority layer. | MUST | `adaptive-brainstorming-grilling@R1`; ADR-BGR-002 | accepted |
| BGR-REQ-002 | Every active Project Workflow Brainstorming route MUST use adaptive grilling as its default interaction method, regardless of whether Brainstorming was entered through `#feature`, `#issue`, generic managed change, Research return, Recovery, legacy/mixed routing, or another legal route. | MUST | `adaptive-brainstorming-grilling@R1`; ADR-BGR-002 | accepted |
| BGR-REQ-003 | Grilling depth MUST be governed by the expected decision value of further questioning and MUST NOT use a fixed question-count or round-count threshold. Knowing enough to implement MUST NOT by itself be sufficient to end Brainstorming. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-004 | A genuinely simple Brainstorming scope MAY complete after one short round when the completion audit finds no further valuable material decisions; the workflow MUST NOT manufacture low-value questions merely to increase depth. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-005 | Brainstorming MUST model material unresolved user/product/strategic decisions as a dependency-aware decision tree and compute a current frontier from decisions whose prerequisites are settled. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-006 | The agent MUST search the relevant decision surface using adaptive internal lenses such as goal/non-goals, user/UX, scope, architecture/interfaces, data/state, dependencies, failure/edge cases, migration/backward compatibility, security/operations, and acceptance; these lenses MUST NOT become a rigid user-facing checklist. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-007 | User-facing frontier rounds MUST be thematic and digestible; questions MUST be numbered and each material decision question MUST include an explicit assistant recommendation. A large frontier MUST be split into coherent groups rather than dumped as one oversized question block. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-008 | After each user round, the agent MUST incorporate the answers and recompute the decision tree/frontier before exposing dependent questions or declaring completion. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-009 | Facts the agent can establish through permitted tools/evidence MUST remain agent-owned work. When a decision branch depends on such a fact, the workflow MUST use the applicable Research route, reconcile the result into the same exploratory subject/tree, and then resume Brainstorming rather than delegating the research to the user. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-010 | Each material settled user choice MUST receive one bounded adversarial/counterfactual challenge before being treated as stable exploratory state. The choice MUST NOT be repeatedly reopened without materially new evidence, contradiction, or changed context. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-011 | Materially new evidence, contradiction, or changed context that undermines a previously challenged choice MUST reopen that choice and recompute affected decision dependencies. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-012 | Before normal completion, the agent MUST perform a bounded completion audit across the relevant decision surface and one final challenge/discovery pass. Completion is allowed only when another sensible round has low expected value for changing scope, UX, architecture, constraints, acceptance, or important edge cases. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-013 | The user MUST be able to stop further Brainstorming questions immediately through clear natural language such as “dobra, wystarczy”. If unresolved material product/strategic blockers remain, Brainstorming MUST stay tentative and MUST NOT become `ready_for_definition`; non-blocking remainder MAY be deferred. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-014 | Durable Brainstorming state MUST preserve accepted exploratory choices, unresolved material decisions, material dependency relations, challenge/reopening state when needed for recovery, and Research needs sufficient for continuation; the workflow MUST NOT require persistence of the full transient decision tree or conversation transcript. | MUST | `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-015 | Adaptive grilling MUST preserve the existing Brainstorming → Project Definition promotion gate; exploratory choices do not become canonical requirements/decisions until Definition reconciles the explicitly promoted scope/revision. | MUST | existing Brainstorming authority; `adaptive-brainstorming-grilling@R1` | accepted |
| BGR-REQ-016 | `#grill` MUST be removed from the active Project Workflow interaction surface. Active routers, Intake contracts, Brainstorming contracts, current docs/examples/specs/tests MUST NOT present it as a supported operator directive or compatibility alias. Historical records MAY retain it as provenance. | MUST | `adaptive-brainstorming-grilling@R1`; ADR-BGR-002 | accepted |
| BGR-REQ-017 | Equivalent adaptive-grilling semantics MUST apply across all active Brainstorming routes, including ChatGPT-only, Codex-only, and legacy/mixed routing, while each policy route retains its own Research/recovery/execution mechanics. | MUST | `adaptive-brainstorming-grilling@R1`; ADR-BGR-002 | accepted |
| BGR-REQ-018 | `wait-what` / repitch behavior MUST remain outside this feature scope. | MUST | prior BGR scope; `adaptive-brainstorming-grilling@R1` | accepted |

## Constraints

- Preserve existing Brainstorming/Research/Definition authority boundaries and user-owned Definition promotion.
- Preserve `#issue` / `#feature` Intake semantics; adaptive grilling is intrinsic to Brainstorming rather than an Intake command.
- Do not introduce a numeric depth quota, generic questionnaire engine, new lifecycle phase, or new mutable global state.
- Keep policy-local routing mechanics isolated even where Brainstorming interaction semantics are equivalent.
- Keep durable exploratory state concise enough for progressive disclosure and fresh-session recovery.

## Non-goals

- Reproducing the upstream `grill-me` skill verbatim.
- Forcing dozens or hundreds of questions when further questions have low expected decision value.
- Creating a standalone Grilling lifecycle phase or workstream type.
- Persisting every transient decision-tree node or every user/assistant turn.
- Implementing/localizing `wait-what`.
- Changing Project Definition promotion authority or execution-policy selection.

## Global invariants

- Brainstorming remains non-authoritative until Project Definition promotes accepted intent.
- User/product/strategic choices remain user-owned.
- Researchable facts remain agent-owned work when they can be established through permitted tooling/evidence.
- Entry route does not change Brainstorming interaction depth semantics.
- No fixed question/round count determines completion.
- User-requested stop always stops new questions immediately.
- Unresolved material blockers cannot be hidden by user-stop handling or by an agent claiming implementation readiness.
- New material evidence can reopen previously settled exploratory choices.

## External contracts / dependencies

- Inspired by Matt Pocock's public `grill-me` / `grilling` productivity skills, but no runtime dependency is required.
- Integration surfaces include current ChatGPT-only, Codex-only, and legacy/mixed Brainstorming routing/contracts.
- Existing Research return and Definition promotion contracts remain authoritative for phase transitions.

## Data integrity / idempotency / security constraints

- Re-entering or recovering the same Brainstorming subject MUST NOT create duplicate workstreams, duplicate Definition authority, or a second decision tree authority source.
- Research return MUST reconcile into the same exploratory subject exactly once under the owning Research contract.
- A completion audit/challenge pass MUST NOT rewrite already accepted canonical Definition authority; it operates only on exploratory state before promotion.
- No new credentials, privileged access, external live-write behavior, or security-sensitive runtime surface is introduced.

## Acceptance-level requirements

- A simple Brainstorming example uses adaptive grilling and may complete after one short round only after its completion audit finds no further material decision value.
- A complex or dependency-heavy example proceeds through multiple thematic rounds, recomputing the frontier after each round.
- A downstream-dependent question is not asked before its prerequisite is settled.
- Each material user decision question is numbered and contains a recommendation.
- A material settled choice receives one counterfactual challenge and remains stable absent new contradictory evidence.
- New evidence that changes a settled premise reopens the affected choice and downstream frontier.
- Agent-findable facts trigger agent-owned Research rather than being pushed to the user.
- A large frontier is split into coherent thematic batches.
- Apparent completion triggers a completion audit plus a final discovery/challenge pass; “we can implement now” alone does not end Brainstorming.
- “Dobra, wystarczy” stops further questions immediately; material unresolved blockers keep the scope tentative.
- No supported `#grill` command remains in active workflow surfaces.
- ChatGPT-only, Codex-only, and legacy/mixed Brainstorming paths expose equivalent adaptive interaction semantics.
- A fresh context can recover enough durable state to continue without a serialized full decision tree.
- Existing explicit promotion into Project Definition remains required.

## Definition completeness

Definition Complete = GREEN:
- target state and all material MUST requirements are explicit;
- constraints, non-goals, invariants, recovery/data-integrity expectations, and acceptance-level outcomes are captured;
- ADR-BGR-002 records the strategic replacement of conditional/manual grilling with adaptive default grilling;
- the old `#grill` operator surface is explicitly superseded rather than left ambiguous;
- all active Brainstorming route families are in scope;
- no unresolved user/product choice remains that can materially alter the target definition.

## Downstream coverage

Planning must map BGR-REQ-001..018 to:
- active Brainstorming/routing/Intake contract changes across the affected route families;
- removal of active `#grill` behavior;
- changed OpenSpec behavior authority;
- conversational/scenario and static contract tests that prove depth/completion semantics rather than only phrase presence;
- user-facing documentation/examples;
- branch-isolated implementation/review evidence.
