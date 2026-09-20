# M03 integrated acceptance — Codex-only lifecycle migration

Date: 2026-09-20
Milestone: `M03`
Plan revision: `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md@BF-R3`
Implementation head: `76abbc14ea2e7ae9a4e6d98146beb2b66f4515b6`
Verdict: **GREEN**

## Accepted outcome

M03 completes the Codex-only policy-local branch-first lifecycle migration covered by the approved milestone.

Integrated acceptance:
- generic/pre-execution Codex-only routing is workstream-local rather than root-`PROJECT.md` mutable state;
- active managed execution uses only the exact manifest-bound workstream Task Board; root/default state is recovery/migration input only;
- historical live root/default state migrates deterministically before mutation, with exact integration target/base and independent-versus-stacked topology proven before branch creation/adoption and ambiguity failing closed;
- manifest ↔ Task Board binding remains exact and mismatch cannot fall back to root/default state;
- Codex Main remains sole shared Task Board/integration-state writer;
- bounded batch membership/base/order, post-batch review drain and recovery lineage remain intact;
- exact-subject independent Tester semantics and Task-Board-owned implementation/recovery Research remain intact;
- runtime worker/session/model/profile/invocation/worktree identity remains outside durable Project Workflow state;
- micro-fix, target-refresh, terminal target-side package, post-merge recovery and branch-deletion safety remain coherent;
- Codex-only lifecycle contracts do not import ChatGPT-only lifecycle mechanics.

## Card/review evidence

- M03-T01: GREEN, independent review `implementation/workstreams/feature-branch-first-managed-changes/evidence/M03-T01_REVIEW_2.md`.
- M03-T02: GREEN, independent review `implementation/workstreams/feature-branch-first-managed-changes/evidence/M03-T02_REVIEW.md`.

## Verification

M03-T01 focused pre-execution regression coverage is GREEN 9/9; its corrected implementation evidence also records repository unittest discovery 19/19 PASS.

M03-T02 independent connector-backed replay against the exact immutable subject is GREEN 14/14, covering workstream-only execution state, topology-before-branch migration, fail-closed binding, Codex Main/Tester/Research ownership, bounded batches, micro-fix/target-refresh/terminal recovery, historical preservation, templates, runtime-identity exclusion and policy separation.

No separate Python/CI runner pass is claimed for M03-T02 because the available checkout attempt recorded in implementation evidence was blocked by DNS.

This milestone checkpoint remains on `feat/branch-first-managed-changes` and performs no cross-branch integration. The final workstream target-refresh/final-integration review gate remains deferred to M04.

## Result

**GREEN.** M03 is accepted and may close. M04 — migration, documentation, dogfood and integrated regression closure — is the next approved milestone.
