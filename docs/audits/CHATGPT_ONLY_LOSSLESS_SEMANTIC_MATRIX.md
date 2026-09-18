# Lossless Semantic Matrix — chatgpt_only Policy Split

Date: 2026-09-18  
Pre-split source checkpoint: `4476ed77b88adbed77702a193e447a0e520c5440`  
Audited branch: `fix/chatgpt-only-lossless-gaps@83b45383ee1fec479552b6dbb4982f5bb7e9a86e`

Verdict: **GREEN**

## Legend

- **PRESERVED** — same applicable semantics exist on the active `chatgpt_only` route.
- **MOVED TO COMMON** — same policy-neutral semantics now live once under `workflow/common/`.
- **POLICY-EXCLUDED** — semantics belong only to another execution policy/executor and are intentionally absent from `chatgpt_only`; legacy source remains untouched for not-yet-migrated policies.
- **SUPERSEDED** — an explicit later workflow/user decision intentionally replaced the older behavior.
- **LEGACY PRESERVED** — source remains byte-for-byte unchanged for routes not yet migrated.

No applicable ChatGPT-only semantic row is unowned.

## 1. Root bootstrap / routing

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| `CHATGPT.md / Durable authority` | workflow main authoritative; project repo durable truth; Task Board sole mutable implementation state; durable > stale chat | `common/AUTHORITY.md` + root `CHATGPT.md` | MOVED TO COMMON |
| `CHATGPT.md / Durable authority` | workflow roles are authority roles, not prescribed model/reasoning identities | `common/AUTHORITY.md#Role semantics` | MOVED TO COMMON |
| `CHATGPT.md / Durable authority` | execution policy never changes automatically | `CONTEXT_ROUTING.md#Policy invariants` | PRESERVED |
| `CHATGPT.md / Bootstrap` | read project PROJECT.md, route, Task Board when state exists, exact authority refs, persist changed durable truth | root `CHATGPT.md` + policy router + `chatgpt_only/ROUTER.md` | PRESERVED |
| `CHATGPT.md / Default non-loading` | load only required route/artifacts; avoid whole trees; fixed-policy no capability inventory | `common/AUTHORITY.md` + `chatgpt_only/ROUTER.md` + `EXECUTION.md` | PRESERVED |
| `CHATGPT.md / Default non-loading` | do not load Codex execution modules during ChatGPT-only work | physical namespace isolation in `chatgpt_only/ROUTER.md` | PRESERVED |
| `CHATGPT.md / Human control surface` | concise what happened / meaning / next action; hide telemetry by default | root `CHATGPT.md` | PRESERVED |
| `CHATGPT.md` | do not end turn merely to announce deterministic work | root `CHATGPT.md` + policy route modules | PRESERVED |
| `CHATGPT.md` | fresh-chat prompt provided immediately when required/recommended | root `CHATGPT.md` + `chatgpt_only/REVIEW.md` | PRESERVED |
| pre-split ChatGPT adapter | ChatGPT Work outside Project Workflow | root `CHATGPT.md` | PRESERVED |
| pre-split ChatGPT adapter | same chat may continue while useful; fresh chat can be context hygiene; no fixed token/milestone cadence; fresh chat recovers repo truth | root `CHATGPT.md#Normal ChatGPT scope and session continuity` | PRESERVED |
| `CONTEXT_ROUTING / Minimal authority precedence` | domain authority ordering | `common/AUTHORITY.md` | MOVED TO COMMON |
| `CONTEXT_ROUTING / Global priority` | pending/in-progress REQUIRED/RECOMMENDED review outranks later implementation | `chatgpt_only/ROUTER.md` + `RECOVERY.md` | PRESERVED |
| `CONTEXT_ROUTING / route dispatch` | phase-specific minimal read sets | `chatgpt_only/ROUTER.md` | PRESERVED |
| `CONTEXT_ROUTING / CODEX EXECUTION` | Codex execution route | legacy router / Codex files | POLICY-EXCLUDED |
| `CONTEXT_ROUTING` | mixed Capability Gate routing | legacy router | POLICY-EXCLUDED |
| `CONTEXT_ROUTING / Independent review` | exact subject, same authority slice, independent durable evidence, no implementing-chat narrative | `chatgpt_only/REVIEW.md` | PRESERVED |
| policy semantics | new project defaults to chatgpt_only unless user explicitly chooses another accepted policy | `CONTEXT_ROUTING.md#Policy invariants` | PRESERVED |

