# Codex-only Terminal Unmerged Branch Cleanup — Master Plan

Revision: CUBC-P1
Status: draft
Updated: 2026-09-20
Independent plan review: RECOMMENDED

> Planning organizes the approved CUBC-R1 Definition. Requirements and accepted decision remain authoritative.

## 1. Accepted target / canonical inputs

- Requirements: requirements/CODEX_ONLY_UNMERGED_BRANCH_CLEANUP.md
- Accepted decision: decisions/ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE.md
- Exploratory provenance: brainstorming/CODEX_ONLY_UNMERGED_BRANCH_CLEANUP.md, revision R1, explicitly promoted by user
- Project branch: feat/codex-only-unmerged-branch-cleanup
- Integration target: main

## 2. Execution baseline

Current Codex-only workflow already provides:
- branch-isolated workstream manifests with stable exact branch identity;
- `superseded` as an accepted terminal state when authority permits it;
- Codex Main ownership of shared workstream/integration state;
- durable terminal-safety rules that forbid branch deletion while live Card, Research, review, stacked-dependency or integration obligations remain;
- target-side terminal recovery for integrated `done` workstreams after source-branch deletion.

Current gap:
- the source-branch deletion gate is described only for successfully integrated workstreams;
- there is no explicit Codex-only terminal-unmerged closure/delete path;
- Recovery does not yet define the idempotent case “terminal unmerged state is durable but the source branch still exists / is already absent”.

Merged workstreams need no new behavior because repository-level automatic deletion owns that path.

## 3. Inherited non-goals / invariants / constraints

- Do not add `branch_cleanup`, `safe_to_delete` or a cleanup registry.
- Do not add a merged-branch fallback cleanup path.
- Do not infer cleanup targets from branch prefixes or PR closure.
- Do not weaken existing terminal-safety or stacked-workstream gates.
- Do not persist runtime worker/session/model/profile identities.
- Codex Main owns the lifecycle action; Executor/Tester workers do not.
- The supported Codex environment provides authenticated `gh` access for normal branch deletion.

## 4. Milestone

### M01 — Terminal-unmerged closure and branch deletion

Outcome:
A branch-isolated Codex-only workstream that is intentionally terminal without final integration/merge becomes durably recoverable without its source branch, then Codex Main removes that exact branch through `gh`. Recovery finishes the same action idempotently after interruption.

Checkpoint:
Reviewed and integrated Codex-only lifecycle/recovery contracts plus regression evidence proving the terminal-unmerged path and unchanged merged path.

Acceptance:
- terminal-unmerged closure cannot proceed while any existing workstream safety obligation still requires the source branch;
- before deletion, the terminal closure/history needed for future recovery is durable independently of the source branch, using the existing namespaced workstream model on the appropriate target-side closure package rather than integrating rejected/superseded implementation content;
- Codex Main deletes only the exact manifest-owned source branch;
- no separate cleanup state is created;
- Recovery deletes the exact branch when terminal-unmerged state is durable and the branch still exists;
- Recovery treats an already-absent exact branch as cleanup complete and never recreates it;
- merged workstreams receive no new Codex-only cleanup lifecycle or fallback;
- stacked/dependent work prevents deletion while the branch is still genuinely required.

Requirement coverage: CUBC-REQ-001 through CUBC-REQ-008.

Dependencies:
Current Codex-only workstream identity, terminal-safety, Recovery and Main/runtime ownership contracts.

Planned work packages:
- extend `workflow/codex_only/WORKSTREAMS.md` with terminal-unmerged closure/recovery semantics and exact-branch cleanup eligibility;
- extend `workflow/codex_only/CLOSE.md` with the Main-owned terminal-unmerged close sequence: durable closure package first, exact branch deletion through `gh` second;
- extend `workflow/codex_only/RECOVERY.md` with idempotent surviving/absent branch handling after terminal-unmerged closure;
- update `workflow/codex_only/ROUTER.md` only as needed so an unfinished terminal-unmerged cleanup obligation routes deterministically to Close/Recovery rather than disappearing from the lifecycle;
- update `workflow/codex_only/REPOSITORY.md` only where recovery/branch-policy wording must recognize terminal-unmerged history after deletion;
- avoid `WORKSTREAM_TEMPLATE.yaml` schema changes unless execution discovers a pre-existing terminal-state field/comment needs clarification; no cleanup field may be added;
- add bounded regression/audit evidence for the terminal-unmerged delete and recovery cases plus unchanged merged behavior.

JIT decomposition trigger:
Execution Prep chooses the smallest Card split after refreshing current `main` and exact Codex-only contract seams. Prefer one implementation Card if the contract edits remain tightly coupled; split regression/docs only if independent acceptance materially improves reviewability.

Planning re-evaluation trigger:
Implementation shows that terminal-unmerged recovery cannot be represented using existing manifest/terminal state plus target-side closure history without introducing a new durable product/system state.

