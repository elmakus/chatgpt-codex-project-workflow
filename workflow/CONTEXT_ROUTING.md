# Context Routing

## Purpose

Progressive disclosure means: **read only the smallest context required for the current obligation, without losing applicable authority**.

Normal ChatGPT reaches this file after `CHATGPT.md` and project `PROJECT.md`. Codex reaches it from `prompts/CODEX_START.md`.

If implementation/review/blocker/recovery state exists or is referenced, read project `implementation/TASK_BOARD.yaml` before final route selection.

## Minimal authority precedence

For ordinary routing, use this compact order without loading the full Project Repository Contract:

1. workflow behavior → current workflow `main`;
2. accepted intent → requirements + accepted decisions;
3. approved execution intent → Master Plan milestone + valid JIT extension;
4. live execution truth → Task Board + exact Git/runtime/external evidence;
5. bounded contract → Task Card + relevant OpenSpec;
6. completed checkpoint summary → cumulative handoff + referenced exact state;
7. research = evidence, not decision;
8. brainstorming = tentative.

`PROJECT.md` points to authority; it does not override referenced authority.

Read `workflow/contracts/PROJECT_REPOSITORY.md` only for a real authority conflict, repository topology/layout issue, legacy-state migration, state-ownership ambiguity or detailed branch/topology-policy question.

## Global priority

A REQUIRED/RECOMMENDED `review_state: pending | in_progress` outranks later dependent implementation.

- `chatgpt_only` → fresh ChatGPT reviewer uses **INDEPENDENT REVIEW** below.
- `codex_only` → Codex Main handles reviewer independence inside its Codex execution route.

## Route dispatch

### BRAINSTORMING
Read `workflow/BRAINSTORMING.md`, current brainstorming material and only accepted decisions/requirements that already constrain it. Do not load execution/OpenSpec/Codex material unless the question actually depends on it.

### RESEARCH
Read `workflow/RESEARCH.md`, the research question/material and only relevant requirements/decisions/source state. Do not load execution contracts by default.

### PLANNING
Read `workflow/PLANNING.md`, requirements, accepted decisions, relevant verified research and current plan. Read Task Board/latest handoff only when replanning an active project. Read Task Card/OpenSpec material only when planning reaches near-term execution decomposition.

### EXECUTION PREPARATION
Read `workflow/EXECUTION_PREP.md`, current plan/milestone authority, Task Board when present, predecessor handoff/evidence when relevant and current source/runtime needed for realistic preparation. Load `TASK_CARDS`, `OPENSPEC` and `GITHUB_STATE` contracts only when their specific semantics are being created/reconciled. Capability Gate is `mixed`-only.

### CHATGPT EXECUTION
Read `workflow/EXECUTION.md`, `workflow/contracts/TASK_EXECUTION.md`, `workflow/chatgpt/EXECUTION.md`, Task Board, current milestone/Card contracts, exact authority slices and required current source/runtime.

Load conditionally:
- `OPENSPEC.md` only when the current card references/requires OpenSpec;
- `TASK_CARDS.md` only for JIT card creation/revision or parallel metadata semantics;
- `GITHUB_STATE.md` only for bounded-parallel/coordinator state, state inconsistency, milestone close/publication or recovery;
- `EXECUTION_PREP.md` only for allowed L2 JIT refinement;
- `REVIEW_AND_HANDOFF.md` only when review/acceptance/close is actually reached.

Do not load `workflow/codex/*`.

### CODEX EXECUTION
Read `workflow/EXECUTION.md`, `workflow/contracts/TASK_EXECUTION.md`, `workflow/codex/EXECUTION.md`, `workflow/codex/CODEX_ORCHESTRATION.md`, Task Board, current contracts/authority slices and required source/runtime.

Load conditionally:
- `GITHUB_STATE.md` for bounded-parallel/coordinator state, state inconsistency, milestone close/publication or recovery;
- `TASK_CARDS.md` for JIT card creation/revision or project-level parallel metadata;
- `OPENSPEC.md` only when current scope references/requires it;
- `EXECUTION_PREP.md` only for allowed JIT refinement/next-milestone prep;
- `REVIEW_AND_HANDOFF.md` only at project review/acceptance/close boundaries.

Do not load `CHATGPT.md` or `workflow/chatgpt/*`.

### MILESTONE CLOSE / PUBLICATION
Read `workflow/REVIEW_AND_HANDOFF.md`, Task Board, milestone contract, required card/review evidence and intended final branch/state. Load `GITHUB_STATE` when closing/reconciling state; load repository/OpenSpec contracts only when their specific semantics are material.

### STRATEGIC BLOCKER
Read the exact blocker/evidence, current contract and smallest requirement/decision/research/source slice needed to decide it. Read `workflow/codex/HANDOFF.md` only for an actual correlated Codex escalation.

### FAILURE RECOVERY
Read Task Board, exact active branch/HEAD/runtime, affected in-progress/blocked contracts, pending review gates and referenced evidence. Then load the route module matching the recovered obligation. Do not load unrelated history or the wrong executor adapter.

---

## INDEPENDENT REVIEW — deterministic read set

Use this for one pending/in-progress REQUIRED/RECOMMENDED review subject. This is **review-only**, not execution.

### REQUIRED

Workflow:
- `workflow/REVIEW_AND_HANDOFF.md`.

Project/Git:
- `PROJECT.md`;
- Task Board;
- exact active branch;
- exact `review_subject`;
- reviewed Task Card or milestone contract;
- the **same authority slice** that governed implementation;
- required evidence referenced for the review;
- actual reviewed diff/source/runtime needed to judge the subject.

### CONDITIONAL — load only on trigger

- `workflow/contracts/TASK_EXECUTION.md` — verdict depends on generic runtime/DoD semantics not already explicit in the reviewed card/review module.
- `workflow/contracts/GITHUB_STATE.md` — task includes closure/state-consistency questions beyond review-state transitions already defined in `REVIEW_AND_HANDOFF.md`.
- `workflow/contracts/OPENSPEC.md` — reviewed authority slice points to OpenSpec or verdict depends on its contract.
- `workflow/contracts/PROJECT_REPOSITORY.md` — authority conflict, topology/layout, legacy state or detailed branch-policy question.
- prior handoff/dependency result/research/external readback — only when the reviewed authority/acceptance actually references it.

### DO NOT READ BY DEFAULT

- `workflow/PLANNING.md`;
- `workflow/EXECUTION_PREP.md`;
- `workflow/EXECUTION.md`;
- `workflow/chatgpt/EXECUTION.md`;
- `workflow/chatgpt/CAPABILITY_GATE.md`;
- all `workflow/codex/*`;
- `prompts/CODEX_START.md`;
- unrelated milestones/cards/OpenSpec/research/history;
- previous implementing-chat narrative as review evidence.

Under `chatgpt_only`, the reviewer must be a fresh normal ChatGPT chat that did not implement the exact subject.

The reviewer writes only review verdict/evidence and required review-state transitions. RED corrective implementation leaves this route and returns through the normal preparation/execution path.
