# ChatGPT-only Final Architecture / Coherence Audit

Date: 2026-09-18
Audit type: fresh independent top-to-bottom architecture/coherence audit
Final verdict: RED

## 1. Frozen subject

The exact semantic subject audited is:

- repository: elmakus/chatgpt-codex-project-workflow
- branch at freeze time: main
- frozen main HEAD: cec0b384af2436890c2ee7a6f395a1131ddae1c8
- commit message: Merge pull request #25 from elmakus/fix/chatgpt-only-brainstorm-promotion-gate
- main was re-read near the end of the audit and still pointed to the same SHA.

This audit does not treat this audit branch/commit as part of the semantic subject. The audit package is evidence-only and is based on the frozen SHA above.

Prior audit reports, PR bodies, previous GREEN verdicts and chat transcripts were not used as authority. README.md was treated only as supporting documentation. Historical/shared/legacy material was read only to test policy isolation and historical semantic preservation.

## 2. Reconstructed authority set

Normative bootstrap and route:

1. CHATGPT.md
2. workflow/CONTEXT_ROUTING.md
3. workflow/chatgpt_only/ROUTER.md

Active policy-neutral common modules reachable from chatgpt_only:

- workflow/common/AUTHORITY.md
- workflow/common/BRAINSTORMING.md
- workflow/common/RESEARCH.md
- workflow/common/DEFINITION.md
- workflow/common/OPENSPEC.md
- workflow/common/USER_STOP.md

Active chatgpt_only modules:

- workflow/chatgpt_only/ROUTER.md
- workflow/chatgpt_only/REPOSITORY.md
- workflow/chatgpt_only/PLANNING.md
- workflow/chatgpt_only/PLAN_REVIEW.md
- workflow/chatgpt_only/EXECUTION_PREP.md
- workflow/chatgpt_only/TASK_CARDS.md
- workflow/chatgpt_only/TASK_CARD_TEMPLATE.md
- workflow/chatgpt_only/EXECUTION.md
- workflow/chatgpt_only/STATE.md
- workflow/chatgpt_only/REVIEW.md
- workflow/chatgpt_only/CLOSE.md
- workflow/chatgpt_only/RECOVERY.md
- workflow/chatgpt_only/CONTEXT_HEALTH.md

Templates/prompts inspected:

- templates/PROJECT.md
- templates/BRAINSTORM.md
- templates/OPEN_QUESTIONS.md
- templates/RESEARCH.md
- templates/REQUIREMENTS.md
- templates/DECISION.md
- templates/MASTER_PLAN.md
- templates/TASK_BOARD.yaml
- templates/TASK_CARD.md
- templates/MILESTONE.md
- templates/HANDOFF.md
- templates/BLOCKER.md
- templates/ACCEPTANCE_EVIDENCE.md
- prompts/CHATGPT_START.md
- prompts/CHATGPT_FRESH_SESSION.md
- prompts/CHATGPT_PROJECT_INSTRUCTIONS.md

Legacy/shared/codex files were inspected only far enough to test reachability, conflicting semantics and losslessness, including workflow/EXECUTION.md, workflow/EXECUTION_PREP.md, workflow/PLANNING.md, workflow/REVIEW_AND_HANDOFF.md, workflow/contracts/TASK_EXECUTION.md, workflow/contracts/GITHUB_STATE.md, workflow/contracts/TASK_CARDS.md, workflow/contracts/PROJECT_REPOSITORY.md, workflow/legacy/CONTEXT_ROUTING.md, workflow/chatgpt/CAPABILITY_GATE.md and workflow/codex/CODEX_ORCHESTRATION.md.

## 3. Reconstructed lifecycle graph

The lifecycle below is reconstructed from normative files, not copied from README.

