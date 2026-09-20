# M02 Integrated Acceptance — 2026-09-20

Milestone: `M02 — Same-repo plugin package and canonical wrapper`
Plan revision: `PWCP-P3`
Result: `GREEN`

## Accepted checkpoint

M02 is GREEN on exact implementation subject `6e16ba11293bbdb7bbc8d96167e8280273d77304` plus its GREEN independent Card review.

Accepted state:
- this repository is the Git-backed marketplace/plugin source;
- marketplace `project-workflow` exposes one root plugin `pw`;
- the plugin exposes one normal Skill `project-workflow`, with current identity `pw:project-workflow`;
- Skill/bootstrap route through workspace `PROJECT.md` and canonical `workflow/CONTEXT_ROUTING.md` without copied policy;
- SessionStart uses the accepted M01 `PLUGIN_ROOT` mechanism and preserves explicit trust behavior;
- canonical workflow files ship with the same root package, so ordinary workflow-module changes do not require a Skill edit;
- no plugin-local updater/timer/poller exists and verification did not mutate live Codex state.

## Evidence

- Implementation: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M02-T01-plugin-package-2026-09-20.md`.
- Independent review: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M02-T01-independent-review-2026-09-20.md` — GREEN on exact subject `6e16ba11293bbdb7bbc8d96167e8280273d77304`.
- Independent rerun: 14/14 repository tests GREEN plus isolated Codex `0.155.0-alpha.9.2` marketplace install/bootstrap/hash readback.
- Predecessor: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-acceptance-2026-09-20.md`.

## Deferred by approved plan

M03 owns full fresh/resume/compaction lifecycle E2E, progressive-disclosure acceptance, control-repository E2E and the intake-UX comparison.

## Next approved milestone

`M03 — Always-on lifecycle, intake UX and progressive-disclosure acceptance`.
