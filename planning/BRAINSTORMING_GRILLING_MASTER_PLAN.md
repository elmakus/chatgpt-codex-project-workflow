# Master Plan — Brainstorming Grilling

Revision: `BGR-P3`
Status: `approved`
Updated: `2026-09-21`
Independent plan review: `RECOMMENDED`
Supersedes plan revision: `BGR-P2` — R2 Definition replaces conditional/manual grilling with adaptive default grilling.

> Planning organizes the approved `requirements/BRAINSTORMING_GRILLING.md` R2 Definition. ADR-BGR-002 is strategic authority and supersedes ADR-BGR-001. This plan does not redefine those choices.

## 1. Accepted target / canonical inputs

- Requirements: `requirements/BRAINSTORMING_GRILLING.md` — `R2`, approved.
- Accepted decision: `decisions/ADR_BRAINSTORMING_ADAPTIVE_GRILLING.md` — `ADR-BGR-002`.
- Exploratory provenance: `brainstorming/ADAPTIVE_BRAINSTORMING_GRILLING.md` — `adaptive-brainstorming-grilling@R1`, explicitly user-promoted.
- Workstream: `implementation/workstreams/change-adaptive-brainstorming-grilling/WORKSTREAM.yaml`.
- Historical baseline: BGR-P2 / integrated M01 established conditional grilling plus `#grill`; that behavior is now the migration baseline to replace.
- External inspiration remains Matt Pocock's public `grill-me` / `grilling` skills; there is no runtime dependency.

## 2. Execution baseline

- ChatGPT-only and Codex-only Brainstorming currently implement conditional grilling, whole-frontier rounds, recommendations, Research ownership, recovery state, user stop, and a manual `#grill` force control.
- Their routers and Intake contracts explicitly recognize `#grill` as a non-Intake Brainstorming directive.
- The active legacy/mixed route still dispatches Brainstorming through `workflow/BRAINSTORMING.md`, which lacks the newer dependency-aware grilling contract.
- Existing BGR tests primarily assert required text/contract presence. They protect routing semantics but do not strongly prevent a future “2–3 questions then declare done” interpretation.
- Existing Brainstorming → Project Definition promotion and Research-return lifecycles are already authoritative and must remain unchanged.

## 3. Inherited non-goals / invariants / constraints

- Adaptive grilling remains Brainstorming interaction behavior, never a new phase, Intake kind, workstream type, scheduler, questionnaire engine, or second authority layer.
- No fixed minimum/maximum question count or round count.
- Simple scopes may end quickly only after the required completion audit/final challenge finds no material remainder.
- Complex scopes may continue for many rounds when decision value remains.
- Agent-findable facts remain agent-owned and use normal Research routes.
- User stop ends new questions immediately but cannot hide material blockers or bypass Definition promotion.
- `#grill` must disappear from active supported surfaces; historical artifacts remain untouched unless they are current authority that must be revised.
- Policy-local lifecycle/recovery semantics remain isolated even where the interaction method is equivalent.
- `wait-what` remains out of scope.
- No new credentials, deployment, data migration, or live-system authorization gate.

## 4. Milestones

### M01 — Historical baseline: conditional dependency-aware grilling

- State: completed/integrated under BGR-P2.
- Purpose in P3: historical dependency only; do not reopen or rewrite its completed implementation evidence.
- Result inherited: conditional grilling exists in migrated fixed-policy namespaces and `#grill` exists as the manual force surface.

### M02 — Make adaptive grilling intrinsic to every Brainstorming route

