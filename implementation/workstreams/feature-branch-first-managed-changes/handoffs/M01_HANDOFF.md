# M01 handoff — branch-first state model and generic managed-change entry

Date: 2026-09-20
Workstream: `feature-branch-first-managed-changes`
Branch: `feat/branch-first-managed-changes`
Plan revision: `BF-R3`

## Completed checkpoint

M01 is GREEN. Final reviewed implementation subject: `aa2d0e578940bf6cac92d9191a3f37277a0f447b`.

All three M01 Cards are terminal with independent GREEN review. The accepted state provides:
- neutral generic managed-change identity and workstream-local routing locators in both fixed policies;
- natural-language managed-change entry plus deterministic recovery/collision behavior;
- branch-before-write bootstrap/adoption;
- recovery/migration-only treatment of historical root/default state;
- integrated-project-only root PROJECT target semantics;
- policy-neutral common invariant with policy-local lifecycle mechanics.

Acceptance evidence: `implementation/workstreams/feature-branch-first-managed-changes/evidence/M01_ACCEPTANCE.md`.

## Authority now in force

- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` R1
- ADR-BF-001..003
- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md@BF-R3`
- `openspec/changes/branch-first-m01-state-entry/`

## Material deferred work

M02 must migrate ChatGPT-only Brainstorming/Research/Definition/Planning/plan-review and execution-state selection to workstream-local ownership. M03 performs the Codex-only equivalent. M04 closes project dogfood/docs/integrated regression.

Current `main` moved after the workstream baseline. M01 acceptance is a same-branch checkpoint; final target refresh remains mandatory before workstream integration.

## Next durable starting point

Return to the ChatGPT-only router. The next deterministic obligation is Execution Prep for approved milestone M02 — ChatGPT-only lifecycle migration.
