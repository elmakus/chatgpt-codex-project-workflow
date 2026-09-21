# Live authoritative-state refresh obligation — L

Experiment: pre-routing authoritative-state refresh
Experiment state: stale_phase_pending
Harness authority: c427bafb31c3f6c79544be3a89300b02503aa7f9:brainstorming/live-tests/ISOLATED_COMMON_CONTRACT_HARNESS.md
Authoritative repository: elmakus/chatgpt-codex-project-workflow
Authoritative branch: feat/common-preexecution-core
Result path: brainstorming/live-tests/refresh-l/result.txt

## Purpose

Validate that routing in a new context/takeover/recovery is selected only after refreshing the exact authoritative branch/ref, not from an intentionally stale local checkout.

This version is the deliberate stale snapshot for the later probe.

## Current synthetic routing state

```yaml
pending_obligation:
  id: L-STALE
  state: pending
  action: write_stale_marker
```

## Phase L-STALE — deliberately stale obligation

If and only if this exact snapshot were still authoritative, the legal action would be:

1. replace `brainstorming/live-tests/refresh-l/result.txt` with exact content `L: STALE\n`;
2. persist `Experiment state: completed_stale`;
3. record concise evidence;
4. STOP.

No other file is authorized to change in this phase except this record and the result fixture.

## Correctness property under test

A later authoritative commit will supersede this routing state with a different obligation.

The actual test runner will begin from a local checkout intentionally pinned to this stale snapshot while the remote authoritative branch has already advanced.

A correct runner must refresh the authoritative branch before selecting a phase. Therefore it must not execute L-STALE when this snapshot is no longer current.

## Test failure signal

The test fails if the runner:
- executes `write_stale_marker` from this stale snapshot;
- attempts to publish the stale phase and relies on push/CAS rejection to discover newer state;
- routes before establishing the current authoritative head.

The later authoritative version of this record owns the real test completion criteria.
