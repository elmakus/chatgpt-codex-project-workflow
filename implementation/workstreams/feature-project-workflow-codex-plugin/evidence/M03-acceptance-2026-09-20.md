# M03 Integrated Acceptance — 2026-09-20

Milestone: `M03 — Always-on lifecycle, intake UX and progressive-disclosure acceptance`
Plan revision: `PWCP-P3`
Result: `GREEN`

## Accepted checkpoint

M03 is GREEN on exact implementation/verification subject `54e142f46571db110a155e0b1efdf5c7afcdfac3` plus its GREEN independent Card review.

Accepted state:
- the exact M02 production package remains the runtime subject;
- enabled repositories receive the bounded Project Workflow SessionStart bootstrap on ordinary use without requiring explicit Skill invocation;
- matched control repositories remain disabled unless a repository-local enable override applies;
- fresh entry, same-thread resume and native compaction preserve the Project Workflow invariant on the tested Codex `0.155.0-alpha.9.2` lifecycle;
- recurring bootstrap context remains bounded and delegates through workspace `PROJECT.md` plus canonical `workflow/CONTEXT_ROUTING.md`;
- current-runtime comparison selects `#feature <description>` and `#issue <description>` as the supported/preferred intake directives;
- `$pw:project-workflow` remains the explicit general entry/recovery path, while its `feature` / `issue` arguments are not documented as equivalent intake aliases on this runtime;
- trust bypass used for acceptance remained disposable and no live Codex marketplace/plugin/config/trust state was mutated.

## Evidence

- Implementation/lifecycle acceptance: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M03-T01-lifecycle-intake-2026-09-20.md`.
- Independent review: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M03-T01-independent-review-2026-09-20.md` — GREEN on exact subject `54e142f46571db110a155e0b1efdf5c7afcdfac3`.
- Independent rerun/readback: 14/14 repository tests GREEN; exact Codex `0.155.0-alpha.9.2`; isolated package install; repository-local enable/control isolation; installed bounded hook readback; native App Server schema exposes `thread/resume` and `thread/compact/start`.
- Predecessor: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M02-acceptance-2026-09-20.md`.

## Deferred by approved plan

M04 owns final install/usage documentation reconciliation, complete requirement matrix, canonical-source drift audit, current-`main` integration refresh, exact final workstream subject freeze, independent final-integration review and integration.

## Next approved milestone

`M04 — Integrated acceptance and release readiness`.
