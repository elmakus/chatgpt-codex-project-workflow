# Fork Release Versioning Requirements

Revision: `R1`
Status: `approved`
Updated: `2026-09-20`

## Goal / target state

Project Workflow must prevent downstream forks from publishing fork-local changes under version numbers that look like later upstream releases.

For a project that is intentionally maintained as a downstream fork, release identity must preserve two independent facts:

1. the exact upstream baseline the fork is based on;
2. the fork-local release revision produced from that baseline.

The canonical downstream release form is:

```text
v<upstream-version>-private.<N>
```

For example, a fork based on upstream `v5.0.8` publishes local releases as `v5.0.8-private.1`, `v5.0.8-private.2`, and so on. After an intentional alignment to upstream `v5.0.9`, the private counter starts again at `v5.0.9-private.1`.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| FRV-REQ-001 | Before Project Workflow chooses a release version for a downstream fork, it MUST establish the exact upstream repository and accepted upstream baseline rather than deriving a new upstream-looking version from the fork's previous tag. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-002 | A fork-local release based on upstream version `X.Y.Z` MUST use `vX.Y.Z-private.N`, where `N` is a positive integer private revision for that exact upstream baseline. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-003 | Fork-local work MUST NOT advance the upstream version component. A fork based on upstream `v5.0.8` MUST NOT publish a local-only change as `v5.0.9`, `v5.0.10`, etc. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-004 | The private revision MUST increase monotonically within one upstream baseline. When the fork intentionally aligns to a different upstream version, the private revision restarts at `1` for the new baseline. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-005 | Release provenance MUST record the exact upstream repository, upstream version/tag and upstream commit SHA that define the release baseline. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-006 | Already-published legacy fork releases that used upstream-looking versions MUST be preserved as immutable historical references. Migration MUST NOT rewrite/delete those tags or releases merely to normalize versioning. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-007 | After migration, release selection/update logic MUST explicitly select the canonical private-release lane. It MUST NOT use generic highest-SemVer selection across upstream tags, legacy fork tags and `-private.N` tags. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-008 | The `-private.N` suffix is a downstream lineage/revision identifier. Consumers MUST NOT infer release quality/stability from that suffix. GitHub's release `prerelease` flag remains an independent publication-quality choice. | MUST | user decision 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-009 | Workflow guidance MUST explicitly account for SemVer precedence: `X.Y.Z-private.N` sorts below `X.Y.Z`, and previously published legacy tags such as `5.0.13` may sort above the canonical private lane. Correctness therefore depends on explicit lineage parsing/selection rather than max-SemVer. | MUST | verified SemVer constraint / ADR-FRV-001 | accepted |
| FRV-REQ-010 | The fork-release rule MUST be policy-neutral workflow authority and be reachable from every supported Project Workflow publication path that can choose or validate a release version. | MUST | user goal / ADR-FRV-001 | accepted |
| FRV-REQ-011 | On first migration to the canonical private lane for a baseline that has no existing canonical `-private.N` release, the new lane starts at `private.1`; historical legacy releases do not get renumbered into the new lane. | MUST | accepted migration direction 2026-09-20 / ADR-FRV-001 | accepted |
| FRV-REQ-012 | If canonical `-private.N` releases already exist for the selected upstream baseline, the next private revision MUST be computed from that lane only as `max(N)+1`; legacy/upstream-looking tags do not participate in that counter. | MUST | lineage invariant / ADR-FRV-001 | accepted |

## Constraints

- The rule applies only when the project is a downstream fork or equivalent explicitly tracked upstream-derived project. Independent projects retain their own accepted versioning policy.
- Upstream lineage must be established from durable repository/project evidence; a coincidentally similar version number is not sufficient.
- A release may not claim a newer upstream baseline until that baseline is actually integrated/accepted in the fork.
- The versioning rule does not by itself authorize publication, deployment, tag deletion, force-push or other external writes.
- Existing release URLs, checksums and immutable provenance must remain valid.

## Non-goals

- Rewriting historical tags/releases into the new format.
- Mirroring every upstream release when the fork has no local release to publish.
- Using `private` to encode alpha/beta/stable quality.
- Replacing project-specific release gates, CI verification, signing or checksum policy.
- Defining an automatic upstream-sync policy.

## Global invariants

1. The upstream version component always identifies the actual accepted upstream baseline.
2. The private revision identifies fork-local release evolution on that baseline.
3. Fork-local releases never consume future upstream-looking version numbers.
4. Historical release identity is immutable.
5. Release/update selection is lineage-aware, not generic max-SemVer.
6. Publication quality metadata is independent from fork lineage.

## External contracts / dependencies

- Git repository/fork metadata or another durable project authority that identifies the upstream repository.
- Exact upstream tag/version and commit SHA.
- GitHub release/tag state when publication is performed.
- SemVer syntax/precedence behavior for prerelease identifiers.
- Project-specific release tooling/resolvers/installers that may need to consume the canonical private lane.

## Acceptance-level requirements

The change is acceptable when:

1. Project Workflow has one canonical policy-neutral fork-release versioning contract.
2. Supported release/publication routes are required to apply that contract before selecting/validating a downstream fork release version.
3. The contract deterministically produces `v5.0.8-private.1`, then `private.2`, etc. for local releases on upstream `v5.0.8`.
4. After an accepted upstream move to `v5.0.9`, the first canonical local release is `v5.0.9-private.1`.
5. A fork-local change cannot legally become `v5.0.9` while the accepted upstream baseline is still `v5.0.8`.
6. Legacy upstream-looking fork tags remain untouched and are excluded from the new private counter.
7. Guidance/tests reject generic highest-SemVer as a canonical resolver across mixed legacy/upstream/private tags.
8. Exact upstream repo/tag/SHA provenance is required for publication evidence.
9. GitHub prerelease status is not inferred from the word `private`.
10. Contract tests cover migration, counter reset/increment and mixed-tag resolution semantics.

## Definition completeness

- The target version format is explicit.
- The upstream/private-revision axes are separated.
- Legacy migration behavior is explicit.
- Resolver behavior is explicit.
- SemVer precedence caveat is captured.
- Publication-quality semantics are separate.
- No unresolved user/product choice remains that can materially change the implementation strategy.

## Downstream coverage

Planning must map every FRV requirement to an implementation milestone/work package and verification path. Execution Prep creates concrete Task Cards before implementation.
