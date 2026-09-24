# Decision — PWv2.1 preserves planner decomposition intent through JIT

- Decision ID: `ADR-PWV21-006`
- Date: `2026-09-24`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@2`
- Related requirements: `PWV21-REQ-115..121`

## Context

Terminal M02 evidence showed that approved Strategic Planning identified four independently falsifiable implementation surfaces, while Execution Prep legally collapsed them into one whole-milestone Card. That topology materially increased implementation and review surface.

The workflow still needs JIT refinement because exact Card identities and dependency-result bindings may be unknowable during Strategic Planning.

## Decision

- Strategic Planning may classify decomposition intent as:
  - `required_seam`: topology boundary whose preservation is part of accepted strategy/correctness;
  - `preferred_seam`: preserve by default but allow justified JIT deviation;
  - `illustrative`: non-binding implementation example.
- Planning does not need speculative future Card IDs to express seam intent.
- Execution Prep owns exact JIT Card materialization, dependency/result binding and additional technically justified splitting.
- Execution Prep cannot merge a `required_seam`; evidence that it is wrong returns to Strategic Planning.
- Merging/splitting a `preferred_seam` requires durable technical rationale grounded in real coupling/atomicity/acceptance/predecessor evidence. Convenience, same-milestone membership or fewer Cards are insufficient.
- Non-trivial decomposition is audited for independent implementability, falsifiability/testability, reviewability, invariant family, dependencies, atomic mutation/migration constraints and cross-surface coupling.
- Materially risky topology/deviation receives a fresh independent topology challenge before first launch.
- The topology challenge is narrow and does not duplicate full Plan Review.
- Card Review remains local; Milestone Review remains composition/integration focused. Execution Prep must not silently create a Card so broad that those review layers collapse into one.

## Consequences

The strongest planning work survives JIT refinement without forcing speculative Card authoring. Simple work remains lightweight, while materially risky mega-Card formation gains an explicit independent check.
