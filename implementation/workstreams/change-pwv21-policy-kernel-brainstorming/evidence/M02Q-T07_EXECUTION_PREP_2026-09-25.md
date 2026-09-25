# M02Q-T07 Execution Prep — RF016 SessionStart canonical-router integrity

Both split P7 order-5 RF002 outcomes are DONE/GREEN. `M02Q-T06` explicit-stop precedence has exact Result `results/M02Q-T06.md@2f9374b4ee31cb8a286bf6b22d53f6d5f1050d1d:bba72c4d1440df0782e535d73756d5a4d6f4ba93` with fresh independent R01 GREEN; its `after-M02Q-T06` trigger is satisfied and now materializes this separate order-6 RF016 Card. The product candidate is `elmakus/project_workflow_v2@95b7c838f4e0e39464252d20036b1dd003039d31`; canonical workflow main remains `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`.

Pre-M03 audit H028 proved the SessionStart two-marker gate insufficient: `canonical_router` in `hooks/session-start.py:34-53` checks only `ROUTER_HEADER`/`ROUTER_SELECTOR` substring presence, so a two-marker-only file and a marker-preserving contradictory/truncated `workflow/ROUTER.md` both ENABLED instead of BLOCKING, with no digest/manifest reference. This Card replaces the substring gate with exact offline verification of canonical router bytes against a shipped bounded local package manifest carrying the exact Git blob identity (e.g. `.codex-plugin/router-integrity.json`); missing/malformed/mismatched manifest or router fails closed while untouched packages stay enabled and thin. P7 order-6 with REQ-011...017/REQ-092 and ADR-PWV2-002 thin bootstrap plus no remote fetch at normal SessionStart are the accepted authority. The manifest is release packaging metadata regenerated with legal future router updates, not workflow policy or a consumer pin. After RF016 is DONE/GREEN, P7 order-7 RF012 is next; M03 remains blocked until all 17 RF families and the separate M02Q Milestone Review are terminal GREEN.

## Seven-dimension decomposition audit

- Independent implementability: exact router-byte verification is independently useful after DONE/GREEN RF002; RF012 Definition-authority key remains a separate downstream Card.
- Falsifiability/testability: H028 two-marker-only and marker-preserving contradictory/truncated routers fail before correction; untouched exact-manifest router enables; missing/malformed/mismatch, escape and root controls discriminate.
- Reviewability: one Card Review covers SessionStart integrity and thin-bootstrap preservation without certifying RF012 authority binding or M02Q composition.
- Invariant/contract family: one delivery-integrity invariant couples shipped manifest identity with offline router-byte verification; manifest/mismatch/escape cases are siblings, not separate outcomes.
- Dependency ordering: consumes exact DONE/GREEN M02Q-T06 and transitive T05 completing both split RF002 outcomes in P7 serial order; RF012 follows by its JIT trigger.
- Atomic mutation/migration: manifest and SessionStart verification land together so no intermediate state enables a corrupted router; historical M01/M02/M02R and valid package behavior stay unchanged.
- Cross-surface coupling: SessionStart hook, package manifest and delivery tests share one RF016-local invariant; no coupling requires merging RF012 or another RF seam.

Decision: materialize one `M02Q-T07` Card for the P7 order-6 RF016 invariant. Simple card-local topology: one independently falsifiable family, no preferred-seam merge, multi-family Card, milestone absorption or review substitution.

## Bounded write/effect scope

Only `elmakus/project_workflow_v2` branch `work/pwv21-policy-kernel` is the product target. Expected edits are the SessionStart router-verification path, one small shipped package integrity manifest, and focused tests/docs essential to this behavior. Git commit/push and exact-head CI readback are authorized external effects.
