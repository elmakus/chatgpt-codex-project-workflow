# OpenSpec Contract

## 1. Role

OpenSpec formalizes behavior and technical contracts where freezing them before implementation reduces ambiguity or risk.

OpenSpec does not replace accepted requirements, Master Plan, Task Cards, Task Board or cumulative handoffs.

A Task Card is a global bounded work package. An OpenSpec task is a smaller implementation checkbox within one change.

## 2. Selective policy

OpenSpec is **not mandatory for every task**.

Normally required/justified for:
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
- pure research/investigation;
- runbooks/deployment checklists that do not change behavior;
- mechanical CI fixes;
- small mechanical refactors without behavior change.

If uncertain, evaluate contract risk rather than applying OpenSpec mechanically.

## 3. Candidate versus actual change

During planning ChatGPT may mark an OpenSpec candidate. Do not build the complete OpenSpec far in advance merely because a distant card might need one.

The **current executor** creates/reconciles actual OpenSpec just-in-time immediately before implementation when required.

## 4. JIT reconciliation inputs

Before implementation reconcile OpenSpec against:
- actual current HEAD/source/runtime;
- latest cumulative handoff;
- current milestone and Task Card;
- authoritative requirements/accepted decisions;
- relevant Master Plan constraints;
- completed dependencies.

Actual code/runtime is an input to implementation design, not authority to silently rewrite product requirements.

## 5. Standard flow

A typical change uses:

```text
proposal.md   # why / what
specs/        # testable behavior / contracts
design.md     # how / trade-offs, only when useful
tasks.md      # implementation subtasks
apply
verify
archive
```

Exact tooling/version may evolve; preserve semantic sequence.

## 6. Gate before coding

When OpenSpec is required:
- proposal/specs/design/tasks must be coherent enough for the card;
- do not implement against an obviously stale/contradictory spec;
- implementation-detail drift may be reconciled by the current executor;
- material strategic drift follows the shared Refresh Gate blocker path.

## 7. Verification

Card verification includes applicable OpenSpec requirements. A completed change leaves OpenSpec consistent with actual behavior and archival policy.

## 8. Multi-card changes

One OpenSpec change may span multiple Task Cards. Do not collapse all work into one oversized card merely because there is one OpenSpec change.