| From | Owning module | Preconditions / durable source | Automatic? | Real user stop? | Fresh independent chat? | Legal next role |
|---|---|---|---|---|---|---|
| project initialization | chatgpt_only/REPOSITORY | repository + PROJECT policy/index | yes after requested initialization | only if policy/topology requires user choice | no | Brainstorming |
| Brainstorming | common/BRAINSTORMING | PROJECT Active exploratory scope pointer + brainstorming record | yes while exploring | no unless user decision is required | no | Brainstorming or Research |
| Brainstorming -> Research | common/BRAINSTORMING + RESEARCH | explicit evidence gap/question | yes | no | no | Research |
| Research -> Brainstorming | common/RESEARCH + router | evidence returns to exploratory scope | yes | no | no | Brainstorming |
| ready_for_definition | chatgpt_only/ROUTER | pointed brainstorming record status ready_for_definition | no promotion without user authority | yes | no | wait for user promotion or continue exploration |
| user promotion -> Definition | chatgpt_only/ROUTER + common/DEFINITION | user_authorized + exact scope-id@revision | yes after explicit user authorization is persisted | promotion itself is the stop before authorization | no | Project Definition |
| Definition -> Research | common/DEFINITION | exact evidence need/open question | yes | no unless evidence cannot be obtained without user input | no | Research |
| Research -> Definition | common/RESEARCH + router | same promoted definition scope still valid | intended yes | no | no | Project Definition |
| Definition -> open-ended Brainstorming | common/DEFINITION + chatgpt_only/ROUTER | problem space materially reopened | yes to Brainstorming; future promotion resets | future promotion is a new user stop | no | Brainstorming |
| Definition Complete -> Planning | common/DEFINITION + router | requirements approved, strategic decisions accepted, no material unresolved definition choice | yes | no | no | Strategic Planning |
| Planning -> PLAN_REVIEW | chatgpt_only/PLANNING + PLAN_REVIEW | exact frozen draft + revision-specific planning/reviews record pending | no in authoring chat | yes | yes | fresh independent plan reviewer |
| PLAN_REVIEW GREEN -> Planning approval | PLAN_REVIEW + PLANNING | same exact subject GREEN and unchanged except lifecycle metadata | yes | no | no additional fresh chat | Planning |
| PLAN_REVIEW RED -> remediation | PLAN_REVIEW + router | RED evidence classified | yes when bounded/deterministic | only if user/product/authorization/runtime blocker | corrected subject needs a later fresh review | Planning, Definition or Research |
| approved plan -> Execution Prep | PLANNING + router | implementation already within approved user/project scope | yes | no unless planning-only scope ended | no | Execution Prep |
| Execution Prep -> Execution | EXECUTION_PREP + router | one eligible ready Card, dependencies satisfied, no gate | yes | no | no | Execution |
| Execution -> implementation review | EXECUTION + STATE + REVIEW | implementation subject frozen, REQUIRED/RECOMMENDED review pending | no verdict in implementing chat | yes | yes | fresh independent reviewer |
| REVIEW GREEN -> continuation | REVIEW + router | exact review subject GREEN | yes | no | no additional fresh chat | expected state finalization / next execution / close |
| REVIEW RED -> remediation | REVIEW + router | bounded L1/L2 correction or classified higher-authority defect | yes if deterministic | only for actual strategic/user/auth/runtime stop | corrected reviewable subject later requires fresh re-review | Execution Prep, Execution, Planning, Definition or Research |
| Card/milestone blocker -> classification | STATE + ROUTER | durable blocker/evidence | yes if classifiable | only if smallest required resolution belongs to user/access/authorization | no unless a separate review/context boundary applies | same Card, Research, Planning or Definition |
| milestone ready for close | CLOSE | required Cards terminal, required reviews GREEN, intended final state exists | yes | no by itself | only if milestone acceptance review requires it | Close |
| milestone GREEN -> publication/finalization | CLOSE | accepted final subject + branch/publication checks | intended automatic inside already authorized scope | explicit publication/deployment/live-write/user gate still stops | no by itself | publication/finalization |
| milestone done -> next approved milestone | CLOSE + STATE + router | next milestone already approved, dependencies satisfied, no gates | yes | no | no unless Context Health or review boundary | Execution Prep |
| end of approved scope | root CHATGPT.md | no deterministic authorized next work | no | yes, informational completion stop | no | none |
| Context Health FRESH | CONTEXT_HEALTH + router | safe durable boundary, no stronger stop, concrete context risk | no next obligation in same chat | yes | fresh chat for hygiene | exact next durable obligation |
| interrupted execution recovery | RECOVERY | Task Board + Git/runtime/external state + exact contracts/evidence | yes when coherent | only if unresolved blocker remains | no by itself | recovered role |

This graph is coherent in most post-planning states, but three blocking defects described below prevent a GREEN architecture verdict.

## 4. Authority / state ownership matrix

