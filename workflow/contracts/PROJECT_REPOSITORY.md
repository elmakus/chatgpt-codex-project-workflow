# Project Repository Contract

## 1. One project = one repository

Every project receives its own repository from the first substantive work. Do not create parallel planning/workspace/execution-control repositories without concrete technical justification and explicit user approval.

## 2. Workflow versus project repository

`elmakus/chatgpt-codex-project-workflow` contains workflow rules only. The project repository contains project knowledge, durable execution state and source/code when applicable.

## 3. Canonical project layout

```text
<project-repo>/
├── PROJECT.md
├── brainstorming/
├── decisions/
├── research/
├── requirements/
├── planning/
├── implementation/
│   ├── TASK_BOARD.yaml
│   ├── milestones/
│   ├── cards/
│   ├── evidence/
│   └── blockers/
├── project-handoffs/
├── openspec/
└── <source/code>
```

Adapt paths when a real repository requires it, but keep knowledge states unambiguous.

## 4. PROJECT.md

`PROJECT.md` is a small router/authority index, not history. At minimum identify project/repository, phase, goal/status, canonical requirements/plan/milestone/Task Board/handoff/OpenSpec/decisions/questions/blockers, workflow repo/ref and:

```yaml
execution_policy: chatgpt_only | mixed
```

### Policy semantics

- `chatgpt_only`: work may execute only in normal ChatGPT chat. Missing ChatGPT capability is a blocker. Do not route to Codex or mutate policy automatically.
- `mixed`: ChatGPT is project router and may execute itself or hand bounded Task Cards to Codex through the Capability Gate.

ChatGPT Work is outside the Project Workflow operating model.

Legacy projects missing `execution_policy` must establish it before new execution; absence is not a third policy mode.

## 5. Authority and conflicts

Apply authority by domain:

1. workflow behavior → current workflow `main`;
2. accepted product/system intent → requirements + accepted decisions;
3. approved execution intent → Master Plan/milestone;
4. current execution state → Task Board/Card/OpenSpec/exact Git/runtime evidence;
5. completed milestone truth → cumulative handoff plus referenced exact state;
6. research → evidence, not decision;
7. brainstorming → tentative.

`PROJECT.md` points to authority; it does not override the artifact it references.

## 6. Durable state and recovery

Chat memory and local convenience checkpoints are not durable authority. Recovery must work from repository state, Task Board/cards/evidence/OpenSpec/handoff and exact Git/runtime pointers.

## 7. Git and branch policy

Use coherent commits per Task Card/logical slice. Large milestones normally use isolated branch/PR when that matches project practice. Card completion can precede shared milestone PR merge if result/evidence pointers are durable. Integrated milestone acceptance runs on intended final state.

Never force-push `main` as a normal workflow action.

### Competing research/prototype paths

When evidence requires independent alternatives, branches such as Path A and Path B may start from the same stable checkpoint, produce isolated findings/prototypes, then feed an A/B/Hybrid decision. Do not merge experimental code merely because it exists; production implementation starts only after the accepted comparison decision. This pattern is optional and introduces no new lifecycle status.

## 8. In-flight execution

For active work, exact branch/HEAD and external/runtime evidence named by the card are authoritative for in-flight state. Record the active executor on the card/Task Board for recovery provenance.

## 9. External effects

Material external writes must satisfy the execution contract's readback/verification rule when meaningful readback exists. Durable evidence should identify the target and verified resulting state.

## 10. Initialization

Initialize only phase-appropriate artifacts. Do not create fake Task Cards/OpenSpec merely to satisfy a directory checklist.
