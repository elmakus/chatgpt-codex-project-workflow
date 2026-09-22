# M01 target integration access blocker

Date: 2026-09-22
Workstream: `feature-common-preexecution-core`
Milestone: `M01`
State: `resolved`

## Exact pending operation

Integrate the independently reviewed target subject through the approved construction path:

- repository: `elmakus/project_workflow_v2`
- head branch: `feat/pwv2-m01-foundation`
- exact reviewed head: `f1f4ed87875877529da6dc954e785d6373de7930`
- base branch: `main`
- base observed before PR attempt: `3b3e1198bdd7f7f145fc1d05bbd89f1a4a62a46d`
- independent review: GREEN (`M01-T05` R01)

No existing PR for this repository was returned by the available GitHub PR listing before the create attempt.

## Blocker

The connected GitHub integration returned HTTP 403 when creating the PR:

`Resource not accessible by integration`

The Tower checkout has authenticated Git-over-SSH push access, but no authenticated GitHub API/CLI surface capable of opening the required PR. Direct push/merge to `main` is intentionally not used because approved PWV2-P1 construction authority requires reviewed branch -> PR -> integration after the empty-root initialization exception.

## Retry — 2026-09-22

A fresh target readback before the retry verified:

- target `main` is still exactly `3b3e1198bdd7f7f145fc1d05bbd89f1a4a62a46d`;
- target `feat/pwv2-m01-foundation` is still exactly the reviewed `f1f4ed87875877529da6dc954e785d6373de7930`;
- the feature branch is 6 commits ahead and 0 behind `main`;
- no existing pull request was returned for `elmakus/project_workflow_v2`.

The connected GitHub integration then retried creation of `feat/pwv2-m01-foundation -> main` and again returned HTTP 403:

`Resource not accessible by integration`

No target branch, reviewed subject, PR or `main` state was mutated by the failed attempt. Because the exact reviewed head and target baseline are unchanged, this retry does not itself invalidate M01-T05 R01 GREEN.

## Diagnostic refinement — 2026-09-22

The retry was narrowed to a repository-specific Pull Requests API authorization failure rather than a general GitHub/ChatGPT write outage:

- the ChatGPT GitHub App installation for account `elmakus` reports `repository_selection: all`;
- `elmakus/project_workflow_v2` is listed by that installation and repository metadata reports the user has admin/push access;
- ChatGPT's GitHub app-specific permission mode is `Allow all actions`;
- on private `elmakus/newproject-skill`, a deliberately invalid `create_pull_request` probe reached GitHub endpoint validation and returned HTTP 422 `head: invalid`, proving the same connector currently reaches the PR-create endpoint with sufficient authorization there;
- the same deliberately invalid PR-create probe against `elmakus/project_workflow_v2` returned HTTP 403 `Resource not accessible by integration` before head validation;
- non-mutating write-authority probes against `project_workflow_v2` reached normal GitHub validation: recreating existing branch `main` returned 422 `Reference already exists`, and creating existing `README.md` without its SHA returned 422 `sha wasn't supplied`.

Therefore the connector is not generally read-only and the target repository is not absent from the installation. The failure is isolated to the Pull Requests write authorization path for this repository. GitHub documents PR creation as requiring repository permission `Pull requests: write`; the connector does not expose the response's accepted-permission headers, so the exact internal token/grant mismatch cannot be read directly. Given that this is a newly created repository while older private repositories pass the same PR endpoint authorization check, the leading diagnosis is stale or inconsistent per-repository GitHub App token/grant propagation or connector credential selection for the new repository, not a Project Workflow or branch-state defect.

## Resolution — 2026-09-22

After the GitHub connection was repaired, the exact reviewed target refs were re-read unchanged. PR #1 was then created successfully and merged with expected head `f1f4ed87875877529da6dc954e785d6373de7930`.

Post-merge readback verified target `main` at `8c955d1d9e8ba9396582753814d5b6c3283dde01`, with no file changes between the reviewed head and integrated target beyond the merge commit.

Durable integration evidence:
`implementation/workstreams/feature-common-preexecution-core/evidence/M01-target-integration-2026-09-22.md`

## Historical recovery / user action

Resolve exactly one of:

1. grant the connected GitHub integration write/PR access to `elmakus/project_workflow_v2`; or
2. manually create and merge a PR from `feat/pwv2-m01-foundation` into `main` while the head is still exactly `f1f4ed87875877529da6dc954e785d6373de7930`.

After access/action is available, Recovery must read back the exact PR/merge result and target `main` before marking M01 complete or materializing M02 Cards. If either branch moved, do not assume the prior review still covers the integration; perform the approved target-refresh compatibility check first.
