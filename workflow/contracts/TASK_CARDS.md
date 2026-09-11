# Task Card Contract

## Meaning

A Task Card is a bounded project work package, distinct from smaller OpenSpec implementation tasks.

## Core fields

Each card defines id/title/milestone, execution status, priority/complexity/phase, expected code locations, dependencies, outcome, included/excluded scope, constraints, acceptance, required tests/checks, relevant authority references, OpenSpec candidate/ref, Refresh Gate, blocker rule, Result and Definition of Done.

### Executor provenance

Use:

```yaml
executor: null | chatgpt | codex
```

Leave `null` while merely planned/ready unless an approved plan intentionally preassigns Codex. Set the actual executor when work starts. This supports recovery/provenance; it is not an executor score.

### Optional required capabilities

Use `required_capabilities` only when explicit capabilities materially improve routing/safety, especially external, unusual, high-risk or environment-specific tasks:

```yaml
required_capabilities:
  - liftosaur_write
  - liftosaur_readback
```

Do not require capability declarations for every banal repository operation. Ordinary capabilities may be inferred from scope, tests, acceptance and evidence.

## Readiness

A card is `ready` only when dependencies and authoritative inputs allow start, acceptance is executable and no known strategic/capability blocker prevents the required execution path.

## Refresh Gate

Before implementation compare branch/HEAD/current state, latest handoff, milestone/card, relevant requirements/decisions/plan/OpenSpec, dependencies, real interfaces and capability/test/evidence requirements.

Implementation-detail drift inside approved contracts may be reconciled by the current executor. Material strategic drift blocks execution.

## Definition of Done

A card is `done` only when included scope is complete, acceptance satisfied, required tests/checks executed, OpenSpec satisfied where applicable, no hidden blocker remains, result is durable, Task Board/card/result pointers agree, evidence identifies exact verification, material external side effects are reconciled/read back when required, and no unassigned TODO remains inside accepted scope.

## Dependencies and sizing

Explicit `depends_on` plus Task Board state are sufficient; do not build a generic DAG engine without a concrete need.

Near-term cards may be detailed. Distant cards stay functionally precise without freezing nonexistent interfaces and must run the Refresh Gate before execution.

## Scope discipline

The selected executor implements only bounded card scope unless a necessary adjacent change is clearly within the same acceptance contract, a new bounded card is created, or strategic authority explicitly changes the plan.
