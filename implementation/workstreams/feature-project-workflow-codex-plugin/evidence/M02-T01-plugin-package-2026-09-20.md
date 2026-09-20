# M02-T01 Implementation Evidence — 2026-09-20

Card: `M02-T01 — Implement same-repo Codex plugin package`
Implementation subject: `6e16ba11293bbdb7bbc8d96167e8280273d77304`
Runtime: `codex-cli 0.155.0-alpha.9.2`
Result: `GREEN implementation / pending independent review`

## Production package at the exact subject

The exact subject introduces the same-repository Codex package required by PWCP-P3 M02:

- `.agents/plugins/marketplace.json` exposes marketplace `project-workflow` with exactly one plugin, `pw`, whose local source is `.` (the repository root).
- `.codex-plugin/plugin.json` identifies `pw` version `0.1.0`, exposes `./skills/`, and does not declare a duplicate hook path or unsupported validator field.
- `skills/project-workflow/SKILL.md` is the only bundled normal Skill. Its frontmatter name is `project-workflow`; current Codex therefore exposes it as `pw:project-workflow` / `$pw:project-workflow`.
- `hooks/hooks.json` declares one plugin-owned `SessionStart` command using `$PLUGIN_ROOT/hooks/session-start.py`.
- `hooks/session-start.py` emits bounded SessionStart `additionalContext` that tells Codex to read workspace `PROJECT.md` and the installed canonical `workflow/CONTEXT_ROUTING.md`; it does not hard-code `codex_only` or `chatgpt_only`.
- `tests/test_codex_plugin_package.py` covers marketplace/root layout, manifest shape, one-Skill naming, thin canonical routing, SessionStart output, canonical workflow update propagation without Skill edits, and absence of plugin-local updater surfaces.

No Project Workflow policy was copied into the Skill or bootstrap. The existing repository `workflow/` tree remains the canonical policy source.

## Deterministic repository test

A clean clone of `feat/project-workflow-codex-plugin` at the exact subject was tested on the connected Tower host:

```text
HEAD = 6e16ba11293bbdb7bbc8d96167e8280273d77304
python3 -m unittest discover -s tests -p "test_*.py"

..............
----------------------------------------------------------------------
Ran 14 tests in 0.022s

OK
```

The new update-propagation test stages `skills/` and `workflow/`, changes only `workflow/codex_only/ROUTER.md`, and verifies the bundled Skill hash remains unchanged. Combined with marketplace source `.`, this proves the canonical workflow tree is carried by the same package root without a Skill synchronization requirement.

## Current Codex validator

The official bundled `plugin-creator/scripts/validate_plugin.py` from `codex-cli 0.155.0-alpha.9.2` was run in a disposable Python venv because Tower's system Python did not include PyYAML.

Result:

```text
Plugin validation passed: /tmp/pwcp-m02-smoke
```

No production or user environment was modified by the validator.

## Isolated local marketplace/runtime smoke

Using a disposable `CODEX_HOME=/tmp/pwcp-m02-codex-home-20260920a` and a disposable npm cache, native current-runtime commands accepted the production repository package:

1. `codex plugin marketplace add /tmp/pwcp-m02-smoke --json`
   - marketplaceName: `project-workflow`
   - installedRoot: the source repository root
2. `codex plugin list --available --json`
   - pluginId: `pw@project-workflow`
   - version: `0.1.0`
   - installPolicy: `AVAILABLE`
3. `codex plugin add pw@project-workflow --json`
   - installed cache: `.../plugins/cache/project-workflow/pw/0.1.0`
4. `codex plugin list --json`
   - `installed: true`
   - `enabled: true`

Native App Server `skills/list` against the same isolated state returned:

```text
name: pw:project-workflow
pluginId: pw@project-workflow
enabled: true
path: .../plugins/cache/project-workflow/pw/0.1.0/skills/project-workflow/SKILL.md
errors: []
```

Native `hooks/list` returned the production SessionStart declaration from the installed cache:

```text
key: pw@project-workflow:hooks/hooks.json:session_start:0:0
eventName: sessionStart
handlerType: command
command: python3 "$PLUGIN_ROOT/hooks/session-start.py"
source: plugin
pluginId: pw@project-workflow
enabled: true
trustStatus: untrusted
errors: []
```

The default `untrusted` readback is expected and preserves the M01 explicit hook-trust contract; this M02 verification did not bypass or mutate live trust state.

The installed production bootstrap was then executed with `PLUGIN_ROOT` set to the installed cache root. Its JSON parsed successfully as SessionStart output, stayed within the 900-character bound, referenced workspace `PROJECT.md` and the installed canonical `workflow/CONTEXT_ROUTING.md`, and contained neither `codex_only` nor `chatgpt_only`.

## Git-backed marketplace/runtime smoke

A second fresh isolated `CODEX_HOME=/tmp/pwcp-m02-git-codex-home-20260920a` used the actual Git source:

```text
codex plugin marketplace add elmakus/chatgpt-codex-project-workflow \
  --ref feat/project-workflow-codex-plugin --json
```

Readback proved:

- marketplace source type: `git`;
- source URL: `https://github.com/elmakus/chatgpt-codex-project-workflow.git`;
- marketplace name: `project-workflow`;
- plugin `pw@project-workflow` available, then installed and enabled;
- fetched marketplace HEAD: `6e16ba11293bbdb7bbc8d96167e8280273d77304`.

Installed-cache hashes matched the fetched Git source at that exact subject:

```text
SKILL.md
6d2ab5358212c633f26ef3620f39d4c95179b48b9a5aec3f30cb9adf636b4d72

workflow/codex_only/ROUTER.md
c2e09ebb6006fb6a775c0fe9a6fe618afb51640b3e8fd5a2e8bb4280375175cf
```

This proves the Git-backed package installs the canonical workflow file together with the unchanged thin Skill. Generic marketplace refresh/update behavior remains qualified platform evidence reused under PWCP-REQ-012; M02's project-specific delta is the proven repo-root packaging and no-Skill-edit source topology.

## Live-state boundary

Verification used only:

- disposable clones under `/tmp`;
- disposable `CODEX_HOME` directories under `/tmp`;
- a disposable npm cache under `/tmp`;
- a disposable Python venv under `/tmp`.

The user's live Codex marketplace registration, plugin installation, hook trust/config state, and normal `~/.codex` state were not mutated.

## Acceptance mapping

1. Git-backed marketplace source installs/enables: GREEN.
2. Current validator-compatible root plugin manifest: GREEN.
3. Exactly one bundled `project-workflow` Skill and native `pw:project-workflow` discovery: GREEN.
4. Thin Skill delegates through workspace `PROJECT.md` + canonical router without copied policy: GREEN.
5. Bounded installed-root SessionStart bootstrap with no hard-coded execution policy: GREEN.
6. Canonical `workflow/codex_only/*` update path requires no Skill-content edit: GREEN via deterministic topology test + exact Git/install hash readback + reused generic update mechanism.
7. No plugin-local updater/timer/poller: GREEN.
8. Isolated current-runtime production package smoke: GREEN.

The implementation subject is ready for the Card's RECOMMENDED independent exact-subject review.
