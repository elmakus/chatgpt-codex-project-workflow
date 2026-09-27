# M02Q-T23 late-oversize evidence — RF006 historical attempt-id compatibility

## Exact execution boundary

- Returning Card: `M02Q-T23`
- Origin: execution
- Consumer phase-1 subject: `elmakus/chatgpt-codex-project-workflow@a90424383e0613b36c18affbf60c6868c54ffdfa`
- Pre-migration source snapshot: `fbe55b3d76746d54ca05e8dda7ea99473d60cc25`
- Candidate RF006 verifier: `elmakus/project_workflow_v2@ae3d2d303fde8ee67dcfa24342549e96c0cf1d13`

## Preserved independently valid evidence

The source Board contains 48 path-only terminal Review locators. Phase 1 changes only the 31 legacy-shaped Review files by adding explicit `legacy_migration` provenance; the 17 current-schema `review_kind` files remain byte-identical.

Fresh exact-checkout readback proves:

- 25 legacy-shaped attempts pass `verify_legacy_migration` and exact `verify_review_attempt_locator`;
- 17 current-schema attempts remain byte-identical to the source and pass exact `verify_review_attempt_locator`;
- therefore 42/48 affected Review records already have independently valid identity/provenance evidence preserved at phase-1 commit `a90424383e0613b36c18affbf60c6868c54ffdfa`.

No Task Board Review locator has yet been rewritten, so the migration has not been laundered into completion.

## Newly exposed separable residual

Six historical M02 review attempts are legacy-shaped but carry a historical full attempt identifier in the `attempt` field:

- M02-T01-R07 through M02-T01-R12.

For example, the durable path is `reviews/M02-T01-R07.toml` and `attempt = "M02-T01-R07"`. Current RF006 canonical-path verification constructs `M02-T01-M02-T01-R07.toml` and rejects the exact historical record before legacy provenance can be accepted. All six fail for the same compatibility class.

Changing those six historical `attempt` values would rewrite terminal attempt identity and violate historical preservation. The remaining scope therefore requires a separately reviewable product compatibility correction that accepts this exact proven legacy form without weakening new/current canonical attempt identity, followed by completion of consumer Board exact-locator migration.

## REQ-130 classification

This is not an ordinary T23 implementation bug: the accepted T23 consumer migration cannot safely authorize a change to the already GREEN RF006 product verifier, and the product compatibility correction can be independently implemented, falsified and reviewed while the preserved 42-record evidence remains valid.

The residual scope returns to Execution Prep. No required Planning seam is merged, no new product intent is introduced, historical terminal Review semantics remain preserved, and T23 does not claim GREEN.
