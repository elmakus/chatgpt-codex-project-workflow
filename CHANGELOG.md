# CHANGELOG

## Unreleased — dual-executor architecture

### Execution routing

- Replaced the hard-coded `ChatGPT plans → Codex executes` model with `ChatGPT manages project → Capability Gate selects ChatGPT or Codex executor`.
- Added project-level `execution_policy: chatgpt_only | mixed`.
- Added a lightweight ChatGPT Capability Gate with three outcomes: `EXECUTE IN CHATGPT`, `HANDOFF TO CODEX`, or `BLOCKED`.
- Explicitly scoped Project Workflow to normal ChatGPT chat + Codex; ChatGPT Work is not used by this workflow.
- Made the execution core executor-neutral and added thin ChatGPT/Codex execution adapters.
- Added optional Task Card capability requirements for external, unusual or routing-significant work and executor provenance for active work.
- Added the shared external-write rule `WRITE → READBACK → VERIFY` when readback materially validates the resulting state.
- Added independent-review tiers: required for high-risk work, recommended for major architecture/refactors, optional for simple changes.
- Added an optional competing research-path pattern for A/B/Hybrid evaluation without making it a mandatory lifecycle stage.

### Progressive disclosure

- Codex no longer loads `CHATGPT.md` or ChatGPT-specific execution instructions.
- ChatGPT loads Codex handoff rules only when actually handing work to/from Codex.
- Moved the Codex runtime boundary contract under `workflow/codex/`.
- Removed the monolithic ChatGPT↔Codex responsibility contract whose old role split is no longer valid.

## v3.0.3

### Execution-prep handoff UX

- ChatGPT execution prep must now finish with an explicit `EXECUTION PREP COMPLETE:` handoff instead of leaving the user to infer how to start Codex.
- Every completed prep must include `CODEX SESSION RECOMMENDATION: FRESH` or `CODEX SESSION RECOMMENDATION: CONTINUE EXISTING`, a short reason, a copy-paste-ready `CODEX START PROMPT:`, and the smallest concrete `USER ACTION:`.
- `FRESH` is the default at a clean new-milestone boundary after a GREEN checkpoint; `CONTINUE EXISTING` is preferred when prep extends the same active milestone and the existing Codex context remains useful and current.
- A fresh-session recommendation is explicitly context-hygiene guidance, not a product decision or authorization gate.
- Added a reusable execution-prep start-prompt template that points Codex to durable repository routers/kickoffs and preserves automatic deterministic Task Card progression.

## v3.0.2

### Explicit continuation status

- Codex user-visible execution checkpoints must now state unambiguously whether execution is continuing automatically, user action is required, a fresh session is only recommended, or the milestone is complete.
- A routine GREEN Task Card no longer permits a neutral status-only ending that can be mistaken for a request to intervene; deterministic READY-card progression remains automatic.
- Added standard markers: `NEXT ACTION:`, `USER ACTION REQUIRED:`, `SESSION HANDOFF RECOMMENDED:` and `MILESTONE COMPLETE:`.

## v3.0.1

### Authority boundary

- Clarified Project Workflow versus `codex_workflow` authority domains.
- Project Workflow owns lifecycle/state/evidence/acceptance; installed `codex_workflow` owns internal Codex runtime orchestration.

## v3

v3 established one-project-one-repository, progressive disclosure, durable Task Card/GitHub state, JIT OpenSpec, Refresh Gate, milestone acceptance and cumulative handoffs.

## v2.1

Historical execution-state baseline retained by v3.

## v2

Historical ChatGPT↔Codex strategic communication baseline.
