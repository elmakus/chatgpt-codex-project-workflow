# Fork Release Versioning — Master Plan

Revision: `FRV-P3`
Status: `draft`
Updated: `2026-09-21`
Supersedes plan revision: `FRV-P2` (approved and implemented through M01)
Review requirement: `RECOMMENDED`

## Authority

- Requirements: `requirements/FORK_RELEASE_VERSIONING.md` R2
- Decision: `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / `ADR-FRV-001`
- Current intake provenance: `implementation/workstreams/change-fork-release-order-latest-alias/INTAKE.md`
- Current workstream: `implementation/workstreams/change-fork-release-order-latest-alias/WORKSTREAM.yaml`
- Current branch: `work/fork-release-order-latest-alias`
- Integration target: `main`
- Prior completed workstream: `implementation/workstreams/issue-fork-release-versioning/WORKSTREAM.yaml`

## Goal

Extend the already-integrated downstream-fork release contract so every Project Workflow consumer has one deterministic domain rule for both:

1. choosing the next canonical release in an accepted upstream baseline lane; and
2. choosing the current/latest canonical fork release across canonical private releases.

The extension must preserve `vX.Y.Z-private.N`, define cross-baseline canonical ordering as numeric `(X, Y, Z, N)`, keep generic SemVer out of fork-channel selection, and define `latest` only as an optional moving alias on publication systems that natively support aliases.

## Execution baseline

The prior FRV workstream has already integrated M01 on `main`:

- `workflow/common/FORK_RELEASE_VERSIONING.md` is the single policy-neutral semantic source;
- ChatGPT-only, Codex-only and legacy/shared publication paths already defer to it;
- deterministic regression coverage exists in `tests/test_fork_release_versioning.py`;
- README documents the convention;
- historical release identity and GitHub prerelease-quality independence are already explicit.

Current gap:

- the common contract describes baseline-local private-lane selection but does not fully define one canonical cross-baseline fork-channel order for updater/current-release selection;
- it does not define the allowed semantics of a moving `latest` alias;
- downstream tooling can therefore still implement ordinary SemVer sorting and get a wrong fork-channel result.

This Project Workflow workstream updates workflow authority/contracts/tests only. It does not directly patch `codex_workflow`, workstation images, or another downstream project repository; each adopter applies the updated authority through its own managed workstream.

## Inherited invariants

1. Canonical release identity remains `vX.Y.Z-private.N`.
2. `X.Y.Z` is always the actual accepted upstream baseline; fork-local work never advances it.
3. Baseline-local next-release selection uses only that baseline's exact canonical `private.N` lane and numeric `max(N)+1`.
4. Historical upstream-looking/legacy tags remain immutable provenance.
5. The common contract remains the only canonical semantic source; publication modules reference it rather than copying algorithms.
6. Generic SemVer remains valid for SemVer semantics but is not the accepted fork-channel resolver.
7. `private.N` is lineage/revision metadata, not stability metadata.
8. External publication/tag/deployment authorization rules remain unchanged.
9. A moving alias never replaces immutable/versioned release identity.
10. YAGNI applies: do not add a runtime library/service to this contract repository when deterministic contract logic/tests are sufficient.

## Milestone M01 — Canonical fork-release identity and baseline-local selection

Status: `completed by prior workstream`

### Outcome

The repository already has the canonical `vX.Y.Z-private.N` contract, baseline-local counter semantics, publication-route wiring, legacy preservation, provenance requirements and initial regression coverage.

### Authority already covered

- FRV-REQ-001 through FRV-REQ-012 under Definition R1 / FRV-P2.
- R2 clarifies FRV-REQ-004/007/009 without invalidating the completed M01 outcome.

M01 is historical prerequisite evidence only. This workstream MUST NOT replay its implementation or mutate its completed Task Board/history.

## Milestone M02 — Canonical fork-channel ordering and moving aliases

### Outcome

Project Workflow has one explicit canonical fork-channel ordering rule and one bounded moving-alias contract, with deterministic regression coverage that prevents ordinary SemVer selection from reappearing in downstream guidance.

### Requirement ownership

Primary:
- FRV-REQ-013 through FRV-REQ-017.

Clarified/extended behavior:
- FRV-REQ-007;
- FRV-REQ-009.

### Planned work packages

1. **JIT OpenSpec reconciliation**
   - Materialize/reconcile one OpenSpec change for the M02 behavior surface immediately before the first behavior-changing implementation Card.
   - Freeze the distinction between baseline-local next-release selection and cross-baseline canonical fork-channel selection.
   - Freeze exact-candidate parsing, numeric tuple ordering, non-canonical exclusion and moving-alias boundaries.

2. **Extend the common fork-release contract**
   - Preserve the existing `vX.Y.Z-private.N` identity and baseline-local `max(N)+1` algorithm.
   - Add a separate canonical fork-channel resolver rule:
     - accept only exact `vX.Y.Z-private.N` tags with positive integer components;
     - compare numeric `(X, Y, Z, N)`;
     - ignore upstream-only, legacy upstream-looking, malformed and other non-canonical tags.
   - State explicitly that generic SemVer ordering must not be wrapped with ad-hoc exceptions and used as the canonical downstream resolver.

3. **Define moving `latest` alias semantics**
   - Permit `latest` only on publication surfaces with native moving-alias/channel semantics.
   - Require it to point to the newest accepted stable canonical fork release according to the canonical fork-channel order plus project release-quality policy.
   - Require the immutable/versioned canonical reference to remain available.
   - Require alias and canonical version to identify the same released artifact/content at publication time.
   - Explicitly forbid inventing a canonical Git tag/release such as `vlatest`.
   - Do not require systems without native alias semantics to emulate one.

4. **Strengthen deterministic regression coverage**
   - Add a test helper/representation that parses canonical private versions independently of generic SemVer precedence.
   - Prove numeric same-baseline ordering, including `private.10 > private.4`.
   - Prove cross-baseline tuple ordering.
   - Prove an upstream-only `v1.1.18` cannot outrank `v1.1.18-private.4` in the fork channel because it is not a canonical candidate.
   - Prove legacy/malformed/non-canonical tags are excluded.
   - Assert the common contract contains moving-alias, stable-eligibility, immutable-reference and no-`vlatest` semantics.
   - Preserve existing publication-surface reference tests and the repository-local auto-patch-tagger boundary.

5. **Update concise discoverability documentation**
   - Update README only enough to distinguish canonical version identity, fork-channel ordering and optional moving aliases.
   - Keep detailed semantics in the common contract; do not duplicate the full algorithm in README or policy-local Close modules.

### Acceptance

- One common contract still owns all fork-release semantics.
- Baseline-local next-release selection and cross-baseline current/update selection are explicitly different operations.
- Canonical cross-baseline ordering is numeric `(X, Y, Z, N)` over exact canonical private releases only.
- Generic SemVer is explicitly invalid as the canonical fork-channel resolver.
- `v1.1.18` is excluded from the fork-channel candidates even when SemVer would rank it above `v1.1.18-private.4`.
- `v1.1.18-private.10` orders after `v1.1.18-private.4`.
- `v1.1.19-private.1` orders after every canonical `v1.1.18-private.N` release.
- Legacy/upstream-only/malformed tags do not participate in canonical channel ordering.
- `latest` is optional, surface-native channel metadata only.
- No contract instructs creation of `latest`/`vlatest` as a canonical Git release/tag.
- When `latest` exists it selects the newest accepted stable canonical fork release and does not remove the immutable/versioned reference.
- Existing publication authorization, provenance, historical-tag immutability and prerelease-quality separation remain unchanged.
- Focused tests and the repository's relevant full test discovery are GREEN.
- OpenSpec, common contract, README and regression tests are coherent.

### JIT trigger

Execution Prep may use one bounded Card for M02 because the contract/test/documentation change is tightly coupled and small enough to review as one immutable subject. Split only if current repository evidence proves materially separate implementation risk.

The first behavior-changing Card MUST bind/reconcile the M02 OpenSpec immediately before implementation. No additional strategic/user decision is required.

## Requirement coverage

| Requirement | Owner milestone | Execution path |
|---|---|---|
| FRV-REQ-001 | M01 complete | accepted upstream baseline/provenance |
| FRV-REQ-002 | M01 complete | canonical private identity |
| FRV-REQ-003 | M01 complete | prohibit fork-local upstream bump |
| FRV-REQ-004 | M01 complete / R2 clarification | independent per-baseline numeric lane |
| FRV-REQ-005 | M01 complete | upstream repo/tag/SHA provenance |
| FRV-REQ-006 | M01 complete | immutable legacy history |
| FRV-REQ-007 | M01 + M02 | explicit canonical lane/channel selection, never generic max-SemVer |
| FRV-REQ-008 | M01 complete | quality independence |
| FRV-REQ-009 | M01 + M02 | SemVer consequence + domain-ordering regression |
| FRV-REQ-010 | M01 complete | single policy-neutral source and publication-route references |
| FRV-REQ-011 | M01 complete | empty baseline lane begins at private.1 |
| FRV-REQ-012 | M01 complete | baseline-local numeric max(N)+1 |
| FRV-REQ-013 | M02 | exact canonical parsing + numeric (X,Y,Z,N) order |
| FRV-REQ-014 | M02 | non-canonical candidate exclusion |
| FRV-REQ-015 | M02 | optional native latest alias + stable eligibility |
| FRV-REQ-016 | M02 | no synthetic vlatest/canonical alias identity |
| FRV-REQ-017 | M02 | immutable versioned reference + artifact identity |

## Verification strategy

- Extend `tests/test_fork_release_versioning.py` instead of creating a second semantic test suite.
- Keep canonical parsing/order logic in the regression test self-contained and deterministic; Project Workflow remains a contract repository rather than introducing an unnecessary runtime release library.
- Exercise representative mixed sets containing canonical private releases, upstream-only tags, legacy upstream-looking tags, malformed private tags, multiple baselines and multi-digit private revisions.
- Verify common-contract wording for both resolver contexts and moving-alias boundaries.
- Verify supported publication surfaces continue to reference the one common contract and do not duplicate the algorithm.
- Run focused FRV tests plus relevant repository-wide test discovery.
- During Close, refresh against current `main` and independently review the exact final integrated workstream subject under normal branch-isolated rules.

## Migration / rollback

This Project Workflow change mutates no external release history and creates no external alias.

Downstream adoption is project-local:

- existing canonical private tags remain unchanged;
- a downstream updater/resolver switches from generic SemVer selection to exact canonical private parsing/order;
- a publication pipeline may add/update a native `latest` alias only if that project's accepted publication policy uses one;
- immutable versioned releases remain available.

Rollback of this workflow workstream is ordinary branch/PR reversion before integration. No tag deletion, retagging or alias mutation is part of this repository's rollback.

## Security / integrity

- Never treat a display/version string alone as proof of upstream lineage.
- Never include upstream-only/legacy/malformed tags in canonical fork-channel ordering.
- Never move a publication alias to an artifact that is not the exact accepted canonical release content.
- Never remove the immutable versioned reference merely because a moving alias exists.
- Existing authorization gates for tag/release/container publication remain in force.

## OpenSpec boundary

M02 changes externally observable release-selection/channel behavior and therefore requires JIT OpenSpec before the first behavior-changing implementation Card.

The OpenSpec must remain inside approved FRV R2 / ADR-FRV-001 authority and formalize only:

- exact canonical-private candidate grammar;
- baseline-local versus cross-baseline resolver distinction;
- numeric `(X, Y, Z, N)` ordering;
- non-canonical exclusion;
- optional moving-`latest` semantics;
- stable eligibility being determined by the project's release-quality policy;
- immutable canonical-reference and artifact-identity requirement;
- no-`vlatest` boundary.

Do not use OpenSpec to invent a cross-repository deployment mechanism or automatically modify downstream projects.

## Pre-implementation planning audit

- Definition R2 is approved and internally coherent.
- The canonical identity `vX.Y.Z-private.N` remains unchanged.
- The new requirement is a bounded semantic extension, not a new versioning scheme.
- M01 is complete historical prerequisite state and is not replayed.
- M02 owns all new FRV-REQ-013..017 obligations plus the necessary FRV-REQ-007/009 clarification.
- One common contract remains the semantic source.
- The plan distinguishes baseline-local next-release selection from cross-baseline current/update selection.
- The plan does not require a moving alias on systems that do not natively support one.
- The plan preserves immutable releases, provenance and publication authorization.
- Tests cover the exact SemVer failure mode that triggered this change.
- No downstream repository mutation is smuggled into this Project Workflow workstream.
- No unresolved product/system choice remains.
- Added complexity is justified by current accepted requirements; no new runtime service/library/registry is introduced.

Planning audit result: `GREEN`.

## Independent plan review

- Review requirement: `RECOMMENDED`
- Reason: FRV-P3 materially extends externally visible release/update-channel semantics and requirement coverage; independent review is practical.
- Review record: `planning/reviews/FRV-P3.md`
- Review state: `pending`
- Review subject: frozen by the review record after this draft write.
