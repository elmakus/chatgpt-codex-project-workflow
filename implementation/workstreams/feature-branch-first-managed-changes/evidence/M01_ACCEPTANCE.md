# M01 integrated acceptance — branch-first state model and generic managed-change entry

Date: 2026-09-20
Milestone: `M01`
Plan revision: `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md@BF-R3`
Implementation head: `aa2d0e578940bf6cac92d9191a3f37277a0f447b`
Verdict: **GREEN**

## Accepted outcome

M01 establishes the branch-first fixed-policy state model and generic managed-change entry contract without performing the full M02/M03 lifecycle migration.

Integrated acceptance:
- both fixed-policy workstream schemas support neutral `kind: change` plus the same three workstream-local pre-execution routing locators;
- natural-language managed-change authorization enters policy-local Intake while read-only exploration remains branch-free;
- generic identity/naming/recovery is deterministic and fail-closed;
- newly authorized managed work creates or recovers an exact branch-isolated workstream before the first durable change-specific write;
- historical root/default state is recovery/migration input only and cannot be the mutable destination for new or continued managed work;
- root `PROJECT.md` target/template is integrated-project navigation rather than active workstream-local routing state;
- common authority carries only the neutral branch-first/integration-target invariant; policy lifecycle mechanics remain separate.

## Card/review evidence

- M01-T01: GREEN, independent review `implementation/workstreams/feature-branch-first-managed-changes/evidence/M01-T01_REVIEW.md`.
- M01-T02: GREEN, independent review `implementation/workstreams/feature-branch-first-managed-changes/evidence/M01-T02_REVIEW.md`.
- M01-T03: GREEN, independent review `implementation/workstreams/feature-branch-first-managed-changes/evidence/M01-T03_REVIEW.md`.

## Verification

Focused integrated readback confirms the neutral kind/routing schema, natural-language entry, read-only boundary, deterministic generic identity, branch-before-write ordering, recovery-only default boundary, integrated PROJECT target semantics and policy-local separation.

No exact-subject CI/status checks or workflow runs were reported for M01-T03; no CI-execution claim is made.

This milestone checkpoint remains on `feat/branch-first-managed-changes` and performs no cross-branch integration. Final target refresh/reconciliation is therefore not run at this checkpoint and remains mandatory before final workstream integration.

## Deferred scope

- M02 owns the full ChatGPT-only lifecycle migration away from root PROJECT pre-execution pointers/default execution state.
- M03 owns the analogous Codex-only lifecycle migration.
- M04 owns repository dogfood, README/documentation closure and integrated regression/final integration work.

## Result

**GREEN.** M01 is accepted and may close. M02 is the next approved milestone.
