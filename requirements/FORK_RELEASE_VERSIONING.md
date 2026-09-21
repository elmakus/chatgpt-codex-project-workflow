# Fork Release Versioning Requirements

Revision: `R2`
Status: `approved`
Updated: `2026-09-21`

## Goal / target state

Project Workflow must prevent downstream forks from publishing fork-local changes under version numbers that look like later upstream releases, and must define one deterministic ordering/channel model for canonical fork releases that does not depend on generic SemVer precedence.

For a project that is intentionally maintained as a downstream fork, release identity preserves two independent facts:

1. the exact upstream baseline the fork is based on;
2. the fork-local release revision produced from that baseline.

The canonical downstream release form remains:

```text
v<upstream-version>-private.<N>
```

For example, a fork based on upstream `v5.0.8` publishes local releases as `v5.0.8-private.1`, `v5.0.8-private.2`, and so on. Each accepted upstream baseline owns an independent private-revision lane.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| FRV-REQ-001 | Before Project Workflow chooses a release version for a downstream fork, it MUST establish the exact upstream repository and accepted upstream baseline rather than deriving a new upstream-looking version from the fork's previous tag. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-002 | A fork-local release based on upstream version `X.Y.Z` MUST use `vX.Y.Z-private.N`, where `N` is a positive integer private revision for that exact upstream baseline. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-003 | Fork-local work MUST NOT advance the upstream version component. A fork based on upstream `v5.0.8` MUST NOT publish a local-only change as `v5.0.9`, `v5.0.10`, etc. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-004 | Private revisions MUST increase numerically within one upstream baseline. Each baseline has an independent lane; a lane starts at `private.1` only when that baseline has no existing canonical private release. | MUST | user decision 2026-09-20, clarified 2026-09-21 / ADR-FRV-001 | accepted |
| FRV-REQ-005 | Release provenance MUST record the exact upstream repository, upstream version/tag and upstream commit SHA that define the release baseline. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-006 | Already-published legacy fork releases that used upstream-looking versions MUST be preserved as immutable historical references. Migration MUST NOT rewrite/delete those tags or releases merely to normalize versioning. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-007 | After migration, release selection/update logic MUST explicitly select canonical private releases. It MUST NOT use generic highest-SemVer selection across upstream tags, legacy fork tags and `-private.N` tags. | MUST | user decision 2026-09-20, reaffirmed 2026-09-21 / ADR-FRV-001 | accepted |
| FRV-REQ-008 | The `-private.N` suffix is a downstream lineage/revision identifier. Consumers MUST NOT infer release quality/stability from that suffix. GitHub's release `prerelease` flag remains an independent publication-quality choice. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-009 | Workflow guidance MUST explicitly account for SemVer precedence: `X.Y.Z-private.N` sorts below `X.Y.Z`, while legacy upstream-looking tags may sort above the canonical private lane. Correctness therefore depends on explicit fork-lineage parsing/selection rather than max-SemVer. | MUST | verified SemVer constraint / ADR-FRV-001 | accepted |
| FRV-REQ-010 | The fork-release rule MUST be policy-neutral workflow authority and be reachable from every supported Project Workflow publication path that can choose or validate a release version. | MUST | user goal / ADR-FRV-001 | accepted |
| FRV-REQ-011 | On first migration to the canonical private lane for a baseline that has no existing canonical `-private.N` release, the new lane starts at `private.1`; historical legacy releases do not get renumbered into the new lane. | MUST | accepted migration direction 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-012 | If canonical `-private.N` releases already exist for the selected upstream baseline, the next private revision MUST be computed from that lane only as `max(N)+1`; legacy/upstream-looking tags do not participate in that counter. | MUST | lineage invariant / ADR-FRV-001 | accepted |
| FRV-REQ-013 | A resolver that needs the current/latest canonical fork release across baselines MUST consider only tags that exactly match `vX.Y.Z-private.N` with positive integer components and MUST order them numerically by the tuple `(X, Y, Z, N)`. Generic SemVer precedence is not the canonical fork-channel order. | MUST | user decision 2026-09-21 / ADR-FRV-001 | accepted |
| FRV-REQ-014 | Upstream-only tags, legacy upstream-looking fork tags, malformed private tags, and other non-canonical tags MUST NOT participate in canonical fork-channel ordering or in a moving `latest` alias decision. | MUST | user decision 2026-09-21 / ADR-FRV-001 | accepted |
| FRV-REQ-015 | A publication surface that natively supports moving aliases MAY expose `latest` as a convenience channel. That alias MUST point to the newest accepted stable canonical fork release according to FRV-REQ-013 and the project's release-quality policy; it MUST NOT replace the canonical versioned identity. | MUST | user decision 2026-09-21 / ADR-FRV-001 | accepted |
| FRV-REQ-016 | Project Workflow MUST NOT model `latest` as a synthetic canonical Git tag/release such as `vlatest`. Surfaces without native moving-alias semantics continue to use the versioned canonical release and their normal discovery mechanism. | MUST | user decision 2026-09-21 / ADR-FRV-001 | accepted |
| FRV-REQ-017 | When a moving alias is published, the immutable/versioned reference MUST remain available for reproducibility and rollback, and the alias MUST resolve to the same released artifact/content identity as that canonical version at publication time. | MUST | user decision 2026-09-21 / ADR-FRV-001 | accepted |