## 2. Common brainstorming / research

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| `BRAINSTORMING / Goal` | ideas are tentative, not decisions | `common/BRAINSTORMING.md` | MOVED TO COMMON |
| `BRAINSTORMING / Canonical location` | `brainstorming/`; optional brainstorming/open-question templates | `common/BRAINSTORMING.md` | MOVED TO COMMON |
| `BRAINSTORMING / Non-negotiable distinction` | explicit acceptance promotes to decisions/requirements/planning; do not rewrite history | `common/BRAINSTORMING.md` | MOVED TO COMMON |
| `BRAINSTORMING / Working method` | separate facts/decisions/assumptions/implementation choices; research unknowns; delay architecture freeze; persist tentative work | `common/BRAINSTORMING.md` | MOVED TO COMMON |
| `BRAINSTORMING / Exit` | research when verification needed; planning when enough accepted facts; no premature Cards/OpenSpec | `common/BRAINSTORMING.md` | MOVED TO COMMON |
| `RESEARCH / Goal` | source-grounded evidence, not decision | `common/RESEARCH.md` | MOVED TO COMMON |
| `RESEARCH / Canonical location` | `research/`; optional research template | `common/RESEARCH.md` | MOVED TO COMMON |
| `RESEARCH / Workflow` | discovery → verification → alternatives → authority decisions → requirements/planning | `common/RESEARCH.md` | MOVED TO COMMON |
| `RESEARCH / Required distinctions` | facts/sources, repo observations, assumptions, uncertainty, alternatives, requested recommendation, unresolved authority questions | `common/RESEARCH.md` | MOVED TO COMMON |
| `RESEARCH / Context discipline` | only research-relevant authority/source; no unrelated implementation history | `common/RESEARCH.md` | MOVED TO COMMON |
| `RESEARCH / Promoting findings` | promotion targets requirements/decisions/planning/Card/OpenSpec/evidence; preserve provenance | `common/RESEARCH.md` | MOVED TO COMMON |

## 3. Strategic planning

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| `PLANNING / Responsibility` | strategic planner owns problem, requirements, architecture, invariants, milestone outcomes, coverage; code-dependent detail waits for Refresh | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING / Inputs` | PROJECT, requirements, research, decisions, source baseline | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING / Master Plan` | goal/baseline/target/requirements/architecture/non-goals/invariants/seams/milestones/dependencies/gates/coverage/deployment/system verification/security/fresh-context/policy refs | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING` | Master Plan is not tracker; approved milestone subsection default contract; JIT extension only if materially useful | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING / Milestones` | stable integrated/testable checkpoint; preserve rationale; approved sequence authorizes scope but not explicit gates | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING` | automatic crossing of approved GREEN milestone boundary when no strategic/authorization gate | `PLANNING.md` + `CLOSE.md` | PRESERVED |
| `PLANNING / Deferred decomposition` | defer unknowable Cards; persist stable outcome/requirements/dependencies/invariants/acceptance/gates/JIT trigger | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING / L1/L2/L3` | delegated JIT authority without repeated strategic planner; L3 returns to authority | `chatgpt_only/PLANNING.md` + `EXECUTION_PREP.md` | PRESERVED |
| `PLANNING / Requirement coverage` | milestone owner + Card before execution + OpenSpec when required; JIT trigger may stand in for unknown Card IDs | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING / Pre-implementation audit` | independent plan review when practical; assumptions/P0/P1/dependencies/tests/coverage/security/migration/OpenSpec/overengineering | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING / Competing paths` | optional Path A/Path B evidence then accepted A/B/Hybrid; no automatic merge | `chatgpt_only/PLANNING.md` | PRESERVED |
| `PLANNING / Distant work` | near-term detail, distant functional precision, Refresh Gate for driftable detail | `PLANNING.md` + `TASK_CARDS.md` | PRESERVED |
| `PLANNING` codex-only execution note | Codex cannot invent strategic authority | legacy/Codex route | POLICY-EXCLUDED |

