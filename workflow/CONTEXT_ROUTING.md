# Context Routing

## Purpose

Progressive disclosure reduces what an agent reads for a task while preserving the complete applicable workflow contract.

**Agent reads less at a given stage. Workflow contains no fewer rules.**

Each route defines:

- **REQUIRED** — read before acting on that route;
- **CONDITIONAL** — read only when the stated trigger exists;
- **DO NOT READ BY DEFAULT** — explicitly outside the normal context set for that route.

A conditional item becoming relevant is not a failure of progressive disclosure. Loading it without its trigger is.

## Entrypoints

### Normal ChatGPT

1. `CHATGPT.md`;
2. project root `PROJECT.md`;
3. this file;
4. when implementation/review/blocker/recovery state exists or is referenced, project `implementation/TASK_BOARD.yaml`;
5. one primary route below;
6. only that route's REQUIRED items plus triggered CONDITIONAL items.

### Codex

1. `prompts/CODEX_START.md`;
2. project root `PROJECT.md`;
3. this file;
4. project Task Board when implementation state exists;
5. shared execution modules/contracts required by assigned/continuing scope;
6. only the required `workflow/codex/*` runtime boundary modules.

Codex does **not** automatically read `CHATGPT.md` or `workflow/chatgpt/*`.

ChatGPT may read `workflow/codex/HANDOFF.md` only for a real Codex handoff/return/strategic escalation.

## Minimal authority precedence

Use this compact precedence without loading `workflow/contracts/PROJECT_REPOSITORY.md` merely to route ordinary work:

1. workflow behavior → current workflow `main` unless an explicitly frozen in-flight boundary applies;
2. accepted product/system intent → canonical requirements + accepted decisions;
3. approved execution intent → approved Master Plan milestone contract + any valid JIT extension;
4. current mutable execution truth → Task Board + exact Git/runtime/external evidence;
5. bounded work/acceptance → Task Card + relevant OpenSpec;
6. completed milestone summary → cumulative handoff + referenced exact state;
7. research is evidence, not an accepted decision;
8. brainstorming is tentative until promoted.

`PROJECT.md` points to authority; it does not override the referenced authority.

### Load the full Project Repository Contract only when needed

Read `workflow/contracts/PROJECT_REPOSITORY.md` only when the task materially involves:
- authority conflict/precedence ambiguity not resolved by the compact rules above;
- repository topology/split-repository decisions;
- canonical layout/state-ownership ambiguity;
- legacy-state migration;
- branch/topology policy requiring the detailed repository contract.

## Global priority: pending independent review

If Task Board has `review_state: pending | in_progress` for a REQUIRED/RECOMMENDED gate, route to **INDEPENDENT REVIEW** before later dependent implementation.

Under `chatgpt_only`, a fresh reviewer chat treats that exact pending subject as its first obligation.

Under `codex_only`, Codex Main handles reviewer independence through its own execution route/runtime orchestration.

---

## BRAINSTORMING

### REQUIRED
Workflow:
- `workflow/BRAINSTORMING.md`

Project:
- `PROJECT.md`;
- current brainstorming note/question;
- accepted decisions already known to constrain the discussion.

### CONDITIONAL
- canonical requirements — only if the brainstorming question must remain inside already-frozen requirements;
- research — only if the current idea explicitly depends on prior verified findings.

### DO NOT READ BY DEFAULT
- Task Board;
- Task Cards;
- OpenSpec;
- GitHub State contract;
- execution/review modules;
- `workflow/codex/*`.

---

## RESEARCH

### REQUIRED
Workflow:
- `workflow/RESEARCH.md`

Project:
- `PROJECT.md`;
- current research question/material;
- directly relevant accepted decisions/requirements.

### CONDITIONAL
- current source/runtime state — when the research question depends on actual implementation;
- prior research — only the referenced/relevant slice.

### DO NOT READ BY DEFAULT
- Task Cards;
- OpenSpec execution changes;
- execution/review modules;
- `workflow/codex/*`.

---

## PLANNING

### REQUIRED
Workflow:
- `workflow/PLANNING.md`

Project:
- `PROJECT.md`;
- canonical requirements;
- accepted decisions;
- current approved/draft plan;
- only verified research needed by the plan.

