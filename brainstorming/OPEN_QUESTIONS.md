# Open Questions

## PWCP-OQ-001 — Explicit Codex Skill entrypoint under bundled-Skill namespacing

Status: `resolved`
Date opened: `2026-09-20`
Origin: `implementation/workstreams/feature-project-workflow-codex-plugin/blockers/M01-T01-definition-naming-constraint-2026-09-20.md`
Evidence: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-runtime-contract-2026-09-20.md`

Current Codex runtime verification proves that a plugin-bundled Skill is exposed as `<plugin-name>:<skill-name>`. With the shortest practical names, plugin `pw` + Skill `pw` is invoked as `$pw:pw`. Literal `$pw` does not invoke that bundled Skill.

### Resolution

User/product authority accepted `YES` on 2026-09-20: use the verified bundled-Skill command `$pw:pw`.

Definition reconciliation updates PWCP-REQ-003, PWCP-REQ-009, PWCP-REQ-010, acceptance outcomes and ADR-PWCP-002 accordingly. `#issue/#feature` remain preferred when M03 proves them reliable; otherwise the fallback is `$pw:pw issue ...` / `$pw:pw feature ...`.
