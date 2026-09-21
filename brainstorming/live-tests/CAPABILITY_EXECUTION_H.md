# Live Execution obligation — H

Experiment: concurrent execution-set takeover
Experiment state: completed
Execution subject: 3f18dd1483dc5bb4cd42257c47bf0187d55f9c14:brainstorming/live-tests/CAPABILITY_EXECUTION_H_SUBJECT.md
Execution evidence: T01 and T02/B1 ran concurrently in separate isolated mutable contexts; both returned exact accepted artifacts, were reconciled in order, and all old member realizations ended before transfer. Phase 2 resumed the same X01 from the durable B1 checkpoint, executed B2 only, preserved T01 and B-prefix byte-for-byte, and closed X01.

## Synthetic Task Board

```yaml
cards:
  - id: T01
    execution_status: done
    depends_on: []
    result_ref: 2a48259a9e1bbb3086581f3d88bc169eb9fba8c5
    evidence: Exact A.txt content verified after isolated concurrent realization and canonical reconciliation.

  - id: T02
    execution_status: done
    depends_on: []
    result_ref: f3630798b7bfb2002efc57e3d7051123d834c4dc
    evidence: Continued X01 from exact B1 checkpoint 1ee12e95ca96fc08a4ed5719d036e3c5f32ec525; executed B2 only; exact B.txt verified; A.txt and B-prefix.txt verified unchanged.

  - id: T03
    execution_status: ready
    depends_on: [T01, T02]
    result_ref: null
    evidence: Readiness recomputed after T01 and T02 became terminal; T03 implementation was not executed.
```

## Active execution

```yaml
null
```

## Common execution contract for this experiment

Use only durable repository truth.

### Phase 1 — concurrent realization and transfer checkpoint

This phase specifically tests concurrent realization.

1. Verify T01 and T02 are both READY from project legality.
2. Verify the current runtime can actually provide qualifying concurrent isolated mutable realization for both members.
   - If not, do not fake concurrency and do not run them serially merely to obtain the expected end state.
   - Persist `Experiment state: not_exercised` with concise evidence and STOP.
3. Before launching either member, durably persist:
   - T01 `in_progress`;
   - T02 `in_progress`;
   - Active execution:
     ```yaml
     id: X01
     state: active
     base_ref: <exact current durable branch head before member work>
     reconciliation_order: [T01, T02]
     members:
       - card_id: T01
         state: active
         canonical_result_ref: null
       - card_id: T02
         state: active
         checkpoint_ref: null
         canonical_result_ref: null
     ```
4. Read back the durable start state.
5. Actually realize the following concurrently in isolated mutable execution contexts/workspaces:
   - member T01: execute full T01;
   - member T02: execute **Unit B1 only**, then return/stop without B2.
6. The shared coordinator verifies both returned outputs against the immutable subject.
7. Reconcile returned outputs into the canonical workstream branch without allowing either member realization to mutate the shared Task Board/record directly.
8. Persist T01 as terminal:
   - `execution_status: done`;
   - exact canonical result ref;
   - concise evidence.
9. Keep T02 non-terminal:
   - `execution_status: in_progress`;
   - exact durable B1 checkpoint ref;
   - no final result ref.
10. Establish transfer safety:
    - no old T01 realization remains capable of mutation;
    - no old T02 realization remains capable of mutation;
    - no member runtime operation remains active for X01.
11. Durably persist:
    ```yaml
    Active execution:
      id: X01
      state: transfer_ready
      base_ref: <preserved base>
      reconciliation_order: [T01, T02]
      members:
        - card_id: T01
          state: reconciled
          canonical_result_ref: <exact T01 canonical result>
        - card_id: T02
          state: quiesced
          checkpoint_ref: <exact canonical B1 checkpoint>
          canonical_result_ref: null
    ```
12. T03 must remain `planned` because T02 is not done.
13. Persist concise evidence that actual concurrent realization was used and that all old member realizations are quiescent. Do not persist concrete worker/session/worktree identifiers.
14. Read back the durable transfer state.
15. STOP. Do not execute B2 or T03.

### Phase 2 — serial continuation of the same execution set

A later context/runtime recovering this exact record:

1. If `Experiment state: not_exercised`, STOP; do not reinterpret it as a successful concurrency test.
2. Require:
   - T01 `done` with exact durable canonical result;
   - T02 `in_progress`;
   - T03 `planned`;
   - X01 `transfer_ready`;
   - T01 member `reconciled`;
   - T02 member `quiesced` with exact checkpoint.
3. Verify T01 artifact/result and T02 B1 checkpoint against the immutable subject.
4. MUST NOT rerun/rewrite T01.
5. MUST NOT rewrite/replay T02 Unit B1.
6. Continue the same project attempt X01. Do not create X02 merely because the runtime/context changed.
7. Durably transition X01 back to `active` while preserving:
   - base_ref;
   - reconciliation_order;
   - T01 as `reconciled`;
   - T02 as `active`;
   - T02 checkpoint ref.
8. Read back the resumed state.
9. Execute **T02 Unit B2 only**. Serial execution is legal even though Phase 1 used concurrency.
10. Verify full T02 acceptance and that T01 + B-prefix are unchanged.
11. Persist T02:
    - `execution_status: done`;
    - exact canonical result ref;
    - evidence.
12. Recompute readiness:
    - T03 becomes `ready`.
13. Close X01:
    - persist its completed member facts if needed for evidence;
    - then set `Active execution: null`.
14. Set `Experiment state: completed`.
15. Read back durable final state and STOP. Do not execute T03.

### Unsafe takeover rule

If any old member realization may still be live, or quiescence cannot be proven, Phase 2 MUST NOT continue T02. Preserve/fail closed instead of creating a duplicate realization.

## Test success condition

PASS requires:
- Phase 1 actually uses concurrent isolated realization for T01 and T02/B1;
- both were marked in_progress before member work began;
- T01 becomes durable `done` and is preserved;
- T02 remains `in_progress` at a durable quiescent B1 checkpoint;
- X01 becomes `transfer_ready`;
- Phase 2 preserves and continues the same X01;
- Phase 2 does not replay T01 or B1;
- Phase 2 may continue T02 serially;
- after T02 becomes done, T03 becomes READY;
- Active execution is null at the final boundary;
- no product-specific conversion schema or concrete runtime identity is introduced.

This test validates bounded concurrent-set takeover after all old member realizations have reached a quiescent durable boundary. It does not validate forced cancellation of a still-running worker or non-idempotent external-write takeover.