## 4. Execution preparation / Task Card authoring

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| `EXECUTION_PREP / Preconditions` | identifiable requirements/decisions/approved milestone/no hidden strategic blocker | `chatgpt_only/EXECUTION_PREP.md` | PRESERVED |
| `EXECUTION_PREP / State ownership` | Cards/JIT milestone stable contracts; Task Board mutable state only | `EXECUTION_PREP.md` + `STATE.md` | PRESERVED |
| `EXECUTION_PREP / Steps` | inspect current state; exact authority slice; acceptance/tests; external writes; review class; selective OpenSpec; coverage; blockers | `chatgpt_only/EXECUTION_PREP.md` | PRESERVED |
| `EXECUTION_PREP / Incremental` | JIT create/revise only not-yet-started work from predecessor evidence; no strategic reinterpretation | `chatgpt_only/EXECUTION_PREP.md` | PRESERVED |
| `EXECUTION_PREP / Authority preservation` | exact refs; must-preserve constraints/rationale; summaries never override authority | `EXECUTION_PREP.md` + `TASK_CARDS.md` | PRESERVED |
| `EXECUTION_PREP / Evidence granularity` | simple Card may use tests_summary; standalone evidence for rich/high-risk proof | `chatgpt_only/EXECUTION_PREP.md` | PRESERVED |
| `EXECUTION_PREP / Card vs OpenSpec task` | global Card vs smaller OpenSpec checkbox | `common/OPENSPEC.md` | MOVED TO COMMON |
| `EXECUTION_PREP / chatgpt_only selection` | ChatGPT fixed executor; no Capability Gate/preflight; concrete runtime blocker only | namespace + `EXECUTION.md` | PRESERVED |
| `EXECUTION_PREP / codex_only` | Codex-specific prep | legacy route | POLICY-EXCLUDED |
| `EXECUTION_PREP / mixed` | Capability Gate assignment | legacy route | POLICY-EXCLUDED |
| `EXECUTION_PREP / Parallel preparation` | project-level bounded parallel Cards | legacy route | SUPERSEDED for chatgpt_only by explicit serial-only architecture |
| `EXECUTION_PREP / Git preparation` | branch/PR policy; no topology changes mid-milestone | `chatgpt_only/REPOSITORY.md` + `EXECUTION_PREP.md` | PRESERVED |
| `EXECUTION_PREP / Handoff input` | prior cumulative handoff only when materially useful | `EXECUTION_PREP.md` + `EXECUTION.md` | PRESERVED |
| `EXECUTION_PREP / Multi-milestone continuation` | continue approved next milestone when GREEN/reviews/gates allow | `CLOSE.md` | PRESERVED |
| old `EXECUTION PREP COMPLETE` status-only handoff | stop to report prep status before execution | active auto-transition in `EXECUTION_PREP.md` | SUPERSEDED by later explicit user decision: do not require “continue” |
| `TASK_CARDS / Meaning` | stable bounded work package, not live state | `chatgpt_only/TASK_CARDS.md` | PRESERVED |
| `TASK_CARDS / Required fields` | exact authority/outcome/scope/acceptance/tests/external/review | `TASK_CARDS.md` + new template | PRESERVED |
| `TASK_CARDS / Authority Preservation` | exact refs; carry implementation-shaping constraints/rationale | `TASK_CARDS.md` + template | PRESERVED |
| `TASK_CARDS / mixed required_capabilities` | task hints for mixed routing | legacy route | POLICY-EXCLUDED |
| `TASK_CARDS / Executor provenance/status` | mutable state in Task Board | `chatgpt_only/STATE.md` | PRESERVED |
| `TASK_CARDS / Deferred creation` | no placeholders; predecessor result binds new Card | `TASK_CARDS.md` + `EXECUTION_PREP.md` | PRESERVED |
| `TASK_CARDS / bounded-parallel metadata` | parallel_safe/write_scope/exclusive resources | legacy route | SUPERSEDED for chatgpt_only by serial-only architecture |
| `TASK_CARDS / Runtime contract` | runtime behavior belongs execution/state, not authoring | physical split into `EXECUTION.md` + `STATE.md` | PRESERVED |
| `TASK_CARDS / Near-term vs distant` | detailed near-term, functional distant, JIT trigger preferred | `chatgpt_only/TASK_CARDS.md` | PRESERVED |
| `TASK_CARDS / Scope discipline` | no hidden adjacent cleanup/architecture changes | `TASK_CARDS.md` + `EXECUTION.md` | PRESERVED |

