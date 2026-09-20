# Orchestration recovery specification

## Manifest-owned binding

A branch-first `codex_only` workstream SHALL own one `orchestration` block with exactly these policy-binding fields:

```yaml
orchestration:
  runtime_owner: <opaque-owner-or-null>
  policy_ref: <opaque-policy-profile-ref-or-null>
  contract_fingerprint: <opaque-runtime-contract-fingerprint-or-null>
```

The binding SHALL NOT contain worker/session/process/model-instance/invocation/lease/resume/worktree identifiers or concrete role→harness/model mappings.

The binding SHALL NOT be mirrored into root `PROJECT.md`, Task Board, Task Cards or a repository-global mutable registry.

## Binding validity and establishment

A usable established binding requires non-null/non-empty `runtime_owner` and `policy_ref`. The fingerprint MAY be null when the runtime exposes no stable contract identifier.

A newly materialized manifest MAY temporarily contain null fields only while its initial Intake/materialization transition is incomplete. Before Intake completes, and before any policy-dependent worker realization after the manifest exists, Main SHALL ask the runtime owner to resolve the selected opaque policy and persist a usable binding.

A selected pre-schema branch-first manifest with no `orchestration` block SHALL use the bounded Recovery schema-upgrade transition. An existing block with missing/unknown/contradictory required values SHALL fail closed and SHALL NOT be treated as the legacy absence case.

## Current-context latch

Successful re-bind SHALL establish a conceptual `current_context_binding_valid` latch only in the current coordinator context.

The latch SHALL NOT be persisted. Durable binding data or a matching fingerprint SHALL NOT be accepted as proof of current-context readiness.

After known context compaction/loss/reconstruction, coordinator replacement, repository-only recovery, or uncertainty about whether current-context re-bind occurred, the latch SHALL be treated as absent/uncertain.

## Bounded recovery kernel

When the latch is absent/uncertain, Project Workflow SHALL need only:

- root `PROJECT.md`;
- selected `WORKSTREAM.yaml`;
- `workflow/codex_only/ORCHESTRATION_KERNEL.md`;
- the exact canonical state record required by the current obligation.

Before any policy-dependent worker realization/re-realization, Main SHALL re-bind the durable policy through `runtime_owner`.

If re-bind cannot be proven, the operation SHALL fail closed to the normal concrete runtime blocker path and SHALL NOT silently change execution policy or select a different harness.

## Runtime contract drift

When `contract_fingerprint` is available and differs from the current runtime contract, the binding SHALL be stale. Main SHALL re-resolve the same selected opaque policy and SHALL refresh the durable binding only after successful resolution.

A matching fingerprint SHALL NOT bypass the current-context re-bind requirement after reconstruction.

## Canonical project invariants

The kernel SHALL point back to existing canonical owners for accepted execution policy, exact review subject/requirement, implementation/reviewer separation, workstream/Task Board ownership and deterministic real-stop routing. It SHALL NOT copy their mutable state.

## Runtime boundary

Project Workflow SHALL NOT interpret `policy_ref` into concrete roles/models/harnesses. The installed/enabled runtime remains authoritative for that interpretation and for concrete worker lifecycle/recovery.
