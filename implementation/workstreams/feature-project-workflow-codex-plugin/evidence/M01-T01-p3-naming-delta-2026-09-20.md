# M01-T01 — PWCP-P3 naming-delta reconciliation

Card: `M01-T01 — Verify current Codex plugin activation contract`
State: `implementation complete; pending independent review`
Date: `2026-09-20`

## Authority

- Definition: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md` R3.
- Decisions: `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_PACKAGING.md`, `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_ACTIVATION.md`.
- Approved plan: `planning/PROJECT_WORKFLOW_CODEX_PLUGIN_MASTER_PLAN.md` PWCP-P3.
- Plan review: `planning/reviews/PWCP-P3.md` GREEN on immutable blob `634806af9a3325d2c1078317d20f94cd842b0451`.
- Reconciled Card: `implementation/workstreams/feature-project-workflow-codex-plugin/cards/M01-T01.md`.
- Reused runtime evidence: `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-runtime-contract-2026-09-20.md`.
- Naming provenance: `implementation/workstreams/feature-project-workflow-codex-plugin/blockers/M01-T01-command-name-reopened-2026-09-20.md`.

## Reuse boundary

The workstation still runs `codex-cli 0.155.0-alpha.9.2`, identical to the original M01 evidence. Packaging, installed-root resolution, SessionStart activation, hook/trust, enabled/control isolation, canonical-source behavior, and marketplace/update mechanisms are unchanged, so those results are reused by exact reference under PWCP-REQ-012.

The only affected delta is the accepted explicit bundled-Skill identity:

- plugin `pw`;
- Skill `project-workflow`;
- native identity `pw:project-workflow`;
- command `$pw:project-workflow`.

## Isolated current-runtime probe

All test writes were confined to disposable `/tmp/pw-p3-name-probe-a91f` inside `chatgpt-ce-workstation`. No live Codex marketplace, plugin, configuration, workflow repository, or Workstation service state was modified.

The local probe marketplace `pw-p3-probe` contained plugin `pw` version `0.0.1` with exactly one Skill at `skills/project-workflow/SKILL.md`, declaring `name: project-workflow` and sentinel `PWCP_P3_SENTINEL_7C91`.

### Install/readback

`codex plugin marketplace add` accepted the local marketplace. `codex plugin add pw@pw-p3-probe --json` succeeded with:

```json
{
  "pluginId": "pw@pw-p3-probe",
  "name": "pw",
  "marketplaceName": "pw-p3-probe",
  "version": "0.0.1",
  "installedPath": "/tmp/pw-p3-name-probe-a91f/codex-home/plugins/cache/pw-p3-probe/pw/0.0.1",
  "authPolicy": "ON_USE"
}
```

The installed payload contained `.../pw/0.0.1/skills/project-workflow/SKILL.md`.

### Native App Server discovery

After normal App Server `initialize`, `skills/list` with `forceReload: true` returned:

```json
{
  "name": "pw:project-workflow",
  "description": "PWCP P3 naming delta probe.",
  "path": "/tmp/pw-p3-name-probe-a91f/codex-home/plugins/cache/pw-p3-probe/pw/0.0.1/skills/project-workflow/SKILL.md",
  "scope": "user",
  "enabled": true,
  "pluginId": "pw@pw-p3-probe"
}
```

The workspace entry reported no Skill errors.

### Real explicit invocation

A real isolated `codex exec --ephemeral` prompt beginning with `$pw:project-workflow` loaded the bundled Skill. Its completed agent message was exactly:

`PWCP_P3_SENTINEL_7C91`

Therefore the current runtime accepts Skill name `project-workflow`, exposes it natively as `pw:project-workflow`, and invokes it through `$pw:project-workflow`.

## Acceptance reconciliation

1. Runtime/version: GREEN — unchanged `0.155.0-alpha.9.2`.
2. Generic marketplace/plugin evidence reuse boundary: GREEN.
3. Same-repository isolated install/readback: GREEN by prior exact evidence; local naming probe also installed successfully.
4. Installed canonical-path resolution without copied policy: GREEN by prior exact evidence; unaffected by naming.
5. Bounded always-on activation candidate: GREEN by prior exact evidence.
6. Startup/resume/compact substrate sufficient for M02: GREEN by prior exact evidence; full lifecycle E2E stays in M03.
7. Trust behavior: GREEN by prior exact evidence.
8. Enabled/control isolation: GREEN by prior exact evidence.
9. No live marketplace/plugin/config mutation: GREEN.
10. P3 naming delta: GREEN — native `skills/list` returned `pw:project-workflow` and real invocation returned the sentinel.
11. Concrete M02 implementation contract: GREEN below.

## Concrete M02 implementation contract

M02 may implement the production package using the proven shape:

- package from this repository;
- plugin `pw` with exactly one Skill `project-workflow`, exposed as `$pw:project-workflow`;
- keep Skill/bootstrap thin and route through workspace `PROJECT.md`, `workflow/CONTEXT_ROUTING.md`, and selected canonical policy routing;
- resolve canonical workflow files from the installed plugin root; do not copy policy semantics into the Skill;
- use the proven minimal always-on activation approach with the same explicit trust condition and bounded injected context;
- preserve per-repository opt-in/control isolation;
- keep marketplace/update ownership in Workstation; add no plugin-local updater;
- reuse qualified generic marketplace/install/update evidence where unchanged;
- leave full lifecycle E2E, progressive-disclosure acceptance, and `#issue/#feature` versus `$pw:project-workflow issue` / `$pw:project-workflow feature` selection to M03.

## Side effects

- No production plugin files were implemented in M01.
- No live Codex marketplace/plugin/config state was mutated by this delta.
- The disposable isolated home referenced existing Codex authentication only for the ephemeral real invocation; authentication content is not recorded here.
- No new credentials or persistent external state were introduced.
- Historical R1/R2 evidence, blockers, and obsolete review subjects remain provenance only.

## Result

`GREEN_FOR_INDEPENDENT_REVIEW`

M01-T01 has no remaining implementation blocker. Its Card review requirement is `RECOMMENDED`, so it remains non-terminal until a fresh independent reviewer evaluates the exact immutable implementation subject.
