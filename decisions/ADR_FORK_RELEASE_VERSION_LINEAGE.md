# Decision — Downstream forks use upstream-anchored private release versions

- Decision ID: `ADR-FRV-001`
- Date: `2026-09-20`
- Status: `accepted`
- Authority: `user/product`
- Supersedes: `none`
- Related requirements: `requirements/FORK_RELEASE_VERSIONING.md`
- Related milestone/card: `none`

## Context

A downstream fork currently published local releases by incrementing the apparent upstream SemVer patch number. In the observed case, upstream `miuuyy/codex-chatgpt-web` is at `v5.0.8`, while the downstream fork published `v5.0.9` through `v5.0.13`.

That scheme conflates upstream lineage with downstream release iteration. It can also consume version numbers that upstream may later publish, and a tag no longer tells a user which upstream baseline the fork actually contains.

The existing `elmakus/codex_workflow` fork already uses an upstream-anchored private suffix such as `v1.1.17-private.12`, providing a useful established convention.

## Decision

For downstream forks governed by Project Workflow, the canonical fork-local release version is:

```text
v<upstream-version>-private.<N>
```

where:

- `<upstream-version>` is the exact accepted upstream release/version baseline actually contained by the fork;
- `N` is a positive monotonically increasing fork-local revision for that exact baseline.

Example:

```text
upstream baseline: v5.0.8

fork releases:
v5.0.8-private.1
v5.0.8-private.2
v5.0.8-private.3
```

After an intentional accepted alignment to upstream `v5.0.9`, the new lane begins at:

```text
v5.0.9-private.1
```

Fork-local work never advances the upstream component.

Every canonical downstream release records the exact upstream repository, upstream tag/version and upstream commit SHA.

Existing historical releases that used upstream-looking versions remain untouched as legacy provenance. They are not retagged, deleted or retroactively mapped into the private counter. If no canonical private release yet exists for the current baseline, migration starts at `private.1`; otherwise the next revision is `max(private.N)+1` for that baseline.

Release consumers/resolvers must select the private lane explicitly. Generic highest-SemVer across upstream, legacy and private tags is not a valid canonical selection algorithm.

The `private` suffix identifies downstream lineage, not release quality. GitHub's `prerelease` flag is independent and must be chosen according to the project's release-quality policy.

## Rationale

This scheme:

- makes the upstream baseline visible in every downstream release;
- prevents a fork from impersonating future upstream version numbers;
- gives deterministic ordering inside one fork/upstream lane;
- matches an already-established convention in another maintained fork;
- preserves historical release provenance instead of rewriting published artifacts;
- separates lineage from release quality.

## SemVer consequence

The chosen syntax is valid SemVer prerelease syntax, so standard SemVer precedence treats `5.0.8-private.1` as lower than `5.0.8`. It also treats historical legacy `5.0.13` as higher than either.

That ordering does not represent this fork's lineage semantics. Therefore Project Workflow and downstream tooling must not use generic max-SemVer to select the current fork release across mixed tag classes. They must first identify the accepted upstream baseline/private lane, then compare the numeric private revision inside that lane.

## Alternatives considered

### Keep incrementing normal SemVer patch numbers

Rejected because it hides the true upstream baseline and collides conceptually with future upstream releases.

### Use build metadata, for example `5.0.8+private.1`

Rejected because SemVer ignores build metadata for precedence, so `private.1` and `private.2` do not provide a useful ordered release lane to generic consumers.

### Use a fork-specific suffix such as `-elmakus.1`

Technically valid and more owner-specific, but not selected because `-private.N` is already the established convention in the maintained `codex_workflow` fork and provides one consistent local standard.

### Rewrite legacy tags to the new scheme

Rejected because published tags/releases are durable external provenance and may be referenced by release URLs, installers and checksums.

## Consequences

- Project Workflow needs one shared fork-release contract and publication-path integration.
- Release resolvers/installers that currently choose the numerically highest tag need lineage-aware selection.
- Existing legacy tags remain visible but are excluded from the canonical private counter.
- A deliberate upstream upgrade changes the upstream component and resets the private counter.
- Release notes/evidence gain exact upstream provenance fields.
- Tests must cover mixed legacy/private/upstream tag sets and SemVer edge behavior.

## Required authoritative updates

- Requirements / Project Definition: `requirements/FORK_RELEASE_VERSIONING.md`.
- Planning: add shared contract, publication-route integration and migration/resolver verification.
- Task Card/OpenSpec: materialize during Execution Prep; OpenSpec only if an executable parser/state interface warrants it.
- PROJECT.md: no project-global mutable pointer required; branch-isolated workstream authority is manifest-owned.

## Provenance

- Source discussion/request: user `#issue` about fork agents publishing upstream-looking release numbers, followed by explicit acceptance of the upstream-anchored `private.N` direction on 2026-09-20.
- Evidence: upstream `miuuyy/codex-chatgpt-web` latest release `v5.0.8`; downstream `elmakus/codex-chatgpt-web` legacy releases through `v5.0.13`; `elmakus/codex_workflow` established `v1.1.17-private.N` convention.
- Strategic `request_id`: none.
- Exact `DECISION FOR CODEX:` marker: none.
- Persisting commit: recorded by Git history.