## 5. Execution runtime / state

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| `EXECUTION / State authority` | Task Board sole mutable state; exact stable authority | `common/AUTHORITY.md` + `STATE.md` | PRESERVED |
| `EXECUTION / Core loop` | recover active obligation, review priority, current Card authority, Refresh, execute, verify, persist, continue | `chatgpt_only/EXECUTION.md` | PRESERVED |
| `EXECUTION / Executor selection chatgpt_only` | fixed ChatGPT; no gate | namespace itself | PRESERVED |
| `EXECUTION / codex_only,mixed` | alternate routing | legacy route | POLICY-EXCLUDED |
| `EXECUTION / Runtime operation` | no tool inventory; attempt concrete operation; exact blocker only | `chatgpt_only/EXECUTION.md` | PRESERVED |
| `EXECUTION / Authority preserving` | code/runtime cannot silently rewrite strategic authority | `common/AUTHORITY.md` + `EXECUTION.md` | PRESERVED |
| `EXECUTION / External writes` | WRITE → READBACK → VERIFY → EVIDENCE; auth gate | `chatgpt_only/EXECUTION.md` | PRESERVED |
| `EXECUTION / Bounded parallel` | concurrent project Cards/lane coordination | legacy route | SUPERSEDED for chatgpt_only by one-Card serial execution |
| `EXECUTION / JIT refinement` | predecessor evidence triggers L2 prep | `EXECUTION.md` + `EXECUTION_PREP.md` | PRESERVED |
| `EXECUTION / Review` | freeze subject/evidence, independent verdict | `EXECUTION.md` + `REVIEW.md` | PRESERVED |
| `EXECUTION / Close/publication` | conditional acceptance/close route | `CLOSE.md` | PRESERVED |
| `EXECUTION / Strategic blocker` | stop affected work, route to authority | `ROUTER.md` + `EXECUTION.md` | PRESERVED |
| `EXECUTION / Recovery` | reconstruct durable state and resume right obligation | `RECOVERY.md` | PRESERVED |
| `EXECUTION / Continuation` | routine GREEN not a user stop | `EXECUTION.md` + `CLOSE.md` | PRESERVED |
| `chatgpt/EXECUTION / Runtime` | actual normal ChatGPT runtime; local != production truth | `chatgpt_only/EXECUTION.md` | PRESERVED |
| `chatgpt/EXECUTION / Human output` | global concise control surface | root `CHATGPT.md` | PRESERVED |
| `chatgpt/EXECUTION / Review boundary` | fresh reviewer required; prompt immediately | `EXECUTION.md` + `REVIEW.md` | PRESERVED |
| `chatgpt/EXECUTION / Session continuity` | context-hygiene fresh chat optional; no fixed cadence; repo recovery | root `CHATGPT.md` | PRESERVED |
| `chatgpt/EXECUTION / Continuation` | deterministic continuation until real stop | `EXECUTION.md` + root | PRESERVED |
| old ChatGPT bounded-parallel adapter behavior | may handle subset/one Card without manufacturing concurrency | serial-only state + legacy migration reconciliation | SUPERSEDED by explicit serial-only architecture |

## 6. Task Execution contract

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| Authority/scope | bounded Card + exact authority/dependencies | `EXECUTION.md` + `TASK_CARDS.md` | PRESERVED |
| Readiness/start | ready, deps done, no blocker/review gate, persist in_progress/executor/branch | `TASK_CARDS.md` + `STATE.md` | PRESERVED |
| Refresh Gate | exact runtime/authority/deps/tests/evidence/review/OpenSpec; handoff conditional; L3 blocker | `EXECUTION.md` | PRESERVED |
| Runtime-operation rule | no capability inventory; concrete blocker only | `EXECUTION.md` | PRESERVED |
| Execute/verify | bounded scope, tests/OpenSpec/readback, no silent drift | `EXECUTION.md` | PRESERVED |
| Blocked state | persist blocker, stop dependent work, smallest user action | `STATE.md` + `EXECUTION.md` | PRESERVED |
| Definition of Done | scope/acceptance/tests/OpenSpec/review/durable result/readback/state | `EXECUTION.md` + `STATE.md` | PRESERVED |
| Review boundary | freeze exact subject/evidence; pending; no self-verdict | `EXECUTION.md` + `REVIEW.md` | PRESERVED |
| After Card | reconcile state, JIT/next Card/close automatically | `EXECUTION.md` + `CLOSE.md` | PRESERVED |

