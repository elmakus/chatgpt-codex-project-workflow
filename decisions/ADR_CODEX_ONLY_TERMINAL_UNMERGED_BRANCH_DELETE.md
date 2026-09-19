# Decision — Codex Main deletes terminal unmerged workstream branches

- Decision ID: `ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE`
- Date: `2026-09-20`
- Status: `accepted`
- Authority: `user`
- Supersedes: `none`
- Related requirements: `requirements/CODEX_ONLY_UNMERGED_BRANCH_CLEANUP.md`
- Related milestone/card: `none`

## Context

Normal merged workstream branches are already removed by repository-level automatic branch deletion after merge. The remaining cleanup case is a Codex-only branch-isolated workstream that intentionally becomes terminal without final integration/merge, such as a superseded workstream.

Earlier brainstorming considered a broader cleanup lifecycle with durable `safe_to_delete` state and merged-branch fallbacks. The supported environment makes that unnecessary: merged branches are repository-cleaned automatically, while Codex Main has authenticated `gh` access for direct branch deletion.

## Decision

Use the existing terminal workstream lifecycle as the cleanup authority.

When a branch-isolated Codex-only workstream intentionally reaches a terminal state without final integration/merge and the existing terminal-safety conditions are satisfied, Codex Main deletes the exact manifest-owned source branch through `gh`.

Do not add a separate cleanup lifecycle or manifest field for this feature.

Recovery is idempotent:
- terminal-unmerged + exact branch exists → delete it;
- terminal-unmerged + exact branch absent → cleanup is complete.

Normal merged workstreams remain outside this decision and continue to rely on repository automatic branch deletion.

## Rationale

The terminal workstream state already expresses the semantic fact needed to authorize cleanup. A second durable cleanup state would duplicate that authority without adding useful information.

Using exact manifest identity keeps deletion deterministic and avoids branch-prefix heuristics. Recovery can derive the only unfinished action directly from durable terminal state plus current branch existence.

## Alternatives considered

### Separate `branch_cleanup/safe_to_delete` lifecycle

Rejected for Codex-only in this scope. It adds state for a condition already represented by terminal workstream state.

### Codex fallback deletion for merged branches

Rejected. Repository automatic deletion already owns the merged path.

### Cleanup by Executor/Tester worker

Rejected. Branch cleanup is workstream lifecycle/finalization owned by Codex Main, not implementation or independent-review work.

## Consequences

- Codex-only Close/terminal-transition contracts must invoke deletion for intentional terminal-unmerged workstreams once existing safety gates pass.
- Codex-only Recovery must finish the delete when terminal state is durable but the branch remains.
- Codex-only routing/repository/workstream contracts may need small wording updates so a missing terminal-unmerged source branch is normal.
- No cleanup state is added to `WORKSTREAM.yaml` or Task Board.
- Merged-workstream behavior remains unchanged.

## Required authoritative updates

- Requirements / Project Definition: `requirements/CODEX_ONLY_UNMERGED_BRANCH_CLEANUP.md`
- Planning: create a minimal plan for Codex-only lifecycle/recovery contract updates and regression evidence.
- Task Card/OpenSpec: only if required later by Planning/Execution Prep.
- PROJECT.md: point current requirements/decision authority to this Definition after completion.

## Provenance

- Source discussion/request: user-approved Brainstorming scope `codex-only-unmerged-branch-cleanup@R1`
- Evidence/research: current Codex-only workstream/Close/Recovery contracts; supported environment includes authenticated `gh`
- Strategic `request_id`: `none`
- Exact `DECISION FOR CODEX:` marker: `none`
- Persisting commit: `recorded by repository history`
