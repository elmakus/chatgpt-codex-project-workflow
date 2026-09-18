# Common OpenSpec Contract

## Role

OpenSpec formalizes behavior and technical contracts when freezing them before implementation reduces ambiguity or risk.

It does not replace requirements, accepted decisions, Master Plan, Task Cards, Task Board or cumulative handoffs.

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

Normally skip:
- simple bug fixes with unambiguous intended behavior;
- documentation-only work;
- pure research;
- runbooks/checklists that do not change behavior;
- mechanical CI fixes;
- small mechanical refactors without behavior change.

## JIT creation/reconciliation

Do not build complete distant OpenSpec changes merely because they might later be useful.

When OpenSpec is required, reconcile it immediately before implementation against:
- actual current source/runtime;
- current milestone and Task Card;
- exact authority slice;
- accepted dependency results;
- relevant prior handoff when it materially supplies predecessor truth.

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

## Verification

Card verification includes applicable OpenSpec requirements. Completed behavior and OpenSpec must not contradict one another.
