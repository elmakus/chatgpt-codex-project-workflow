# MXX — <milestone title>

Plan revision: `<R#>`

> This file is the milestone **contract**, not live state. Current decision/execution status, checkpoint, implementation head, handoff and acceptance-evidence pointers live in `implementation/TASK_BOARD.yaml`.

## Outcome

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
