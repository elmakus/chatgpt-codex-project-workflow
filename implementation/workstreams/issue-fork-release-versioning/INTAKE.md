# Issue Intake — Fork release version lineage

- Workstream ID: `issue-fork-release-versioning`
- Intake kind: `issue`
- Branch: `fix/fork-release-versioning`
- Integration target: `main`
- Base ref: `f3cdb60367da3e978397409b51c37faa181d613f`
- Classification: independent
- Intake state: active

## Operator intent

Correct Project Workflow behavior for releases of downstream forks. The observed agents currently publish fork-local changes by incrementing the upstream-looking SemVer patch number. The preferred model is the one already used by `elmakus/codex_workflow`: retain the upstream version as the lineage base and append a private revision suffix.

## Baseline evidence

- `elmakus/codex-chatgpt-web` is a fork of `miuuyy/codex-chatgpt-web`.
- Upstream's latest published release at intake time is `v5.0.8` (published 2026-09-16).
- The fork currently has published releases `v5.0.8`, `v5.0.9`, `v5.0.10`, `v5.0.11`, `v5.0.12`, and `v5.0.13`; latest is `v5.0.13` (published 2026-09-20).
- Therefore fork-local releases already occupy version numbers that can later be used by upstream, and the tag alone no longer identifies which upstream baseline the fork actually contains.
- `elmakus/codex_workflow` demonstrates the desired lineage form with releases such as `v1.1.17-private.12`.

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

## Proposed contract direction

Recommended naming shape:

```text
v<upstream-version>-private.<fork-revision>
```

Example:

```text
v5.0.8-private.1
v5.0.8-private.2
v5.0.8-private.3
```

When the fork is deliberately rebased/aligned to a new upstream release, the upstream component changes and the private counter restarts:

```text
v5.0.9-private.1
```

Recommended supporting provenance:
- record the exact upstream repository, upstream tag/version, and upstream commit SHA in release metadata;
- never consume a future upstream-looking version number merely for a fork-local change;
- keep the GitHub `prerelease` quality flag separate from the `-private.N` lineage suffix rather than inferring one from the other.

## Migration concern

Existing published `v5.0.9`–`v5.0.13` tags are already durable external references. Rewriting/deleting them would damage provenance and may break existing URLs/checksums. The preferred migration is therefore to preserve them as legacy releases and make resolvers/updaters explicitly understand the new fork-version lane, instead of sorting all historical tags as ordinary SemVer.

This migration detail matters because SemVer gives `5.0.8-private.1` lower precedence than `5.0.8`, while the already-published legacy `5.0.13` would sort above both. A generic "highest SemVer wins" resolver is therefore not sufficient after migration.

## Path classification

This does **not** qualify as a micro-fix. It changes accepted workflow behavior for release/version publication and migration semantics, so the smallest correct downstream route is Project Definition.

Provisional route:
- path: `project_definition`
- next_route: `project_definition:fork-release-versioning`

## Unresolved strategic gate

Before Intake can complete, user authority is required for the exact publication contract, especially:

1. adopt `v<upstream>-private.<N>` as the canonical fork-release naming rule;
2. preserve already-published legacy tags/releases rather than rewriting them;
3. require release consumers/resolvers to select the fork release lane explicitly rather than generic max-SemVer;
4. keep GitHub `prerelease` status independent from the `private` suffix.

Until that authority is explicit, this Intake remains active and no implementation contract is created.
