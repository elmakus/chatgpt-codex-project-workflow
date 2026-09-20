# M02-T01 Independent Review — 2026-09-20

Card: `M02-T01 — Implement same-repo Codex plugin package`
Review subject: `6e16ba11293bbdb7bbc8d96167e8280273d77304`
Reviewer role: fresh normal ChatGPT, independent from implementation
Verdict: `GREEN`

## Authority and scope

Reviewed against:
- `implementation/workstreams/feature-project-workflow-codex-plugin/cards/M02-T01.md`;
- `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md` R3, including PWCP-REQ-001/002/003/010/011/013/015 and the preserved M01 activation/trust/isolation constraints;
- `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_PACKAGING.md`;
- `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_ACTIVATION.md`;
- `planning/PROJECT_WORKFLOW_CODEX_PLUGIN_MASTER_PLAN.md` PWCP-P3 M02;
- accepted M01 handoff/acceptance/runtime evidence.

The immutable reviewed implementation subject remained `6e16ba11293bbdb7bbc8d96167e8280273d77304`.

## Independent inspection

Inspected the exact subject package surfaces:
- `.agents/plugins/marketplace.json`;
- `.codex-plugin/plugin.json`;
- `skills/project-workflow/SKILL.md`;
- `hooks/hooks.json`;
- `hooks/session-start.py`;
- `tests/test_codex_plugin_package.py`;
- implementation evidence and the M01 accepted mechanism contract.

Findings:
- marketplace `project-workflow` contains one plugin `pw` whose source is the repository root;
- plugin manifest exposes `./skills/` and no duplicate hook field;
- exactly one bundled normal Skill exists, named `project-workflow`, and it remains a thin router through workspace `PROJECT.md` plus canonical `workflow/CONTEXT_ROUTING.md`;
- SessionStart uses `$PLUGIN_ROOT/hooks/session-start.py`, emits bounded `additionalContext`, and hard-codes neither execution policy;
- no plugin-local updater/timer/poller surface was introduced;
- M03-owned lifecycle/intake-UX work is not incorrectly claimed as M02 acceptance.

No acceptance or authority conflict was found.

## Independent verification

A clean checkout of the exact subject on the connected Tower host produced:

```text
HEAD=6e16ba11293bbdb7bbc8d96167e8280273d77304
python3 -m unittest discover -s tests -p "test_*.py"

..............
----------------------------------------------------------------------
Ran 14 tests in 0.025s

OK
```

The host had no global `codex` command in PATH, so the review invoked the exact accepted runtime through an isolated npm cache:

```text
npx -y @openai/codex@0.155.0-alpha.9.2 --version
codex-cli 0.155.0-alpha.9.2
```

Using a disposable `CODEX_HOME`, the exact reviewed repository was added as a local marketplace. Native readback showed `pw@project-workflow` available, then installed and enabled at version `0.1.0`. The installed SessionStart bootstrap emitted `hookEventName=SessionStart`, context length 569, references to `PROJECT.md` and `workflow/CONTEXT_ROUTING.md`, and neither `codex_only` nor `chatgpt_only`.

Installed-cache SHA-256 hashes matched the exact source for both:
- `skills/project-workflow/SKILL.md`: `6d2ab5358212c633f26ef3620f39d4c95179b48b9a5aec3f30cb9adf636b4d72`;
- `workflow/codex_only/ROUTER.md`: `c2e09ebb6006fb6a775c0fe9a6fe618afb51640b3e8fd5a2e8bb4280375175cf`.

All runtime checks used disposable `/tmp` checkout/cache/CODEX_HOME state. No live Codex marketplace, plugin, trust or config state was mutated.

## Verdict

`GREEN`.

The exact M02-T01 subject satisfies its accepted authority and Card acceptance surface. No corrective route is required. Per Project Workflow, the Card remains non-terminal until the router assigns deterministic post-review finalization.
