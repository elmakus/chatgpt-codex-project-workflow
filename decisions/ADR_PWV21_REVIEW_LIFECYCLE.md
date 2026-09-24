# Decision — PWv2.1 requires layered fresh independent review

- Decision ID: `ADR-PWV21-004`
- Date: `2026-09-24`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@3`
- Related requirements: `requirements/PWV21_POLICY_KERNEL.md`

## Context

The user deliberately prefers systematic verification over lower review cost/latency and wants freshness defined by exact subject production/repair rather than runtime labels.

## Decision

- Formal review distinguishes **finding-closure verification** from **fresh full-scope discovery review**. Closure verification is intentionally anchored to known findings, the repair diff, regression evidence and the materially implicated causal blast radius; it cannot satisfy the next required fresh full-scope discovery review.
- A fresh full-scope review reconstructs correctness from accepted authority, the exact current subject/artifacts and raw evidence. Prior verdict rationales/repair narratives are not its correctness checklist.
- Finding one blocker does not end the full review pass. The reviewer completes the applicable acceptance surface and freezes the complete independently discovered material finding set before repair begins.
- RED repair targets the defect class/root cause, sibling representations and relevant negative space, with generalized regression coverage where feasible.
- Review loops use a stable authority/acceptance epoch. Ordinary implementation/test repair does not reset it; only material accepted authority/acceptance redesign can start a new epoch with durable reset basis.
- Default hard ceilings are 5 Card, 4 Milestone and 3 Final Integration **material defect-class discovery epochs** per stable authority/acceptance epoch. A discovery epoch is consumed only by a qualifying fresh full-scope RED that discovers at least one genuinely new material defect class. Closure verification, ordinary repair, GREEN fresh discovery and recurrence/reopening of an already-known class do not increment the discovery counter.
- Each material defect class has a default ceiling of 3 failed repair→closure-verification rounds before Main convergence/root-cause analysis. Either this per-class breaker or a material-discovery ceiling is a mode switch, never acceptance. Main may then authorize one fresh post-convergence validation.
- A RED post-convergence validation routes to broader structural classification/restructuring rather than another automatic ordinary review loop.

- Every Card receives independent review.
- Every Milestone receives a separate fresh independent review.
- Every completed workstream receives a separate fresh final-integration review.
- A context/agent that materially produced or repaired the exact subject cannot independently review that subject.
- A new Card gets a fresh Reviewer. The Reviewer that discovered a finding may perform bounded closure verification after Worker repair if that Reviewer did not repair the subject; after all known material findings close, the next full-scope discovery review must use a fresh independent Reviewer assignment.
- If a Reviewer repairs the subject, a fresh Reviewer is required for the changed subject.
- Milestone/final reviewers receive authority, current subject and raw/relevant evidence without prior GREEN opinions as anchoring context.
- Review GREEN requires complete required evidence.
- RED repair/re-review is automatic and bounded while inside accepted scope.
- A reopened historical Card gets a fresh Worker and fresh Reviewer.
- When OR/Paseo can instantiate a qualifying fresh Reviewer automatically, no user stop is needed; handoff is required only when freshness cannot be satisfied internally.

- A finding blocks GREEN only when concrete evidence shows it is materially load-bearing for the applicable acceptance/correctness/safety/security/data-integrity/dependency/compatibility/invariant/contract/required-evidence surface. Advisory or speculative observations cannot keep a subject RED merely because improvement remains possible.
- Non-load-bearing observations remain durable and must be reconciled before Final Integration as resolved, cleanup_candidate, deferred, promoted or tracked.
- Bounded safe in-scope cleanup candidates should be grouped into explicit cleanup work with their own exact subject, tests/evidence and independent review rather than mutating already-GREEN Cards ad hoc. Cleanup does not recursively remain open merely because another advisory improvement can be imagined.
- GitHub Issues/trackers may carry intentionally exported future work but remain optional bookkeeping and never the primary canonical review-observation store or workflow authority.
- After all known material findings from a discovery pass close, one fresh full-scope rediscovery gate is mandatory. A fresh RED with a genuinely new material defect class opens the next discovery epoch; recurrence of an already-known class reopens that class without consuming another discovery epoch.

## Consequences

Review cost is intentionally higher, but unbounded reviewer repetition is forbidden. Independence remains semantic and subject-relative, integration review cannot substitute for individual Card review, and repeated RED changes the workflow response from local repair repetition to systemic convergence analysis.

The M02 R09→R12 sequence is retained as empirical design evidence, not as normative authority or a requirement to replay M02.
