# Requirements — branch-first managed changes

Revision: `R1`
Status: `approved`
Updated: `2026-09-20`

## Goal / target state

Project Workflow must treat the repository integration target (normally `main`) as integrated project truth only. Every new managed repository change, from the first durable change-specific write through implementation and review, must live on a branch-isolated workstream and reach the integration target only through a pull request and merge.

The user must not need to know or choose `#issue` / `#feature` before Project Workflow can create the correct isolated workstream.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| REQ-BF-001 | A new managed change MUST NOT author change-specific durable state directly on its integration target. | MUST | User decision; ADR-BF-001 | accepted |
| REQ-BF-002 | Before the first durable managed-change write, Project Workflow MUST create or recover an exact branch-isolated workstream. | MUST | User decision; ADR-BF-001 | accepted |
| REQ-BF-003 | Read-only exploration/comparison MAY occur before a workstream exists. The transition to a managed repository change occurs when the user authorizes repository/project mutation or otherwise clearly requests Project Workflow to implement/adopt the change. | MUST | User decision; ADR-BF-001 | accepted |
| REQ-BF-004 | Natural-language change authorization MUST be sufficient to create/recover a workstream. `#issue` and `#feature` remain optional explicit intake shortcuts, not required syntax. | MUST | User decision; ADR-BF-001 | accepted |
| REQ-BF-005 | A generic unclassified managed change MUST be representable without guessing issue versus feature; the target model MUST provide a neutral workstream kind/naming path. | MUST | Consequence of REQ-BF-004; ADR-BF-001 | accepted |
| REQ-BF-006 | A workstream MUST span the full managed-change lifecycle applicable to that scope: discovery/brainstorming, Research, Project Definition, Planning, Execution Prep, implementation, review, integration and terminal closure. | MUST | User decision; ADR-BF-001 | accepted |
| REQ-BF-007 | The legacy/default root execution-state model MUST NOT be selected for new work under either `chatgpt_only` or `codex_only`. Existing legacy/default state may be read only for recovery/migration and MUST transition to a branch-isolated workstream before further managed-change mutation. | MUST | User decision; ADR-BF-001 | accepted |
| REQ-BF-008 | Root `PROJECT.md` MUST describe integrated project-level routing/authority and MUST NOT own active workstream-local mutable pointers such as the current exploratory scope or pre-execution Research obligation in the target model. | MUST | User decision; ADR-BF-002 | accepted |
| REQ-BF-009 | Active workstream-local routing/lifecycle pointers MUST be owned by the workstream manifest or exact artifacts referenced from that manifest; no repository-global mutable workstream registry may be required. | MUST | User decision; ADR-BF-002 | accepted |
| REQ-BF-010 | Root canonical artifacts such as `requirements/`, `decisions/`, `planning/` and project source MAY be edited on a workstream branch as the proposed future integrated state. The integration-target versions remain canonical integrated truth until the PR merges. | MUST | User decision; ADR-BF-002 | accepted |
| REQ-BF-011 | Every managed change, including trivial documentation/configuration/code changes, MUST integrate through branch → PR → merge. Project Workflow MUST NOT use normal direct pushes to the integration target. | MUST | User decision; ADR-BF-001 | accepted |
| REQ-BF-012 | Final integration MUST preserve the existing target-refresh/conflict/verification/review safety semantics before merge. | MUST | Existing workstream safety model; ADR-BF-001 | accepted |
| REQ-BF-013 | After merge, the terminal namespaced workstream package MUST remain on the integration target as durable provenance/recovery history. No automatic archival or deletion policy is introduced by this scope. | MUST | User decision; ADR-BF-002 | accepted |
| REQ-BF-014 | Source workstream branch deletion MAY occur only after terminal durable state is independently recoverable from the integration target and existing terminal-safety rules are satisfied. | MUST | Existing workstream safety model; ADR-BF-002 | accepted |
| REQ-BF-015 | The branch-first invariant MUST apply to both `chatgpt_only` and `codex_only`. Lifecycle/routing mechanics MUST remain policy-local; only genuinely policy-neutral invariants may remain in `workflow/common/*`. | MUST | User decision; ADR-BF-003 | accepted |
| REQ-BF-016 | Bootstrap/adoption of Project Workflow into an existing repository with an integration target MUST obey the same branch-first rule: workflow/project state for the managed change is authored on the workstream branch, not directly on the target. | MUST | User decision; ADR-BF-001 | accepted |
| REQ-BF-017 | Recovery MUST remain possible without prior chat from the integration target plus the exact active workstream branch/manifest (or terminal target-side package after integration), authority artifacts and exact Git/PR evidence. | MUST | Existing durability invariant; ADR-BF-002 | accepted |

