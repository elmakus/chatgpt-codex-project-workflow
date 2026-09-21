# Brainstorming handoff — common pre-execution core — self-contained L

Date: 2026-09-21
Workstream: `feature-common-preexecution-core`
Branch: `feat/common-preexecution-core`
Canonical exploratory record: `brainstorming/COMMON_PREEXECUTION_CORE.md`
Phase: Brainstorming
Scope: `common-preexecution-core@R1`
Definition promotion authorization: `pending`

## Current obligation

Run live test L from:

`brainstorming/live-tests/CAPABILITY_REFRESH_L.md`

The test is now self-contained.

The user does not prepare a stale checkout manually.

The starting context:
1. refreshes the authoritative branch and reads the current L record;
2. verifies stale snapshot `2e52d793c597da27dc1000b126cf60cb90a8a491`;
3. creates a clean disposable checkout at that exact snapshot;
4. starts a fresh isolated probe rooted in that checkout;
5. gives the probe only the repository/branch/start-pointer locator;
6. does not execute the tested routing phase itself.

The probe must refresh `feat/common-preexecution-core` before selecting a phase and discover the current obligation from refreshed durable state.

Success requires:
- stale-rooted probe selects current `L-FRESH`;
- `L-STALE` is never executed or published;
- freshness is discovered before any push/CAS rejection;
- result becomes exact `L: FRESH\n`;
- canonical evidence remains runtime-neutral;
- production workflow modules remain unchanged.

After L:
1. run M — clean review evidence;
2. audit ROUTER / RECOVERY / WORKSTREAMS / CLOSE and relevant templates/tests;
3. reconcile the target common-core architecture;
4. stop at the user-owned Brainstorming -> Definition promotion gate unless the user explicitly authorizes Definition.

Do not enter Definition yet.
