# OpenSpec Contract

OpenSpec formalizes behavior/technical contracts only when freezing them reduces ambiguity or risk. It does not replace requirements, Master Plan, Task Cards, Task Board or handoffs.

## Selective policy

Normally justified for new/changed behavior, APIs, persistent state/schema, retry/idempotency/reconciliation semantics, migrations, security-sensitive behavior, cross-package architecture, external side effects or complex multi-card changes.

Normally skip simple unambiguous bug fixes, docs-only work, pure research, mechanical CI fixes and small mechanical refactors without behavior change.

## Candidate versus actual change

Planning may mark an OpenSpec candidate. Do not create distant specs merely "for later".

The **current executor** creates/reconciles actual OpenSpec just-in-time before implementation when required.

## JIT inputs

Reconcile against current HEAD/runtime state, latest handoff, milestone/card, authoritative requirements/decisions, plan constraints and completed dependencies.

Actual code/runtime state informs implementation design but does not silently rewrite product requirements.

## Verification

Card verification includes applicable OpenSpec requirements. Completed changes leave OpenSpec consistent with implemented behavior and archival policy.

One OpenSpec change may span multiple cards; do not collapse work into an oversized card merely because there is one spec.
