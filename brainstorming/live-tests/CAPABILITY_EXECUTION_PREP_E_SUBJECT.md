# Capability-first Execution Prep live-test subject E

Status: approved synthetic milestone authority

## Milestone M01 outcome

Prepare three bounded Cards.

### T01 — Alpha
- Dependencies: none
- Acceptance: exact synthetic output A exists
- No authorization blocker
- Scope is fully knowable now

### T02 — Beta
- Dependencies: none
- Acceptance: exact synthetic output B exists
- No authorization blocker
- Scope is fully knowable now

### T03 — Combine
- Dependencies: T01 and T02
- Acceptance: exact synthetic output C combines accepted results A and B
- No authorization blocker
- Card contract is knowable now, but execution prerequisites are not yet satisfied

## Invariants

- T01 and T02 are project-legally executable immediately.
- T03 is not executable until both T01 and T02 are done.
- No runtime/product capability is part of project readiness.
- This test concerns Execution Prep only. Do not execute any Card.