### CONDITIONAL
- current source/runtime — when baseline or feasibility depends on it;
- Task Board/latest handoff — when replanning an already-running project;
- Task Card/OpenSpec contracts — only when planning reaches near-term execution decomposition.

Do not create speculative future cards when a JIT decomposition trigger is more truthful.

### DO NOT READ BY DEFAULT
- `workflow/EXECUTION.md`;
- `workflow/chatgpt/EXECUTION.md`;
- `workflow/codex/*`;
- unrelated implementation evidence/history.

---

## EXECUTION PREPARATION

### REQUIRED
Workflow:
- `workflow/EXECUTION_PREP.md`

Project:
- `PROJECT.md`;
- approved Master Plan/current milestone contract;
- canonical requirement/decision slice for the milestone;
- Task Board when it exists;
- latest handoff when it is the predecessor checkpoint.

### CONDITIONAL
Workflow:
- `workflow/contracts/TASK_CARDS.md` — when creating/revising Task Card contracts;
- `workflow/contracts/OPENSPEC.md` — only for an actual OpenSpec candidate/required change;
- `workflow/contracts/GITHUB_STATE.md` — when initializing/reconciling mutable execution state or branch/lane state;
- `workflow/chatgpt/CAPABILITY_GATE.md` — only for a new assignment under `mixed`.

Project:
- current source/runtime — only the surfaces needed to prepare realistic near-term contracts;
- predecessor evidence — when a JIT trigger depends on it.

### DO NOT READ BY DEFAULT
- `workflow/codex/*` unless the output is an actual Codex handoff;
- unrelated historical milestones/cards/evidence;
- Capability Gate under `chatgpt_only` or `codex_only`.

---

## CHATGPT EXECUTION

### REQUIRED
Workflow:
- `workflow/EXECUTION.md`;
- `workflow/chatgpt/EXECUTION.md`.

Project:
- `PROJECT.md`;
- Task Board;
- current milestone contract;
- current Task Card(s);
- each current card's exact authority slice;
- exact current source/runtime surfaces needed by those cards.

### CONDITIONAL
Workflow:
- `workflow/contracts/TASK_CARDS.md` — when generic Card/DoD/Refresh semantics are not already sufficient from the current card + execution module;
- `workflow/contracts/OPENSPEC.md` — when the current card has/needs OpenSpec;
- `workflow/contracts/GITHUB_STATE.md` — when mutating/reconciling execution-state structure, lane/integration state, or resolving state inconsistency;
- `workflow/EXECUTION_PREP.md` — only for allowed L2 JIT decomposition/refinement;
- `workflow/REVIEW_AND_HANDOFF.md` — when a review/close boundary is actually reached.

Project:
- latest handoff — when needed to recover predecessor truth;
- evidence/dependency results — only when referenced by the card/authority slice.

### DO NOT READ BY DEFAULT
- `workflow/codex/*`;
- `prompts/CODEX_START.md`;
- unrelated cards/milestones/OpenSpec/research/history;
- Capability Gate under fixed `chatgpt_only`.

---

## CODEX EXECUTION

### REQUIRED
Workflow:
- `workflow/EXECUTION.md`;
- `workflow/codex/EXECUTION.md`;
- `workflow/codex/CODEX_ORCHESTRATION.md`.

Project:
- `PROJECT.md`;
- Task Board;
- current milestone contract;
- current Task Card(s);
- exact authority slices;
- exact current source/runtime needed by assigned scope.

### CONDITIONAL
- `workflow/EXECUTION_PREP.md` — for allowed L2 JIT refinement / deterministic next-milestone prep;
- shared contracts only when their specific semantics are needed;
- latest handoff / OpenSpec / evidence only when referenced by current scope.

### DO NOT READ BY DEFAULT
- `CHATGPT.md`;
- `workflow/chatgpt/*`;
- unrelated project-history trees.

---

## INDEPENDENT REVIEW

Use this route for a pending/in-progress REQUIRED/RECOMMENDED review of one exact card/milestone subject. This route is **review-only**, not an execution route.

### REQUIRED
Workflow:
- `workflow/REVIEW_AND_HANDOFF.md`.

Project:
- `PROJECT.md`;
- Task Board;
- exact active branch from durable state / fresh-chat locator;
- exact `review_subject`;
- reviewed Task Card or milestone contract;
- the **same exact authority slice** that governed the implementation;
- required implementation/test evidence referenced for the review;
- the actual reviewed diff/source/runtime state needed to judge the subject.

