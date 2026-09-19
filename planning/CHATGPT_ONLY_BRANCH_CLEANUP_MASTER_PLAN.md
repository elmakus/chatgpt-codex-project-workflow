# ChatGPT-only Branch Cleanup — Master Plan

Revision: BC-R1
Status: draft
Updated: 2026-09-19
Independent plan review: RECOMMENDED

> Planning organizes the approved branch-cleanup Definition. Requirements and accepted decision remain authoritative.

## 1. Accepted target / canonical inputs

- Requirements: requirements/CHATGPT_ONLY_BRANCH_CLEANUP.md
- Accepted decision: decisions/ADR_CHATGPT_ONLY_AUTODELETE_MERGED_HEAD_BRANCHES.md
- Exploratory provenance: brainstorming/BRANCH_DELETE_PREFIX.md, revision R3, explicitly promoted by user
- Workstream: implementation/workstreams/feature-branch-delete-prefix/WORKSTREAM.yaml
- Integration target: main

## 2. Execution baseline

Current ChatGPT-only workflow already provides:
- branch-isolated workstream manifests and workstream-local Task Boards;
- final integration refresh and fresh independent final-integration review;
- target-side terminal durable package requirements;
- terminal recovery after source-branch deletion;
- stacked parent/child reconciliation semantics.

