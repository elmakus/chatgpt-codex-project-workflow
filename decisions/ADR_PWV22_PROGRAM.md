# ADR — PWv2.2 Program Definition R3

- Decision ID: `ADR-PWV22-PROGRAM-R3`
- Status: accepted Definition authority; supersedes the earlier predecessor-rebind/backward-compatibility assumption
- Source subject: `pwv22-program@19`

## Decisions

- PWv2.2 is a semantic workflow contract, not a runtime orchestration specification.
- ChatGPT and Pi/Paseo are required PWv2.2.0 hosts; Codex is non-blocking.
- Runtime/model/session/worker identity is never canonical workflow authority.
- Typed Execution Obligation / Result remain transport-neutral with JSON as the common portable interchange format.
- Exact Result identity is repository + commit + path + blob.
- Freshness is material-input-local.
- Canonical writes are guarded and read back.
- Review attempts are append-only and exact-subject-bound; deterministic finalization remains non-semantic.
- Premium A/B/C remain real stops; reviewer model quality is advisory, review independence is mandatory.
- PWv2.2.0 preserves accepted PWv2.1 bounded parallel-safe Card behavior.
- One Card has one mutating ownership domain; runtime worker topology remains runtime-local.
- Worker/subagent cleanup is an explicit runtime expectation, but shutdown/session/capacity mechanics are not canonical state.
- Review convergence ceilings from PWv2.1 remain part of workflow law.
- Falsification/test-first remains SHOULD rather than MUST.
- Simplification Review is mandatory inside Planning before freeze and introduces no new top-level stage.
- Context Compiler/shadow DAG/frontier are disposable projections only.
- Dedicated candidate storage is rejected; Git-native isolation/publication is allowed.
- External-effect uncertainty uses UNKNOWN + exact readback; blind retry is forbidden.
- Policy evolution uses minimal preserve/revalidate/stale/Recovery handling.
- PWv2.2 is a new native workflow contract, not a compatibility layer over PWv1/PWv2.0/PWv2.1 durable state.
- No backward-compatible legacy reader, old-state continuation guarantee, automatic workstream/schema migration, mixed-version mode or downgrade path is required.
- Intentional transfer of an old project into PWv2.2 is a separate owner-authorized reconstruction/adoption task that establishes fresh PWv2.2-native authority from current product facts and useful evidence; preserving old workflow-state semantics is not required.
- Definition completion does not depend on terminal PWv2.1 or a final PWv2.1 rebind.
- The direct pivot must still perform an anti-loss reconciliation so desired capabilities from the unstarted PWv2.1 M03-M07 scope are retained, superseded deliberately, deferred or explicitly rejected rather than disappearing accidentally.


## Execution preparation and hand-back decisions

- Strategic Planning must classify execution seams as `materialization_ready` or `jit_dependent`; JIT requires a real not-yet-durable dependency and is not the default deferral mechanism.
- Premium C remains the real stop before Execution Prep, but its PWv2.2 recommendation is to move to the best available strong reasoning context for the Initial Execution Prep pass rather than to a cheaper context.
- Initial Execution Prep is the one-time high-quality pass that validates Plan decomposition, eagerly materializes every currently knowable stable Card, and leaves only genuinely predecessor-dependent work behind bounded JIT triggers.
- PWv2.2 adds Premium D immediately after Initial Execution Prep and before first Execution. D is a user-facing hand-back gate so the owner can deliberately stay or return to a lighter/normal execution context before implementation begins.
- Premium D is not a new workflow stage and does not alter Plan or Card authority. Once its exact satisfaction is durably read back, normal Execution/Review auto-continuation resumes.
- Routine later JIT refinement stays in the normal execution context by default. A true strategy/outcome ambiguity routes back to Strategic Planning instead of being solved by silently escalating inside Execution Prep.
