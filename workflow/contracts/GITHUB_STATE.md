# GitHub State Contract

This is the normative contract for durable execution state in a project repository, independent of whether the active executor is ChatGPT or Codex.

## 1. Card execution states

Allowed card `execution_status` values:

```text
planned
ready
in_progress
blocked
done
superseded
```

Decision state is separate and, when used, has:

```text
accepted
deferred
rejected
review
```

Do not infer execution completion from decision acceptance.

## 2. Milestone execution lifecycle

Normal milestone lifecycle:

```text
planned → ready → in_progress → done
```

`blocked` is allowed for an unresolved milestone gate/blocker. `superseded` requires an explicit decision.

A milestone that passed integrated GREEN acceptance on its implementation branch is not yet terminal `done` until required/recommended review policy, milestone PR merge and post-merge reconciliation are complete.

## 3. Task Board

`implementation/TASK_BOARD.yaml` is the live index of execution state, not the complete implementation narrative.

It should identify at least:
- project;
- plan revision/reference;
- current milestone;
- milestone states and checkpoint fields;
- card states, dependencies and active executor when applicable;
- result pointers;
- relevant OpenSpec change;
- branch/PR information needed to recover in-flight work;
- strategic control-chat identity only when that optional Codex communication mechanism is configured.

During active milestone execution, `execution_ref.branch` identifies the one primary milestone implementation branch. `execution_ref.pr` remains null until the final milestone PR is opened.

## 4. Starting a card

Before any normal production implementation starts, the current milestone must have one primary implementation branch created from the exact latest GREEN `main` checkpoint.

When card execution begins:
- Task Board card `ready → in_progress`;
- card file `Execution status: IN_PROGRESS`;
- record `executor: chatgpt | codex` in card and Task Board;
- milestone `ready → in_progress` when this is its first real started card;
- ensure `execution_ref.branch` points to the primary milestone implementation branch and HEAD is on that branch, not `main`;
- persist a Refresh Gate note/evidence only when the gate discovers something material.

The durable transition should be committed/pushed on the milestone implementation branch before relying on it for recovery.

## 5. Done-card result pointer contract

Before a card is terminal `done`, both Task Board and card Result section must record:

```yaml
execution_status: done
executor: chatgpt | codex
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path>
```

The card also records a concise `tests_summary`.

Rules:
- `result_commit` identifies the commit containing or verifiably representing the accepted card result on the primary milestone implementation branch.
- individual Task Cards do not require separate PRs; `result_pr` may remain `null` until the milestone PR exists, then may point to that shared milestone PR when useful.
- `evidence` points to durable test/review evidence or an unambiguous cumulative evidence section.
- evidence names exact tests/review/checks; `tests passed` alone is insufficient.
- when material external writes require readback under `workflow/EXECUTION.md`, evidence records the target, readback method and verified resulting state.

## 6. Definition of Done state coupling

A card can be `done` only after the Task Card Definition of Done has passed. At minimum:
- scope is complete;
- acceptance criteria are satisfied;
- required tests/checks ran;
- tests/checks are green or a baseline exception was explicitly accepted;
- relevant OpenSpec requirements are satisfied;
- no hidden blocker remains;
- result exists in durable repository state;
- Task Board is updated;
- result pointers/evidence are durable;
- relevant side effects/readback/idempotency/reconciliation are verified;
- no unassigned TODO remains inside accepted scope.

Card `done` does not authorize merging the milestone to `main`; integrated milestone acceptance/review/PR policy still applies.

## 7. Blocked card

When execution is blocked:
- card `execution_status: blocked`;
- write durable evidence under `implementation/blockers/` when material;
- make a safe commit/push on the milestone branch before messaging when possible;
- do not start dependent cards.

Capability routing and runtime capability failure are different stages:

- **Before assignment**, normal ChatGPT may use `workflow/chatgpt/CAPABILITY_GATE.md` to choose ChatGPT, Codex, or BLOCKED according to project `execution_policy`.
- **After assignment/execution start**, a newly discovered missing capability is a runtime blocker, not an automatic executor-routing event.

For a runtime capability blocker, record the exact missing MCP/access/credential/runtime/tool/test/readback/evidence capability, surface `USER ACTION REQUIRED`, and resume the **same card with the same executor** after the user provides it.

