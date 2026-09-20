# M04 Integrated Acceptance Candidate — 2026-09-20

Milestone: `M04 — Integrated acceptance and release readiness`
Plan revision: `PWCP-P3`
Status: `GREEN_FOR_FINAL_INTEGRATION_REVIEW`

This is the closure-ready pre-review acceptance surface. M04 is intentionally **not terminal** until the distinct manifest-owned final-integration review is GREEN and final integration/readback completes.

## Accepted implementation state

The Project Workflow Codex plugin feature is complete on the refreshed workstream branch with:
- plugin `pw`;
- one bundled Skill `project-workflow` exposed as `$pw:project-workflow`;
- bounded SessionStart activation that routes through workspace `PROJECT.md` and canonical `workflow/CONTEXT_ROUTING.md`;
- repository-local opt-in/control isolation;
- current-runtime trust semantics explicitly documented;
- `#feature <description>` / `#issue <description>` selected as the supported preferred intake forms by M03 evidence;
- `$pw:project-workflow` retained as explicit general entry/recovery;
- no plugin-local updater/timer/poller;
- Git-backed marketplace/update ownership left with Codex/Workstation;
- user-facing install/enable/usage documentation at `docs/CODEX_PLUGIN.md`.

## Requirement acceptance

`implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04-T01-release-readiness-2026-09-20.md` contains the complete PWCP-REQ-001…015 matrix with no unresolved requirement gap.

Predecessor accepted evidence:
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-acceptance-2026-09-20.md`;
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M02-acceptance-2026-09-20.md`;
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M03-acceptance-2026-09-20.md`.

## Current-main refresh

Final integration refresh evidence:
`implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04_FINAL_INTEGRATION_REFRESH_2026-09-20.md`.

Exact refreshed compatibility baseline:
- target `main`: `edb83e0c6c7ed06dcfce6df1e711fc3363d62d06`;
- refreshed workstream merge: `bde88f919c0d26326949a757223f146e9b1e6976`;
- exact merge tree: `305d43de76b8bfdb637ad43616ca1f480a6e9088`;
- GitHub readback: workstream is `behind_by: 0` against that target;
- post-refresh full repository regression: 70/70 GREEN;
- post-refresh plugin drift/semantic audit: GREEN;
- post-refresh isolated Codex `0.155.0-alpha.9.2` install/readback: GREEN;
- no live Codex state mutation.

The only textual refresh conflict was root `PROJECT.md`; it was resolved to current-`main` branch-first authority because root Project state must not mirror this workstream's live state. All plugin authority/state remains under the namespaced workstream package.

## Remaining acceptance gate

PWCP-P3 M04 acceptance item “final subject passes required/recommended review and integration refresh” is only partially complete:
- integration refresh: GREEN;
- manifest-owned final-integration review: pending freeze/fresh independent review;
- final target merge/readback: pending until that review is GREEN.

Therefore the workstream is ready to freeze one exact closure-ready subject for the manifest `RECOMMENDED` final-integration review, but M04/workstream must remain non-terminal.
