# ChatGPT-only Policy Split — Pre-Migration Semantic Inventory

Date: 2026-09-18
Base: `main@4476ed77b88adbed77702a193e447a0e520c5440`

## Goal

Create a physically isolated `workflow/chatgpt_only/` execution/review/state path so a project with `execution_policy: chatgpt_only` does not load policy branches, executor semantics or coordination machinery that cannot apply to normal ChatGPT execution.

This phase migrates **only chatgpt_only**. Existing mixed/codex paths remain untouched until separate migrations.

## Safe common candidates

The following semantics are executor-policy neutral and may live under `workflow/common/`:
- authority precedence and durable-source rules;
- brainstorming;
- research;
- selective OpenSpec policy.

Current `workflow/PLANNING.md` is not fully neutral because it contains execution-policy-specific continuation semantics, so chatgpt_only receives its own planning file in this phase.

Current `PROJECT_REPOSITORY.md` is not neutral because it defines all execution policies and executor-specific routing, so chatgpt_only receives a policy-clean repository contract.

## Current contaminated sources → new chatgpt_only owner

| Current source | ChatGPT-only semantics to preserve | New owner |
|---|---|---|
| `workflow/PLANNING.md` | strategic planning, milestones, L1/L2/L3, requirement coverage, JIT decomposition | `chatgpt_only/PLANNING.md` |
| `workflow/EXECUTION_PREP.md` | JIT cards, authority slices, acceptance/tests, review classification, serial readiness, continuation | `chatgpt_only/EXECUTION_PREP.md` |
| `workflow/contracts/TASK_CARDS.md` | stable bounded card contract, authority preservation, deferred card creation, scope discipline | `chatgpt_only/TASK_CARDS.md` |
| `workflow/contracts/TASK_EXECUTION.md` | readiness/start, Refresh Gate, runtime blocker, DoD, result pointers, review boundary | `chatgpt_only/EXECUTION.md` + `STATE.md` |
| `workflow/EXECUTION.md` | deterministic card loop, authority preservation, external readback, JIT/review/close triggers | `chatgpt_only/EXECUTION.md` |
| `workflow/chatgpt/EXECUTION.md` | ChatGPT runtime/session behavior, fresh-review stop, context hygiene | `chatgpt_only/EXECUTION.md` + `REVIEW.md` |
| `workflow/contracts/GITHUB_STATE.md` | Task Board ownership, serial card/milestone lifecycle, review fields, done state, blockers, corrective work, recovery | `chatgpt_only/STATE.md` |
| `workflow/REVIEW_AND_HANDOFF.md` | fresh independent review, RED auto-remediation, milestone acceptance/publication, handoff | `chatgpt_only/REVIEW.md` + `CLOSE.md` |
| `workflow/contracts/PROJECT_REPOSITORY.md` | project layout, authority ownership, branch policy, durable recovery | `chatgpt_only/REPOSITORY.md` |

## Explicitly excluded from chatgpt_only

The new path does not carry:
- executor selection/routing between alternatives;
- pre-assignment capability routing;
- project-level concurrent card/lane scheduling;
- lane/worktree ownership;
- alternate-executor handoffs;
- alternate-executor reviewer/session mechanics;
- policy comparison/invariants between executors.

Normal ChatGPT executes **one READY project Task Card at a time**.

## Migration gates

1. Create new common + chatgpt_only files while legacy files remain authoritative.
2. Static audit: no policy-crossing/executor-crossing semantics in `chatgpt_only/`.
3. Semantic coverage audit: every chatgpt_only behavior from current authority maps to a new owner.
4. Only then update `CHATGPT.md` so `execution_policy: chatgpt_only` routes to `workflow/chatgpt_only/ROUTER.md`.
5. Validate live route and fresh-review behavior after router switch.
6. Do not delete legacy shared files while mixed/codex paths still depend on them.
