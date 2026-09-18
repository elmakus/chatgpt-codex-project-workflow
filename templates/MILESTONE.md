# MXX — <milestone title>

Plan revision: `<R#>`

> Create this file only when the approved Master Plan milestone section is insufficient for deterministic execution/integrated acceptance. It extends that milestone **contract**; it must not merely duplicate or weaken it. Current decision/execution status, checkpoint, implementation head, handoff and acceptance-evidence pointers live in `implementation/TASK_BOARD.yaml`.

## Authority inherited

- Master Plan milestone section: `<planning/MASTER_PLAN.md#...>`
- Requirements / accepted decisions: `<exact IDs/paths>`

## Additional must-preserve constraints / rationale

Only detail that materially extends the approved plan.

...

## Outcome

Only restate when the JIT contract materially sharpens the approved milestone outcome.

...

## Requirements owned

- `REQ-...`

## Dependencies

...

## Planned Task Cards

- `MXX-T01`
- `MXX-T02`

## Boundary gates / user authorization

`none` or exact strategic/deployment/live-write/user gate that must stop automatic continuation.

If `none`, fixed-policy execution may continue automatically to the next already-approved milestone after this milestone is GREEN.

## Integrated acceptance contract

...

## Corrective-work rule

If integrated acceptance is RED, do not mark milestone done in Task Board. Reopen/create bounded corrective work and persist failing evidence.

## Close contract

Task Board milestone may become `done` only when:
- all required cards are done;
- integrated acceptance is GREEN;
- final publication/merge state is resolved;
- exact checkpoint and `implementation_head` are known;
- durable acceptance evidence exists;
- cumulative handoff exists.