### CONDITIONAL
Workflow:
- `workflow/contracts/TASK_CARDS.md` — only when the verdict depends on generic Task Card/DoD semantics not explicit in the reviewed contract/review module;
- `workflow/contracts/GITHUB_STATE.md` — only when the task includes closure/state-consistency verification beyond the review-state transitions already defined in `REVIEW_AND_HANDOFF.md`;
- `workflow/contracts/OPENSPEC.md` — only when the reviewed card's authority slice points to OpenSpec or the verdict depends on an OpenSpec contract;
- `workflow/contracts/PROJECT_REPOSITORY.md` — only for the conflict/topology/legacy/branch-policy triggers listed above;
- `workflow/RESEARCH.md` — only if the authority slice explicitly makes a research result part of the review basis.

Project:
- prior cumulative handoff — only if referenced by the authority slice or needed to establish predecessor truth;
- dependency results — only if the reviewed contract depends on them;
- external readback — only when the reviewed acceptance includes external state.

### DO NOT READ BY DEFAULT
- `workflow/PLANNING.md`;
- `workflow/EXECUTION_PREP.md`;
- `workflow/EXECUTION.md`;
- `workflow/chatgpt/EXECUTION.md`;
- `workflow/chatgpt/CAPABILITY_GATE.md`;
- all `workflow/codex/*`;
- `prompts/CODEX_START.md`;
- unrelated milestones/cards/OpenSpec/research/history;
- the previous implementing chat transcript as review evidence.

Under `chatgpt_only`, the reviewer must be a fresh normal ChatGPT chat that did not implement the exact subject.

A reviewer may write only review evidence/verdict and required review-state transitions. RED corrective implementation routes back through execution preparation/execution; the reviewer does not silently become the implementer inside the review route.

---

## MILESTONE CLOSE / PUBLICATION

Use this after required card/review gates are complete and the task is closure, integrated acceptance, publication/PR verification or checkpoint reconciliation.

### REQUIRED
Workflow:
- `workflow/REVIEW_AND_HANDOFF.md`;
- `workflow/contracts/GITHUB_STATE.md`.

Project:
- `PROJECT.md`;
- Task Board;
- current milestone contract;
- required card result pointers;
- required review evidence;
- intended final branch/state;
- cumulative handoff target.

### CONDITIONAL
- `workflow/contracts/TASK_CARDS.md` — when a card DoD inconsistency must be resolved;
- `workflow/contracts/PROJECT_REPOSITORY.md` — when detailed branch/publication/topology policy is material;
- relevant OpenSpec/external readback — only if milestone acceptance depends on it.

### DO NOT READ BY DEFAULT
- planning/research history not referenced by acceptance;
- unrelated milestone/card trees;
- `workflow/codex/*` for normal ChatGPT close.

---

## STRATEGIC BLOCKER

### REQUIRED
Workflow:
- owning strategic/planning module needed to decide the blocker.

Project:
- `PROJECT.md`;
- Task Board when implementation exists;
- exact blocker/evidence;
- current milestone/Card contract;
- exact authority needed for the decision.

### CONDITIONAL
- `workflow/codex/HANDOFF.md` — only for actual correlated Codex strategic escalation;
- research/source/runtime — only as needed to resolve the blocker.

### DO NOT READ BY DEFAULT
- unrelated execution trees;
- unrelated Codex modules.

---

## FAILURE RECOVERY

### REQUIRED
Workflow:
- route module matching the recovered obligation after state is reconstructed.

Project:
- `PROJECT.md`;
- exact active branch/HEAD/runtime state;
- Task Board;
- every `in_progress`/`blocked` card contract;
- every pending/in-progress review gate;
- recorded executor/lane pointers;
- exact referenced evidence/results needed to recover.

### CONDITIONAL
- latest handoff — when needed to establish predecessor checkpoint;
- OpenSpec/tests — only for affected work;
- `workflow/contracts/GITHUB_STATE.md` — when Task Board/state consistency itself is damaged or ambiguous;
- local `current.md` — convenience hint only.

### DO NOT READ BY DEFAULT
- unrelated completed history;
- unrelated phase modules;
- executor-specific modules for an executor that is not the recorded/selected one.

Recovery must succeed from durable state without prior chat.
