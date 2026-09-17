# ChatGPT ↔ Codex Project Workflow

A GitHub-backed workflow for technical projects managed from normal ChatGPT chat and/or Codex according to an explicit project execution policy.

> Scope: this workflow uses **normal ChatGPT chat + Codex only**. ChatGPT Work is not part of the architecture, routing model or required operating mode.

## Core model

**ONE PROJECT = ONE REPOSITORY from the first idea.**

The project repository is durable project truth. It stores brainstorming, research, accepted decisions, requirements, approved planning, implementation contracts/state, OpenSpec, evidence and cumulative handoffs. This workflow repository stores only workflow rules, contracts, templates and bootstrap prompts.

### State ownership

The workflow deliberately separates contract from state:

- `implementation/TASK_BOARD.yaml` — **sole mutable execution-state authority**, including active independent-review state;
- milestone/Card files — stable scope, acceptance and test contracts;
- cumulative handoff — summary of what became true at a completed milestone;
- root `PROJECT.md` — small high-level project router/policy/index, not a live tracker.

This avoids repeatedly synchronizing status, executor, SHA and result pointers across several documents.

### Execution policies

Every project chooses exactly one:

- `chatgpt_only` — ChatGPT is the fixed Task Card executor. No Capability Gate and no capability preflight. Start the work; if a concrete required operation cannot be performed, persist the runtime blocker and ask for the smallest remedy or an explicit policy change.
- `codex_only` — Codex is the fixed Task Card executor. No Capability Gate and no capability preflight. Codex starts directly, self-remediates ordinary installable non-secret tooling/dependencies when permitted, and asks the user only when a concrete operation requires unavailable user-provided MCP/credential/token/access/authorization.
- `mixed` — ChatGPT remains project router and uses the Capability Gate before new execution assignment to choose ChatGPT, Codex or BLOCKED.

Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`.

Changing policy requires an explicit user decision.

## Capability semantics

For fixed policies, capability availability is **runtime discovery**, not a recurring planning gate.

Execution Prep and Refresh Gate do not inventory tools/MCPs or attempt to prove that the fixed executor can perform every future operation. Refresh Gate checks current state, contracts, dependencies, interfaces, tests/evidence obligations and drift.

A capability becomes a blocker only when the active card reaches a concrete required operation that cannot proceed. No automatic executor/policy switch occurs. The user may provide the missing capability or explicitly change policy, after which Task Board is reconciled before reassignment.

## Independent review

Independent means independent from the worker/session that implemented the reviewed subject.

- `chatgpt_only` — a ChatGPT chat that implemented a REQUIRED/RECOMMENDED review subject must freeze exact `review_subject`, persist `review_state: pending`, and **stop**. The user opens a fresh normal ChatGPT chat, which performs the independent review from durable Task Board state. After GREEN, that fresh chat may continue later deterministic work.
- `codex_only` — Codex Main obtains an independent reviewer worker/session. When `codex_workflow` is installed/enabled, it owns the internal execute/review-worker orchestration. Project Workflow owns only the project-level review requirement, exact subject, durable verdict/evidence and acceptance boundary. No user handoff is required solely for review independence.
- `mixed` — reviewer path follows the accepted review contract and must remain independent from implementation.

Task Board records active review state using `review_state`, `review_subject` and `review_evidence`.

## Milestone continuity

Milestones remain stable integrated/testable checkpoints. They are **not** automatically human handoff points.

Under `chatgpt_only` or `codex_only`, the fixed executor may run an approved multi-milestone plan continuously:

`M01 → acceptance/review/checkpoint → M02 → ...`

Each boundary still performs required close/handoff, just-in-time execution prep and fresh state/contract Refresh Gate. Execution stops only for real strategic/product/architecture decisions, explicit deployment/live-write/user authorization gates, concrete runtime blockers that cannot be self-remediated, RED requiring strategic resolution, required `chatgpt_only` fresh-review handoff, or end of approved scope.

Under `mixed`, the next new execution assignment is routed again by Capability Gate.

No separate Campaign object or scheduler is required.

## Task execution

Task Cards are serial by default. A prepared milestone may opt into **bounded parallel** execution when multiple READY cards have completed dependencies, explicit `parallel_safe` ownership, non-overlapping mutable `write_scope` and no shared `exclusive_resources`.

Task Board plus ordinary Git lane branches/worktrees remain the durable coordination mechanism; there is no generic DAG/scheduler service.

## Roles

ChatGPT is the strategic/research/planning agent and user-facing router. It is also the fixed executor in `chatgpt_only` and a possible executor in `mixed`.

Codex is the fixed executor in `codex_only` and a possible executor in `mixed`. When `codex_workflow` is installed/enabled, it governs internal Codex runtime orchestration — including execute/review workers, worker/model routing, delegation, lifecycle, waiting and runtime recovery. Project Workflow retains project-level Task Card/state/review/acceptance authority.

## Progressive disclosure

Agents read the smallest applicable path:

- ChatGPT starts at `CHATGPT.md`, then project `PROJECT.md`, then shared phase modules and ChatGPT-specific modules only when needed.
- Codex starts at `prompts/CODEX_START.md`, then project `PROJECT.md`, then shared execution modules and Codex-specific modules. Codex does **not** load `CHATGPT.md` or ChatGPT-specific execution instructions.
- ChatGPT reads `workflow/codex/HANDOFF.md` only when preparing/interpreting a Codex handoff.

## Bootstrap prompts

- normal ChatGPT start: `prompts/CHATGPT_START.md`
- reusable ChatGPT Project Instructions: `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md`
- Codex execution start: `prompts/CODEX_START.md`

## Start an existing project

Use:

> Użyj mojego Project Workflow z `elmakus/chatgpt-codex-project-workflow`. Repo projektu: `elmakus/example-project`. Kontynuujemy <cel/faza>.

Current `main` is canonical Project Workflow authority except deliberately frozen in-flight migration boundaries documented by migration guidance.
