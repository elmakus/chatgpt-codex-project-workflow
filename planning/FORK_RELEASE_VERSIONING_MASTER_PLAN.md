# Fork Release Versioning — Master Plan

Revision: `FRV-P1`
Status: `draft`
Updated: `2026-09-20`
Review requirement: `RECOMMENDED`

## Authority

- Requirements: `requirements/FORK_RELEASE_VERSIONING.md` R1
- Decision: `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / `ADR-FRV-001`
- Intake provenance: `implementation/workstreams/issue-fork-release-versioning/INTAKE.md`
- Workstream: `implementation/workstreams/issue-fork-release-versioning/WORKSTREAM.yaml`
- Branch: `fix/fork-release-versioning`
- Integration target: `main`

## Goal

Make fork release-version selection an explicit Project Workflow contract so publication agents cannot turn fork-local changes into future-looking upstream versions.

The implementation must establish one policy-neutral lineage contract, wire every supported publication path to it, preserve progressive disclosure, and add regression coverage for canonical `v<upstream>-private.<N>` selection plus legacy migration semantics.

## Execution baseline

- Current workflow publication contracts verify publication/PR state but do not define a fork-specific release-version lineage rule.
- The migrated ChatGPT-only and Codex-only Close modules are separate policy-local publication paths.
- Policies still on the legacy/shared route use the shared review/handoff publication surface.
- The repository is primarily contract/documentation driven; deterministic contract tests are the appropriate regression mechanism unless implementation discovers an existing executable release-version parser.
- Existing downstream release history is external evidence/provenance only; this workstream changes Project Workflow behavior and does not rewrite releases in `elmakus/codex-chatgpt-web` or another project repository.

## Inherited invariants

1. Accepted fork-release semantics come only from `requirements/FORK_RELEASE_VERSIONING.md` and `ADR-FRV-001`.
2. The policy-neutral versioning rule has one canonical source; policy-local Close modules reference it instead of duplicating the algorithm.
3. Loading remains conditional: projects that are not downstream forks do not need fork-versioning context.
4. Historical releases/tags are never rewritten by this workflow change.
5. Release publication remains subject to existing authorization, acceptance, review, signing/checksum and external-write rules.
6. The word `private` is lineage metadata, not a stability decision.

## Milestone M01 — Canonical fork-release contract and publication enforcement

### Outcome

Project Workflow has one shared, deterministic fork-release versioning contract that is applied by every supported publication route and guarded by regression tests/documentation.

### Requirement ownership

- FRV-REQ-001 through FRV-REQ-012.

### Planned work packages

1. Add a policy-neutral common contract, normally `workflow/common/FORK_RELEASE_VERSIONING.md`, that defines:
   - downstream-fork applicability/detection;
   - exact upstream baseline evidence;
   - canonical `v<upstream>-private.<N>` construction;
   - per-baseline private-counter increment/reset;
   - first-migration `private.1` behavior;
   - legacy-tag preservation;
   - exact upstream repo/tag/SHA provenance;
   - explicit lane selection instead of generic max-SemVer;
   - SemVer precedence caveat;
   - independence of GitHub `prerelease` quality status.
2. Wire the migrated ChatGPT-only publication path to load/apply the common contract only when release-version selection/validation for a downstream fork is material.
3. Wire the migrated Codex-only publication path to the same common contract without duplicating semantics.
4. Wire the legacy/shared publication surface used by still-unmigrated policies to the same common contract, preserving existing policy routing.
5. Add deterministic regression tests that prove:
   - `v5.0.8` baseline produces `v5.0.8-private.1` when no private lane exists;
   - existing `private.1` / `private.2` produces `private.3`;
   - accepted move to upstream `v5.0.9` resets to `v5.0.9-private.1`;
   - legacy `v5.0.9`–`v5.0.13` remain historical and are excluded from the private counter;
   - generic highest-SemVer is explicitly rejected for mixed lineage;
   - upstream repo/tag/SHA provenance and prerelease-independence rules are present;
   - all supported publication surfaces reference the canonical common contract.
6. Update concise user/operator documentation so the fork-version convention is discoverable without duplicating the full common contract.

### Acceptance

- One canonical common fork-release contract exists.
- All supported publication surfaces defer fork release-version selection/validation to that common contract.
- No publication module contains a divergent copy of the version algorithm.
- Regression tests cover all FRV acceptance-level outcomes that can be verified statically/deterministically in this workflow repository.
- The canonical examples produce `v5.0.8-private.1` and reset correctly on an accepted upstream-baseline change.
- Legacy tags are explicitly preserved and excluded from the private counter.
- The contract rejects generic max-SemVer as the canonical mixed-tag resolver.
- Upstream provenance and prerelease-quality separation are explicit.
- Existing publication authorization/review semantics remain unchanged.

### JIT trigger

Execution Prep may split M01 into bounded Cards for common-contract authoring, policy-surface wiring and regression/documentation work if that improves reviewability. No further strategic decision is required.

## Requirement coverage

| Requirement | Owner milestone | Execution path |
|---|---|---|
| FRV-REQ-001 | M01 | common contract applicability + baseline evidence |
| FRV-REQ-002 | M01 | canonical version construction |
| FRV-REQ-003 | M01 | prohibit upstream-component bump for local work |
| FRV-REQ-004 | M01 | per-baseline counter semantics |
| FRV-REQ-005 | M01 | provenance contract + publication checks |
| FRV-REQ-006 | M01 | legacy preservation/migration rules |
| FRV-REQ-007 | M01 | lineage-aware selection algorithm + tests |
| FRV-REQ-008 | M01 | prerelease-quality separation |
| FRV-REQ-009 | M01 | SemVer caveat + mixed-tag tests |
| FRV-REQ-010 | M01 | publication-surface wiring + route coverage test |
| FRV-REQ-011 | M01 | first-migration `private.1` rule + test |
| FRV-REQ-012 | M01 | canonical-lane `max(N)+1` rule + test |

## Verification strategy

- Add focused deterministic repository tests rather than relying on prose inspection alone.
- Verify exact common-contract references from each supported publication surface.
- Test representative mixed tag sets that include upstream-looking legacy releases and canonical private releases.
- Assert that no rule instructs generic highest-SemVer selection.
- Run the repository test suite after implementation.
- During workstream Close, refresh against current `main` and independently review the exact final integrated subject under normal workstream rules.

## Migration / rollback

This Project Workflow change does not mutate existing downstream release history.

Migration for a downstream fork begins on its next new release after it adopts the updated workflow:
- preserve legacy releases/tags;
- establish exact current upstream baseline;
- if no canonical private release exists for that baseline, start at `private.1`;
- otherwise use the next private revision in that baseline's canonical lane.

Rollback of this workflow workstream is ordinary branch/PR reversion before integration. No external release deletion or retagging is part of rollback.

## Security / integrity

- Never derive upstream baseline solely from a version string when repository/project evidence can establish exact provenance.
- Never delete/rewrite historical tags as a normalization step.
- Existing authorization gates for tag/release publication remain in force.
- Exact upstream SHA is part of release evidence to prevent false-lineage claims.

## OpenSpec boundary

No OpenSpec is required by default because this scope changes workflow contracts rather than a runtime API/schema. Execution Prep may introduce one only if implementation creates an executable parser/state interface whose behavior benefits from a machine-checkable contract.

## Pre-implementation planning audit

- Approved Definition R1 is complete and internally coherent.
- The naming format, migration behavior, resolver semantics and prerelease-quality separation are frozen by accepted authority.
- One common contract avoids policy drift.
- All supported publication paths have an explicit integration path.
- The plan does not rewrite external release history.
- Requirement coverage is complete.
- Verification covers the known SemVer/migration failure modes.
- No unresolved user/product choice remains.
- No speculative runtime mechanism is frozen beyond what the contract repository requires.

Planning audit result: `GREEN`.

## Independent plan review

- Review requirement: `RECOMMENDED`
- Reason: this is a new cross-publication workflow contract that changes how agents choose externally visible release versions; independent review is practical before implementation.
- Review record: `planning/reviews/FRV-P1.md`
- Review state: `pending`
- Reviewed subject: populated from the exact immutable draft blob after persistence.
