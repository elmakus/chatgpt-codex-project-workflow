# Intake — fork release ordering and latest alias

- Workstream: `change-fork-release-order-latest-alias`
- Kind: `change`
- Branch: `work/fork-release-order-latest-alias`
- Integration target: `main`
- Base: `main`
- Dependency classification: independent
- Parent workstream: none

## Authorized scope

Change Project Workflow's downstream-fork release policy so that:

1. canonical fork releases remain `vX.Y.Z-private.N`;
2. downstream release ordering/selection never relies on generic SemVer precedence across upstream, legacy and private tags;
3. canonical fork ordering is lineage-aware and compares the accepted upstream baseline plus numeric private revision;
4. publication-time lane selection remains baseline-scoped: only `vX.Y.Z-private.N` for the accepted upstream baseline contributes to the next `N`;
5. update/latest-channel selection has an explicit canonical ordering across canonical fork releases and excludes upstream-only, legacy upstream-looking and malformed tags;
6. `latest` is defined only as an optional moving alias/channel on publication surfaces that natively support aliases (for example container registries), never as the canonical release identity or a synthetic Git tag such as `vlatest`;
7. a moving `latest` alias points only to the newest accepted stable canonical fork release according to the fork-release ordering contract;
8. immutable/versioned references remain available for reproducibility and rollback;
9. `private.N` remains independent of GitHub's prerelease-quality flag.

## Evidence / current defect

The existing common contract already forbids generic highest-SemVer selection for baseline-local publication, but it does not fully specify a reusable global canonical-fork ordering for update channels or the semantics of a moving `latest` alias. Downstream implementations can therefore still use ordinary SemVer sorting and obtain incorrect results such as treating `1.1.18` as newer than `1.1.18-private.4` for the fork's private release channel.

## Route classification

This changes accepted workflow semantics rather than only implementation detail. Route to Project Definition to extend canonical requirements/decision authority, then use proportional planning/execution for the bounded contract/documentation change.

- Path: `project_definition`
- Next route: Project Definition
