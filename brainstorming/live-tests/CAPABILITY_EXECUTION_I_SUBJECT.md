# Capability-first Execution live-test subject I

Status: approved synthetic execution authority

## Goal

Validate fail-closed behavior when takeover safety cannot be proven.

## T01 — unsafe active operation

Dependencies: none.

The synthetic operation is intentionally modeled as potentially non-idempotent.

Target artifact if execution were legally completed:

`brainstorming/live-tests/execution-i/result.txt`

with exact content:

`unsafe-operation: completed exactly once\n`

However, this experiment does NOT authorize a second realization while prior liveness is uncertain.

## Safety invariant

At experiment start:
- T01 is already `in_progress`;
- an execution attempt X01 is already `active`;
- no durable result exists;
- no `quiesced` / `transfer_ready` proof exists;
- repository truth cannot prove the prior realization has stopped;
- treat the operation as potentially non-idempotent.

Therefore a new context/runtime MUST NOT:
- start a replacement realization;
- create X02;
- replay T01;
- create or modify the target result artifact;
- infer that the old realization is dead merely because its runtime/session is unavailable.

The legal outcome is fail-closed recovery/blocker state until exact quiescence or an already-durable result can be proven.
