# ChatGPT-only Router

This router applies only after root `CHATGPT.md` confirms project `execution_policy: chatgpt_only`.

Once here, stay inside:
- `workflow/common/*` for genuinely policy-neutral rules;
- `workflow/chatgpt_only/*` for planning/execution/review/state/recovery.

Do not load legacy/shared execution trees or another policy directory.

## Bootstrap

1. Read `workflow/common/AUTHORITY.md`.
2. Read project root `PROJECT.md`.
3. If implementation/review/blocker/recovery state exists or is referenced, read `implementation/TASK_BOARD.yaml` before choosing the route.
4. A REQUIRED/RECOMMENDED implementation `review_state: pending | in_progress` outranks later implementation.
5. A referenced current plan-review record in `pending | in_progress` outranks plan approval and Execution Prep.
6. Select exactly one primary route below.
7. Read only that route's required project artifacts plus exact authority refs.
8. Continue deterministic work automatically until a real workflow stop is reached.

## Role-transition protocol

A route module owns only its current role.

When that role finishes:
1. persist the durable state/evidence produced by the role;
2. re-evaluate Task Board + accepted authority;
3. return to this router;
4. if durable state already owns a real stop from root `CHATGPT.md#Real-stop-response-contract` — fresh-review handoff, unresolved strategic/product decision requiring user authority, explicit authorization, concrete runtime/access/input blocker, or end of approved scope — handle that stop first and do not run a separate hygiene handoff;
5. only when a deterministic authorized next role exists, perform the context-health trigger check below;
6. select the next legal route;
7. load that route's module(s);
8. continue in the same chat without a user-facing stop when context health remains CONTINUE.

The same chat may therefore move, for example:

```text
RESEARCH → PROJECT DEFINITION → PLANNING → PLAN_REVIEW → PLANNING → EXECUTION_PREP → EXECUTION
REVIEW → EXECUTION_PREP → EXECUTION → CLOSE → EXECUTION_PREP → EXECUTION
```

Role identity is per obligation, not permanent for the whole chat.

A reviewer that has completed its verdict is no longer governed by `REVIEW.md` once the router assigns a new route. If the same chat later implements a new reviewable subject, it is the implementing chat for that new subject and cannot independently review it.

Only a real boundary from root `CHATGPT.md#Real-stop-response-contract` ends the turn.

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

## Routes

### Brainstorming

Read:
- `workflow/common/BRAINSTORMING.md`;
- current brainstorming material;
- only accepted constraints already relevant.

### Research

Read:
- `workflow/common/RESEARCH.md`;
- the exact research question/material;
- only relevant accepted requirements/decisions/source state.

### Project Definition

Read:
- `workflow/common/DEFINITION.md`;
- current user/product goal and explicit accepted choices;
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
- `workflow/chatgpt_only/TASK_CARDS.md`;
- current milestone/plan authority;
- Task Board when implementation state exists;
- exact predecessor evidence needed by current decomposition.

Read `workflow/common/OPENSPEC.md` only when current preparation marks/reconciles an OpenSpec-relevant contract.

### Execution

Read:
- `workflow/chatgpt_only/EXECUTION.md`;
- `workflow/chatgpt_only/STATE.md`;
- Task Board;
- current milestone/Card;
- exact authority slice;
- only source/runtime/evidence needed for that card.

Read `workflow/common/OPENSPEC.md` only when the current card references/requires it.

### Independent review

Read:
- `workflow/chatgpt_only/REVIEW.md`;
- `workflow/chatgpt_only/STATE.md`;
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

Then:
- if accepted product/system intent or a strategic decision must change, route to Project Definition;
- if accepted definition remains valid but milestone sequencing/plan must change, route to Strategic planning;
- if more evidence is needed before either can be decided, route to Research.

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
