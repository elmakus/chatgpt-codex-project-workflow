# ChatGPT-only Router

This router applies only after root `CHATGPT.md` confirms project `execution_policy: chatgpt_only`.

Once here, stay inside:
- `workflow/common/*` for genuinely policy-neutral rules;
- `workflow/chatgpt_only/*` for Brainstorming/Research/Definition plus planning/execution/review/state/recovery.

Do not load legacy/shared execution trees or another policy directory.

## Bootstrap

1. Read `workflow/common/AUTHORITY.md`.
2. Read project root `PROJECT.md`.
3. If implementation, implementation-review, blocker or execution-recovery state exists or is referenced, resolve the state context **before** reading mutable execution state. Read `workflow/chatgpt_only/WORKSTREAMS.md` when a branch-isolated workstream is referenced or present; select its exact manifest + Task Board only after branch/manifest validation. When no branch-isolated workstream is selected, keep the legacy/default `implementation/TASK_BOARD.yaml` fallback. In the rest of this router, `Task Board` means that exact selected canonical board.
4. A REQUIRED/RECOMMENDED implementation `review_state: pending | in_progress` outranks later implementation and routes to Independent review.
5. If Task Board `research_obligation` points to an implementation/recovery Research record, read that exact record before choosing later implementation, including when the Research obligation was opened from a RED review. `Status: active | blocked` routes to Research; `Status: complete` routes to its exact recorded Return target; `Status: consumed` means the Task Board pointer is stale and should be cleared at the next safe edit.
6. A non-terminal REQUIRED/RECOMMENDED subject with `review_state: red` outranks unrelated/later implementation. Read its exact RED evidence and apply the single canonical classification in `REVIEW.md#RED → corrective-route transition` against current durable state: bounded L1/L2 correction → Execution Prep/Execution; plan-only correction → Strategic planning; accepted-authority correction → Project Definition; missing evidence → materialize the implementation-owned Research handoff before Research; unresolved real gate → user stop. If the RED evidence/current state cannot be coherently classified, route to Recovery rather than guessing.
7. An `in_progress` Card with `review_state: green` routes to Execution for terminal Post-review Card finalization before later work.
8. If `PROJECT.md → Active research obligation` points to a pre-execution research record, read that exact record before choosing the route. `Status: active | blocked` routes to Research; `Status: complete` routes to the exact recorded Return target; `Status: consumed` means the pointer is stale and should be cleared at the next safe edit.
9. If both Task Board and PROJECT point to different active/blocked/complete Research obligations, treat that as inconsistent state and route to Recovery instead of guessing which obligation owns continuation.
10. If the current request/handoff or current planning state references a plan-review record, read that `planning/reviews/<plan-revision>.md` record before plan approval or Execution Prep. Treat the request/handoff only as a locator; the record is authority. `pending | in_progress` outranks both.
11. Select exactly one primary route below.
12. Read only that route's required project artifacts plus exact authority refs.
13. Continue deterministic work automatically until a real workflow stop is reached.

## Fresh-session entry semantics

A fresh-session handoff target is a **recovery/entry locator only**. It identifies the first obligation to recover; it does not narrow the approved project scope to one role, one verdict, one Card or one milestone.

After the located obligation completes:
- persist its durable result/state;
- return to this router;
- continue all deterministic authorized role transitions under the normal protocol below;
- stop only when durable state reaches a real workflow boundary.

Do not interpret wording such as `Kontynuuj`, `Punkt wejścia`, a review target, a Card ID or a milestone ID as an implicit instruction to reply immediately after that obligation. Only explicit user/project authority can deliberately narrow the approved scope.

## Role-transition protocol

A route module owns only its current role.

When that role finishes:
1. persist the durable state/evidence produced by the role;
2. re-evaluate the applicable durable state (plan-review record and/or Task Board) + accepted authority;
3. return to this router;
4. if durable state/current phase already owns a real stop — including a root `CHATGPT.md#Real-stop-response-contract` boundary or the `chatgpt_only` Brainstorming → Project Definition promotion gate below — handle that stop first and do not run a separate hygiene handoff;
5. only when a deterministic authorized next role exists, perform the context-health trigger check below;
6. select the next legal route;
7. load that route's module(s);
8. continue in the same chat without a user-facing stop when context health remains CONTINUE.

The same chat may therefore move across deterministic role transitions when no real boundary intervenes, for example:

```text
PROJECT DEFINITION → PLANNING → EXECUTION_PREP → EXECUTION
PLAN_REVIEW → PLANNING → EXECUTION_PREP → EXECUTION
REVIEW → EXECUTION_PREP → EXECUTION → CLOSE → EXECUTION_PREP → EXECUTION
```

