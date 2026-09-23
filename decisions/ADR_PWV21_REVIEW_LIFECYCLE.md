# Decision — PWv2.1 requires layered fresh independent review

- Decision ID: `ADR-PWV21-004`
- Date: `2026-09-23`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@1`
- Related requirements: `requirements/PWV21_POLICY_KERNEL.md`

## Context

The user deliberately prefers systematic verification over lower review cost/latency and wants freshness defined by exact subject production/repair rather than runtime labels.

## Decision

- Every Card receives independent review.
- Every Milestone receives a separate fresh independent review.
- Every completed workstream receives a separate fresh final-integration review.
- A context/agent that materially produced or repaired the exact subject cannot independently review that subject.
- A new Card gets a fresh Reviewer; a same-Card Reviewer may recheck Worker repairs if the Reviewer did not repair the subject.
- If a Reviewer repairs the subject, a fresh Reviewer is required for the changed subject.
- Milestone/final reviewers receive authority, current subject and raw/relevant evidence without prior GREEN opinions as anchoring context.
- Review GREEN requires complete required evidence.
- RED repair/re-review is automatic and bounded while inside accepted scope.
- A reopened historical Card gets a fresh Worker and fresh Reviewer.
- When OR/Paseo can instantiate a qualifying fresh Reviewer automatically, no user stop is needed; handoff is required only when freshness cannot be satisfied internally.

## Consequences

Review cost is intentionally higher. Independence remains semantic and subject-relative, and integration review cannot substitute for individual Card review.
