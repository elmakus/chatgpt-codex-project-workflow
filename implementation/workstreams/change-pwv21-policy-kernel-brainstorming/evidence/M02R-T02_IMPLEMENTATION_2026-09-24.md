# M02R-T02 implementation evidence

Date: 2026-09-24
Card: `M02R-T02`
Implementation repository: `elmakus/project_workflow_v2`
Branch: `work/pwv21-policy-kernel`
Accepted predecessor implementation head: `19b7b9c0d335afb046493bff1a0a13dc4c310ec6`
Implemented head: `4b63b0645432b185b12ffb04bd83268d1c584116`

## Implemented outcome

The candidate now derives review convergence accounting from append-only review-attempt history instead of a mutable counter store.

- Convergence-aware attempts bind one stable review scope (`card`, `milestone`, or `final`) and review epoch.
- Ordinary repair stays in the same epoch; an epoch change requires a durable accepted-redesign reset basis, and an earlier epoch identity cannot be reused.
- Fresh RED discovery consumes a discovery epoch only when it adds at least one genuinely new material defect class in that stable epoch.
- Default discovery ceilings are Card=5, Milestone=4, Final Integration=3.
- GREEN discovery, closure verification, ordinary repair and recurrence of an already-known class do not consume a discovery epoch.
- Each material defect class derives failed repair→closure-verification rounds; the third RED closure round reaches the default per-class breaker.
- Reaching either breaker routes to Main convergence/root-cause analysis without converting RED to GREEN.
- After closure of known findings, a reached breaker freezes exactly one fresh post-convergence full-scope validation.
- RED post-convergence validation routes to structural resolution and terminal post-convergence state forbids another ordinary same-epoch review continuation.
- A new accepted structural authority/acceptance redesign may establish a new epoch with durable reset basis.
- Existing explicit T01 RED discovery history with frozen finding IDs can transition into the first convergence-aware T02 closure without retroactive discovery-epoch invention.
- Active V1-migrated review attempts receive the explicit convergence-aware Card/E01 shape.

## Changed surface

The exact comparison `19b7b9c0d335afb046493bff1a0a13dc4c310ec6...4b63b0645432b185b12ffb04bd83268d1c584116` is ahead by 14 commits with no divergence. It modifies only:

- `tools/review_contract.py`
- `tools/state_contract.py`
- `tools/router.py`
- `templates/REVIEW_ATTEMPT.toml`
- `tools/v1_migration.py`
- `workflow/REVIEW.md`
- `workflow/STATE.md`
- `workflow/RECOVERY.md`
- focused tests in `tests/test_review_contract.py`, `tests/test_state_contract.py`, `tests/test_router.py`, and `tests/test_v1_migration.py`

No BOOT-B/C/D, observation/disposition, M03+ or runtime/provider/model/session semantics were introduced.

## Falsification coverage

Focused fixtures cover:

- Card/Milestone/Final 5/4/3 discovery ceiling matrix;
- genuinely-new-class-only discovery counting;
- known-class recurrence excluded from discovery counting;
- three failed closure rounds for one class triggering convergence;
- stable epoch preservation and reset-basis enforcement;
- prohibition on epoch-ID reuse;
- T01 RED → T02 convergence-aware closure compatibility;
- post-convergence validation only after a reached threshold;
- exactly one post-convergence validation;
- no same-epoch review continuation after terminal post-convergence validation;
- router convergence mode-switch and structural-resolution routing;
- active V1 migration convergence shape.

## Raw verification

GitHub Actions push run `36023156689`, job `107712851684`, ran on exact head `4b63b0645432b185b12ffb04bd83268d1c584116` and completed **SUCCESS**. The `Run repository checks` step completed successfully.

Exact final readback blob identities:

- `tools/review_contract.py@b8f485b983934d6a2b71530eb2ecdde236789ae6`
- `tools/state_contract.py@2d125b27e3ddb534038119c52b6bbba8f5dc8d4f`
- `tools/router.py@1cbfd896b3cbbfec893c992313c5f643b163d2a8`
- `templates/REVIEW_ATTEMPT.toml@153e675ff418b9686e80fae0a95397edf143f8fa`
- `tools/v1_migration.py@9852ff6c0d546213bde5ac9ec54bee3bfd27aac4`
- `workflow/REVIEW.md@a3f0d21ce5794b11623377e68f9d0308054ba038`
- `workflow/STATE.md@f9ac2110acf21a0bf10462b0d358d46bec8f587f`
- `workflow/RECOVERY.md@3872e36688f5cce4c1fa75ff8d4f23d6cbb45648`
- `tests/test_review_contract.py@eae850979b8fa653102a4fd58e9add0cdf9b4e2f`
- `tests/test_state_contract.py@8bb39156a11eb6b9c47c5de4d46b6a6e353413e4`
- `tests/test_router.py@35e295fd943c915779c50437453dfc51003b246b`
- `tests/test_v1_migration.py@a42b6eaf607c66eb06d408924d868685d611adae`

The implementation is ready for independent exact-subject review.
