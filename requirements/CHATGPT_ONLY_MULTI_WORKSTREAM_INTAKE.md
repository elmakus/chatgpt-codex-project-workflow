# ChatGPT-only Multi-Workstream + Intake Requirements

Status: approved
Date: 2026-09-18
Scope ID: chatgpt-only-multi-workstream-intake
Execution policy affected: chatgpt_only

## Goal

Allow normal ChatGPT to work on multiple independent project changes at the same time without weakening the existing serial execution invariant inside any one change.

The primary operator experience is:

- `#issue <problem>` starts diagnosis/repair intake for a new issue workstream;
- `#feature <goal>` starts discovery/definition intake for a new feature workstream;
- an already-running workstream on another branch must not globally block an independent workstream;
- every workstream remains independently recoverable from durable repository state and exact Git refs;
- independent-review boundaries remain real and fresh-session review independence is preserved.

## Required behavior

### R1 — seriality is workstream-local

The invariant "exactly one project Card may be in_progress" MUST be scoped to one workstream Task Board, not the whole repository.

Two independent workstreams MAY each have one in-progress Card concurrently when they:
- use different exact workstream branches;
- use distinct mutable workstream state;
- do not claim the same active workstream identity;
- satisfy their own dependencies/gates.

Parallel Cards inside one workstream remain forbidden under chatgpt_only.

### R2 — durable workstream identity

Every branch-isolated workstream MUST have a durable manifest that identifies at minimum:
- stable workstream ID;
- kind: issue | feature | maintenance;
- status;
- exact branch;
- base ref / integration target;
- optional parent workstream for stacked work;
- canonical workstream Task Board pointer when implementation state exists;
- authority/definition/plan pointers as applicable;
- PR/result pointers as applicable.

Workstream mutable execution state MUST NOT be stored in another workstream's Task Board.

### R3 — backward-compatible single-workstream mode

Existing chatgpt_only projects using `implementation/TASK_BOARD.yaml` MUST remain valid without immediate migration.

A project MUST NOT require repository-wide state migration merely to consume the new workflow.

When no branch-isolated workstream manifest is selected, current single-workstream recovery remains authoritative.

### R4 — issue intake

An explicit `#issue` directive MUST route to issue intake before normal execution selection.

Issue intake MUST:
1. recover repo, current main/default integration target, active relevant branches/PRs and existing workstream state;
2. reproduce or otherwise establish the problem when practical before implementation;
3. determine the correct base:
   - main/default integration target for independent fixes;
   - an active parent workstream branch only when the fix genuinely depends on unmerged parent state;
4. classify overlap/dependency with active workstreams;
5. create a distinct fix workstream branch and durable workstream state before implementation mutation;
6. choose the smallest legal workflow path:
   - micro-fix path for bounded, well-understood changes;
   - normal Research/Definition/Planning/Execution path when uncertainty/scope requires it;
7. preserve review and integration gates.

Issue intake MUST NOT mutate an unrelated active workstream merely because that workstream exposed the symptom.

### R5 — feature intake

An explicit `#feature` directive MUST route to feature intake for a new branch-isolated workstream.

Feature intake MUST begin with Brainstorming/Research as needed and MUST preserve the existing user-owned Brainstorming → Project Definition promotion gate.

The `#feature` marker alone starts the workstream/discovery; it MUST NOT silently count as authorization to promote an unresolved exploratory scope into Project Definition.

Once Definition is explicitly authorized and GREEN, normal Planning → plan review → Execution Prep → Execution semantics apply.

### R6 — micro-fix path

A small issue MAY skip a full Master Plan/milestone decomposition when all are true:
- root cause and intended behavior are concrete;
- change is bounded and low strategic risk;
- no accepted requirement/architecture/product decision needs change;
- acceptance can be stated directly;
- no substantial migration/deployment strategy is needed.

A micro-fix still MUST have durable scope/acceptance, implementation evidence, exact subject freeze, and an independent review before integration when it changes code, runtime configuration or user-visible/system behavior.

### R7 — review policy

For `#issue` / `#feature` workstreams that change code, runtime configuration, external behavior or system behavior, final integration review is at least RECOMMENDED and is a real fresh independent-review gate.

REQUIRED still applies for existing high-risk categories.

`none` is allowed only when current review authority permits it and the workstream is genuinely non-behavioral/trivial; convenience or concurrent workload is not a reason to skip review.

A reviewer of one workstream MUST judge the exact frozen subject of that workstream and MUST NOT infer correctness from another workstream's review.

