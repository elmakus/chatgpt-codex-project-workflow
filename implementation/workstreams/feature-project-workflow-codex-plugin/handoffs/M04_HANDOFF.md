# M04 Handoff — Project Workflow Codex Plugin

> Completed milestone/workstream truth. Terminal state is owned by this workstream's selected Task Board and manifest on the integration target.

- Milestone: `M04 — Integrated acceptance and release readiness`
- Plan revision: `PWCP-P3`
- Status: `COMPLETED / INTEGRATED`
- Behavioral refreshed implementation head: `bde88f919c0d26326949a757223f146e9b1e6976`
- Final independent review subject: `69b12d651728d041e64c51e9dfae69a560bbf9f3`
- Final independent review evidence: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04_FINAL_INTEGRATION_REVIEW_2026-09-20.md`
- Integration target: `main`
- Pre-merge target baseline: `edb83e0c6c7ed06dcfce6df1e711fc3363d62d06`
- Pull request: `#44`
- Final integration result: `1f18f2dc0bc8c9a2c56b49967df12d4e94bd5e2f`
- Target-side closure evidence: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M04_FINAL_CLOSURE_2026-09-20.md`
- Source branch: automatically deleted by GitHub after successful merge; no fallback cleanup marker required
- Previous handoff: `implementation/workstreams/feature-project-workflow-codex-plugin/handoffs/M03_HANDOFF.md`

## Achieved state

The approved PWCP-P3 feature is integrated into `main`.

The integrated package provides:
- Git-backed Project Workflow plugin `pw` from this repository;
- exactly one bundled Skill `project-workflow`, explicitly exposed as `$pw:project-workflow`;
- bounded SessionStart activation that delegates through workspace `PROJECT.md` and canonical `workflow/CONTEXT_ROUTING.md`;
- explicit repository-local opt-in/control isolation and normal hook-trust semantics;
- verified preferred intake forms `#feature <description>` / `#issue <description>`;
- `$pw:project-workflow` as the general explicit entry/recovery path;
- no plugin-local updater/timer/poller;
- release-facing install/enable/usage documentation at `docs/CODEX_PLUGIN.md`.

PWCP-REQ-001…015 are covered with no unresolved acceptance gap. M01–M03 predecessor review gates and the distinct manifest-owned final-integration review are GREEN.

The final target refresh reconciled the workstream with then-current `main`, including the branch-first root-`PROJECT.md` authority change. Immediately before merge, the target remained unchanged and the PR was mergeable at the exact expected source head.

PR #44 merged the closure-ready package into `main`. Exact merge-result readback confirms the behavior-bearing plugin/Skill/hook/docs/test/router blobs are byte-identical to the refreshed compatibility subject whose durable evidence records 70/70 repository tests plus isolated Codex `0.155.0-alpha.9.2` install/readback. No fresh post-merge executable rerun is claimed; the terminal closure evidence records that limitation and the exact immutable readback used instead.

## Terminal recovery

Recover completed truth from the target-side `implementation/workstreams/feature-project-workflow-codex-plugin/` package plus manifest result and immutable PR #44 / merge-result evidence.

Preserve `feat/project-workflow-codex-plugin` as source-workstream provenance even though GitHub automatically deleted that merged head. `branch_cleanup` remains null because the normal auto-deletion path completed successfully.

No live Card, Research, review, integration or cleanup obligation remains.
