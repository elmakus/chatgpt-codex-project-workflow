# Live Execution obligation — F

Experiment: completed-Card cross-runtime takeover
Execution state: active
Execution subject: 6e580867cc3090ef59efbede19d8e6fb17cb8c31:brainstorming/live-tests/CAPABILITY_EXECUTION_F_SUBJECT.md
Active execution: null
Execution evidence: none

## Synthetic Task Board

```yaml
cards:
  - id: T01
    execution_status: ready
    depends_on: []
    result_ref: null
    evidence: null

  - id: T02
    execution_status: planned
    depends_on: [T01]
    result_ref: null
    evidence: null
```

## Common execution contract for this experiment

Use only durable repository truth.

### Selecting work

- recover any non-null `Active execution` before selecting new work;
- otherwise choose the first legal READY Card;
- do not infer execution behavior from product identity;
- do not persist product, worker, model, session, invocation, lane or worktree identity.

### Starting one Card

Before performing the Card's repository mutation:
1. durably set that Card to `in_progress`;
2. durably set `Active execution` to:
   ```yaml
   id: <next Xnn>
   state: active
   member:
     card_id: <Txx>
     state: active
     result_ref: null
   ```
3. read back the durable start state.

This test is serial because only one Card is dependency-legal at each boundary. The one-member active-execution wrapper is intentional.

### Completing one Card

1. execute only the exact Card contract from the immutable subject;
2. verify its acceptance;
3. create an exact durable Git result commit containing the Card output;
4. persist in this record:
   - Card `execution_status: done`;
   - exact `result_ref`;
   - concise evidence;
   - `Active execution: null`;
5. recompute readiness from project dependencies:
   - a planned Card whose dependencies are now done and whose other prerequisites are satisfied becomes `ready`;
6. read back the durable result/state;
7. STOP at this completed-Card boundary. Do not start the next Card in the same context.

### Recovery / takeover invariant

A later context recovering this record:
- MUST NOT rerun or rewrite a Card already `done` with a verified durable result;
- MUST consume accepted dependency results from repository truth;
- may select the next READY Card regardless of which runtime completed the prior Card;
- if `Active execution` is non-null, recover that exact active obligation before selecting new work.

## Test phases

### Phase 1

Initial state is T01 READY, T02 planned.

PASS requires one context to execute T01 only, persist its exact result, make T02 READY, clear Active execution, and STOP.

### Phase 2

A different context/runtime opens this same durable record.

PASS requires it to:
- recognize T01 as terminal and not replay/rewrite it;
- execute T02 only;
- persist T02 terminal result;
- leave both Cards done and Active execution null;
- preserve T01 exact artifact/result unchanged.

## Final success condition

The experiment passes only if two contexts/runtimes can cross the completed-Card boundary using this one runtime-neutral durable state without a product-specific conversion or handoff schema.