## Constraints

- The rule applies only when the project is a downstream fork or equivalent explicitly tracked upstream-derived project. Independent projects retain their own accepted versioning policy.
- Upstream lineage must be established from durable repository/project evidence; a coincidentally similar version number is not sufficient.
- A release may not claim a newer upstream baseline until that baseline is actually integrated/accepted in the fork.
- The versioning rule does not by itself authorize publication, deployment, tag deletion, force-push or other external writes.
- Existing release URLs, checksums and immutable provenance must remain valid.
- `latest` is channel metadata only where the underlying publication system has native alias semantics; it is never the authority for release identity.

## Non-goals

- Rewriting historical tags/releases into the new format.
- Mirroring every upstream release when the fork has no local release to publish.
- Using `private` to encode alpha/beta/stable quality.
- Replacing project-specific release gates, CI verification, signing or checksum policy.
- Defining an automatic upstream-sync policy.
- Requiring every publication system to invent a `latest` alias.
- Mutating downstream project repositories as part of this Project Workflow policy change; each downstream project adopts the contract through its own managed work.

## Global invariants

1. The upstream version component always identifies the actual accepted upstream baseline.
2. The private revision identifies fork-local release evolution on that baseline.
3. Fork-local releases never consume future upstream-looking version numbers.
4. Historical release identity is immutable.
5. Release/update selection is fork-lineage-aware, not generic max-SemVer.
6. Canonical cross-baseline fork order is numeric `(X, Y, Z, N)` over exact canonical private tags only.
7. Publication quality metadata is independent from fork lineage.
8. A moving `latest` alias is optional channel metadata, never a canonical release identity.
9. Versioned immutable references remain the reproducibility/rollback authority even when a moving alias exists.

## External contracts / dependencies

- Git repository/fork metadata or another durable project authority that identifies the upstream repository.
- Exact upstream tag/version and commit SHA.
- GitHub release/tag state when publication is performed.
- Container/package registries or other publication systems when they provide native moving-alias semantics.
- SemVer syntax/precedence behavior for prerelease identifiers.
- Project-specific release tooling/resolvers/installers that may need to consume the canonical private lane.

## Acceptance-level requirements

The change is acceptable when:

1. Project Workflow has one canonical policy-neutral fork-release versioning contract.
2. Supported release/publication routes are required to apply that contract before selecting/validating a downstream fork release version.
3. The contract deterministically produces `v5.0.8-private.1`, then `private.2`, etc. for local releases on upstream `v5.0.8`.
4. After an accepted upstream move to `v5.0.9`, an empty `v5.0.9-private.N` lane begins at `v5.0.9-private.1`; an existing lane continues from its own numeric maximum.
5. A fork-local change cannot legally become `v5.0.9` while the accepted upstream baseline is still `v5.0.8`.
6. Legacy upstream-looking fork tags remain untouched and are excluded from private counters and canonical fork-channel ordering.
7. Guidance/tests reject generic highest-SemVer as a canonical resolver across mixed legacy/upstream/private tags.
8. Exact upstream repo/tag/SHA provenance is required for publication evidence.
9. GitHub prerelease status is not inferred from the word `private`.
10. A mixed set such as `v1.1.18`, `v1.1.18-private.4`, `v1.1.17-private.99`, and `v1.1.19-private.1` resolves the canonical fork channel to `v1.1.19-private.1`; the upstream-only `v1.1.18` never outranks the canonical private lane merely because of SemVer precedence.
11. Numeric private ordering handles multi-digit revisions, so `v1.1.18-private.10` is newer in the fork channel than `v1.1.18-private.4`.
12. A native moving `latest` alias, when used, points to the newest accepted stable canonical fork release, while the versioned reference remains available and authoritative for reproducibility.
13. No workflow rule requires a synthetic `vlatest` Git tag/release.
14. Contract tests cover migration, counter increment, cross-baseline canonical ordering, non-canonical exclusion and moving-alias semantics.

## Definition completeness

- The canonical version format remains explicit.
- Baseline-local private-counter behavior is explicit.
- Cross-baseline canonical fork-channel ordering is explicit.
- Legacy/non-canonical exclusion is explicit.
- Moving-alias semantics and the no-`vlatest` boundary are explicit.
- SemVer precedence caveat is captured.
- Publication-quality semantics remain separate.
- No unresolved user/product choice remains that can materially change the implementation strategy.

## Downstream coverage

Planning must map every FRV requirement to an implementation milestone/work package and verification path. Execution Prep creates concrete Task Cards before implementation.
