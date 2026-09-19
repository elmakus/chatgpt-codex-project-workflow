# Codex-only Context Health

> M02 contract. This namespace is not selected by root routing before M04.

## Ownership

This module protects the coordinating Codex Main project context from stale Project Workflow state carryover. It does not own runtime worker/session lifecycle.

## Safe-boundary rule

Evaluate project-context health only after the current durable project role/obligation is reconciled and the exact next obligation is recoverable from repository state.

Do not interrupt:

- active project-state transition;
- in-flight production mutation;
- incomplete external write/readback;
- active formal verdict persistence;
- unresolved partial-state recovery.

No fixed token, turn, Card or milestone count forces a project-context handoff.

## Runtime separation

Executor/Tester/Investigator worker creation, waiting, resume, loss and replacement are `codex_workflow` concerns.

A worker reset/replacement:

- is not a Project Workflow context-health event;
- does not change review subject/attempt;
- does not change implementation-owner role;
- does not require a fresh Project Workflow session when durable project state remains coherent.

Conversely, restarting the coordinating Codex Main context is safe only when repository-backed project state is sufficient to recover the exact next obligation without transcript state.

## Invariants

Context hygiene never changes accepted authority, review verdict/state, execution policy or user/deployment authorization gates.

If another real stop already owns the boundary, use that boundary rather than inventing a separate hygiene stop.

M04 reconciles final user-facing/session-continuation behavior with the complete codex_only lifecycle before root activation.
