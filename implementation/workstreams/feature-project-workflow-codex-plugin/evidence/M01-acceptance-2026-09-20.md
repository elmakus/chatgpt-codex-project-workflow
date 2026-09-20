# M01 Integrated Acceptance — 2026-09-20

Milestone: `M01 — Current-runtime plugin and activation contract`
Plan revision: `PWCP-P3`
Result: `GREEN`

## Accepted checkpoint

M01's intended outcome is satisfied by the exact M01-T01 result subject `e37c30d8c53e9b1bfc1cb88ab62077d1ca18ff40` plus its GREEN independent review.

The accepted current-runtime contract is:

- same-repository Project Workflow plugin packaging is viable;
- installed plugin-root resolution can reach canonical `workflow/CONTEXT_ROUTING.md` / selected policy routing without copied policy;
- a bounded plugin-owned SessionStart activation candidate is viable and has an explicit deterministic trust condition;
- per-repository enabled/control isolation is proven for the M01 contract;
- plugin identity is `pw`, the one bundled Skill is `project-workflow`, native identity is `pw:project-workflow`, and explicit invocation is `$pw:project-workflow`;
- marketplace/update ownership remains Workstation-owned; no plugin-local updater is introduced;
- full lifecycle E2E, progressive-disclosure acceptance and intake-UX comparison remain M03-owned as planned.

## Evidence

- Implementation: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-p3-naming-delta-2026-09-20.md`.
- Unchanged-mechanism runtime evidence at the reviewed subject: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-runtime-contract-2026-09-20.md`.
- Independent review: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-independent-review-2026-09-20.md` — GREEN on exact subject `e37c30d8c53e9b1bfc1cb88ab62077d1ca18ff40`.
- No production plugin package was implemented in M01 and no live Codex marketplace/plugin/config state was mutated by the accepted M01 verification.

## Next approved milestone

`M02 — Same-repo plugin package and canonical wrapper`.

Its JIT preparation may use this accepted M01 contract as predecessor authority.
