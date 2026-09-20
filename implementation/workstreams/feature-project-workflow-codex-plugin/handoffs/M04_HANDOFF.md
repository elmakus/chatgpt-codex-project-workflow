# M04 Handoff — Project Workflow Codex Plugin

Milestone: `M04 — Integrated acceptance and release readiness`
Plan revision: `PWCP-P3`
Status: `PRE-INTEGRATION / FINAL REVIEW GREEN`

## Closure-ready state

- M01–M03: GREEN and terminal.
- M04-T01: done with complete PWCP-REQ-001…015 evidence matrix.
- Release-facing plugin documentation: `docs/CODEX_PLUGIN.md`.
- Current-`main` refresh: GREEN.
- Refreshed compatibility commit: `bde88f919c0d26326949a757223f146e9b1e6976`.
- Refresh target baseline: `edb83e0c6c7ed06dcfce6df1e711fc3363d62d06`.
- Full post-refresh repository regression: 70/70 GREEN.
- Current-runtime isolated plugin install/readback: GREEN on Codex `0.155.0-alpha.9.2`.
- Manifest-owned final-integration review: GREEN on exact subject `69b12d651728d041e64c51e9dfae69a560bbf9f3`.
- Final-review evidence: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04_FINAL_INTEGRATION_REVIEW_2026-09-20.md`.
- Final integration pull request: `#44` (open; merge pending final target re-read).

## Authority now in force

- Definition: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md` R3.
- Decisions:
  - `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_PACKAGING.md`;
  - `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_ACTIVATION.md`.
- Plan: `planning/PROJECT_WORKFLOW_CODEX_PLUGIN_MASTER_PLAN.md` PWCP-P3.
- Current workflow authority at finalization: repository `main`, reconciled into this workstream by the M04 integration refresh.

## Evidence

- M04 Card acceptance matrix:
  `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04-T01-release-readiness-2026-09-20.md`.
- Final integration refresh:
  `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04_FINAL_INTEGRATION_REFRESH_2026-09-20.md`.
- Pre-review integrated acceptance candidate:
  `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04_ACCEPTANCE_CANDIDATE_2026-09-20.md`.
- Final independent review:
  `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04_FINAL_INTEGRATION_REVIEW_2026-09-20.md`.
- M01–M03 acceptance/review evidence remains referenced by the selected Task Board.

## Remaining gate and deterministic continuation

The manifest-owned `RECOMMENDED` final-integration review is GREEN. The workstream remains non-terminal only because final target integration/readback has not yet completed.

Close must now:
1. immediately re-read current `main`; if target moved, rerun the integration refresh contract before merging and preserve or invalidate review coverage according to the exact-change rules;
2. verify PR `#44` still carries this namespaced closure-ready package;
3. merge only while the review/refresh gates remain current;
4. perform target-side terminal manifest/Task Board/handoff/result reconciliation and readback;
5. treat automatic source-branch deletion as normal success, or use the manifest-local cleanup fallback only if the merged source branch survives.
