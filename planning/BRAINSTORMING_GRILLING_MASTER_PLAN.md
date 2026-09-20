# Master Plan — Brainstorming Grilling

Revision: `BGR-P2`
Status: `draft`
Updated: `2026-09-20`
Independent plan review: `RECOMMENDED`
Supersedes plan revision: `BGR-P1` — corrected OpenSpec boundary after independent review RED.

> Planning organizes the approved `requirements/BRAINSTORMING_GRILLING.md` Definition. Requirements and `ADR-BGR-001` remain product/system authority; this plan does not redefine them.

## 1. Accepted target / canonical inputs

- Requirements: `requirements/BRAINSTORMING_GRILLING.md` — `R1`, approved.
- Accepted decision: `decisions/ADR_BRAINSTORMING_GRILLING.md` — `ADR-BGR-001`.
- Exploratory provenance: `brainstorming/BRAINSTORMING_GRILLING.md` — `brainstorming-grilling@R1`, user-promoted.
- Workstream: `implementation/workstreams/feature-brainstorming-grilling/WORKSTREAM.yaml`.
- External pattern reference: Matt Pocock's public `grill-me` / `grilling` skills; no runtime dependency.

## 2. Execution baseline

- `workflow/chatgpt_only/BRAINSTORMING.md` and `workflow/codex_only/BRAINSTORMING.md` define Brainstorming goals, authority boundaries and Research/Definition exits but do not define dependency-aware grilling/frontier rounds.
- `workflow/chatgpt_only/INTAKE.md` and `workflow/codex_only/INTAKE.md` reserve explicit new-workstream intake for `#issue` and `#feature`.
- The routers distinguish explicit Intake directives from ordinary route selection.
- Existing Brainstorming → Project Definition promotion semantics are already explicit and must remain unchanged.
- Existing tests/docs should be extended rather than introducing a new lifecycle/state machine.

## 3. Inherited non-goals / invariants / external constraints

- Grilling is not a workflow phase, intake kind, workstream kind or authority layer.
- `#feature` remains the feature workstream entry directive; `#grill` only modifies interaction behavior for an active Brainstorming scope.
- Brainstorming remains tentative until Definition promotion.
- Agent-findable facts remain agent-owned work; user-facing grilling focuses on user/product/strategic decisions.
- Full transient decision trees are not required durable state.
- The user can stop grilling at any time; the workflow must not force low-value follow-up questions.
- `wait-what` localization/implementation is out of scope.
- ChatGPT-only and Codex-only must receive equivalent Brainstorming semantics without importing execution mechanics across policy namespaces.

## 4. Milestones

### M01 — Integrate dependency-aware grilling into Brainstorming

- Outcome: current Project Workflow Brainstorming supports conditional automatic grilling plus manual `#grill` forcing, while preserving existing lifecycle/authority boundaries and durable-state minimality.
- Checkpoint: policy-local contracts, routing/intake interpretation, tests and user-facing documentation agree on one coherent grilling behavior.
- Acceptance:
  - simple Brainstorming can remain lightweight;
  - materially ambiguous, multi-path or dependency-linked decisions trigger grilling without numeric thresholds;
  - the decision tree/frontier only exposes questions whose prerequisites are settled;
  - each frontier question is numbered and carries an assistant recommendation;
  - agent-findable facts are investigated rather than delegated back to the user;
  - answers cause frontier recomputation before dependent questions appear;
  - `#grill` forces the method for the active Brainstorming scope without creating Intake/workstream state;
  - full transient decision-tree persistence is not required, while durable recovery retains accepted choices/open material decisions/dependencies/research needs;
  - all material branches must be resolved or explicitly deferred/non-blocking for normal completion;
  - a clear user stop such as “dobra, wystarczy” stops grilling immediately and classifies the unresolved remainder by materiality;
  - Definition promotion rules remain unchanged;
  - `wait-what` remains outside scope;
  - regression tests prove the above semantics and existing Intake routing remains intact.
- Requirement coverage: BGR-REQ-001 through BGR-REQ-014.
- Dependencies: approved BGR R1 Definition and ADR-BGR-001.
- Inherited constraints / rationale:
  - `requirements/BRAINSTORMING_GRILLING.md`
  - `decisions/ADR_BRAINSTORMING_GRILLING.md`
