# Brainstorming handoff — common pre-execution core — topology test N

Date: 2026-09-21
Workstream: `feature-common-preexecution-core`
Branch: `feat/common-preexecution-core`
Canonical exploratory authority: `brainstorming/COMMON_PREEXECUTION_CORE.md`
Phase: Brainstorming
Scope: `common-preexecution-core@R1`
Definition promotion authorization: `pending`

## Verified checkpoint

Live test M is PASS at:
`9435ebd56d9628588e64cde22efc631e1463dca0`.

M proved that independent review can persist only normalized semantic evidence with no concrete runtime identity telemetry.

## Current obligations

### First: N-CAPABLE

Start pointer:
`brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_CAPABLE.md`

This tests one capable coordinating invocation across:
`R01 RED -> correction S2 -> R02 independent GREEN -> deterministic finalization`

No intermediate user-facing stop is allowed unless a real blocker occurs.

### Then: N-CHATGPT

Start pointer:
`brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_CHATGPT.md`

This tests:
- fresh chat A: R01 RED -> same-chat correction -> freeze R02 -> stop only at the new fresh-review boundary;
- fresh chat B: R02 GREEN -> same-chat finalization -> completed.

Shared authority:
`43aef1d58367d2cfea1f561c58eee7791322c203:brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_AUTHORITY.md`

## After N

Audit current ROUTER / RECOVERY / WORKSTREAMS / CLOSE and relevant templates/tests, then reconcile target composition architecture.

Do not enter Definition without explicit user authorization.
Do not modify production workflow modules during N.
