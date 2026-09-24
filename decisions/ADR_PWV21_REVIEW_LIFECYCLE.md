# Decision — PWv2.1 requires layered fresh independent review

- Decision ID: `ADR-PWV21-004`
- Date: `2026-09-24`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@2`
- Related requirements: `requirements/PWV21_POLICY_KERNEL.md`

## Context

The user deliberately prefers systematic verification over lower review cost/latency and wants freshness defined by exact subject production/repair rather than runtime labels.

## Decision

- Formal review distinguishes **finding closure / repair verification** from **fresh full-scope review**. Verification of known findings cannot satisfy a later required fresh full-scope review.
- A fresh full-scope review reconstructs correctness from accepted authority, the exact current subject/artifacts and raw evidence. Prior verdict rationales/repair narratives are not its correctness checklist.
- Finding one blocker does not end the full review pass. The reviewer completes the applicable acceptance surface and freezes the complete independently discovered material finding set before repair begins.
- RED repair targets the defect class/root cause, sibling representations and relevant negative space, with generalized regression coverage where feasible.
- Review loops use a stable authority/acceptance epoch. Ordinary implementation/test repair does not reset it; only material accepted authority/acceptance redesign can start a new epoch with durable reset basis.
- Default hard ceilings are 5 fresh full-scope Card reviews, 4 Milestone reviews and 3 final-integration reviews per stable epoch. Finding-verification passes do not count.
- A hard ceiling is a mode switch, not acceptance: Main performs root-cause/convergence analysis and may authorize one fresh post-convergence validation.
- A RED post-convergence validation routes to broader structural classification/restructuring rather than another automatic ordinary review loop.

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

Review cost is intentionally higher, but unbounded reviewer repetition is forbidden. Independence remains semantic and subject-relative, integration review cannot substitute for individual Card review, and repeated RED changes the workflow response from local repair repetition to systemic convergence analysis.

The M02 R09→R12 sequence is retained as empirical design evidence, not as normative authority or a requirement to replay M02.
