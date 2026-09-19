# Codex-only Task Card Contract

> Live Codex-only Task Card contract. M03 safety metadata is optional; Cards remain serial-valid when it is absent.

## Meaning

A Task Card is a bounded project work-package contract. Codex Main owns project-level execution coordination; concrete worker realization is runtime-owned.

## Required project contract

Each Card identifies:
- stable ID/title/milestone;
- dependencies;
- exact durable authority slice;
- bounded included/excluded scope;
- outcome and acceptance;
- required tests/evidence/readback;
- authorization gates;
- independent-review requirement when applicable.

Mutable execution/review/result/batch state belongs to the selected canonical Task Board, not the stable Card contract.

## Optional parallel-safety contract

Serial execution is valid by default. Absence of M03 parallel fields is equivalent to:

```yaml
parallel_safe: false
write_scope: []
exclusive_resources: []
```

A Card may be considered for concurrent execution only when it explicitly declares `parallel_safe: true`.

For an opted-in Card:

- `write_scope` is a non-empty finite list of normalized repository-relative path prefixes covering every repository mutation the lane may make, including lane-owned evidence;
- absolute paths, `..` traversal and glob semantics are invalid for parallel eligibility;
- `.` claims the whole repository;
- two path claims conflict when equal or when one is an ancestor prefix of the other on a path-segment boundary;
- `exclusive_resources` is a finite list of stable project-level resource tokens; exact token equality conflicts;
- the live selected Task Board, workstream manifest and shared integration bookkeeping are reserved Main-owned state and cannot be delegated to a worker lane through a broad write scope.

These fields are JIT inputs, not a planning-time concurrency guarantee.

## JIT rule

Planning may identify candidate overlap, but only Execution Prep may freeze a current compatible batch after current dependencies, scopes/resources, workspace isolation and exact integration base are proven.

If any required safety fact is missing or incompatible, the Card remains eligible for deterministic serial execution unless a separate blocker exists.

## Runtime boundary

Project Card metadata describes project safety and ownership only. Do not encode concrete worker/session/model/profile/invocation/lease/resume identity or concrete worktree paths in the Card contract.

A lane may produce bounded implementation/evidence under its Card authority. It never becomes an independent writer of shared Task Board/integration state.
