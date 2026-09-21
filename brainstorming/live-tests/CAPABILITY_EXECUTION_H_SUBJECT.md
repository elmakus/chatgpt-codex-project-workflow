# Capability-first Execution live-test subject H

Status: approved synthetic execution authority

## Goal

Validate transfer of one durable multi-member execution set from a concurrency-capable runtime to a runtime that may continue the unresolved member serially.

## Cards

### T01 — Parallel member A

Dependencies: none.

Create or replace:

`brainstorming/live-tests/execution-h/A.txt`

with exact content:

`A: completed concurrent member\n`

Acceptance:
- exact content exists;
- exact canonical durable result is recorded;
- T01 is `done`.

### T02 — Checkpointed parallel member B

Dependencies: none.

T02 has two bounded units.

#### Unit B1 — transferable checkpoint

Create or replace:

`brainstorming/live-tests/execution-h/B-prefix.txt`

with exact content:

`B-prefix: concurrent checkpoint\n`

B1 is independently verifiable but does not complete T02.

#### Unit B2 — completion after takeover

After accepted B1 exists, create or replace:

`brainstorming/live-tests/execution-h/B.txt`

with exact content:

`B: completed after concurrent takeover\n`

Acceptance:
- B-prefix.txt remains byte-for-byte unchanged;
- B.txt has exact required content;
- exact canonical durable result is recorded;
- T02 is `done`.

### T03 — downstream readiness witness

Dependencies: T01 and T02.

No implementation is performed for T03 in this experiment.

Acceptance for this experiment:
- T03 remains non-READY while either dependency is non-terminal;
- T03 becomes `ready` after T01 and T02 are both `done`.

## Portability invariants

- T01 and T02 are both project-legal at Phase-1 start.
- Phase 1 must actually realize T01 and T02/B1 concurrently through qualifying isolated mutable execution contexts/workspaces. Do not claim concurrency if it was not actually used.
- Project Workflow state must not persist concrete worker/model/session/invocation/worktree identity.
- The shared coordinating context is the only writer of the common durable execution record.
- T01 may become terminal while T02 remains non-terminal inside the same execution set.
- Transfer is legal only after every unresolved old realization is quiescent.
- A later runtime may continue remaining members serially; it must not replay terminal/reconciled members.
- The same project execution attempt X01 survives the runtime switch.
- This synthetic test has repository-local writes only and no external side effect.
