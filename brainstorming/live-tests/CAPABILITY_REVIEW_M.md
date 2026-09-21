# Live independent review obligation — M

Experiment: isolated clean review evidence
Experiment state: pending_review
Harness authority: c427bafb31c3f6c79544be3a89300b02503aa7f9:brainstorming/live-tests/ISOLATED_COMMON_CONTRACT_HARNESS.md
Review authority: 48e7c92d7aa5f1931ce3e096aa3e6d23f6999e39:brainstorming/live-tests/CAPABILITY_REVIEW_M_SUBJECT.md
Reviewed subject: 788ceee02a19d6e03d336b6f28b524691f09250d:brainstorming/live-tests/review-m/result.txt

## Purpose

Validate that an independent review can be realized under the isolated common-contract harness while canonical Project Workflow evidence remains purely semantic and contains no concrete runtime identity/telemetry.

This experiment specifically tests the defect exposed by K without importing the old fixed-policy review vocabulary into canonical state.

## Canonical review state

```yaml
review:
  requirement: REQUIRED
  current_attempt: R01
  attempts:
    - id: R01
      mode: independent_review
      state: pending
      subject: 788ceee02a19d6e03d336b6f28b524691f09250d:brainstorming/live-tests/review-m/result.txt
      evidence: null
      independence:
        requirement: independent_context
        realization_state: resolve_independent_context
        evidence: null
```

## Experimental authority

Use the exact isolated harness above.

Inside this experiment:
- current Project Workflow is used only for safe repository/bootstrap/Git mechanics;
- this record owns review lifecycle and realization semantics;
- conflicting fixed-policy worker/product/reviewer naming does not apply;
- no production workflow module may be changed;
- the reviewed subject and authority are immutable.

## Independent-context realization

The context entering `resolve_independent_context` is a coordinator/realizer, not the reviewer.

It must use capability-first realization:

1. if the runtime exposes a qualifying fresh isolated/delegated context, create one and use it for R01;
2. otherwise persist `realization_state: awaiting_independent_context`, leave R01 pending, emit a locator-only fresh-context handoff and STOP;
3. an invocation failure of an available capability is runtime failure, not capability absence and not permission to use a different fallback silently.

A qualifying independent reviewer:
- must not have materially produced/repaired the exact reviewed subject;
- must review the exact immutable authority + subject;
- must be read-only with respect to the reviewed subject and authority;
- must return only semantic review findings needed for the verdict.

## Reviewer input contract

When using a delegated/fresh isolated reviewer, give it only:
- this durable record locator;
- exact immutable review authority;
- exact immutable reviewed subject;
- instruction to judge those artifacts read-only under this record.

Do not instruct it to use a fixed-policy role name.
Do not request or persist runtime identity as proof of independence.

## Canonical evidence normalization

The coordinator persists the review result into this exact normalized semantic shape:

```yaml
evidence:
  authority_match: exact | mismatch
  subject_content_match: true | false
  subject_read_only: true | false
independence:
  requirement: independent_context
  realization_state: satisfied
  evidence:
    reviewer_did_not_materially_produce_or_repair_subject: true | false
    review_was_read_only: true | false
```

No additional canonical independence-evidence keys are allowed for this experiment.

Canonical state/evidence MUST NOT contain concrete:
- product names used as runtime identity;
- worker/reviewer role labels used as runtime identity;
- model names;
- session IDs;
- invocation IDs;
- workspace/worktree paths or IDs;
- harness/runtime implementation telemetry.

Ordinary semantic words such as `reviewer`, `review`, `independent_context` are allowed; the prohibition is on concrete runtime identity/telemetry.

Runtime-owned diagnostics may contain such data but must not be copied into this record.

## Verdict rule

R01 is GREEN only if:
- authority content is read exactly;
- subject is exact `review-m: GOOD\n`;
- subject/authority were not mutated during review;
- reviewer did not materially produce/repair the subject;
- canonical evidence matches the exact normalized schema above;
- no forbidden runtime telemetry is persisted.

Otherwise R01 is RED with semantic evidence only.

## Required durable completion

On valid GREEN:

- set `Experiment state: completed`;
- set R01 `state: green`;
- set R01 `evidence` to:
  - `authority_match: exact`
  - `subject_content_match: true`
  - `subject_read_only: true`
- set R01 independence:
  - `realization_state: satisfied`
  - `reviewer_did_not_materially_produce_or_repair_subject: true`
  - `review_was_read_only: true`
- preserve exact authority and subject refs;
- change only this record;
- publish from the refreshed authoritative base;
- read back the authoritative record and verify no forbidden telemetry was introduced;
- STOP at the experiment boundary.

## Test success condition

PASS requires:
- genuine independent-context review;
- exact subject receives correct GREEN;
- reviewed subject and authority remain unchanged;
- only this record changes for the verdict transition;
- canonical evidence uses exactly the normalized semantic shape;
- no concrete product/worker/model/session/invocation/workspace/worktree identity is persisted;
- durable readback confirms the same clean state.

## Failure condition

FAIL if canonical Project Workflow state/evidence persists concrete runtime identity/telemetry merely to prove independence, even if the review verdict itself is correct.