The first line begins only after Project Definition has been legally entered. For a new exploratory `chatgpt_only` scope, Brainstorming/Research cannot enter Project Definition until the user-owned promotion gate below is satisfied. Once Definition is entered, `Definition Complete = GREEN → Planning` remains deterministic. When Planning creates a REQUIRED/RECOMMENDED independent plan-review gate, the authoring chat stops before entering `PLAN_REVIEW`. The `PLAN_REVIEW → PLANNING → ...` line begins in the fresh reviewer chat after that reviewer has completed its verdict and the router assigns the next legal role.

Role identity is per obligation, not permanent for the whole chat.

A reviewer that has completed its verdict is no longer governed by `REVIEW.md` once the router assigns a new route. If the same chat later implements a new reviewable subject, it is the implementing chat for that new subject and cannot independently review it.

Only a real boundary from root `CHATGPT.md#Real-stop-response-contract` or an explicit policy-specific boundary defined by this router ends the turn.

## Brainstorming → Project Definition promotion gate

Under `chatgpt_only`, the first transition from exploratory Brainstorming into Project Definition for a definition scope is **user-owned**.

Brainstorming may reach `ready_for_definition`, but that state is only a recommendation that formalization is now possible. It is not permission to start Definition.

The active exploratory scope is discovered from project `PROJECT.md → Active exploratory scope`. That pointer identifies the exact brainstorming record used for recovery. The record carries a stable `Scope ID`, `Revision`, and `Definition promotion subject`.

Before entering Project Definition from an exploratory Brainstorming/Research path, require one of:
- an explicit current user instruction to promote the current scope into Project Definition; or
- durable `Definition promotion authorization: user_authorized` in the PROJECT-pointed brainstorming record, with `Definition promotion subject` exactly matching that record's current `<scope-id>@<revision>`.

A durable `user_authorized` value without an exact matching promotion subject is stale/insufficient and must not authorize Definition.

Examples of sufficient user intent include “przejdź do Definition”, “formalizuj wymagania/decyzje”, or another unambiguous instruction to leave exploration and begin Project Definition. Mere agreement with an individual idea, answering a brainstorming question, or asking for more research is not phase-promotion authority.

When Brainstorming is ready but promotion is not authorized:
1. persist the useful brainstorming state;
2. ensure `PROJECT.md → Active exploratory scope` points to that exact record;
3. set `Status: ready_for_definition`, `Definition promotion authorization: pending`, and `Definition promotion subject: none`;
4. do **not** enter Project Definition or Planning;
5. treat this as a policy-specific real user stop;
6. use `workflow/common/USER_STOP.md` and ask only whether to continue brainstorming/research or promote the current scope into Project Definition.

When the user explicitly authorizes promotion:
1. ensure the current exploratory record and its PROJECT pointer are persisted;
2. persist `Definition promotion authorization: user_authorized` plus `Definition promotion subject: <scope-id>@<revision>` before entering Definition;
3. route to Project Definition;
4. continue normally from there.

If substantive exploratory scope changes after authorization but before Definition begins, increment/change the brainstorming revision and reset authorization to `pending` with promotion subject `none`. Never carry authorization across a materially changed revision.

Research completion does not bypass this gate. If Research was entered from an unpromoted exploratory scope, return to Brainstorming/promotion handling rather than entering Definition automatically.

The authorization applies only to the exact promoted scope/revision. Once Definition has begun, keep the active exploratory pointer/record available so bounded Research ↔ Definition recovery for that same promoted subject does not require repeated authorization. If Definition deliberately returns to open-ended Brainstorming because the product/problem space has materially reopened, create a new brainstorming revision (or a new scope when appropriate) and reset authorization to `pending` with promotion subject `none`.

When Definition Complete becomes GREEN, the exploratory promotion obligation is complete. Clear `PROJECT.md → Active exploratory scope` when it no longer represents an active exploratory/Definition recovery pointer, then continue to Planning.

This gate does **not** apply to `Definition Complete = GREEN → Planning`; that transition remains deterministic and automatic when planning is in scope.

## Context-health trigger check

Do not load context-health machinery after every role by default.

Before starting the next substantial obligation at a safe durable boundary, ask whether the accumulated chat may now materially increase the risk of stale-state carryover, authority confusion or omission.

If there is no concrete signal, continue without loading another module.

