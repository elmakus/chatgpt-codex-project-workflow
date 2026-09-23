# Decision — PW owns typed obligation/result authority; OR/Paseo owns runtime realization

- Decision ID: `ADR-PWV21-002`
- Date: `2026-09-23`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@1`
- Related requirements: `requirements/PWV21_POLICY_KERNEL.md`

## Context

PWv2.1 must let ChatGPT or OR/Paseo realize the same legal work without making orchestration-runtime a second authority source.

## Decision

- PW derives a disposable typed `Execution Obligation` containing exact role/subject, applicable authority bundle, prerequisites, constraints and completion/evidence contract.
- PW alone determines which authority applies and validates exact refs/hashes.
- OR/Paseo transports and realizes that package but does not add/drop/reinterpret PW authority.
- OR returns a typed semantic `Execution Result`; runtime telemetry remains non-canonical.
- Obligation identity and freshness are deterministic and bound to only the canonical inputs that materially determined the obligation.
- PW revalidates result freshness before acceptance.
- The kernel provides mutation pre/postconditions; the governed coordinator/role performs canonical writes and mandatory readback.
- OR/Paseo does not directly finalize canonical PW state.
- Worker/reviewer model assignment remains fixed by OR configuration with no silent substitution; exceptional stronger/different model use requires explicit user approval.

## Consequences

PW remains governance/authority; OR/Paseo remains execution infrastructure. Runtime loss or provider/session replacement cannot change Project Workflow semantics.
