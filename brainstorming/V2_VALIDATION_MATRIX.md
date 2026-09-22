# Project Workflow V2 — Validation Matrix

Date: 2026-09-22
Status: planned
V2 target repository: `elmakus/project_workflow_v2`

## Principle

Do not use more manual/user live testing than necessary.

Automate deterministic contract/schema/router/state behavior in the V2 repository. Reserve user-run live tests for behavior that depends on the real ChatGPT/Codex product surface, model/context switching, installed plugin packaging, or end-to-end GitHub integration.

No additional live test is required before Project Definition. The tests below are post-implementation acceptance/compatibility validation.

## A. Automated / agent-run validation

These should normally be implemented as repository tests or controlled integration fixtures and do **not** require the user to manually drive ChatGPT/Codex.

| ID | Scenario | Required result |
|---|---|---|
| A01 | V2 router progressive disclosure | Bootstrap/router loads only the current semantic module and exact durable refs; unrelated stage/docs/templates/migration files are not required. |
| A02 | No legacy semantic routing | No `execution_policy`, `chatgpt_only`, `codex_only`, Context Health, parallel-Card batch/lane or orchestration-binding semantics are required for new V2 state. |
| A03 | Workstream/manifest/Task Board binding | Exact branch/workstream identity and mutable board binding are validated; mismatches fail closed/recover. |
| A04 | One active Project Card | Only one Project Workflow Card executes at a time in the selected workstream; runtime-internal subagents do not create extra Cards. |
| A05 | Delegated result recovery | Durable completed worker result is reconciled rather than replayed after runtime loss. |
| A06 | Uncertain external effect | Readback occurs before retry; unresolved occurrence fails closed rather than duplicating the side effect. |
| A07 | Review attempt model | Exact immutable subject, append-only RED -> corrected subject -> new attempt -> GREEN behavior. |
| A08 | Review coverage reuse | Target SHA movement alone does not invalidate GREEN when subject/acceptance are unchanged and compatibility verification is GREEN. |
| A09 | Integration refresh | Actual behavior/content reconciliation creates a new review subject. |
| A10 | Terminal package / branch disappearance | Workstream remains recoverable after merged source branch auto-deletion. |
| A11 | Selective technical contract | Simple fix can be fully contracted by Task Card without duplicate OpenSpec; complex API/schema/idempotency/migration/security case triggers technical-contract module JIT. |
| A12 | YAGNI guard | Speculative complexity without current authority/evidence is rejected; required present-day quality obligations remain. |
| A13 | Research source breadth | Research contract requires mandatory-but-proportional official/upstream + issue/community prior-art coverage and explicit source weighting/conflict handling. |
| A14 | GitHub tracker dedup logic | Existing exact Issue/workstream is recovered instead of creating duplicate tracker state. |
| A15 | Legacy migration fixtures | Representative V1 `execution_policy`/state can be migrated once into common V2 without carrying permanent legacy semantic routes. |
| A16 | Fork release module trigger | Fork-version policy loads only for a durably declared downstream-fork release/version operation. |
| A17 | Coverage-matrix regression | Every V1 surface in `V1_TO_V2_COVERAGE_MATRIX.md` has an implemented KEEP/GENERALIZE/TRIGGER/MIGRATION/DROP assertion or documented non-code disposition. |

## B. User-run live acceptance tests

These validate real product/runtime behavior and should be run only after the relevant V2 implementation exists.

### L01 — ChatGPT Android bootstrap + adaptive Brainstorming

Surface: normal ChatGPT Android Project.

Setup:
- Project Instructions point to `elmakus/project_workflow_v2`;
- test project contains a valid V2 `PROJECT.md`.

Action:
- start a new chat with a nontrivial `#feature`.

PASS:
- ChatGPT resolves workflow from the V2 GitHub repo;
- creates/recovers the feature tracker/workstream as implemented;
- enters adaptive grilling automatically;
- user does not need `#grill`;
- agent does not begin implementation;
- questions are material, numbered and include recommendations;
- prior-art Research is performed when factual investigation is needed.

Why manual:
- validates actual Android ChatGPT Project Instructions/bootstrap behavior.

### L02 — `#issue` human-control boundary + GitHub tracker

Surface: normal ChatGPT Android + GitHub.

Action:
1. submit a real/disposable `#issue` with only the symptom, intentionally **without** explaining the desired repair;
2. allow diagnosis;
3. when the agent proposes a repair, ask a follow-up such as “czy to będzie bezpieczne?” instead of authorizing implementation;
4. only later explicitly authorize the accepted repair.

PASS:
- one GitHub Issue is created/recovered after dedup checks;
- diagnosis may proceed read-only;
- no implementation mutation happens before the post-diagnosis user response;
- follow-up discussion/grilling works;
- implementation starts only after explicit aligned authorization;
- workstream retains tracker correlation.

