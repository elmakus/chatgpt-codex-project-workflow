# M01-T01 — Target baseline evidence

Date: 2026-09-22
Card: `M01-T01`
Target repository: `elmakus/project_workflow_v2`
Target default branch: `main`
Target implementation branch: `feat/pwv2-m01-foundation`

## Result

GREEN.

Exact root initialization commit:
`3b3e1198bdd7f7f145fc1d05bbd89f1a4a62a46d`

Exact M01 baseline implementation commit:
`2ca48653b19e5641cbc2d0edb7ba871b84aff99d`

## External readback

Immediately before initialization, GitHub returned:
- branches: none;
- commits: repository empty (409);
- visibility: private.

After initialization:
- `main` resolves to `3b3e1198bdd7f7f145fc1d05bbd89f1a4a62a46d`;
- root `main` contents read back as an empty tree;
- `feat/pwv2-m01-foundation` initially resolved to the same root before product writes;
- after the baseline write it resolves to `2ca48653b19e5641cbc2d0edb7ba871b84aff99d`;
- repository visibility remains `private`.

Target feature-branch root entries after the baseline commit:
- `.github/`
- `README.md`
- `docs/`
- `scripts/`

Exact baseline files read back from GitHub:
- `.github/workflows/test.yml`
- `README.md`
- `docs/CONSTRUCTION_AUTHORITY.md`
- `scripts/test.sh`

No target-side live construction Task Board was created.

## Test

Command executed on the target checkout:

`sh scripts/test.sh`

Result:

`M01 baseline checks: PASS`

The test verifies the baseline authority files exist and rejects:
- root `implementation/TASK_BOARD.yaml`;
- construction-workstream Task Board in the target repository;
- V1-style `workflow/chatgpt_only` and `workflow/codex_only` semantic trees.

A first attempt used `make test`, but the Tower runtime has no `make`. No product commit had been pushed at that point. The test entry was simplified within L1 authority to `sh scripts/test.sh`, and CI uses that same command. This avoided adding a tool dependency solely for the baseline.

At readback time GitHub combined commit status reported no status records yet for the feature commit. This is not recorded as a CI PASS; the required local baseline test is independently recorded above and the CI workflow bytes were read back from GitHub.

## Custody

The sole mutable construction Task Board remains:
`elmakus/chatgpt-codex-project-workflow@feat/common-preexecution-core:implementation/workstreams/feature-common-preexecution-core/TASK_BOARD.yaml`.

The target repository contains product baseline/provenance only. No production adoption, migration, plugin replacement or custody transfer occurred.
