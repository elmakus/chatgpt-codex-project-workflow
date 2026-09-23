# Decision — Runtime handoff, recovery and PWv2 migration are Git-first and fail-closed

- Decision ID: `ADR-PWV21-005`
- Date: `2026-09-23`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@1`
- Related requirements: `requirements/PWV21_POLICY_KERNEL.md`

## Context

PWv2.1 must survive runtime/session loss, user-directed switching between ChatGPT and OR/Paseo, stale results and gradual adoption by existing PWv2 projects without creating another migration/state authority.

## Decision

- Runtime choice is user-directed and never canonical PW preference.
- One locator-only handoff format works across ChatGPT and OR/Paseo.
- Handoffs prefer durable boundaries; current Git state always outranks stale prompt narrative.
- OR/Paseo outage/session loss must not prevent recovery when canonical state permits direct ChatGPT continuation.
- Existing PWv2 workstreams migrate lazily/on-entry at natural durable boundaries when unambiguous.
- Historical GREEN remains valid when exact evidence still proves it; newly material evidence needs bounded revalidation, not retroactive RED.
- Migration preserves history and minimally normalizes uniquely derivable fields/results.
- Ambiguous legacy bindings, unknown external effects and kernel/docs/helper disagreement fail closed to Recovery.
- Recovery reuses safe existing results before replay and blocks only dependent paths where possible.
- Automatic deterministic continuation proceeds until a real user-owned stop.

## Consequences

Projects can switch runtimes repeatedly without transferring private runtime state, and PWv2.1 adoption does not require a flag-day rewrite of every historical project.
