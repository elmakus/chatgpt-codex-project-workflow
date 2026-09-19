# Change: codex_only M02 formal review state and recovery

## Why

M01 established the dedicated `workflow/codex_only/` ownership surface but deliberately deferred exact formal-review provenance/state/recovery mechanics. M02 must make the Project Workflow state machine recoverable without owning `codex_workflow` worker/session mechanics.

## Authority

- `requirements/CODEX_ONLY_POLICY.md` — CO-REQ-007..016, CO-REQ-024..025
- `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
- `planning/CODEX_ONLY_MASTER_PLAN.md#M02--projectruntime-boundary-formal-independent-review-state-and-recovery`
- `implementation/workstreams/feature-codex-only-policy/cards/M02-T01.md`
- M01 GREEN checkpoint `8ded26f50275ab04e35a07438ca1abd2836901c2`

## Proposed change

Define a project-level review-attempt model with semantic implementation/reviewer roles, immutable exact subjects, durable attempt history and deterministic RED/repair/recheck recovery. Codex Main remains the only shared Project Workflow state writer. Runtime worker/session/model/profile/invocation/resume/replacement identities remain exclusively owned by `codex_workflow`.

## Non-goals

- no root routing cutover;
- no ChatGPT-only changes;
- no M03 bounded-parallel ready-set/lane/worktree schema;
- no runtime worker orchestration implementation;
- no second normal-ChatGPT review after a qualifying Codex-managed verdict.