## 7. Durable state

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| `GITHUB_STATE / Single live-state authority` | Task Board sole mutable state | `chatgpt_only/STATE.md` | PRESERVED |
| Card states | planned/ready/in_progress/blocked/done/superseded | `STATE.md` | PRESERVED |
| Milestone lifecycle | planned→ready→in_progress→done; GREEN cannot stay active | `STATE.md` | PRESERVED |
| Task Board minimum state | project/plan, milestone, Card/deps/executor/results/tests/evidence/OpenSpec/branch/review/blocker | `STATE.md` | PRESERVED |
| Review fields | state/subject/evidence; immutable subject per attempt | `STATE.md` | PRESERVED |
| Executor assignment | ChatGPT fixed | namespace + `STATE.md` | PRESERVED |
| Incremental Card-set | no speculative future Cards; JIT trigger makes absence valid; active Card not silently redefined | `STATE.md#Incremental Card-set state` | PRESERVED |
| Starting serial Card | ready→in_progress; executor/branch; milestone starts | `STATE.md` | PRESERVED |
| Bounded-parallel start/coordinator/lane integration | concurrent lane machinery | legacy route | SUPERSEDED for chatgpt_only; safe legacy-state reconciliation retained |
| Independent-review lifecycle | pending→in_progress→green/red; changed subject new attempt | `STATE.md` + `REVIEW.md` | PRESERVED |
| Done result pointer contract | result commit/PR/evidence/tests provenance | `STATE.md` | PRESERVED |
| Runtime blocker/policy assignment | runtime blocker does not silently switch policy; explicit user policy decision only | `STATE.md` + root policy router | PRESERVED |
| Milestone GREEN | integrated acceptance + final pointers + all reviews green | `STATE.md` + `CLOSE.md` | PRESERVED |
| Automatic next milestone | approved next milestone continues after reviews/gates | `STATE.md` + `CLOSE.md` | PRESERVED |
| Corrective work | RED reopens bounded work; changed subject re-reviewed; reviewer auto-remediates deterministic RED | `STATE.md` + `REVIEW.md` | PRESERVED |
| Handoff/recovery | durable handoff + exact state recovery; local current.md convenience only | `REPOSITORY.md` + `RECOVERY.md` | PRESERVED |
| Consistency invariants | missing result/review/dependency/durable truth/readback/policy/self-review invalid | `STATE.md` | PRESERVED |
| parallel-only consistency invariants | lane overlap/parallel_card_limit/etc. | legacy route | POLICY-EXCLUDED |

## 8. Independent review / close / publication

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| Card close | executor claim alone insufficient; apply DoD; durable evidence as needed | `EXECUTION.md` + `STATE.md` | PRESERVED |
| Milestone completion | all Cards done necessary, not sufficient; integrated acceptance | `CLOSE.md` | PRESERVED |
| Review requirement | pre-split required/recommended/optional tiering | `REVIEW.md` + `TASK_CARDS.md` now use `REQUIRED | RECOMMENDED | none` | SUPERSEDED by explicit user decision: OPTIONAL removed; `none` means no gate and a later explicit review request promotes it to RECOMMENDED |
| ChatGPT hard review handoff | freeze subject/evidence, pending, commit/push when possible, stop before verdict, user action + prompt | `EXECUTION.md` + `REVIEW.md` | PRESERVED |
| Fresh prompt | repo, exact branch, target, durable pointer; no telemetry duplication | `REVIEW.md` + unchanged `prompts/CHATGPT_FRESH_SESSION.md` | PRESERVED |
| RED auto-remediation | same reviewer chat immediately performs bounded deterministic fix, freezes new pending subject, then stops for fresh re-review | `REVIEW.md` | PRESERVED |
| Codex review continuity | Codex reviewer workers | legacy/Codex route | POLICY-EXCLUDED |
| High-risk external writes | independent review at last useful reversible checkpoint; write + readback after GREEN | `REVIEW.md` | PRESERVED |
| No permanent review role | do not review every trivial Card | `REVIEW.md` | PRESERVED |
| Milestone acceptance | substantive integrated gate | `CLOSE.md` | PRESERVED |
| Publication verification | exact branch/head, accepted diff/handoff, only authorized post-review closure commits, status checks, no unauthorized deployment | `CLOSE.md` | PRESERVED |
| Cumulative handoff | compact completed truth + authority/evidence + next start; not live tracker | `CLOSE.md` | PRESERVED |
| Finalization/checkpoint | acceptance→PR verify→merge→reconcile→handoff/checkpoint | `CLOSE.md` | PRESERVED |
| Next milestone chatgpt_only | auto prep/Refresh/execute when approved/reviews green/no gate | `CLOSE.md` | PRESERVED |
| Next milestone codex/mixed | other policy continuation | legacy route | POLICY-EXCLUDED |
| System verification/cutover | independent system gate when required; runbook/Card-driven; OpenSpec only for behavior change; explicit live-write auth stop | `CLOSE.md` | PRESERVED |