Definition re-open trigger:
Implementation would require adding a separate cleanup lifecycle, changing merged-workstream behavior, weakening terminal-safety gates, or moving lifecycle ownership away from Codex Main.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Planned work package / proof |
|---|---|---|
| CUBC-REQ-001, CUBC-REQ-003, CUBC-REQ-004 | M01 | Close/Workstreams exact manifest branch deletion by Codex Main through `gh` |
| CUBC-REQ-002 | M01 | reuse and explicitly bind existing terminal-safety + target-side closure durability gates |
| CUBC-REQ-005 | M01 | Recovery surviving-branch delete / absent-branch success cases |
| CUBC-REQ-006 | M01 | schema/state audit proving no `branch_cleanup` or equivalent lifecycle added |
| CUBC-REQ-007 | M01 | merged-path regression proving no new Codex-only fallback |
| CUBC-REQ-008 | M01 | Main ownership and runtime-boundary audit |

## 6. Dependency / execution order

1. Refresh exact current `main` and compare Codex-only Workstreams/Close/Recovery/Router/Repository seams.
2. Define the minimal terminal-unmerged closure package and routing semantics using existing workstream state.
3. Add the Main-owned delete step after durable closure safety is satisfied.
4. Add Recovery for interruption before/after delete.
5. Run coherence/regression checks including stacked/dependency safety and unchanged merged behavior.
6. Freeze the exact implementation subject for the required/recommended downstream review path and integrate normally after GREEN.

## 7. Deployment / migration / rollback

No repository-wide migration.

- Existing historical workstreams remain valid.
- New behavior applies when current workflow contracts contain CUBC-R1 semantics.
- No historical branch sweep is part of this milestone.
- Rollback is a workflow-contract revert; no cleanup-state migration is required because no new cleanup state exists.

## 8. System verification strategy

Verify at minimum:
1. terminal `superseded` workstream + all safety gates satisfied → target-side closure history is durable, exact source branch is deleted;
2. interruption after durable terminal closure but before delete → Recovery sees the exact branch and deletes it;
3. interruption after branch deletion → Recovery sees the exact branch absent and completes without recreation;
4. live stacked/dependency obligation → terminal-unmerged deletion is not eligible;
5. merged workstream path remains repository-auto-delete only, with no new Codex-only cleanup state/fallback;
6. deletion target always comes from exact manifest identity, never naming heuristics;
7. no Task Board cleanup registry or runtime worker/session identity is introduced.

## 9. Data integrity / idempotency / security

- Terminal history required for recovery must survive source-branch deletion.
- A delete is safe only after existing terminal-safety conditions are satisfied.
- Recovery derives unfinished cleanup from terminal-unmerged durable state plus exact current branch existence.
- Absence of the exact branch is success, not an error and never a reason to recreate it.
- No substitute/alias refs are created.
- No implementation content rejected by supersession is merged merely to preserve cleanup metadata.

## 10. Authorization boundaries

The approved Definition authorizes this Codex-only lifecycle behavior. No additional per-delete Project Workflow user gate is introduced for a workstream that has already validly reached the terminal-unmerged state under accepted authority.

This planning/implementation scope does not bulk-delete historical branches or change repository settings.

## 11. JIT / OpenSpec boundary

No OpenSpec is planned by default. The workflow Markdown contracts themselves own this lifecycle behavior.

Execution Prep may introduce a small OpenSpec only if current-source refresh reveals a real cross-file state-transition ambiguity that cannot be reviewed clearly in the owning workflow contracts.

## 12. Fresh-context / review boundary

Independent plan review is RECOMMENDED because this is a new material plan changing Codex-only terminal/recovery semantics.

Implementation subject review follows the existing current policy/workstream review rules after Execution Prep.

## 13. Pre-implementation planning audit

- Definition Complete: GREEN.
- Scope: one terminal-unmerged cleanup behavior; merged cleanup explicitly excluded.
- False assumptions / P0-P1 risks: primary risk is deleting the only durable copy of terminal history; plan requires target-side closure durability before delete.
- Milestone structure: one milestone is sufficient; there is one integrated lifecycle outcome.
- Requirement coverage: CUBC-REQ-001..008 fully mapped.
- Dependency completeness: current terminal-safety and stacked-workstream gates are reused.
- Migration/rollback: no schema/data migration.
- Verification: interruption before delete, interruption after delete, stacked dependency, exact branch identity and unchanged merged path are explicit.
- Data integrity/idempotency: terminal state + branch existence is the complete recovery input; no duplicate cleanup state.
- Authorization: accepted Definition owns automatic cleanup after valid terminal-unmerged closure.
- OpenSpec: not needed unless JIT finds a concrete cross-contract ambiguity.
- Overengineering check: no cleanup registry, no merged fallback, no permission framework, no CAS/lease protocol.
- Remaining blockers: none.

Planning audit: GREEN.

## 14. Workflow references

- Policy router: workflow/chatgpt_only/ROUTER.md
- Project Definition: workflow/chatgpt_only/DEFINITION.md
- Planning: workflow/chatgpt_only/PLANNING.md
- Plan review: workflow/chatgpt_only/PLAN_REVIEW.md
- Codex-only workstreams: workflow/codex_only/WORKSTREAMS.md
- Codex-only Close: workflow/codex_only/CLOSE.md
- Codex-only Recovery: workflow/codex_only/RECOVERY.md
- Codex-only repository contract: workflow/codex_only/REPOSITORY.md
