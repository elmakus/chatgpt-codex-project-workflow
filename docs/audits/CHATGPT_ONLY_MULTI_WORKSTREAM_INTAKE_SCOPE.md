# ChatGPT-only Multi-Workstream + Intake — Final Independent Architecture/Coherence Review Scope

Date: 2026-09-19  
Implementation baseline: `main@03035876f3283d33e8a10ff43265f5be21a27a06`  
Implementation branch: `feat/chatgpt-only-multi-workstream-intake`  
Review requirement: **REQUIRED**  
Canonical review state: `implementation/TASK_BOARD.yaml → M05-T01`  
Review subject: recover the exact immutable `M05-T01.review_subject` from Task Board at independent-review entry. Do not use this file, the PR body or implementation-author evidence as verdict authority.

## Accepted target behavior

The feature adds branch-isolated workstreams to active `chatgpt_only` while preserving serial execution inside each selected workstream and preserving legacy/default single-workstream operation.

A workstream is recoverable from its exact branch + durable manifest. Its selected Task Board owns Card/milestone execution, Card/milestone review and implementation/recovery Research state. The manifest owns workstream identity/routing/intake metadata and the distinct workstream final-integration review gate.

Explicit `#issue` / `#feature` directives create/recover independent or genuinely stacked workstreams without turning intake markers into permanent session scope. Feature intake preserves explicit user-owned Definition promotion. Qualified issue micro-fixes may skip a full Master Plan without losing durable acceptance/evidence or independent review.

Concurrent local mutation uses isolated worktrees/equivalent checkouts. Stacked parent dependencies are explicit. Final integration refreshes against the current target, reruns affected verification, checks textual and semantic conflicts, and invalidates review only when the exact covered workstream content/behavior or acceptance surface materially changes.

Fresh ChatGPT handoffs remain locator-only and use the smallest canonical state owner. Finishing the named entry role returns to router-owned deterministic continuation until a real workflow stop.

## Authority to check

- `requirements/CHATGPT_ONLY_MULTI_WORKSTREAM_INTAKE.md` — R1–R15, scenarios A–F
- `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
- `planning/CHATGPT_ONLY_MULTI_WORKSTREAM_MASTER_PLAN.md` revision `MW-R1`, including M01–M05 and final verification strategy
- `implementation/cards/M01-T01.md` through `implementation/cards/M05-T01.md`
- accepted M01–M04 handoffs/acceptance/review evidence
- current workflow `main` at independent-review entry
- exact frozen final feature-branch subject from Task Board

Exact accepted authority outranks this navigation scope when wording differs.

## Review objectives

Independently verify the exact final subject against current workflow authority and actual branch diff.

At minimum verify:

1. **Workstream-local seriality and state ownership**
   - one `in_progress` Card per selected Task Board, not per repository;
   - independent branch-isolated workstreams use distinct branch + mutable state;
   - manifest ↔ Task Board identity binding occurs before branch-isolated mutable state is trusted;
   - manifest workstream final-review state is not mirrored into Card/milestone Task Board review state.

2. **Legacy/default compatibility**
   - projects with only `implementation/TASK_BOARD.yaml` remain legal/recoverable without migration;
   - creating a branch-isolated workstream does not reinterpret/move legacy active state;
   - operator-facing docs/templates do not imply branch-isolated state is mandatory.

3. **Issue intake**
   - explicit `#issue` has intake precedence over unrelated existing workstream obligations without mutating them;
   - diagnosis/discovery happens far enough before base choice to classify independent vs genuine parent-only dependency;
   - qualified micro-fix versus normal Research/Definition/Planning/Execution Prep routing is durable and recoverable.

4. **Feature intake and promotion authority**
   - explicit `#feature` creates/recovers a feature workstream and discovery state;
   - the marker itself never authorizes Brainstorming → Project Definition;
   - exact scope/revision promotion remains user-owned and normal Planning begins only after Definition is GREEN.

5. **Micro-fix execution/review/recovery**
   - all R6 criteria are required before skipping a full Master Plan;
   - one bounded fix Card + evidence + exact subject review is sufficient when criteria hold;
   - same-branch fresh chat recovers the existing obligation instead of creating a second lane;
   - RED correction/Research remains inside the affected selected workstream.

6. **Local filesystem isolation**
   - concurrent local mutation requires separate Git worktrees/equivalent isolated checkouts;
   - distinct branches alone are not enough in one mutable checkout;
   - remote-only GitHub execution is exempt;
   - worktrees do not authorize a second Card lane inside one workstream.

7. **Stacked dependency semantics**
   - parent selection requires parent-only state, not overlap/convenience;
   - manifest records parent workstream/branch, creation base, integration target and exact parent dependency;
   - direct child → final target is forbidden while required parent-only content is absent;
   - both legal paths are coherent: child folded into parent, or parent integrated first then child reconciled onto current target.

