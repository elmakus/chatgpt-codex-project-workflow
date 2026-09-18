# Common OpenSpec Contract

## Role

OpenSpec formalizes behavior and technical contracts when freezing them before implementation reduces ambiguity or risk.

It does not replace requirements, accepted decisions, Master Plan, Task Cards, Task Board or cumulative handoffs.

A Task Card is a global bounded work package. An OpenSpec task is a smaller implementation checkbox inside one change.

## Selective policy

Normally justified for:
- new/changed behavior contracts;
- API contracts;
- persistent schema/state contracts;
- retry/idempotency/reconciliation semantics;
- migrations;
- security-sensitive behavior;
- cross-package architecture;
- external side-effect semantics;
- complex multi-card changes;
- changes where a technical contract should be frozen before implementation.

If uncertain, evaluate contract risk rather than applying OpenSpec mechanically.

Normally skip:
- simple bug fixes with unambiguous intended behavior;
- documentation-only work;
- pure research;
- runbooks/checklists that do not change behavior;
- mechanical CI fixes;
- small mechanical refactors without behavior change.

## Candidate versus actual change

Planning may mark an OpenSpec candidate. Do not build a complete distant change merely because a later Card might need one.

The current executor creates/reconciles actual OpenSpec just-in-time immediately before implementation when required.

## JIT creation/reconciliation

Do not build complete distant OpenSpec changes merely because they might later be useful.

When OpenSpec is required, reconcile it immediately before implementation against:
- actual current HEAD/source/runtime;
- relevant prior handoff when it materially supplies predecessor truth;
- current milestone and Task Card;
- the Task Card's exact authority slice;
- authoritative requirements/accepted decisions;
- relevant approved-plan constraints;
- accepted/completed dependency results.

Implementation detail may be reconciled within accepted authority. Strategic drift must not be hidden by rewriting the spec.

## Typical flow

```text
proposal.md
specs/
design.md      # only when useful
tasks.md
apply
verify
archive
```

Exact tooling may evolve; preserve the semantic sequence.

## Gate before coding

When OpenSpec is required:
- proposal/specs/design/tasks must be coherent enough for the current Card;
- do not implement against an obviously stale or contradictory spec;
- implementation-detail drift may be reconciled within accepted authority;
- material strategic drift follows the normal strategic blocker path.

## Verification

Card verification includes applicable OpenSpec requirements. Completed behavior and OpenSpec must not contradict one another and should follow the project's archival policy.

## Multi-card changes

One OpenSpec change may span multiple Task Cards. Do not collapse all work into one oversized Card merely because there is one OpenSpec change.
