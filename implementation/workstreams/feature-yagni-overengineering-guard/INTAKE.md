# Feature Intake — YAGNI / overengineering guard

## Identity

- Workstream ID: `feature-yagni-overengineering-guard`
- Intake kind: `feature`
- Branch: `feat/yagni-overengineering-guard`
- Integration target: `main`
- Base ref: `13e27863cb11ec9e223ee2af191f79fe6b8d559d`

## Operator intent

Evaluate whether Project Workflow already has a general rule against overengineering and, if not, discover a small YAGNI-style principle that prevents speculative complexity without blocking complexity that is justified by current accepted requirements or evidence.

## Pre-creation discovery

- Current `main` contains no literal `YAGNI`, `KISS`, `overengineering`, `over-engineering`, `keep it simple`, or `future-proof` rule found by repository search.
- Existing rules are narrower:
  - progressive disclosure says to read the smallest context required;
  - private-infrastructure access is limited to the smallest scope needed;
  - Brainstorming keeps simple scopes lightweight;
  - issue intake supports a proportional micro-fix path for bounded low-risk changes;
  - delegated planning forbids placeholder work for unknown future scope.
- Those rules reduce unnecessary work in specific situations but do not state a general engineering invariant against speculative abstractions, genericity, extensibility, or machinery.
- No matching branch/workstream was found for YAGNI / overengineering.
- No parent-only state is required; this is independent work based on current `main`.

## Intake state

- State: active
- Path classification: feature discovery / Brainstorming
- Downstream owner: pending canonical Brainstorming record
- Definition promotion: pending
