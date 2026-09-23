# Decision — PWv2.1 permits only plan-authorized parallel Cards with one mutating Worker per Card

- Decision ID: `ADR-PWV21-003`
- Date: `2026-09-23`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@1`
- Related requirements: `requirements/PWV21_POLICY_KERNEL.md`

## Context

Current PWv2 serializes Cards inside a workstream. PWv2.1 needs bounded Card-level parallelism where Planning can prove independence, but must not hide a second mutating topology inside OR.

## Decision

- Accepted Plan/JIT may explicitly declare finite parallel-safe Card sets.
- The kernel validates dependencies, structured write scopes, external effect domains and relevant authority/scope overlap.
- It never invents parallelism merely because a dependency edge is absent.
- Overlapping mutating write scopes always serialize; no override exists.
- Every parallel Card remains a separate semantic PW Card with its own obligation/result/review.
- One Card has one primary mutating Worker. Multiple mutating workers inside one Card are forbidden.
- A Worker may request bounded read-only/advisory sibling helpers through OR; workers do not recursively spawn subagents.
- OR controls concrete scheduling/concurrency/isolation only after PW has established legality.
- Sibling invalidation makes only affected results stale; unaffected valid results are preserved.
- Composed sibling results require an integrated compatibility obligation before downstream combined consumption, but compatibility review never replaces individual Card review.

## Consequences

PW gains bounded parallel Card semantics without becoming a runtime scheduler or obscuring mutation ownership.
