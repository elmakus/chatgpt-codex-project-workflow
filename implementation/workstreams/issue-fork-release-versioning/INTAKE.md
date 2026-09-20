# Issue Intake — Fork release version lineage

- Workstream ID: `issue-fork-release-versioning`
- Intake kind: `issue`
- Branch: `fix/fork-release-versioning`
- Integration target: `main`
- Base ref: `f3cdb60367da3e978397409b51c37faa181d613f`
- Classification: independent
- Intake state: complete

## Operator intent

Correct Project Workflow behavior for releases of downstream forks. The observed agents currently publish fork-local changes by incrementing the upstream-looking SemVer patch number. The accepted model is the one already used by `elmakus/codex_workflow`: retain the upstream version as the lineage base and append a private revision suffix.

## Baseline evidence

- `elmakus/codex-chatgpt-web` is a fork of `miuuyy/codex-chatgpt-web`.
- Upstream's latest published release at intake time is `v5.0.8` (published 2026-09-16).
- The fork currently has published releases `v5.0.8`, `v5.0.9`, `v5.0.10`, `v5.0.11`, `v5.0.12`, and `v5.0.13`; latest is `v5.0.13` (published 2026-09-20).
- Therefore fork-local releases already occupy version numbers that can later be used by upstream, and the tag alone no longer identifies which upstream baseline the fork actually contains.
- `elmakus/codex_workflow` demonstrates the accepted lineage form with releases such as `v1.1.17-private.12`.

## Dependency / base discovery

Relevant active workflow-repository branches at intake time:
- `feat/branch-first-managed-changes`
- `feat/project-workflow-codex-plugin`

No open PR or active branch is required to reproduce or define this issue. The defect is a missing/insufficient publication-versioning contract on current `main`, so this workstream is independent and bases directly on `main`.

## Diagnosis

The current release behavior conflates two different axes:

1. **upstream lineage** — which upstream version the fork is based on;
2. **fork revision** — how many fork-local releases have been produced from that upstream baseline.

Incrementing `5.0.8` to `5.0.9` for a fork-only change falsely makes the fork revision look like a newer upstream version. It also creates future tag collisions when upstream eventually publishes those versions.

## Accepted publication contract

User/product authority accepted on 2026-09-20:

1. canonical fork-local versions use `v<upstream-version>-private.<N>`;
2. fork-local work never advances the upstream component;
3. `N` increases inside one upstream baseline and restarts at `1` after an accepted upstream-baseline change;
4. exact upstream repository, tag/version and commit SHA are release provenance;
5. already-published upstream-looking fork releases are preserved as legacy history rather than rewritten/deleted;
6. release consumers/resolvers must select the canonical private lane explicitly rather than generic max-SemVer across mixed tag classes;
7. the `private` suffix identifies downstream lineage, not quality; GitHub `prerelease` is independent;
8. first migration to a baseline with no existing canonical private releases begins at `private.1`.

Canonical Definition authority:
- `requirements/FORK_RELEASE_VERSIONING.md` R1 — approved
- `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / `ADR-FRV-001` — accepted

## Migration concern

Existing published `v5.0.9`–`v5.0.13` tags are durable external references and remain untouched.

SemVer gives `5.0.8-private.1` lower precedence than `5.0.8`, while legacy `5.0.13` sorts above both. Therefore a generic "highest SemVer wins" resolver is explicitly outside the accepted contract.

## Path classification

This does **not** qualify as a micro-fix. It changes accepted workflow behavior for release/version publication and migration semantics.

- path: `project_definition`
- next_route: `strategic_planning:fork-release-versioning`

Project Definition is now complete and GREEN. The next legal route is Strategic Planning.
