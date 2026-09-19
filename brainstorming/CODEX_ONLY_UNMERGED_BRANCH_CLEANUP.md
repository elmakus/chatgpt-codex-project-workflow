# Brainstorm — Codex-only terminal unmerged branch cleanup

Date: `2026-09-20`
Scope ID: `codex-only-unmerged-branch-cleanup`
Revision: `R1`
Status: `ready_for_definition`

## Problem / goal

Keep Codex-only branch cleanup simple.

Merged workstream branches are already handled by repository-level automatic deletion after merge. This scope therefore addresses only branch-isolated Codex-only workstreams that become terminal without final integration/merge, for example a superseded workstream.

## Current understanding

### Verified repository facts

- Codex-only already models branch-isolated workstreams and terminal lifecycle state in `WORKSTREAM.yaml`.
- Current Codex-only Close/Recovery rules already require terminal work to be durably recoverable and free of live Card, Research, review, stacked-dependency and integration obligations before a branch may disappear.
- The supported workstation image installs `gh`.

### Explicit user/product choices

- All current repositories have automatic deletion of merged branches enabled, and future repositories will have it enabled by default.
- The supported Codex environment has authenticated `gh` access with the permissions needed for normal repository branch operations.
- No new cleanup lifecycle is needed for merged workstreams.
- No `branch_cleanup`, `safe_to_delete`, CAS/lease protocol or merged-branch fallback is needed for this Codex-only scope.
- The only new behavior needed is cleanup of terminal workstreams that end without merge.

## Accepted direction to promote

For a branch-isolated Codex-only workstream that intentionally reaches a terminal state without final integration/merge:

1. existing terminal-safety/recovery conditions must already be satisfied;
2. Codex Main deletes the exact workstream branch through `gh`;
3. if execution is interrupted after terminal state is durable but before deletion completes, Recovery checks the terminal-unmerged workstream and deletes the branch if it still exists;
4. if the branch is already absent, Recovery treats cleanup as complete;
5. no separate cleanup state is persisted solely to track the deletion.

Merged workstreams remain outside this feature and rely on repository automatic branch deletion.

## Alternatives considered

Earlier broader designs added merged-branch fallback state, `safe_to_delete`, explicit post-merge deletion handling and guarded deletion protocols. They are rejected for this scope because repository auto-delete and the supported Codex environment make them unnecessary.

## Research needed

None before Definition.

## Open questions

None that require user/product authority before Definition.

## Outcome of this session

- Tentative conclusions: only terminal-unmerged Codex-only workstreams need explicit active cleanup.
- Explicit user/product choices to promote through Project Definition: the accepted direction above.
- Research still needed: none before Definition.
- Open questions: none.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `user_authorized`
- Definition promotion subject: `codex-only-unmerged-branch-cleanup@R1`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
