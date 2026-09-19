# Decision — Auto-delete merged workstream branches

- Decision ID: ADR-CHATGPT-ONLY-AUTODELETE-MERGED-HEAD-BRANCHES
- Date: 2026-09-19
- Status: accepted
- Authority: user
- Supersedes: none
- Related requirements: requirements/CHATGPT_ONLY_BRANCH_CLEANUP.md
- Related milestone/card: none

## Context

The initial cleanup proposal used a visible delete/ prefix. The currently available ChatGPT GitHub connector cannot perform a true branch rename/delete operation; creating a new delete/... branch at the same SHA creates a duplicate ref and leaves the original branch in place.

GitHub natively supports repository-level automatic deletion of merged PR head branches. Current ChatGPT-only finalization semantics can be reorganized so source-branch survival is unnecessary after merge.

## Decision

For normal ChatGPT-only GitHub PR integration, design Project Workflow so the source workstream branch is disposable immediately after successful merge and may be automatically deleted by GitHub.

Do not use delete/* alias branches as cleanup markers.

For terminal branches that are not removed automatically — including intentionally closed/superseded unmerged branches and merged branches retained by repository settings/rules — use a durable, exact safe_to_delete fallback state after terminal safety is proven. Physical deletion remains an operation for a cleanup-capable actor.

Codex-only is not changed by this workstream and may port the accepted behavior later.

## Rationale

- removes stale merged branches at the repository level without extra agent actions;
- avoids duplicate refs caused by connector limitations;
- reduces branch-list ambiguity;
- strengthens the architecture by making terminal recovery target-side rather than source-branch-dependent;
- preserves a safe fallback for non-merged or undeletable branches;
- does not require ChatGPT connector to gain rename/delete capability.

## Alternatives considered

### Prefix every deletion-ready branch with delete/

Rejected as the normal ChatGPT-only mechanism because the current connector cannot perform a true rename and can create duplicate refs instead.

### Durable cleanup marker for every merged branch

Retained only as fallback. It is unnecessary operational state when GitHub can remove the merged head branch automatically.

### Immediate manual deletion by ChatGPT

Rejected as a workflow assumption because the current connector does not expose the required delete-ref operation.

## Consequences

- pre-merge finalization must guarantee target-side recoverability;
- post-merge close/reconciliation cannot depend on source-branch existence;
- repository auto-delete becomes the preferred normal merged-PR cleanup mechanism;
- a small fallback cleanup lifecycle must exist for surviving/non-merged terminal branches;
- stacked child recovery must not require parent source branches after parent merge;
- accidental duplicate delete/* refs are treated as cleanup debt, not valid workflow markers.

## Required authoritative updates

- Requirements / Project Definition: requirements/CHATGPT_ONLY_BRANCH_CLEANUP.md
- Planning: new branch-cleanup Master Plan
- Task Card/OpenSpec: determine JIT during Execution Prep
- PROJECT.md: clear completed exploratory-scope pointer when Definition closes

## Provenance

- Source discussion/request: user explicitly preferred changing Project Workflow to support GitHub automatic head-branch deletion after merge rather than retaining branches for post-merge bookkeeping.
- Evidence/research: current ChatGPT GitHub connector surface lacks true branch rename/delete operations; current workflow already supports target-side terminal recovery after source-branch deletion.
