# YAGNI / Proportional Design Requirements

Revision: `R1`
Status: `approved`
Updated: `2026-09-21`

## Goal / target state

Project Workflow has one policy-neutral engineering invariant that prevents speculative overengineering across its lifecycle while preserving all complexity required by current accepted authority, verified evidence and current quality obligations.

The invariant must help Brainstorming, Definition, Planning, Execution Prep, implementation and independent review distinguish justified present complexity from hypothetical future-proofing without adding a new workflow phase, score, registry or approval gate.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| YAGNI-REQ-001 | Project Workflow MUST prefer the least-complex solution that fully satisfies the complete applicable current requirements, accepted decisions, constraints, invariants and verified evidence. | MUST | `yagni-overengineering-guard@R3`; ADR-YAGNI-001 | accepted |
| YAGNI-REQ-002 | Project Workflow MUST NOT introduce speculative abstractions, generality, extensibility, configuration, dependencies, infrastructure, compatibility paths or future-proofing solely for hypothetical future needs. | MUST | `yagni-overengineering-guard@R3`; research `yagni-practices-r1` | accepted |
| YAGNI-REQ-003 | Every material increase in solution complexity MUST have a concrete current justification traceable to accepted authority, verified evidence, an existing current contract/constraint, or demonstrated current reuse/variation. | MUST | `yagni-overengineering-guard@R3`; ADR-YAGNI-001 | accepted |
| YAGNI-REQ-004 | YAGNI MUST NOT be used to omit or weaken correctness, security, testing, maintainability/refactoring, compatibility, observability, migration or other obligations that are required by the current applicable authority/evidence surface. | MUST | research `yagni-practices-r1`; ADR-YAGNI-001 | accepted |
| YAGNI-REQ-005 | “Simplest” MUST mean least unnecessary complexity while preserving the full applicable authority/acceptance surface; it MUST NOT be interpreted as shortest code, fewest files or minimum immediate effort. | MUST | `yagni-overengineering-guard@R3` | accepted |
| YAGNI-REQ-006 | Project Workflow SHOULD prefer an existing fitting mechanism/helper/platform capability over new machinery when it satisfies current authority cleanly; new machinery remains valid when current requirements/evidence justify it. | SHOULD | research `yagni-practices-r1` | accepted |
| YAGNI-REQ-007 | Generalization/abstraction MUST be justified by demonstrated current shared need/variation or another concrete current constraint, not merely by possible future reuse. Temporary duplication MAY be preferable to a premature/wrong abstraction while the real variation is still unknown. | MUST | research `yagni-practices-r1`; ADR-YAGNI-001 | accepted |
| YAGNI-REQ-008 | Changes SHOULD remain focused on the accepted current obligation; unrelated cleanup/refactoring MUST NOT be bundled unless it is required by the current change or another explicit accepted obligation. | SHOULD | research `yagni-practices-r1` | accepted |
| YAGNI-REQ-009 | The workflow MUST NOT create a YAGNI-specific lifecycle phase, gate, complexity score/budget, numeric abstraction threshold, registry or other durable state mechanism unless a later concrete requirement independently justifies one. | MUST | `yagni-overengineering-guard@R3`; ADR-YAGNI-001 | accepted |
| YAGNI-REQ-010 | Planning and independent review MUST be able to challenge material complexity by asking which current requirement, accepted constraint, verified evidence, existing contract or demonstrated current reuse justifies it. | MUST | research `yagni-practices-r1`; ADR-YAGNI-001 | accepted |

## Constraints

- The rule is policy-neutral and must apply consistently across migrated execution-policy namespaces without copying divergent versions of the invariant.
- Existing authority precedence remains unchanged: YAGNI cannot override accepted requirements/decisions, safety/security constraints, compatibility obligations or verified hard constraints.
- Known current compatibility, security/safety, migration, integration and measured performance/capacity constraints count as present justification when supported by accepted authority/evidence.
- Existing bounded workflow machinery should be reused; the feature should not add a parallel anti-overengineering subsystem.

## Non-goals

- Forcing the fewest lines/files regardless of correctness or maintainability.
- Banning abstraction, extensibility, dependencies, infrastructure or compatibility work when current requirements justify them.
- Defining a numeric “rule of three” or other universal call-site threshold for abstractions.
- Creating a complexity scoring system, budget, registry or new approval gate.
- Replacing DRY, refactoring discipline, security review, test requirements or existing acceptance obligations.
- Automatically removing unrelated existing complexity outside the current accepted change scope.

## Global invariants

- Accepted authority and verified current evidence outrank simplicity preferences.
- Additional complexity must earn its place from a current need, not an imagined future one.
- YAGNI protects proportional design; it does not reduce current quality obligations.
- Abstractions should emerge from demonstrated current concepts/variation rather than speculative reuse.
- The anti-overengineering mechanism itself must remain proportionate and reuse existing workflow roles/state.

## External contracts / dependencies

- No runtime dependency is introduced.
- Research evidence is recorded in `research/YAGNI_PRACTICES_R1.md` and includes Martin Fowler, Google Engineering Practices and sampled public agent/repository guidance.
- Existing policy-neutral authority and policy-local planning/execution/review contracts are the intended integration surface.

## Data integrity / idempotency / security constraints

- The invariant must not weaken existing security, compatibility, migration, recovery or review guarantees.
- Reapplying the rule must not create duplicate gates/state or require new durable bookkeeping.
- Existing accepted project authority remains the source of truth for whether complexity is currently required.

## Acceptance-level requirements

- A planner can reject an extra abstraction/config/plugin point whose only justification is a hypothetical future use.
- A planner can retain a complex mechanism when a current accepted requirement or verified hard constraint requires it.
- An executor/reviewer does not interpret YAGNI as permission to skip required tests, security behavior, compatibility or necessary refactoring.
- Review can ask for the concrete present justification for material complexity and treat “maybe later” alone as insufficient.
- A premature generic abstraction may be deferred while concrete current cases remain insufficient to establish its stable shape.
- Existing fitting mechanisms are preferred when adequate, without forbidding new mechanisms that are concretely justified.
- No YAGNI-specific state machine, scoring system or numeric abstraction threshold is introduced.
- Both migrated fixed-policy routes consume the same policy-neutral invariant rather than maintaining competing copies.

## Definition completeness

Definition Complete = GREEN:
- target state and all material MUST requirements are explicit;
- non-goals and authority/quality guardrails are explicit;
- policy-neutral scope and cross-policy consistency are explicit;
- research uncertainty is resolved and non-blocking;
- ADR-YAGNI-001 captures the strategic integration decision;
- no unresolved user/product choice can materially alter planning.

## Downstream coverage

Planning must map YAGNI-REQ-001 through YAGNI-REQ-010 to:
- one canonical policy-neutral invariant location;
- the smallest policy-local planning/execution/review integration needed to make the invariant operational;
- regression/contract tests proving both anti-speculation behavior and quality/authority guardrails;
- user/workflow documentation where discoverability materially benefits the control surface.

Execution Prep must avoid duplicating the rule across files when exact common authority references are sufficient.
