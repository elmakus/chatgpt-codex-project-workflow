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
- Added optional `bounded_parallel` Task Card execution while preserving serial as the default.
- Parallel project cards now require completed dependencies, explicit `parallel_safe`, bounded non-overlapping `write_scope`, no shared `exclusive_resources`, isolated mutable lanes and coordinator-owned Task Board/integration state.
- Added a project `parallel_card_limit` ceiling and deterministic compatible-ready-set selection without introducing a generic DAG engine or shadow scheduler.
- Codex Main may map compatible project Task Cards to isolated `codex_workflow` workers while remaining responsible for project-level lane state, integration, post-integration verification and card completion.

### Progressive disclosure

- Codex no longer loads `CHATGPT.md` or ChatGPT-specific execution instructions.
- ChatGPT loads Codex handoff rules only when actually handing work to/from Codex.
- Moved the Codex runtime boundary contract under `workflow/codex/`.
- Removed the monolithic ChatGPT↔Codex responsibility contract whose old role split is no longer valid.

### Migration

- Added a safe transition rule for projects with execution already in progress under v3.0.3: finish/recover bounded in-flight work under its frozen workflow revision and adopt `execution_policy` at the next clean GREEN boundary.
- Added a reusable short ChatGPT Project Instructions bootstrap.

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
- Fresh-session recommendations must distinguish context hygiene/recovery from real product or authorization gates and include a durable continuation pointer.

## v3.0.1

### Authority boundary

- Clarified that `elmakus/chatgpt-codex-project-workflow` is authoritative for project lifecycle/process, durable project state, Task Cards, selective JIT OpenSpec, acceptance/evidence, strategic escalation and cumulative handoffs.
- Clarified that, when the owner's `codex_workflow` is installed and enabled, its installed instructions are authoritative for internal Codex runtime orchestration such as worker roles/models, Companion lifecycle, delegation mechanics, wait/event/message behavior, polling/silence and worker-runtime recovery.
- Replaced the duplicated runtime-orchestration rules in `workflow/contracts/CODEX_ORCHESTRATION.md` with a thin integration/boundary contract.
- Preserved project-level delegation accountability: worker completion is not Task Card completion, Main still owns integration/acceptance/evidence, and workers cannot independently rewrite strategic/product authority.
- Project Workflow no longer needs to read or reproduce the remote `elmakus/codex_workflow` repository during ordinary project work.

### Version snapshots

- Added a persistent GitHub Actions workflow that automatically creates the next annotated SemVer patch tag for each push to `main`.
- `main` remains canonical authority; tags are immutable historical snapshots.
- Major/minor version changes remain explicit; automatic tagging increments only the patch component from the highest existing SemVer tag.

## v3

v3 reorganizes the v2.1 workflow without intentionally losing its execution semantics.

### Project truth and repository model

- A project repository now exists from the first brainstorming session.
- **ONE PROJECT = ONE REPOSITORY** is the default from idea through implementation and handoff.
- The workflow repository stores workflow only; there are no central project workspaces.
- Project knowledge is explicitly separated into brainstorming, decisions, research, requirements, planning, implementation, project handoffs and OpenSpec.
- Root `PROJECT.md` is the small project context router and authority index.
- A split-repository project is an exception requiring technical justification and an explicit user decision; legacy topology changes still occur only at a green milestone boundary.

### Context and authority

- Added phase-aware progressive context routing.
- `CHATGPT.md` is a small global router rather than a copy of the complete workflow.
