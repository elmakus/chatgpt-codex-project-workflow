# Codex-only Repository Contract

> M03 contract. This namespace remains non-routable from root policy routing until M04.

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

## M03 lane base and result contract

Every frozen parallel batch records one exact Git `integration_base`.

Each member lane:

- starts from that exact base or a provably equivalent isolated checkout of it;
- mutates only its stable Card `write_scope`;
- does not mutate Main-owned Task Board/manifest/integration bookkeeping;
- returns one exact result commit/ref plus evidence from which Main can derive the base-to-result diff.

Project Workflow persists exact Git refs needed for recovery but not concrete checkout/worktree paths.

## Isolation rule

When two or more worker lanes perform concurrent local mutation:

1. each lane must have a distinct mutable worktree/equivalent workspace;
2. no two lanes may share an index/working tree;
3. no lane may use the coordinating Main checkout for its bounded mutation while another local lane is active;
4. inability to prove isolation before launch makes parallel execution ineligible and triggers serial fallback.

This applies to intra-workstream batches exactly as it does to cross-workstream local concurrency.

## Result verification

Before integration, Codex Main derives the exact `integration_base..result` change set and verifies:

- every changed repository path is within the Card's normalized write scope;
- no reserved shared-state artifact was changed by the lane;
- required evidence/tests are present;
- the result remains inside accepted authority.

Scope escape is preserved as evidence but not integrated.

## Deterministic integration

Main integrates valid results in the frozen member order onto the selected workstream branch. A material conflict is recovered fail-closed; returned results are preserved and successful members are not replayed.

The resulting `integrated_commit` becomes the Card's exact shared implementation result and, when review applies, the M02 review subject.

M04 reconciles stacked-workstream and final target-refresh behavior. M03 does not treat internal lane integration as workstream publication.
