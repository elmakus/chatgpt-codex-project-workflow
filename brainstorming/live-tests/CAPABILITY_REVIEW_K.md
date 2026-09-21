# Live Review obligation — K

Experiment: RED correction append-only recheck
Experiment state: pending_r01
Review authority: 569a439b3ffa75a8fa7d0fd6947e89d4bde1d0cd:brainstorming/live-tests/CAPABILITY_REVIEW_K_SUBJECT.md
Active execution: null

## Synthetic Task Board

```yaml
cards:
  - id: T01
    execution_status: in_progress
    result_ref: f72d08ae5d4aa8faf06dcedb586bc1618887200c
    evidence: S1 durable; intentionally defective

    review:
      requirement: REQUIRED
      current_attempt: R01
      attempts:
        - id: R01
          mode: independent_review
          state: in_progress
          subject: f72d08ae5d4aa8faf06dcedb586bc1618887200c:brainstorming/live-tests/review-k/result.txt
          evidence: null
          independence:
            requirement: independent_context
            realization_state: independent_context_active
            evidence: "Fresh independent delegated Tester context invoked; read-only review of exact R01/S1 subject."
          covered_by: null
```

## Common review contract for this experiment

Use only durable repository truth.

### Phase 1 — independent R01 review of S1

Resolve independent context using the same capability-first lifecycle as test J:
- qualifying delegated independent context when available;
- otherwise `awaiting_independent_context` + fresh-context STOP;
- receiving fresh context becomes `independent_context_active`;
- invocation failure is not capability absence.

Review exact R01/S1 without mutation.

Because S1 violates the accepted requirement, correct verdict is RED.

Persist:
- R01 `state: red`;
- exact evidence identifying the S1 defect;
- R01 independence `realization_state: satisfied`;
- preserve exact immutable S1 subject;
- `Experiment state: r01_red`.

STOP at this experiment boundary. Do not correct S1 while still acting as reviewer.

### Phase 2 — bounded correction and R02 freeze

A later correction context recovering `r01_red`:

1. Verify R01 remains exact RED for S1.
2. Apply only the authorized bounded correction:
   - change `brainstorming/live-tests/review-k/result.txt`
   - exact content becomes `review-k: GOOD\n`.
3. Create exact durable canonical correction commit S2.
4. Update T01 `result_ref` to exact S2.
5. MUST NOT mutate R01 subject/state/evidence.
6. Append a new attempt:

```yaml
- id: R02
  mode: independent_review
  state: pending
  subject: <S2 commit>:brainstorming/live-tests/review-k/result.txt
  evidence: null
  independence:
    requirement: independent_context
    realization_state: resolve_independent_context
    evidence: null
  covered_by: null
```

7. Set `current_attempt: R02`.
8. Set `Experiment state: pending_r02`.
9. STOP.

The correction-producing context MUST NOT itself issue the R02 verdict. This experiment intentionally stops after R02 freeze so the append-only boundary is directly observable.

### Phase 3 — independent R02 recheck

A later context/runtime recovering `pending_r02`:

1. Verify:
   - R01 is immutable RED for S1;
   - R02 is pending for exact S2;
   - current T01 result equals S2.
2. Resolve independent context for R02 capability-first.
3. Reviewer must be independent from the realization/context that produced S2.
4. Review exact S2 without mutation.
5. Correct verdict is GREEN.
6. Persist:
   - R02 `state: green`;
   - durable evidence;
   - R02 independence `realization_state: satisfied`;
   - R01 unchanged;
   - `Experiment state: completed`.
7. STOP.

T01 remains non-terminal in this test; deterministic post-review finalization is already covered by J.

## Test success condition

PASS requires:
- R01 RED for exact S1;
- bounded correction creates distinct S2;
- R01 remains immutable and addressable;
- R02 is appended rather than replacing R01;
- correction-producing context does not self-review S2;
- independent R02 GREEN;
- both attempts remain durable;
- no product/worker identity is required review state.
