# M03-T02 — runtime-neutral execution acceptance evidence

Date: 2026-09-22
Card: `M03-T02`
Result: GREEN
Target repository: `elmakus/project_workflow_v2`
Target commit: `d4e9f9f261aca0c13f6f0ab36e03e421e084639d`
Target tree: `bf0ffd0675f8c359da3ca41d3154229274095f2d`
Draft PR: `elmakus/project_workflow_v2#3`

## Accepted behavior

The exact target implements M03.P2 without runtime-specific state:
- one selected Project Workflow Card remains the execution unit;
- Main/coordinator is the sole canonical Task Board/manifest reconciler;
- delegated execution qualifies only from runtime capability + bounded context + valid return path; otherwise direct execution uses the same semantic contract;
- zero/one/many runtime-internal workers do not create extra Cards or canonical worker state;
- Main validates returned work before one normalized semantic result is persisted;
- semantic result records Card ID, immutable implementation subject, durable evidence refs and tests/readback summary only;
- runtime/provider/model/session/worker/invocation identity is rejected from the result contract;
- invalid/incomplete return stays in the current Card for correction; real blocker is distinct;
- an already durable valid result routes to result reconciliation/no-replay rather than implementation replay.

No Codex worker schema, Pi subagent adapter/package, scheduler or runtime role catalog was added.

## Verification

GitHub Actions run `35744790039` on the exact head completed successfully:
- production state tests: 25/25 PASS;
- production router tests: 33/33 PASS;
- M03 execution-contract tests: 4/4 PASS;
- package probe, production bundle validation, router CLI smoke and M01 baseline checks PASS.

Deterministic coverage includes direct/delegated realization reaching one semantic result contract, runtime-identity rejection, multiple evidence contributions without extra Cards, bad-return versus blocker classification, and durable-result no-replay routing.

PR #3 exact head/base is current and mergeable at readback.

## Pi boundary

Pi remains a runtime compatibility candidate. The implementation provides only the common semantic contract that a later audited Pi adapter may realize; existing Codex delivery/acceptance remains unchanged.
