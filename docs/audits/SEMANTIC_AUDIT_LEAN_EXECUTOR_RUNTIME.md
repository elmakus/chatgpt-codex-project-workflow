# Semantic Audit — Lean Executor Runtime

Date: 2026-09-18
Base: `main@56263c5941610874b2a6ee292e93632c177d309b`
Audited branch subject: `refactor/lean-executor-runtime@bee1da35bb8f7e1ff8f90d611c5fbb142f7243b6`
Verdict: **GREEN**

## Scope

Audit the executor-context refactor that:
1. reduces ordinary Task Card execution context;
2. separates Task Card authoring from runtime execution;
3. makes full GitHub/project state contracts conditional for ordinary serial execution;
4. removes active runtime instructions that enumerate executor tool/capability catalogs;
5. preserves all Codex-specific orchestration/parallel/review/continuation semantics.

## GREEN — lean normal ChatGPT execution path

Before this change, the always-read normal ChatGPT execution workflow core was approximately:
- `CHATGPT.md`: 405 words
- `CONTEXT_ROUTING.md`: 701 words
- `EXECUTION.md`: 2226 words
- `workflow/chatgpt/EXECUTION.md`: 1119 words
- total: **4451 words**

In practice, runtime inheritance could additionally force the executor into:
- `TASK_CARDS.md`: 1747 words
- `GITHUB_STATE.md`: 2073 words

After this change, ordinary serial ChatGPT execution reads:
- `CHATGPT.md`: 405 words
- `CONTEXT_ROUTING.md`: 784 words
- `EXECUTION.md`: 813 words
- `TASK_EXECUTION.md`: 796 words
- `workflow/chatgpt/EXECUTION.md`: 455 words
- total: **3253 words**

That is about **27% less always-read workflow context** versus the prior core, while also eliminating the normal need to read the ~3820 words of Task Card authoring + full GitHub state contracts.

## GREEN — Task Card authoring separated from execution

`workflow/contracts/TASK_CARDS.md` now owns:
- stable Task Card authoring/decomposition;
- exact authority-slice construction;
- deferred card creation;
- optional mixed-routing task requirements;
- bounded-parallel metadata.

`workflow/contracts/TASK_EXECUTION.md` now owns runtime semantics for an already-defined card:
- readiness/start;
- Refresh Gate;
- runtime-operation behavior;
- blocker handling;
- bounded execution/verification;
- Definition of Done;
- result state;
- review boundary;
- post-card continuation.

Task Card template inheritance points to `TASK_EXECUTION.md` + `EXECUTION.md`, not to the authoring contract.

## GREEN — full GitHub State is conditional

`GITHUB_STATE.md` remains authoritative for extended state semantics:
- bounded-parallel coordinator/lane state;
- review lifecycle;
- milestone close/continuation;
- consistency/recovery;
- other advanced Task Board reconciliation.

Core single-card start/block/done semantics are canonical in `TASK_EXECUTION.md`.

Ordinary serial execution therefore does not need to load the full state contract.

## GREEN — shared execution core remains complete by routing

`workflow/EXECUTION.md` retains the ordinary shared loop and routes conditional boundaries explicitly:

- bounded parallel → `TASK_CARDS.md` + `GITHUB_STATE.md` + executor orchestration;
- JIT decomposition/refinement → `EXECUTION_PREP.md` + Task Card authoring;
- independent review → `REVIEW_AND_HANDOFF.md`;
- milestone acceptance/close/publication → `REVIEW_AND_HANDOFF.md` + `GITHUB_STATE.md`;
- strategic blocker → strategic authority;
- failure recovery → `CONTEXT_ROUTING.md#failure-recovery`.

No conditional class was deleted merely because ordinary ChatGPT does not need it.

## GREEN — Codex knowledge preserved

Codex-specific files remain essentially the same size and retain their responsibilities:

- `workflow/codex/EXECUTION.md` still contains codex-only continuous execution, JIT refinement, independent review, mixed boundary, continuation and strategic boundary.
- `workflow/codex/CODEX_ORCHESTRATION.md` still contains project/runtime domain boundary, Main accountability, bounded-parallel Task Card mapping, independent reviewer orchestration boundary, worker strategic boundary and completion boundary.
- `workflow/codex/HANDOFF.md` still owns ChatGPT↔Codex kickoff/return/strategic escalation.
- `GITHUB_STATE.md` still retains advanced coordinator/parallel/review/milestone/recovery state needed by Codex Main.
- installed `codex_workflow` remains authoritative for internal Codex worker/model/lifecycle mechanics.

Automated semantic checks confirmed presence of:
- Codex Main accountability;
- bounded-parallel mapping;
- codex-only continuous execution;
- codex-only independent review;
- shared JIT route;
- milestone continuation;
- review state and milestone state contracts.

## GREEN — no executor tool catalog

Active normative runtime/bootstrap files no longer enumerate specific executor tool families or credential mechanisms as a capability catalog.

The rule is now:
- do not inventory capabilities under fixed policy;
- do not teach the executor which tools it has;
- attempt the concrete required operation with the actual runtime;
- allow ordinary executor-local remediation when permitted;
- if the operation still cannot proceed, persist the exact blocker and request the smallest user-provided input/access/authorization actually required.

This applies to ChatGPT and Codex.

The `mixed` Capability Gate remains intentionally unchanged as **pre-assignment routing**. It is not a fixed-policy/runtime capability inventory.

## GREEN — ChatGPT-specific behavior preserved

The slim ChatGPT adapter still owns:
- normal ChatGPT runtime/session behavior;
- local-vs-production truth boundary;
- human-facing ELI5 control summary;
- fresh-session/review handoff behavior;
- session continuity;
- fixed/mixed continuation behavior;
- bounded-parallel rule that ChatGPT need not manufacture concurrency.

## GREEN — review/close semantics preserved

`REVIEW_AND_HANDOFF.md` now applies `TASK_EXECUTION.md` DoD for card close and loads full GitHub State only when advanced state semantics are relevant.

Fresh-chat independent review, branch-aware copy-paste prompt, milestone acceptance/publication verification and next-milestone continuation remain unchanged.

## Final assessment

**GREEN.** The refactor reduces ordinary executor context and removes runtime tool catalogs without deleting Codex-specific knowledge or weakening Task Card authority, state durability, review independence, parallel coordination, JIT planning, milestone continuation or blocker semantics.
