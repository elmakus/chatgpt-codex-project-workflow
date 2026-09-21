# Capability-first Execution live-test subject F

Status: approved synthetic execution authority

## Goal

Validate cross-runtime takeover at a completed Card boundary without product-specific execution provenance.

## Synthetic work

### T01 — Produce A

Dependencies: none.

Execution:
- create or replace `brainstorming/live-tests/execution-f/A.txt`;
- exact content: `A: durable result from T01\n`.

Acceptance:
- file exists with exact content;
- exact result commit is durable;
- Card state is `done`.

### T02 — Produce B from accepted T01

Dependencies:
- T01 must be `done`;
- T01 exact result must be durable.

Execution:
- read accepted durable T01 result;
- create or replace `brainstorming/live-tests/execution-f/B.txt`;
- exact content: `B: continued from accepted T01\n`.

Acceptance:
- T01 is not re-executed or rewritten;
- B exists with exact content;
- exact result commit is durable;
- T02 becomes `done`.

## Portability invariants

- runtime/product identity is not part of Card completion semantics;
- a terminal durable T01 result must never be replayed merely because another runtime takes over;
- after T01 is done and T02 becomes READY, another runtime may continue directly from repository truth;
- this test stops at every completed Card boundary;
- no independent review is required for these synthetic Cards;
- no external writes exist outside this repository.
