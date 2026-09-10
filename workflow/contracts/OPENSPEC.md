# OpenSpec Contract

## 1. Role

OpenSpec formalizes behavior and technical contracts for changes where freezing those contracts before implementation reduces ambiguity or risk.

OpenSpec does not replace:
- accepted project requirements;
- the Master Plan;
- Task Cards;
- Task Board;
- cumulative handoffs.

A Task Card is a global bounded work package. An OpenSpec task is a smaller implementation checkbox within an OpenSpec change.

## 2. Selective policy

OpenSpec is **not mandatory for every task**.

It is normally required/justified for:
- new or changed behavior contracts;
- API contracts;
- persistent schema/state contracts;
- retry, idempotency or reconciliation semantics;
- migrations;
- security-sensitive behavior;
- cross-package architecture;
- external side-effect semantics;
- complex changes spanning multiple Task Cards;
- changes where a technical contract should be frozen before implementation.

It is normally skipped for:
- a simple bug fix whose intended behavior is already unambiguous;
- documentation-only changes;
- pure research/investigation;
- runbooks/deployment checklists that do not change behavior;
- mechanical CI fixes;
- small mechanical refactors without behavior change;
- other small unambiguous changes.

If uncertain, evaluate contract risk rather than applying OpenSpec mechanically.

## 3. Candidate versus actual change

During planning, ChatGPT may mark an OpenSpec candidate.

Do not build the complete OpenSpec far in advance merely because a distant card might need one.

Codex creates or reconciles the actual OpenSpec **just in time** immediately before implementation.

## 4. JIT reconciliation inputs

Before implementation, reconcile the OpenSpec against:
- actual current HEAD/source;
- latest cumulative handoff;
- current milestone;
- current Task Card;
- authoritative requirements and accepted decisions;
- relevant Master Plan constraints;
- completed dependencies.

The actual code is an input to implementation design, not authority to silently rewrite product requirements.

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

The exact OpenSpec tooling/version may evolve; preserve the semantic sequence.

## 6. Gate before coding

When OpenSpec is required:
- proposal/specs/design/tasks must be coherent enough for the card;
- do not implement against an obviously stale or contradictory spec;
- reconcile implementation-detail drift within Codex authority;
- material strategic drift triggers the Refresh Gate blocker path.

## 7. Verification

Card verification includes applicable OpenSpec requirements.

A completed change should leave OpenSpec state consistent with actual implemented behavior and archival policy.

## 8. Multi-card changes

One OpenSpec change may span multiple Task Cards when the behavior contract crosses those cards.

Do not collapse all work into one oversized Task Card merely because there is one OpenSpec change.
