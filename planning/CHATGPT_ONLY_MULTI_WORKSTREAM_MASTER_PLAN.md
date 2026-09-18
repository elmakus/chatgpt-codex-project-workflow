# ChatGPT-only Multi-Workstream + Intake — Master Plan

Status: approved
Plan revision: MW-R1
Date: 2026-09-18
Independent plan review: REQUIRED

## Authority

- Requirements: `requirements/CHATGPT_ONLY_MULTI_WORKSTREAM_INTAKE.md`
- Accepted decision: `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
- Workflow baseline: current `main` at branch creation, after PR #27 fresh-handoff continuation merge.

## Objective

Add branch-isolated concurrent workstreams to `chatgpt_only` without reintroducing parallel execution inside one workstream, and add explicit `#issue` / `#feature` intake routes that select the smallest legal workflow path.

The implementation must remain backward-compatible with existing projects that use one `implementation/TASK_BOARD.yaml`.

## Global invariants

1. Exactly one Card may be `in_progress` per selected workstream Task Board.
2. A second independent workstream does not mutate or wait on another workstream's mutable state unless a real dependency/conflict exists.
3. Existing single-workstream projects remain legal and recoverable without migration.
4. The active branch/workstream is resolved before implementation/review/recovery state is loaded.
5. `#feature` never bypasses the user-owned Brainstorming → Definition promotion gate.
6. Behavioral issue/feature integration has a real fresh independent review gate.
7. Local concurrent execution requires separate worktrees/equivalent isolated checkouts.
8. Stacked workstreams explicitly record parent/base/integration relationships.
9. Target movement before integration triggers an integration refresh and invalidates review only when the exact covered subject materially changes.
10. No legacy/mixed/Codex parallel-lane semantics enter `chatgpt_only`.

## M01 — Workstream state model and routing foundation

### Outcome

Current workflow can deterministically resolve either:
- legacy/default single-workstream state; or
- one exact branch-isolated workstream manifest + its Task Board.

### Planned work

- add a policy-local workstream contract, expected path:
  `workflow/chatgpt_only/WORKSTREAMS.md`;
- add a branch-isolated manifest template;
- add a workstream Task Board template or parameterize the existing ChatGPT-only template without weakening serial semantics;
- update `STATE.md` so "one in_progress Card" is workstream-local;
- update `ROUTER.md` bootstrap to resolve workstream before implementation/review/recovery routing;
- update `CONTEXT_ROUTING.md` wording so canonical mutable implementation state may be the selected workstream Task Board;
- update `REPOSITORY.md` canonical layout/state ownership/recovery rules;
- preserve legacy `implementation/TASK_BOARD.yaml` fallback exactly.

### Acceptance

- legacy project with only `implementation/TASK_BOARD.yaml` routes unchanged;
- two branch-isolated manifests may each own one in-progress Card without either state being invalid;
- two in-progress Cards in the same selected workstream remain invalid;
- no global mutable registry is required for correctness.

## M02 — Intake route: #issue / #feature

### Outcome

Explicit operator markers route into a deterministic intake layer before normal phase/execution selection.

### Planned work

- add `workflow/chatgpt_only/INTAKE.md`;
- update router entry precedence for explicit `#issue` / `#feature`;
- define issue intake:
  - diagnostic/reproduction-first when practical;
  - active branch/PR/workstream discovery;
  - base selection;
  - independent vs stacked classification;
  - branch/workstream creation;
  - micro-fix vs normal workflow classification;
- define feature intake:
  - new workstream creation;
  - Brainstorming/Research entry;
  - preservation of explicit Definition promotion authority;
- define naming/identity rules for workstream IDs and branches;
- ensure marker semantics are entry locators, not session-scope boundaries.

### Acceptance

- `#issue` cannot be blocked merely because another unrelated workstream has an in-progress Card;
- `#feature` enters discovery without silently authorizing Definition;
- existing ordinary prompts continue to use normal router behavior;
- intake never modifies an unrelated active workstream merely because it discovered the symptom.

## M03 — Micro-fix, execution, review and recovery semantics

### Outcome

Small fixes can complete without a heavyweight plan while still retaining durable scope, verification and independent review; normal workstream execution/recovery is branch-local.

### Planned work

- define micro-fix contract and qualifying criteria;
- update `EXECUTION_PREP.md` / `EXECUTION.md` for selected workstream state;
- update `REVIEW.md` and `STATE.md` for workstream-local subjects/evidence;
- update `RECOVERY.md` so exact branch + manifest + Task Board recover the obligation;
- adapt implementation-owned Research pointers to the selected workstream Task Board;
- keep Card/milestone review mechanics unchanged inside a workstream;
- add final integration review requirement for behavioral issue/feature workstreams when no stronger existing review already covers the exact integrated subject.

### Acceptance

- Tint2-style bounded fix can use one durable fix contract, implementation evidence, regression check and fresh review without a full Master Plan;
- recovery does not inspect another workstream Task Board by default;
- RED correction remains inside the affected workstream;
- same-branch second chat recovers the same active obligation instead of creating a parallel lane.

