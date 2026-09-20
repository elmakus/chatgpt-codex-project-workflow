# ADR — Codex-only uses continuous Main orchestration

Status: accepted
Date: 2026-09-20

## Context

The `codex_only` policy already assigns project-level coordination to Codex Main and runtime worker/session lifecycle to `codex_workflow`. Independent Tester review returns to Main without a user stop, and Close already defines automatic next-milestone continuation.

A policy-local Context Health Gate is inconsistent with that model because it can turn coordinator transcript hygiene into a project-workflow boundary even when all required authority and continuation state are durable and the next obligation is deterministic.

## Decision

Remove Context Health from the active `codex_only` lifecycle.

Codex Main continues through all deterministic authorized obligations and approved milestone boundaries until a genuine human/project stop occurs or approved scope ends.

Coordinator/session/runtime replacement is treated as runtime/recovery behavior reconstructed from durable repository state, not as a normal planned Project Workflow checkpoint.

The existing Brainstorming → Project Definition user-promotion gate remains a deliberate human-authority boundary.

## Consequences

- A single authorized `codex_only` run may execute many milestones end-to-end without asking the user to continue.
- Executor/Tester separation and RED repair loops remain internal to Main orchestration.
- `workflow/codex_only/CONTEXT_HEALTH.md` is no longer active policy authority and should be removed rather than kept as a dormant competing contract.
- Router language and tests must make the absence of a context-hygiene stop explicit.
- Recovery remains strict and durable; this decision does not authorize state reconstruction from chat narrative.
- `chatgpt_only` remains unchanged and may continue to use its own Context Health Gate.
