# Brainstorming handoff — common pre-execution core — live test M

Date: 2026-09-21
Workstream: `feature-common-preexecution-core`
Branch: `feat/common-preexecution-core`
Canonical exploratory authority: `brainstorming/COMMON_PREEXECUTION_CORE.md`
Phase: Brainstorming
Scope: `common-preexecution-core@R1`
Definition promotion authorization: `pending`

## Verified checkpoint

Live test L is complete and PASS at commit:
`b10eaa864b2a58831868e8b6efbea29bd0164c1e`.

The durable L record proves:
- exact stale pre-refresh HEAD was used;
- authoritative branch refresh happened before routing;
- current `L-FRESH` was selected;
- stale `L-STALE` was not executed/published;
- no push/CAS rejection was needed to discover freshness;
- result is exact `L: FRESH\n`;
- canonical evidence contains no concrete runtime identity telemetry.

## Current obligation

Run isolated clean-evidence live test M from:

`brainstorming/live-tests/CAPABILITY_REVIEW_M.md`

Harness:
`c427bafb31c3f6c79544be3a89300b02503aa7f9:brainstorming/live-tests/ISOLATED_COMMON_CONTRACT_HARNESS.md`

Immutable authority:
`48e7c92d7aa5f1931ce3e096aa3e6d23f6999e39:brainstorming/live-tests/CAPABILITY_REVIEW_M_SUBJECT.md`

Immutable reviewed subject:
`788ceee02a19d6e03d336b6f28b524691f09250d:brainstorming/live-tests/review-m/result.txt`

M must realize a genuine independent review capability-first and persist only the normalized semantic evidence allowed by its record. Concrete product/worker/model/session/invocation/workspace/worktree identity must not enter canonical Project Workflow evidence.

Expected correct subject verdict from the immutable authority is GREEN, but the reviewer must derive that verdict from the exact authority and subject rather than from this handoff or chat narrative.

## After M

If M completes:
1. return to canonical Brainstorming;
2. audit current ROUTER / RECOVERY / WORKSTREAMS / CLOSE plus relevant templates/tests;
3. reconcile capability-first routing, authoritative refresh, active_execution, append-only review history, final-integration review and cross-runtime continuation;
4. choose the target composition/migration architecture;
5. do not enter Definition without explicit user authorization.

Do not modify production workflow modules during M.
