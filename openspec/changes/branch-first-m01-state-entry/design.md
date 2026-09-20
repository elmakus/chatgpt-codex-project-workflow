# Design — branch-first M01

Both fixed-policy manifests add `kind: change` and a workstream-local `routing` block with exact nullable locators for active exploratory scope, pre-execution Research and active plan review. These are locators only; pointed artifacts own lifecycle/status, Task Board owns Card/milestone state, and manifest review remains final-integration-review-only.

Clear natural-language authorization to implement/adopt repository state is a managed-change intake trigger; read-only exploration alone is not. Generic identity uses `change-<slug>` on `work/<slug>` with deterministic smallest-suffix collision handling. Existing exact identity is recovered; a deterministic branch with missing/inconsistent manifest fails closed into Recovery. The branch exists before any durable change-specific artifact.

Historical root/default state is recovery/migration input only. Common authority may state only the neutral branch-first/integration-target invariant; lifecycle mechanics remain policy-local. M02/M03 perform full lifecycle rewiring and M04 performs documentation/dogfood closure.
