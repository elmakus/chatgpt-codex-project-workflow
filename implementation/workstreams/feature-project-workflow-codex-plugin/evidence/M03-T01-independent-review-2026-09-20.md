# M03-T01 Independent Review — 2026-09-20

Card: `M03-T01 — Verify always-on lifecycle, isolation and intake UX`
Review subject: `54e142f46571db110a155e0b1efdf5c7afcdfac3`
Reviewer role: fresh normal ChatGPT, independent from implementation
Verdict: `GREEN`

## Authority and scope

Reviewed against:
- `implementation/workstreams/feature-project-workflow-codex-plugin/cards/M03-T01.md`;
- `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md` R3, PWCP-REQ-004/005/006/007/008/009/010/012/014;
- `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_PACKAGING.md`;
- `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_ACTIVATION.md`;
- `planning/PROJECT_WORKFLOW_CODEX_PLUGIN_MASTER_PLAN.md` PWCP-P3 M03;
- accepted M02 acceptance/handoff and the exact M03 implementation evidence.

The immutable reviewed subject remained `54e142f46571db110a155e0b1efdf5c7afcdfac3`. The production plugin under lifecycle test remains exact M02 subject `6e16ba11293bbdb7bbc8d96167e8280273d77304`.

## Independent inspection

The exact M03 subject adds the lifecycle/isolation/intake evidence while leaving the production plugin package unchanged from the accepted M02 subject. The evidence covers ordinary enabled-repository activation, a matched disabled control, same-thread resume, native compaction with a post-compaction bootstrap, bounded progressive disclosure, comparative intake routing, explicit Skill entry, isolated hook-trust bypass, package regression, and no live Codex-state mutation.

The accepted activation decision permits `#feature/#issue` when they reliably reach canonical Intake; the recorded current-runtime comparison shows both directives reaching Intake while the Skill-argument forms do not. Selecting `#feature/#issue` therefore follows the accepted decision and does not create an unsupported alias Skill or duplicate policy surface.

## Independent verification

On the connected Tower host, a fresh disposable review workspace checked out the exact review subject and reproduced:

```text
HEAD=54e142f46571db110a155e0b1efdf5c7afcdfac3
python3 -m unittest discover -s tests -p "test_*.py"

..............
----------------------------------------------------------------------
Ran 14 tests in 0.021s

OK

codex-cli 0.155.0-alpha.9.2
```

A separate exact M02 package worktree was installed through a disposable `CODEX_HOME`. Native plugin readback reproduced `pw@project-workflow` version `0.1.0`.

The plugin was then globally disabled in that disposable home and enabled only by the trusted enabled repository's repo-local `.codex/config.toml`. Native readback reproduced:
- enabled repository: `installed: true`, `enabled: true`;
- matched control repository: `installed: true`, `enabled: false`.

Direct execution of the installed SessionStart hook reproduced a bounded canonical bootstrap:
- `hookEventName=SessionStart`;
- context length 573 characters for this disposable installed path (below the 900-character bound; absolute path length explains the difference from the implementation run);
- contains `PROJECT.md` and `workflow/CONTEXT_ROUTING.md`;
- contains neither `codex_only` nor `chatgpt_only`.

Current-runtime generated App Server protocol schemas independently expose `skills/list`, `hooks/list`, `thread/resume`, and `thread/compact/start`, matching the lifecycle mechanism recorded by the immutable M03 evidence.

The current Tower CLI had no active model login during this review, so the reviewer did not fabricate or mutate credential state merely to repeat model turns. The immutable M03 evidence's exact ordinary-prompt/resume/compaction/intake traces were instead checked against the independently reproduced package, enablement/isolation, hook output, protocol capabilities, router semantics, and repository regression suite. No inconsistency was found.

All reviewer-created runtime state was disposable under `/tmp`; no live Codex marketplace/plugin/config/trust state was changed.

## Verdict

`GREEN`.

The exact M03-T01 review subject satisfies the accepted Card authority and acceptance surface. No corrective route is required. Per Project Workflow, the Card remains non-terminal until deterministic post-review finalization.
