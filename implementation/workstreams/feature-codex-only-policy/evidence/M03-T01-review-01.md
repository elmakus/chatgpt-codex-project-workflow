# M03-T01 Independent Review 01

Card: `M03-T01`
Exact review subject: `b03225ac0b92a87a938f9cd79c70ee1715eecd33`
Verdict: **RED**

## Authority reviewed

- `implementation/workstreams/feature-codex-only-policy/cards/M03-T01.md`
- `requirements/CODEX_ONLY_POLICY.md` — CO-REQ-017..025
- `planning/CODEX_ONLY_MASTER_PLAN.md#M03--bounded-parallel-task-cards-and-jit-safety`
- `decisions/ADR_CODEX_ONLY_BOUNDED_PARALLEL_CARDS.md`
- `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
- `openspec/changes/codex-only-m03-bounded-parallel-safety/`
- exact implementation diff `43c234e59e6db081a0b3dbf7efd9ae16948e0553..b03225ac0b92a87a938f9cd79c70ee1715eecd33`

## Finding

### RED-01 — pre-launch stale-batch dissolution can create invalid Card state

`EXECUTION_PREP.md` freezes a batch by setting every member Card to `execution_status: in_progress` before runtime launch. Its immediate pre-launch refresh can then decide that the base/safety proof is stale and route to Recovery for batch dissolution/serial fallback.

`RECOVERY.md#Prepared` says to record/reconcile the stale prepared outcome, clear it from `current_batch`, and form a new batch or execute serially. No contract specifies the required reconciliation of the member Cards that were already changed to `in_progress`.

That omission conflicts with `STATE.md`, which permits multiple `in_progress` Cards only when all are covered by one valid current parallel batch. Clearing `current_batch` while those Cards remain `in_progress` creates an explicitly inconsistent state and makes deterministic serial fallback impossible without an unspecified repair.

This is reachable whenever the safety proof changes after freeze but before launch (for example, workspace isolation becomes unavailable or the frozen base is invalidated). It therefore fails the Card acceptance requirement that pre-launch safety failure deterministically falls back without losing valid project state, and weakens CO-REQ-019/020/022/024 recovery semantics.

## Independent verification

- exact subject/base relationship verified: subject is 18 commits ahead of implementation base;
- exact implementation file set matches the M03 bounded-parallel scope;
- `git diff --check` is clean;
- root `workflow/CONTEXT_ROUTING.md` and `workflow/chatgpt_only/` match current workflow `main`;
- root project policy remains `execution_policy: chatgpt_only`;
- no corrective transition for stale prepared member Card `execution_status` was found across M03 State/Execution Prep/Execution/Recovery/Router/OpenSpec/audit contracts.

## Required correction

Define one deterministic pre-launch dissolution transition that:
1. records the abandoned/stale prepared batch outcome durably without reusing the batch ID;
2. clears `current_batch` only after every still-unlaunched member Card is reconciled from batch-owned `in_progress` back to its legal READY/serial state;
3. preserves any Main-owned bookkeeping/evidence needed for recovery;
4. keeps launched batches immutable and does not reuse this unwind path after any member has entered runtime-active state;
5. updates State, Execution Prep, Recovery, Router, OpenSpec and scenario audit/templates only where needed so the transition is explicit and recoverable.
