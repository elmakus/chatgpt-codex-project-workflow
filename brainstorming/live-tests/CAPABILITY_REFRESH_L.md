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

The test runner must begin with a clean local checkout whose pre-refresh HEAD is exactly the known stale snapshot above, while the authoritative remote branch has advanced beyond it.

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

## Required entry sequence

Before selecting any phase:

1. establish and record the local pre-refresh HEAD;
2. require it to equal `2e52d793c597da27dc1000b126cf60cb90a8a491`;
3. refresh the exact authoritative branch `feat/common-preexecution-core`;
4. establish the refreshed authoritative head;
5. prove that authoritative head is newer than / different from the stale snapshot;
6. reconcile or validate the clean local checkout against that refreshed head;
7. read this record from refreshed authoritative durable state;
8. only then select the legal obligation.

If the local starting condition is not exact, do not fake the test; leave this record pending and report the setup mismatch.

## Phase L-FRESH — authoritative obligation

After the required entry sequence proves this is the current obligation:

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
4. STOP at the experiment boundary.

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

- runner really started from local HEAD `2e52d793c597da27dc1000b126cf60cb90a8a491`;
- authoritative remote state had already advanced;
- remote refresh happened before phase selection;
- runner selected `L-FRESH`, not the stale `L-STALE`;
- result is exact `L: FRESH\n`;
- no stale marker was produced;
- no stale-phase publication was attempted;
- freshness was discovered before any push/CAS rejection;
- evidence contains no product/worker/model/session/invocation/worktree identity.

## Failure conditions

FAIL if:
- the runner acts on `L-STALE`;
- the runner learns freshness only from rejected publication;
- local starting HEAD was not the exact stale snapshot but the test is nevertheless claimed valid;
- canonical evidence imports runtime identity/telemetry forbidden by the harness;
- any production workflow module is changed.
