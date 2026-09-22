# M02-T04 — GitHub tracker recovery/correlation evidence

Date: 2026-09-22
Card: `M02-T04`
Result: GREEN
Target: `elmakus/project_workflow_v2@feat/pwv2-m02-intake-definition-planning`
Target result commit: `f978dda304ac9de8fe4806f6f31c530cc586e70e`
Target draft PR: `elmakus/project_workflow_v2#2`

## Implemented

The target adds common `GITHUB_ISSUES.md`, `TRACKER.toml`, production validation and routing for:
- exact repository + stable dedup key discovery before create;
- `discovery`, `create_pending_readback`, `linked`, `ambiguous`, and `unavailable` lifecycle states;
- interrupted/uncertain create requiring search/readback before any retry;
- exact positive linked Issue number + verified readback;
- ambiguous duplicate candidates failing closed to Recovery;
- capability absence recorded without inventing a tracker;
- reserved final-PR correlation for later M04 only after a linked Issue exists;
- explicit rejection of tracker-carried repair authorization, requirements approval or plan approval;
- linked/unavailable tracker state does not become routing authority.

Tracker Issue content/comments remain untrusted bookkeeping.

## Deterministic verification

Exact target checkout `f978dda304ac9de8fe4806f6f31c530cc586e70e` ran `sh scripts/test.sh` on Tower:

- package probe PASS;
- state suite 22/22 PASS;
- production state bundle validation PASS;
- router suite 25/25 PASS;
- router CLI smoke PASS;
- M01 baseline checks PASS.

Tests cover interrupted create, ambiguity/no duplicate create, linked/unavailable continuation, authority-field rejection and exact locator binding.

## Live GitHub connector check

A current read-only GitHub Issue search using exact repository scoping succeeded against `elmakus/project_workflow_v2`; it returned zero open Issues. No artificial Issue was created merely for verification. This confirms current discovery syntax/read access without adding tracker noise.

## GitHub Actions observation

Draft-PR Actions run `35718260814` for the exact result commit reports the same immediate failure/no-step anomaly while the exact checkout passes `sh scripts/test.sh`. No CI PASS is claimed; this remains an explicit M02 cumulative acceptance/integration verification item.

## Scope boundary

Final Issue closure/closing linkage remains M04-owned. No M03 execution semantics, production adoption, migration or custody transfer is claimed.