## 9. OpenSpec

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| Role | behavior/technical contract; does not replace core authority; Card vs OpenSpec task distinction | `common/OPENSPEC.md` | MOVED TO COMMON |
| Selective policy | required/justified by contract risk; skip simple mechanical/docs/research cases | `common/OPENSPEC.md` | MOVED TO COMMON |
| Candidate vs actual | planning candidate only; JIT actual change | `common/OPENSPEC.md` | MOVED TO COMMON |
| JIT inputs | HEAD/source/runtime/handoff/milestone/Card/authority/requirements/decisions/plan/deps | `common/OPENSPEC.md` | MOVED TO COMMON |
| Standard flow | proposal/specs/design/tasks/apply/verify/archive | `common/OPENSPEC.md` | MOVED TO COMMON |
| Gate before coding | coherent, non-stale spec; local drift okay; strategic drift blocks | `common/OPENSPEC.md` | MOVED TO COMMON |
| Verification | implementation consistent with OpenSpec and archival policy | `common/OPENSPEC.md` | MOVED TO COMMON |
| Multi-card | one OpenSpec may span several Cards; do not create oversized Card | `common/OPENSPEC.md` | MOVED TO COMMON |

## 10. Repository contract / recovery

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| One project = one repo | no second project-state repo without technical justification + explicit user decision | `chatgpt_only/REPOSITORY.md` | PRESERVED |
| Workflow repo vs project repo | workflow repo stores workflow only; project repo stores project truth/code/state | `common/AUTHORITY.md` + `REPOSITORY.md` | MOVED TO COMMON / PRESERVED |
| Canonical project layout | knowledge/implementation/handoff/OpenSpec/source separation | `REPOSITORY.md` | PRESERVED |
| Knowledge/state ownership | Task Board only live mutable state; stable contracts/handoffs/evidence roles | `REPOSITORY.md` | PRESERVED |
| PROJECT.md | small router/index with chatgpt_only policy and pointers; not tracker | `REPOSITORY.md` | PRESERVED |
| Execution policy | default new project chatgpt_only; accepted policy changes explicit user decision only | root policy router | PRESERVED |
| Authority/conflicts | domain authority order; code/runtime cannot silently rewrite accepted intent | `common/AUTHORITY.md` | MOVED TO COMMON |
| Durable vs local convenience | current.md optional/non-authoritative; recovery without prior chat | `REPOSITORY.md` + `RECOVERY.md` | PRESERVED |
| Git/branch policy | coherent Card commits, PR for substantial work, acceptance on final branch, no force-push main | `REPOSITORY.md` | PRESERVED |
| Competing prototype branches | optional A/B prototype paths | `chatgpt_only/PLANNING.md` | PRESERVED |
| In-flight state | repo canonical on implementation branch/external runtime; exact branch/evidence pointers | `REPOSITORY.md` + `STATE.md` | PRESERVED |
| External write state | persisted readback where meaningful | `REPOSITORY.md` + `EXECUTION.md` | PRESERVED |
| Legacy state migration | no history churn; old status duplicates non-authoritative; existing milestones/evidence/handoffs remain; contract pointer JIT; topology migration only GREEN | `REPOSITORY.md` | PRESERVED |
| New project initialization | phase-appropriate artifacts, decisions/requirements/planning when meaningful, JIT Task Board/Cards/OpenSpec/evidence, no placeholders | `REPOSITORY.md` + root policy router | PRESERVED |

