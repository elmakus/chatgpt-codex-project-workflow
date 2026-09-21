# Master Plan — Research Agent Behavior

Revision: `RAB-P1`
Status: `draft`
Updated: `2026-09-21`
Independent plan review: `RECOMMENDED`
Supersedes plan revision: `none`

> Planning organizes the approved `requirements/RESEARCH_AGENT_BEHAVIOR.md` Definition. Requirements and `ADR-RAB-001` remain product/system authority; this plan does not redefine them.

## 1. Accepted target / canonical inputs

- Requirements: `requirements/RESEARCH_AGENT_BEHAVIOR.md` — R1, approved.
- Accepted decision: `decisions/ADR_RESEARCH_AGENT_BEHAVIOR.md` — ADR-RAB-001.
- Exploratory provenance: `brainstorming/RESEARCH_AGENT_BEHAVIOR.md` — `research-agent-behavior@R2`, user-promoted.
- Workstream: `implementation/workstreams/feature-research-agent-behavior/WORKSTREAM.yaml`.

## 2. Execution baseline

- `workflow/common/RESEARCH.md` defines shared evidence/authority distinctions but does not explicitly require prior-art discovery.
- `workflow/chatgpt_only/RESEARCH.md` and `workflow/codex_only/RESEARCH.md` own policy-local continuation/routing semantics.
- `workflow/codex_only/RESEARCH.md` delegates concrete Investigator realization to `codex_workflow`; that boundary must remain unchanged.
- `templates/RESEARCH.md` contains stale ChatGPT-only pre-execution pointer commentary referring to root `PROJECT.md`; current policy-local routing uses selected workstream manifest `routing.research_obligation`.
- Existing tests include policy-local branch-first pre-execution/execution contracts; no focused Research investigation-quality contract test currently exists.

## 3. Inherited non-goals / invariants / constraints

- Research remains evidence, not accepted product/system authority.
- Exact Origin/Return-target and reconciliation lifecycle remain unchanged.
- External search is proportional; purely local/private facts do not force broad internet research.
- Community evidence may inform practical behavior but does not become authoritative by popularity.
- Project Workflow must not define the concrete Codex Investigator model/harness/session lifecycle.
- No new crawler, search service, state store or workflow phase is introduced.
- No root-level mutable Research pointer may be reintroduced.

## 4. Milestones

### M01 — Strengthen Research investigation quality and prior-art discovery

- Outcome: both fixed policies execute Research with one coherent proportional prior-art/source-quality contract, while current routing/runtime boundaries remain intact and shared template commentary is corrected.
- Dependencies: approved RAB R1 Definition and ADR-RAB-001.
- Requirement coverage: RAB-REQ-001 through RAB-REQ-010.
- Acceptance:
  - common/shared Research guidance explicitly requires external prior-art discovery when it is reasonably likely to materially help;
  - official/upstream, issue/discussion, comparable implementation and community evidence classes are distinguished with source-quality semantics;
  - conflicting/anecdotal evidence is surfaced and checked against stronger sources when practical;
  - purely local/private questions may skip broad web search when external prior art cannot materially help;
  - bounded stopping criteria prevent open-ended searching once the exact question is sufficiently answered;
  - both `chatgpt_only` and `codex_only` Research paths explicitly inherit/apply the same evidence-quality behavior;
  - Codex-only Investigator realization remains runtime-owned by `codex_workflow`;
  - `templates/RESEARCH.md` no longer claims ChatGPT-only pre-execution Research is rooted in `PROJECT.md`;
  - regression tests prove the positive prior-art case, proportional local-only case, source-quality distinction, policy parity, runtime-boundary preservation and pointer correction.
- Planned work packages:
  - Create/reconcile one JIT OpenSpec change for the changed Research behavior contract before implementation.
  - Update `workflow/common/RESEARCH.md` with the shared proportional prior-art/source-quality/stopping contract.
  - Update `workflow/chatgpt_only/RESEARCH.md` and `workflow/codex_only/RESEARCH.md` so each policy-local route explicitly applies the shared evidence behavior while retaining its own continuation semantics.
  - Preserve the Codex-only pre-dispatch/Investigator ownership boundary; do not add model/harness mapping to Project Workflow.
  - Correct `templates/RESEARCH.md` pointer commentary and align its evidence structure if needed without creating new routing semantics.
  - Add focused contract tests, preferably a bounded new Research behavior test file, and run relevant existing branch-first/pre-execution tests.
  - Update README/docs only if current user-facing Research documentation becomes inconsistent with the changed contract.
