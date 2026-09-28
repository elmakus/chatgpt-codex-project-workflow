# M02-S08-T01-R10 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@954d2a620ea5a4800cab0c3e3cfe2187948e6551:572a4cfb3fff860a793e6c38c5b947875139df60`

Exact implementation subject: `elmakus/project_workflow_v2@1c704352cb814f8b948570409578ab349010d07c`; `tools/pwv22_parallel.py` blob `69f89a665dfc68211acfc1bf97e92433d83a6d45`; `tests/test_pwv22_parallel.py` blob `dc26b8e5fdcef29e39caec4b32ac06c71c595199`.

## Independence

This fresh review context did not materially produce or repair the exact R10 subject. It independently inspected the frozen Result, R09 finding/correction, implementation and focused tests against the stable Task Card acceptance surface.

## Finding

The R09 implementation correction adds the required `sibling_claims` operand to `compatible_fan_in()` and checks each sibling proof against the admitted exact Card subject and admission-bound `mutating_owner`. The new focused owner-mismatch test exercises that correction.

However, the existing `test_stale_card_subject_rejected` call was not updated for the new function signature. Its direct `compatible_fan_in(...)` invocation passes `ADM` in the new `sibling_claims` position and shifts every following positional argument by one, leaving the required final `compatibility` argument absent. Python therefore raises `TypeError` at call binding instead of entering the function and producing the expected `NativeFoundationError`.

Consequently the focused test module as published cannot be GREEN, and the required stale-card-subject fan-in protection is no longer actually exercised by that regression. This contradicts the Result summary's statement that the existing exact-subject protections are retained in the focused fixture and fails the Card's required focused native-fixture test/readback surface.

## Required correction

Update the stale-card-subject fan-in regression to supply a valid `sibling_claims` sequence aligned with the exact sibling Card IDs/subjects, so the call reaches `compatible_fan_in()` and verifies rejection of the stale expected Card subject as `NativeFoundationError`. Run/read back the complete focused `tests.test_pwv22_parallel` module after the correction, preserve the R09 fan-in ownership proof checks, and publish a new immutable Result subject for fresh independent review.
