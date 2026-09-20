# M01-T01 Runtime Contract Evidence — 2026-09-20

Card: `M01-T01 — Verify current Codex plugin activation contract`
Status: `BLOCKED on Definition-owned explicit Skill naming decision`

## Runtime subject

- Workstation runtime: `codex-cli 0.155.0-alpha.9.2`.
- Verification used disposable isolated `CODEX_HOME` instances and disposable test workspaces.
- Live `/home/codex/.codex/config.toml`, live marketplace registration and live plugin installation state were not mutated.
- Generic Git-backed marketplace/plugin installability is reused from the qualified `elmakus/newproject-skill` M01 evidence; PWCP-specific packaging, hook, path-resolution and per-repository activation deltas were tested here.

## GREEN findings

1. Same-repository plugin packaging is viable.
   - A local Git-marketplace-shaped source containing plugin manifest(s), `skills/pw/`, `hooks/` and sibling `workflow/` files installed successfully through native `codex plugin marketplace add` + `codex plugin add`.
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

## Definition-changing constraint found

Current Codex namespaces a plugin-bundled Skill as:

`<plugin-name>:<skill-name>`

Observed native App Server identities:

- plugin `project-workflow-probe` + Skill `pw` → `project-workflow-probe:pw`;
- plugin `pw` + Skill `pw` → `pw:pw`.

A real `codex exec` invocation of `$project-workflow-probe:pw` loaded the Skill and returned the unique sentinel `PWCP_SKILL_SENTINEL_73A1`.

A real invocation of literal `$pw` did not load that bundled Skill and returned the missing-skill sentinel.

Therefore the shortest verified normal bundled-Skill entrypoint is currently `$pw:pw`, not literal `$pw`.

## Authority impact

This does not invalidate same-repository packaging, canonical-source architecture, always-on activation, progressive disclosure, trust handling or per-repository isolation.

It does conflict with accepted authority that still requires literal `$pw` in:

- PWCP-REQ-009;
- PWCP-REQ-010;
- acceptance-level outcomes 1 and 5;
- related wording in ADR-PWCP-002 / plan assumptions.

PWCP-REQ-003 already anticipates a current-Codex naming constraint, but that fallback has not yet been reconciled through the literal `$pw` requirements above. Execution may not silently reinterpret those accepted requirements.

## Required next route

Return to Project Definition. User/product authority must decide whether to:

- accept the verified normal bundled-Skill name `$pw:pw` and reconcile literal `$pw` requirements accordingly; or
- retain literal `$pw` as mandatory, which requires a different explicit-entry surface outside normal bundled-Skill namespacing and therefore further verification/replanning.

M01-T01 remains non-terminal until that Definition decision is reconciled and execution is re-contracted.
