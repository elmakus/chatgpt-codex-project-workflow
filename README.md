# ChatGPT ↔ Codex Project Workflow

A GitHub-backed workflow for technical projects managed from normal ChatGPT chat and/or Codex according to an explicit project execution policy.

> Scope: this workflow uses **normal ChatGPT chat + Codex only**. ChatGPT Work is not part of the architecture, routing model or required operating mode.

## Core model

**ONE PROJECT = ONE REPOSITORY from the first idea.**

The project repository is durable project truth. It stores brainstorming, research, accepted decisions, requirements, approved planning, implementation contracts/state, OpenSpec, evidence and cumulative handoffs. This workflow repository stores only workflow rules, contracts, templates and bootstrap prompts.

### State ownership

The workflow deliberately separates contract from state:

- `implementation/TASK_BOARD.yaml` — **sole mutable execution-state authority**, including active independent-review state;
- approved Master Plan milestone subsections — default milestone contracts;
- `implementation/milestones/MXX.md` — optional JIT contract extensions only when the Master Plan needs material execution/acceptance detail;
- Task Card files — bounded authority/scope/acceptance/test contracts;
- cumulative handoff — compact summary of what became true at a completed milestone;
- root `PROJECT.md` — small high-level project router/policy/index, not a live tracker.

This avoids repeatedly synchronizing status, executor, SHA and result pointers across several documents.

### Execution policies

Every project chooses exactly one:

