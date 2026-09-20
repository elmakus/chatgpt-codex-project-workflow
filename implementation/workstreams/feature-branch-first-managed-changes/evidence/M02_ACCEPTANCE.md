# M02 integrated acceptance — ChatGPT-only lifecycle migration

Date: 2026-09-20
Milestone: `M02`
Plan revision: `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md@BF-R3`
Implementation head: `a3726bf22db1103e1a53c8d6e8256647699b6267`
Verdict: **GREEN**

## Accepted outcome

M02 completes the ChatGPT-only policy-local branch-first lifecycle migration covered by the approved milestone.

Integrated acceptance:
- pre-execution exploratory, Research and plan-review routing is recovered from the selected workstream-local manifest/records rather than root mutable project pointers;
- the user-owned Brainstorming → Project Definition promotion gate remains intact;
- pre-execution Research return/reconciliation remains crash-safe and workstream-local;
- Execution Prep and mutable execution state use only the exact manifest-bound workstream Task Board for active managed work;
- historical root/default execution state is recovery/migration input only and must migrate deterministically before further managed mutation;
- historical migration proves exact integration target/base and independent-versus-stacked dependency topology before branch creation/adoption, fails closed on ambiguity, and validates persisted topology/binding before ownership switches;
- Card/milestone review and implementation/recovery Research remain Task-Board-owned while manifest review remains final-integration-only;
- micro-fix proportionality, target refresh, terminal target-side recovery and source-branch-deletion safety remain coherent;
- ChatGPT-only lifecycle contracts do not import Codex-only lifecycle semantics.

## Card/review evidence

- M02-T01: GREEN, independent review `implementation/workstreams/feature-branch-first-managed-changes/evidence/M02-T01_REVIEW.md`.
- M02-T02: GREEN, independent review `implementation/workstreams/feature-branch-first-managed-changes/evidence/M02-T02_REVIEW.md`.

## Verification

M02-T01 exact branch readback/focused scenarios are GREEN for workstream-local pre-execution routing, promotion, Research reconciliation, plan-review recovery and policy separation.

M02-T02 exact subject readback plus independent connector-backed replay of the committed focused contract suite is GREEN **52/52**, covering workstream-only execution, deterministic historical migration, binding failure behavior, review/Research ownership, micro-fix/target-refresh/terminal recovery, historical preservation, templates/OpenSpec and policy separation.

No Python/CI runner pass is claimed for M02-T02 because the available local checkout attempt was blocked by DNS. The acceptance relies only on the exact durable evidence actually obtained.

This milestone checkpoint remains on `feat/branch-first-managed-changes` and performs no cross-branch integration. The final workstream target-refresh/final-integration gate therefore remains deferred to M04.

## Result

**GREEN.** M02 is accepted and may close. M03 — Codex-only lifecycle migration — is the next approved milestone.