Critical regression protected:
- prevents the V1 failure mode `#issue -> diagnose -> autonomous fix/merge`.

### L03 — GitHub Issue/Feature final PR closure

Surface: GitHub integration.

Action:
- complete a test `#issue` or `#feature` through final integration.

PASS:
- intermediate PRs reference but do not prematurely close the tracker;
- final scope-completing PR carries the intended closing linkage;
- after default-branch merge, Close reads back Issue state;
- if automatic closure does not occur, explicit closure happens only after durable accepted completion;
- no duplicate Issue is created on recovery.

This can be combined with L02 where practical.

### L04 — Codex plugin entry and context economy

Surface: real Codex with updated `pw` plugin.

Action:
- install/update plugin from V2 package;
- invoke `$pw:project_workflow_v2` in a V2 project.

PASS:
- exact invocation resolves;
- Codex reads bundled local `workflow/`, not remote workflow repo, for ordinary policy acquisition;
- Skill/hook remain thin;
- only current router/module/durable refs are loaded progressively;
- missing/broken bundled router fails closed instead of reconstructing policy from memory/GitHub;
- no legacy policy route is selected.

### L05 — One-product plugin update propagation

Surface: real Codex plugin update.

Action:
1. land a harmless observable V2 workflow semantic/text fixture change that does **not** modify Skill/hook/bootstrap;
2. update the installed plugin;
3. start a fresh Codex session.

PASS:
- Codex sees the updated bundled canonical `workflow/`;
- no duplicate plugin-policy edit was required;
- `SKILL.md`/hook did not need modification.

This validates the core “plugin is delivery, not a second product” invariant.

### L06 — Cross-runtime durable portability

Surface: ChatGPT + Codex.

Action:
- start a V2 workstream in ChatGPT;
- stop at a safe durable boundary;
- continue the same exact workstream in Codex;
- later continue again in ChatGPT at another durable boundary.

PASS:
- no state conversion;
- no `runtime: chatgpt|codex` / execution-policy rewrite;
- same workstream/Card/review authority is recovered;
- completed durable work is reused, not replayed.

### L07 — Premium planning block A/B/C

Surface: ChatGPT model/context switching.

Action:
1. complete Project Definition;
2. observe stop A;
3. switch to best available model for Strategic Planning;
4. freeze Master Plan and observe stop B;
5. open fresh independent best-model context for Plan Review;
6. after GREEN observe stop C;
7. switch to lighter/cheaper model for downstream execution preparation.

PASS:
- no automatic crossing of A/B/C;
- planner does not spawn its own Stage-6 reviewer;
- fresh reviewer recovers exact durable subject;
- after GREEN reviewer does not enter Execution Prep;
- Recovery at any of these boundaries re-presents the stop.

### L08 — N-CAPABLE orchestration-topology continuity

Carry forward the existing deferred V1-harness scenario against real V2.

PASS sequence in one capable coordinating invocation:
`R01 RED -> bounded correction S2 -> R02 independent GREEN -> deterministic finalization`

No artificial user-facing stop is introduced.

### L09 — N-CHATGPT fresh-context continuity

Carry forward the existing deferred scenario against real V2.

PASS:
- first fresh review chat: `R01 RED -> same-chat correction S2 -> freeze R02 -> STOP at new independent-review boundary`;
- second fresh review chat: `R02 GREEN -> same-chat deterministic finalization -> completed`;
- stopping immediately after RED or immediately after GREEN is failure.

This specifically validates that a role boundary is not accidentally treated as a session-scope stop.

## C. Optional exploratory smoke tests

These are useful but not required for first V2 acceptance if equivalent automated coverage is strong:

- `#feature` GitHub tracker recovery in a second Android chat;
- intentionally break plugin package router and confirm fail-closed message;
- fork release flow on a disposable downstream-fork fixture;
- explicit safe branch-cleanup fallback when auto-delete is unavailable;
- legacy V1 workstream migration through a real project clone rather than only fixtures.

## User effort recommendation

Minimum manual set for first production acceptance:

1. **L01** ChatGPT Android feature/grilling;
2. **L02+L03 combined** Android issue -> discussion -> approved fix -> PR -> Issue closure;
3. **L04+L05 combined** Codex Skill/plugin/update propagation;
4. **L06** ChatGPT -> Codex -> ChatGPT portability;
5. **L07** premium A/B/C;
6. **L08/L09** deferred topology continuity tests.

Everything else should be automated or run by the implementing/reviewing agents where possible.

## Timing

Do not run L01-L09 now against V1.

Attach them to the V2 implementation plan and execute each only after its prerequisite V2 slice is actually implemented. A failed live test creates evidence for correction; it does not reopen unrelated already-settled product decisions unless the failure reveals a genuine semantic contradiction.
