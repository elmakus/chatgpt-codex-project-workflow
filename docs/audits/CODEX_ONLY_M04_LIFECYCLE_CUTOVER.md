# Audit — CODEX_ONLY M04 lifecycle integration and routing cutover

Status: implementation verification for `M04-T01`
Plan: `planning/CODEX_ONLY_MASTER_PLAN.md#M04--full-lifecycle-integration-routing-cutover-and-compatibility`
Requirements: CO-REQ-001..006, CO-REQ-024, CO-REQ-026..028 plus lifecycle integration of prior requirements.

## 1. Root routing split

Current branch root dispatcher contains exactly three policy shapes:

| Selected policy | Route |
|---|---|
| `chatgpt_only` | `workflow/chatgpt_only/ROUTER.md` |
| `codex_only` | `workflow/codex_only/ROUTER.md` |
| any other accepted non-migrated policy | `workflow/legacy/CONTEXT_ROUTING.md` |

The `codex_only` route explicitly restricts Project Workflow semantics to `workflow/common/*` + `workflow/codex_only/*`, keeps Codex Main as the sole shared project-state/integration writer, and leaves concrete runtime realization to `codex_workflow`.

The repository's own `PROJECT.md` still declares `execution_policy: chatgpt_only`.

## 2. Dedicated namespace completeness

The 22-file `workflow/codex_only/` ownership surface remains complete.

M04 replaced the remaining foundation/deferred lifecycle contracts with live policy contracts for:
- Intake;
- Brainstorming;
- Research;
- Project Definition;
- Planning;
- micro-fix;
- Context Health;
- Workstreams and Repository;
- Router;
- Close/final integration.

M02/M03 production contracts for Review, State, Execution, Execution Prep, Recovery and Task Cards were retained and reconciled rather than overwritten.

A full namespace scan found no remaining `non-routable before M04`, foundation-deferred or `M04 will reconcile` activation markers.

## 3. Feature lifecycle trace

A `#feature` request follows this durable path:

1. root dispatcher -> Codex-only Router;
2. Intake discovers/reuses or creates exact branch-isolated workstream and manifest;
3. Feature Intake materializes canonical Brainstorming state;
4. Brainstorming may open Research with exact Origin/Return target;
5. Research completion returns to the exact owning exploratory subject;
6. first Brainstorming -> Definition promotion is user-owned for the exact scope/revision;
7. Definition formalizes accepted requirements/decisions;
8. Planning creates milestone strategy and exact plan review record when required/recommended;
9. independent plan review is realized by a qualifying Tester, not by mandatory normal-ChatGPT identity;
10. Execution Prep/Execution use serial default or one finite M03 JIT batch;
11. Card/milestone review uses M02 immutable attempts and Tester non-repair;
12. Close performs integrated acceptance, branch target refresh/final-review reconciliation when applicable, publication and deterministic next-milestone continuation.

No step requires another policy namespace or legacy shared execution ownership.

## 4. Issue micro-fix trace

A qualified `#issue` micro-fix:

1. Intake records the exact bounded qualification and `next_route: execution_prep:micro_fix`;
2. Execution Prep materializes one bounded fix Card plus manifest-selected Codex-only Task Board;
3. Card state uses semantic `implementation_owner_role` plus the M02 nested review-attempt structure;
4. normal Execution/Review/Recovery apply without a synthetic milestone;
5. after terminal Card review, Close runs current-target refresh before final-review reuse/freeze;
6. identical stronger independent coverage may satisfy the distinct manifest gate via exact `covered_by`; otherwise exact manifest subject is frozen for an independent Tester;
7. final integration reconciles manifest/result/Task Board terminal package without inventing milestone state.

## 5. Branch-isolated, stacked and target-refresh trace

`WORKSTREAMS.md` preserves:
- manifest-first state selection and exact manifest ↔ Task Board binding;
- independent versus genuinely parent-dependent stacked workstreams;
- legal child -> parent or parent-first -> target integration paths;
- current-target refresh before final review/integration;
- textual plus semantic conflict checks;
- exact review-subject preservation when target movement changes ancestry only;
- invalidation/new review subject only when covered workstream behavior/content or acceptance surface materially changes;
- terminal namespaced workstream package and target readback before source-branch deletion.

M03 internal lane integration is explicitly distinct from workstream final integration.

## 6. M02/M03 compatibility

Preserved M02:
- one immutable subject per review attempt;
- append-only prior RED/GREEN evidence;
- semantic `implementation_owner_role: executor`;
- independent `reviewer_role: tester`;
- Tester never repairs production;
- qualifying Codex-managed verdict needs no second normal-ChatGPT review.

Preserved M03:
- serial execution valid by default;
- current-state JIT proof before concurrency;
- finite frozen batch membership/order/base;
- Main-only shared Task Board/integration writes;
- separate mutable workspace per concurrent local lane;
- deterministic ordered lane integration;
- deferred member review while batch is unresolved;
- prepared-batch unwind, bounded same-member retry and terminal launched-batch reconciliation;
- immutable historical lane/result/integration provenance.

## 7. Static boundary checks

GREEN:
- current branch vs current `main`: changed `workflow/chatgpt_only/*` files = **0**;
- root dispatcher is the intentional routing change;
- all 22 Codex-only policy-owner files remain present;
- active Codex-only policy files contain no path dependency on `workflow/chatgpt_only/*`, `workflow/codex/*`, `workflow/legacy/*` or `workflow/contracts/*`;
- the only legacy-policy reference needed for dispatch remains in root `workflow/CONTEXT_ROUTING.md`, outside the dedicated Codex-only runtime path;
- active YAML in `TASK_BOARD_TEMPLATE.yaml`, `WORKSTREAM_TASK_BOARD_TEMPLATE.yaml` and `WORKSTREAM_TEMPLATE.yaml` contains no concrete runtime worker/session/model/profile/invocation/resume/worktree identity and no scheduler/queue schema;
- conflict-marker scan: GREEN;
- trailing-whitespace scan: GREEN;
- root `PROJECT.md`: `execution_policy: chatgpt_only`.

The branch is intentionally still a branch-isolated workstream and may be behind current target `main`; M04 does not bypass the later `CLOSE.md` integration-refresh gate.

## 8. Acceptance conclusion

GREEN author-side verification for M04-T01 implementation.

The implementation changes root routing and live lifecycle behavior, so the Card remains non-terminal until a fresh independent review role judges one exact immutable implementation subject. The implementing chat must not issue that verdict.
