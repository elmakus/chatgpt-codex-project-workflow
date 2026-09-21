# Live independent plan-review obligation — B

Experiment: capability-first live A/B
Review requirement: RECOMMENDED
Review state: RED
Review subject: dcdc80769c0b64d4444aa330285a780f8483ec5c:brainstorming/live-tests/CAPABILITY_PLAN_R1.md
Subject author provenance: live-test-author-context
Independence requirement: the context that initiates this review must not issue the verdict; the verdict must be produced by a separate independent context
Review evidence: RED — M01 preserves one runtime-neutral review obligation, reviewer independence, immutable subject, and GREEN/RED evidence semantics. M02 is materially incomplete because it defines only successful use of an available independent-context capability and the capability-absent fresh-context handoff. It leaves the available-but-invocation-fails state undefined, implicitly assuming capability availability implies successful realization. That can produce divergent runtime behavior or incorrectly reclassify invocation failure as capability absence; the independent-review obligation must remain intact and invocation failure needs an explicit distinct continuation/failure rule.

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
