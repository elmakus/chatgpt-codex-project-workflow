# V1 -> V2 Coverage Matrix

Date: 2026-09-22
Scope: Project Workflow V2 pre-Definition salvage audit
Status: complete — all identified V1 surfaces classified
V1 authority inspected: `elmakus/chatgpt-codex-project-workflow@main`
V2 target repo: `elmakus/project_workflow_v2` (verified empty)

## Legend

- **KEEP CORE** — preserve semantics in canonical V2 `workflow/`.
- **GENERALIZE** — preserve useful semantics but remove V1 product/policy-specific shape.
- **TRIGGER-ONLY** — preserve as optional module loaded only on a concrete trigger.
- **MIGRATION-ONLY** — support only for bounded V1 -> V2 transition.
- **DROP** — intentionally do not carry into V2.
- **BOOTSTRAP** — preserve only as thin delivery/entry surface.
- **OPEN** — material decision not yet closed.

## Lifecycle / semantic modules

| V1 source/mechanism | V2 disposition | V2 target / rationale |
|---|---|---|
| `workflow/BRAINSTORMING.md` + fixed-policy Brainstorming copies | KEEP CORE | One common adaptive-grilling Brainstorming module. `#grill` removed; grilling is intrinsic. |
| `workflow/common/BRAINSTORMING.md` | KEEP CORE | Merge useful common authority boundaries into the single V2 Brainstorming module. |
| `workflow/chatgpt_only/INTAKE.md` + `codex_only/INTAKE.md` | GENERALIZE | One Intake. Preserve `#feature`, `#issue`, neutral managed change, branch-first identity/recovery. Remove runtime binding/policy split. |
| automatic V1 `#issue -> micro_fix` fast path | DROP | Replaced by diagnosis -> mandatory user-alignment Brainstorming -> only then authorized micro-fix. |
| V1 micro-fix contract | GENERALIZE | Keep proportional direct-fix route after user alignment; skip full Planning when justified, never skip durable scope/tests/review. |
| `workflow/RESEARCH.md` + `workflow/common/RESEARCH.md` + fixed-policy Research | KEEP CORE | One Research with mandatory-but-proportional prior-art check: official/upstream + project/runtime + issues/discussions + community practice. |
| `workflow/common/DEFINITION.md` + fixed-policy Definition | KEEP CORE | One accepted product/system authority stage. Explicit user promotion from Brainstorming remains. |
| `workflow/PLANNING.md` + fixed-policy Planning | KEEP CORE | One Strategic Planning stage with premium stop A before material planning. |
| fixed-policy `PLAN_REVIEW.md` | GENERALIZE | One exact-subject independent Plan Review. Always for new/materially revised Master Plan; fresh best-model context; premium stops B/C. |
| `workflow/EXECUTION_PREP.md` + fixed-policy prep | GENERALIZE | Preserve JIT decomposition, exact authority slices, READY rules; remove execution-policy routing and Project-Card parallel scheduling. |
| root/shared `workflow/EXECUTION.md` + fixed-policy Execution | GENERALIZE | One serial Project-Card execution lifecycle; delegated implementation where capability exists; runtime-internal concurrency remains outside PW. |
| fixed-policy `REVIEW.md` | GENERALIZE | One append-only exact-subject review-attempt model for implementation/final integration. |
| fixed-policy `CLOSE.md` | KEEP CORE | Preserve integration refresh, review coverage reuse, publication/readback, terminal durable package, cleanup safety. |
| fixed-policy `RECOVERY.md` | GENERALIZE | One runtime-neutral durable recovery model; no Context Health or orchestration binding. |
| fixed-policy `ROUTER.md` + root `CONTEXT_ROUTING.md` | GENERALIZE | One small V2 router/semantic index; no execution-policy selection. Progressive disclosure only. |
| `workflow/common/USER_STOP.md` | GENERALIZE | Preserve concise human stop formatting + locator-only fresh-context handoff; remove Context Health variant. |
| `workflow/common/AUTHORITY.md` | KEEP CORE | Preserve authority-by-domain, durable truth > chat recollection, YAGNI/proportional design. |

## Durable project/state model

