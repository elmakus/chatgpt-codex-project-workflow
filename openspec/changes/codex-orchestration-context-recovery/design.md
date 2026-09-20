# Design — Codex orchestration context recovery

## Durable selection

The selected branch-first `codex_only` `WORKSTREAM.yaml` owns:

```yaml
orchestration:
  runtime_owner: null
  policy_ref: null
  contract_fingerprint: null
```

Only `runtime_owner` and `policy_ref` are required for a usable established binding. `contract_fingerprint` is optional and exists only for stale-contract detection.

This block is workstream-local routing/recovery metadata. It is not mirrored into root `PROJECT.md`, Task Board, Task Cards or a global registry.

## Non-durable current-context latch

Successful runtime re-bind conceptually establishes `current_context_binding_valid` for the current coordinator context only.

The latch is never serialized and carries no worker/session identifier. It must be treated as absent or uncertain whenever Main reconstructs from durable state, resumes after known context loss/compaction, or cannot positively establish that re-bind already occurred in the current context.

A matching durable fingerprint never establishes this latch.

## Reconstruction and dispatch

At a reconstruction/uncertainty boundary the bounded Project Workflow read set is:

1. project `PROJECT.md` for accepted execution policy;
2. selected branch-isolated `WORKSTREAM.yaml` for workstream identity/routing and orchestration binding;
3. `workflow/codex_only/ORCHESTRATION_KERNEL.md`;
4. only the exact canonical state record already required for the current obligation.

Before the first policy-dependent runtime realization/re-realization while the latch is absent/uncertain, Main asks the bound runtime owner to resolve/re-bind the opaque policy selection. Success establishes the non-durable latch.

The kernel is conditional; an already positively established current-context latch avoids repeated recovery loads in steady state.

## Failure and drift

- Missing/stale/contradictory/unresolvable established binding fails closed.
- When installed/enabled `codex_workflow` owns runtime orchestration, loss of transient routing context must not silently choose native/internal harness instead.
- A changed runtime contract fingerprint makes the durable binding stale and requires re-resolution plus durable refresh only after successful resolution.
- An unchanged fingerprint does not remove reconstruction re-bind.

## Ownership boundary

Project Workflow owns durable policy selection, binding/latch/re-bind gate, canonical project invariants and fail-closed continuation semantics.

The active runtime owns policy interpretation, concrete role→harness/model selection, worker/session lifecycle, resume/replacement and runtime-side enforcement.

## Schema evolution

A newly created Codex-only manifest may contain null orchestration fields only during initial materialization. Follow-on lifecycle wiring requires establishment before Intake completes and before policy-dependent runtime realization after the manifest exists.

A pre-schema branch-first manifest with no `orchestration` block is a distinct one-time Recovery migration case. A manifest where the block exists but required binding values are missing/unknown/contradictory is invalid and fails closed rather than being treated as legacy schema absence.
