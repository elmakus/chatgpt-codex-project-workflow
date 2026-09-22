# M02-T02 — Brainstorming, Research and Definition evidence

Date: 2026-09-22
Card: `M02-T02`
Result: GREEN
Target: `elmakus/project_workflow_v2@feat/pwv2-m02-intake-definition-planning`
Target result commit: `17f30348618319df04b6c4bf785d425584e8cf96`
Target draft PR: `elmakus/project_workflow_v2#2`

## Implemented slice

The target adds common `BRAINSTORMING.md`, `RESEARCH.md` and `DEFINITION.md` semantics plus minimal owner-driven TOML state and production validation.

Implemented invariants include:
- intrinsic adaptive grilling with no active `#grill` command;
- exact exploratory `scope_id@revision`, GREEN challenge audit and explicit user-owned Definition promotion;
- stale promotion subject fails closed after revision movement;
- agent-findable facts route through Research rather than user questioning;
- Research accounts explicitly for official/upstream, project/runtime, tracker/discussion and practitioner/community source classes with explicit weight/status;
- completed Research has one exact return owner; applied return result is consume-only and cannot be replayed;
- Definition is bound to the exact promoted exploratory subject;
- Definition GREEN requires accepted authority + GREEN completeness audit;
- premium stop A becomes due after Definition GREEN and blocks material Planning;
- no runtime/model/session identity, Context Health or V1 policy tree was introduced.

## Deterministic verification

Exact target checkout `17f30348618319df04b6c4bf785d425584e8cf96` ran `sh scripts/test.sh` on Tower and passed:

- M01 package probe: PASS;
- state-contract suite: 17/17 PASS;
- production bundle validation: PASS;
- router suite: 17/17 PASS;
- router CLI smoke: PASS;
- M01 baseline checks: PASS.

The preserved M01 literal `fail closed` package-probe contract was restored after a documentation-only wording regression; no lifecycle behavior changed in that repair.

## GitHub Actions observation

Draft-PR Actions run `35717491840` for the exact result commit reports `failure`. The job exposes no steps and the connector cannot retrieve a job log, while the exact immutable checkout passes the same repository test command. No CI PASS is claimed. This remains an explicit cumulative M02 integration verification item rather than being treated as accepted CI.

## Scope boundary

T02 does not implement Strategic Planning/Plan Review stops B/C, GitHub Issue mutation/correlation, M03 execution/review, Close, migration, production adoption or custody transfer.
