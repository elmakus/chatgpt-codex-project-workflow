# M06-T02 — safe semantic conversion and obligation preservation

Date: 2026-09-23
Result: GREEN

## Exact target

- Repository: `elmakus/project_workflow_v2`
- Branch: `feat/pwv2-m06-migration`
- Commit: `ca92f27192eb4e54901a31de78c206cf814ed98c`
- Tree: `bccae82be133b38240aaad8044877f81d66d1b6d`
- Draft PR: #6
- Base: `main@27b9132e173850e7d596092e023b0af7e0507472`

## Implemented conversion contract

The bounded migration module now converts a GREEN dry-run snapshot to an in-memory common-V2 bundle without mutation:
- canonical V2 `WORKSTREAM` and `TASK_BOARD` objects validate through the production state validators;
- source branch/base/parent/dependency/integration target, plan/milestone snapshot and review snapshot are retained as migration provenance;
- legacy root state is mapped to a branch-local V2 destination owner rather than treating historical root state as live V2 state;
- stable Card/result/review/evidence artifacts are expressed as destination locators/planned copies;
- DONE V1 Cards remain result-to-reconcile records rather than replayed execution;
- V1 runtime/policy/scheduler keys are absent from canonical V2 output;
- unresolved research is mapped to the common workstream-local Research locator.

Review semantics are fail-closed:
- a V1 terminal verdict is reusable only with exact git-blob subject identity, exact binding to the current V1 review subject, terminal evidence, and durable semantic-independence proof;
- absent or mismatched proof does not invent GREEN: the Card becomes blocked with an explicit review obligation while source verdict/subject/evidence remain provenance;
- exact RED remains blocking;
- exact RED -> corrected subject -> GREEN history remains ordered append-only attempts.

No destination write or activation was added in T02.

## Verification

GitHub Actions run `35842412193`, job `107120370741`: completed / success.

`sh scripts/test.sh` readback includes:
- migration/conversion combined final group: 56/56 GREEN;
- state: 28/28 GREEN;
- router: 39/39 GREEN;
- execution: 4/4 GREEN;
- review and recovery suites GREEN;
- existing package/shell probes PASS.

## Acceptance

M06-T02 is GREEN for A02/A03/A05/A07/A15/A17 affected semantics. Apply/idempotency/restart/rollback remains exclusively M06-T03.
