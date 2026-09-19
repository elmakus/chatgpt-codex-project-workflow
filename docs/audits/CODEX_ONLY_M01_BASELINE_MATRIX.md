# Audit — CODEX_ONLY M01 baseline parity and legacy behavior matrix

Status: implementation evidence for `M01-T01`  
Baseline: Project Workflow `main` / workstream base `6b0445256b417f82431fb7b2704f56691eb4e7ae`  
Plan: `planning/CODEX_ONLY_MASTER_PLAN.md` (`CO-P1`, approved)  
Requirements: `requirements/CODEX_ONLY_POLICY.md` (`CO-R1`)  
Purpose: prevent semantic loss while migrating `codex_only` out of the legacy shared stack.

## 1. Binding rules for this inventory

- `workflow/chatgpt_only/` is the semantic lifecycle reference, not a mechanical copy source.
- The future policy owner for migrated semantics is `workflow/codex_only/`; controlled duplication is acceptable.
- `workflow/common/` is used only for semantics already proven genuinely policy-neutral. M01 does not extract new shared execution semantics merely to deduplicate text.
- Legacy `workflow/codex/*`, shared top-level workflow execution/review files, `workflow/contracts/*`, legacy routing and the historical `feat/bounded-parallel-task-cards` branch are evidence only.
- Root `workflow/CONTEXT_ROUTING.md` is a later M04 cutover target. M01-T01 does not edit routing.
- Project Workflow owns durable project authority/state. `codex_workflow` owns concrete worker/session/model/profile/invocation/wait/resume/concurrency mechanics.
- The repository itself remains `execution_policy: chatgpt_only`.

Classification vocabulary:
- **carry over** — lifecycle meaning is expected to remain materially the same, with policy-local naming/actor wording as needed;
- **adapt** — the lifecycle concept remains, but Codex-specific execution/review/concurrency/runtime-boundary semantics must change;
- **common** — use an already-genuinely-common contract rather than duplicating policy-specific semantics;
- **N/A** — evidence/mechanism does not become a `codex_only` policy contract.

## 2. Current chatgpt_only policy-local parity matrix

Every current file under `workflow/chatgpt_only/` appears exactly once below.

