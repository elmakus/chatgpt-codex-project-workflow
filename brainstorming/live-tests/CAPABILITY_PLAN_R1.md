# Capability-routing live-test plan R1

Status: draft

## Goal

Validate capability-first independent plan review without naming a concrete worker role.

## Requirements

- Preserve one common Project Workflow review obligation across runtimes.
- The reviewer must be independent from the author of this exact plan subject.
- The reviewed subject is immutable during review.
- Verdict must be GREEN or RED with concise evidence.

## Milestones

### M01 — Common review contract

Outcome:
- one common independent-review obligation exists;
- runtime-specific realization is not encoded in the plan.

Acceptance:
- both runtime variants can consume the same semantic obligation;
- no concrete worker-role name is required by the obligation.

### M02 — Capability realization

Outcome:
- a runtime with an independent-context capability may realize review without a user handoff;
- a runtime without such capability must preserve the same obligation and use a fresh-context handoff.

Acceptance:
- transport differs, durable review semantics do not.

## Deliberate review point

The plan intentionally does not define what should happen when an independent-context capability is reported available but its invocation fails.
A correct independent reviewer should identify whether this omission matters to the capability-first contract.
