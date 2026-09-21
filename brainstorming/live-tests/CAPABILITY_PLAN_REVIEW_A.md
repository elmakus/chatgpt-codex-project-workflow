# Live independent plan-review obligation — A

Experiment: capability-first live A/B
Review requirement: RECOMMENDED
Review state: pending
Review subject: dcdc80769c0b64d4444aa330285a780f8483ec5c:brainstorming/live-tests/CAPABILITY_PLAN_R1.md
Subject author provenance: live-test-author-context
Independence requirement: verdict must be produced from a context independent of the subject author
Review evidence: none

## Review obligation

Independently review the exact immutable plan subject for:
- consistency and completeness;
- hidden assumptions or material omissions;
- whether capability-first transport preserves one common Project Workflow semantic contract;
- whether the deliberate omission around "capability exists but invocation fails" creates a material correctness gap.

Do not mutate the reviewed plan while judging it.

Return exactly one semantic verdict:
- GREEN — no material defect found; or
- RED — material defect found.

Persist concise evidence with the verdict.

## Runtime-neutral realization rule

This record intentionally names no concrete worker role, model, product, harness, or delegation mechanism.

The executing Main/runtime must satisfy the independence requirement using an available independent context. If no such delegated/native independent context exists, preserve this same durable obligation and use a fresh-context handoff.

An invocation failure of an available capability must not be reclassified as capability absence.
