# Shared Execution Core

This is the lean shared execution loop for ChatGPT and Codex.

The selected executor also reads:
- ChatGPT → `workflow/chatgpt/EXECUTION.md`;
- Codex → `workflow/codex/EXECUTION.md`.

Every executing agent reads `workflow/contracts/TASK_EXECUTION.md`.

Do **not** load `TASK_CARDS.md`, `GITHUB_STATE.md`, `OPENSPEC.md`, execution-prep, review/close, recovery, or the other executor's adapter unless the current state triggers them.

## State authority

`implementation/TASK_BOARD.yaml` is the sole mutable execution-state authority.

Stable authority comes from the current milestone contract, Task Card and its exact referenced requirements/accepted decisions/plan/OpenSpec/dependency results.

Progressive disclosure is **lossless by authority, selective by context**: less context is allowed; loss of an applicable implementation-shaping constraint is not.

## Core execution loop

1. Establish exact project repository, active/integration branch, HEAD and relevant runtime/external baseline.
2. Read project `PROJECT.md`, Task Board and current execution policy.
3. Recover any current `in_progress`/`blocked` obligation before selecting new work.
4. If REQUIRED/RECOMMENDED review is pending/in-progress, do not start later dependent implementation; route to the applicable review mechanism.
5. Resolve the current milestone contract and READY Task Card/set from Task Board.
6. Read each selected card plus its exact authority slice and only the source/runtime/evidence needed by that scope.
7. Apply `workflow/contracts/TASK_EXECUTION.md` readiness/start rules and persist the start transition before relying on it.
8. Run the card-level Refresh Gate.
9. If the card requires OpenSpec creation/reconciliation, load `workflow/contracts/OPENSPEC.md` just-in-time; otherwise do not load it.
10. Execute bounded scope.
11. Run required tests/checks and verify acceptance.
12. Perform required external readback/verification when material.
13. Apply Task Execution Definition of Done and persist exact result/test/evidence pointers.
14. Unblock deterministic dependents and continue while policy/state allows.
15. When a conditional boundary below is reached, load that boundary's owning module instead of carrying its rules in ordinary card execution.

A simple serial card should complete without loading advanced coordinator/planning/review modules.

## Executor selection

- `chatgpt_only` → ChatGPT is fixed executor; no Capability Gate.
- `codex_only` → Codex is fixed executor; no Capability Gate.
- `mixed` → use the already-performed ChatGPT Capability Gate assignment for the selected card/set.

Do not rerun Capability Gate merely because a runtime operation later fails. Execution policy changes only by explicit user decision.

## Runtime-operation rule

Project Workflow does not maintain or teach agents a catalog of their tools/capabilities.

Attempt concrete required operations using the runtime actually available. Under fixed policy, do not perform a separate capability inventory/preflight.

Executor-specific runtime remediation behavior belongs in the executor adapter/runtime. If a concrete required operation cannot proceed, persist a runtime blocker and request only the smallest user input/access/authorization actually needed.

## Authority-preserving execution

Before implementation, every applicable implementation-shaping constraint must either be present in the card/package or read from exact durable authority.

Actual code/runtime is an implementation input, not authority to silently rewrite requirements, accepted decisions or approved milestone outcome.

Implementation-detail reconciliation inside accepted contracts is allowed. Material change to accepted requirements, frozen architecture/decisions, global invariants, milestone outcome/behavior contract or explicit authorization boundary is a strategic blocker.

## External writes

For a material mutation of an external system, use meaningful readback when available:

```text
WRITE → READBACK → VERIFY EXPECTED STATE → EVIDENCE
```

Do not invent a readback where none meaningfully exists. Explicit deployment/live-write authorization remains a hard stop.

## Conditional execution modules

### Bounded parallel

Trigger: Task Board `execution_mode: bounded_parallel` or an active parallel lane/set.

Load:
- relevant parallel sections of `workflow/contracts/TASK_CARDS.md`;
- `workflow/contracts/GITHUB_STATE.md`;
- executor-specific orchestration rules.

Project-level coordinator owns shared Task Board/integration/review state. Lane workers own only bounded implementation/test/evidence scope. Exact project-level parallel semantics remain in the advanced contracts; they are not part of every serial execution context.

### JIT decomposition/refinement

Trigger: predecessor evidence makes deferred card/milestone detail knowable or current scope requires allowed L2 refinement.

Load:
- `workflow/EXECUTION_PREP.md`;
- `workflow/contracts/TASK_CARDS.md`;
- `GITHUB_STATE.md` only when mutable card-set/state structure must be reconciled;
- relevant OpenSpec only when required.

L2 refinement may change not-yet-started implementation decomposition but not L3 strategic authority.

### Independent review

Trigger: REQUIRED/RECOMMENDED review becomes due.

Load:
- `workflow/REVIEW_AND_HANDOFF.md`.

Freeze the subject/evidence first. The implementing worker/session never issues its own required/recommended independent verdict.

### Milestone acceptance / close / publication

Trigger: all required card/review gates needed for milestone acceptance are satisfied or close/publication reconciliation is due.

Load:
- `workflow/REVIEW_AND_HANDOFF.md`;
- `workflow/contracts/GITHUB_STATE.md`;
- only acceptance-relevant evidence/OpenSpec/external state.

### Strategic blocker

Trigger: evidence requires an authority decision beyond executor L1/L2 scope.

Persist exact blocker/evidence, stop affected dependent work and route to strategic authority. Load Codex handoff rules only for an actual Codex strategic escalation.

### Failure recovery

Trigger: interrupted/ambiguous in-flight execution.

Return to `workflow/CONTEXT_ROUTING.md#failure-recovery`, reconstruct durable state, then load the executor/obligation-specific route. Do not carry recovery machinery in every healthy execution session.

## Continuation

A routine GREEN card is not a user stop. Continue deterministic READY work when policy/state allows.

A GREEN milestone is also not automatically a user stop; milestone continuation rules are evaluated at the close/acceptance boundary using `workflow/REVIEW_AND_HANDOFF.md` and executor-specific rules.

Do not ask the user to select among equivalent deterministic runnable cards.