| Concept | Canonical owner | Audit result |
|---|---|---|
| exploratory scope and promotion authorization | PROJECT Active exploratory scope pointer -> exact brainstorming record | coherent |
| accepted requirements | requirements/ canonical artifact produced by Definition | coherent |
| accepted strategic/high-level decisions | decisions/ records produced by Definition | coherent |
| Master Plan | planning/MASTER_PLAN.md or project-declared equivalent | coherent |
| plan-review lifecycle | planning/reviews/<plan-revision>.md | coherent and separate from plan subject |
| Task Card contracts | implementation/cards/ + chatgpt_only Task Card contract | coherent |
| mutable implementation state | implementation/TASK_BOARD.yaml | coherent in normative modules |
| implementation-review lifecycle | Task Board review_state/review_subject/review_evidence | coherent owner, but card done ordering is contradictory |
| Git/branch/result provenance | Task Board pointers + exact Git state | coherent |
| blockers | Task Board blocked state + durable blocker evidence where material | coherent |
| OpenSpec | openspec/ exact change/spec + Card pointer | coherent |
| milestone acceptance | CLOSE + acceptance evidence + Task Board terminal fields | coherent |
| cumulative handoff | project-handoffs/MXX_HANDOFF.md | coherent; summary only |
| execution policy | PROJECT.md execution_policy, guarded by workflow/CONTEXT_ROUTING.md | coherent; explicit user change required |
| external-state readback | exact external readback evidence + Task Board/evidence pointer | coherent |
| active Definition/Research continuation | no single canonical owner for exact active research/return obligation | BLOCKING GAP |

No active implementation truth is intended to live only in chat. The blocking recovery finding concerns pre-execution Definition/Research lifecycle state, not Task Board execution state.

## 5. Real-stop / fresh-chat matrix

| Boundary | Real stop | Fresh chat | Notes |
|---|---:|---:|---|
| Brainstorm ready, promotion pending | yes | no | user chooses continue exploration or promote |
| unresolved product/strategic choice | yes | no | user authority required |
| explicit deployment/live-write/user authorization | yes | no unless separately needed | hard gate |
| concrete runtime/access/input blocker | yes when not self-remediable | no unless separately needed | smallest user action only |
| plan review REQUIRED/RECOMMENDED pending | yes | yes | author cannot review exact subject |
| implementation review REQUIRED/RECOMMENDED pending | yes | yes | implementer cannot review exact subject |
| GREEN plan review | no | no | route to Planning approval |
| RED plan review with deterministic correction | no | no immediately | correcting chat becomes plan author; later fresh re-review |
| GREEN implementation review | no | no | reviewer role ends, router continues |
| RED implementation review with bounded remediation | no | no immediately | remediating chat later stops for fresh re-review |
| Card completion with no review gate | no | no | router continues |
| milestone GREEN | no | no | Close/finalization/next approved milestone may continue |
| end of approved scope | yes | no | no action required unless user wants new scope |
| Context Health FRESH | yes | yes | only at safe durable boundary; cannot outrank stronger stop |

Context Health precedence is correct: existing review/user/authorization/runtime/strategic/end-scope stops own the boundary first. Context Health is neither a token/Card counter nor an authority source.

## 6. Normative duplication / contradiction inventory

| Rule family | Canonical owner / intended owner | Duplicate locations | Classification |
|---|---|---|---|
| global real stops | root CHATGPT.md | router, review, execution, close, context health | OK; role modules mostly specialize/pointer |
| Brainstorm promotion | chatgpt_only/ROUTER.md | common/BRAINSTORMING, common/DEFINITION, template/BRAINSTORM | OK; route owns policy-specific gate |
| plan review lifecycle | PLAN_REVIEW.md | PLANNING.md, root stop contract, README | OK |
| implementation review lifecycle | REVIEW.md + STATE.md | EXECUTION.md, TASK_CARDS.md, CLOSE.md, root | CONTRADICTION in terminal Card ordering; see B-01 |
| one-card-at-a-time | STATE.md | EXECUTION.md, EXECUTION_PREP.md, README | OK in normative route |
| JIT L1/L2 boundary | PLANNING.md + EXECUTION_PREP.md | TASK_CARDS.md, EXECUTION.md, STATE.md, README | DRIFT RISK; semantics currently aligned but repeated |
| strategic escalation Definition vs Planning vs Research | router / authority boundary | PLANNING, EXECUTION_PREP, EXECUTION, REVIEW, STATE, CLOSE | DRIFT RISK; same mapping independently restated many times |
| Task Board ownership | STATE.md + common/AUTHORITY | REPOSITORY, EXECUTION_PREP, EXECUTION, templates/docs | BLOCKING template contradiction; see B-03 |
| automatic next milestone | CLOSE.md + STATE.md | EXECUTION.md, router, README | DRIFT RISK but currently consistent |
| explicit authorization boundary | root + accepted Definition/Plan/Card contract | PLANNING, EXECUTION_PREP, EXECUTION, REVIEW, CLOSE | DRIFT RISK but currently consistent |
| Context Health precedence | CONTEXT_HEALTH.md + router | root CHATGPT.md, README | OK |
| recovery priority | RECOVERY.md + router bootstrap | STATE.md | OK for implementation; pre-execution gap remains |
| execution policy change | workflow/CONTEXT_ROUTING.md | PROJECT template, runtime modules, README | OK; explicit user decision consistently required |

