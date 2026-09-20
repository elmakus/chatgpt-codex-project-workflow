# M01-T01 Result Reconciliation — 2026-09-20

Card: `M01-T01 — Verify current Codex plugin activation contract`
State: `implementation complete; pending independent review`

## Authority reconciled

- Approved Definition: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md` R2.
- Accepted packaging decision: `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_PACKAGING.md`.
- Accepted activation decision: `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_ACTIVATION.md`.
- Approved plan: `planning/PROJECT_WORKFLOW_CODEX_PLUGIN_MASTER_PLAN.md` revision `PWCP-P2`.
- Independent plan review: `planning/reviews/PWCP-P2.md` GREEN on exact reviewed plan blob `4932fcfa47a0a6a8dc9c4404fe76cb6f4a4c4346`.
- Runtime evidence: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-runtime-contract-2026-09-20.md`.
- Resolved blocker provenance: `implementation/workstreams/feature-project-workflow-codex-plugin/blockers/M01-T01-definition-naming-constraint-2026-09-20.md`.

## Reconciliation result

The original M01 runtime probes remain valid. Their mechanism and observed runtime did not change; only the Definition-owned explicit bundled-Skill naming requirement was corrected after the runtime proved the native identity contract.

The accepted explicit entry contract is now:

- plugin name: `pw`;
- bundled Skill name: `pw`;
- native bundled-Skill identity: `pw:pw`;
- explicit user command: `$pw:pw`.

Literal `$pw` is not an acceptance obligation and is not treated as a supported bundled-Skill invocation.

The existing runtime evidence remains GREEN for:

1. same-repository Git-backed plugin packaging;
2. installed plugin-root resolution of sibling canonical workflow files;
3. a bounded plugin-owned `SessionStart` activation candidate;
4. deterministic trust behavior for that activation surface;
5. per-repository enabled/control isolation;
6. native bundled-Skill discovery and explicit invocation;
7. preservation of the canonical workflow source rather than copied Skill policy.

No runtime probe was repeated during this reconciliation because no runtime mechanism, package probe, hook behavior, trust behavior, isolation behavior or installed-path behavior changed after the evidence was captured. Re-running unchanged probes would duplicate already-qualified evidence rather than test a changed contract.

## Concrete M02 implementation contract

M02 may now implement the production package inside the accepted authority using the M01-proven shape:

- package from this repository; do not create a mirror repository;
- use plugin `pw` with exactly one bundled Skill `pw`, exposed as `$pw:pw`;
- keep the Skill/bootstrap thin and route through workspace `PROJECT.md` and canonical `workflow/CONTEXT_ROUTING.md` / selected policy routing;
- resolve canonical workflow files from the installed plugin package root; do not copy `workflow/codex_only/*` semantics into the Skill;
- use the proven minimal always-on activation approach subject to the same explicit trust condition and keep its injected context bounded;
- preserve per-repository opt-in/control isolation;
- keep marketplace/update ownership in Workstation and add no plugin-local updater;
- reuse qualified generic marketplace/install/update evidence where the mechanism is unchanged;
- leave full startup/resume/compaction lifecycle E2E, progressive-disclosure acceptance, and `#issue/#feature` versus `$pw:pw issue/$pw:pw feature` UX selection to M03 as planned.

## Card acceptance check

1. Current runtime/version: recorded in the runtime evidence.
2. Generic marketplace/plugin baseline reuse boundary: recorded and preserved.
3. Same-repository isolated install/readback: GREEN.
4. Installed canonical path resolution without copied policy: GREEN.
5. Bounded always-on activation candidate: GREEN.
6. Current runtime supports the required SessionStart lifecycle surface sufficiently for M02; full lifecycle E2E remains M03-owned.
7. Trust behavior: GREEN and deterministic.
8. Enabled repository versus control repository isolation: GREEN.
9. Live Codex marketplace/plugin state mutation: none; disposable isolated state only.
10. Concrete M02 implementation contract: now resolved above after Definition R2 and approved PWCP-P2 removed the sole naming blocker.

## Verification / side effects

- No production plugin files were implemented in M01.
- No live Workstation plugin/marketplace/config state was mutated by this reconciliation.
- No credentials or external persistent state were introduced.
- Historical runtime evidence and blocker records are preserved unchanged as provenance.

## Result

`GREEN_FOR_INDEPENDENT_REVIEW`

M01-T01 has no remaining implementation blocker. Because its Card contract classifies independent review as `RECOMMENDED`, the Card remains non-terminal until a fresh independent reviewer evaluates the exact immutable result subject.
