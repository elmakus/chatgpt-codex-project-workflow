# M01-T01 Definition Blocker — bundled Skill naming

Date: 2026-09-20
Card: `M01-T01`
Classification: `accepted-authority correction required`
Route: `Project Definition → user/product authority`

## Trigger

Exact current-runtime evidence is recorded at:

`implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-runtime-contract-2026-09-20.md`

The current Codex App Server namespaces a plugin-bundled Skill as `<plugin-name>:<skill-name>`. The shortest verified Project Workflow shape is therefore `$pw:pw`; literal `$pw` does not select the bundled Skill.

## Why execution is blocked

Accepted PWCP authority still requires literal `$pw` in PWCP-REQ-009, PWCP-REQ-010 and acceptance outcomes 1/5. Execution cannot silently weaken or reinterpret that user/product UX requirement.

The rest of M01 packaging/activation evidence is compatible with the accepted same-repository, canonical-source, always-on, progressive-disclosure, trust and per-repository-isolation architecture.

## Smallest unresolved product decision

Choose whether the explicit supported Skill command may use the verified normal bundled-Skill form `$pw:pw`.

- If yes: Definition should reconcile the literal `$pw` requirements/ADR wording to the current Codex naming constraint, then Planning/Execution Prep should reconcile the affected plan/Card and resume M01.
- If no: literal `$pw` remains mandatory; Definition preserves that requirement and downstream work must research/plan a separate supported explicit-entry surface outside normal bundled-Skill namespacing.

No implementation route may continue across this decision boundary without user/product authority.
