# Live Review obligation — K

Experiment: RED correction append-only recheck
Experiment state: completed
Review authority: 569a439b3ffa75a8fa7d0fd6947e89d4bde1d0cd:brainstorming/live-tests/CAPABILITY_REVIEW_K_SUBJECT.md
Active execution: null

## Synthetic Task Board

```yaml
cards:
  - id: T01
    execution_status: in_progress
    result_ref: 073f6d569c44d609de5eee3bf2bf1e550ca74938
    evidence: S1 durable; intentionally defective

    review:
      requirement: REQUIRED
      current_attempt: R02
      attempts:
        - id: R01
          mode: independent_review
          state: red
          subject: f72d08ae5d4aa8faf06dcedb586bc1618887200c:brainstorming/live-tests/review-k/result.txt
          evidence: "RED: authority 569a439b3ffa75a8fa7d0fd6947e89d4bde1d0cd requires exact 15-byte 'review-k: GOOD' plus LF; S1 f72d08ae5d4aa8faf06dcedb586bc1618887200c:brainstorming/live-tests/review-k/result.txt has blob 8d96510edd2bc4958b989e6c3b78c839ae057d28, 14 bytes 'review-k: BAD' plus LF (hex 72 65 76 69 65 77 2d 6b 3a 20 42 41 44 0a); content mismatch, no subject mutation."
          independence:
            requirement: independent_context
            realization_state: satisfied
            evidence: "Fresh distinct read-only review context completed R01; reviewer did not produce S1 and inspected immutable objects only. Delegation trail: initial delegated invocation interrupted by connection loss; exact resume returned session_busy; replacement same-workspace invocation returned session_busy; review completed in fresh isolated workspace."
          covered_by: null
        - id: R02
          mode: independent_review
          state: green
          subject: 073f6d569c44d609de5eee3bf2bf1e550ca74938:brainstorming/live-tests/review-k/result.txt
          evidence: "GREEN: authority 569a439b3ffa75a8fa7d0fd6947e89d4bde1d0cd requires exact 15-byte 'review-k: GOOD' plus LF; S2 073f6d569c44d609de5eee3bf2bf1e550ca74938:brainstorming/live-tests/review-k/result.txt has blob 8f32fdb2d2ea509a8100b786c82ad28148c6cbaa, 15 bytes (hex 72 65 76 69 65 77 2d 6b 3a 20 47 4f 4f 44 0a); exact match, T01 result_ref equals S2, R01 RED block unchanged, clean tree, no subject mutation."
          independence:
            requirement: independent_context
            realization_state: satisfied
            evidence: "Fresh distinct read-only tester CAP-REVIEW-K-R02 (session 57c1fd08-f79a-44f0-9ad6-8fe69296387f, invocation 8263b14b-5c71-4279-a436-83a30bfbb942) reviewed exact S2 without mutation; tester did not produce S2 and inspected immutable objects only under a no-Git-write role; this record persists that verified verdict."
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
