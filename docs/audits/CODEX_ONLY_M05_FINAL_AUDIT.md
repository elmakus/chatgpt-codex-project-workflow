# Audit — CODEX_ONLY M05 final regression and publication readiness

Status: implementation verification for `M05-T01`
Plan: `planning/CODEX_ONLY_MASTER_PLAN.md#M05--end-to-end-regression-architecture-audit-and-publication-readiness`
Requirements: CO-REQ-001..028
Current target checked: `main` at `d64d8c1d7f05ce2a2584ffcb3ade4634263bbc95`
Workstream merge base: `6b0445256b417f82431fb7b2704f56691eb4e7ae`

## 1. Routing and namespace isolation

GREEN:
- root routing contains distinct `chatgpt_only`, `codex_only` and legacy fallback routes;
- `workflow/codex_only/` and current-main `workflow/chatgpt_only/` each contain 22 policy-owner files with the same filename set;
- active Codex-only owner files contain no dependency on `workflow/chatgpt_only/*`, `workflow/codex/*`, `workflow/legacy/*` or `workflow/contracts/*`;
- no M04 foundation/deferred activation marker remains in the live Codex-only namespace;
- feature-side changes under `workflow/chatgpt_only/*` relative to the workstream merge base are zero;
- root `PROJECT.md` still declares `execution_policy: chatgpt_only`.

## 2. Project/runtime and review boundary

GREEN:
- Codex Main alone writes shared Task Board/integration state;
- runtime worker/session/model/profile/invocation/resume/concurrency identity remains outside required Project Workflow state;
- formal review uses one immutable exact subject and independent Tester role;
- Tester does not repair production;
- RED routes to owning Executor correction and a changed implementation creates a new review subject;
- same logical Tester reuse and fail-closed replacement are runtime-transparent;
- no second mandatory normal-ChatGPT review follows a qualifying Codex-managed verdict.
## 3. Bounded-parallel and recovery regression

GREEN semantic checks cover:
- serial execution remains valid by default;
- JIT parallel eligibility requires dependencies, `parallel_safe`, disjoint `write_scope`, non-conflicting `exclusive_resources`, workspace isolation and recoverable integration base;
- unsafe candidates deterministically fall back to serial;
- batch membership/order/base remain finite and frozen;
- Codex Main validates/integrates worker results and preserves shared-state single-writer ownership;
- same-member retry and terminal blocked-batch reconciliation preserve failed/successful lineage;
- runtime loss/replacement does not alter durable project obligations or review meaning.

## 4. Full lifecycle and workstream scenarios

GREEN semantic matrix:
- `#issue` / `#feature` Intake and idempotent workstream recovery;
- Brainstorming with user-owned first promotion into Definition;
- Research Origin/Return reconciliation including execution-resolution chaining;
- Definition Complete and Planning/plan-review;
- qualified one-Card micro-fix;
- Execution Prep, Execution, formal Review and Recovery;
- exact manifest ↔ Task Board binding plus legacy/default fallback;
- independent versus genuinely stacked workstreams and legal stacked integration paths;
- current-target integration refresh and exact review preservation/invalidation;
- terminal target-side durable package, source-branch deletion gate and automatic continuation.

## 5. Schema/static hygiene

GREEN:
- Codex-only Task Board/workstream templates contain no required `session_id`, `invocation_id`, worker/model/profile/worktree identity or scheduler/queue schema;
- no added conflict markers are present in the feature diff;
- historical M01 trailing-space findings were non-behaviorally normalized in M05 so final feature-range `git diff --check` can be GREEN.

Parser-based YAML validation is not claimed because PyYAML is unavailable on the verification runner; structural inspection and prior policy/template checks remain the claimed evidence.
## 6. Legacy-property and documentation regression

GREEN:
- the M01 legacy inventory still covers Codex Main accountability, continuous multi-milestone progression, bounded parallelism, Executor/Tester separation, strategic escalation, worktree isolation, integration ownership, recovery and no capability-preflight policy switching;
- README now documents both dedicated migrated policy namespaces and the Codex-only runtime/project boundary;
- CHANGELOG records the Codex-only migration;
- `docs/CODEX_ONLY_MIGRATION_NOTES.md` records routing, state ownership, review, concurrency, workstream and integration-safety rules.

## 7. Current-target trial integration

A trial merge tree against current `main` is textually clean.

Semantic inspection is intentionally **not** treated as clean: without target refresh/reconciliation, merged root `PROJECT.md` would retain feature-branch global status/authority pointers for the Codex-only workstream instead of current target-owned project state.

Required Close action before final integration:
1. refresh/reconcile the workstream against current `main`;
2. preserve current target-owned global `PROJECT.md` state and `execution_policy: chatgpt_only`;
3. rerun affected compatibility verification on the reconciled subject;
4. freeze or reuse manifest final-integration review only after that refresh;
5. reread target immediately before integration and repeat refresh if it moved.

This is a bounded technical integration obligation already owned by M05/Close, not a reason to reopen Definition or M01–M04.

## 8. Requirement coverage conclusion

- CO-REQ-001..006 and CO-REQ-026..028: GREEN through M01/M04 plus M05 routing/isolation/non-regression checks.
- CO-REQ-007..016 and CO-REQ-024..025: GREEN through M02 plus M05 review/runtime/recovery regression.
- CO-REQ-017..023: GREEN through M03 plus M05 serial/parallel/recovery regression.
- CO-REQ-005 lifecycle integration across all prior groups: GREEN through M04 plus the M05 end-to-end scenario matrix.

No unexplained accepted-requirement or legacy-property loss was found.

## 9. M05-T01 conclusion

GREEN verification/readiness result, subject to the normal Close-owned current-target reconciliation and manifest final-integration review gate described above.

No behavioral correction Card is required from this audit.
