# M01 Handoff — Project Workflow Codex Plugin

Milestone: `M01 — Current-runtime plugin and activation contract`
Plan revision: `PWCP-P3`
Status: `GREEN / complete`

## Completed checkpoint

- Final implementation subject: `e37c30d8c53e9b1bfc1cb88ab62077d1ca18ff40`.
- Card `M01-T01`: done.
- Independent Card review: GREEN.
- Milestone acceptance: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-acceptance-2026-09-20.md`.

## Authority now in force

- Definition: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md` R3.
- Decisions: `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_PACKAGING.md`, `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_ACTIVATION.md`.
- Plan: `planning/PROJECT_WORKFLOW_CODEX_PLUGIN_MASTER_PLAN.md` PWCP-P3.

## Achieved state

M01 proves the current-runtime contract needed by M02: same-repository packaging, canonical installed-root routing, bounded always-on SessionStart activation with explicit trust behavior, per-repository isolation, and the accepted one-Skill identity plugin `pw` + Skill `project-workflow` → `$pw:project-workflow`.

The reusable M01 boundary is mechanism-specific: unchanged packaging/activation/path/trust/isolation findings may be reused, while any changed runtime mechanism must refresh its affected verification.

## Deferred by approved plan

M03 owns full fresh/resume/compaction E2E, progressive-disclosure acceptance, and the evidence-based `#issue/#feature` versus `$pw:project-workflow issue/feature` convention.

## Next durable starting point

Proceed to JIT Execution Prep for `M02 — Same-repo plugin package and canonical wrapper` on `feat/project-workflow-codex-plugin`, using M01 acceptance as predecessor evidence.