If the assigned executor is Codex, do not re-apply the ChatGPT Capability Gate and do not fall back to ChatGPT. Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`; therefore a required capability absent from Codex is not available from ChatGPT as an executor fallback.

Under `chatgpt_only`, a ChatGPT runtime capability failure likewise remains blocked until the user provides the missing capability or explicitly changes project policy; policy never changes automatically.

For a strategic/product/architecture blocker, obtain the relevant authority decision and persist an accepted decision record under `decisions/`. When Codex uses a correlated ChatGPT control-chat exchange, follow `workflow/codex/HANDOFF.md` including matching `request_id` and `DECISION FOR CODEX:`.

Resume only after the blocker is actually resolved and Task Card/OpenSpec/plan/Task Board are reconciled as required.

## 8. Milestone GREEN and merge

A milestone is not done merely because all cards are done or because integrated branch acceptance is GREEN.

Required finalization sequence:
1. all required cards are `done` on the one primary milestone implementation branch;
2. run integrated milestone acceptance on the intended final branch HEAD;
3. if RED, keep/reopen corrective work on that same branch and do not merge to `main`;
4. if GREEN, complete REQUIRED independent review and any RECOMMENDED review unless explicitly waived by the user/authority;
5. open one milestone PR from the primary implementation branch to `main`;
6. merge only the accepted GREEN state;
7. reconcile `project-handoffs/MXX_HANDOFF.md`, Task Board and milestone metadata against the actual resulting `main` state;
8. record `implementation_head` as the exact implementation-bearing `main` commit produced by merging the accepted final milestone PR;
9. record `checkpoint` as the actual accepted final `main` checkpoint after any metadata-only reconciliation (commit SHA or immutable tag according to policy);
10. write/reconcile acceptance evidence under `implementation/evidence/`;
11. set milestone `execution_status: done` only after merge and reconciliation are complete.

A metadata-only closure commit directly on `main` is allowed only when necessary to record the actual post-merge checkpoint/handoff/result metadata that could not be known before merge. It must not change production behavior or implementation scope. If such a closure commit is required, `implementation_head` remains the merge-produced implementation-bearing `main` commit and the resulting `main` HEAD becomes `checkpoint`. If no closure commit is required, both may identify the same `main` commit.

A done milestone stores at minimum:

```yaml
execution_status: done
checkpoint: <final-main-checkpoint-sha-or-tag>
implementation_head: <merged-main-implementation-sha>
handoff: project-handoffs/MXX_HANDOFF.md
acceptance_evidence: implementation/evidence/MXX_ACCEPTANCE.md
```

## 9. Corrective work

If integrated milestone acceptance or independent review is RED:
- do not mark the milestone done;
- do not merge the milestone to `main`;
- reopen the appropriate card or create a bounded corrective card on the same primary milestone implementation branch;
- record failing evidence;
- preserve dependencies, capability gates and strategic escalation rules;
- rerun relevant acceptance/review before opening or merging the milestone PR.

Corrective production work before merge never moves to a separate primary PR/branch merely because it is corrective.

## 10. Cumulative handoff and recovery

`project-handoffs/MXX_HANDOFF.md` is the canonical cumulative handoff for the completed milestone.

Fresh-session recovery also uses:
- exact Git branch/HEAD;
- Task Board;
- current milestone/card;
- recorded executor for in-flight work;
- relevant OpenSpec;
- evidence/result pointers.

For an in-progress milestone, recovery returns to its one primary implementation branch. For a completed milestone, recovery starts from its recorded GREEN `main` checkpoint.

A local `current.md` is optional convenience only and cannot be required for recovery.

## 11. Repository topology changes

Do not change project repository ownership/layout in the middle of an active milestone. Legacy split-repository migration occurs only at a green milestone boundary and follows `PROJECT_REPOSITORY.md`.

## 12. Consistency invariants

Invalid states include:
- normal production Task Card implementation committed directly to `main`;
- more than one primary implementation branch or final production PR for the same milestone, excluding explicit experimental Path A/Path B branches;
- a milestone branch not based on the previous accepted GREEN `main` checkpoint without an explicit reconciled reason;
- a RED milestone merged to `main`;
- milestone `done` before its final milestone PR is merged and post-merge reconciliation is complete;
- card `done` with missing required result pointers or executor provenance;
- milestone `done` with missing checkpoint, `implementation_head`, handoff or acceptance evidence;
- `implementation_head` that does not identify the implementation-bearing merged `main` commit for the milestone;
- a milestone checkpoint that does not identify the actual accepted final `main` state at milestone close;
- all required cards `done` while a green milestone remains `ready`;
- a dependent card `in_progress` while a required dependency is `blocked`;
- durable state existing only in chat or local `current.md`;
- Task Board/card disagreement left unreconciled at a durable checkpoint;
- claimed external success when required readback/verification evidence shows a different persisted state;
- a Codex runtime capability blocker being rerouted to ChatGPT instead of remaining blocked for user-provided capability.