8. **Integration refresh and conflict semantics**
   - final integration compares the frozen/validated workstream with the current target;
   - material target movement triggers only bounded authorized reconciliation + affected verification;
   - both textual and material semantic/interface conflicts are checked;
   - file overlap alone is not a blocker;
   - target is re-read immediately before actual integration.

9. **Exact-subject independent review**
   - behavioral issue/feature final integration has at least RECOMMENDED independent review unless exact stronger independent coverage proves the identical immutable subject + whole acceptance surface;
   - target SHA/ancestry movement alone does not invalidate review;
   - materially changed covered content/behavior/acceptance freezes a new exact subject and requires fresh independent review;
   - the chat that performs the changed reconciliation cannot self-review it.

10. **Fresh-session UX / continuation**
    - fresh prompts remain short, branch-aware locator-only handoffs;
    - selected Task Board is the pointer for Card/milestone review; selected manifest is the pointer for workstream final-integration review;
    - workstream state, checklists, SHAs and remediation branches are not copied into prompt text;
    - after the entry role completes, the fresh chat returns to the policy router and continues until a real stop.

11. **Policy isolation**
    - no active `chatgpt_only` contract imports mixed-policy capability routing, Codex orchestration, legacy bounded-parallel lanes or a global scheduler/registry;
    - no change weakens explicit user/deployment/live-write authorization gates or accepted review independence.

12. **Migration/documentation coherence**
    - README/start/fresh-session/PROJECT template describe selected-state ownership consistently;
    - `PROJECT.md` workstream-root convention is non-live navigation, not an active registry/state mirror;
    - existing manifest/Task Board templates are sufficient for fresh recovery;
    - changelog describes the actual final behavior without claiming nonexistent automation.

## Required logical E2E matrix

### 1. Legacy single-workstream project

```text
PROJECT.md → no branch-isolated manifest selected
→ implementation/TASK_BOARD.yaml remains canonical
→ one in_progress Card rule unchanged
→ normal review/recovery/continuation
```

### 2. Active feature A + independent #issue B

```text
A active on feat/a
→ fresh chat #issue B
→ issue diagnosis/discovery proves main/default base
→ create fix/b + distinct manifest/state
→ B executes/reviews/refreshes/integrates without waiting for A
→ A later refreshes against moved target
```

### 3. Parent-dependent #issue B stacked on A

```text
issue needs A-only behavior
→ Intake records A parent + exact parent_dependency
→ create B from A
→ B executes/reviews
→ direct B → final target forbidden while dependency absent
→ either fold B into A, or integrate A then reconcile B onto current target
```

### 4. #feature lifecycle

```text
#feature
→ workstream + Brainstorming/Research state
→ promotion pending
→ explicit user promotion of exact scope/revision
→ Definition GREEN
→ Planning / reviewed plan
→ Execution Prep / Execution
```

### 5. Micro-fix

```text
#issue reproduction + all R6 criteria
→ path: micro_fix
→ completed Intake is pre-Task-Board anchor
→ Execution Prep creates one bounded fix Card + selected board
→ implementation/evidence
→ fresh independent Card review
→ final-integration gate coverage/review
→ integration
```

### 6. Two local workstreams

```text
A and B mutate locally at same time
→ distinct branches + distinct Task Boards
→ distinct worktrees/equivalent mutable checkouts
→ max one in_progress Card inside each selected board
```

### 7. Same-workstream second chat

```text
fresh chat targets same exact branch/manifest
→ recover active Intake/Task Board/review/Research obligation
→ no second lane / duplicate workstream state
```

### 8. Target moves after GREEN

```text
workstream has exact GREEN coverage
→ integration target moves
→ refresh + affected compatibility verification
→ exact covered content/acceptance unchanged: prior verdict may remain valid
→ covered behavior/acceptance changed: new exact subject → fresh independent review
```

### 9. RED review in B

```text
B review RED
→ persist RED in B's exact review owner
→ correction/Research uses B selected state only
→ unrelated A Task Board is not correction state
```

### 10. Fresh handoff

```text
fresh boundary
→ prompt includes repo + exact branch + entry obligation + smallest canonical pointer
→ no workstream-state dump
→ fresh chat reconstructs exact state from repository
→ named role completes
→ router-owned deterministic continuation resumes until real stop
```

## Implementation-author self-check boundary

Implementation-author validation may execute lexical/static/coherence checks and trace the matrix above, but it is **not** the independent verdict.

The independent reviewer must reconstruct the exact frozen subject and current authority from the repository. A GREEN verdict may proceed through router-owned post-review finalization and final project/PR integration checks. A RED verdict follows current ChatGPT-only corrective routing; bounded deterministic remediation continues in that reviewer-started chat until a new independent-review boundary or another real stop.
