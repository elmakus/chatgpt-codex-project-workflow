# Codex-only Workstreams

> M03 contract. This namespace remains non-routable from root policy routing until M04.

## Core model

A branch-isolated workstream has one stable ID, exact branch/base/target, one manifest and at most one canonical Task Board. The manifest owns workstream identity/routing/final-integration review; the selected Task Board owns Card/milestone execution plus M03 bounded-batch state.

## Foundation invariants

- Validate manifest ID/branch binding before trusting its Task Board.
- Legacy/default Task Board mode remains valid when no branch-isolated workstream is selected.
- Independent workstreams remain distinct from genuinely parent-dependent stacked work.
- No repository-global mutable workstream scheduler is introduced.
- Final integration uses current-target refresh and exact-subject review coverage.
- Codex Main owns shared workstream integration/project state.
- Runtime worker identity/lifecycle is not durable workstream authority.

M04 completes stacked integration, target refresh, final-review coverage and full Close routing.

## Intra-workstream bounded parallelism

One selected workstream may temporarily have multiple `in_progress` Cards only through one valid current M03 batch.

The batch:

- is local to that workstream's selected Task Board;
- has one exact workstream Git integration base;
- freezes finite membership/order before launch;
- assigns semantic lane labels that identify project result provenance, not workers;
- never creates another Task Board or mutable workstream registry;
- leaves non-member Cards in ordinary lifecycle state.

A workstream with `parallel: null` or no eligible batch remains fully serial.

## Mutable workspace isolation

Concurrent local mutation inside one workstream requires the same filesystem isolation as concurrent mutation across workstreams:

- each concurrently mutating lane uses a separate Git worktree or equivalent isolated checkout;
- different branch names inside one shared mutable checkout are not sufficient isolation;
- Project Workflow records the requirement/proof outcome, not concrete local paths or runtime handles;
- if isolation cannot be established immediately before launch, the candidate set falls back to serial execution.

Remote-only operations that do not share a mutable local working tree do not require artificial worktree creation merely to imitate the local rule.

## Integration ownership

Lane work does not directly become shared workstream state.

- each member starts from the exact frozen integration base;
- lane result/evidence returns to Codex Main;
- Main validates the base-to-result diff against the Card's write scope and reserved shared-state rule;
- Main integrates members sequentially in frozen order;
- `integrated_commit` is the durable shared-workstream result for that member;
- Card review/finalization uses that integrated result under M02 semantics.

A lane cannot update the workstream manifest, selected Task Board or shared integration bookkeeping. Those remain Main-only even when their file paths would otherwise match a broad Card scope.

## Interaction with workstream final integration

M03 batches integrate only into the selected workstream branch/state. They do not bypass the distinct manifest-owned final-integration review or target-refresh gate.

M04 determines the complete branch-isolated workstream close/integration flow. A completed internal batch is not evidence that the workstream is ready to merge to its final target.

## Recovery

Recover intra-workstream batch state only from the selected canonical Task Board plus exact Git/evidence refs. Never inspect another workstream's Task Board or runtime worker list to reconstruct this batch.

Returned/integrated member results survive worker loss and are never replayed merely because runtime state disappeared.
