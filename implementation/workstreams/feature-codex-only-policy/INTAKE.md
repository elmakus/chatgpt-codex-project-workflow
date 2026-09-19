# Feature Intake — dedicated codex_only policy namespace

Workstream ID: `feature-codex-only-policy`
Kind: `feature`
Branch: `feat/codex-only-policy`
Status: complete
Date: 2026-09-19

## Operator intent

Create a complete dedicated `workflow/codex_only/` policy namespace for projects that select `execution_policy: codex_only`, using current `workflow/chatgpt_only/` lifecycle semantics as the reference baseline while adapting execution/review semantics to Codex Main + `codex_workflow`.

The workflow repository itself remains on `execution_policy: chatgpt_only`. This scope does not change that project execution policy.

## Accepted scope boundaries

- Route `chatgpt_only` only to `workflow/chatgpt_only/...`.
- Route `codex_only` only to `workflow/codex_only/...`.
- Leave other not-yet-migrated policies on the legacy route for later scopes.
- Controlled duplication between `chatgpt_only` and `codex_only` is acceptable.
- Do not introduce a new large shared/fixed execution core merely to reduce duplication.
- Only genuinely policy-neutral contracts may live under `workflow/common/`.
- Preserve the current ChatGPT-only lifecycle shape as the semantic reference: Intake, branch-isolated workstreams, manifest-selected Task Boards, legacy/default Task Board compatibility, Brainstorming/Research/Definition/Planning, Execution Prep/JIT, Task Cards, micro-fix, Research return, stacked workstreams, integration refresh, exact review subjects, durable recovery, Close/publication, locator-only fresh recovery, and no global mutable workstream scheduler.
- Project Workflow owns project semantics/state; `codex_workflow` owns worker/runtime mechanics.
- Project Workflow must not own session IDs, invocation IDs, Muse leases, worker resume protocol, model/reasoning/profile selection, worker waiting, or worker concurrency mechanics.
- `codex_workflow` must not own Project Workflow Task Board/review/router state.
- A qualifying independent Codex reviewer may satisfy the formal Project Workflow independent-review obligation; no additional mandatory normal-ChatGPT review is added merely because the formal reviewer is managed through `codex_workflow`.
- Implementation Tester cannot implement or repair production changes; RED returns findings through Main to the owning Executor, and a corrected implementation is a new immutable review subject.
- Reusing the same logically independent Tester for the new exact subject is allowed when independence remains valid; replacement is runtime-owned when resume/reuse is unsafe.
- Add bounded parallel Task Card support inside one `codex_only` workstream. Serial remains the default. Planning may identify candidate dependency/parallel structure; Execution Prep/JIT must verify current-state safety before concurrent execution.
- JIT safety includes dependency completion, `parallel_safe`, disjoint mutable `write_scope`, no conflicting `exclusive_resources`, isolated lane/worktree/equivalent workspace, recoverable integration base, and Codex Main ownership of shared Task Board/integration state.
- Legacy `workflow/codex/*`, shared `workflow/EXECUTION.md`, `workflow/contracts/*`, and legacy routing are compatibility/evidence inventory only.

## Pre-creation discovery

Repository baseline:
- integration target: `main`
- exact base: `6b0445256b417f82431fb7b2704f56691eb4e7ae`
- project execution policy: `chatgpt_only`
- open PRs: none

Existing potentially related branch evidence:
- `feat/bounded-parallel-task-cards` is 433 commits behind current `main`, diverged by 13 commits, and targets the former shared/legacy execution stack.
- it is evidence inventory only and does not provide required parent-only state.
- no existing dedicated `codex_only` branch/workstream/PR was found.

Base classification: independent.
Parent workstream: none.
Parent dependency: none.

## Runtime capability evidence

Verified external baseline:
- repository: `elmakus/codex_workflow`
- release/tag: `v1.1.17-private.12`
- release source commit: `d285aa1a271258052d23e3a2d3b585117fc1e862`
- published: 2026-09-19
- release includes stateful Muse logical worker sessions and fail-closed reservation/resume handling.

Runtime capability is evidence only, not Project Workflow authority.

## Policy-delta discovery result

Exact policy-specific deltas are durably captured in:
`brainstorming/CODEX_ONLY_POLICY.md`

The principal deltas from `chatgpt_only` are:
- explicit `codex_only` namespace routing;
- project-role contracts instead of fixed normal-ChatGPT executor identity;
- semantic independent-review contracts that can be fulfilled by Codex-managed independent workers;
- bounded intra-workstream parallel Cards with serial default and JIT safety verification;
- intra-workstream lane/worktree isolation when parallel local mutation exists;
- runtime-agnostic recovery/provenance that excludes worker/session mechanics.

No Definition-blocking research or unresolved strategic contradiction remains.

## Post-creation classification

Canonical exploratory record:
`brainstorming/CODEX_ONLY_POLICY.md`

Path classification: `brainstorming`
Next route: `brainstorming:codex-only-policy@R1`

The exploratory record is `ready_for_definition`. The initiating user explicitly authorized promotion of the conforming discovered scope if discovery found no unresolved strategic contradiction; the exact `codex-only-policy@R1` record therefore persists `Definition promotion authorization: user_authorized`.

Intake is complete. Router continuation is Project Definition for `codex-only-policy@R1`.
