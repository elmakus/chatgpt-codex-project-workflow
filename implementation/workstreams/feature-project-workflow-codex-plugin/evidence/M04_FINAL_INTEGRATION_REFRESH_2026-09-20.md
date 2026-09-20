# M04 Final Integration Refresh — 2026-09-20

Workstream: `feature-project-workflow-codex-plugin`
Integration target: `main`
Refresh result: `GREEN`

## Exact refresh subjects

- Pre-refresh workstream head: `09e9b528c65d890607cbdfed2f4beb1ace2fefa2`.
- Current target read at refresh: `edb83e0c6c7ed06dcfce6df1e711fc3363d62d06`.
- Prior merge base: `cdaf47245e45836917b152904d70807bca355e7d`.
- Refresh merge commit: `bde88f919c0d26326949a757223f146e9b1e6976`.
- Refresh merge tree: `305d43de76b8bfdb637ad43616ca1f480a6e9088`.
- Merge parents, in order:
  - `09e9b528c65d890607cbdfed2f4beb1ace2fefa2`;
  - `edb83e0c6c7ed06dcfce6df1e711fc3363d62d06`.

GitHub readback after the merge reports the workstream branch `ahead` of `main`, `behind_by: 0`, with merge base equal to the refreshed target `edb83e0c6c7ed06dcfce6df1e711fc3363d62d06`.

## Reconciliation

The current target had materially moved since the workstream creation base, so Close ran the required current-target reconciliation rather than freezing a stale final-review subject.

A trial merge exposed exactly one textual conflict: root `PROJECT.md`. Current `main` now owns the branch-first integrated-project contract under which root `PROJECT.md` must not mirror workstream-local live routing/execution state. The conflict was therefore resolved to the current-`main` root `PROJECT.md`. The plugin workstream's live authority and state remain correctly namespaced in:
- `implementation/workstreams/feature-project-workflow-codex-plugin/WORKSTREAM.yaml`;
- its selected `TASK_BOARD.yaml`;
- its requirements/decisions/plan/evidence.

`README.md` merged cleanly and retained the M04 link to `docs/CODEX_PLUGIN.md`.

The exact remote merge tree was constructed and checked against the independently prepared local reconciliation tree. Both were exactly `305d43de76b8bfdb637ad43616ca1f480a6e9088`.

## Compatibility verification after refresh

A fresh clone of the remote workstream branch at exact head `bde88f919c0d26326949a757223f146e9b1e6976` reproduced:

```text
......................................................................
----------------------------------------------------------------------
Ran 70 tests in 0.026s

OK
```

The larger 70-test suite includes the current-`main` branch-first/fixed-policy/fork-versioning contract tests in addition to the Project Workflow Codex plugin package tests.

Static/semantic audit on that exact refreshed remote subject:
- exactly one bundled Skill directory: `project-workflow`;
- neither Skill nor SessionStart bootstrap contains a copied policy-specific router body;
- no plugin-local updater/timer/poller file exists;
- current `workflow/codex_only/ROUTER.md` still contains `#issue`, `#feature` and canonical `INTAKE.md` routing;
- `docs/CODEX_PLUGIN.md` still documents `pw@project-workflow`, `$pw:project-workflow`, `#feature <description>`, `#issue <description>`, repo-local enabled/control semantics and canonical `workflow/CONTEXT_ROUTING.md`.

Current-runtime disposable install/readback at `codex-cli 0.155.0-alpha.9.2`:
- marketplace source accepted;
- `pw@project-workflow` version `0.1.0` installed and read back enabled;
- installed SessionStart hook returned `hookEventName=SessionStart`;
- injected context length was 578 characters for the disposable absolute path;
- context references `PROJECT.md` and `workflow/CONTEXT_ROUTING.md`;
- context contains neither `codex_only` nor `chatgpt_only` policy bodies.

All runtime writes were disposable under `/tmp`; no live Codex marketplace/plugin/config/trust state was changed.

## Semantic conclusion

The target reconciliation changes the canonical workflow tree to current `main` as required, but does not introduce an incompatible plugin wrapper, activation, intake, progressive-disclosure or update contract. The refreshed integrated workstream acceptance surface remains consistent with Definition R3, ADR-PWCP-001/002 and PWCP-P3.

The manifest-owned final-integration review must cover the refreshed closure-ready subject created after this evidence/acceptance/handoff state is persisted. No prior Card review is reused as whole-workstream final coverage.