| Current source | Future semantic owner | Classification | Required preservation / Codex delta | Primary milestone |
|---|---|---|---|---|
| `workflow/chatgpt_only/BRAINSTORMING.md` | `workflow/codex_only/BRAINSTORMING.md` | carry over | Preserve exploratory authority, durable scope/revision and user-owned Definition promotion; no worker-runtime semantics. | M01/M04 |
| `workflow/chatgpt_only/CLOSE.md` | `workflow/codex_only/CLOSE.md` | adapt | Preserve acceptance/publication/target-refresh/continuation; replace fresh-ChatGPT review realization with qualifying Codex-managed formal review and Codex Main continuation. | M04 |
| `workflow/chatgpt_only/CONTEXT_HEALTH.md` | `workflow/codex_only/CONTEXT_HEALTH.md` | adapt | Preserve safe durable handoff/recovery hygiene for the coordinating context only; must not own worker/session lifecycle, resume or replacement mechanics belonging to `codex_workflow`. | M02/M04 |
| `workflow/chatgpt_only/DEFINITION.md` | `workflow/codex_only/DEFINITION.md` | carry over | Preserve requirements/decision authority, Definition completeness and escalation boundaries; actor wording may become policy-neutral/Codex Main wording. | M01/M04 |
| `workflow/chatgpt_only/EXECUTION.md` | `workflow/codex_only/EXECUTION.md` | adapt | Codex Main fixed executor/coordinator; worker delegation remains runtime-owned; support serial default, bounded ready sets, Main-owned shared state and formal review continuity. | M02/M03 |
| `workflow/chatgpt_only/EXECUTION_PREP.md` | `workflow/codex_only/EXECUTION_PREP.md` | adapt | Preserve JIT/L2 authority and deferred decomposition; add current-state parallel eligibility proof and bounded lane preparation without runtime worker selection. | M03 |
| `workflow/chatgpt_only/INTAKE.md` | `workflow/codex_only/INTAKE.md` | carry over | Preserve explicit `#issue`/`#feature` discovery, branch-isolated manifest creation/recovery and path classification; no global scheduler. | M01/M04 |
| `workflow/chatgpt_only/MICRO_FIX.md` | `workflow/codex_only/MICRO_FIX.md` | adapt | Preserve bounded no-plan exception, manifest/Task Board binding and final-integration gate; adapt executor/reviewer realization to Codex Main + formal independent worker review. | M02/M04 |
| `workflow/chatgpt_only/PLANNING.md` | `workflow/codex_only/PLANNING.md` | adapt | Preserve strategic planning authority and JIT boundaries; candidate parallelism remains planning-only and cannot certify future runtime safety; plan review realization changes. | M02/M03/M04 |
| `workflow/chatgpt_only/PLAN_REVIEW.md` | `workflow/codex_only/PLAN_REVIEW.md` | adapt | Preserve exact immutable plan subjects and independent verdict/evidence; independence is role/subject behavior, not mandatory fresh normal-ChatGPT identity. | M02 |
| `workflow/chatgpt_only/RECOVERY.md` | `workflow/codex_only/RECOVERY.md` | adapt | Recover project obligations from durable repository state regardless of worker resume/replacement; never require runtime session IDs as project identity. | M02/M03 |
| `workflow/chatgpt_only/REPOSITORY.md` | `workflow/codex_only/REPOSITORY.md` | adapt | Preserve branch/workstream isolation and add intra-workstream lane/worktree isolation for concurrent local mutation; keep integration ownership with Main. | M03/M04 |
| `workflow/chatgpt_only/RESEARCH.md` | `workflow/codex_only/RESEARCH.md` | carry over | Preserve durable Research origin/return/reconciliation semantics and strategic ownership; runtime Investigator realization stays outside Project Workflow. | M01/M04 |
| `workflow/chatgpt_only/REVIEW.md` | `workflow/codex_only/REVIEW.md` | adapt | Formal reviewer must be independent of implementation owner, cannot repair production, reviews immutable subject, preserves RED evidence, and may be reused on a new subject when still independent/safe. | M02 |
| `workflow/chatgpt_only/ROUTER.md` | `workflow/codex_only/ROUTER.md` | adapt | Preserve durable-priority routing, locator-only recovery and deterministic continuation; route review/corrections/parallel-ready state without fresh-ChatGPT identity as a universal gate. | M02/M03/M04 |
| `workflow/chatgpt_only/STATE.md` | `workflow/codex_only/STATE.md` | adapt | Replace one-in-progress-Card invariant with serial default plus bounded compatible ready/active set; Codex Main remains sole shared Task Board/integration writer. | M02/M03 |
| `workflow/chatgpt_only/TASK_BOARD_TEMPLATE.yaml` | `workflow/codex_only/TASK_BOARD_TEMPLATE.yaml` | adapt | Preserve default-board compatibility while adding only project-level bounded-parallel/recovery/provenance fields required by CO-R1; exclude runtime IDs. | M02/M03 |
| `workflow/chatgpt_only/TASK_CARDS.md` | `workflow/codex_only/TASK_CARDS.md` | adapt | Preserve bounded authority slices/JIT; add explicit dependency/`parallel_safe`/`write_scope`/`exclusive_resources` semantics needed for JIT eligibility. | M03 |
| `workflow/chatgpt_only/TASK_CARD_TEMPLATE.md` | `workflow/codex_only/TASK_CARD_TEMPLATE.md` | adapt | Add optional policy-level parallel metadata while keeping runtime worker/profile/session details out of Card authority. | M03 |
| `workflow/chatgpt_only/WORKSTREAMS.md` | `workflow/codex_only/WORKSTREAMS.md` | adapt | Preserve manifest selection, default-board compatibility, stacked workstreams and target refresh; add bounded intra-workstream lanes while keeping no global mutable scheduler. | M03/M04 |
| `workflow/chatgpt_only/WORKSTREAM_TASK_BOARD_TEMPLATE.yaml` | `workflow/codex_only/WORKSTREAM_TASK_BOARD_TEMPLATE.yaml` | adapt | Preserve manifest binding and workstream-local state; support serial default + bounded compatible Card sets with Main-owned coordination and no runtime IDs. | M02/M03 |
| `workflow/chatgpt_only/WORKSTREAM_TEMPLATE.yaml` | `workflow/codex_only/WORKSTREAM_TEMPLATE.yaml` | carry over | Workstream identity/routing/final-integration review ownership remains project-level; reviewer realization changes in REVIEW/CLOSE, not by storing worker sessions here. | M01/M04 |

### Already-common contracts

The existing `workflow/common/` namespace remains the first candidate for genuinely policy-neutral authority only:

- `AUTHORITY.md`
- `BRAINSTORMING.md`
- `DEFINITION.md`
- `OPENSPEC.md`
- `RESEARCH.md`
- `USER_STOP.md`

M01 must not move execution, review, Task Board, workstream, concurrency or runtime-boundary semantics into `common` merely to reduce duplication.

