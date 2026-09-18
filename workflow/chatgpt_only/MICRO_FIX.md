# ChatGPT-only Micro-fix Contract

This module defines the bounded issue path selected by Intake when `path: micro_fix`.

A micro-fix skips a full Master Plan/milestone decomposition. It does **not** skip durable scope, execution state, verification, evidence or independent review.

## Entry requirements

Micro-fix is legal only for a branch-isolated issue workstream whose completed Intake record proves every accepted R6 criterion:

- root cause and intended behavior are concrete;
- the change is bounded and low strategic risk;
- no accepted requirement, architecture or product decision must change;
- acceptance can be stated directly;
- no substantial migration/deployment strategy is needed.

The Intake record must identify the exact workstream/branch, baseline evidence, selected base/integration target, `path: micro_fix`, the qualification evidence, and `next_route: execution_prep:micro_fix`.

If any criterion is false or materially uncertain, do not materialize a micro-fix. Return through the router to the smallest normal Research / Project Definition / Strategic Planning / Execution Prep path justified by durable evidence.

## Durable materialization

Execution Prep owns micro-fix materialization.

Use the selected workstream manifest and create/reconcile:

1. one bounded stable fix contract, normally `implementation/workstreams/<id>/cards/MF-T01.md`;
2. the manifest-selected workstream Task Board from `workflow/chatgpt_only/WORKSTREAM_TASK_BOARD_TEMPLATE.yaml`;
3. manifest `task_board` plus workstream authority/review metadata needed for recovery.

The Task Board uses:

```yaml
plan_revision: "micro-fix"
current_milestone: "micro-fix"
milestones: {}
```

and exactly one initially prepared Card:

```yaml
id: "MF-T01"
milestone: "micro-fix"
decision_state: accepted
execution_status: ready
executor: null
```

The `micro-fix` value is a direct-fix state discriminator, not a synthetic approved Master Plan milestone. Do not create a Master Plan or milestone contract merely to satisfy normal-path shape.

If a project already has an exact non-placeholder fix Card identity in the Intake record, preserve that stable identity instead of renaming it to `MF-T01`.

## Fix-contract minimum

The bounded fix contract uses the normal Task Card contract shape, except its Master Plan/milestone authority entry is explicitly:

`none — qualified micro-fix under requirements R6 and the exact completed Intake record`.

It must bind:

- exact Intake record and diagnostic/root-cause evidence;
- applicable accepted requirements/decisions;
- exact base/branch/workstream identity;
- included and excluded scope;
- measurable acceptance;
- regression tests/checks;
- material external write/readback needs;
- independent-review requirement;
- any implementation-shaping compatibility/failure constraints.

A behavioral/code/runtime-configuration micro-fix has at least `RECOMMENDED` independent review. Existing high-risk rules may raise it to `REQUIRED`.

## Execution semantics

After materialization, normal selected-workstream `EXECUTION.md`, `STATE.md`, `REVIEW.md`, `RESEARCH.md` and `RECOVERY.md` semantics apply.

Micro-fix differences are only:

- there is no approved Master Plan/milestone contract to read;
- `current_milestone: micro-fix` has no entry in `milestones`;
- the one bounded fix Card is the execution/acceptance contract;
- milestone lifecycle/start/close mutations are skipped;
- Card result/evidence/review state remains canonical only in the selected Task Board.

Implementation-owned Research still uses only that selected Task Board's `research_obligation`.

## Workstream final-integration review

For behavioral/code/runtime-configuration issue work, the selected workstream manifest must carry at least:

```yaml
review:
  requirement: RECOMMENDED
  state: null
  subject: null
  evidence: null
  covered_by: null
```

`REQUIRED` replaces `RECOMMENDED` when existing risk authority demands it.

This manifest review is a distinct **workstream final-integration gate**, not a mirror of Card review state.

For a one-Card micro-fix, an independent GREEN Card review may satisfy the workstream final-integration gate without a second reviewer only when all are proven:

1. the Card is the entire behavioral workstream change;
2. the workstream integrated/final subject is exactly the immutable subject reviewed GREEN;
3. no behavioral/config/code change occurred after that subject;
4. the Card review used the same applicable authority/acceptance needed for the whole workstream.

When all four hold **after `WORKSTREAMS.md#Integration refresh contract` has run against the current target**, the owning Close/finalization role may reconcile the manifest gate as:

```yaml
state: green
subject: <same exact immutable subject>
evidence: <same independent review evidence>
covered_by: "task_board:MF-T01"
```

This is coverage reuse of an already independent verdict, not a new self-review. Execution must not perform this reuse before target refresh. If exact coverage cannot be proven after refresh, freeze the workstream final subject as `pending`, set `covered_by: null`, and require a fresh independent workstream review before integration.

After the bounded fix Card is terminal, return through the router to `CLOSE.md` for target refresh, final-integration review coverage/freeze, and integration. Do not invent a milestone merely to enter Close.

## Recovery

A fresh chat targeting the same micro-fix branch recovers:

- current workflow `main`;
- project `PROJECT.md`;
- exact branch;
- validated workstream manifest;
- completed Intake record;
- manifest-selected Task Board;
- exact fix Card;
- exact result/review/Research evidence pointers.

It resumes the one existing obligation. It never creates a second micro-fix lane or consults an unrelated workstream Task Board to infer state.

## Boundary with later milestones

This module establishes the durable final-integration review gate but does not implement M04 worktree isolation, stacked integration or target-refresh/rebase/retarget mechanics, and does not implement M05 final UX/migration/E2E closure.
