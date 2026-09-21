# Live Execution obligation — G

Experiment: active-Card cross-runtime checkpoint takeover
Execution subject: 82cac004ad0c47e4d94e766aaabf604d84e2f748:brainstorming/live-tests/CAPABILITY_EXECUTION_G_SUBJECT.md
Execution evidence: Unit A matches the immutable subject byte-for-byte at commit `9625b8de23914975acc09e8a3549332c46c16287`; no delegated or detached realization was used; X01 is quiesced for transfer.

## Synthetic Task Board

```yaml
cards:
  - id: T01
    execution_status: in_progress
    depends_on: []
    result_ref: null
    evidence: null
```

## Active execution

```yaml
id: X01
state: active
member:
  card_id: T01
  state: active
  checkpoint_ref: 9625b8de23914975acc09e8a3549332c46c16287
  result_ref: null
```

## Common execution contract for this experiment

Use only durable repository truth.

### Phase 1 — establish transfer checkpoint

From the initial state:

1. select T01 and durably persist:
   - `execution_status: in_progress`;
   - Active execution:
     ```yaml
     id: X01
     state: active
     member:
       card_id: T01
       state: active
       checkpoint_ref: null
       result_ref: null
     ```
2. read back the durable start state;
3. execute **Unit A only** from the immutable subject;
4. verify Unit A and persist its exact durable Git commit as `checkpoint_ref`;
5. establish quiescence for this synthetic execution:
   - no delegated/detached realization remains active;
   - no operation for T01 may continue after this context yields;
6. durably transition:
   ```yaml
   Active execution:
     id: X01
     state: transfer_ready
     member:
       card_id: T01
       state: quiesced
       checkpoint_ref: <exact Unit-A commit>
       result_ref: null
   ```
7. keep T01 `in_progress`;
8. persist concise checkpoint evidence;
9. read back the durable checkpoint;
10. STOP. Do not execute Unit B.

The context that establishes `transfer_ready` MUST stop and MUST NOT complete T01.

### Phase 2 — resume from checkpoint

A later context recovering this exact record:

1. if Active execution is `transfer_ready` and the member is `quiesced`, verify:
   - T01 is still `in_progress`;
   - exact `checkpoint_ref` exists;
   - Unit A matches the immutable subject;
2. MUST NOT rewrite/replay Unit A;
3. continue the same project execution attempt `X01`; do not create a new execution attempt merely because runtime/context changed;
4. before Unit B, durably transition:
   ```yaml
   Active execution:
     id: X01
     state: active
     member:
       card_id: T01
       state: active
       checkpoint_ref: <preserved Unit-A commit>
       result_ref: null
   ```
5. read back resumed active state;
6. execute **Unit B only**;
7. verify full T01 acceptance and that Unit A remained unchanged;
8. create the exact durable final result commit;
9. persist:
   - T01 `execution_status: done`;
   - exact T01 `result_ref`;
   - concise evidence;
   - `Active execution: null`;
10. read back final durable state;
11. STOP at the completed-Card boundary.

### Unsafe state rule

If Active execution is `active` rather than `transfer_ready`, or quiescence cannot be proven, another context MUST NOT start/restart T01 from that state. It must recover/fail closed rather than duplicate an uncertain live realization.

## Test success condition

PASS requires:
- first context performs only Unit A and stops with T01 still `in_progress`;
- durable state is `X01 transfer_ready / T01 quiesced` with exact checkpoint ref;
- second context preserves Unit A and executes only Unit B;
- the same project attempt X01 survives the runtime/context switch;
- T01 ends `done` with exact result/evidence and no active execution;
- no product-specific conversion state is introduced.

This test validates a repository-local quiescent active-Card transfer. It does not validate detached-worker cancellation or external-side-effect takeover.
