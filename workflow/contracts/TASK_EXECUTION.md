# Task Execution Runtime Contract

This is the shared runtime contract for executing an **already-defined** Task Card. ChatGPT and Codex read it on the execution route.

Task Card authoring/decomposition belongs to `workflow/contracts/TASK_CARDS.md`. Full coordinator/milestone/parallel/recovery state belongs to `workflow/contracts/GITHUB_STATE.md`.

## 1. Authority and scope

Execution uses:
- Task Board as sole mutable execution-state authority;
- current milestone contract;
- current Task Card;
- the Task Card's exact authority slice;
- accepted dependency results actually required by the card;
- exact current source/runtime state needed to implement and verify it.

A summary or coordinator paraphrase never outranks exact referenced authority. Implement only bounded card scope unless normal corrective/replan rules explicitly change it.

## 2. Readiness and start

A new card may start only when:
- Task Board marks it `ready`;
- required dependencies are `done`;
- required authoritative inputs exist;
- acceptance is testable enough to execute;
- no unresolved strategic or explicit authorization blocker exists;
- no REQUIRED/RECOMMENDED pending review blocks the work.

At start:
- transition `ready → in_progress`;
- record the assigned executor;
- record/reconcile the exact execution branch/base/workspace pointer needed for recovery;
- transition the milestone to `in_progress` when this is its first real started card.

For `bounded_parallel`, additionally load the relevant parallel/coordinator rules from `TASK_CARDS.md`, `GITHUB_STATE.md`, and the executor-specific orchestration module.

## 3. Refresh Gate

Before implementation compare only the state that can affect this card:
- exact branch/HEAD and relevant runtime/external state;
- Task Board card/milestone/execution pointers;
- milestone + Task Card contracts;
- exact requirements/accepted decisions/plan constraints in the card's authority slice;
- required dependency results;
- relevant actual interfaces/source;
- required tests/checks, evidence/readback and review obligations;
- relevant OpenSpec only when the card references or requires it.

Read a prior cumulative handoff only when it is part of predecessor truth, recovery, or the current authority slice. Do not load it mechanically for every card.

Refresh Gate is not a capability inventory.

Local implementation-detail drift inside accepted requirements/architecture may be reconciled by the executor. Evidence requiring a change to accepted requirements, frozen architecture/decisions, global invariants, milestone outcome/behavior contract, or an explicit authorization boundary is a strategic blocker.

## 4. Runtime-operation rule

Workflow does not enumerate what tools or capabilities the executor has.

Attempt the concrete required operation using the runtime actually available. Do not perform a separate fixed-policy capability inventory/preflight.

Ordinary executor-local remediation is implementation detail when permitted by the environment and accepted constraints. If a concrete required operation still cannot proceed, persist the exact blocker and request only the smallest user-provided input/access/authorization actually required.

A runtime blocker never changes `execution_policy` or executor automatically.

## 5. Execute and verify

- Preserve every implementation-shaping constraint in the exact authority slice.
- Implement only included scope; do not smuggle unrelated cleanup or architecture changes into the card.
- Run the Task Card's required tests/checks and applicable OpenSpec verification.
- For material external writes, perform meaningful readback/verification when available.
- Surface material deviations or conflicting evidence instead of silently redefining authority.

## 6. Blocked state

When the card cannot satisfy its contract:
- stop affected work safely;
- set Task Board card `execution_status: blocked`;
- persist durable blocker evidence when material;
- do not start dependent work;
- ask the user only for the smallest real decision/input/access/authorization when user action is actually required.

## 7. Definition of Done

A card may become `done` only when all applicable conditions hold:
1. included scope is complete and excluded scope was not silently expanded;
2. acceptance criteria are satisfied;
3. required tests/checks ran and are GREEN, or an authorized baseline exception exists;
4. relevant OpenSpec obligations are satisfied;
5. REQUIRED/RECOMMENDED independent review is GREEN when applicable;
6. no hidden blocker or unassigned TODO remains inside accepted scope;
7. accepted result exists in durable Git/external state;
8. material external side effects/readback obligations are verified;
9. for parallel execution, the accepted lane result is integrated and required post-integration checks are GREEN;
10. Task Board result state is reconciled.

Persist at least:
```yaml
execution_status: done
executor: chatgpt | codex
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path-or-null>
tests_summary: <concise exact summary or evidence pointer>
```

Standalone evidence is expected when required by contract or when proof is materially richer/independently useful, including required/recommended review, integrated milestone acceptance, material external write/readback, baseline exception, or complex multi-stage verification.

## 8. Review boundary

When REQUIRED/RECOMMENDED independent review becomes due:
- freeze/persist the exact review subject and implementation/test evidence;
- set `review_state: pending`;
- do not claim the reviewed subject GREEN;
- route to `workflow/REVIEW_AND_HANDOFF.md` and the executor-specific independence mechanism.

## 9. After card completion

Persist/reconcile Task Board, unblock newly eligible dependencies, and continue deterministically when current policy/state allows.

If the milestone reaches a review/acceptance/close boundary, leave this runtime route and load `workflow/REVIEW_AND_HANDOFF.md`.

If predecessor evidence triggers L2 JIT decomposition/refinement, leave ordinary card execution and load `workflow/EXECUTION_PREP.md`.