- Outcome: every active Project Workflow Brainstorming route uses one adaptive dependency-aware discovery method; completion is resistant to shallow early exit; `#grill` is no longer a supported active operator surface.
- Dependencies: approved BGR R2 Definition + ADR-BGR-002; integrated M01 baseline.
- Checkpoint: current Brainstorming contracts, route surfaces, OpenSpec behavior, tests/scenario evidence, and user-facing docs agree on the R2 semantics with no active conditional/manual-grilling path left.
- Acceptance:
  - ChatGPT-only, Codex-only, and legacy/mixed Brainstorming all express the adaptive-default method;
  - no entry route controls whether grilling happens;
  - decision-tree/frontier recomputation, relevant internal decision lenses, thematic batching, numbered questions, and recommendation-per-material-question are explicit;
  - each material settled choice receives one bounded counterfactual challenge and is reopened only by materially new evidence/contradiction/context;
  - agent-findable facts use Research and return to the same exploratory subject;
  - normal completion requires relevant-surface completion audit plus one final challenge/discovery pass;
  - implementation readiness alone is explicitly insufficient to end Brainstorming;
  - no numeric depth quota exists;
  - a simple scenario can terminate after a short round only after completion audit;
  - a complex/dependency-rich scenario demonstrably requires successive rounds as new consequences/frontiers appear;
  - clear user stop halts questions immediately while unresolved material blockers keep the scope tentative;
  - active `#grill` support is absent from routers, Intake, Brainstorming contracts, current README/docs/examples, current OpenSpec, and current BGR tests;
  - explicit Brainstorming → Definition promotion remains unchanged;
  - regression verification covers all active route families and prevents reintroduction of conditional/manual semantics.
- Requirement coverage: BGR-REQ-001..018.
- Planned work packages:
  1. Create/reconcile one JIT OpenSpec change for BGR R2 adaptive-default behavior, explicitly superseding the prior conditional/manual behavior contract without rewriting historical evidence.
  2. Refactor ChatGPT-only and Codex-only Brainstorming interaction sections to adaptive-default semantics while preserving each namespace's own durable Research/Definition mechanics.
  3. Bring the active legacy/mixed `workflow/BRAINSTORMING.md` path to equivalent adaptive interaction semantics without importing migrated fixed-policy state mechanics.
  4. Remove supported `#grill` handling from active ChatGPT-only/Codex-only routers and Intake contracts and remove active documentation/spec/test references that advertise it.
  5. Strengthen BGR verification so it checks anti-shortcut completion semantics, cross-route parity, user-stop/blocker behavior, evidence-driven reopening, Research interleave, and absence of the manual trigger; add scenario-oriented evidence that distinguishes simple versus multi-round complex Brainstorming instead of only checking isolated phrases.
  6. Update README/current user-facing documentation/examples to describe adaptive Brainstorming as intrinsic behavior and explain that the user only needs natural-language stop/continuation.
  7. Run integrated verification across the exact affected route/doc/spec/test surfaces and existing repository regression suite.
- JIT decomposition trigger: Execution Prep may split contract/OpenSpec/tests/docs/removal work into bounded Cards based on actual current file layout and reviewability, but every BGR requirement must be assigned before its implementation starts.
- Planning re-evaluation trigger: implementation shows equivalent semantics cannot be delivered across active route families without materially changing routing topology or milestone strategy.
- Definition re-open trigger: implementation requires restoring a manual trigger, introducing numeric depth quotas, changing Definition promotion authority, adding a new lifecycle/state owner, or weakening any R2 requirement.
- Boundary/user authorization gate: none beyond normal independent review gates.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Planned work package / JIT path | OpenSpec |
|---|---|---|---|
| BGR-REQ-001 | M02 | Brainstorming interaction contracts / lifecycle boundary regression | yes |
| BGR-REQ-002 | M02 | All active Brainstorming route families + route tests | yes |
| BGR-REQ-003 | M02 | Completion/depth semantics + anti-quota tests | yes |
| BGR-REQ-004 | M02 | Simple-scope scenario + completion audit behavior | yes |
| BGR-REQ-005 | M02 | Decision-tree/frontier contract + dependency scenarios | yes |
| BGR-REQ-006 | M02 | Internal decision-lens coverage contract + scenario evidence | yes |
| BGR-REQ-007 | M02 | Thematic batching/numbering/recommendations contract | yes |
| BGR-REQ-008 | M02 | Frontier recomputation + multi-round scenario | yes |
| BGR-REQ-009 | M02 | Research interleave/return-to-same-subject behavior | yes |
| BGR-REQ-010 | M02 | Bounded counterfactual challenge behavior | yes |
| BGR-REQ-011 | M02 | Evidence-driven reopening behavior | yes |
| BGR-REQ-012 | M02 | Completion audit + final discovery pass + anti-shortcut tests | yes |
| BGR-REQ-013 | M02 | User-stop and blocker-preservation behavior | yes |
| BGR-REQ-014 | M02 | Recovery-state minimality / no transcript-tree authority | yes |
| BGR-REQ-015 | M02 | Existing Definition-promotion regression coverage | yes |
| BGR-REQ-016 | M02 | Remove active `#grill` route/docs/spec/test surfaces | yes |
| BGR-REQ-017 | M02 | ChatGPT-only/Codex-only/legacy-mixed parity verification | yes |
| BGR-REQ-018 | M02 | Scope-boundary documentation/regression | no — scope boundary |

