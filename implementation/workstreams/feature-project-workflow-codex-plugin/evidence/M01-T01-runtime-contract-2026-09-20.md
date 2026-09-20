# M01-T01 Runtime Contract Evidence — 2026-09-20

Card: `M01-T01 — Verify current Codex plugin activation contract`
Status: `GREEN implementation evidence; pending independent review`

## Runtime subject

- Workstation runtime: `codex-cli 0.155.0-alpha.9.2`.
- Verification used disposable isolated `CODEX_HOME` instances and disposable test workspaces.
- Live `/home/codex/.codex/config.toml`, live marketplace registration and live plugin installation state were not mutated.
- Generic Git-backed marketplace/plugin installability is reused from the qualified `elmakus/newproject-skill` M01 evidence; PWCP-specific packaging, hook, path-resolution and per-repository activation deltas were tested here.
- Definition R3 / approved plan PWCP-P3 accepts plugin `pw` + Skill `project-workflow` → `$pw:project-workflow`.

## GREEN findings

1. Same-repository plugin packaging is viable.
   - A local Git-marketplace-shaped source containing plugin manifest(s), Skill content, hooks/bootstrap and sibling `workflow/` files installed successfully through native `codex plugin marketplace add` + `codex plugin add`.
   - Installed cache readback contained the Skill, hook/bootstrap and canonical sibling workflow files together.

2. Canonical plugin-root path resolution is viable.
   - The SessionStart probe resolved `workflow/CONTEXT_ROUTING.md` and `workflow/codex_only/ROUTER.md` from `PLUGIN_ROOT`.
   - The hook injected only a bounded routing reminder; it did not copy or inject workflow policy contents.

3. Minimal always-on SessionStart activation works.
   - With hook trust bypassed only for the isolated test invocation, real `codex exec` received the injected marker and returned `PWCP_HOOK_SEEN`.
   - Without trust/bypass, the same invocation did not receive the hook marker and returned `PWCP_HOOK_MISSING`.
   - This proves trust is a real deterministic activation condition rather than documentation-only behavior.
   - Current runtime exposes hooks as stable and accepts SessionStart configuration for startup/resume/compact; full lifecycle E2E acceptance remains M03-owned.

4. Per-repository opt-in/isolation works on the current runtime.
   - User-level plugin state was set disabled in the disposable home.
   - A trusted test repository with local `[plugins."<plugin-id>"] enabled = true` received the SessionStart marker.
   - A trusted control repository without that override did not receive the marker.
   - This satisfies the M01 contract for an enabled repository versus an unaffected control repository without globally forcing Project Workflow on all repositories.

5. Plugin Skill discovery works through the native Desktop/App Server surface.
   - Native App Server `skills/list` discovered the installed bundled Skill and returned the installed cache path plus plugin ownership.
   - A real explicit invocation using the returned Skill ID loaded the Skill and exposed a unique sentinel from its `SKILL.md`.

## Historical naming constraint and Definition reconciliation

The first M01 runtime probe established the current namespace shape:

`<plugin-name>:<skill-name>`

Observed historical identities included:

- plugin `project-workflow-probe` + Skill `pw` → `project-workflow-probe:pw`;
- plugin `pw` + Skill `pw` → `pw:pw`.

A real invocation of literal `$pw` did not load that bundled Skill, so the then-current Definition required correction. That blocker is now resolved by Definition R3 and ADR-PWCP-002: the accepted normal bundled-Skill identity is plugin `pw` + Skill `project-workflow` → `$pw:project-workflow`.

The old `$pw:pw` result remains historical provenance only; it is not the current acceptance target.

## Definition R3 naming-delta revalidation

A fresh bounded probe revalidated only the affected naming delta; unchanged packaging/activation/path/trust/isolation evidence above was intentionally reused.

Probe setup:
- disposable root: `/tmp/pw-p3-name-probe-final-7c91`;
- isolated `CODEX_HOME`;
- local marketplace plugin name: `pw`;
- bundled Skill name: `project-workflow`;
- unique Skill sentinel: `PWCP_P3_SENTINEL_7C91`.

Results:
1. Native marketplace/plugin installation accepted plugin `pw` with Skill directory `skills/project-workflow/SKILL.md`.
2. Native App Server `skills/list` exposed the bundled Skill as `pw:project-workflow`.
3. A real `codex exec` invocation of `$pw:project-workflow` loaded the Skill and returned exactly `PWCP_P3_SENTINEL_7C91`.
4. Live `codex plugin list --json` and `codex plugin marketplace list --json` snapshots were byte-identical before versus after the isolated probe.
5. No live marketplace/plugin/config mutation was required.

Naming-delta verdict: `GREEN`.

## Concrete M02 implementation contract

M02 may now implement the accepted same-repository package with these bounded contracts:

1. Plugin identity is `pw`; the single bundled Skill is named `project-workflow` and is exposed as `$pw:project-workflow`.
2. The Skill remains a thin bootstrap/router only; canonical Project Workflow semantics stay in the existing workflow files.
3. The plugin package must carry the canonical sibling workflow files needed by bootstrap/path resolution.
4. The selected minimal always-on SessionStart activation/trust mechanism from the existing M01 evidence remains the implementation baseline because that mechanism was unchanged by Definition R3.
5. Per-repository opt-in/control-repository isolation remains required.
6. No plugin-local updater is introduced; marketplace/update ownership remains Workstation-owned.
7. M03 still owns full startup/resume/compaction E2E acceptance and the evidence-based `#issue/#feature` versus `$pw:project-workflow issue/feature` usage choice.

No current-runtime contradiction remains for M02.

## Review boundary

M01-T01 is implementation-complete but non-terminal until its contracted RECOMMENDED independent review is GREEN. The exact implementation subject is the commit that persists this refreshed evidence; Task Board owns the pending review pointer.
