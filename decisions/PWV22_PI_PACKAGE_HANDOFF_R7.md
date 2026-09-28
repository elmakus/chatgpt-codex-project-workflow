# PWv2.2 R7 — Official Pi package and universal handoff decision

Status: accepted Definition authority for `pwv22-program@22`.

## Decision

1. PWv2.2 ships the first official **Project Workflow for Pi** package rather than deferring the Pi packaging boundary to PWv2.3.
2. The package is the normal local operational Project Workflow surface for Pi. It carries the Pi bootstrap/skill/instructions and the qualified thin deterministic helper. It does not become a second semantic state store, scheduler, journal, database, Task Board or orchestration control plane.
3. Git/GitHub remains canonical release/provenance authority. The package must identify the official workflow release/policy it implements. When a compatible official package is unavailable, the receiver falls back to `elmakus/project_workflow_v2`.
4. The handoff becomes universal across ChatGPT and Pi runtimes. It always contains a tiny bootstrap rule selecting official local package when available/compatible and canonical GitHub fallback otherwise.
5. The handoff also binds the exact consumer repository, branch, **handoff commit**, entry obligation and durable start pointer.
6. On receipt, the runtime fetches/read-backs the remote branch and confirms that it still points to the handoff commit. If the branch moved, the handoff is stale; the receiver reconstructs current canonical state instead of proceeding from the old commit.
7. Local uncommitted changes and local-only commits are runtime residue unless they were published into canonical durable state. If a newer valid handoff supersedes such residue, the old local attempt is not salvaged or merged merely because it exists.
8. For ordinary same-branch continuation, stale Pi/Paseo worktrees are removed/recreated or equivalently reset to the verified remote handoff commit rather than keeping a second copy of the same branch. Intentionally admitted parallel work still uses distinct worktrees/branches as required by PW.
9. External effects are explicitly excluded from the disposable-local-state rule. If the abandoned runtime may have changed production, an API, database, message, deployment or another non-Git system, that effect must be reconciled through durable effect/readback semantics before cleanup.
10. The Pi package has no private updater. `pi-unraid` owns package installation/update/rollback/readback together with Pi, Paseo and the rest of the deployment stack.

## Scope and prior qualification

This is a Definition refinement inside already-promoted `pwv22-program@22`, not a new product scope. Revision 22 already covers runtime-neutral handoff/bootstrap and the required Pi/Paseo realization.

R6 P0-P6 remains valid architecture evidence: native Paseo + Pi + explicit configuration/skills + a thin reconstructible helper is unchanged. R7 changes the delivery boundary and exact handoff/worktree continuation contract; downstream Planning/implementation must add the corresponding acceptance/regression coverage.
