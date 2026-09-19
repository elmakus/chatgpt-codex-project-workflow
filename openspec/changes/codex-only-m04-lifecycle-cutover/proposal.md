# Proposal — codex_only M04 lifecycle cutover

## Why

M01-M03 established the dedicated namespace, formal review/runtime boundary and bounded-parallel execution, but root routing still sends `codex_only` through legacy and several policy-local lifecycle modules remain foundation/deferred contracts.

## Change

Complete the dedicated `codex_only` lifecycle from Intake through Close, reconcile branch/default workstream semantics with M02/M03, and activate explicit root routing without changing `chatgpt_only` or other legacy policies.

## Non-goals

- no repository execution-policy change;
- no migration of other policies;
- no runtime worker/session schema in Project Workflow;
- no M05 final publication/integration closure.
