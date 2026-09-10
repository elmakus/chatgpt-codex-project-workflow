# MXX — <milestone title>

- Decision state: `accepted | deferred | rejected | review`
- Execution status: `planned | ready | in_progress | blocked | done | superseded`
- Plan revision: `<R#>`
- Checkpoint: `<name | pending>`
- Implementation head: `<sha | pending>`
- Acceptance evidence: `<implementation/evidence/MXX_ACCEPTANCE.md | pending>`
- Cumulative handoff: `<project-handoffs/MXX_HANDOFF.md | pending>`

## Outcome

...

## Requirements owned

- `REQ-...`

## Dependencies

...

## Planned Task Cards

- `MXX-T01`
- `MXX-T02`

## Integrated acceptance

...

## Corrective-work rule

If integrated acceptance is RED, do not mark the milestone done. Reopen/create bounded corrective work and persist failing evidence.

## Close criteria

Milestone `done` requires:
- all required cards done;
- integrated acceptance GREEN;
- final publication/merge state resolved;
- checkpoint and exact `implementation_head`;
- durable acceptance evidence;
- cumulative handoff.
