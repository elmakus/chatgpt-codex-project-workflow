# M03 Execution Prep — 2026-09-22

Workstream: `feature-common-preexecution-core`
Plan: `PWV2-P1`
Milestone: `M03 — JIT execution, delegated results and common independent review`
Target repository: `elmakus/project_workflow_v2`
Target branch: `feat/pwv2-m03-execution-review`
Creation base: `main@95e4fb5b8b31a2d4a456171121d9965ac55d4d9a`

## Preconditions

- M02 is GREEN and integrated through target PR #2.
- Target M02 merge tree is identical to the reviewed M02 tree.
- Frozen Definition R1 and approved PWV2-P1 remain valid.
- Bounded Pi Research `PWV2-PI-R1` is applied/consumed; Strategic Planning reconciliation found no Definition/Plan contradiction.
- Codex remains the accepted/qualified runtime delivery surface; Pi remains a compatibility candidate only.
- Construction custody remains in the V1 control workstream.

## JIT decomposition

Current predecessor evidence makes five bounded Cards contractible now:

1. M03-T01 — JIT Card contracts and execution-readiness semantics.
2. M03-T02 — runtime-neutral execution, delegation and result reconciliation.
3. M03-T03 — exact-subject common independent review.
4. M03-T04 — execution/review recovery and deterministic continuation.
5. M03-T05 — cumulative M03 acceptance and immutable review freeze.

The split follows stable semantic concerns rather than concrete runtime adapters. M03-T01..T04 remain review-free individually and are covered by the cumulative exact-subject independent review in M03-T05. No OpenSpec is created during initial preparation: the current Cards carry the required common state/router behavior contracts, while M03-T01 explicitly tests the selective technical-contract trigger.

## Pi boundary carried into execution

Pi Research validates the existing M03 abstraction boundary and does not add Pi-specific implementation scope:
- no Pi extension/package is implemented in M03 common semantics;
- no model/provider/session/worker identity is persisted;
- no generic runtime adapter API is invented;
- later Pi compatibility qualification may implement a minimal Pi Package/extension against this common contract after a real Pi installation exists.

## Next legal obligation

M03-T01 is READY. The target branch exists exactly from integrated M02 target `main`. A draft PR will be opened after the first M03 implementation commit because GitHub does not allow a PR with zero diff.

No production adoption/cutover, Pi runtime selection or consumer migration is authorized.
