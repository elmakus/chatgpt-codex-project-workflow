# Decision — Downstream forks use upstream-anchored private release versions

- Decision ID: `ADR-FRV-001`
- Date: `2026-09-20`
- Updated: `2026-09-21`
- Status: `accepted`
- Authority: `user/product`
- Supersedes: `none`
- Related requirements: `requirements/FORK_RELEASE_VERSIONING.md`
- Related milestone/card: `none`

## Context

A downstream fork previously published local releases by incrementing the apparent upstream SemVer patch number. That scheme conflates upstream lineage with downstream release iteration, can consume version numbers that upstream may later publish, and makes a tag insufficient to identify the actual upstream baseline.

The accepted `v<upstream>-private.<N>` convention fixes release identity, but a second defect remains if downstream tooling uses generic SemVer precedence to choose the fork's current/update release. SemVer intentionally treats `X.Y.Z-private.N` as lower than `X.Y.Z`, so ordinary max-SemVer does not represent the fork's canonical release channel.

Some publication systems also expose a native moving alias such as a container-registry `latest` tag. That convenience alias must remain separate from immutable release identity.

## Decision

For downstream forks governed by Project Workflow, the canonical fork-local release version remains:

```text
v<upstream-version>-private.<N>
```

where:

- `<upstream-version>` is the exact accepted upstream release/version baseline actually contained by the fork;
- `N` is a positive fork-local revision in that exact baseline's independent lane.

Fork-local work never advances the upstream component. Every canonical downstream release records the exact upstream repository, upstream tag/version and upstream commit SHA.

Existing historical releases that used upstream-looking versions remain untouched as legacy provenance. They are not retagged, deleted or retroactively mapped into the private counter.

### Baseline-local next release

When choosing the next release for an accepted baseline `X.Y.Z`:

1. accept only exact canonical tags `vX.Y.Z-private.N` with positive integer `N`;
2. ignore upstream-only, legacy upstream-looking, malformed and other-baseline tags;
3. choose `private.1` when that baseline has no canonical private release;
4. otherwise choose numeric `max(N)+1`.

### Canonical fork-channel order

When a resolver/update channel needs the current canonical fork release across baselines, it must first restrict candidates to exact canonical `vX.Y.Z-private.N` releases and then compare the numeric tuple:

```text
(X, Y, Z, N)
```

This is a fork-domain ordering rule, not generic SemVer precedence.

For example:

```text
v1.1.17-private.99
v1.1.18-private.4
v1.1.18-private.10
v1.1.19-private.1
```

orders canonically as:

```text
v1.1.19-private.1
> v1.1.18-private.10
> v1.1.18-private.4
> v1.1.17-private.99
```

An upstream-only `v1.1.18` or a legacy upstream-looking fork tag does not enter that canonical fork-channel order.

### Moving `latest` alias

A publication surface that natively supports moving aliases may expose `latest` as a convenience channel.

When used:

- `latest` points to the newest accepted **stable** canonical fork release according to the canonical fork-channel order plus the project's release-quality policy;
- the immutable/versioned canonical reference remains published and is the authority for reproducibility and rollback;
- the alias resolves to the same released artifact/content identity as the canonical version it names at that publication point;
- `latest` is not a canonical version and does not create a synthetic Git release/tag such as `vlatest`;
- systems without native moving-alias semantics continue to use the canonical versioned release and their normal release-discovery mechanism.

The `private` suffix itself still identifies downstream lineage, not release quality. GitHub's `prerelease` flag or equivalent quality metadata remains independent.

## Rationale

This model:

- keeps the actual upstream baseline visible in every downstream release;
- prevents fork-local work from impersonating future upstream versions;
- gives deterministic numeric ordering inside each baseline lane;
- gives deterministic cross-baseline ordering for the fork's own update/current channel;
- removes generic SemVer precedence from a domain where it represents the wrong semantics;
- allows convenient floating aliases without weakening immutable release identity;
- preserves historical release provenance instead of rewriting published artifacts;
- separates lineage, release ordering and release quality.

## SemVer consequence

The chosen syntax is valid SemVer prerelease syntax, so standard SemVer precedence treats `5.0.8-private.1` as lower than `5.0.8`. It also treats historical legacy `5.0.13` as higher than either.

That ordering remains correct **as SemVer**, but it is not the accepted ordering for the downstream fork's canonical private release channel. Project Workflow and downstream tooling therefore must not use generic max-SemVer for fork-channel selection. They parse the canonical fork identity first and apply the accepted fork-domain ordering.

## Alternatives considered

### Keep incrementing normal SemVer patch numbers

Rejected because it hides the true upstream baseline and collides conceptually with future upstream releases.

### Add another numeric component, for example `5.0.8.1`

Rejected because it is not SemVer 2.0.0 and blurs the boundary between upstream identity and fork-local revision.

### Use build metadata, for example `5.0.8+private.1`

Rejected because SemVer ignores build metadata for precedence, and some downstream surfaces such as container tags do not accept `+` uniformly.

### Use a fork-specific suffix such as `-elmakus.1`

Technically valid, but not selected because `-private.N` is already the established local convention.

### Use generic SemVer sorting and special-case equal baselines

Rejected because it leaves the fundamental domain mismatch in place and can fail again in other resolvers/update channels.

### Publish a Git tag/release named `latest` or `vlatest`

Rejected because a moving alias is channel metadata, while Git release/tag identity should remain immutable and versioned.

### Rewrite legacy tags to the new scheme

Rejected because published tags/releases are durable external provenance and may be referenced by release URLs, installers and checksums.

## Consequences

- Project Workflow has one canonical fork-domain version identity and ordering contract.
- Release resolvers/installers that currently choose the numerically highest SemVer need to parse canonical private releases and use fork-domain ordering.
- Existing legacy/upstream-only tags remain visible but are excluded from canonical fork-channel ordering.
- A deliberate upstream upgrade changes the upstream component; that baseline continues its own private lane.
- Publication systems with native moving aliases may maintain `latest`, while immutable versioned references remain authoritative.
- Downstream projects adopt implementation changes through their own managed workstreams; this workflow change does not directly mutate them.
- Tests must cover mixed legacy/private/upstream tag sets, numeric multi-digit private revisions, cross-baseline ordering and moving-alias boundaries.

## Required authoritative updates

- Requirements / Project Definition: `requirements/FORK_RELEASE_VERSIONING.md`.
- Planning: extend the existing fork-release plan with canonical fork-channel ordering and moving-alias semantics.
- Task Card/OpenSpec: materialize during Execution Prep for the new behavior contract.
- PROJECT.md: no project-global mutable pointer required; branch-isolated workstream authority remains manifest-owned.

## Provenance

- Original accepted direction: user discussion on 2026-09-20 establishing upstream-anchored `private.N` releases.
- Extension accepted on 2026-09-21: keep `X.Y.Z-private.N`, fix ordering systemically rather than by repo-specific SemVer exceptions, and support `latest` as a moving alias where the publication surface natively supports it.
- Strategic `request_id`: none.
- Exact `DECISION FOR CODEX:` marker: none.
- Persisting commit: recorded by Git history.
