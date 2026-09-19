# Codex-only Intake

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **carry over**.

## Ownership

This module owns explicit `#issue` and `#feature` discovery for branch-isolated `codex_only` workstreams.

## Invariants

- Recover an existing matching workstream before creating a duplicate.
- Classify independent versus genuinely parent-dependent stacked work from durable evidence.
- Persist stable workstream identity, exact branch/base/target and intake record.
- A feature intake discovers scope but does not bypass the user-owned Brainstorming → Project Definition promotion gate.
- A bounded issue may qualify for the micro-fix path only under the accepted micro-fix criteria.
- No repository-global mutable workstream scheduler is introduced.
- Intake chooses project topology/state context; it does not encode runtime worker identities.

M04 reconciles complete intake-to-lifecycle routing before activation.
