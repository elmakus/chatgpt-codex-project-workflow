# Brainstorming handoff — common pre-execution core — post-M / pre-audit

Date: 2026-09-21
Workstream: `feature-common-preexecution-core`
Branch: `feat/common-preexecution-core`
Canonical exploratory authority: `brainstorming/COMMON_PREEXECUTION_CORE.md`
Phase: Brainstorming
Scope: `common-preexecution-core@R1`
Definition promotion authorization: `pending`

## Verified checkpoint

Live test L: PASS.

Live test M: PASS at:
`9435ebd56d9628588e64cde22efc631e1463dca0`.

M proved that independent review can persist normalized semantic-only evidence without concrete runtime identity telemetry.

## Topology validation N — deferred until V2

The intended compatibility invariant remains:

- a capable coordinator may continue one-shot across deterministic review/correction/re-review/finalization;
- a normal ChatGPT review chat may continue after GREEN;
- after RED it may perform bounded same-chat correction, but if it materially creates the corrected subject it must stop only at the new independent-review boundary;
- independence is per exact subject, not per whole chat/session.

Prepared scenarios remain at:
- `brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_CAPABLE.md`;
- `brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_CHATGPT.md`.

Both are now `deferred_until_v2`.

Do not execute them against current V1. They are V2 implementation/validation tests and are not prerequisites for current Brainstorming/Definition readiness.

Experimental clean-room harness:
`brainstorming/live-tests/CLEANROOM_TOPOLOGY_HARNESS_N.md`.

It is retained only as future validation infrastructure and has no production authority.

## Current obligation

Continue Brainstorming with the cross-cutting repository audit:

- current ROUTER;
- RECOVERY;
- WORKSTREAMS;
- CLOSE;
- relevant templates/tests.

Reconcile those contracts with:
- capability-first realization;
- authoritative-state refresh before routing;
- `active_execution`;
- append-only review attempts;
- final-integration review;
- orchestration-topology preservation;
- cross-runtime continuation.

Then choose the target common-core composition/migration architecture and determine whether any material design question remains.

If Brainstorming becomes ready, STOP at the user-owned Brainstorming -> Definition promotion gate.

Do not enter Definition without explicit user authorization.
Do not modify production workflow modules during this Brainstorming audit.
