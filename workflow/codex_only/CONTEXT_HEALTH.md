# Codex-only Context Health

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Ownership

This module protects the coordinating Codex Main context from stale project-state carryover without becoming a worker-runtime lifecycle manager.

## Invariants

- Evaluate context health only at a safe durable project boundary.
- No fixed token, turn, Card or milestone count forces a handoff.
- Durable repository state must be sufficient to reconstruct the next project obligation.
- Context hygiene never changes accepted authority, review state, execution policy or authorization gates.
- Worker creation, waiting, resume and replacement remain `codex_workflow` runtime concerns.
- A runtime worker reset is not itself a Project Workflow state transition.

M02 refines recovery boundaries and M04 reconciles the complete policy-router continuation behavior.
