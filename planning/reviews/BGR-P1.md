# Independent Plan Review — Brainstorming Grilling

Plan revision: BGR-P1
Review requirement: RECOMMENDED
Review state: red
Review subject: dc6f532b0a4692257c7c16ff1f092d9e753f8190
Plan: planning/BRAINSTORMING_GRILLING_MASTER_PLAN.md
Requirements: requirements/BRAINSTORMING_GRILLING.md
Accepted decision: decisions/ADR_BRAINSTORMING_GRILLING.md
Project branch: feat/brainstorming-grilling
Review evidence: RED — the frozen subject is recoverable and otherwise preserves the approved BGR R1/ADR-BGR-001 authority, one-milestone coverage, non-Intake #grill semantics, promotion gate, user-stop behavior and routing/intake verification. The blocking plan defect is its OpenSpec boundary: section 5 marks BGR-REQ-001..014 as OpenSpec candidate "no" and the planning audit says no OpenSpec is required because this is workflow interaction/routing behavior. Current workflow/common/OPENSPEC.md says new/changed behavior contracts are normally justified for OpenSpec; M01 changes the policy-local Brainstorming behavior contract plus routing/non-Intake behavior across two namespaces. This is a bounded plan-only defect: Definition remains valid; Planning must create a new plan revision that treats the M01 behavior surface as an OpenSpec candidate/required JIT contract and includes corresponding verification/reconciliation semantics.

## Review objective

Independently verify the exact frozen BGR-P1 plan subject against the approved BGR R1 Definition and current Project Workflow contracts.

At minimum verify:
- grilling remains an interaction method inside Brainstorming rather than a new workflow phase, authority layer or Intake kind;
- automatic activation uses semantic ambiguity/dependency/multiple-path criteria rather than numeric thresholds;
- lightweight Brainstorming remains legal;
- `#grill` only forces the method for an active Brainstorming scope and does not create/recover workstreams;
- each frontier decision question requires an assistant recommendation;
- agent-findable facts remain agent-owned work;
- dependent questions are gated by prerequisite decisions and the frontier is recomputed after each user round;
- durable state does not require serializing the full transient decision tree, while remaining recoverable;
- user-requested stop behavior terminates grilling and classifies unresolved remainder by materiality;
- existing Brainstorming → Project Definition promotion remains unchanged;
- `wait-what` remains outside scope;
- the one-milestone plan covers BGR-REQ-001 through BGR-REQ-014 without hiding a Definition change;
- verification includes both policy-local Brainstorming contracts plus routing/intake regression coverage.

Treat this record as the canonical mutable plan-review state. Do not mutate the frozen Master Plan while reviewing it.
