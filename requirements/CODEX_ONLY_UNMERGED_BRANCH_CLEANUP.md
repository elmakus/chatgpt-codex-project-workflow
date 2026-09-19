# Codex-only Terminal Unmerged Branch Cleanup Requirements

Revision: `CUBC-R1`
Status: `approved`
Updated: `2026-09-20`
Scope ID: `codex-only-unmerged-branch-cleanup`
Execution policy affected: `codex_only`

## Goal / target state

Automatically remove the source branch of a branch-isolated Codex-only workstream when that workstream intentionally reaches a terminal state without final integration/merge.

Merged workstreams are outside this feature. Repository-level automatic deletion of merged branches is the normal merged path.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| CUBC-REQ-001 | When a branch-isolated Codex-only workstream reaches an intentional terminal state without final integration/merge, Codex Main MUST delete the exact source branch named by the workstream manifest after the existing terminal-safety conditions are satisfied. | MUST | user / ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE | accepted |
| CUBC-REQ-002 | Existing terminal-safety conditions remain authoritative: no live Card, Research, review, stacked-dependency, integration or other workstream obligation may still require the source branch, and required recovery/history must already be durable independently of that branch. | MUST | existing Codex-only lifecycle | accepted |
| CUBC-REQ-003 | The deletion operation MUST use the exact manifest-owned branch identity and MUST NOT infer cleanup targets from branch prefixes, naming heuristics or PR closure alone. | MUST | safety invariant | accepted |
| CUBC-REQ-004 | In the supported Codex environment, Codex Main performs the branch deletion through authenticated `gh` access with repository permissions sufficient for normal branch deletion. | MUST | explicit user environment contract | accepted |
| CUBC-REQ-005 | Recovery MUST be idempotent: if terminal-unmerged state is durable and the exact source branch still exists, Recovery deletes it; if that branch is already absent, cleanup is complete. | MUST | user / ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE | accepted |
| CUBC-REQ-006 | Codex-only MUST NOT add a separate `branch_cleanup`, `safe_to_delete` or equivalent cleanup lifecycle solely for this behavior. Terminal workstream state plus exact GitHub branch existence is sufficient recovery authority. | MUST | explicit user choice / ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE | accepted |
| CUBC-REQ-007 | Merged-workstream cleanup MUST NOT gain an additional Codex-only fallback path in this feature. Repository-level automatic deletion after merge remains the normal behavior. | MUST | explicit user choice | accepted |
| CUBC-REQ-008 | Branch cleanup is a Codex Main workstream-lifecycle responsibility, not an Executor/Tester Task Card and not durable runtime-worker/session state. | MUST | existing Codex-only ownership boundary | accepted |

## Constraints

- All current project repositories have automatic deletion of merged branches enabled, and future repositories are expected to receive that repository setting by default.
- The supported Codex environment provides authenticated `gh` access with permissions to perform normal repository branch deletion.
- Existing Codex-only terminal-safety, durable-recovery, stacked-workstream and Project Workflow ↔ `codex_workflow` ownership boundaries remain in force.

## Non-goals

- adding cleanup tracking for normal merged workstreams;
- adding `branch_cleanup`, `safe_to_delete`, CAS/lease state or a cleanup registry;
- designing permission-escalation or degraded-permission behavior;
- bulk-cleaning historical branches;
- changing `chatgpt_only` cleanup semantics;
- moving branch-cleanup authority into Executor/Tester workers or `codex_workflow` runtime state.

## Global invariants

1. A branch may be deleted only after the owning workstream is intentionally terminal without integration and no live obligation requires that branch.
2. The exact workstream manifest branch is the only cleanup target.
3. Recovery never needs a separate cleanup state: terminal-unmerged state plus branch existence is enough.
4. Merged branch cleanup remains repository-owned automatic behavior.
5. Runtime worker/session identity is never required to recover or complete cleanup.

## External contracts / dependencies

- GitHub repository automatic deletion of merged branches for the normal merged path.
- Authenticated `gh` access in the supported Codex environment for terminal-unmerged branch deletion.

## Data integrity / idempotency / security constraints

- Re-running Recovery after successful deletion is a no-op because absence of the exact branch is terminal cleanup success.
- An interrupted delete attempt must not create substitute refs or cleanup-marker branches.
- Cleanup must never target a branch other than the exact manifest-owned source branch.

## Acceptance-level requirements

The feature is Definition-complete only if Planning can organize work that proves all of the following:

1. A terminal `superseded`/otherwise intentionally closed unmerged Codex-only workstream with no live obligations causes Codex Main to delete its exact source branch.
2. If terminal state becomes durable and execution stops before deletion, Recovery later deletes the still-existing exact branch.
3. If the exact branch is already absent, Recovery treats cleanup as complete and does not recreate it.
4. A normal merged workstream receives no new Codex-only cleanup state or fallback lifecycle.
5. No `branch_cleanup` field or cleanup registry is introduced for this feature.
6. Executor/Tester workers do not own this lifecycle action or its durable state.

## Definition completeness

- Target behavior is explicit.
- Existing terminal-safety gates are reused rather than redesigned.
- Merged cleanup is explicitly out of scope.
- Ownership is explicit: Codex Main performs the lifecycle action; runtime worker/session state remains outside Project Workflow.
- No unresolved user/product choice remains that can alter planning.

## Downstream coverage

Planning must map every `CUBC-REQ-*` requirement to the minimal Codex-only workflow-contract edits and regression evidence needed to prove the behavior.