Current gap:
- terminal source-branch deletion is ordered after post-merge closure/readback;
- source branch survival is therefore still implied during part of finalization;
- no connector-safe cleanup convention exists for closed/surviving branches;
- creating delete/* aliases is not a real rename and can duplicate refs.

## 3. Inherited non-goals / invariants / external constraints

- Do not create delete/* marker branches.
- Do not require ChatGPT connector support for branch rename/delete.
- Do not weaken review, integration-refresh or terminal recovery gates.
- Do not create a global mutable cleanup registry.
- Keep original workstream branch identity as provenance after deletion.
- Do not modify Codex-only policy in this workstream.
- GitHub automatic head-branch deletion is preferred when available, but workflow correctness must survive it being disabled or blocked.

## 4. Milestones

### M01 — Source-branch-independent finalization and cleanup

- Outcome: ChatGPT-only finalization remains fully recoverable when a merged PR head branch disappears immediately after merge, while non-merged/surviving terminal branches receive a connector-safe durable cleanup fallback.
- Checkpoint: reviewed, integrated workflow contracts and regression evidence on the current integration target.
- Acceptance:
  - pre-merge contract guarantees all unique recovery state is already target-durable or immutable via PR/merge evidence;
  - post-merge closure/readback never requires the source workstream branch;
  - automatic deletion of a merged head branch is normal success;
  - surviving merged branches and terminal unmerged branches can be marked safe_to_delete only after exact terminal safety proof;
  - delete/* alias creation is explicitly forbidden as rename emulation;
  - stacked child reconciliation remains legal after parent source-branch deletion;
  - existing legacy/default and historical workstreams remain valid;
  - Codex-only remains unchanged.
- Requirement coverage: BC-R1 through BC-R12.
- Dependencies: none beyond current accepted ChatGPT-only workstream/finalization contracts.
- Inherited constraints / rationale:
  - requirements/CHATGPT_ONLY_BRANCH_CLEANUP.md
  - decisions/ADR_CHATGPT_ONLY_AUTODELETE_MERGED_HEAD_BRANCHES.md
  - workflow/chatgpt_only/WORKSTREAMS.md
  - workflow/chatgpt_only/CLOSE.md
  - workflow/chatgpt_only/REPOSITORY.md
- Planned work packages:
  - reorder/clarify pre-merge versus post-merge terminal package and readback rules in WORKSTREAMS/CLOSE;
  - add an optional branch_cleanup fallback contract to workstream state/template, with exact ref/head/evidence and safe_to_delete/deleted lifecycle only when needed;
  - define repository policy for GitHub automatic merged-head deletion and connector capability fallback;
  - update Recovery/State/Router seams only where source-branch existence assumptions materially require it;
  - add explicit prohibition on alias-based rename emulation;
  - cover stacked parent deletion and accidental duplicate-ref recovery semantics;
  - update user/operator docs and changelog where necessary;
  - add static/coherence regression evidence for merged-auto-delete, merged-survives, closed-unmerged, stacked-parent-deleted and duplicate-alias cases.
- JIT decomposition / deferred-detail trigger: Execution Prep determines whether branch_cleanup schema needs a small OpenSpec and whether policy edits are best one Card or split into core-contract and regression/docs Cards.
- Planning re-evaluation trigger: implementation discovers that immediate source-branch disappearance cannot be made compatible without changing accepted milestone/review architecture.
- Definition re-open trigger: implementation requires weakening terminal durability, changing the accepted auto-delete/fallback product choice, or changing Codex-only scope.
- Boundary gate / explicit user authorization: repository-setting mutation for delete_branch_on_merge is an external configuration write. The workflow contract may document/prefer it; actually enabling it on a repository requires normal authorization/capability rules and must not block correctness because fallback cleanup exists.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Planned work package or JIT trigger | OpenSpec candidate |
|---|---|---|---|
| BC-R1, BC-R2, BC-R4, BC-R5 | M01 | pre/post-merge finalization ordering and target-side recovery | yes |
| BC-R3, BC-R10 | M01 | repository auto-delete policy + fallback | no |
| BC-R6, BC-R8 | M01 | branch_cleanup fallback state and safety gate | yes |
| BC-R7 | M01 | explicit no-alias rename rule + regression | no |
| BC-R9 | M01 | stacked parent deletion reconciliation | no |
| BC-R11 | M01 | backward compatibility and migration checks | no |
| BC-R12 | M01 | policy-scope audit | no |

## 6. Dependency / execution order

1. Refresh exact current main and workstream branch before implementation.
2. Define finalization ordering and fallback cleanup schema together so no duplicate state source is introduced.
3. Update the smallest policy/template surfaces required by that contract.
4. Run coherence/regression checks across finalization, recovery and stacked workstream paths.
5. Freeze exact implementation subject for independent review.
6. After GREEN review, run integration refresh against current main and integrate normally.

## 7. Deployment / migration / rollback strategy

No repository-wide migration.

- Existing terminal workstreams remain valid under historical semantics.
- New/updated ChatGPT-only workstreams consume the new cleanup contract when current workflow main contains it.
- Existing delete/* duplicate branches are cleanup debt, not state migration targets.
- Repository-level GitHub auto-delete may be enabled independently; disabling it later falls back to durable safe_to_delete behavior rather than invalidating workflow state.
- Rollback of the workflow change means reverting the policy/template changes; no source data migration is required.

## 8. System verification strategy

Verify at minimum:
1. merged PR head branch disappears immediately and terminal recovery still succeeds from target-side package + PR/merge metadata;
2. merged PR branch survives and receives safe_to_delete only after terminal safety;
3. closed/superseded unmerged branch is not marked safe merely because the PR is closed;
4. stacked parent branch disappears after merge and child refresh proves dependency satisfaction from target state;
5. no active policy tells ChatGPT to create delete/* as a rename surrogate;
6. legacy/default state and completed historical workstreams remain recoverable;
7. source-branch deletion never invalidates manifest branch provenance.

## 9. Idempotency / data-integrity / security strategy

- Post-merge closure/readback is idempotent after branch disappearance.
- branch_cleanup, when present, records exact original ref, verified head and evidence.
- A moved surviving branch invalidates stale cleanup readiness until revalidated.
- No force-update/force-rename is allowed to manufacture cleanup success.
- Duplicate refs are reconciled explicitly rather than inferred from names.

## 10. Explicit authorization boundaries

- Editing workflow contracts/templates inside this workstream is authorized by the accepted feature scope.
- Enabling or changing delete_branch_on_merge on a concrete repository is a separate external configuration write and follows normal authorization/capability handling.
- Physical deletion of fallback safe_to_delete branches is not required for this implementation and must only be performed by a cleanup-capable actor.

## 11. JIT / deferred decomposition map

Execution Prep decides:
- exact Card count;
- exact branch_cleanup manifest schema representation;
- whether OpenSpec materially improves schema/transition clarity;
- exact regression/audit artifact paths.

Those decisions must remain inside BC-R1..BC-R12.

## 12. Fresh-context boundaries

Independent plan review is RECOMMENDED because this is a new material plan changing finalization/recovery semantics.

Implementation final-integration review remains at least RECOMMENDED under existing workstream review policy.

## 13. Pre-implementation planning audit

- Definition Complete still GREEN: yes.
- False assumptions / P0/P1 risks: primary risk is relying on source-branch existence after merge; plan explicitly removes that dependency.
- Milestone boundaries/order: one milestone is sufficient; splitting would add ceremony without independent stable checkpoints.
- Dependency completeness: current workstream/finalization model is sufficient; no parent workstream dependency.
- Outcome-level acceptance: covers immediate auto-delete, surviving branch fallback, non-merged closure, stacked parent and duplicate alias cases.
- Requirement coverage: BC-R1..BC-R12 fully mapped.
- Migration/rollback: no repository-wide migration; fallback preserves operation without repo setting.
- System verification: explicit scenario matrix above.
- Data integrity/idempotency/security: exact ref/head evidence and stale-readiness invalidation covered.
- Authorization gates: external repository-setting mutation explicitly separated.
- OpenSpec boundaries: branch_cleanup state transition is a candidate to decide JIT.
- Overengineering/premature detail: no global registry, no speculative automation service, no forced historical cleanup.
- Remaining blockers: none.

Planning audit: GREEN.

## 14. Workflow references

- Policy router: workflow/chatgpt_only/ROUTER.md
- Project Definition: workflow/chatgpt_only/DEFINITION.md
- Planning: workflow/chatgpt_only/PLANNING.md
- Plan review: workflow/chatgpt_only/PLAN_REVIEW.md
- Workstreams: workflow/chatgpt_only/WORKSTREAMS.md
- Close/finalization: workflow/chatgpt_only/CLOSE.md
- Repository: workflow/chatgpt_only/REPOSITORY.md