- JIT decomposition trigger: Execution Prep may split contract, template and tests into bounded Cards according to current file/test layout.
- Planning re-evaluation trigger: implementation evidence shows the shared/common contract cannot be applied by both policy-local routes without materially changing workflow topology.
- Definition re-open trigger: implementation would require changing Research authority ownership, adding a new workflow phase/state owner, or moving Codex runtime orchestration into Project Workflow.
- User/live authorization gate: none beyond normal independent review/integration gates.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Execution path | OpenSpec candidate |
|---|---|---|---|
| RAB-REQ-001 | M01 | shared + policy-local Research contract regression | yes — M01 Research behavior contract |
| RAB-REQ-002 | M01 | proportionality semantics + tests | yes |
| RAB-REQ-003 | M01 | prior-art trigger semantics + tests | yes |
| RAB-REQ-004 | M01 | evidence-class guidance + tests | yes |
| RAB-REQ-005 | M01 | source-quality/conflict handling + tests | yes |
| RAB-REQ-006 | M01 | evidence distinction preservation + tests | yes |
| RAB-REQ-007 | M01 | authority/return-boundary regression | yes |
| RAB-REQ-008 | M01 | both policy-local modules + runtime-boundary regression | yes |
| RAB-REQ-009 | M01 | stopping criteria + tests | yes |
| RAB-REQ-010 | M01 | template pointer correction + test | yes — same behavior/state-contract reconciliation |

## 6. Dependency / execution order

1. JIT OpenSpec reconciliation for the exact M01 Research behavior contract.
2. Shared/common Research evidence-quality semantics.
3. Policy-local ChatGPT-only and Codex-only application while preserving continuation/runtime boundaries.
4. Shared template correction.
5. Focused tests plus relevant existing regression suites.
6. Optional docs/readme alignment only if required by changed user-facing text.

Contract and tests may be developed together when bounded write scope and reviewability permit.

## 7. Deployment / migration / rollback

- Workflow-contract/documentation/test change only; no data migration or live deployment gate.
- Existing durable Research records remain valid because continuation fields/status semantics are unchanged.
- Historical workstreams require no migration.
- Rollback is ordinary Git revert if integrated verification fails.

## 8. System verification strategy

Verification must include:
- OpenSpec-to-contract consistency for the M01 changed behavior;
- static/content tests proving prior-art trigger, proportionality, source-quality and stopping semantics;
- parity checks across `chatgpt_only` and `codex_only`;
- regression proving Codex runtime ownership remains with `codex_workflow`;
- regression proving selected workstream manifest remains the ChatGPT-only pre-execution Research pointer owner;
- existing relevant branch-first/pre-execution tests;
- full repository test suite when practical before final integration.

## 9. Data integrity / idempotency / security

- No new mutable Research state is introduced.
- Existing complete/applied/consumed reconciliation semantics remain unchanged.
- External/public evidence must not cause private/secrets material to be copied into public artifacts without authorization.
- Repeated Research execution must not create duplicate reconciliation or a second authority path.

## 10. Explicit authorization boundaries

- No deployment/live-write authorization is required.
- Existing Brainstorming → Definition gate is already satisfied for this exact scope and is not modified by this feature.
- Independent plan, implementation and final-integration reviews follow normal ChatGPT-only workflow rules.

## 11. JIT / deferred decomposition map

Execution Prep owns exact Card boundaries and the concrete test file selection. M01 requires one JIT OpenSpec because this feature changes a workflow behavior contract across shared and policy-local surfaces. File-level implementation detail remains deferred until current HEAD is read immediately before execution.

## 12. Fresh-context boundaries

- The independent plan review is the next natural fresh-context boundary.
- Later Card/final-integration reviews use normal ChatGPT-only review semantics.
- No extra context-hygiene stop is introduced merely because common and policy-local files are touched.

## 13. Pre-implementation planning audit

- Definition Complete remains GREEN: yes.
- Requirement coverage: RAB-REQ-001..010 all map to M01 and an execution path.
- Milestone structure: one integrated milestone is sufficient; no independent deployment/migration checkpoint exists.
- P0/P1 risk: primary risk is overengineering Research into a mandatory broad web crawl or duplicating Codex runtime orchestration; both are explicitly prohibited.
- Dependency completeness: shared behavior contract precedes policy-local application, template alignment and verification.
- OpenSpec boundary: one JIT OpenSpec is justified because Research behavior is changing; no distant implementation spec is frozen now.
- Data integrity/idempotency/security: no new state model; existing reconciliation and private-data boundaries preserved.
- Migration/rollback: no migration; ordinary Git rollback.
- Authorization gates: no new user gate.
- Overengineering/premature detail: no crawler, service, source-ranking engine or fixed exhaustive checklist is planned; exact test/patch boundaries remain JIT.
- Remaining blockers: none.

Planning audit verdict: GREEN.

## 14. Workflow references

- Shared Research: `workflow/common/RESEARCH.md`
- ChatGPT-only Research: `workflow/chatgpt_only/RESEARCH.md`
- Codex-only Research: `workflow/codex_only/RESEARCH.md`
- Codex runtime boundary: `workflow/codex/CODEX_ORCHESTRATION.md`
- OpenSpec: `workflow/common/OPENSPEC.md`

The Master Plan is not the live task tracker. Mutable implementation state will belong to the selected workstream Task Board after Execution Prep.