| V1 source/mechanism | V2 disposition | V2 target / rationale |
|---|---|---|
| `workflow/contracts/PROJECT_REPOSITORY.md` / fixed-policy `REPOSITORY.md` | GENERALIZE | Retain one-project-one-repository, small `PROJECT.md`, knowledge/state separation, branch-first durability. Remove execution-policy fields. |
| one project = one repository | KEEP CORE | Explicitly accepted for V2. Split control/state repo remains exceptional and user-authorized. |
| branch-first manifest-bound workstreams | KEEP CORE | Explicitly accepted. Stable ID, exact branch, manifest, workstream-local Task Board/evidence/handoffs. |
| mutable repository-global workstream registry | DROP | Correctness must not depend on one. Optional navigation index may be non-authoritative. |
| stacked parent/child workstreams | KEEP CORE | Keep only for genuine unmerged parent-only dependency; preserve provenance and safe integration paths. |
| `WORKSTREAM.yaml` final-integration/cleanup ownership | GENERALIZE | Keep semantic ownership; exact V2 schema to Definition. |
| `TASK_BOARD.yaml` mutable state | KEEP CORE | Keep separation of mutable status/result/review/recovery from stable contracts. |
| stable Task Card vs mutable Task Board | KEEP CORE | Preserve. Card = scope/authority/acceptance/tests; board = status/results/review pointers. |
| root/default legacy Task Board as live destination | DROP | V2 starts clean with branch/workstream state. Legacy root state only migration input. |
| execution-policy field | DROP | No `chatgpt_only/codex_only/mixed` durable semantic router. |
| runtime/model/session/worker identity in canonical state | DROP | Runtime-owned, non-canonical. |
| durable orchestration binding | DROP | Runtime implementation detail, not PW project truth. |
| universal `active_execution` / `transfer_ready` | DROP | No remaining single-Card correctness need. |
| Project-Card parallel batch/lane scheduler | DROP | User explicitly removed parallel Cards. |
| runtime-internal parallel subagents | KEEP OUTSIDE PW | Allowed; runtime-owned and not canonical project state. |
| cumulative milestone handoff/checkpoint | KEEP CORE | Minimal durable checkpoint retained even when continuation is immediate. |
| terminal target-side workstream package | KEEP CORE | Needed for recovery after source branch auto-deletion. |
| branch cleanup `safe_to_delete` fallback | KEEP CORE | Triggered only when branch survives and safe exact deletion cannot happen immediately. |

## Task contracts / technical contracts

| V1 source/mechanism | V2 disposition | V2 target / rationale |
|---|---|---|
| `workflow/contracts/TASK_CARDS.md` + fixed-policy `TASK_CARDS.md` | GENERALIZE | One bounded Task Card contract with exact authority refs, acceptance, tests, external/readback/review obligations. |
| `workflow/contracts/TASK_EXECUTION.md` | GENERALIZE | Preserve Refresh Gate, readiness/start, DoD, blocker/review boundary; remove execution-policy and parallel-Card branches. |
| `workflow/contracts/GITHUB_STATE.md` | GENERALIZE / SHRINK | Salvage only durable Git/state/recovery semantics still needed after deleting parallel scheduler machinery. |
| `workflow/common/OPENSPEC.md` + `workflow/contracts/OPENSPEC.md` | TRIGGER-ONLY / GENERALIZE | Every change has a precise Task Card/fix contract. Separate technical-contract/OpenSpec artifact only when it adds material value beyond the Card; keep core semantics tool-neutral and JIT. |
| speculative distant OpenSpec | DROP | JIT only; do not freeze unknowable implementation detail. |
| OpenSpec as replacement for requirements/plan/Card | DROP | Never; technical contract only. |

## Reviews / human control

| V1 source/mechanism | V2 disposition | V2 target / rationale |
|---|---|---|
| REQUIRED / RECOMMENDED exact-subject implementation review | KEEP CORE | Once activated, both block completion until GREEN. |
| product-specific reviewer identities | DROP | Independence is semantic per exact subject, not named worker/product. |
| Stage-6 planner spawning internal reviewer | DROP | Deliberate exception: fresh independent best-model context. |
| Stage-9 internal independent reviewer when capability exists | KEEP CORE | Capability-first unless another explicit override is later accepted. |
| locator-only fresh ChatGPT handoff | KEEP CORE | Explicitly accepted. Ready-to-copy prompt with repo/branch/obligation/durable pointer only. |
| Context Health / FRESH lifecycle | DROP | Explicitly removed. Normal chat replacement uses durable recovery. |
| issue auto-implementation from initial `#issue` | DROP | Mandatory diagnosis + user alignment before mutation. |
| user stop at deployment/live-write merely because it is deployment/live-write | DROP | Stop only when accepted authority contains an explicit authorization gate. |