## 11. Prompts / templates

| Pre-split source | Semantic | New owner | Status |
|---|---|---|---|
| `CHATGPT_START` detailed policy instructions | bootstrap reads workflow main/project state and routes by policy | simplified `prompts/CHATGPT_START.md` → live router | SUPERSEDED intentionally by repository-owned live policy routing |
| `CHATGPT_START` human status style | concise control surface | root `CHATGPT.md` | PRESERVED |
| `CHATGPT_START` new project | initialize repository/policy then phase-appropriate artifacts | start prompt + policy router + `REPOSITORY.md` | PRESERVED |
| `CHATGPT_PROJECT_INSTRUCTIONS` duplicated policy detail | live workflow main is authority; small bootstrap only | simplified Project Instructions template + live router | SUPERSEDED intentionally to avoid stale duplicated policy semantics |
| `CHATGPT_FRESH_SESSION` | branch-aware thin durable-recovery prompt | file is unchanged from pre-split source | LEGACY PRESERVED / ACTIVE |
| old `templates/TASK_CARD.md` authority/scope/tests/external/review | ChatGPT-only Card template | `chatgpt_only/TASK_CARD_TEMPLATE.md` | PRESERVED |
| old template required_capabilities | mixed routing hint | legacy template | POLICY-EXCLUDED |
| old template parallel fields | bounded-parallel ownership metadata | legacy template | SUPERSEDED for chatgpt_only |
| old template JIT predecessor/authority rule | exact accepted predecessor result travels | `chatgpt_only/TASK_CARD_TEMPLATE.md` | PRESERVED |
| old template optional phase/code hints | optional execution hints | `chatgpt_only/TASK_CARD_TEMPLATE.md` | PRESERVED |
| old template review semantics | independent reviewer sees same authority; fresh ChatGPT for chatgpt_only | `TASK_CARD_TEMPLATE.md` + `REVIEW.md` | PRESERVED |
| old template inherited runtime contracts | standard runtime rules not copied into each Card | `chatgpt_only/EXECUTION.md` + `STATE.md` | PRESERVED |

## 12. Explicit intentional architecture changes

These are not semantic-loss defects:

1. **ChatGPT-only project execution is serial.** Old bounded-parallel Card/lane semantics are not imported. Legacy active concurrency metadata is recovered safely and serialized before new work.
2. **No alternate-executor/capability routing exists inside chatgpt_only.** Those semantics stay in legacy paths until their own policy migrations.
3. **Execution preparation does not stop merely to emit a status package.** Later explicit user direction requires deterministic preparation to continue directly into execution.
4. **Project Instructions/start prompts no longer duplicate policy behavior.** They are thin routers into current workflow `main`.

## 13. Common directory status

The single common directory is:

```text
workflow/common/
├── AUTHORITY.md
├── BRAINSTORMING.md
├── RESEARCH.md
├── OPENSPEC.md
└── USER_STOP.md
```

These files contain policy-neutral semantics only.

