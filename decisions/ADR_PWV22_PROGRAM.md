# ADR — PWv2.2 Program Definition R2

- Decision ID: `ADR-PWV22-PROGRAM-R2`
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
