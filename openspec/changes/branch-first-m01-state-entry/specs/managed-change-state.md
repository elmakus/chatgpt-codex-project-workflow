# Specification — branch-first managed-change entry/state

## Branch-before-write
A fixed-policy route MUST distinguish read-only exploration from managed-change authorization. On clear authorization it MUST create or recover the exact branch-isolated workstream before the first durable change-specific write. Read-only inspect/compare alone MUST NOT create a branch.

## Neutral identity
Both fixed-policy schemas MUST accept `kind: change`. New generic identity defaults to `change-<slug>` on `work/<slug>`, with deterministic smallest-suffix collision handling. `#issue` and `#feature` remain supported shortcuts.

## Workstream-local routing
Both fixed-policy manifests MUST expose the same locator schema:

```yaml
routing:
  exploratory_scope: null
  research_obligation: null
  plan_review: null
```

Each value is nullable. A non-null value MUST be an exact repository-relative path resolving on the exact selected workstream branch for ordinary pre-integration work. `exploratory_scope` points to the active exploratory/brainstorming record, `research_obligation` points only to pre-execution Research, and `plan_review` points to the active plan-review record.

These pointers are locators only. Pointed artifacts retain lifecycle/status and subject/result ownership. Implementation/recovery Research remains Task-Board-owned, Card/milestone state remains Task-Board-owned, and manifest `review` remains final-integration-review-only.

Before a locator is used, the policy-local workstream contract MUST validate expected artifact class plus selected workstream/authority subject. Missing, malformed, wrong-class, branch/workstream-mismatched, plan-subject-mismatched or contradictory stale locators MUST fail closed to Recovery rather than being guessed from another workstream, branch or global registry.

## Fail-closed recovery
A valid exact existing workstream is recovered, not duplicated. Partial branch/state creation MUST be completed/reconciled or blocked; it MUST NOT silently create a second workstream.

## Default-state boundary
For `chatgpt_only` and `codex_only`, root legacy/default state MAY be read for historical recovery/migration but MUST NOT be selected/scaffolded for a newly authorized managed change. Existing active default work migrates to an exact branch-isolated workstream before further managed-change mutation.

## Policy-local mechanics
Only the neutral invariant may live in common authority. Intake/Router/Workstreams/Recovery/Execution Prep mechanics remain separately implemented in each fixed-policy namespace.
