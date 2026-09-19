# Codex-only Independent Review

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Formal review semantics

- Review one immutable exact subject against the same applicable authority and acceptance surface that governed implementation.
- The reviewer is independent from the implementation owner for that subject.
- The reviewer does not mutate or repair the subject while acting as reviewer.
- Persist project-level `pending → in_progress → green|red` state plus durable evidence.
- GREEN returns control to Codex Main for project-state finalization/continuation.
- RED preserves the failed attempt and returns through Codex Main to the owning Executor for bounded repair when authorized.
- Corrected implementation is a new exact review subject/attempt.
- Reusing the same logical reviewer for a later subject is allowed when independence remains valid; replacement mechanics are runtime-owned.
- A qualifying Codex-managed verdict needs no second mandatory normal-ChatGPT review.

## Deferred contract work

M02 finalizes exact project-level provenance fields, review owner/state placement, RED corrective routing and recovery without embedding runtime worker identity.
