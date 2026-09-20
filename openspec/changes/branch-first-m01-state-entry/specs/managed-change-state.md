# Specification — branch-first managed-change entry/state

## Branch-before-write
A fixed-policy route MUST distinguish read-only exploration from managed-change authorization. On clear authorization it MUST create or recover the exact branch-isolated workstream before the first durable change-specific write. Read-only inspect/compare alone MUST NOT create a branch.

## Neutral identity
Both fixed-policy schemas MUST accept `kind: change`. New generic identity defaults to `change-<slug>` on `work/<slug>`, with deterministic smallest-suffix collision handling. `#issue` and `#feature` remain supported shortcuts.

## Workstream-local routing
The manifest MUST be able to locate active exploratory scope, pre-execution Research, and active plan-review records without root PROJECT mutable pointers. These pointers are nullable locators only; pointed artifacts own lifecycle/status. Task Board and final-integration review ownership remain unchanged.

## Fail-closed recovery
A valid exact existing workstream is recovered, not duplicated. Partial branch/state creation MUST be completed/reconciled or blocked; it MUST NOT silently create a second workstream.

## Default-state boundary
For `chatgpt_only` and `codex_only`, root legacy/default state MAY be read for historical recovery/migration but MUST NOT be selected/scaffolded for a newly authorized managed change. Existing active default work migrates to an exact branch-isolated workstream before further managed-change mutation.

## Policy-local mechanics
Only the neutral invariant may live in common authority. Intake/Router/Workstreams/Recovery/Execution Prep mechanics remain separately implemented in each fixed-policy namespace.
