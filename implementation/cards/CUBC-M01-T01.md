# CUBC-M01-T01 — Terminal-unmerged Codex-only branch cleanup contracts

- Milestone: `CUBC-P1:M01`

> This file is a stable Task Card contract. Mutable execution/review/result state lives only in `implementation/TASK_BOARD.yaml`.

## Authority slice

- Master Plan / milestone contract: `planning/CODEX_ONLY_UNMERGED_BRANCH_CLEANUP_MASTER_PLAN.md#M01--terminal-unmerged-closure-and-branch-deletion`
- Requirements: `requirements/CODEX_ONLY_UNMERGED_BRANCH_CLEANUP.md` — CUBC-REQ-001 through CUBC-REQ-008
- Accepted decisions: `decisions/ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE.md`
- Relevant OpenSpec: none
- Accepted dependency results: current `main` Codex-only WORKSTREAMS/CLOSE/RECOVERY/ROUTER/REPOSITORY contracts

### Must preserve

- Scope is only branch-isolated `codex_only` workstreams intentionally terminal without final integration/merge.
- Merged workstreams remain repository-auto-delete only; do not add a Codex-only fallback lifecycle.
- Reuse existing terminal-safety and stacked-dependency gates; no live Card, Research, review, dependency or integration obligation may still require the branch.
- Durable terminal-unmerged closure/history must exist independently of the source branch before deletion, without merging rejected/superseded implementation content.
- Codex Main alone owns deletion of the exact `WORKSTREAM.yaml.branch` ref through authenticated `gh`.
- Recovery is idempotent: terminal-unmerged + branch exists → delete; terminal-unmerged + branch absent → complete.
- No `branch_cleanup`, `safe_to_delete`, cleanup registry, branch-prefix heuristic, alias ref, CAS/lease protocol, or runtime worker/session identity may be introduced for this Codex-only feature.

### Must not / rationale that must travel

Do not import ChatGPT-only fallback cleanup semantics into `codex_only`. The accepted Definition deliberately uses existing terminal state plus exact GitHub branch existence as complete cleanup authority.

## Dependencies

- none

## Outcome

Current Codex-only lifecycle contracts explicitly close, delete and recover terminal-unmerged workstream branches according to CUBC-R1, while preserving merged-path behavior and all existing safety/ownership boundaries.

## Scope

### Included

- `workflow/codex_only/WORKSTREAMS.md`
- `workflow/codex_only/CLOSE.md`
- `workflow/codex_only/RECOVERY.md`
- `workflow/codex_only/ROUTER.md` only if routing needs an explicit unfinished terminal-unmerged cleanup obligation
- `workflow/codex_only/REPOSITORY.md` only where terminal-history/recovery wording requires it
- bounded regression/coherence evidence

### Excluded

- `chatgpt_only` behavior
- WORKSTREAM schema changes adding cleanup state
- merged-branch fallback deletion
- historical bulk cleanup
- permission escalation/degraded-permission design
- runtime worker/session orchestration

## Acceptance

- CUBC-REQ-001..008 are represented without Definition drift.
- Intentional terminal-unmerged closure persists the recovery/history package independently of the source ref before deletion.
- Exact deletion target is manifest `branch`; no heuristic target selection exists.
- Codex Main performs the lifecycle delete through authenticated `gh`.
- Recovery handles both surviving and already-absent exact branches idempotently and never recreates them.
- Existing stacked/dependency/live-obligation safety prevents premature deletion.
- Merged workstream cleanup remains repository-owned automatic behavior.
- No new cleanup lifecycle/state/registry or worker/session state is added.

## Required tests / checks

- Diff audit against CUBC-REQ-001..008 and ADR.
- Scenario audit: terminal superseded/unmerged + safe → durable closure then exact delete.
- Scenario audit: interruption after durable closure before delete → Recovery deletes surviving exact ref.
- Scenario audit: branch already absent → Recovery completes without recreation.
- Scenario audit: live stacked/dependency obligation → deletion forbidden.
- Regression audit: merged path has no new Codex-only fallback lifecycle.
- Schema/text audit: no `branch_cleanup` / `safe_to_delete` / cleanup registry introduced under `workflow/codex_only/`.
- Ownership audit: lifecycle action remains Codex Main-owned and runtime identity is not durable Project Workflow state.

## External write/readback needs

none beyond normal repository changes for this Task Card.

## Independent review

`REQUIRED` — the contract authorizes destructive source-branch deletion and therefore requires independent verification of safety, exact identity and recovery semantics.

## Contract overrides

none
