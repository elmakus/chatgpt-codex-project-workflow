# Independent Plan Review — BF-R1

Plan revision: BF-R1
Review requirement: RECOMMENDED
Review state: red
Review subject: commit `36b4f49a01691e7d31f3a8f892483b65b1408469`, file `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md`
Review evidence: RED — the plan has an internal requirement-ownership inconsistency. M01 declares ownership of `REQ-BF-001..011`, which includes `REQ-BF-010`, while the requirement coverage matrix assigns `REQ-BF-010` only to M04 and M01 acceptance/work packages do not define a distinct canonical-root-artifact merge-semantics outcome for REQ-BF-010. This makes milestone accountability ambiguous. The accepted Definition/ADRs do not need reopening: the defect is bounded to Planning and must reconcile M01 ownership with the coverage matrix/checkpoint. The remaining independent audit areas are GREEN: REQ-BF-001..017 are otherwise covered; natural-language managed-change entry and neutral kind/naming are represented without mandatory markers; branch-before-write versus branch-free read-only exploration is preserved; legacy/default is recovery/migration-only in the target; workstream-local pre-execution routing replaces root mutable pointers; root target truth versus branch-proposed canonical artifacts is preserved; ChatGPT-only/Codex-only mechanics stay policy-local; PR-only integration, target refresh, terminal package retention and source-branch deletion safety are covered; migration/rollback, verification, idempotency, authorization gates, OpenSpec/JIT boundaries and avoidance of speculative Task Cards are represented.

## Review authority

Review the immutable BF-R1 Master Plan against:
- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` Revision R1 (`approved`);
- `decisions/ADR_BRANCH_FIRST_MANAGED_CHANGE_LIFECYCLE.md` (ADR-BF-001);
- `decisions/ADR_WORKSTREAM_LOCAL_ROUTING_STATE.md` (ADR-BF-002);
- `decisions/ADR_POLICY_LOCAL_BRANCH_FIRST.md` (ADR-BF-003);
- `brainstorming/branch-first-managed-changes.md` only as provenance, not authority;
- current workflow/source baseline only where needed to test plan assumptions.

## Required review focus

Apply the standard independent plan-review audit from current Project Workflow, with particular attention to:
- whether the plan fully eliminates legacy/default as a new-work destination under both fixed policies while preserving safe recovery/migration;
- whether generic natural-language managed-change entry can be made deterministic without requiring `#issue` / `#feature`;
- whether branch creation occurs before every durable change-specific write while read-only exploration remains branch-free;
- whether workstream-local pre-execution routing can replace root `PROJECT.md` mutable pointers without losing crash recovery;
- whether root canonical artifacts remain unambiguous integrated truth on the target while branches can propose their future state;
- whether ChatGPT-only and Codex-only mechanics remain policy-local and preserve their different review/execution semantics;
- whether PR-only integration, target refresh, terminal package retention and source-branch deletion safety are complete;
- whether the milestone/JIT structure covers all REQ-BF-001..017 without premature implementation detail.

Do not mutate `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md` while reviewing. Persist GREEN/RED evidence in this record.
