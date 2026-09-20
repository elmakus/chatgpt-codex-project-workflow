# Independent Review — M01-T01 — 2026-09-20

Card: `M01-T01 — Verify current Codex plugin activation contract`
Review owner: selected workstream Task Board
Review requirement: `RECOMMENDED`
Verdict: `GREEN`
Reviewed subject: `e37c30d8c53e9b1bfc1cb88ab62077d1ca18ff40`

## Exact review basis

- Workstream identity/binding: `feature-project-workflow-codex-plugin` on `feat/project-workflow-codex-plugin`.
- Card contract: `implementation/workstreams/feature-project-workflow-codex-plugin/cards/M01-T01.md`.
- Approved authority: Definition `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md` R3, ADR-PWCP-001, ADR-PWCP-002, approved Master Plan `PWCP-P3`.
- Exact reviewed implementation evidence created in the subject: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-p3-naming-delta-2026-09-20.md`.
- Reused unchanged-mechanism evidence was read from the exact subject tree at `e37c30d8c53e9b1bfc1cb88ab62077d1ca18ff40`, not from later branch mutations.
- Naming provenance and official validator evidence confirm normal Skill names are hyphen-case; `project-workflow` satisfies the current validator while `project_workflow` does not.

## Findings

1. The exact subject contains the bounded P3 delta required after Definition R3: plugin `pw`, Skill `project-workflow`, native identity `pw:project-workflow`, explicit invocation `$pw:project-workflow`.
2. The delta evidence records native install/readback, App Server `skills/list` discovery and a real isolated `codex exec` invocation returning `PWCP_P3_SENTINEL_7C91`.
3. The reused M01 runtime evidence at the exact subject independently supports the unchanged same-repository packaging, installed-root canonical path resolution, bounded SessionStart activation, trust condition and enabled/control isolation findings. Its historical naming blocker is explicitly superseded by R3 plus the new P3 delta evidence and is not treated as current authority.
4. The Card's acceptance items remain correctly partitioned: M01 establishes the concrete current-runtime packaging/activation contract; full startup/resume/compaction E2E, progressive-disclosure acceptance and intake-UX comparison remain M03-owned.
5. No production plugin files are introduced by the reviewed subject. The evidence records disposable isolated runtime state and no live marketplace/plugin/config mutation.
6. The concrete M02 contract is consistent with R3/PWCP-P3: same-repository package, one thin bundled Skill, canonical workflow routing, bounded always-on activation, per-repository isolation, no plugin-local updater.
7. A compare from the reviewed subject to the review-start branch shows later state/evidence bookkeeping commits. In particular, the historical runtime-evidence file was refreshed after the subject. This verdict does not rely on those later edits; the P3 naming-delta proof needed for acceptance is already contained in the immutable reviewed subject itself.

## Acceptance verdict

All M01-T01 acceptance conditions applicable to the exact subject are satisfied. No current-runtime contradiction to the approved same-repository / canonical-source / one-Skill / always-on architecture is demonstrated.

`GREEN`

Post-review continuation is the normal deterministic Card-finalization route; the verdict itself does not mark the Card `done`.
