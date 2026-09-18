# ChatGPT-only State Contract

`implementation/TASK_BOARD.yaml` is the sole authoritative mutable execution-state record.

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
- blockers.

## Review fields

When independent review is active:

```yaml
review_state: pending | in_progress | green | red
review_subject: <exact subject>
review_evidence: <repo-relative-path-or-null>
```

One review attempt refers to one immutable exact subject. Corrective work creates a new subject/review attempt.

## Incremental Card-set state

Task Board does not need speculative future Cards whose contracts are not yet knowable.

When accepted milestone/plan authority records a JIT decomposition trigger:
- currently contractible Cards may execute normally;
- after predecessor evidence satisfies the trigger, create/revise the real not-yet-started Card contracts and reconcile their Task Board entries before execution;
- absence of speculative future Cards is not an inconsistent state while the trigger is unsatisfied;
- active/in-progress Cards are not silently redefined through this mechanism.

## Legacy execution-mode reconciliation

The active ChatGPT-only route is serial: exactly one project Card may be in progress.

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

Set milestone `ready → in_progress` when its first real Card starts.

Exactly one project Card may be `in_progress` at a time in this policy path.

## Done result

Before Card becomes `done`, persist:

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

If a blocker exceeds L1/L2 authority, return to the router for strategic classification: Planning when Project Definition remains valid but plan strategy must change, Project Definition when accepted product/system authority must change, or Research when more evidence is required. A user stop exists only when that classification reaches unresolved user/product authority or another explicit real gate.

## Independent review lifecycle

For a Card/milestone contracted as REQUIRED or RECOMMENDED:
1. implementing chat freezes exact subject/evidence;
2. set `review_state: pending`;
3. persist durable state;
4. fresh independent chat sets `in_progress`;
5. reviewer persists GREEN/RED evidence;
6. set `review_state: green | red`;
7. completed reviewer role returns to the router for the next legal obligation.

For `independent_review: none`, do not create review state as routine workflow.

If independent review is later explicitly requested for `none`, persist the requirement as RECOMMENDED before creating `review_state`.

The implementing chat never issues its own REQUIRED/RECOMMENDED verdict.

## Milestone GREEN

A milestone is not done merely because all Cards are done.

After integrated milestone acceptance is GREEN:
- finalize publication/merge as required;
- write/reconcile cumulative handoff;
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
- Task Board;
- exact branch/HEAD/runtime/external state;
- current milestone/Card contracts;
- referenced OpenSpec/evidence/result/review pointers;
- handoff only when materially needed.

Previous chat narrative is not required.

## Invalid states

Examples:
- more than one Card `in_progress`;
- `done` Card missing required result/tests provenance;
- milestone `done` with non-green required review;
- dependent Card started before dependency `done`;
- review verdict attached to wrong subject;
- durable execution truth existing only in chat, `PROJECT.md`, stable Card/milestone files or local `current.md`;
- external success contradicted by required readback;
- `execution_policy` changing without an explicit user decision;
- implementing chat issuing independent verdict on its own required/recommended subject.