## Constraints

- Preserve policy-specific differences between `chatgpt_only` and `codex_only` review/execution orchestration.
- Preserve stacked-workstream semantics and target-refresh safety.
- Preserve existing terminal post-merge/source-branch-deletion recovery.
- Do not require a repository-global mutable workstream registry.
- Migration of old projects must be deterministic and fail closed rather than silently treating root legacy state as new-work state.

## Non-goals

- Removing historical legacy/default files solely for repository cleanliness.
- Rewriting completed historical evidence/handoffs.
- Requiring users to classify every new change as issue or feature.
- Creating a single shared cross-policy lifecycle implementation.
- Mandating GitHub repository branch-protection configuration as the only enforcement mechanism; Project Workflow itself must enforce PR-only integration regardless of hosting settings.
- Defining archival/garbage-collection of terminal workstream history.

## Global invariants

- Integration target = integrated project truth.
- Active managed-change state = exact branch-isolated workstream.
- No new managed-change mutation on the integration target.
- No new legacy/default state.
- Workstream identity is durable and branch-bound before managed-change writes.
- Policy namespaces do not import each other's lifecycle semantics.
- Terminal workstream history survives source-branch deletion.

## External contracts / dependencies

- Git branch/PR/merge semantics and immutable commit evidence.
- GitHub-hosted projects may optionally add branch protection/rulesets as defense in depth, but workflow correctness cannot depend on those settings.

## Data integrity / idempotency / security constraints

- Automatic generic intake must recover an existing exact workstream instead of creating duplicates when durable identity is available.
- Branch creation followed by failed state materialization must recover/abandon safely before mutation.
- Legacy migration must not overwrite unrelated root or workstream state.
- Target refresh must detect both textual and semantic conflict before final integration.
- Terminal source branch deletion must never precede durable target-side recovery proof.

## Acceptance-level requirements

Definition-level acceptance is met when the implemented workflow demonstrates all of the following:

1. A normal-language request such as “use Project Workflow to implement these changes” can start from read-only exploration and automatically create a branch-isolated workstream before the first durable change-specific write.
2. The same behavior exists under both `chatgpt_only` and `codex_only`.
3. `#issue` / `#feature` still work as optional shortcuts.
4. New work cannot fall back to root `implementation/TASK_BOARD.yaml`.
5. Active exploratory/Research routing no longer requires mutable workstream pointers in root `PROJECT.md`.
6. A trivial managed change still follows branch → PR → merge without forcing unnecessary full Planning when a bounded path is legal.
7. A substantial change can remain on one workstream branch from discovery through final integration.
8. After merge, the target contains the terminal workstream package and canonical root artifact changes; deleting the source branch does not lose recoverability.
9. Existing legacy/default projects can be recognized and migrated/recovered without treating legacy as a valid destination for new work.
10. Documentation/router/templates/tests consistently describe the new invariant and contain no active-path statement that presents legacy/default as a normal new-work choice.

## Definition completeness

- Target state and material MUST requirements are explicit.
- Constraints/non-goals/invariants are captured.
- Acceptance-level outcomes are sufficient for Planning.
- Strategic choices are recorded in ADR-BF-001 through ADR-BF-003.
- No unresolved user/product choice remains.

## Downstream coverage

Planning must map every REQ-BF requirement to implementation milestones/work packages and preserve separate policy-local changes for `chatgpt_only` and `codex_only`.
