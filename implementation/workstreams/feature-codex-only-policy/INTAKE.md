# Feature Intake — dedicated codex_only policy namespace

Workstream ID: `feature-codex-only-policy`
Kind: `feature`
Branch: `feat/codex-only-policy`
Status: active
Date: 2026-09-19

## Operator intent

Create a complete dedicated `workflow/codex_only/` policy namespace for projects that select `execution_policy: codex_only`, using current `workflow/chatgpt_only/` lifecycle semantics as the reference baseline while adapting execution/review semantics to Codex Main + `codex_workflow`.

The workflow repository itself remains on `execution_policy: chatgpt_only`. This scope must not change that project execution policy.

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
- A Codex-managed independent Tester may satisfy the formal Project Workflow independent-review obligation. Do not add a mandatory normal-ChatGPT review after a qualifying Tester verdict.
- Tester cannot implement or repair production changes; RED returns findings through Main to the owning Executor, and the corrected implementation is a new immutable review subject.
- Reusing the same logically independent Tester for the new exact subject is allowed when the independence contract remains valid; replacement is fail-closed/runtime-owned when reuse is unsafe.
- Add bounded parallel Task Card support inside one `codex_only` workstream. Serial remains the default. Planning may identify candidate dependency/parallel structure; Execution Prep/JIT must re-verify runtime safety from current repository state before parallel execution.
- Required JIT safety dimensions include dependency completion, `parallel_safe`, disjoint mutable `write_scope`, no conflicting `exclusive_resources`, isolated lane/worktree/equivalent workspace, recoverable integration base, and Codex Main ownership of shared Task Board/integration state.
- Legacy `workflow/codex/*`, shared `workflow/EXECUTION.md`, `workflow/contracts/*`, and legacy routing are compatibility/evidence inventory only, not the architectural base.

## Pre-creation discovery

Repository baseline:
- integration target: `main`
- exact base: `6b0445256b417f82431fb7b2704f56691eb4e7ae`
- project execution policy: `chatgpt_only`
- open PRs: none

Existing potentially related branch evidence:
- `feat/bounded-parallel-task-cards` exists, but it is 433 commits behind current `main`, diverged by 13 commits, and its relevant changes target the former shared/legacy execution stack.
- therefore it is evidence inventory only and does not provide required parent-only state for this feature.
- no existing `codex_only` dedicated workstream/branch/PR was found.

Base classification: independent.
Parent workstream: none.
Parent dependency: none.

## Runtime capability evidence

Verified external baseline:
- repository: `elmakus/codex_workflow`
- release/tag: `v1.1.17-private.12`
- release source commit: `d285aa1a271258052d23e3a2d3b585117fc1e862`
- published: 2026-09-19
- release explicitly includes stateful Muse logical worker sessions plus fail-closed session/workspace reservation and resume-conflict handling.

This is runtime capability evidence only, not Project Workflow authority.

## Post-creation route

The feature requires normal exploratory materialization before Definition.

Planned canonical exploratory record:
`brainstorming/CODEX_ONLY_POLICY.md`

Definition promotion is initially recorded as pending and may only become `user_authorized` for the exact ready revision. The initiating user request already contains explicit authorization to promote the conforming discovered scope after required discovery, provided no unresolved strategic contradiction remains.

Path classification: `brainstorming`
Next route: `brainstorming:codex-only-policy@R1`
