# Decision — PWv2.1 preserves planner decomposition intent through JIT

- Decision ID: `ADR-PWV21-006`
- Date: `2026-09-24`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@3`
- Related requirements: `PWV21-REQ-115..121`, `PWV21-REQ-128..130`

## Context

Terminal M02 evidence showed that approved Strategic Planning identified four independently falsifiable implementation surfaces, while Execution Prep legally collapsed them into one whole-milestone Card. That topology materially increased implementation and review surface.

The workflow still needs JIT refinement because exact Card identities and dependency-result bindings may be unknowable during Strategic Planning.

## Decision

- A Card is the smallest meaningful execution-and-review ownership unit that produces one coherent independently falsifiable outcome substantial enough to justify its own execution/result/review lifecycle.
- A split is presumptively required when a proposed Card contains multiple separable acceptance, contract, invariant or independently useful/consumable outcomes such that each can reach a valid independently verifiable state and GREEN on one remains valid/useful while another is RED.
- The split presumption is rebutted only by concrete atomicity, invalid intermediate state, materially inseparable acceptance or material coupling. File/module/layer/test/tool/step boundaries alone do not establish separate Cards.
- Setup, scaffolding, configuration and documentation normally remain with the meaningful outcome that needs them unless they form an independently consumed prerequisite.
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

- Execution/review may discover new topology evidence but a Worker cannot silently broaden, merge or self-split Card authority. At the smallest safe durable boundary, independently valid evidence is preserved and remaining unaccepted scope returns to Execution Prep for bounded re-decomposition; stronger accepted Planning seams remain authoritative unless revised by their owning stage.

## Consequences

The strongest planning work survives JIT refinement without forcing speculative Card authoring. The semantic Card invariant supplies the primary split/merge decision function, while the topology challenge remains a second-order safeguard. Simple cohesive work is protected from meaningless micro-Card ceremony, and materially risky mega-Card formation or late oversize evidence is routed to the correct topology owner.
