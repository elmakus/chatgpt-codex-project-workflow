# M02Q-T29 implementation evidence — structured Review acceptance compatibility

## Exact implementation subject

- Product repository: `elmakus/project_workflow_v2`.
- Product branch: `work/pwv21-policy-kernel`.
- Exact implementation commit: `0b1bcdf63e4198ae53ace14a69d7c792e620ed19`.
- Exact tree: `ce996279af627719129c435416ffcbec62dc057b`.
- Starting candidate: `5e403db8f82e3fa7b8c7dc12bb1904ff441dcaa3`.
- Remote branch readback resolves exactly to the implementation commit.

Changed surface from the starting candidate:
- `tools/review_acceptance_provenance.py@e710fff6e84e20b79c097ad064b2feea17bb6351` — new immutable historical path-only acceptance proof verifier.
- `tools/state_contract.py@43330fe6fb7b3d302f25a025c88b53166e1109b8` — Board proof-shape/coherence validation.
- `tools/router.py@b1d6ea35d8a74715d2ca91811237e7b66e81eee5` — proved structured-success historical acceptance serving in ordinary routing and DONE/Close.
- `tests/test_review_acceptance_provenance.py@522a71765cba6db171f23d4a2a1fa3bd113ae8b9`.
- `tests/test_router.py@ebaa44ac4d3be26b9efc847b517b3d29e51f5203`.

No consumer Review, Card or Board migration record was changed by the product implementation.

## Contract behavior

The new `review_acceptance_migrations` record is append-only Board proof. It binds:
- selected Card and Review attempt identity;
- exact immutable Review repository/commit/path/blob;
- exact workstream/Card identity;
- exact Task Card path and blob visible at the immutable Review commit.

Serving is permitted only for an already-DONE Card with an explicit terminal GREEN review, wholly path-only Task Card acceptance and structured `Result status: success`. The exact Review locator must equal the proof, Review bytes must remain identical, the accepted Task Card blob must resolve at the Review commit, and current Task Card bytes must still equal that blob. Board validation requires uniqueness, the exact selected review locator, the selected Card contract path, and disallows overlap with `legacy_result_migrations`.

Without the proof, the pre-existing RF004 error remains: path-only acceptance cannot prove exact content. Partially exact acceptance is not migratable. The T26 statusless legacy-Result adapter is unchanged and remains a separate path.

## Exact T09–T12 analogue readback

The preserved consumer histories satisfy the immutable prerequisites for the downstream proof population without modifying them:

- M02Q-T09: Review `a90424383e0613b36c18affbf60c6868c54ffdfa:36518e7ceafc412173335b8f2de4df0c8dd8ff8c`; accepted/current Card blob `b26de9f74281fdbad056b3bbae61bb86e63d4ef6`.
- M02Q-T10: Review `a90424383e0613b36c18affbf60c6868c54ffdfa:8caccba6389810e861d32206028d944c0418ca26`; accepted/current Card blob `20293174c6fb30dbb8f348bb71c2c9b79a242a25`.
- M02Q-T11: Review `a90424383e0613b36c18affbf60c6868c54ffdfa:061010388a0661565327702fc8efdc524df11a37`; accepted/current Card blob `e15aa88ff2d029d80e34cf119732183616876509`.
- M02Q-T12: Review `6184b0dea00ce1f85d57dae8372c167de94eba66:d6725fe8999cbfab9b35f032d10c71062ed79024`; accepted/current Card blob `ad626edf7b2fd5f1aaf4c9a9075b370380c57cc0`.

All four Reviews remain byte-identical to their exact Board locators, all four source-time Card blobs equal their current Card blobs, all four Results are structured `Result status: success`, and none of the four Cards is covered by `legacy_result_migrations`. This is only prerequisite readback; the four proof records are deliberately left for the downstream consumer Card.

## Tests / exact-head CI

GitHub Actions push run `36335203774` executed `sh scripts/test.sh` on exact head `0b1bcdf63e4198ae53ace14a69d7c792e620ed19` and completed **success**.

Relevant readback from the exact run:
- new router control `test_structured_path_only_review_acceptance_requires_exact_migration`: PASS;
- router suite: 118/118 PASS;
- cumulative Python unittest discovery: 1219/1219 PASS;
- M01 baseline checks: PASS;
- repository-check job: success.

The intermediate state remains fail-closed because no consumer `review_acceptance_migrations` entries have yet been added.
