# M03 Cumulative Handoff

Workstream: `feature-codex-only-policy`
Milestone: `M03`
Status: **GREEN / done**
Checkpoint: `1fbb601461604fe07151478e017cb94bf60de47b`

## Achieved state

The dedicated `codex_only` namespace now has the accepted M03 bounded-parallel execution model: serial-by-default Cards, JIT-compatible finite batches, isolated lane mutation, Main-only shared-state ownership, deterministic result integration, exact review subjects and repository-first recovery.

All three independent-review defects found during M03 were repaired. The final exact subject `1fbb6014...` received GREEN in review attempt 04.

## Authority now in force

- Requirements: `requirements/CODEX_ONLY_POLICY.md`
- Plan: `planning/CODEX_ONLY_MASTER_PLAN.md`
- Decisions:
  - `decisions/ADR_CODEX_ONLY_DEDICATED_NAMESPACE.md`
  - `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
  - `decisions/ADR_CODEX_ONLY_BOUNDED_PARALLEL_CARDS.md`
- M03 OpenSpec: `openspec/changes/codex-only-m03-bounded-parallel-safety/`

## Evidence

- M03 acceptance: `implementation/workstreams/feature-codex-only-policy/evidence/M03-acceptance.md`
- M03 implementation: `implementation/workstreams/feature-codex-only-policy/evidence/M03-T01.md`
- Final independent review: `implementation/workstreams/feature-codex-only-policy/evidence/M03-T01-review-04.md`

## Continuation

Next approved milestone: `M04 — Full lifecycle integration, routing cutover and compatibility`.

Durable start pointer remains:
`implementation/workstreams/feature-codex-only-policy/TASK_BOARD.yaml`

M04 must use current `main` ChatGPT-only lifecycle authority as the compatibility reference, complete the codex_only lifecycle/cutover contract, preserve other policy routing, and keep this repository's own `execution_policy: chatgpt_only`.
