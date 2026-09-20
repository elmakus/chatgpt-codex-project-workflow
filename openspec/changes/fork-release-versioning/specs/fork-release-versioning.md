# Specification — fork release versioning

## Requirement: applicability and baseline

The contract MUST apply only when durable project/repository authority establishes that the project is a downstream fork or equivalent upstream-derived project.

Before choosing or validating a downstream release version, the publication path MUST establish one accepted upstream baseline tuple:

- exact upstream repository;
- exact upstream version/tag;
- exact upstream commit SHA.

A coincidentally similar version string MUST NOT establish lineage, and a project MUST NOT claim a newer upstream baseline until that baseline is actually integrated and accepted.

## Requirement: canonical downstream version

For accepted upstream version `X.Y.Z`, a fork-local release MUST use `vX.Y.Z-private.N`, where `N` is a positive integer.

Fork-local work MUST NOT advance the `X.Y.Z` component.

### Scenario: first canonical release

Given accepted baseline `v5.0.8` and no canonical `v5.0.8-private.N` release, the next fork-local release is `v5.0.8-private.1`.

### Scenario: numeric lane increment

Given canonical releases `v5.0.8-private.2` and `v5.0.8-private.10`, the next release is `v5.0.8-private.11`.

The counter is numeric; tag count and lexicographic order MUST NOT determine it.

### Scenario: accepted baseline change

Given the accepted baseline changes from `v5.0.8` to `v5.0.9`, and no canonical private release exists on `v5.0.9`, the next release is `v5.0.9-private.1`.

A high private revision on another baseline MUST NOT affect the selected baseline's counter.

## Requirement: lane selection

The canonical counter MUST be computed only from tags matching the accepted baseline's canonical `vX.Y.Z-private.N` lane with a positive integer `N`.

Upstream tags, upstream-looking legacy fork tags, malformed private tags, and canonical private tags for another baseline MUST NOT participate in that counter.

Generic highest-SemVer across mixed upstream, legacy and private tags MUST NOT be used as the canonical downstream resolver.

## Requirement: legacy preservation

Already-published legacy fork tags/releases MUST remain immutable historical provenance. Migration MUST NOT rewrite, delete, retag, or renumber them into the private lane.

## Requirement: provenance

Every canonical downstream release MUST carry evidence of the exact upstream repository, upstream tag/version, and upstream commit SHA that define its accepted baseline.

## Requirement: release quality independence

The `private.N` suffix identifies downstream lineage/revision only.

GitHub release `prerelease` state MUST remain an independent quality decision and MUST NOT be inferred from the word `private`.

## Requirement: publication-route integration

One policy-neutral common contract MUST own the fork-release semantics.

When downstream fork release-version selection or validation is material, the following supported publication surfaces MUST load/apply that common contract rather than duplicate the algorithm:

- ChatGPT-only Close;
- Codex-only Close;
- legacy/shared Review and Handoff publication flow.

The contract MUST NOT itself authorize publication, deployment, tag deletion, force-push, release mutation, or upstream synchronization.
