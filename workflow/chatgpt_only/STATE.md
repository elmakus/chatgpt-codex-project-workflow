# ChatGPT-only State Contract

The **selected canonical Task Board** is the sole authoritative mutable Card/milestone execution-state record for the current ChatGPT-only state context.

Resolve that context through `workflow/chatgpt_only/WORKSTREAMS.md` before using this contract:
- branch-isolated workstream → the exact Task Board named by its validated manifest;
- otherwise → legacy/default `implementation/TASK_BOARD.yaml`.

Do not combine Cards from multiple workstream Task Boards into one synthetic execution state.

For a branch-isolated selected board, `workstream_id` and `execution_ref.branch` are binding identity fields. Before any mutable state in that board is trusted, they must exactly match the validated manifest `id` and `branch` under `workflow/chatgpt_only/WORKSTREAMS.md`. A mismatch is invalid state, not a reason to fall back to the legacy/default board.

## Card states

Allowed `execution_status`:

```text
planned
ready
in_progress
blocked
done
superseded
```

Optional decision state is separate:

```text
accepted
deferred
rejected
review
```

Do not infer implementation completion from decision acceptance.

## Milestone lifecycle

Normal lifecycle:

```text
planned → ready → in_progress → done
```

`blocked` is allowed for a real unresolved milestone gate. `superseded` requires an explicit decision.

A GREEN accepted milestone must not remain `ready` or `in_progress`.

### Qualified micro-fix state

A qualified branch-isolated micro-fix is a deliberate no-Master-Plan/no-milestone exception defined by `workflow/chatgpt_only/MICRO_FIX.md`.

Its selected Task Board uses:
- `plan_revision: micro-fix`;
- `current_milestone: micro-fix`;
- `milestones: {}`;
- one bounded fix Card as the direct execution/acceptance contract.

Do not synthesize a milestone entry merely to reuse milestone lifecycle transitions. Card/review/Research state remains otherwise normal and canonical in this selected Task Board.

## Minimum Task Board state

Track as applicable:
- project/plan revision/reference;
- current milestone;
- milestone decision/execution state;
- milestone checkpoint/final result pointers;
- Card state/dependencies;
- `executor: chatgpt` for active/completed execution provenance;
- current integration branch/HEAD information needed for recovery;
- Card result pointers + exact concise tests summary;
- standalone evidence pointer when required;
- relevant OpenSpec pointer;
- active review state;
- implementation/recovery Research pointer when active;
- blockers.

## Review fields

When independent review is active:

```yaml
review_state: pending | in_progress | green | red
review_subject: <exact subject>
review_evidence: <repo-relative-path-or-null>
```

One review attempt refers to one immutable exact subject. Corrective work creates a new subject/review attempt.

## Implementation-owned Research pointer

For Research triggered from implementation/recovery, Task Board carries only one routing pointer:

```yaml
research_obligation: research/<record>.md | null
```

The pointed Research record owns its `Status`, Origin role/subject, Return target, question, `Return reconciliation` state and exact reconciliation-result refs. Do not duplicate those lifecycle fields into Task Board and do not mirror this execution obligation into `PROJECT.md`.

Before Execution Prep / execution / recovery yields to Research, persist both the exact research record and this pointer. Keep the pointer through Research `complete`. Normally clear it only after the final Return target has durably persisted `Return reconciliation: applied`, then marked the record `consumed`. The sole exception is classifier-to-Research chaining: `execution_resolution` may consume completed `R1` only by atomically recording the exact new `R2` obligation as its reconciliation result, creating `R2 active`, and replacing this pointer from `R1` to `R2` in the same durable Git transition. Recovery from ordinary `applied + complete` is consume/clear-only.

## Incremental Card-set state

Task Board does not need speculative future Cards whose contracts are not yet knowable.

When accepted milestone/plan authority records a JIT decomposition trigger:
- currently contractible Cards may execute normally;
- after predecessor evidence satisfies the trigger, create/revise the real not-yet-started Card contracts and reconcile their Task Board entries before execution;
- absence of speculative future Cards is not an inconsistent state while the trigger is unsatisfied;
- active/in-progress Cards are not silently redefined through this mechanism.

## Legacy execution-mode reconciliation

The active ChatGPT-only route is serial **per selected Task Board**: exactly one Card may be in progress in that workstream/default board. Another independent workstream may have its own one in-progress Card without making this board invalid.

If a legacy ChatGPT-only Task Board still contains old concurrent-card metadata:
- do not invent or start new concurrent lanes;
- if no conflicting Cards are active, treat obsolete concurrency metadata as non-operative and clean it up at the next safe state edit;
- if multiple old Cards are genuinely active, recover each exact durable result/state first, then serialize/reconcile them before starting new work;
- never discard lane/result/evidence history merely to fit the new serial model.

## Starting a Card

Before implementation:
- Card must be `ready`;
- dependencies must be `done`;
- no blocking review/strategic/authorization condition may exist.

Persist:
- `ready → in_progress`;
- `executor: chatgpt`;
- exact execution branch/base pointer needed for recovery.

Set milestone `ready → in_progress` when its first real Card starts. In qualified micro-fix mode there is no milestone entry, so skip this milestone mutation.

Exactly one Card may be `in_progress` at a time in the selected Task Board.

## Done result

A Card with REQUIRED/RECOMMENDED independent review remains non-terminal until the exact current subject has `review_state: green`.

Before Card becomes `done`, verify all applicable Definition of Done conditions, including GREEN required/recommended review, then persist:

```yaml
execution_status: done
executor: chatgpt
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path-or-null>
tests_summary: <concise exact summary or evidence pointer>
```

Standalone evidence may be null for simple reproducible work.

Do not edit stable Task Card contract merely to mirror completion state.

## Blocked state