If there is a concrete signal — for example materially superseded state in the transcript, major role/authority-area transition, large irrelevant diagnostic/tool history, or uncertainty reconstructing current truth from the conversation — read:

`workflow/chatgpt_only/CONTEXT_HEALTH.md`

Then obey its decision:
- `CONTEXT_HEALTH: CONTINUE` → select/load the next route now;
- `CONTEXT_HEALTH: FRESH` → do not start the next obligation; perform the context-hygiene user stop.

Never run a separate context-health handoff when another real stop already owns the boundary. A pending REQUIRED/RECOMMENDED fresh independent review is one such case and already provides the context reset.

## Research return ownership and crash recovery

For any `complete` Research record, the exact current `Return target` owns continuation and the owning pointer remains until durable consumption.

- `execution_resolution:<subject>` is the only intermediate classifier. Ordinarily it refines the exact final Return target while keeping `Status: complete`, `Return reconciliation: pending`, and the Task Board pointer. If classification itself requires more evidence, it instead uses the explicit classifier-to-Research chain transition in `RESEARCH.md`.
- Every final target — Brainstorming, Project Definition, Strategic Planning, Execution Prep or Execution — MUST follow `workflow/chatgpt_only/RESEARCH.md#Final Return-target protocol`.
- Final target mutation and `Return reconciliation: applied` + exact result refs are persisted in the same durable Git transition.
- If a crash occurs after that transition but before `consumed`/pointer-clear, re-entry is consume/clear-only; target work must not be replayed.
- Normally only the final owning Return target consumes/clears. The sole exception is classifier-to-Research chaining, where `execution_resolution` atomically records `R1` reconciliation as the exact new `R2` obligation, consumes `R1`, creates `R2 active`, and switches the Task Board pointer in the same durable Git transition.

Research never selects a different route by itself; only the authorized classifier may refine a Return target.

## Routes

### Brainstorming

Read:
- `workflow/chatgpt_only/BRAINSTORMING.md`;
- the exact record referenced by `PROJECT.md → Active exploratory scope` when that pointer exists;
- the exact `complete` research record referenced by `PROJECT.md → Active research obligation` when its Return target is this Brainstorming subject;
- otherwise the current brainstorming material needed to establish/create that pointer;
- only accepted constraints already relevant.

### Research

Read:
- `workflow/chatgpt_only/RESEARCH.md`;
- the exact record referenced by `PROJECT.md → Active research obligation` for pre-execution Research when that pointer exists;
- otherwise the exact Task Board `research_obligation` pointer when Research was triggered from active execution/recovery;
- the exact research question/material;
- only relevant accepted requirements/decisions/source state.

The durable research record owns its `Status`, Origin subject and Return target. Do not infer the return role from chat history.

### Project Definition

Read:
- `workflow/chatgpt_only/DEFINITION.md`;
- current user/product goal and explicit accepted choices;
- the exact `PROJECT.md → Active exploratory scope` record when Definition was entered through the promotion gate and the pointer is still active;
- the exact `complete` research record referenced by `PROJECT.md → Active research obligation` when its Return target is this Project Definition subject;
- the exact `complete` record referenced by Task Board `research_obligation` when its final Return target is this Project Definition subject;
- relevant brainstorming conclusions;
- relevant verified research/evidence;
- existing requirements/decisions when redefining accepted authority;
- only current source/external baseline needed to constrain the definition.

Do not load Planning or execution modules merely to define product/system intent.


### Repository / project initialization

Read:
- `workflow/chatgpt_only/REPOSITORY.md`;
- `workflow/common/AUTHORITY.md`;
- existing `PROJECT.md` when present;
- only project artifacts needed for topology/layout/state-ownership/legacy-migration or detailed Git/branch questions.

Use this route for:
- new project initialization;
- repository topology/layout;
- split-repository questions;
- detailed branch policy;
- state-ownership ambiguity;
- legacy repository/state migration.

### Strategic planning

Read:
- `workflow/chatgpt_only/PLANNING.md`;
- approved canonical requirements;
- accepted decisions;
- the exact `complete` research record referenced by `PROJECT.md → Active research obligation` when its Return target is this Strategic Planning subject;
- the exact `complete` record referenced by Task Board `research_obligation` when its final Return target is this Strategic Planning subject;
- only verified research/baseline that the accepted definition or plan actually references;
- current approved plan when replanning.

Planning assumes Project Definition is complete. If requirements/strategic decisions are missing or contradictory, return to Project Definition instead of silently deciding them.

Read Task Board/current handoff only when planning/replanning an active project. Do not load execution files merely to organize strategy.