## Git / integration / external effects

| V1 source/mechanism | V2 disposition | V2 target / rationale |
|---|---|---|
| GitHub as durable commit/PR/evidence source | KEEP CORE | Retain. |
| coherent commits / branch-PR managed changes | KEEP CORE | Exact policy details can remain project-sensitive; branch-first managed change is retained. |
| never force-push main as normal remediation | KEEP CORE | Safety invariant. |
| integration refresh against current target | KEEP CORE | Target movement alone does not invalidate review; actual subject/acceptance change does. |
| textual merge cleanliness = semantic compatibility | DROP | Explicitly reject; affected semantic verification remains required. |
| external `ACTION/WRITE -> READBACK -> VERIFY -> EVIDENCE` | KEEP CORE | Retain. |
| uncertain interrupted external side effect -> blind retry | DROP | Readback first; fail closed if occurrence cannot be established. |
| GitHub auto-delete merged branch | KEEP CORE | Normal cleanup realization; closure must already survive source ref disappearance. |

## Optional / specialized policy

| V1 source/mechanism | V2 disposition | V2 target / rationale |
|---|---|---|
| `workflow/common/FORK_RELEASE_VERSIONING.md` | TRIGGER-ONLY | Explicitly accepted. Load only for durably-declared downstream fork release/version selection. |
| `vX.Y.Z-private.N` lineage rules | TRIGGER-ONLY | Preserve as specialized module, not ordinary router context. |
| competing research/prototype branches | TRIGGER-ONLY | Keep as optional technique when real A/B prototype evidence is needed; not lifecycle state. |
| `BLOCKER.md` durable blocker record/template | KEEP SUPPORT | Use only when a durable blocker record adds recovery value. |
| acceptance evidence template | KEEP SUPPORT | Optional structured evidence, not mandatory boilerplate. |

## Runtime/product adapters

| V1 source/mechanism | V2 disposition | V2 target / rationale |
|---|---|---|
| `workflow/chatgpt/CAPABILITY_GATE.md` | DROP as product gate | V2 realization is capability-first inside common semantics; no durable mixed policy. |
| `workflow/chatgpt/EXECUTION.md` | GENERALIZE/MINIMIZE | Keep only surface-specific UX/fresh-context behavior if needed; common execution owns semantics. |
| `workflow/codex/CODEX_ORCHESTRATION.md` | GENERALIZE/MINIMIZE | Preserve boundary: PW owns project semantics, runtime owns worker/session orchestration. Delete policy binding/parallel Card specifics. |
| `workflow/codex/EXECUTION.md` | GENERALIZE/MINIMIZE | Codex surface bootstrap/runtime realization only; no separate semantic execution route. |
| `workflow/codex/HANDOFF.md` | MOSTLY DROP | Cross-product task handoff no longer primary semantic model. Durable state + router replaces it; salvage locator-only/strategic evidence principles only if still needed. |
| named Codex Main/Executor/Tester/Investigator in canonical policy | DROP | Runtime may use any concrete roles/models. |

## Delivery / plugin / prompts

| V1 source/mechanism | V2 disposition | V2 target / rationale |
|---|---|---|
| `.codex-plugin/plugin.json` | BOOTSTRAP | Keep plugin packaging, version/name adjusted for V2. |
| marketplace metadata | BOOTSTRAP | Keep only packaging/distribution metadata. |
| `skills/project-workflow/SKILL.md` | BOOTSTRAP | Rename Skill to `project_workflow_v2`; tiny pointer only, no workflow policy copy. |
| `hooks/session-start.py` + `hooks.json` | BOOTSTRAP | Keep tiny local bundled-router pointer; fail closed if package router missing. |
| Codex fetching remote workflow repo in normal operation | DROP | Plugin bundle is Codex policy source. |
| `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md` | BOOTSTRAP | Keep a recommended minimal template; actual Project Instructions are user-owned. |
| `prompts/CHATGPT_START.md` | SHRINK / OPTIONAL | Mostly redundant when Project Instructions bootstrap is present; may remain convenience/manual recovery prompt. |
| `prompts/CHATGPT_FRESH_SESSION.md` | KEEP SUPPORT | Preserve locator-only pattern for actual fresh-context gates. |
| `prompts/CODEX_START.md` | DROP / DEBUG-ONLY | Normal Codex entry is plugin/session bootstrap + `$pw:project_workflow_v2`; no “use current main” semantic bootstrap. |
| duplicate semantic policy inside plugin Skill/hook | DROP | One product, one canonical `workflow/` tree. |
| project-local plugin/MCP/Skill provisioning | OUT OF SCOPE | Owned by user's `newproject-skill`. |

