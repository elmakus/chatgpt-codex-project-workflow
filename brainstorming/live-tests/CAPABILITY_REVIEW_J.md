# Live Review obligation — J

Experiment: cross-runtime GREEN review and finalization
Experiment state: completed
Review authority: dbe81191afb840e096ef0aadde9b922ee5ccf5da:brainstorming/live-tests/CAPABILITY_REVIEW_J_SUBJECT.md
Active execution: null

## Synthetic Task Board

```yaml
cards:
  - id: T01
    execution_status: done
    result_ref: a23712266f36ae70cda129a9b3242c6391b50b49
    evidence: exact synthetic implementation result is durable

    review:
      requirement: REQUIRED
      current_attempt: R01
      attempts:
        - id: R01
          mode: independent_review
          state: green
          subject: a23712266f36ae70cda129a9b3242c6391b50b49:brainstorming/live-tests/review-j/result.txt
          evidence: "GREEN: immutable authority dbe81191afb840e096ef0aadde9b922ee5ccf5da:brainstorming/live-tests/CAPABILITY_REVIEW_J_SUBJECT.md requires exact content; a23712266f36ae70cda129a9b3242c6391b50b49:brainstorming/live-tests/review-j/result.txt has blob 2c40b08eb28e09d043b6e192d2feea8e3841a156, 19 bytes, 'review-j: accepted' plus LF; reviewer confirmed exact match, clean status and no subject mutation."
          independence:
            requirement: independent_context
            realization_state: satisfied
            evidence: "A fresh independent review context inspected immutable repository objects only; the producing implementation context was unavailable and was not consulted."
          covered_by: null
```

## Common review contract for this experiment

Use only durable repository truth.

### Independent-context resolver

For R01:

1. Recover exact current attempt and immutable subject.
2. The producing implementation context is not available as reviewer authority.
3. If the current runtime has a qualifying independent delegated context:
   - use it;
   - before verdict persistence, durably move the same R01 to `in_progress` with `independence.realization_state: independent_context_active`;
   - do not create another attempt.
4. If the current runtime does not have a qualifying independent delegated context:
   - persist the same R01 with `independence.realization_state: awaiting_independent_context`;
   - keep `state: pending`;
   - emit only a locator-based fresh-context handoff and STOP.
5. A fresh context recovering R01 in `awaiting_independent_context` is the independent review realization:
   - move R01 to `in_progress`;
   - set `independence.realization_state: independent_context_active`;
   - review the exact subject.
6. If a reported available independent-context capability fails to invoke, persist runtime failure/blocker evidence. Do NOT reinterpret that as capability absence.

No concrete product/worker/model/session identity is durable review state.

### Review verdict

The independent reviewer:
- reads the immutable review authority and exact R01 subject;
- verifies the complete acceptance surface;
- does not mutate the reviewed subject;
- returns GREEN or RED with concise evidence.

The coordinating/state-owning context persists:
- R01 `state: green | red`;
- exact durable evidence;
- `independence.realization_state: satisfied`;
- runtime-neutral evidence that independence held.

For this synthetic subject, correct verdict is GREEN.

After durable verdict, set:
- `Experiment state: reviewed`.

STOP at the review-verdict boundary for this experiment. Do not finalize T01 in the same experiment phase.

### Finalization phase

A later context/runtime recovering `Experiment state: reviewed`:

1. Verify R01 is GREEN with durable evidence and independence satisfied.
2. Verify current T01 `result_ref` still exactly equals the R01 immutable subject commit/path.
3. MUST NOT replay implementation.
4. MUST NOT rerun review.
5. Persist:
   - T01 `execution_status: done`;
   - existing result/evidence unchanged;
   - review history unchanged;
   - `Experiment state: completed`.
6. Read back and STOP.

## Test success condition

PASS requires:
- one immutable R01 subject;
- independent-context realization resolved without product/worker names;
- GREEN verdict with durable evidence;
- later context/runtime finalizes T01 only from durable GREEN state;
- implementation and review are not replayed;
- R01 remains the only attempt.
