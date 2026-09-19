# Codex-only Repository Contract

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Repository truth

One project repository owns durable project truth. Project Workflow state is recovered from repository artifacts plus exact Git/runtime/external evidence; transcript state is not canonical.

## Foundation invariants

- Branch-isolated workstreams use exact manifests and manifest-selected Task Boards.
- No repository-global mutable workstream registry/scheduler is required.
- Codex Main is the sole writer of shared Task Board and integration bookkeeping.
- Concurrent mutable local work requires isolated worktrees/equivalent workspaces; a branch name alone is not filesystem isolation.
- Worker lanes may own bounded implementation/evidence scope but never become independent owners of shared project coordination state.
- Runtime worker identity/lifecycle is not durable repository authority.
- Never force-push the integration target as routine remediation.

M03 finalizes intra-workstream lane/worktree ownership and recoverable integration-base semantics. M04 reconciles stacked-workstream and target-refresh behavior.