- Planned work packages:
  - Create/reconcile one JIT OpenSpec change for the M01 changed behavior contract, covering dependency-aware Brainstorming grilling plus `#grill` non-Intake routing semantics, before implementing that behavior.
  - Update ChatGPT-only Brainstorming contract with conditional decision-tree/frontier method, recommendations, fact ownership, durable-state minimality and user-stop semantics.
  - Update Codex-only Brainstorming contract with equivalent semantics inside its own policy namespace.
  - Define `#grill` as a Brainstorming interaction directive and explicitly preserve `#issue` / `#feature` as the only Intake directives; adjust router/intake text only where needed to prevent misclassification.
  - Add/extend tests covering automatic trigger criteria, dependency ordering, recommendation requirement, fact ownership, `#grill` non-intake behavior, user-stop handling, durable-state expectations and promotion-gate preservation.
  - Update README/workflow-facing documentation/examples where needed so the user control surface and lifecycle distinction are discoverable.
- JIT decomposition / deferred-detail trigger: Execution Prep may split the planned work packages into bounded Cards according to actual test/document layout; no strategic detail depends on predecessor evidence.
- Planning re-evaluation trigger: implementation evidence shows the accepted behavior cannot be expressed without introducing a new lifecycle/state owner or materially restructuring Intake.
- Definition re-open trigger: implementation reveals that `#grill` must create/recover workstreams, that grilling must become a separate phase, or that any accepted BGR requirement cannot be preserved.
- Boundary gate / explicit user authorization: none beyond normal independent review gates.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Planned work package or JIT trigger | OpenSpec candidate |
|---|---|---|---|
| BGR-REQ-001 | M01 | Brainstorming + routing contracts | yes — shared M01 behavior contract |
| BGR-REQ-002 | M01 | Brainstorming trigger semantics + tests | yes — shared M01 behavior contract |
| BGR-REQ-003 | M01 | Lightweight-path semantics + tests | yes — shared M01 behavior contract |
| BGR-REQ-004 | M01 | `#grill` routing/non-intake semantics + tests | yes — shared M01 behavior contract |
| BGR-REQ-005 | M01 | Decision-tree/frontier contract + tests | yes — shared M01 behavior contract |
| BGR-REQ-006 | M01 | Frontier-round recommendation contract + tests | yes — shared M01 behavior contract |
| BGR-REQ-007 | M01 | Fact-ownership contract + tests | yes — shared M01 behavior contract |
| BGR-REQ-008 | M01 | Frontier recomputation contract + tests | yes — shared M01 behavior contract |
| BGR-REQ-009 | M01 | Durable-state minimality/recovery contract + tests | yes — shared M01 behavior contract |
| BGR-REQ-010 | M01 | Completion/deferred semantics + tests | yes — shared M01 behavior contract |
| BGR-REQ-011 | M01 | User-stop semantics + tests | yes — shared M01 behavior contract |
| BGR-REQ-012 | M01 | Remainder classification semantics + tests | yes — shared M01 behavior contract |
| BGR-REQ-013 | M01 | Promotion-gate preservation + regression tests | yes — shared M01 behavior contract |
| BGR-REQ-014 | M01 | Scope boundary/docs | no — scope boundary only |

## 6. Dependency / execution order

Within M01, Execution Prep may create multiple Cards but must preserve this logical order where dependencies require it:

1. JIT OpenSpec reconciliation for the exact M01 changed behavior contract;
2. contract semantics for Brainstorming and manual forcing;
3. router/intake wording needed to distinguish `#grill`;
4. tests against the resulting exact contract surface and OpenSpec requirements;
5. documentation/readme alignment;
6. integrated verification across both policy-local namespaces.

Contract and tests may be developed together when a bounded Card can verify them without crossing review/write-scope boundaries.

## 7. Deployment / migration / rollback strategy

- Documentation/workflow-contract change only; no data migration or live deployment gate.
- Existing projects/workstreams remain valid because no new mandatory mutable state is introduced.
- Rollback is ordinary Git revert of the feature changes if integration verification fails.
- Do not require migration of historical Brainstorming records to a serialized decision-tree format.

## 8. System verification strategy

Verification must include:

- OpenSpec-to-implementation consistency for the M01 changed behavior contract, including the non-Intake `#grill` routing boundary;
- static/content tests proving the new required semantics exist in the appropriate policy-local contracts;
- routing/intake regression tests proving `#feature` / `#issue` behavior remains unchanged and `#grill` is not treated as new-workstream Intake;
- scenario-style tests for:
  - lightweight Brainstorming;
  - automatic grilling from dependent decisions;
  - manual `#grill`;
  - question dependency ordering;
  - recommendations on frontier questions;
  - agent-owned fact lookup;
  - user-requested early stop;
  - blocking versus non-blocking remainder classification;
  - recovery without a full persisted decision tree;
  - unchanged explicit Definition promotion gate;
- existing relevant repository test suites to catch broader router/workflow regressions.

## 9. Idempotency / data-integrity / security strategy

- Repeated `#grill` for the same active Brainstorming scope changes interaction mode only and must not create duplicate durable workstreams/authority.
- Durable records remain concise recovery state, not a transcript or hidden second authority source.
- No new credentials, remote execution, external writes or security-sensitive runtime behavior are introduced.

## 10. Explicit authorization boundaries

- No deployment/live-write authorization is required.
- Existing user-owned Brainstorming → Project Definition promotion semantics remain authoritative and unchanged.
- Independent plan/implementation/final-integration review gates follow normal ChatGPT-only workflow rules.

## 11. JIT / deferred decomposition map

Execution Prep may decide exact Card boundaries after reading current tests and contract file layout. It may split contract, tests and documentation into separate Cards if write scopes or reviewability benefit. It must not reinterpret the accepted trigger criteria, `#grill` semantics, persistence boundary or user-stop behavior.

M01 requires one JIT OpenSpec behavior-contract change. Execution Prep reconciles that change against current HEAD, the exact authority slice and the concrete Task Card immediately before implementation, rather than freezing distant file-level detail in Planning.

## 12. Fresh-context boundaries

- The independent plan review is a natural fresh-context boundary.
- Later Card/final-integration reviews follow normal ChatGPT-only review semantics.
- No extra context-health handoff is planned solely because the work crosses policy-local contract files.

## 13. Pre-implementation planning audit

- Definition Complete still GREEN: yes; BGR R1 is approved and ADR-BGR-001 is accepted.
- False assumptions / P0/P1 risks: primary risk is accidental creation of a third Intake directive or new lifecycle; the plan explicitly forbids both.
- Milestone boundaries/order: one integrated milestone is sufficient because all changes form one coherent workflow behavior and can be verified together.
- Dependency completeness: contract semantics precede/own router wording, tests and docs; no external runtime dependency exists.
- Outcome-level acceptance: complete and traceable to all BGR requirements.
- Requirement coverage: BGR-REQ-001..014 each map to M01 and a planned work package.
- Migration/rollback: no data migration; historical Brainstorming remains valid.
- System verification: scenario and regression coverage specified.
- Data integrity/idempotency/security: no new mutable authority or security surface; repeated manual trigger must be idempotent with respect to durable workstream state.
- Authorization gates: no new gates; Definition promotion remains unchanged.
- OpenSpec boundaries: M01 is a changed behavior contract and therefore requires one JIT OpenSpec change covering the Brainstorming grilling semantics plus `#grill` non-Intake routing boundary; concrete spec/task detail remains deferred to Execution Prep.
- Overengineering/premature detail: exact file/test patch boundaries deferred to Execution Prep.
- Remaining blockers: none.

Planning audit verdict: GREEN.

## 14. Workflow references

- Policy router: `workflow/CONTEXT_ROUTING.md`
- ChatGPT-only Planning: `workflow/chatgpt_only/PLANNING.md`
- ChatGPT-only Brainstorming: `workflow/chatgpt_only/BRAINSTORMING.md`
- Codex-only Brainstorming: `workflow/codex_only/BRAINSTORMING.md`
- ChatGPT-only Intake: `workflow/chatgpt_only/INTAKE.md`
- Codex-only Intake: `workflow/codex_only/INTAKE.md`
- OpenSpec: `workflow/common/OPENSPEC.md`

The Master Plan is not the live task tracker. Mutable implementation state will belong to the workstream-selected Task Board after Execution Prep.