### R8 — local worktree isolation

When multiple workstreams execute against the same local clone/filesystem, each actively executing workstream MUST use an isolated Git worktree or equivalent isolated checkout.

Remote-only GitHub operations do not require a local worktree.

The workflow MUST distinguish branch isolation from filesystem isolation: different branches are insufficient if two executors mutate the same checkout.

### R9 — stacked workstreams

A workstream MAY use another unmerged workstream as its parent only when the new change genuinely depends on parent-only state.

Stacked workstream state MUST record:
- parent workstream/branch;
- integration target;
- dependency relation.

A stacked child MUST NOT be merged to main/default target as though it were independent while parent-only commits remain required.

After parent integration, the child MUST rebase/retarget/reconcile before final integration as appropriate.

### R10 — integration refresh gate

Before final merge/integration, each workstream MUST compare its frozen/validated state with the current integration target.

If the target moved materially:
- reconcile/rebase/merge as appropriate;
- rerun only affected verification;
- freeze a new exact review subject if behavioral content changed;
- require a new independent verdict when the prior verdict no longer covers the exact integrated subject.

### R11 — cross-workstream conflicts

Concurrent workstreams MAY touch overlapping files, but overlap MUST NOT be treated as proof that concurrency is illegal.

A workstream becomes blocked on another only when there is a real dependency, incompatible authority, unresolved semantic conflict, or integration conflict that cannot be reconciled inside current authority.

Cross-workstream integration MUST detect both textual and material semantic conflicts.

### R12 — recovery

A fresh chat for an existing branch-isolated workstream MUST be able to recover from:
- current workflow main;
- project PROJECT.md;
- exact workstream branch;
- workstream manifest;
- workstream Task Board when implementation exists;
- exact authority/evidence/review pointers.

Previous chat narrative MUST NOT be required.

### R13 — intake handoff and fresh-session UX

Fresh-session prompts for a workstream MUST remain locator-only.

They SHOULD include the exact workstream branch and smallest canonical workstream state pointer, while the workstream manifest/state owns detailed scope, parent/base, cards, findings and evidence.

### R14 — no foreign-policy leakage

The change MUST remain inside active chatgpt_only + policy-neutral common contracts.

It MUST NOT re-import legacy parallel-lane, mixed-policy capability routing or Codex orchestration semantics.

### R15 — safe migration

Current projects with one in-progress Card in the legacy/default Task Board MUST remain legal.

Creating a new branch-isolated workstream MUST NOT reinterpret or move that existing Card unless the user explicitly chooses to migrate that workstream.

## Acceptance-level scenarios

### A — independent hotfix while feature is active

- Workstream A has one Card in_progress on `feat/a`.
- User opens a fresh chat and submits `#issue` for an independent bug.
- Intake proves the bug is based on main/default target.
- Workstream B is created on `fix/b` with its own mutable state.
- B may execute, review and merge without waiting for A.
- A later refreshes against moved main before integration.

### B — stacked hotfix

- Workstream A has unmerged behavior required to reproduce/fix an issue.
- `#issue` intake records A as parent and creates `fix/b` from A.
- B executes/reviews independently.
- B cannot be integrated to main without reconciling the parent dependency.

### C — small Tint2-style fix

- Root cause is reproduced and acceptance is measurable directly.
- Intake chooses micro-fix.
- No full Master Plan is required.
- One bounded fix contract + regression verification + fresh independent review is sufficient before merge.

### D — new feature

- User enters `#feature <goal>`.
- A feature workstream is created.
- Brainstorming/Research may proceed.
- Definition does not start until user-owned promotion is explicit.
- After Definition, normal reviewed planning and serial per-workstream execution continue.

### E — two workstreams, one local machine

- A and B execute concurrently.
- Each uses a different branch and a different worktree/checkout.
- Neither may start a second in-progress Card inside its own Task Board.

### F — same-branch collision

- A second chat targets a branch/workstream that already has an active execution obligation.
- It recovers that same obligation rather than creating a second workstream lane inside the same state.
- The workflow does not interpret multi-workstream support as permission for two simultaneous executors on one workstream.

## Non-goals

- parallel Card execution inside one chatgpt_only workstream;
- a global scheduler for all branches;
- automatic cross-policy executor selection;
- automatic conflict resolution that changes accepted product/system authority;
- forcing every project to migrate existing single-workstream state;
- replacing Git branches/PRs with a custom workflow scheduler.
