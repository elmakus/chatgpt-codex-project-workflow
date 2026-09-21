# Intake — fork release ordering and latest alias

- Workstream: `change-fork-release-order-latest-alias`
- Kind: `change`
- Branch: `work/fork-release-order-latest-alias`
- Integration target: `main`
- Base: `main`
- Dependency classification: independent
- Parent workstream: none
- Intake state: complete

## Authorized scope

Change Project Workflow's downstream-fork release policy so that:

1. canonical fork releases remain `vX.Y.Z-private.N`;
2. downstream release ordering/selection never relies on generic SemVer precedence across upstream, legacy and private tags;
3. baseline-local publication selection compares only the accepted baseline's canonical private revisions;
4. current/update-channel selection across canonical fork releases uses numeric `(X, Y, Z, N)` ordering over exact canonical private tags only;
5. upstream-only, legacy upstream-looking and malformed tags do not participate in the canonical fork channel;
6. `latest` is defined only as an optional moving alias/channel on publication surfaces that natively support aliases, never as the canonical release identity or a synthetic Git tag/release such as `vlatest`;
7. a moving `latest` alias points only to the newest accepted stable canonical fork release according to the fork-channel ordering and the project's release-quality policy;
8. immutable/versioned references remain available for reproducibility and rollback;
9. `private.N` remains independent of GitHub's prerelease-quality flag.

## Evidence / current defect

The existing common contract already forbids generic highest-SemVer selection for baseline-local publication, but it does not fully specify a reusable global canonical-fork ordering for update/current channels or the semantics of a moving `latest` alias.

A downstream implementation can therefore still sort releases by ordinary SemVer and obtain the wrong fork-channel result, for example treating `1.1.18` as higher-precedence than `1.1.18-private.4`, even though the upstream-only tag is not a canonical candidate for the fork's private channel.

## Existing authority / prior completed work

The prior `issue-fork-release-versioning` workstream is complete and remains historical authority/evidence. It established:

- `requirements/FORK_RELEASE_VERSIONING.md` R1;
- `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / `ADR-FRV-001`;
- approved plan `FRV-P2`;
- the common `workflow/common/FORK_RELEASE_VERSIONING.md` contract;
- publication-route references and deterministic regression tests.

This workstream extends that accepted domain; it does not replay or rewrite the completed historical workstream.

## Project Definition result

Project Definition has been reconciled and is GREEN:

- `requirements/FORK_RELEASE_VERSIONING.md` R2 — approved;
- `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / `ADR-FRV-001` — accepted and extended 2026-09-21;
- no unresolved product/system choice remains.

R2 preserves the existing canonical identity and adds the accepted canonical fork-channel ordering plus moving-alias boundaries.

## Path classification

This is not an implementation-only correction: it changes accepted workflow behavior for update/current-channel resolution and publication aliases. It therefore routes through the existing strategic plan.

- Path: `project_definition -> strategic_planning`
- Next route: `strategic_planning:FRV-P3`
