# ADR — Branch-Isolated Workstream State for ChatGPT-only

Status: accepted
Date: 2026-09-18
Scope: chatgpt_only multi-workstream execution

## Decision

Introduce branch-isolated workstreams as the unit of concurrency for normal ChatGPT.

A workstream is identified by a stable durable manifest and owns its own mutable implementation Task Board. The existing repository-global/default `implementation/TASK_BOARD.yaml` remains valid as the legacy/default single-workstream board when no branch-isolated workstream is selected.

The existing serial execution invariant is narrowed from repository-global to workstream-local:

> exactly one Card may be `in_progress` per selected chatgpt_only workstream Task Board.

Different workstreams may execute concurrently only when they use distinct branches and distinct mutable workstream state.

## Canonical layout

For a branch-isolated workstream:

```text
implementation/
└── workstreams/
    └── <workstream-id>/
        ├── WORKSTREAM.yaml
        ├── TASK_BOARD.yaml
        ├── cards/
        ├── evidence/
        └── blockers/
```

The exact project may adapt subpaths, but the manifest must identify the canonical paths.

## Workstream manifest

Minimum fields:

```yaml
id: <stable-id>
kind: issue | feature | maintenance
status: discovery | definition | planning | ready | in_progress | review | blocked | done | superseded
branch: <exact branch>
base_ref: <exact branch/ref used to create the workstream>
integration_target: <target branch>
parent_workstream: <id-or-null>
parent_branch: <branch-or-null>
task_board: <repo-relative-path-or-null>
authority:
  requirements: <path-or-null>
  decisions: []
  plan: <path-or-null>
review:
  requirement: REQUIRED | RECOMMENDED | none
  state: pending | in_progress | green | red | null
  subject: <exact-ref-or-null>
  evidence: <path-or-null>
pr: <number-or-null>
```

The manifest is routing/state-location metadata, not a duplicate Task Board. Card/milestone live execution state remains only in that workstream's Task Board.

## No global mutable workstream registry requirement

Do not require a single mutable repository-wide workstream registry as the concurrency authority.

Reason:
- concurrent workstreams would contend on that one file;
- active unmerged workstreams already have exact Git branches/PRs as durable discoverable roots;
- a fresh intake may inspect relevant branches/PRs and exact branch manifests;
- project `PROJECT.md` may document the workstream root convention but must not mirror live workstream/card state.

A future optional index may be added only as non-authoritative navigation or with conflict-safe semantics.

## Base selection

Issue/feature intake chooses one exact base:

1. default/main integration target when the new work is independent;
2. an unmerged parent workstream branch only when the new work requires parent-only state.

Choosing a parent is a dependency decision, not a convenience optimization.

## Worktree rule

Branch isolation and filesystem isolation are separate.

If two workstreams run against the same local repository storage at the same time, each must receive its own Git worktree/equivalent isolated checkout. A branch name alone does not prevent one chat from changing the checkout beneath another.

## Review model

Workstream concurrency does not weaken independence.

Behavioral `#issue` / `#feature` integration has at least a RECOMMENDED final independent review gate; existing risk-based REQUIRED semantics continue.

A micro-fix may use a single bounded workstream/fix contract instead of a Master Plan, but it still freezes an exact implementation subject for fresh independent review before integration.

## Intake markers

Add a ChatGPT-only Intake route with explicit operator markers:

- `#issue` — issue diagnosis/repair intake;
- `#feature` — feature discovery intake.

These markers select the entry route only. They do not become permanent session scope boundaries.

`#feature` does not bypass the existing user-owned Brainstorming → Definition promotion gate.

## Integration semantics

Before merging a workstream:
- refresh against the current integration target;
- detect parent/stacked dependency;
- reconcile target drift;
- rerun materially affected verification;
- invalidate/re-freeze independent review when the exact behavioral subject changed.

Overlapping files across workstreams are allowed. A real dependency/conflict, not mere overlap, determines whether one must wait for another.

## Alternatives rejected

### Keep one global Task Board and allow multiple in-progress Cards

Rejected because it reintroduces concurrent mutable-state contention and weakens the current serial execution/recovery model inside one workstream.

### One global Task Board per repository, but branch-specific copies only

Rejected as the general solution because stacked branches inherit unrelated active state and eventual merges create unnecessary state conflicts.

### Global workstream scheduler/lock service

Rejected as unnecessary complexity. Git branches/PRs plus branch-local durable manifests/state already provide the required isolation and recovery anchors.

### Force every existing project to migrate

Rejected. Existing single-workstream projects remain valid and migrate only when branch-isolated workstreams are actually needed.

## Consequences

Positive:
- independent hotfixes/features no longer wait behind unrelated active Cards;
- same-workstream execution remains simple and serial;
- fresh-chat recovery stays repository-backed;
- stacked dependencies become explicit;
- worktrees prevent local checkout collisions.

Costs:
- router/state/recovery logic must resolve the selected workstream before reading a Task Board;
- integration needs explicit target-refresh semantics;
- templates/docs/tests need single-mode + multi-workstream coverage;
- workstream-specific state remains as durable history unless later archival policy is added.