## 6. Dependency / execution order

Within M02 preserve this logical dependency order:

1. JIT OpenSpec reconciliation against BGR R2 + ADR-BGR-002 and current HEAD.
2. Core adaptive interaction contract for the three active Brainstorming route families.
3. Removal/reconciliation of active `#grill` router/Intake/operator surfaces.
4. Verification strengthening and scenario-oriented behavior evidence against the resulting exact contract.
5. README/current docs/examples alignment.
6. Integrated regression and cross-route consistency verification.

Execution Prep may combine adjacent items in one bounded Card when write scope and independent review remain clear. It must not separate tests/docs so far from the changed contract that the exact behavior subject becomes ambiguous.

## 7. OpenSpec / behavior-contract strategy

M02 changes a workflow behavior contract and therefore requires one JIT OpenSpec change.

Preferred new change identity: `adaptive-brainstorming-grilling` rather than mutating the already-integrated historical `brainstorming-grilling` change package. The new OpenSpec should:
- reference BGR R2 and ADR-BGR-002;
- state adaptive-default semantics and completion invariants;
- state complete removal of active `#grill` support;
- cover all active Brainstorming route families;
- preserve Research return and Definition promotion boundaries;
- avoid encoding implementation-file details beyond what current execution needs.

Execution Prep confirms exact archival/current OpenSpec layout before authoring it.

## 8. Migration / rollback strategy

- Workflow-contract/documentation/test change only; no persistent project data migration is required.
- Historical Brainstorming records and historical BGR M01/OpenSpec/evidence remain valid provenance and need no rewrite.
- Existing active Brainstorming scopes recover under current durable state; the changed interaction method applies when they next enter/resume Brainstorming.
- Removing `#grill` is an intentional operator-surface breaking change; no compatibility alias is retained.
- Rollback is an ordinary Git revert of M02 if integrated verification fails; do not rewrite historical M01 evidence.

## 9. System verification strategy

Verification must combine deterministic repository checks with behavior-oriented scenario evidence:

- repository regression suite;
- contract parity checks across ChatGPT-only, Codex-only, and legacy/mixed Brainstorming;
- negative scans/assertions proving active `#grill` support is removed from current route/Intake/Brainstorming/docs/spec/test surfaces while allowing historical provenance;
- focused checks for every R2 completion invariant: expected-decision-value continuation, completion audit, final challenge pass, implementation-readiness insufficiency, no numeric quota, counterfactual challenge, evidence-driven reopening, Research interleave, user-stop blocker preservation;
- a **simple-scope scenario** demonstrating that adaptive grilling can terminate quickly only after audit;
- a **complex/dependency-rich scenario** demonstrating multiple successive rounds/frontier recomputation rather than a single shallow 2–3-question pass;
- a **Research-interleave scenario** demonstrating fact ownership and return to the same exploratory subject;
- Definition-promotion regression proving adaptive grilling does not bypass explicit promotion.

Because the workflow behavior is instruction-driven rather than an executable questionnaire engine, scenario evidence may be maintained as bounded contract fixtures/audit cases rather than inventing a new runtime solely for tests. Execution Prep chooses the smallest deterministic representation that materially catches regressions.

## 10. Data integrity / idempotency / security

