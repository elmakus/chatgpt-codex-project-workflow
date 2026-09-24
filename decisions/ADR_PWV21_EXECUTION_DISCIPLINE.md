# Decision — PWv2.1 uses bounded falsification-first Worker discipline

- Decision ID: `ADR-PWV21-008`
- Date: `2026-09-24`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@3`
- Related requirements: `PWV21-REQ-131..132`

## Context

R3 research found value in Superpowers-style test-first/YAGNI execution discipline, but the user explicitly does not want fixed small/medium/large project classes or wall-clock optimization policy in PWv2.1. Worker discipline must improve correctness without introducing another workflow-ceremony layer or speculative abstraction pressure.

## Decision

- Where an accepted Card outcome can be meaningfully falsified through an automated or observable check, the Worker starts from that failing check before implementation.
- The Worker then implements the minimum in-scope change needed to satisfy accepted Card authority and produce GREEN evidence.
- YAGNI is binding scope discipline: speculative functionality, abstraction, future-proofing or adjacent product work outside the Card is forbidden.
- After GREEN local evidence, bounded refactoring is allowed only when it remains within Card authority and does not create new product/architecture scope.
- DRY is guidance, not an absolute invariant. Local duplication may remain preferable to premature abstraction when abstraction would increase coupling, risk or scope.
- Documentation, migration, workflow-policy and other work that is not naturally expressed as a unit test uses an explicit observable/falsifiable acceptance check rather than forcing artificial test form.
- These rules constrain Worker execution inside an already-authorized Card. They do not create new Milestones, Cards, premium gates or runtime orchestration semantics.
- PWv2.1 introduces no fixed LOC/file/token/time maxima and no small/medium/large project category. The LLM/Planning/Execution Prep derives Milestone and Card topology from semantic decomposition.

## Consequences

Workers receive a narrower search space and stronger correctness feedback while preserving Card authority. TDD/falsification-first is used where meaningful, YAGNI prevents speculative scope expansion, and DRY cannot force risky abstraction. Performance/wall-clock tuning remains deferred to later evidence rather than becoming PWv2.1 policy.