Matching duplicated text was not automatically treated as success. The broad strategic-escalation and authorization mappings should be converted to one canonical rule plus short local pointers to reduce future drift.

## 7. Policy isolation / leakage matrix

| Check | Result | Evidence / reasoning |
|---|---|---|
| active chatgpt_only imports legacy/shared execution runtime | PASS | active module reference scan found no workflow/EXECUTION.md, workflow/contracts/TASK_EXECUTION.md, workflow/chatgpt/* or workflow/codex/* references; only top-level dispatcher references legacy route for other policies |
| mixed Capability Gate leaks into chatgpt_only | PASS | no active chatgpt_only reference; fixed ChatGPT executor is explicit |
| codex_only orchestration leaks into chatgpt_only | PASS | no active namespaced reference |
| Codex worker/model semantics leak into active chatgpt_only | PASS | none in active route |
| bounded-parallel project-card execution leaks into active normative modules | PASS in namespaced modules | STATE requires exactly one in_progress Card |
| bounded-parallel leaks through provided Task Board template | FAIL / BLOCKING | templates/TASK_BOARD.yaml explicitly offers serial or bounded_parallel and parallel metadata; no namespaced Task Board template exists |
| old shared workflow/EXECUTION.md or TASK_EXECUTION.md is active runtime authority | PASS | router forbids loading it under chatgpt_only |
| execution policy can silently change on runtime blocker | PASS | router/runtime modules require explicit user decision |
| common workflow modules impose chatgpt_only execution semantics on other policies | PASS | common AUTHORITY/BRAINSTORMING/RESEARCH/DEFINITION/OPENSPEC are policy-neutral |
| shared templates are entirely policy-neutral | PARTIAL | Task Board template is not; DECISION/BLOCKER contain optional Codex-specific provenance wording; shared TASK_CARD is intentionally legacy/shared and is bypassed by explicit namespaced TASK_CARD_TEMPLATE |

The shared templates/TASK_CARD.md is not an active chatgpt_only template because chatgpt_only/TASK_CARDS.md explicitly requires workflow/chatgpt_only/TASK_CARD_TEMPLATE.md. Therefore its parallel/shared-execution semantics are cleanup/isolation risk, not direct active leakage. The Task Board case is different because there is no equivalent namespaced board template.

## 8. Progressive-disclosure audit

PASS with one template exception.

The router provides role-specific REQUIRED context and conditional OpenSpec/handoff/evidence loads. It explicitly forbids loading legacy/shared execution or another policy namespace. Project Definition does not preload Planning/execution. Planning does not preload implementation machinery except active-project state when needed. Reviewers read the exact subject, same implementation-shaping authority slice and required evidence, not implementing-session narrative.

Common AUTHORITY correctly states that exact durable references outrank summaries and that context may be reduced only when applicable constraints remain lossless.

The exception is scaffolding: when Execution Prep creates the first Task Board, the route has no explicit serial-only board template. The only repository Task Board template contains other-policy parallel semantics, creating avoidable context/policy leakage.

## 9. Fresh-session recovery matrix

| Scenario | Result | Recovery basis |
|---|---|---|
| A. tentative Brainstorming | PASS | PROJECT Active exploratory scope pointer -> brainstorming record status tentative |
| B. ready_for_definition, promotion pending | PASS | pointed record contains ready status, pending authorization and no promotion subject |
| C. authorized exact Brainstorm scope before Definition | PASS | pointed record contains user_authorized + exact scope-id@revision |
| D. Definition <-> Research loop | FAIL | no canonical active research/return pointer or required research lifecycle status; Definition persists an evidence need, but Research artifact/template does not durably encode active/completed + origin/return target |
| E. draft plan pending independent plan review | PASS | revision-specific planning/reviews record is canonical; fresh-review handoff supplies exact pointer |
| F. GREEN plan awaiting approval/Execution Prep | PASS with discovery caveat | review record GREEN + exact plan subject allows Planning approval; standard plan/review naming or handoff locates state |
| G. READY Card | PASS | Task Board |
| H. in_progress Card | PASS | Task Board + branch/HEAD/runtime + RECOVERY priority |
| I. blocked Card | PASS | Task Board + blocker evidence |
| J. pending implementation review | PASS | Task Board review state outranks later implementation |
| K. review RED followed by correction | PASS if correction persists new exact subject/evidence | new subject must become pending for fresh re-review |
| L. milestone ready for Close | PASS | Task Board + milestone contract + review/evidence |
| M. GREEN milestone before next approved milestone | PASS | Close/STATE recover finalization or next approved milestone from Task Board/plan/checkpoint |
| N. Context Health fresh handoff | PASS | safe boundary + exact next obligation + durable pointer in generated fresh prompt |

Failure D is sufficient to violate the requested guarantee that exact next obligation be recoverable from repo/Git/runtime without the prior transcript.

## 10. Review independence audit

Plan review:

- exact plan author cannot independently review that exact subject: PASS.
- review state is separate from the plan subject: PASS.
- GREEN returns to Planning for deterministic approval: PASS.
- RED can route to bounded Planning correction, Definition or Research: PASS.
- substantive correction requires a new plan revision/review record: PASS.
- correcting reviewer becomes author of corrected subject and cannot self-review it: PASS.

Implementation review:

- implementer cannot independently review exact subject: PASS.
- reviewer may leave reviewer role after verdict and continue a new role: PASS.
- RED bounded remediation in same chat is allowed: PASS.
- after remediation that chat is implementer for new subject and fresh re-review is required: PASS.
- verdict is tied to exact review_subject: PASS in review fields.
- terminal Card state ordering: FAIL. EXECUTION.md line 27 says to mark the Card done before the later review boundary, while the same file line 103 requires GREEN independent review for Card completion and line 111 onward creates pending review after implementation. This is B-01.

## 11. JIT / authority-boundary audit

The intended boundaries are clear and currently coherent:

- L1: implementation detail inside accepted Card/milestone authority.
- L2: create/split/merge/reorder/replace not-yet-started Cards; refine technical interfaces/tests/implementation acceptance from predecessor evidence.
- Planning-owned: milestone structure/order/outcomes and execution strategy while Definition remains valid.
- Definition-owned: requirements, accepted strategic/high-level decisions, global product/system invariants, behavior/external contracts and authorization boundaries.
- Research-owned: evidence gaps.
- User-owned: unresolved product/strategic choices and explicit authorization decisions.

EXECUTION_PREP, PLANNING, EXECUTION and REVIEW all forbid hiding higher-authority changes as JIT/implementation detail. No direct JIT bypass was found.

The main weakness is duplication: the same escalation classifier is independently restated across many files. It is aligned at the frozen subject but is a future drift risk.

## 12. Publication / merge / approved-scope audit

The current route correctly separates implementation review from milestone Close. GREEN implementation review returns to the router; it is not itself a merge command. CLOSE performs integrated milestone acceptance, publication verification, finalization, Task Board reconciliation and cumulative handoff.

Automatic continuation into a next milestone is correctly conditioned on already-approved milestone authority, satisfied dependencies, green required reviews, deterministic JIT preparation and absence of strategic/user/deployment/live-write gates.

Non-blocking wording risk: CLOSE.md line 38 says GREEN proceeds to publication/finalization and line 59 says merge/finalize after required approval/checks, but it does not state as explicitly as it should that GREEN is evidence only and cannot expand the user's approved action scope. Global root scope/stop semantics already constrain this, so this is not classified blocking. Add an explicit sentence in CLOSE that merge/publish is legal only when already authorized by approved project scope/branch policy; otherwise stop for authorization/end-of-scope.

## 13. External writes / authorization audit

PASS.

EXECUTION requires meaningful material external mutation verification using WRITE -> READBACK -> VERIFY EXPECTED STATE -> EVIDENCE. Explicit deployment/live-write authorization remains a hard stop. Review recommends high-risk independent review at the last useful reversible point. CLOSE repeats that deployment/cutover/live-write gates remain hard.

Runtime blockers do not silently change execution policy. Destructive/high-risk work is routed into REQUIRED independent review categories, while user authorization remains a separate gate when required by accepted authority.

No automatic continuation path was found that explicitly overrides a due authorization gate.

## 14. Context Health audit

PASS.

Precedence is correct: an existing review/user/authorization/runtime/strategic/end-scope stop owns the boundary before Context Health. CONTEXT_HEALTH only runs at a safe durable boundary after the current obligation is persisted. It cannot interrupt an active Card, active review inspection or write/readback sequence. It does not create project state, alter authority, change execution policy or use fixed token/turn/Card/milestone counts.

## 15. Templates / prompts / docs audit

Prompts:

- CHATGPT_START.md routes through CHATGPT.md -> PROJECT.md -> CONTEXT_ROUTING.md and does not paste policy semantics: PASS.
- CHATGPT_PROJECT_INSTRUCTIONS.md stays small and router-driven: PASS.
- CHATGPT_FRESH_SESSION.md treats prompt text as a locator and durable repo as truth: PASS.
- no prompt was found that intentionally bypasses policy routing.

Core templates:

- PROJECT, BRAINSTORM, REQUIREMENTS, DECISION and MASTER_PLAN broadly match current Definition/Planning model.
- namespaced TASK_CARD_TEMPLATE matches serial ChatGPT-only policy and authority-slice requirements.
- shared TASK_BOARD template does not match active ChatGPT-only serial state contract: BLOCKING.
- RESEARCH template lacks lifecycle/origin/return metadata needed for deterministic Definition <-> Research recovery: part of B-02.
- MILESTONE template has no first-class field for REQUIRED/RECOMMENDED milestone-level independent review even though STATE/CLOSE permit such a contract. This is a non-blocking schema drift risk: the requirement can be written in free-form acceptance/gates, but the template should make it explicit when used.
- shared DECISION/BLOCKER templates retain optional Codex-specific provenance/correlation fields. They are conditional and do not change active chatgpt_only semantics, but they are not perfectly policy-neutral.

README:

README is consistent with the main normative architecture on policy-first routing, serial chatgpt_only execution, review independence, Context Health, JIT boundaries, explicit Brainstorm promotion and automatic approved-milestone continuation. No README statement was found that makes legacy/mixed/Codex runtime semantics active for chatgpt_only.

## 16. Dead / superseded instruction audit

The top-level shared workflow files and workflow/contracts files look generic, but they remain intentionally reachable by policies still on workflow/legacy/CONTEXT_ROUTING.md. They therefore should not be deleted merely because chatgpt_only has migrated.

For chatgpt_only, the active router explicitly forbids loading them. This isolation is sound.

Risky-looking but non-active files:

- templates/TASK_CARD.md still contains bounded-parallel/shared TASK_EXECUTION references. It is bypassed by the explicit namespaced TASK_CARD_TEMPLATE, so this is not an active contradiction.
- old workflow/chatgpt/CAPABILITY_GATE.md and codex orchestration remain reachable only through non-chatgpt_only routes.

Cleanup recommendation: mark legacy/shared Task Card and related templates with an explicit route-ownership header so a normal ChatGPT browsing the repository cannot mistake them for chatgpt_only scaffolding.

The Task Board template cannot be dismissed this way because no chatgpt_only-specific alternative currently exists.

## 17. Logical E2E scenario results

| # | Scenario | Result |
|---:|---|---|
| 1 | happy-path new project | PASS through Definition/Planning; architecture remains RED because first Task Board scaffolding has a contradictory shared template |
| 2 | long Brainstorming with several Research loops | PASS in one chat; fresh mid-Research recovery inherits B-02 |
| 3 | premature attempt to enter Definition | PASS; router stops for explicit promotion |
| 4 | authorized Definition needing more Research | PASS same-session; FAIL deterministic fresh recovery while Research is active |
| 5 | Definition returning to open-ended Brainstorming | PASS; new/revised exploratory subject resets promotion authorization |
| 6 | new plan + independent plan review GREEN | PASS |
| 7 | plan review RED + correction + re-review | PASS |
| 8 | normal serial execution | PASS for review-none Cards in normative modules; shared Task Board scaffold contradicts serial-only policy |
| 9 | JIT Card creation after predecessor evidence | PASS |
| 10 | implementation review GREEN | FAIL state-machine coherence because Card done transition is ordered before review gate |
| 11 | implementation review RED + bounded remediation + fresh re-review | remediation/fresh re-review logic PASS; terminal Card state before review is still ambiguous under B-01 |
| 12 | strategic defect discovered during Execution | PASS; routes Definition/Planning/Research by authority owner |
| 13 | runtime blocker | PASS; no silent policy/executor switch |
| 14 | explicit live-write authorization | PASS; hard stop before unauthorized mutation |
| 15 | milestone Close + automatic next milestone | PASS, with non-blocking wording hardening recommended for merge scope |
| 16 | fresh recovery from every material intermediate state | FAIL because Definition <-> Research exact continuation is not durably unique |

## 18. Historical losslessness

Historical/pre-split semantics were used only as comparison material.

Preserved:

- project repository as durable truth;
- Task Board as execution-state owner;
- exact authority slices and lossless progressive disclosure;
- WRITE -> READBACK -> VERIFY external-state semantics;
- runtime blocker behavior without silent policy change;
- L1/L2 JIT refinement and strategic escalation boundaries;
- independent review and fresh ChatGPT reviewer under chatgpt_only;
- automatic continuation across already-approved milestone boundaries;
- cumulative handoff and exact Git/result provenance.

Intentionally not preserved in chatgpt_only:

- mixed Capability Gate;
- project-card bounded parallel execution;
- Codex worker/model/orchestration semantics;
- legacy shared execution-runtime imports.

No additional required pre-split semantic was found missing merely because of the namespace isolation. However, the old shared Task Execution contract already made GREEN independent review a precondition for Card done; the namespaced EXECUTION.md now explicitly says mark Card done before it later creates pending review. That is a coherence regression against the intended preserved review gate, even though the surrounding review semantics themselves were retained.

The Definition/Research fresh-recovery gap appears to be a current architecture deficiency rather than a policy-isolation loss: the new promotion pointer solved Brainstorm recovery, but there is still no equivalent exact durable continuation record for an active Definition/Research evidence loop.

## 19. Findings

### RED / blocking

#### B-01 — Card done transition contradicts required independent-review gate

Evidence:

- workflow/chatgpt_only/EXECUTION.md line 27: step 14 says persist result/tests/evidence and mark Card done.
- the same file line 103: Definition of Done requires REQUIRED/RECOMMENDED independent review GREEN when review is a Card-completion requirement.
- the same file line 111 onward: after implementation, the implementing chat freezes subject, sets review_state pending and stops.
- workflow/chatgpt_only/TASK_CARDS.md line 82: REQUIRED and RECOMMENDED are real independent-review gates.

Why blocking:

A required-review Card cannot both be done and still await the review required for its Definition of Done. Following the loop literally creates an illegal terminal state; refusing to mark done means step 14 is wrong. The workflow does not define an unambiguous terminal transition after reviewer GREEN.

Exact remediation scope:

1. Choose one canonical state sequence and encode it in EXECUTION.md + STATE.md + REVIEW.md.
2. Recommended minimal sequence:
   - implementation/tests complete;
   - persist result pointers while Card remains non-done, normally in_progress;
   - set review_state pending and stop;
   - fresh reviewer sets green/red;
   - after GREEN, router performs deterministic Card-finalization transition and only then sets execution_status done;
   - after RED, correction keeps/reopens non-terminal state and produces a new subject.
3. Explicitly declare done + pending/in_progress REQUIRED/RECOMMENDED review invalid.
4. Add E2E state tests for GREEN and RED review paths.

#### B-02 — Definition <-> Research is not fully recoverable from durable state

Evidence:

- common/DEFINITION.md lines 113-115 says to persist the exact evidence need and route to Research.
- common/RESEARCH.md has no canonical active/completed research lifecycle state or origin/return contract.
- templates/RESEARCH.md records the question and findings but has no required Status, Origin, Definition subject/revision, or Return target.
- templates/PROJECT.md has Active exploratory scope, Requirements, Approved plan and Task Board pointers, but no exact active Research/Definition continuation pointer.
- router has explicit recovery pointer semantics for Brainstorm promotion and plan-review records, but not for active Research inside Definition.

Why blocking:

A fresh chat can encounter the same durable files while the legal obligation is either continue Research or return to Definition. The route can re-evaluate evidence heuristically, but the requested architecture requires exact recovery without previous transcript. This is especially ambiguous with multiple open research questions.

Exact remediation scope:

1. Add one canonical, policy-neutral durable continuation mechanism for pre-execution Definition/Research loops.
2. Keep PROJECT as a router/index, not a tracker: it may point to the exact active pre-execution record, while mutable lifecycle fields live in that pointed record.
3. Extend the Research contract/template with at least exact question ID/subject, origin role/scope, status active|complete|blocked, and exact return target.
4. Require Definition to persist and point to the research obligation before leaving Definition; require Research completion to persist the result and next return obligation before routing back.
5. Add fresh-session recovery tests for multiple simultaneous/open research questions and interrupted Research.

#### B-03 — Shared Task Board template violates chatgpt_only serial policy

Evidence:

- workflow/chatgpt_only/STATE.md line 103: exactly one project Card may be in_progress.
- workflow/chatgpt_only/EXECUTION_PREP.md line 40: set exactly the next eligible Card ready.
- templates/TASK_BOARD.yaml line 10 explicitly advertises execution_mode serial or bounded_parallel.
- the same template contains parallel_card_limit, chatgpt_control_chat, parallel_safe/write_scope/exclusive_resources/lane fields.
- repository tree at the frozen subject contains no chatgpt_only-specific Task Board template.

Why blocking:

The provided Task Board scaffold can create a state that the active chatgpt_only state contract declares illegal. It also leaks mixed/codex/legacy coordination semantics into the only shared board template available during first Execution Prep.

Exact remediation scope:

1. Add a chatgpt_only-specific serial Task Board template and explicitly reference it from EXECUTION_PREP.md and/or REPOSITORY.md; or split templates into policy-neutral core plus route-owned policy overlays.
2. ChatGPT-only template must not advertise bounded_parallel, lane ownership, Codex control-chat or other-policy scheduling fields.
3. Mark the existing shared Task Board template as legacy/other-policy scaffolding until all routes have explicit templates.
4. Add a policy-isolation test asserting that a newly scaffolded chatgpt_only Task Board cannot represent more than one active Card or bounded_parallel mode.

### Non-blocking drift risk

#### D-01 — Strategic escalation mapping is independently duplicated

The Definition vs Planning vs Research classifier is repeated across ROUTER, PLANNING, EXECUTION_PREP, EXECUTION, REVIEW, STATE and CLOSE. It is aligned at the frozen SHA but is a high-value future drift surface.

Remediation: place the authoritative classifier in one canonical common/authority or router section and replace most copies with local trigger wording plus pointer.

#### D-02 — CLOSE should state explicitly that GREEN does not grant merge/publication authority

Global scope/authorization rules already prevent unauthorized action, so current behavior is not classified contradictory. However CLOSE directly says GREEN proceeds to finalization.

Remediation: add one explicit invariant: GREEN is evidence/acceptance only; merge/publish/deploy occurs only if that action is already authorized by approved project scope/branch policy and no explicit gate is due. Otherwise stop at end-of-scope/authorization boundary.

#### D-03 — Milestone-level independent review is supported by runtime but not first-class in milestone templates

STATE/CLOSE allow a Card or milestone to be contracted REQUIRED/RECOMMENDED, while templates/MASTER_PLAN.md and templates/MILESTONE.md do not expose a dedicated milestone-review requirement field.

Remediation: add an optional explicit milestone independent-review field or a clearly named acceptance-review contract section.

### Cleanup only

#### C-01 — Legacy/shared Task Card template looks generic

templates/TASK_CARD.md contains parallel/shared-runtime references and legacy TASK_EXECUTION inheritance, but active chatgpt_only explicitly uses workflow/chatgpt_only/TASK_CARD_TEMPLATE.md.

Cleanup: add a strong route-ownership/legacy header rather than deleting it while other policies still depend on shared semantics.

#### C-02 — Optional Codex-specific fields remain in otherwise shared templates

templates/DECISION.md and templates/BLOCKER.md retain optional Codex correlation/provenance wording. They do not activate Codex semantics under chatgpt_only.

Cleanup: eventually move executor-specific provenance to policy-specific optional sections or rename fields generically.

## 20. Final verdict

RED.

The frozen chatgpt_only path is substantially improved and most of the policy-first architecture is coherent, including:

- explicit Brainstorming promotion authority;
- separation of Definition from Planning;
- independent plan-review subject/state separation;
- serial namespaced execution semantics;
- JIT authority boundaries;
- independent implementation review role transitions;
- Context Health precedence;
- explicit policy-change/user authorization gates;
- external write readback;
- milestone Close and automatic continuation inside already-approved scope;
- isolation from Capability Gate, Codex orchestration and legacy shared execution runtime.

It is not GREEN because three blocking inconsistencies remain:

1. Card completion is ordered before the independent review that its own Definition of Done requires.
2. an active Definition <-> Research loop is not deterministically recoverable from durable state without transcript/heuristic inference.
3. the only provided Task Board template can instantiate bounded-parallel/Codex coordination state forbidden by chatgpt_only.

No semantic remediation was applied in this audit. Any remediation changes the subject and requires a new fresh independent re-review against the new exact HEAD.
