# ChatGPT-only Milestone Close / Publication / Workstream Integration

This module owns integrated milestone acceptance, publication verification, branch-isolated workstream integration, cumulative handoff and automatic next-milestone continuation.

## Entry condition

Enter when:
- required Cards for milestone are done;
- required/recommended Card review gates are green;
- intended final milestone state exists.

If a pending/in-progress review still exists, route to `REVIEW.md` first.

## Integrated milestone acceptance

Evaluate intended final milestone state against:
- approved milestone outcome/acceptance;
- applicable requirements/accepted decisions;
- integrated behavior;
- required tests;
- migration/rollback/data-integrity/security constraints;
- material external-state readback;
- relevant OpenSpec;
- required evidence.

If milestone acceptance itself requires/recommends independent review and current chat implemented the accepted subject, freeze exact milestone subject as `pending` and stop with fresh-review prompt.

### RED

- milestone is not done;
- create/reopen bounded corrective work;
- persist failing evidence;
- continue immediately into deterministic remediation when legally bounded and unblocked;
- changed subject receives fresh independent review when required/recommended.

### GREEN

Proceed to publication/finalization.

## Branch-isolated integration refresh gate

Run this gate when the selected branch-isolated workstream is about to be integrated/published into another branch or its final `integration_target`.

A milestone checkpoint that remains on the same workstream branch and performs no cross-branch integration does not run this gate merely because milestone acceptance is GREEN.

Read the selected `WORKSTREAM.yaml` and apply `workflow/chatgpt_only/WORKSTREAMS.md#Integration refresh contract`.

Required ordering:

1. Verify exact workstream branch/manifest identity, current integration target and stacked metadata.
2. For a stacked child, prove whether the declared `parent_dependency` is already satisfied by the current target.
   - If required parent-only commits/content are still absent from the target, direct child → target integration is forbidden.
   - Use only a legal path from `WORKSTREAMS.md#Legal stacked integration paths`: fold child into the parent, or integrate the parent first and then reconcile the child onto the resulting target.
3. Compare the current target with the target state against which the workstream was last reconciled/validated.
4. If the target moved materially, perform only the smallest authorized rebase/merge/retarget/reconciliation, then rerun affected verification and detect both textual and material semantic conflicts.
5. Decide final-integration review coverage **after** that refresh:
   - if exact covered workstream content/behavior and the acceptance surface are unchanged, an existing exact GREEN verdict/stronger coverage may remain valid after affected compatibility verification is GREEN;
   - if reconciliation materially changes the covered content/behavior or acceptance surface, prior coverage is stale: persist the new exact manifest `review.subject`, set REQUIRED/RECOMMENDED review to `pending`, persist reconciliation evidence and stop at the normal fresh-review boundary;
   - target movement or changed commit ancestry alone is not sufficient reason to invalidate review.
6. Immediately before the actual merge/integration, read the target again. If it moved after the comparison/review decision, loop through this gate again.

File overlap alone never blocks this gate. A real dependency, incompatible authority, unresolved semantic conflict or unreconcilable integration conflict does.

Do not perform an unauthorized live/deployment write while satisfying this Git integration gate.

## Publication / PR verification

Verify as applicable:
- correct base/head branches and current integration target;
- branch-isolated integration refresh is current for the target actually being merged;
- any stacked parent dependency is satisfied for this exact integration path;
- expected PR head/publication state is correct;
- PR/publication artifact matches accepted milestone state and cumulative handoff;
- commits after the reviewed implementation head are only authorized closure/publication changes;
- no unreviewed behavioral/scope drift after accepted subject;
- required status checks/mergeability understood;
- publication does not perform unauthorized live/deployment action.

Publication verification is lighter than substantive milestone acceptance. Re-run substantive tests only when new evidence gives concrete reason.

## Finalization

When milestone uses PR:
1. milestone acceptance GREEN;
2. open/update PR as appropriate;
3. verify actual PR artifact;
4. merge/finalize after required approval/checks;
5. reconcile Task Board to actual final state;
6. write/update cumulative handoff;
7. persist acceptance evidence;
8. record final implementation head/checkpoint;
9. set milestone `done`.

A small closure documentation commit is allowed when required.

### Branch-isolated workstream final integration

For a branch-isolated workstream:
- do not integrate until the refresh gate above is current and the manifest-owned final-integration review requirement is satisfied;
- integrate only into the manifest `integration_target`, or into the declared parent branch when intentionally using the legal child → parent path;
- when a child is folded into its parent, treat the parent's integrated subject as changed when the child adds covered behavior/content; the parent must perform its own refresh/review reconciliation before its later final integration;
- never record a child as independently integrated to main/default merely because it was merged into an unmerged parent;
- after final-target integration, reconcile durable manifest/result/PR state plus the selected Task Board/handoff as applicable to the actual Git result.

## Cumulative handoff

Canonical location: `project-handoffs/MXX_HANDOFF.md`.

Record minimum continuation truth:
- completed checkpoint/final implementation head;
- achieved state;
- authority now in force by exact refs;
- concise acceptance/review/external-readback results + evidence pointers;
- only material exceptions/deferred items;
- next durable starting point and explicit gate.

Do not turn handoff into a duplicate Task Board/history dump.

## Automatic next milestone

After GREEN/finalization, continue automatically when:
- next milestone already approved;
- prerequisite checkpoint satisfies dependencies;
- required/recommended review gates green;
- JIT prep derives deterministically from durable authority;
- no strategic decision unresolved;
- no explicit user/deployment/live-write authorization gate due.

Then:
1. reconcile Task Board/current milestone to the finalized checkpoint;
2. the close role is complete;
3. return to `workflow/chatgpt_only/ROUTER.md`;
4. let the router select execution preparation for the next approved milestone;
5. continue without requiring user “continue”.

Return strategic changes to the router for Planning / Project Definition / Research classification. Stop only for unresolved user/product authority, an explicit user/deployment/live-write authorization gate, a concrete runtime/access/input blocker, or end of approved scope. At a stop, use root `CHATGPT.md#Real-stop-response-contract`.
## System verification and cutover

Independent system verification acts as its own gate when required.

Deployment, cutover and migration should be runbook- or Task-Card-driven rather than improvised from chat.

Runbooks/checklists do not automatically require OpenSpec unless they change a behavior contract.

Explicit deployment/live-write authorization remains a hard stop.

