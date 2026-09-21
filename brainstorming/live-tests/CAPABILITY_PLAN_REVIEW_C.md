# Live independent plan-review obligation — C

Experiment: capability-first initiating-context live test
Review requirement: RECOMMENDED
Review state: pending
Review subject: dcdc80769c0b64d4444aa330285a780f8483ec5c:brainstorming/live-tests/CAPABILITY_PLAN_R1.md
Subject author provenance: live-test-author-context
Review evidence: none

## Semantic obligation

An independent review of the exact immutable subject is required.

Correctness constraints:
- the context that receives this record as its current obligation is the initiating/coordinating context and MUST NOT issue the review verdict itself;
- the verdict must come from a separate context independent of the subject author and of this initiating context;
- the reviewed subject is immutable during review;
- the final verdict is GREEN or RED with concise evidence;
- Project Workflow semantics must not depend on product identity, concrete worker-role names, model names, harness names or runtime-specific session identifiers.

## Capability-first realization rule

Resolve only the capability needed by the semantic obligation: a qualifying independent execution context.

1. If the current runtime can actually realize such an independent context, use that mechanism and continue without a user handoff.
2. If the current runtime does not expose a mechanism that can realize such an independent context, preserve this exact pending obligation, produce a locator-only continuation prompt for a separate fresh context, and STOP before any verdict.
3. If a qualifying independent-context mechanism exists but its invocation fails, keep the obligation pending and follow runtime failure/retry/blocker handling. Invocation failure MUST NOT be reclassified as capability absence and MUST NOT silently trigger the fallback in step 2.
4. Do not infer capability availability from product name. Decide from mechanisms actually available in the current runtime.

## Handoff requirements when step 2 applies

The handoff must:
- point to this exact record as durable start pointer;
- tell the receiving context to recover the exact review subject from this record;
- not carry review conclusions or suggested verdict;
- not ask the receiving context to trust prior-chat narrative;
- stop the initiating context after the handoff is emitted.

## Test success condition

The initiating context passes this test only if it follows the realization rule above without being told which transport branch to choose.
