# Common Fork Release Versioning Contract

## Role

This policy-neutral contract governs release-version selection and validation only for projects that are durably established as downstream forks or equivalent upstream-derived projects.

It does not apply merely because two repositories use similar version numbers. Independent projects keep their own accepted versioning policy.

Publication modules MUST reference this contract instead of copying its lineage algorithm.

## Applicability and accepted upstream baseline

Before choosing or validating a downstream fork release version, establish from durable project/repository evidence:

1. the exact upstream repository;
2. the exact accepted upstream version/tag;
3. the exact upstream commit SHA represented by that accepted baseline.

A release MUST NOT claim a newer upstream baseline until that baseline is actually integrated and accepted.

The three values above form the release-lineage provenance tuple and must be retained in publication evidence.

## Canonical downstream release identity

For accepted upstream version `X.Y.Z`, a fork-local release uses:

```text
vX.Y.Z-private.N
```

where `N` is a positive integer private revision for that exact upstream baseline.

Fork-local work never increments or otherwise advances `X.Y.Z`.

### First migration / empty lane

If the accepted baseline has no existing canonical `vX.Y.Z-private.N` release, the next canonical fork release is:

```text
vX.Y.Z-private.1
```

Historical upstream-looking fork releases do not get renumbered into the new lane.

### Existing canonical lane

For the accepted baseline, consider only tags that exactly match `vX.Y.Z-private.N` with positive integer `N`.

The next private revision is numeric:

```text
max(N) + 1
```

For example, `v5.0.8-private.2` plus `v5.0.8-private.10` produces `v5.0.8-private.11`.

Do not use tag count, lexical ordering, or another baseline's private revisions.

### Accepted upstream-baseline change

When accepted upstream lineage moves to another version, that version has its own private lane.

If accepted lineage moves from `v5.0.8` to `v5.0.9` and no `v5.0.9-private.N` exists, the first release is `v5.0.9-private.1`.

If canonical private releases already exist for the newly accepted baseline, continue that baseline's own numeric lane rather than forcing `private.1`.

## Lineage-aware selection

Generic highest-SemVer selection across mixed upstream, legacy fork, and canonical private tags is forbidden as the canonical downstream resolver.

SemVer precedence treats `5.0.8-private.1` as lower than `5.0.8`, while a historical legacy tag such as `5.0.13` sorts above both. That ordering does not encode downstream lineage.

A downstream resolver therefore:

1. starts from the accepted upstream baseline;
2. selects only that baseline's canonical `-private.N` lane;
3. compares `N` numerically inside that lane.

Upstream tags, upstream-looking legacy fork tags, malformed private tags, and canonical private tags for another baseline do not participate in the current baseline's private counter.

## Legacy release immutability

Already-published fork releases/tags that used upstream-looking versions are immutable historical provenance.

Migration MUST NOT rewrite, delete, retag, or retroactively map them into the private counter.

Existing release URLs, checksums and references remain valid.

## Release quality is independent

The `private.N` suffix identifies downstream lineage and fork-local revision. It does not mean alpha, beta, unstable, or prerelease quality.

GitHub's release `prerelease` flag remains a separate publication-quality decision governed by the project's release policy.

## Publication-route obligation

When release-version selection or validation for a downstream fork is material, each supported Project Workflow publication path MUST load and apply this common contract:

- ChatGPT-only Close;
- Codex-only Close;
- legacy/shared Review and Handoff publication flow.

Those modules may add policy-specific routing, review, authorization and publication mechanics, but MUST NOT duplicate or alter the lineage algorithm here.

## Authorization and non-goals

This contract does not authorize:

- creating/pushing tags or releases;
- deployment or other live writes;
- deleting/moving historical tags;
- force-push;
- automatic upstream synchronization.

Existing review, acceptance, signing/checksum, external-write authorization and readback requirements remain in force.