## 3. Legacy/shared evidence inventory and disposition

| Evidence source | Useful evidence | Disposition for dedicated codex_only |
|---|---|---|
| `workflow/CONTEXT_ROUTING.md` | Current root dispatcher and migration invariant. | **Preserve then edit in M04 only**: add explicit `codex_only -> workflow/codex_only/...`; keep `chatgpt_only` isolated and other policies on legacy. Not an implementation base. |
| `workflow/legacy/CONTEXT_ROUTING.md` | Existing legacy policy dispatch/recovery precedence. | **Preserve for non-migrated policies**. After M04, `codex_only` must no longer enter this route. |
| `workflow/codex/CODEX_ORCHESTRATION.md` | Codex Main accountability; project/runtime boundary; bounded parallel mapping; independent reviewer worker; Main integration ownership. | **Adapt semantics** into policy-local M02/M03/M04 contracts. Do not import this file at runtime from the new namespace. Runtime worker mechanics remain in `codex_workflow`. |
| `workflow/codex/EXECUTION.md` | Fixed Codex execution, no capability preflight, continuous multi-milestone execution, independent-review continuity. | **Adapt semantics** into `workflow/codex_only/EXECUTION.md`/ROUTER/CLOSE. Reject dependency on shared `workflow/EXECUTION.md`. |
| `workflow/codex/HANDOFF.md` | Strategic escalation boundary from worker evidence back to project authority. | **Preserve intent / adapt route** through codex_only Router -> Research/Planning/Definition/user gate. Do not make a correlated ChatGPT control channel or runtime session handle a Project Workflow requirement. |
| `workflow/EXECUTION.md` | Shared legacy Refresh/DoD/no-preflight/parallel/continuation semantics. | **Evidence only**. Preserve applicable behavior in policy-local modules; **reject** the shared execution core as architecture for migrated codex_only. |
| `workflow/EXECUTION_PREP.md` | Legacy JIT decomposition and bounded-parallel metadata preparation. | **Evidence only / adapt** into codex_only Execution Prep with CO-R1 JIT proof and single-Main ownership. |
| `workflow/REVIEW_AND_HANDOFF.md` | Legacy policy-specific reviewer selection, milestone close, handoff and automatic next-milestone continuation. | **Evidence only / adapt** into codex_only Review/Close/Router. No mandatory user/normal-ChatGPT handoff solely for Codex reviewer independence. |
| `workflow/BRAINSTORMING.md`, `workflow/PLANNING.md`, `workflow/RESEARCH.md` | Older shared lifecycle semantics. | **Secondary evidence only**. Current `workflow/chatgpt_only/` is the lifecycle reference where the two differ. |
| `workflow/contracts/GITHUB_STATE.md` | Coordinator-owned shared state, lane/base pointers, bounded parallel integration/recovery. | **Adapt useful project semantics** into codex_only policy-local State/Workstreams/Repository/Recovery. Reject assumptions that conflict with current manifest-selected Task Board model. |
| `workflow/contracts/TASK_CARDS.md` | `parallel_safe`, `write_scope`, `exclusive_resources`, dependency/JIT semantics. | **Adapt** into codex_only Task Cards; eligibility remains JIT and serial is default. |
| `workflow/contracts/TASK_EXECUTION.md` | Readiness, Refresh Gate, DoD, no capability-preflight policy switching, review boundary. | **Adapt** into codex_only Execution/State. Do not copy executor/session mechanics into project state. |
| `workflow/contracts/OPENSPEC.md` | OpenSpec behavior-contract conventions. | **Use common policy-neutral owner where applicable** (`workflow/common/OPENSPEC.md`); do not create a legacy-contract dependency. |
| `workflow/contracts/PROJECT_REPOSITORY.md` | Legacy authority/topology/state ownership rules. | **Evidence only** for compatibility/recovery; codex_only uses current Project Workflow authority + policy-local repository/workstream contracts. |
| `workflow/chatgpt/CAPABILITY_GATE.md`, `workflow/chatgpt/EXECUTION.md` | Mixed/legacy ChatGPT adapter and capability routing. | **N/A to codex_only**. Preserve for legacy/mixed routes; never import into fixed `codex_only`. |
| historical branch `feat/bounded-parallel-task-cards` | Prior bounded-parallel implementation ideas against the old shared stack. | **Evidence only, not parent/dependency**. Use only to detect useful behavior not already captured by CO-R1; do not merge/copy its architecture wholesale. |

## 4. CO-REQ-026 useful legacy property disposition matrix

All nine properties named by `CO-REQ-026` have an explicit disposition.