- `chatgpt_only` — ChatGPT is the fixed Task Card executor. No Capability Gate and no capability preflight. Start the work; if a concrete required operation cannot be performed, persist the runtime blocker and ask for the smallest remedy or an explicit policy change.
- `codex_only` — Codex is the fixed Task Card executor. No Capability Gate and no capability inventory/preflight. Project Workflow does not prescribe Codex's tool inventory; Codex starts with its actual runtime, handles ordinary executor-local remediation when permitted, and asks the user only when a concrete required operation still needs user-provided input/access/authorization.
- `mixed` — ChatGPT remains project router and uses the Capability Gate before new execution assignment to choose ChatGPT, Codex or BLOCKED.

Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`.

Changing policy requires an explicit user decision.

## Policy-first routing

Normal ChatGPT now enters through a small policy dispatcher:

```text
CHATGPT.md
→ project PROJECT.md
→ workflow/CONTEXT_ROUTING.md
→ one execution-policy namespace
```

The first migrated namespace is `workflow/chatgpt_only/`.

For `chatgpt_only`:
- common authority/brainstorming/research/OpenSpec/user-stop rules come only from `workflow/common/`;
- planning, execution preparation, Task Cards, state, execution, independent review, close/publication and recovery come only from `workflow/chatgpt_only/`;
- normal project execution handles exactly one READY Task Card at a time;
- other policy execution/orchestration semantics are outside the route.

The prior multi-policy router is preserved at `workflow/legacy/CONTEXT_ROUTING.md` for policies not yet migrated. This is a staged migration: legacy shared execution/contracts remain in place until those policies receive their own namespaces.

## Capability semantics

For fixed policies, capability availability is **runtime discovery**, not a recurring planning gate.

Execution Prep and Refresh Gate do not inventory executor tools/capabilities or attempt to prove that the fixed executor can perform every future operation. Refresh Gate checks current state, contracts, dependencies, interfaces, tests/evidence obligations and drift.

A capability becomes a blocker only when the active card reaches a concrete required operation that cannot proceed. No automatic executor/policy switch occurs. The user may provide the missing capability or explicitly change policy, after which Task Board is reconciled before reassignment.

## Authority preservation

Progressive disclosure reduces context volume, not accepted intent. Planning/decomposition/delegation follows **lossless by authority, selective by context**:

- a Task Card identifies the exact durable authority slice applicable to its bounded scope;
- implementation-shaping constraints are either carried explicitly into a downstream package or the worker/reviewer must read the exact authority reference;
- planner rationale is retained when omitting it could reasonably lead to a different implementation choice;
- executor and independent reviewer use the same applicable authority slice;
- summaries/paraphrases are navigation aids and never override requirements, accepted decisions or approved plan authority.

This allows stronger planning models to produce rich durable intent while smaller execution/review contexts remain bounded without semantic loss.

## ChatGPT context health

Under `chatgpt_only`, completed role/Card boundaries return through the policy router before the next substantial obligation starts.

A REQUIRED/RECOMMENDED fresh-review boundary is the preferred natural context reset when one is already due.

Otherwise, the router may conditionally load `workflow/chatgpt_only/CONTEXT_HEALTH.md` only when the accumulated chat shows a concrete material risk of stale-state carryover, authority confusion or irrelevant-history overload.

Context health:
- is evaluated only after the current obligation is durably complete;
- never interrupts an active Card/review/write/readback sequence;
- uses no fixed token, turn, Card or milestone-count threshold;
- defaults to continuing when no concrete material context risk exists;
- may return `CONTEXT_HEALTH: FRESH`, which creates a context-hygiene session handoff before the next obligation starts;
- never overrides an existing review/user/authorization/runtime/strategic/end-of-scope stop.

A hygiene handoff is session continuity only. It does not change requirements, execution policy, review state or project authority.

## Independent review

Independent means independent from the worker/session that implemented the reviewed subject.

- `chatgpt_only` — a ChatGPT chat that implemented a REQUIRED/RECOMMENDED review subject must freeze exact `review_subject`, persist `review_state: pending`, and **stop**. The user opens a fresh normal ChatGPT chat, which performs the independent review from durable Task Board state. After GREEN the review role ends and the same chat returns to the policy router for the next legal role. After RED, if remediation is bounded/deterministic/authorized, the review role ends and the router assigns execution preparation/execution to the same chat; once that chat implements the corrected reviewable subject, it freezes a new pending review and stops with the next fresh re-review prompt.
- `codex_only` — Codex Main obtains an independent reviewer worker/session. When `codex_workflow` is installed/enabled, it owns the internal execute/review-worker orchestration. Project Workflow owns only the project-level review requirement, exact subject, durable verdict/evidence and acceptance boundary. No user handoff is required solely for review independence.
- `mixed` — reviewer path follows the accepted review contract and must remain independent from implementation.

For `chatgpt_only`, a Task Card uses `REQUIRED | RECOMMENDED | none`. REQUIRED and RECOMMENDED are real independent-review gates; `none` creates no review state. An explicit later request for independent review promotes `none` to RECOMMENDED before the gate is activated.

Task Board records active review state using `review_state`, `review_subject` and `review_evidence`.

## Milestone continuity

Milestones remain stable integrated/testable checkpoints. They are **not** automatically human handoff points.

Under `chatgpt_only` or `codex_only`, the fixed executor may run an approved multi-milestone plan continuously:

`M01 → acceptance/review/checkpoint → M02 → ...`

Each boundary still performs required close/handoff, just-in-time execution prep and fresh state/contract Refresh Gate. Execution stops only for real strategic/product/architecture decisions, explicit deployment/live-write/user authorization gates, concrete runtime blockers that cannot be self-remediated, RED requiring strategic resolution, required `chatgpt_only` fresh-review handoff, or end of approved scope.

Under `mixed`, the next new execution assignment is routed again by Capability Gate.

No separate Campaign object or scheduler is required.

## Delegated JIT planning

A strong strategic plan does not need to predict every downstream implementation card before predecessor evidence exists.

The execution orchestrator may, without returning to the original planner:
- create later Task Cards only when predecessor evidence makes their scope deterministic;
- split, merge, reorder or replace **not-yet-started** implementation cards;
- complete an optional JIT milestone extension;
- refine implementation-level acceptance/tests/interfaces from actual predecessor results.

This authority is bounded. It must not change accepted requirements, frozen architecture/decisions, global invariants, milestone outcome or explicit user/deployment/authorization gates. If new evidence requires one of those to change, execution stops for strategic replan.

Do not create placeholder cards whose real scope is merely “whatever the previous card reveals.” Persist the dependency/JIT trigger instead and create the real card when the evidence exists.

## Lean executor runtime

Ordinary execution of an already-defined Task Card uses a small shared runtime path:

```text
workflow/EXECUTION.md
→ workflow/contracts/TASK_EXECUTION.md
→ executor adapter
→ current Task Card + exact authority slice + required source/runtime
```

`TASK_CARDS.md` is an authoring/decomposition contract, not a mandatory executor read. `GITHUB_STATE.md` is the extended coordinator/parallel/review/milestone/recovery state contract, not a mandatory serial-card read.

Conditional material is loaded only on trigger:
- OpenSpec when current scope references/requires it;
- Task Card authoring + Execution Prep for JIT decomposition/refinement;
- full GitHub State for bounded parallel/coordinator state, close/publication, inconsistency or recovery;
- Review and Handoff only when review/acceptance/close is reached.

Project Workflow does not teach ChatGPT or Codex a catalog of their tools/capabilities. Executors attempt concrete operations with their actual runtime; fixed-policy capability inventory/preflight is not part of normal execution.

## Task execution

Task Cards are serial by default. A prepared milestone may opt into **bounded parallel** execution when multiple READY cards have completed dependencies, explicit `parallel_safe` ownership, non-overlapping mutable `write_scope` and no shared `exclusive_resources`.

Task Board plus ordinary Git lane branches/worktrees remain the durable coordination mechanism; there is no generic DAG/scheduler service.

## Roles

Project Workflow defines **roles, not model identities**. It never requires a named model or reasoning level for planning, orchestration, execution or review. The user/runtime may choose different models, reasoning levels or sessions for the same role at different times.

- **Strategic planner** — establishes or revises project goal, requirements, accepted architecture/decisions, global invariants, milestone outcomes and explicit boundary gates.
- **Execution orchestrator / JIT planner** — turns accepted strategic authority plus current durable evidence into executable milestone detail and Task Cards, coordinates execution, and refines not-yet-started work within delegated planning authority.
- **Executor / worker** — implements bounded Task Card scope against its exact authority slice.
- **Independent reviewer** — evaluates the exact reviewed subject against the same applicable authority slice without having implemented that subject.

Roles may be performed by normal ChatGPT or Codex according to project `execution_policy` and current routing. Under `codex_only`, Codex Main commonly occupies the execution-orchestrator role; when `codex_workflow` is installed/enabled, it governs internal Codex worker/model routing and lifecycle. Project Workflow does not choose those models or duplicate those mechanics.

A strategic replan returns to the **strategic-planning role**, not necessarily to the same model/session that authored the original plan.

## Progressive disclosure

Agents follow deterministic route read sets from `workflow/CONTEXT_ROUTING.md`.

Each route separates:
- **REQUIRED** files/artifacts;
- **CONDITIONAL** files loaded only when a concrete trigger exists;
- **DO NOT READ BY DEFAULT** files that are outside the normal context set.

Normal ChatGPT starts with the intentionally small `CHATGPT.md` router, project `PROJECT.md`, and `CONTEXT_ROUTING.md`; when implementation/review/recovery state exists it reads Task Board before final route selection. It then follows one primary route rather than loading neighboring phase modules "just in case."

For a `chatgpt_only` independent-review obligation, the normal workflow modules are `workflow/chatgpt_only/REVIEW.md` + `STATE.md` with the exact reviewed subject/authority/evidence. When the verdict is persisted, the review role ends and the chat returns to `workflow/chatgpt_only/ROUTER.md`; downstream execution/close modules are loaded only if the router assigns those roles.

Codex starts from `prompts/CODEX_START.md` and its own route. Codex does **not** load `CHATGPT.md` or ChatGPT-specific execution instructions. ChatGPT reads `workflow/codex/HANDOFF.md` only for an actual Codex handoff/return/strategic escalation.

## ChatGPT human control surface

User-facing normal ChatGPT status is intentionally different from agent-to-agent execution communication.

For ChatGPT → user:
- summarize actual findings/errors in plain language;
- explain impact briefly;
- state the next action clearly;
- keep technical provenance in durable repository state instead of dumping it into chat;
- expose SHAs, blob IDs, evidence paths, raw Task Board state and detailed test telemetry only when requested or materially actionable.

This rule does **not** reduce the information available to Codex Main, workers, reviewers or other execution agents. Agent-to-agent packages continue to carry whatever authority/evidence detail the execution workflow requires.

## Fresh Chat handoff UX

Whenever Project Workflow requires or recommends that the user open a fresh normal ChatGPT chat, the current response must also provide the ready-to-copy start prompt immediately.

The prompt is intentionally thin:
- project repository;
- exact active project/implementation branch;
- exact continuation target (for example pending independent review for one card);
- smallest durable start pointer;
- instruction to recover exact state/subject/authority/evidence from the repository.

Do not duplicate SHAs, test summaries, changed-file lists or evidence prose that already exist in durable state. The user should be able to press **Copy**, open a new chat and paste once.

## Bootstrap prompts

- normal ChatGPT start: `prompts/CHATGPT_START.md`
- fresh ChatGPT session handoff: `prompts/CHATGPT_FRESH_SESSION.md`
- reusable ChatGPT Project Instructions: `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md`
- Codex execution start: `prompts/CODEX_START.md`

## Start an existing project

Use:

> Użyj mojego Project Workflow z `elmakus/chatgpt-codex-project-workflow`. Repo projektu: `elmakus/example-project`. Kontynuujemy <cel/faza>.

Current `main` is canonical Project Workflow authority except deliberately frozen in-flight migration boundaries documented by migration guidance.
