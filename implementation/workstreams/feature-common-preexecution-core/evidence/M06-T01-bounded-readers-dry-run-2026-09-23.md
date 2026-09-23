# M06-T01 — bounded V1 readers and deterministic dry run

Date: 2026-09-23
Result: GREEN

## Exact target

- Repository: `elmakus/project_workflow_v2`
- Branch: `feat/pwv2-m06-migration`
- Commit: `026b784a6ab45bd65f4d6841f98d4371b39ee1ce`
- Tree: `ce56d3e8efda6d77ca1640a3a9d936643e9dbca8`
- Draft PR: #6
- Base: `main@27b9132e173850e7d596092e023b0af7e0507472`

## Implemented bounded surface

`tools/v1_migration.py` implements a dependency-free bounded YAML reader and mutation-free dry-run planner for exactly:
- `chatgpt_workstream_yaml_v1`;
- `codex_workstream_yaml_v1`;
- `legacy_root_yaml_v1`.

The fixture origin manifest records exact real V1 source commits and Git blobs selected during M06 Execution Prep. The dry run:
- requires expected and observed source commit identity to match;
- validates the finite V1 manifest/board semantic shape;
- always maps live destination state under one V2 workstream directory;
- emits deterministic source fingerprint, destination, mapping and outstanding obligations;
- treats more than one active/in-progress Card as a blocker and chooses no winner;
- fails closed on unknown source class, unknown semantic fields, branch/workstream mismatch, racing source identity and terminal review without an exact V1 review subject;
- performs no source/destination writes.

No conversion/apply semantics were added in T01.

## Verification

GitHub Actions:
- run `35841918124`: completed / success;
- job `107118750956`: completed / success;
- repository checks ran `sh scripts/test.sh`.

Readback from the job log:
- state-contract suite: 28/28 GREEN;
- router suite: 39/39 GREEN;
- execution: 4/4 GREEN;
- review: 1/1 GREEN;
- recovery: 2/2 GREEN;
- final combined unittest group (close/fork/delivery plus new migration dry-run tests): 49/49 GREEN;
- existing package/shell probes also PASS.

PR #6 readback after the run: open/draft, exact head `026b784a6ab45bd65f4d6841f98d4371b39ee1ce`, exact base `27b9132e173850e7d596092e023b0af7e0507472`, mergeable.

## Acceptance

M06-T01 acceptance is GREEN. A02/A03/A15/A17 foundations affected by the reader/dry-run boundary are covered without adding any ordinary V2 dependency on V1 readers. Safe semantic conversion remains owned by M06-T02.