## Templates

| V1 template | V2 disposition | Notes |
|---|---|---|
| `templates/PROJECT.md` | GENERALIZE | Remove execution policy; add common V2 contract marker and navigation only. |
| `templates/BRAINSTORM.md` | KEEP SUPPORT | Adapt to adaptive grilling durable minimum, not transcript/tree dump. |
| `templates/OPEN_QUESTIONS.md` | KEEP SUPPORT | Optional unresolved material decisions/research needs. |
| `templates/RESEARCH.md` | KEEP SUPPORT | Add mandatory-but-proportional prior-art source classes/evidence weighting. |
| `templates/REQUIREMENTS.md` | KEEP SUPPORT | Definition authority. |
| `templates/DECISION.md` | KEEP SUPPORT | Accepted decision authority. |
| `templates/MASTER_PLAN.md` | KEEP SUPPORT | Strategic plan subject/revision. |
| `templates/MILESTONE.md` | KEEP SUPPORT / OPTIONAL | JIT extension only when it adds useful detail beyond Master Plan. |
| `templates/TASK_CARD.md` | KEEP SUPPORT | Stable bounded Card contract. |
| `templates/TASK_BOARD.yaml` | GENERALIZE | Workstream-local common mutable execution state. |
| `templates/ACCEPTANCE_EVIDENCE.md` | KEEP SUPPORT | Use proportionally. |
| `templates/BLOCKER.md` | KEEP SUPPORT | Use when durable blocker artifact is warranted. |
| `templates/HANDOFF.md` | GENERALIZE | Minimal cumulative recovery checkpoint; not chat narrative. |

## Explicit V1 drops checklist

The following are intentionally absent from V2, not forgotten:

- fixed `chatgpt_only` semantic tree;
- fixed `codex_only` semantic tree;
- legacy shared semantic route;
- `execution_policy`;
- mixed-policy Capability Gate;
- Context Health/FRESH project lifecycle;
- Project-Card parallel execution;
- batch/lane/frozen-member scheduler metadata;
- `parallel_safe`/scheduler-oriented write-scope fields as a concurrency contract;
- universal `active_execution`;
- `transfer_ready`;
- durable runtime/orchestration binding;
- canonical runtime/model/session/worker identity;
- named product-specific implementation/reviewer roles;
- automatic `#issue -> repair` continuation;
- planner-spawned Stage-6 independent review;
- unconditional deployment/live-write human stop;
- duplicate plugin semantic policy;
- Codex remote-repo workflow-policy fetch during ordinary operation;
- source-branch existence as a requirement for terminal recovery.

## GitHub Issue tracking addition

| V2 managed-change behavior | Disposition | Notes |
|---|---|---|
| Official GitHub Issue for `#issue` | KEEP SUPPORT / DEFAULT TRACKER | Create/recover after dedup check; never implies implementation authorization. |
| Official GitHub Issue for `#feature` | KEEP SUPPORT / DEFAULT TRACKER | Create/recover after dedup check; refine during discovery/Brainstorming. |
| Workstream -> GitHub Issue exact reference | KEEP CORE POINTER | Enables recovery/correlation without making Issue canonical authority. |
| Final PR closing keyword | KEEP SUPPORT | Use only on final scope-completing default-branch PR; intermediate PRs reference without closing. |
| Post-merge Issue readback | KEEP CORE CLOSE CHECK | Verify expected closed/open state; explicit close only after durable GREEN completion when needed. |

## Matrix conclusion

All currently identified V1 production surfaces and the newly accepted GitHub Issue tracking behavior have an explicit V2 disposition.

No unresolved V1-salvage decision remains. Selective separate OpenSpec/technical-contract creation is accepted to preserve rigor without duplicating simple Task Card contracts or wasting Codex context.
