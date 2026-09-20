# Change: Codex orchestration context recovery

## Why

A Codex Main coordinator can recover the exact Project Workflow obligation after context compaction while losing the transient fact that the selected runtime policy must still govern the next worker dispatch. The primary failure occurs even when the external runtime version has not changed.

Project Workflow therefore needs a compact durable policy selection plus a deliberately non-durable current-context readiness rule. It must not absorb concrete `codex_workflow` role/model/harness or worker-session mechanics.

## Authority

- `requirements/CODEX_ORCHESTRATION_CONTEXT_RECOVERY.md` R2 — CCOR-R1…R10
- `decisions/ADR_CODEX_ORCHESTRATION_POLICY_BINDING.md`
- `planning/CODEX_ORCHESTRATION_CONTEXT_RECOVERY_MASTER_PLAN.md@CCOR-P2`
- `implementation/workstreams/issue-codex-compaction-routing-recovery/cards/M01-T01.md`

## Proposed change

Define a branch-isolated manifest `orchestration` binding containing only an opaque runtime owner, opaque selected policy/profile reference and optional contract fingerprint. Add one small Codex-only orchestration kernel that makes current-context readiness non-durable, requires re-bind after reconstruction/uncertainty before policy-dependent worker realization, and fails closed when the binding cannot be established.

Follow-on Cards wire deterministic binding establishment/migration and every runtime realization path through the generic kernel boundary, then add focused regressions/documentation.

## Non-goals

- no concrete role→harness/model map in Project Workflow;
- no worker/session/process/model-instance/invocation/resume/worktree identity in project state;
- no durable current-context latch;
- no repository-global orchestration registry;
- no `chatgpt_only` behavior change;
- no runtime-side `codex_workflow` enforcement implementation.