### Independent plan review

Read:
- `workflow/chatgpt_only/PLAN_REVIEW.md`;
- exact `planning/reviews/<plan-revision>.md` record;
- exact immutable Master Plan review subject;
- approved canonical requirements;
- accepted decisions;
- relevant Definition authority;
- only research/baseline/source evidence materially referenced by the plan.

Read Task Board/current handoff only when reviewing a replan whose correctness materially depends on active execution state.

Do not load the planning-session narrative as review evidence.

### Execution preparation / JIT refinement

Read:
- `workflow/chatgpt_only/EXECUTION_PREP.md`;
- `workflow/chatgpt_only/WORKSTREAMS.md` when the current execution context is branch-isolated;
- `workflow/chatgpt_only/TASK_CARDS.md`;
- current milestone/plan authority;
- Task Board when implementation state exists;
- exact predecessor evidence needed by current decomposition;
- the exact `complete` record referenced by Task Board `research_obligation` when its final Return target is this Execution Prep subject.

Read `workflow/common/OPENSPEC.md` only when current preparation marks/reconciles an OpenSpec-relevant contract.

### Execution

Read:
- `workflow/chatgpt_only/EXECUTION.md`;
- `workflow/chatgpt_only/STATE.md`;
- `workflow/chatgpt_only/WORKSTREAMS.md` when the current execution context is branch-isolated;
- Task Board;
- current milestone/Card;
- exact authority slice;
- only source/runtime/evidence needed for that card;
- the exact `complete` record referenced by Task Board `research_obligation` when its final Return target is this Execution subject.

Read `workflow/common/OPENSPEC.md` only when the current card references/requires it.

### Independent review

Read:
- `workflow/chatgpt_only/REVIEW.md`;
- `workflow/chatgpt_only/STATE.md`;
- `workflow/chatgpt_only/WORKSTREAMS.md` when the reviewed subject belongs to a branch-isolated workstream;
- Task Board;
- exact active branch;
- exact review subject;
- reviewed Card/milestone contract;
- the same authority slice that governed implementation;
- required review evidence;
- actual subject/source/runtime needed to judge it.

Do not load implementing-session narrative as review evidence.

### Milestone close / publication

Read:
- `workflow/chatgpt_only/CLOSE.md`;
- `workflow/chatgpt_only/STATE.md`;
- Task Board;
- milestone contract;
- required card/review evidence;
- intended final branch/state.

### Strategic blocker

Read only:
- exact blocker/evidence;
- current Card/milestone contract;
- smallest requirements/decision/research/source slice needed to classify it.

If this route is the exact `execution_resolution:<subject>` Return target of a completed implementation/recovery Research record:
1. verify that Task Board `research_obligation` still points to that record and that its Origin/Return subjects match the affected durable Card/blocker state;
2. classify the findings against current durable authority;
3. if classification identifies an exact final owning role/subject, persist that classification by replacing the record's Return target with that final owner while keeping `Status: complete`, `Return reconciliation: pending`, and keeping Task Board `research_obligation`;
4. for that ordinary final-owner case, return through this router; the pointer now deterministically routes to the final target and the classifier does **not** mark the record `consumed`;
5. if classification instead proves that more evidence is needed before any final owner can be named, do not invent or persist a final Return target; use the classifier-to-Research chain transition in `RESEARCH.md`.

Then:
- bounded L1/L2 correction inside accepted authority → refine Return target to Execution Prep or Execution;
- if accepted product/system intent or a strategic decision must change → refine Return target to Project Definition;
- if accepted definition remains valid but milestone sequencing/plan must change → refine Return target to Strategic planning;
- if more evidence is still needed before either can be decided → in one durable Git transition persist `R1 Return reconciliation: applied` with exact `R2` ref, set `R1 Status: consumed`, create `R2 Status: active`, and switch Task Board `research_obligation` directly from `R1` to `R2`; then route to Research. Never expose `R1 complete` after moving the pointer and never expose a null-pointer gap.

Do not continue affected work until the owning authority is resolved.

### Recovery

Read:
- `workflow/chatgpt_only/RECOVERY.md`;
- Task Board;
- exact active branch/HEAD/runtime;
- affected in-progress/blocked/review state;
- referenced contracts/evidence.

After recovery, route to the recovered obligation above.

## Human-facing behavior

Use the global normal-ChatGPT control-surface rules from root `CHATGPT.md`.

Do not end a turn merely to announce deterministic work that this route already authorizes. Continue first; respond at a real review/user/authorization/runtime/strategic/end-of-scope boundary.
