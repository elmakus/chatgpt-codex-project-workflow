# M03 handoff — Codex-only lifecycle migration

Date: 2026-09-20
Workstream: `feature-branch-first-managed-changes`
Branch: `feat/branch-first-managed-changes`
Plan revision: `BF-R3`

## Completed checkpoint

M03 is GREEN. Final reviewed implementation subject: `76abbc14ea2e7ae9a4e6d98146beb2b66f4515b6`.

Both M03 Cards are terminal with independent GREEN review. The accepted state provides:
- workstream-local Codex-only pre-execution routing/recovery;
- workstream-only active execution and Task Board ownership;
- deterministic fail-closed historical root/default migration before mutation with topology proof before branch creation/adoption;
- preserved Codex Main sole-writer ownership;
- preserved bounded-batch/post-batch review-drain and exact-subject Tester semantics;
- preserved implementation/recovery Research, micro-fix, target-refresh, terminal-package and source-deletion safety;
- policy-local separation from ChatGPT-only lifecycle mechanics.

Acceptance evidence: `implementation/workstreams/feature-branch-first-managed-changes/evidence/M03_ACCEPTANCE.md`.

## Authority now in force

- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` R1
- ADR-BF-001..003
- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md@BF-R3`
- `openspec/changes/branch-first-m03-codex-lifecycle/`

## Material deferred work

M04 owns repository dogfood, README/documentation/template closure, integrated active-path scans/regressions, final target refresh, final-integration review and PR integration.

The workstream remains unmerged on `feat/branch-first-managed-changes`; no milestone-local cross-branch refresh was required for M03.

## Next durable starting point

Return to the ChatGPT-only router. The next deterministic obligation is Execution Prep for approved milestone M04 — migration, documentation, dogfood and integrated regression closure.
