# M02Q-T23 bounded contract correction — mixed path-only Review inventory

## Trigger

Pre-mutation RF006 proof of the exact source snapshot `fbe55b3d76746d54ca05e8dda7ea99473d60cc25` showed that the 48 path-only Task Board `review_attempt` locators are not one homogeneous legacy-shaped set.

## Exact inventory

- Path-only review locators: 48.
- Legacy-shaped terminal attempts without `review_kind`: 31.
- Current-schema attempts already carrying `review_kind`: 17.
- No branch mutation of Review files or Task Board review locators occurred under the over-broad 48-legacy wording. Temporary Git blob/tree objects created during proof were never committed or referenced by the branch and carry no durable workflow authority.

The 17 current-schema attempts are M02R-T08 through M02R-T13 and M02Q-T01 through M02Q-T11. They require only exact Task Board commit+blob locators. Adding `legacy_migration` to them would violate RF006 because explicit/current attempts cannot prove legacy status.

## Bounded correction

T23 remains one OBL-M02Q-02 RF006 serving-migration outcome. Correct the stable contract before substantive mutation:

1. add exact uniquely derived `legacy_migration` provenance only to the 31 genuinely legacy-shaped terminal attempts;
2. preserve the 17 current-schema Review files byte-for-byte;
3. update all 48 path-only Task Board Review refs to exact commit+blob identity from one immutable post-file-migration snapshot;
4. prove the 31 legacy migrations with `verify_legacy_migration`, prove all 48 exact locators with `verify_review_attempt_locator`, and prove source/current semantic preservation.

This does not alter accepted strategy, required-seam topology, terminal verdict semantics or downstream ordering, so the correction remains bounded Execution work rather than Planning/Definition re-entry.
