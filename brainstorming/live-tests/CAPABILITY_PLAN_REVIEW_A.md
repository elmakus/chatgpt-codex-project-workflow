# Live independent plan-review obligation — A

Experiment: capability-first live A/B
Review requirement: RECOMMENDED
Review state: completed
Review subject: dcdc80769c0b64d4444aa330285a780f8483ec5c:brainstorming/live-tests/CAPABILITY_PLAN_R1.md
Subject author provenance: live-test-author-context
Independence requirement: the context that initiates this review must not issue the verdict; the verdict must be produced by a separate independent context
Review verdict: RED
Reviewer: fresh logical Muse Tester cap-plan-review-a-tester-20260921
Reviewer invocation: 7481e708-8105-4904-9a59-02b4014bbff7
Reviewer writes: none
Reviewer inputs: exact immutable subject dcdc80769c0b64d4444aa330285a780f8483ec5c:brainstorming/live-tests/CAPABILITY_PLAN_R1.md and this record
Review evidence: Subject L31-32 define available->independent review and absent->fresh-context handoff, but L39 explicitly leaves available-yet-invocation-fails undefined, against L11/L35 one-common-obligation/invariant-semantics promise. Record L33 forbids reclassifying invocation failure as absence. Target-branch common preexecution core requires failed invocation to follow retry/blocker/evidence, preserve pending obligation, no silent handoff/fallback (COMMON_PREEXECUTION_CORE.md L146/L268/L314-316/L351/L380). Material completeness/correctness gap; hidden assumption that availability implies successful invocation. Independence/immutability/no-role-name aspects passed.

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