- No second mutable decision-tree authority is introduced.
- Durable state remains recovery-relevant exploratory outcomes/dependencies, not full transcript telemetry.
- Research return remains exactly-once under existing Research contracts.
- Re-entry/recovery of the same exploratory scope must not duplicate workstream or Definition authority.
- No credentials, external writes, privileged infrastructure, or security-sensitive runtime behavior are introduced.

## 11. Explicit authorization boundaries

- No deployment/live-write authorization gate.
- Existing user-owned Brainstorming → Project Definition promotion remains unchanged.
- Independent plan review is RECOMMENDED and forms the next fresh-chat boundary.
- Card/final-integration independent review follows normal ChatGPT-only rules after Execution Prep.

## 12. JIT / deferred decomposition map

Execution Prep owns exact Card boundaries and may split M02 into contract/OpenSpec, verification, and docs/removal Cards when current source layout makes that safer.

It must preserve:
- one exact R2 authority slice for all Cards;
- requirement coverage before implementation of each requirement;
- current OpenSpec coherence before behavior implementation;
- cross-route parity verification before milestone close.

Do not create speculative future Cards whose scope depends on actual changed-file/test structure.

## 13. Fresh-context boundaries

- Independent plan review is the immediate fresh-context boundary after this draft is frozen.
- Later REQUIRED/RECOMMENDED Card/final-integration reviews use normal fresh-review boundaries.
- No extra context-hygiene stop is planned merely because M02 touches three routing families.

## 14. Pre-implementation planning audit

- Definition Complete: GREEN — BGR R2 approved, ADR-BGR-002 accepted, no unresolved product choice.
- False assumptions / P0-P1 risks:
  - **P0:** accidentally leaving an active `#grill` path creates two behavior modes → explicitly covered by removal and negative verification.
  - **P0:** updating only migrated fixed-policy Brainstorming leaves legacy/mixed behavior divergent → M02 explicitly owns all active route families.
  - **P1:** another phrase-only test suite still permits shallow runtime interpretation → completion invariants and scenario-oriented evidence are explicit acceptance.
  - **P1:** overcorrecting into a fixed exhaustive questionnaire → numeric quotas and rigid user-facing lens checklist are forbidden.
- Milestone structure/order: one new integrated M02 is sufficient; M01 remains completed historical baseline.
- Dependency completeness: OpenSpec/current contract before implementation; interaction contract before removal/tests/docs finalization.
- Outcome-level acceptance: covers route parity, depth/completion, user stop, Research, trigger removal, promotion preservation.
- Requirement coverage: BGR-REQ-001..018 all map to M02 and a concrete planned package.
- Migration/rollback: no durable data migration; intentional operator-surface removal; ordinary revert available.
- System verification: deterministic regressions + simple/complex/Research scenario evidence.
- Data integrity/security: no new state authority or sensitive runtime surface.
- Authorization gates: none new; promotion/review gates preserved.
- OpenSpec boundary: one new JIT change justified by changed workflow behavior.
- Overengineering check: no new questionnaire runtime, scheduler, generic scoring system, persisted full tree, or numeric depth engine; scenario representation deferred to the smallest useful execution-time mechanism.
- Remaining blockers: none.

Planning audit verdict: GREEN.

## 15. Workflow references

- Policy router: `workflow/CONTEXT_ROUTING.md`
- ChatGPT-only Planning: `workflow/chatgpt_only/PLANNING.md`
- ChatGPT-only Brainstorming: `workflow/chatgpt_only/BRAINSTORMING.md`
- Codex-only Brainstorming: `workflow/codex_only/BRAINSTORMING.md`
- Legacy/mixed Brainstorming: `workflow/BRAINSTORMING.md`
- ChatGPT-only/Codex-only Intake and routers for active `#grill` removal
- OpenSpec: `workflow/common/OPENSPEC.md`
- Independent plan review: `workflow/chatgpt_only/PLAN_REVIEW.md`

The Master Plan is planning authority, not the live Task Board. Mutable implementation state will be created only after plan review/approval and Execution Prep.
