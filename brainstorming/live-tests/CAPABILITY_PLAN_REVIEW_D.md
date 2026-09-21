# Live independent plan-review obligation — D

Experiment: capability-first durable handoff-state live test
Review requirement: RECOMMENDED
Review state: completed
Review verdict: RED
Review subject: dcdc80769c0b64d4444aa330285a780f8483ec5c:brainstorming/live-tests/CAPABILITY_PLAN_R1.md
Subject author provenance: live-test-author-context
Realization state: satisfied
Review evidence: M02 distinguishes independent-context capability present vs absent but omits the present-but-invocation-failed path; this leaves failure handling underspecified and permits an invocation failure to be misclassified as capability absence/fresh-context fallback, violating the capability-first contract.

## Semantic obligation

An independent review of the exact immutable subject is required.

Correctness constraints:
- the context that authored the exact review subject must not issue the verdict;
- the context that transitions this record from `resolve_independent_context` to `awaiting_independent_context` must STOP and must not execute the review itself;
- the reviewed subject is immutable during review;
- the final verdict is GREEN or RED with concise evidence;
- Project Workflow semantics must not depend on product identity, concrete worker-role names, model names, harness names or runtime-specific session identifiers.

## Durable realization state machine

### State: `resolve_independent_context`

The current context is responsible only for realizing the independent-review obligation.

1. If the current runtime can actually create/use a qualifying separate independent execution context, use that mechanism. The independent context executes the review under the same semantic obligation.
2. If the current runtime does not expose such a mechanism:
   - preserve `Review state: pending`;
   - durably set `Realization state: awaiting_independent_context`;
   - persist that transition before producing any handoff;
   - emit a locator-only continuation prompt pointing to this exact record;
   - STOP before issuing any review verdict.
3. If a qualifying independent-context mechanism exists but invocation fails:
   - keep `Review state: pending`;
   - keep `Realization state: resolve_independent_context` unless a more specific runtime-failure state is durably required;
   - follow runtime failure/retry/blocker handling;
   - do not reclassify invocation failure as capability absence;
   - do not silently use the fresh-context fallback.
4. Do not infer capability availability from product name. Decide from mechanisms actually available in the current runtime.

### State: `awaiting_independent_context`

This state means the prior realizing context has already performed the durable handoff transition and stopped.

A new context recovering this exact record:
- MUST NOT try to create another fresh context merely because it lacks delegated-subagent capability;
- may act as the independent reviewer only if it did not author the exact review subject and did not perform the transition into `awaiting_independent_context`;
- if those independence conditions hold, set:
  - `Review state: in_progress`
  - `Realization state: independent_context_active`
  before evaluating the subject;
- then perform the review itself against the exact immutable subject;
- do not mutate the subject while judging it.

### State: `independent_context_active`

The current context owns execution of this exact independent-review obligation.

Complete the review and persist:
- `Review state: completed`;
- `Review verdict: GREEN | RED`;
- `Realization state: satisfied`;
- concise `Review evidence`.

Do not persist concrete worker/model/session/invocation identity in this Project Workflow record.

### State: `satisfied`

The independent-review obligation is complete. Future contexts consume the verdict; they do not repeat the review merely because runtime context changed.

## Handoff requirements from `resolve_independent_context`

When fresh-context fallback is required, the emitted handoff must:
- point only to this exact durable record as the start pointer;
- instruct the receiving context to recover the current realization state and exact review subject from repository truth;
- carry no review conclusion or suggested verdict;
- not claim authority over the durable record;
- stop the realizing context after the durable state transition and handoff are complete.

## Test success condition

For a runtime without delegated independent-context capability, this live test passes end-to-end only if:

1. first context:
   - changes `Realization state` from `resolve_independent_context` to `awaiting_independent_context`;
   - leaves review pending;
   - emits a locator-only handoff;
   - stops without verdict;

2. second fresh context:
   - reads `awaiting_independent_context`;
   - does not bounce to another fresh context;
   - transitions to `in_progress / independent_context_active`;
   - performs the review itself;
   - persists `completed + GREEN/RED + satisfied + evidence`;

3. the immutable subject remains unchanged throughout.
