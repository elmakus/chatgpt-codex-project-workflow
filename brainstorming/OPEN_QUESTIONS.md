# Open Questions

## PWCP-OQ-001 — Explicit Codex Skill entrypoint under bundled-Skill namespacing

Status: `requires user/product authority`
Date opened: `2026-09-20`
Origin: `implementation/workstreams/feature-project-workflow-codex-plugin/blockers/M01-T01-definition-naming-constraint-2026-09-20.md`
Evidence: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-runtime-contract-2026-09-20.md`

Current Codex runtime verification proves that a plugin-bundled Skill is exposed as `<plugin-name>:<skill-name>`. With the shortest practical names, plugin `pw` + Skill `pw` is invoked as `$pw:pw`. Literal `$pw` does not invoke that bundled Skill.

### Decision required

May Project Workflow revise its explicit supported Skill command from literal `$pw` to the verified bundled-Skill command `$pw:pw`?

- `YES` → reconcile PWCP-REQ-009, PWCP-REQ-010, acceptance outcomes 1/5 and ADR-PWCP-002 wording to `$pw:pw`, while keeping `#issue/#feature` preferred when M03 proves them reliable.
- `NO` → retain literal `$pw` as mandatory and require downstream research/planning for another supported explicit-entry surface outside normal bundled-Skill namespacing.

Do not resolve this question from implementation preference alone.
