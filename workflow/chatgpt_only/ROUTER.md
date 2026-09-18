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
4. A REQUIRED/RECOMMENDED `review_state: pending | in_progress` outranks later implementation.
5. Select exactly one primary route below.
6. Read only that route's required project artifacts plus exact authority refs.
7. Continue deterministic work automatically until a real workflow stop is reached.

## Role-transition protocol

A route module owns only its current role.

When that role finishes:
1. persist the durable state/evidence produced by the role;
2. re-evaluate Task Board + accepted authority;
3. return to this router;
4. select the next legal route;
5. load that route's module(s);
6. continue in the same chat without a user-facing stop when the transition is deterministic and authorized.

The same chat may therefore move, for example:

```text
REVIEW → EXECUTION_PREP → EXECUTION → CLOSE → EXECUTION_PREP → EXECUTION
```

Role identity is per obligation, not permanent for the whole chat.

A reviewer that has completed its verdict is no longer governed by `REVIEW.md` once the router assigns a new route. If the same chat later implements a new reviewable subject, it is the implementing chat for that new subject and cannot independently review it.

Only a real boundary from root `CHATGPT.md#Real-stop-response-contract` ends the turn.

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
- canonical requirements;
- accepted decisions;
- relevant verified research;
- current approved plan when replanning.

Read Task Board/current handoff only when planning an active project. Do not load execution files merely to plan strategy.

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
- smallest requirements/decision/research/source slice needed to decide it.

Do not continue affected work until authority is resolved.

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
