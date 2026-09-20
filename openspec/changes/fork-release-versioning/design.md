# Design — fork release versioning

## Baseline

Current publication modules validate publication/PR state but do not own downstream-fork lineage semantics. The repository is contract/documentation driven and has no existing executable release-version resolver that should become a new runtime dependency.

## Semantic ownership

Add one common policy-neutral authority file:

`workflow/common/FORK_RELEASE_VERSIONING.md`

It owns applicability, baseline/provenance requirements, version construction, numeric per-baseline counter rules, migration/legacy handling, mixed-tag resolver semantics, SemVer caveat, and prerelease-quality independence.

Policy-local publication modules reference this common contract conditionally when they need to choose or validate a downstream-fork release version. They do not restate the algorithm.

## Publication surfaces

Integrate the common contract into:

- `workflow/chatgpt_only/CLOSE.md`;
- `workflow/codex_only/CLOSE.md`;
- `workflow/REVIEW_AND_HANDOFF.md`.

No additional policy route is introduced.

The repo-local `.github/workflows/auto-patch-tag.yml` is an independent-project self-release mechanism, not a generic downstream-fork Project Workflow publication surface, and remains unchanged by this Card.

## Deterministic verification

Add a standard-library repository regression test that:

- verifies the canonical common contract contains the required normative clauses/examples;
- models numeric private-lane selection for the approved examples, including gaps/multi-digit values, baseline reset/isolation, legacy exclusion and mixed-tag behavior;
- verifies all three publication surfaces reference the common contract;
- verifies provenance and prerelease-independence requirements remain present;
- verifies the repo-local auto-patch workflow is outside the changed contract surface.

The test model is verification code only; production/workflow semantics remain owned by the common contract.

## Integrity and authorization

This change never mutates external release history and does not grant tag/release/deployment authority. Existing publication, review, signing/checksum and external-write gates remain controlling.
