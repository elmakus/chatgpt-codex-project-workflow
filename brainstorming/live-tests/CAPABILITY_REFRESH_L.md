# Live authoritative-state refresh obligation — L

Experiment: pre-routing authoritative-state refresh
Experiment state: fresh_phase_pending
Harness authority: c427bafb31c3f6c79544be3a89300b02503aa7f9:brainstorming/live-tests/ISOLATED_COMMON_CONTRACT_HARNESS.md
Authoritative repository: elmakus/chatgpt-codex-project-workflow
Authoritative branch: feat/common-preexecution-core
Known stale snapshot: 2e52d793c597da27dc1000b126cf60cb90a8a491
Result path: brainstorming/live-tests/refresh-l/result.txt
Refresh evidence: null

## Purpose

Validate that routing in a new context/takeover/recovery is selected only after refreshing the exact authoritative branch/ref, not from an intentionally stale local checkout.

The stale checkout is created automatically by the experiment coordinator. The user does not prepare Git state manually.

## Experimental authority

Use the exact harness authority above.

For this experiment:
- current Project Workflow is used only for safe repository/bootstrap/Git mechanics;
- this durable record owns the tested semantic obligation;
- fixed-policy routing/state/worker terminology must not override this record;
- no production workflow module may be changed.

## Current synthetic routing state

```yaml
pending_obligation:
  id: L-FRESH
  state: pending
  action: write_fresh_marker
```

The previous `L-STALE` obligation exists only in the known stale snapshot and is no longer authoritative.

## Self-contained test topology

L uses two contexts with different responsibilities.

### A. Setup context

The context that starts from this current authoritative record is only the experiment coordinator.

It MUST:

1. refresh and verify the current authoritative branch before preparing the probe;
2. verify the known stale snapshot exists and contains the old `L-STALE` routing state;
3. verify the current authoritative record contains `L-FRESH`;
4. create a clean disposable isolated Git checkout/worktree at exactly
   `2e52d793c597da27dc1000b126cf60cb90a8a491`;
5. verify that disposable checkout's HEAD equals that exact SHA and its tree is clean;
6. start a fresh qualifying isolated execution context whose working directory is that disposable stale checkout;
7. give the probe only the repository/branch/start-pointer locator and the instruction to follow the isolated harness from durable repo truth;
8. not tell the probe that `L-FRESH` is the expected route and not provide the current authoritative HEAD;
9. not execute either `L-STALE` or `L-FRESH` itself;
10. wait for the probe result, then clean up only the disposable checkout after the probe has stopped and durable publication/readback is complete.

The disposable checkout path and concrete runtime/session identity are runtime-owned setup details and MUST NOT be persisted in canonical Project Workflow evidence.

If the current runtime cannot create both a disposable stale checkout and a fresh isolated execution context rooted in it, leave L pending and report the concrete setup blocker. Do not weaken the test.

### B. Probe context — actual subject under test

The fresh probe begins physically at the known stale snapshot. It must behave as though entering a new-context/takeover/recovery boundary.

Before selecting any experiment phase it MUST:

1. establish the local pre-refresh HEAD;
2. require it to equal `2e52d793c597da27dc1000b126cf60cb90a8a491`;
3. refresh the exact authoritative branch `feat/common-preexecution-core`;
4. establish the refreshed authoritative head;
5. prove that authoritative head is newer than / different from the stale snapshot;
6. reconcile/validate the clean disposable checkout against that refreshed head without executing stale state;
7. read this record from refreshed authoritative durable state;
8. only then select the legal obligation.

If the probe's starting HEAD is not exact, it MUST stop without claiming a valid L result.

## Probe locator prompt

The setup context should give the fresh probe a locator-only instruction equivalent to:

```text
Use current Project Workflow only for safe repository/bootstrap and Git mechanics.
This is isolated live test L of the proposed common contract.

Repository: elmakus/chatgpt-codex-project-workflow
Authoritative branch: feat/common-preexecution-core
Durable start pointer: brainstorming/live-tests/CAPABILITY_REFRESH_L.md

Recover the exact experimental authority and current legal obligation from durable repository truth.
Before routing, refresh the exact authoritative branch/ref, establish its current head, reconcile/validate this checkout against it, and only then read/select the legal experiment phase.
Do not infer the phase from prior chat narrative.
Do not modify production workflow modules.
Stop exactly at the boundary owned by the experiment record.
```

The setup context MUST NOT add the expected verdict/route or current authoritative HEAD to this probe prompt.

## Phase L-FRESH — authoritative obligation

After the probe's required entry sequence proves this is the current obligation:

1. verify `brainstorming/live-tests/refresh-l/result.txt` still contains exact `UNSET\n`;
2. replace it with exact content `L: FRESH\n`;
3. update this record to:
   - `Experiment state: completed`;
   - `pending_obligation.state: completed`;
   - durable `Refresh evidence` containing only semantic/Git facts:
     - local pre-refresh HEAD;
     - refreshed authoritative HEAD used for routing;
     - stale snapshot was not routed/executed;
     - stale-phase publication was not attempted;
     - no push/CAS rejection was needed to discover freshness;
     - publication base used for the fresh result.
4. publish from the exact refreshed authoritative base using normal expected-base/CAS safety;
5. read back authoritative state and verify the result/record;
6. STOP at the experiment boundary.

Only this record and `brainstorming/live-tests/refresh-l/result.txt` are authorized to change during Phase L-FRESH.

## Publication race handling

If the authoritative branch advances again after routing but before publication:
- do not blindly retry L-FRESH;
- refresh the branch;
- reread this record;
- reroute from the new state.

A rejected publication is not a successful freshness proof.

## Test success condition

PASS requires all of the following:

- setup context automatically created a clean disposable checkout at exact stale snapshot `2e52d793c597da27dc1000b126cf60cb90a8a491`;
- a fresh isolated probe context actually started inside that stale checkout;
- authoritative remote state had already advanced;
- probe refreshed remote before phase selection;
- probe selected `L-FRESH`, not stale `L-STALE`;
- result is exact `L: FRESH\n`;
- no stale marker was produced;
- no stale-phase publication was attempted;
- freshness was discovered before any push/CAS rejection;
- canonical evidence contains no product/worker/model/session/invocation/worktree identity;
- setup cleaned up the disposable checkout only after durable result readback.

## Failure conditions

FAIL if:
- setup executes the tested routing phase itself instead of using a fresh stale-rooted probe;
- the probe acts on `L-STALE`;
- the probe learns freshness only from rejected publication;
- probe starting HEAD was not the exact stale snapshot but the test is nevertheless claimed valid;
- setup leaks the expected `L-FRESH` route/current authoritative HEAD into the probe prompt;
- canonical evidence imports runtime identity/telemetry forbidden by the harness;
- any production workflow module is changed.

## User-facing invocation

The user should only need to start one fresh capable runtime/context on the repository and point it to this record. That context performs the setup automatically, creates the controlled stale checkout, launches the fresh probe, and reports the durable experiment result.
