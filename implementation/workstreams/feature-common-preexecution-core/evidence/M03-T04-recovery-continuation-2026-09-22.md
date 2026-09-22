# M03-T04 — execution/review recovery and deterministic continuation evidence

Date: 2026-09-22
Card: `M03-T04`
Result: **GREEN**
Target repository: `elmakus/project_workflow_v2`
Target branch: `feat/pwv2-m03-execution-review`
Accepted target commit: `1d9aa10721d7eb5764dec9bfae857715bd555a34`
Accepted target tree: `4402bbb83461564717ced5ddcdf96eb6ba31e9e8`
Draft PR: `elmakus/project_workflow_v2#3`

## Recovery of interrupted durable work

At re-entry, the target branch already contained ten durable M03-T04 commits through `edb0009fa4a48d9cb1d2988292b40e3fcae6b67f`. The execution route reused and reconciled those durable results rather than replaying implementation.

That partial implementation already added:
- recovery/RED/blocker classification helpers and runtime-neutral recovery contract;
- proportional blocker state;
- exact-result / review-subject recovery checks;
- implementation-owned Research routing and once-only return behavior;
- deterministic route/crash-point tests.

## Pi Research interruption and reconciliation

The user-requested current Pi compatibility Research was durably opened from M03-T04, temporarily blocking the Card. It was completed against current upstream Pi/docs/source plus proportional tracker/community evidence, classified by `execution_resolution`, reconciled back to this Card and consumed.

Result:
- no accepted Definition, ADR or PWV2-P1 M03 strategy change is required;
- Pi remains only a compatibility/runtime candidate;
- Codex delivery/acceptance authority remains unchanged;
- M03 continues under the already accepted runtime-neutral Main/worker/reviewer boundary;
- no Pi/runtime/model/provider/session identity is added to Project Workflow state.

The earlier pre-execution Pi Research `research/PWV2_PI_RUNTIME_COMPATIBILITY_R1.md` and its accepted Strategic Planning reconciliation remain the milestone-level authority. The current M03-T04 Research independently reconfirmed that conclusion after durable recovery showed M03 was already active.

## CI correction and validation

The recovered T04 head initially had Actions run `35746126661` RED. The failure was not a strategy/semantic blocker:
1. three new review-recovery fixtures constructed a result locator without the exact commit/blob identity now required by the production recovery contract;
2. after fixing that fixture, run `35751050491` left one stale T03 expectation that RED review routed directly to `review_correction`, while M03-T04 intentionally introduced the intermediate `execution_resolution` classifier.

Bounded fixes:
- make the reviewable-result fixture carry exact immutable result identity;
- update the stale RED route expectation to `execution_resolution`.

No production behavior was weakened or rolled back.

Actions run `35751124535` on exact accepted head `1d9aa10721d7eb5764dec9bfae857715bd555a34` is GREEN:
- state-contract suite: **27/27 PASS**;
- router suite: **38/38 PASS**;
- execution-contract suite: **4/4 PASS**;
- review-contract suite: PASS;
- recovery-contract suite: **2/2 PASS**;
- package probe, production bundle validation, router checks and M01 baseline checks: PASS.

PR #3 readback at acceptance:
- exact head `1d9aa10721d7eb5764dec9bfae857715bd555a34`;
- base `main@95e4fb5b8b31a2d4a456171121d9965ac55d4d9a`;
- draft/open and mergeable;
- 26 changed files across the cumulative M03 branch.

## Accepted M03-T04 behavior

The exact target now proves:
- durable semantic result is reconciled before replay after runtime/session loss;
- a changed result cannot finalize under stale GREEN review coverage;
- pending/in-progress review for a different current result fails closed;
- terminal old review history remains immutable while changed result requires a new attempt;
- RED classification routes through the exact execution-resolution owner;
- missing evidence, user authority and runtime/access/input blockers have distinct routes;
- implementation-owned Research recovery precedes unrelated execution and preserves once-only reconciliation;
- no worker/session/model/provider identity is required for recovery.

No M04 behavior, deployment/cutover, Pi runtime adapter/package or live Pi qualification was introduced.
