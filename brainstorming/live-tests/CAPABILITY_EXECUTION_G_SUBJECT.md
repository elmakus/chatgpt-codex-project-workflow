# Capability-first Execution live-test subject G

Status: approved synthetic execution authority

## Goal

Validate cross-runtime takeover of one non-terminal Card at a durable quiescent checkpoint.

## T01 — Checkpointed result

Dependencies: none.

The Card has two bounded implementation units.

### Unit A — durable prefix

Create or replace:

`brainstorming/live-tests/execution-g/part1.txt`

with exact content:

`part1: durable checkpoint prefix\n`

Unit A is independently verifiable but does NOT complete T01.

### Unit B — completion suffix

After accepted Unit A exists, create or replace:

`brainstorming/live-tests/execution-g/part2.txt`

with exact content:

`part2: resumed after checkpoint\n`

## T01 acceptance

T01 is done only when:
- part1.txt has the exact Unit-A content;
- part2.txt has the exact Unit-B content;
- Unit A remains unchanged while Unit B is completed;
- exact durable result/evidence is recorded.

## Portability invariants

- T01 remains `in_progress` across the runtime switch.
- A transfer checkpoint is legal only after the old realization is quiescent: no old realization may continue mutating this Card after `transfer_ready` is persisted.
- Durable Unit-A work must not be replayed merely because another runtime takes over.
- The same project execution attempt continues across the switch; concrete runtime/session identity is not Project Workflow state.
- No product, worker, model, session, invocation, lane or worktree identity is required.
- This synthetic test has repository-local writes only and no detached worker or external side effect.