When a concrete required operation or accepted contract cannot proceed:
- set Card `blocked`;
- persist durable blocker evidence when material;
- stop dependent work;
- request only the smallest real user input/access/authorization if user action is actually required.

A runtime blocker does not silently redefine accepted requirements or execution authority.

If a blocker exceeds L1/L2 authority, return to the router for strategic classification: Planning when Project Definition remains valid but plan strategy must change, Project Definition when accepted product/system authority must change, or Research when more evidence is required. Before yielding to implementation-triggered Research, persist the exact Research record + Task Board `research_obligation` using `EXECUTION.md#Implementation → Research handoff`. A user stop exists only when that classification reaches unresolved user/product authority or another explicit real gate.

## Independent review lifecycle

For a Card/milestone contracted as REQUIRED or RECOMMENDED:
1. implementing chat persists implementation/result evidence while the Card remains non-terminal;
2. implementing chat freezes exact subject/evidence;
3. set `review_state: pending`;
4. persist durable state;
5. fresh independent chat sets `in_progress`;
6. reviewer persists GREEN/RED evidence;
7. set `review_state: green | red`;
8. completed reviewer role returns to the router for the next legal obligation;
9. for a Card-completion review, GREEN routes to Execution for deterministic terminal finalization; the reviewer verdict itself does not mark the Card `done`;
10. RED keeps the reviewed Card non-terminal until corrected/replaced within legal authority and a new subject is reviewed when still required/recommended.

For `independent_review: none`, do not create review state as routine workflow.

If independent review is later explicitly requested for `none`, persist the requirement as RECOMMENDED before creating `review_state`.

The implementing chat never issues its own REQUIRED/RECOMMENDED verdict.

## Workstream final-integration review state

For a branch-isolated intake-created workstream, the distinct final-integration review lifecycle is owned by the selected `WORKSTREAM.yaml` manifest, not by this Task Board.

- Card/milestone `review_state/review_subject/review_evidence` remain unchanged and Task-Board-owned.
- Manifest `review.requirement/state/subject/evidence/covered_by` must not mirror an active Task Board review attempt.
- Behavioral issue/feature workstreams require at least RECOMMENDED final-integration review unless exact coverage by a stronger already-independent review is proven under `WORKSTREAMS.md` / `MICRO_FIX.md`.
- RED workstream review correction uses this same selected Task Board for corrective execution/Research; it must not create or select another mutable board.
- A non-green REQUIRED/RECOMMENDED manifest review blocks workstream integration even if all Task Board Cards are terminal.

## Milestone GREEN

A milestone is not done merely because all Cards are done.

After integrated milestone acceptance is GREEN:
- finalize publication/merge as required;
- write/reconcile cumulative handoff at the canonical location for the selected state context from `CLOSE.md`;
- persist acceptance evidence;
- record exact final implementation head/checkpoint;
- set milestone `done`;
- ensure all required Cards are done;
- ensure all required/recommended review gates for accepted subject are green.

## Corrective work

If review/acceptance is RED:
- milestone stays not-done;
- reopen/create bounded corrective work;
- record failing evidence;
- preserve dependencies and strategic boundaries;
- changed subject receives a new independent review when still required/recommended.

When a fresh reviewer produces RED and corrective work is bounded, deterministic, authorized and unblocked, the reviewer role ends and the same chat returns to the router. The router assigns execution preparation/execution for the correction. After that chat implements the corrected reviewable subject, it freezes the new exact subject as `pending` and stops before self-review.

For qualified micro-fix there is no milestone GREEN transition. After its Card is terminal, return through the router to Close. Close runs current-target integration refresh first, then reconciles or freezes the selected manifest's final-integration review gate under `WORKSTREAMS.md` / `MICRO_FIX.md`, and only then may integrate or record the workstream `done`. Do not synthesize a milestone.

## Next milestone

After GREEN, advance automatically into next already-approved milestone when:
- dependencies are satisfied;
- required/recommended reviews are green;
- preparation can be derived from durable authority;
- no explicit user/deployment/live-write gate is due;
- no unresolved strategic decision exists.

Use fresh JIT preparation + Refresh Gate.

## Recovery state

Fresh-session recovery uses:
- `PROJECT.md`;
- exact workstream branch + validated manifest when branch-isolated;
- the selected canonical Task Board;
- exact branch/HEAD/runtime/external state;
- current milestone/Card contracts;
- referenced OpenSpec/evidence/result/review pointers;
- Task Board `research_obligation` + exact pointed Research record when present;
- handoff only when materially needed.

Previous chat narrative is not required.

## Invalid states

Examples:
- more than one Card `in_progress` in the same selected Task Board;
- branch-isolated Task Board `workstream_id` or `execution_ref.branch` does not exactly match its selected manifest, or required branch-isolated implementation/review/recovery state has a null/missing Task Board;
- `done` Card missing required result/tests provenance;
- `done` Card with a REQUIRED/RECOMMENDED review still `pending | in_progress | red`;
- milestone `done` with non-green required review;
- branch-isolated behavioral issue/feature final integration attempted while manifest `review.requirement` is REQUIRED/RECOMMENDED and its distinct final-integration gate is not GREEN;
- manifest workstream review fields used as a mirror of Card/milestone Task Board review lifecycle;
- dependent Card started before dependency `done`;
- review verdict attached to wrong subject;
- non-terminal REQUIRED/RECOMMENDED `review_state: red` bypassed in favor of later implementation;
- implementation/recovery Research active or complete across a role/session boundary without an exact Task Board `research_obligation` pointer;
- durable execution truth existing only in chat, `PROJECT.md`, stable Card/milestone files or local `current.md`;
- external success contradicted by required readback;
- `execution_policy` changing without an explicit user decision;
- implementing chat issuing independent verdict on its own required/recommended subject.