## M04 — Worktree, stacked branch and integration refresh contracts

### Outcome

The workflow defines safe concurrency at both Git and local-filesystem levels and can integrate workstreams after target drift.

### Planned work

- update `REPOSITORY.md` with worktree/equivalent isolation requirement for concurrent local execution;
- define stacked-parent fields and legal child integration paths;
- define integration refresh gate in `CLOSE.md` / workstream contract;
- define target-drift handling:
  - current target comparison;
  - rebase/merge/retarget decision inside accepted authority;
  - affected verification rerun;
  - exact review-subject invalidation/re-freeze rules;
- define overlap/conflict semantics: file overlap alone is not a blocker; real dependency/semantic/integration conflict is;
- prevent child-to-main integration that silently depends on unmerged parent-only commits.

### Acceptance

- independent branch can merge while another feature remains active;
- stacked branch cannot masquerade as independent;
- moved main triggers refresh for stale branch before final integration;
- behavioral changes caused by reconciliation receive a new exact independent review subject.

## M05 — UX, templates, migration and regression coverage

### Outcome

Operators can actually use the new model from fresh chats without knowing internal state layout, and existing projects are not broken.

### Planned work

- update `workflow/common/USER_STOP.md` fresh handoff shapes to support an exact workstream start pointer without prompt inflation;
- update `CHATGPT.md`, README and fresh-session/start documentation where necessary;
- update `templates/PROJECT.md` with optional workstream-root convention while keeping PROJECT non-live;
- add workstream manifest/Task Board examples/templates;
- update changelog;
- add durable architecture/coherence audit scope covering single-mode, multi-workstream, issue intake, feature intake, micro-fix, stacked branch, local worktrees, review and integration refresh;
- add static/coherence regression checks where practical.

### Required logical E2E matrix

1. legacy single-workstream project continues unchanged;
2. active feature A + independent `#issue` B → B executes/reviews/merges without waiting;
3. active feature A + parent-dependent `#issue` B → stacked B records A and cannot integrate independently;
4. `#feature` → Brainstorming/Research → explicit promotion → Definition → Planning;
5. micro-fix → direct bounded contract → implementation → independent review → integration;
6. two local workstreams → separate worktrees;
7. same workstream targeted by second chat → recovery, not a second lane;
8. target main moves after GREEN → refresh → unchanged subject preserves verdict only if exact covered content remains identical; otherwise new review;
9. RED review in B never redirects unrelated A;
10. fresh handoff carries branch + smallest canonical workstream pointer and resumes normal router-owned continuation.

### Acceptance

- current single-workstream wording is either scoped correctly or explicitly marked legacy/default;
- no active ChatGPT-only doc still claims repository-global single-Card seriality where workstream-local semantics are intended;
- no user-facing handoff requires dumping workstream state into prompt text;
- no Codex/mixed/legacy execution semantics are imported.

## JIT decomposition strategy

Implementation Cards should be created milestone-by-milestone after plan review.

Known first-card boundaries:
- M01 contract/state/router foundation is independently implementable.
- M02 depends on M01 workstream resolution.
- M03 depends on M01 and M02 intake identity.
- M04 depends on M01 branch/parent model and M03 review state.
- M05 integrates all prior semantics.

Execution Prep may split these milestones into smaller Cards based on actual file coupling discovered at Refresh Gate. It must not change the accepted state model, backward-compatibility invariant, review requirement or user-owned feature promotion semantics.

## Migration strategy

No repository-wide migration.

For existing projects:
- absence of a branch-isolated workstream manifest means legacy/default single-workstream recovery;
- first use of `#issue` / `#feature` may create a new workstream layout on that new branch;
- an existing active default Task Board is not moved automatically;
- deliberate conversion of an existing active branch into a named workstream requires a bounded explicit reconciliation step.

## Verification strategy

At each milestone:
- inspect active workflow docs for contradictory state ownership/seriality text;
- trace required E2E scenarios against router precedence;
- verify recovery from durable state without prior transcript;
- verify no duplicate canonical state source is created;
- verify review independence and fresh-handoff continuation remain intact.

Before merge:
- run a fresh independent architecture/coherence review over the exact implementation subject;
- verify current main has not moved in a way that invalidates the implementation assumptions;
- if main moved materially, reconcile and re-review the changed exact subject.

## Planning audit

GREEN.

Specifically checked:
- concurrency unit is workstream, not Card lane;
- no global mutable registry is needed;
- single-workstream compatibility is explicit;
- stacked dependencies are modeled rather than hidden;
- local worktree isolation is not conflated with branch isolation;
- micro-fix avoids unnecessary planning overhead without dropping review;
- `#feature` preserves the existing user-owned Definition promotion gate;
- integration drift has an explicit refresh/review rule;
- review independence remains per exact workstream subject;
- implementation can be decomposed JIT without freezing speculative Card IDs.

Independent plan review is REQUIRED because this changes core routing, state ownership, recovery and review/integration semantics of `chatgpt_only`.
