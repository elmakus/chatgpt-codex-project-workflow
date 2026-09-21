# Tasks — fork release versioning

- [x] Reconcile the JIT OpenSpec against FRV R1, ADR-FRV-001, approved FRV-P2, M01-T01, current main and current publication surfaces.
- [x] Add the canonical policy-neutral fork-release contract.
- [x] Wire ChatGPT-only Close to the common contract.
- [x] Wire Codex-only Close to the common contract.
- [x] Wire legacy/shared Review and Handoff publication flow to the common contract.
- [x] Add deterministic regression coverage for canonical selection, migration, provenance, prerelease independence and route coverage.
- [x] Add concise operator/user discoverability documentation.
- [x] Verify OpenSpec, implementation/docs and tests are coherent and no unrelated auto-tagging/upstream-sync/history mutation is introduced.
- [x] Freeze the exact implementation subject for independent review.


## M02 — canonical fork-channel ordering and moving aliases

- [x] Reconcile the JIT OpenSpec against FRV R2, ADR-FRV-001, approved FRV-P3, M02-T01, current main and the completed M01 baseline.
- [ ] Extend the common contract with separate cross-baseline canonical fork-channel ordering.
- [ ] Define exact non-canonical exclusion and explicitly reject generic SemVer as the canonical fork-channel resolver.
- [ ] Define optional native moving-`latest` semantics, stable-eligibility policy, immutable-reference preservation, artifact/content identity and no-`vlatest` boundary.
- [ ] Extend deterministic regression coverage for the SemVer failure mode, multi-digit private revisions, cross-baseline ordering and non-canonical exclusion.
- [ ] Update concise README discoverability without duplicating detailed semantics.
- [ ] Verify publication surfaces still reference the one common contract and the repo-local auto-patch workflow remains unchanged.
- [ ] Verify OpenSpec, common contract, README and tests are coherent.