| Useful legacy property | Disposition | Target ownership / proof path |
|---|---|---|
| Codex Main accountability | **preserve + tighten** | M02/M03: Codex Main is project-level coordinator and sole shared Task Board/integration writer; worker lanes cannot become project-state owners. |
| Continuous multi-milestone progression | **preserve + adapt** | M04 Close/Router/Execution: continue across already-approved milestones without returning to normal ChatGPT solely for routing/review; real strategic/user/authorization/runtime blockers still stop. |
| Bounded parallelism | **preserve + redesign to CO-R1** | M03: serial default, bounded compatible ready set, JIT proof immediately before concurrency; no generic DAG/global scheduler. |
| Executor/Tester separation | **preserve + tighten** | M02 Review/Execution: Tester cannot repair production; RED goes through Main to owning Executor; corrected implementation is a new immutable subject. |
| Strategic escalation | **preserve** | M02/M04 Router/Research/Planning/Definition: workers cannot change accepted authority; Main routes evidence to the correct project authority boundary. |
| Lane/worktree isolation | **preserve + extend** | M03 Repository/Workstreams: separate worktree/equivalent for concurrent local mutation both intra-workstream lanes and cross-workstream work. |
| Integration ownership | **preserve + tighten** | M03/M04: Codex Main integrates lane results deterministically and owns shared integration state; workers return bounded results/evidence only. |
| Recovery | **preserve + decouple from runtime identity** | M02/M03: reconstruct obligations/review subjects/lane results from repository state whether runtime resumes or replaces workers; no session/profile/model IDs in project authority. |
| No capability-preflight policy switching | **preserve** | M02/M04 Execution/Router: fixed `codex_only` never invokes policy switching because a capability might be missing; concrete blockers use normal recovery/authority paths. |

No useful property is rejected outright. What is rejected are legacy **mechanisms** that violate the accepted architecture.

## 5. Explicitly rejected legacy mechanisms

The following must not leak into the dedicated policy even when a legacy file contains otherwise-useful behavior:

1. shared `workflow/EXECUTION.md` / `workflow/contracts/*` as the architectural runtime base for migrated codex_only semantics;
2. a new shared ChatGPT/Codex conditional execution core created for deduplication;
3. fresh normal-ChatGPT identity as the universal realization of codex_only independent review;
4. Tester/reviewer production repair;
5. Project Workflow persistence of `session_id`, `invocation_id`, Muse leases, model/profile/reasoning selection or worker-resume protocol;
6. worker lanes mutating shared Task Board/integration state;
7. planning-time certification of future parallel safety without current-state JIT proof;
8. unbounded/generic DAG scheduling or a repository-global mutable workstream scheduler;
9. fixed-policy Capability Gate/capability inventory or automatic execution-policy switching after runtime failure;
10. treating the historical bounded-parallel branch as a merge parent or architectural source of truth.

## 6. M01 implementation dependency map

The inventory yields the following safe order for subsequent M01 work:

1. **Policy-local skeleton and low-delta lifecycle modules** — establish the full `workflow/codex_only/` file ownership surface without root cutover.
2. **Foundational boundary/state placeholders** — adapt only enough Router/State/Execution/Review/Recovery/template contracts to establish policy-local ownership and explicit M02/M03 JIT boundaries; do not prematurely freeze detailed provenance/parallel schema.
3. **Static parity/boundary checks** — verify every CO-REQ-005 lifecycle owner exists, no codex_only module imports `workflow/chatgpt_only/*` or legacy shared execution ownership, and root routing remains unchanged.
4. Defer exact formal-review provenance fields to **M02** and exact bounded-parallel fields/ready-set semantics to **M03**, as required by CO-P1.

This means M01 can create a complete namespace **ownership surface** without pretending M02/M03 implementation details are already final.

## 7. Requirement trace for this evidence

- `CO-REQ-005`: every current ChatGPT-only lifecycle module/template is mapped to a future codex_only semantic owner.
- `CO-REQ-026`: all nine required useful legacy properties have preserve/adapt dispositions.
- `CO-REQ-027`: legacy Codex/shared/routing/contracts are explicitly evidence-only and are not the architectural base.
- `CO-REQ-028`: repository root execution policy stays `chatgpt_only`; this Card does not edit `PROJECT.md` execution policy or root routing.

Runtime capability baseline remains external evidence only: `elmakus/codex_workflow v1.1.17-private.12`, source `d285aa1a271258052d23e3a2d3b585117fc1e862`. Its worker/session implementation details are intentionally not copied into this matrix as Project Workflow authority.
