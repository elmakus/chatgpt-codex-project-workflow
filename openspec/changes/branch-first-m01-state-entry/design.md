# Design — branch-first M01

Both fixed-policy manifests add `kind: change` and an equivalent workstream-local `routing` block with three exact nullable repository-relative locators: `exploratory_scope`, `research_obligation`, and `plan_review`. These are locators only; pointed artifacts own lifecycle/status and subject/result data, Task Board owns Card/milestone plus implementation/recovery Research state, and manifest `review` remains final-integration-review-only. Non-null locators are validated on the exact selected workstream branch against the expected artifact/subject and fail closed to Recovery when missing, malformed, mismatched or contradictory.

Clear natural-language authorization to implement/adopt repository state is a managed-change intake trigger; read-only exploration alone is not. Generic identity uses `change-<slug>` on `work/<slug>` with deterministic smallest-suffix collision handling. Existing exact identity is recovered; a deterministic branch with missing/inconsistent manifest fails closed into Recovery. The branch exists before any durable change-specific artifact.

Historical root/default state is recovery/migration input only. Common authority may state only the neutral branch-first/integration-target invariant; lifecycle mechanics remain policy-local. M02/M03 perform full lifecycle rewiring and M04 performs documentation/dogfood closure.