At this staged migration point:
- `chatgpt_only` actively uses them;
- `mixed` and `codex_only` still use the preserved legacy route and therefore are **not yet wired to common/**;
- their future migrations should reference these same common files rather than create copies, unless later audit proves a supposedly-common rule is actually policy-specific.

## 14. Static validation

PASS:
- all previously identified semantic gaps now have explicit owners;
- no active ChatGPT-only module contains mixed/Codex execution semantics;
- no active ChatGPT-only module reintroduces project-level concurrent Card execution;
- the only historical lane reference is inside safe migration/recovery guidance;
- legacy router/shared execution/contracts/Codex modules remain unchanged;
- `prompts/CHATGPT_FRESH_SESSION.md` remains unchanged;
- no legacy deletion occurred.

## 15. Context footprint

Pre-split always-read normal ChatGPT execution workflow core: approximately **3350 words**.

Current active ChatGPT-only execution core after restoring lossless semantics:
- root `CHATGPT.md`: 356
- policy dispatcher: 243
- common authority: 324
- ChatGPT-only router: 466
- execution: 668
- state: 886

Total: approximately **2943 words** before project artifacts.

This remains about **12% smaller** than the pre-split already-optimized core while providing stronger physical policy isolation.

## 16. Later role-transition and review-requirement refinement

A later explicit user decision refined the active ChatGPT-only state machine without reopening the lossless migration itself:

- `OPTIONAL` independent review was removed from ChatGPT-only and replaced by `REQUIRED | RECOMMENDED | none`;
- both REQUIRED and RECOMMENDED are real independent-review gates once contracted;
- `none` creates no review state; a later explicit review request first promotes the requirement to RECOMMENDED;
- completion of REVIEW, EXECUTION_PREP, EXECUTION, CLOSE or RECOVERY returns the same chat to the policy router before any next role is loaded;
- role completion is not a user stop;
- all normal-ChatGPT real-stop responses use `workflow/common/USER_STOP.md`.

## Later Project Definition / Planning refinement

A later explicit user decision intentionally superseded the earlier combined strategic-planner ownership model.

The active lifecycle is now:

```text
BRAINSTORMING ↔ RESEARCH
        ↓
PROJECT DEFINITION
        ↓
PLANNING
        ↓
EXECUTION PREP
        ↓
EXECUTION
```

This refinement changes ownership without dropping the underlying pre-split semantics:

- brainstorming remains tentative;
- research remains evidence;
- accepted product/system requirements and strategic/high-level decisions are now promoted through `workflow/common/DEFINITION.md`;
- Planning no longer invents or owns product/system intent;
- Planning owns Master Plan execution organization: milestones, dependencies, planned work packages, outcome-level acceptance, verification/migration strategy and JIT triggers;
- exact Task Cards remain Execution Prep responsibility;
- strategic escalation is split: Definition change when accepted target authority changes, Planning replan when Definition remains valid but milestone/strategy changes.

Historical matrix rows that say the strategic planner directly owns requirements/architecture or that Brainstorming/Research promote directly into Planning should be read as **SUPERSEDED BY EXPLICIT USER DECISION**, with their authority-preservation intent retained through the new Definition boundary.

The single common directory now also contains:

```text
workflow/common/DEFINITION.md
```

## Final verdict

**GREEN — lossless for applicable ChatGPT-only semantics, with explicit documented supersessions and policy exclusions.**

No remaining applicable pre-split ChatGPT-only rule is unowned in this matrix.

## 12. 2026-09-18 additive delegated-worker semantics

These rows are additive post-split semantics rather than migrated legacy behavior.

| New semantic | Owner | Status |
|---|---|---|
| ChatGPT remains fixed Task Card executor when a Card delegates bounded work | `chatgpt_only/DELEGATED_WORKERS.md` + `EXECUTION.md` + `STATE.md` | ADDED |
| Delegation is opt-in in stable Card authority; existing no-delegation Cards are unchanged | `DELEGATED_WORKERS.md` + `TASK_CARDS.md` + template | ADDED |
| Worker invocation is awaited; normal busy-loop completion polling is forbidden | `DELEGATED_WORKERS.md#Execution semantics` | ADDED |
| Raw worker event/transcript output stays outside normal parent context; bounded normalized result returns | `DELEGATED_WORKERS.md#Execution semantics` + `#State and evidence` | ADDED |
| Delegated tester receives contract + resulting state rather than executor transcript by default | `DELEGATED_WORKERS.md#Executor--tester separation` | ADDED |
| Delegated tester is not REQUIRED/RECOMMENDED workflow Independent Review | `DELEGATED_WORKERS.md#Independent Review remains separate` + `TASK_CARDS.md` + `STATE.md` | ADDED |
| Delegated workers are leaf workers by default; no backend-native nested fan-out | `DELEGATED_WORKERS.md#Leaf-worker invariant` | ADDED |
| Task Board remains sole mutable execution-state authority; no worker state ledger is introduced | `DELEGATED_WORKERS.md#State and evidence` + `STATE.md` | ADDED |
| Runtime worker availability is discovered at concrete invocation, not capability preflight | `EXECUTION.md#Runtime-operation rule` + `DELEGATED_WORKERS.md` | ADDED |
