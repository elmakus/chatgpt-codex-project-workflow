# Review and Handoff

## Card close

A card is not done because an executor says it is done. Apply Task Card Definition of Done and GitHub State Contract.

Individual Task Cards do not get separate production PRs. Their durable commits/results remain on the current milestone's one primary implementation branch until milestone finalization.

## Milestone completion

All required cards being `done` is necessary but not sufficient.

Run integrated milestone acceptance against the intended final state of the primary milestone implementation branch.

- **RED:** create/reopen bounded corrective work on the same milestone branch; milestone is not done and must not be merged to `main`.
- **GREEN:** complete applicable independent review, then open the one final milestone PR to `main`.

A branch-level GREEN result is a merge candidate, not yet the completed durable milestone checkpoint. The milestone becomes terminal `done` only after the final PR is merged and post-merge reconciliation is complete.

## Independent review policy

Use a fresh independent **normal ChatGPT chat** that reads durable repo/evidence rather than relying on executor narrative:

- **REQUIRED** for high-risk work: security/auth, destructive/data migrations, difficult-to-reverse production/live configuration, important external-state protection boundaries, or comparable risk.
- **RECOMMENDED** for major architecture, large refactors, complex state machines and broad cross-package changes.
- **OPTIONAL** for simple low-risk mechanical/docs changes.

For milestone finalization, perform REQUIRED review before opening the final milestone PR. Perform RECOMMENDED review before the PR unless the user/relevant authority explicitly waives it. Any review finding that makes the milestone RED returns corrective work to the same milestone branch before PR/merge.

For high-risk external writes, place independent review at the last useful reversible checkpoint when practical, then perform write + post-write readback/verification.

Do not create a permanent review role or review every trivial Task Card.

## Cumulative handoff

Canonical location: `project-handoffs/MXX_HANDOFF.md`.

A cumulative handoff must be sufficient for a fresh ChatGPT chat or Codex session to start without prior conversation. Record as applicable:
- goal/status/checkpoint;
- implemented behavior;
- accepted decisions;
- changed files/packages;
- schemas/migrations/APIs/contracts;
- side effects/idempotency/external readback;
- tests/results and independent review;
- known issues/deferred items;
- provenance and exact Git state;
- accepted milestone implementation branch HEAD for review provenance;
- implementation-bearing merged `main` commit (`implementation_head`);
- final accepted `main` checkpoint after reconciliation;
- architecture reopen assessment;
- requirements satisfied/outstanding;
- next durable starting point;
- exact context needed by the next executor/session.

A handoff summarizes durable truth; it does not replace Task Board, cards, specs, evidence or exact Git objects.

## Finalization and checkpoint

The canonical milestone publication sequence is:

1. start milestone execution from the previous accepted GREEN `main` checkpoint on one primary implementation branch;
2. complete all Task Cards and pre-merge corrective work on that branch;
3. run integrated milestone acceptance on the intended final branch HEAD;
4. RED stays on the branch and is not merged;
5. after GREEN, complete REQUIRED review and any RECOMMENDED review unless explicitly waived;
6. open one milestone PR from the primary implementation branch to `main`;
7. merge only the accepted GREEN state;
8. reconcile cumulative handoff, Task Board and milestone metadata to the actual merged `main` state;
9. record `implementation_head` as the exact implementation-bearing `main` commit produced by merging the accepted final milestone PR;
10. record `checkpoint` as the actual accepted final `main` state after any metadata-only reconciliation;
11. set the milestone `done` only after this reconciliation is complete.

Because the actual merge SHA may not be knowable before merge, a small **metadata-only closure commit on `main`** is allowed when necessary to record the actual checkpoint/handoff/result metadata. It must not change production behavior, requirements or implementation scope. If such a closure commit is required, `implementation_head` remains the merge-produced implementation-bearing `main` commit and the resulting `main` HEAD becomes `checkpoint`. If no closure commit is required, both may identify the same `main` commit.

Do not use direct `main` commits for normal production implementation or corrective work.

The next milestone starts from that final GREEN `main` checkpoint and re-runs Capability Gate for its first executable card; it does not automatically inherit the previous executor.

## Experimental path integration

Path A/Path B/Hybrid research or prototype branches may exist independently, but they are not production publication branches. After an alternative is accepted, integrate the selected result onto the one primary milestone implementation branch, then run normal integrated acceptance/review/PR finalization from that branch.

## System verification and cutover

Independent system verification should act as its own gate when required. Deployment/cutover/migration should be runbook- or Task-Card-driven rather than improvised from chat. Runbooks/checklists do not automatically require OpenSpec unless they change a behavior contract.
