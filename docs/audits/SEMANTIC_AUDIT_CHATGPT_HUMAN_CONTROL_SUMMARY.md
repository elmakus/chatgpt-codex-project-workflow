# Semantic Audit — ChatGPT Human Control Summary

Date: 2026-09-18
Base: `main@e19779d19ab1ec63b2a69c77900f281f3b333347`
Audited branch: `docs/chatgpt-human-control-summary`
Verdict: **GREEN**

## Scope

Audit the new user-facing UX rule for normal ChatGPT while preserving full technical detail in durable state and agent-to-agent execution communication.

## GREEN — ChatGPT-only presentation change

Changed normative execution adapter:
- `workflow/chatgpt/EXECUTION.md`

No `workflow/codex/*` file changed.
No worker/reviewer orchestration contract changed.
No Task Board/evidence/review semantics changed.

## GREEN — human-facing default

Normal ChatGPT status now defaults to:
1. what happened / what errors were found;
2. what it means;
3. what happens next / smallest user action;
4. ready-to-copy fresh-chat prompt when applicable.

Internal workflow jargon is minimized when plain language conveys the same meaning.

## GREEN — telemetry remains durable

Hidden from default user-facing response:
- commit/review SHAs;
- blob/tree IDs;
- branch/HEAD pointers;
- internal evidence paths;
- raw Task Board fields;
- long test inventories/exact counts;
- changed-file lists;
- OpenSpec/internal orchestration bookkeeping.

These facts remain persisted and available to agents/recovery/review.

## GREEN — technical details remain available when needed

Exact identifiers/details are still shown when:
- user explicitly asks;
- user must copy/use the exact value;
- a blocker/ambiguity cannot be explained safely without it;
- debugging/security/recovery materially requires it.

## GREEN — Codex/agent communication untouched

This change does not constrain:
- Codex Main ↔ worker packages;
- reviewer packages;
- internal evidence transfer;
- authority slices;
- technical provenance required for execution/recovery.

## Final assessment

**GREEN.** The workflow now separates machine-grade durable/agent detail from a simple human control summary in normal ChatGPT without losing technical evidence.
