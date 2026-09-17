# CHANGELOG

## Unreleased — policy-fixed execution and single live-state authority

### Execution state

- Made `implementation/TASK_BOARD.yaml` the sole authoritative mutable execution-state record.
- Milestone and Task Card files are now stable scope/acceptance/test contracts rather than status/result mirrors.
- `PROJECT.md` is now explicitly high-level project routing/policy only; current milestone/card/executor/branch/HEAD/checkpoint/OpenSpec/blocker state belongs in Task Board.
- Cumulative handoffs remain completed-milestone summaries, not live trackers.
- Removed the requirement to synchronize `execution_status`, executor and result pointers between Task Board and Task Card files.

### Execution routing

- Added third execution policy: `codex_only`.
- `chatgpt_only` and `codex_only` are fixed-executor modes and no longer run Capability Gate.
- Capability Gate is now explicitly `mixed`-only.
- Preserved routing invariant `ChatGPT capabilities ⊆ Codex capabilities`.
- Missing capability under fixed policy is a blocker for the fixed executor; policy never changes automatically.

### Multi-milestone continuation

- GREEN milestone boundaries are no longer automatic routing/user stops under fixed execution policy.
- ChatGPT under `chatgpt_only` and Codex Main under `codex_only` may continue automatically into the next already-approved milestone after normal close/handoff + just-in-time execution prep + fresh Refresh Gate.
- Explicit strategic/product/architecture decisions, user/deployment/live-write authorization gates, missing capability/evidence and end of approved scope remain hard stops.
- Under `mixed`, new execution assignments continue to route through Capability Gate.
- No separate Campaign or scheduler abstraction was added; approved Master Plan + Task Board + existing milestone gates are sufficient.

### Review

- Independent review is now defined by independence from implementing worker/session rather than hard-coded to normal ChatGPT.
- `chatgpt_only` uses fresh independent ChatGPT review when required/recommended; `codex_only` may use a distinct Codex reviewer/worker/session; `mixed` follows the accepted independent review contract.

## Previous Unreleased — dual-executor architecture

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
- Parallel project cards require completed dependencies, explicit `parallel_safe`, bounded non-overlapping `write_scope`, no shared `exclusive_resources`, isolated mutable lanes and coordinator-owned Task Board/integration state.
- Added project `parallel_card_limit` ceiling and deterministic compatible-ready-set selection without generic DAG engine/shadow scheduler.
- Codex Main may map compatible project Task Cards to isolated `codex_workflow` workers while remaining responsible for project-level lane state, integration, post-integration verification and card completion.

### Progressive disclosure

- Codex no longer loads `CHATGPT.md` or ChatGPT-specific execution instructions.
- ChatGPT loads Codex handoff rules only when actually handing work to/from Codex.
- Moved Codex runtime boundary contract under `workflow/codex/`.
- Removed monolithic ChatGPT↔Codex responsibility contract whose old role split is no longer valid.

### Migration

- Added safe transition rule for projects with execution already in progress under v3.0.3: finish/recover bounded in-flight work under frozen workflow revision and adopt `execution_policy` at next clean GREEN boundary.
- Added reusable short ChatGPT Project Instructions bootstrap.

## v3.0.3

### Execution-prep handoff UX

- ChatGPT execution prep must finish with explicit `EXECUTION PREP COMPLETE:` handoff instead of leaving user to infer how to start Codex.
- Every completed prep includes executor/session recommendation appropriate to routing result.
- Fresh-session recommendation is context-hygiene guidance, not product decision or authorization gate.

## v3.0.2

### Explicit continuation status

- User-visible execution checkpoints state unambiguously whether execution continues automatically, user action is required, fresh session is only recommended, or milestone is complete.
- Routine GREEN Task Card does not permit neutral status-only ending that can be mistaken for request to intervene.

## v3.0.1

### Authority boundary

- Clarified Project Workflow authority for lifecycle/process/durable project state/Task Cards/selective JIT OpenSpec/acceptance/evidence/strategic escalation/cumulative handoffs.
- Clarified installed `codex_workflow` authority for internal Codex runtime orchestration.
- Preserved project-level delegation accountability and separated worker completion from Task Card completion.
- Added automatic SemVer patch tags for pushes to `main`; `main` remains canonical authority.

## v3

v3 reorganized v2.1 workflow around one-project-one-repository, progressive disclosure and durable GitHub-backed project truth while preserving execution safety semantics.
