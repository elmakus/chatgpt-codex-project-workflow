# Codex-only Milestone Close / Publication / Workstream Integration

This module owns integrated milestone acceptance, publication verification, branch-isolated workstream integration, cumulative handoff and automatic next-milestone continuation.

## Entry condition

Enter through exactly one legal close shape.

### Normal milestone close

- required Cards for the milestone are done;
- required/recommended Card review gates are green;
- intended final milestone state exists.

### Qualified micro-fix workstream close

- the selected branch-isolated issue workstream has a completed Intake with `path: micro_fix`;
- manifest ↔ Task Board binding is valid;
- the one bounded fix Card is terminal with all required/recommended Card review gates GREEN;
- no higher-priority Task Board Research/RED/correction obligation remains;
- the selected workstream is not already `done`.

A qualified micro-fix does not need a Master Plan or milestone entry merely to enter Close.

If a Card/milestone review or manifest final-integration review is `pending | in_progress`, route to `REVIEW.md` first. A GREEN manifest final-integration review may proceed to Close subject to refresh-preservation checks; a null manifest final-integration review state is also not a blocker to entering Close because this role runs target refresh before first coverage reuse/freeze.

## Integrated milestone acceptance

This section applies only to the normal milestone-close path. A qualified micro-fix skips milestone acceptance because its bounded fix Card is the direct execution/acceptance contract; proceed to **Branch-isolated integration refresh gate**.

For a normal milestone, evaluate intended final milestone state against:
- approved milestone outcome/acceptance;
- applicable requirements/accepted decisions;
- integrated behavior;
- required tests;
- migration/rollback/data-integrity/security constraints;
- material external-state readback;
- relevant OpenSpec;
- required evidence.

If milestone acceptance itself requires/recommends independent review, Codex Main freezes the exact milestone subject as the next `pending` attempt and returns through the router for a qualifying independent Tester. The coordinator does not require a second normal-ChatGPT review boundary.

### RED

- milestone is not done;
- create/reopen bounded corrective work;
- persist failing evidence;
- continue immediately into deterministic remediation when legally bounded and unblocked;
- changed subject receives a new immutable independent-review attempt when required/recommended.

### GREEN

Proceed to publication/finalization.

## Branch-isolated integration refresh gate

Run this gate when the selected branch-isolated workstream is about to be integrated/published into another branch or its final `integration_target`.

A milestone checkpoint that remains on the same workstream branch and performs no cross-branch integration does not run this gate merely because milestone acceptance is GREEN.

Read the selected `WORKSTREAM.yaml` and apply `workflow/codex_only/WORKSTREAMS.md#Integration refresh contract`.

Required ordering:

1. Verify exact workstream branch/manifest identity, current integration target and stacked metadata.
2. For a stacked child, prove whether the declared `parent_dependency` is already satisfied by the current target.
   - If required parent-only commits/content are still absent from the target, direct child → target integration is forbidden.
   - Use only a legal path from `WORKSTREAMS.md#Legal stacked integration paths`: fold child into the parent, or integrate the parent first and then reconcile the child onto the resulting target.
3. Compare the current target with the target state against which the workstream was last reconciled/validated.
4. If the target moved materially, perform only the smallest authorized rebase/merge/retarget/reconciliation, then rerun affected verification and detect both textual and material semantic conflicts.
5. Decide final-integration review coverage **after** that refresh:
   - if `review.requirement: none` is legally allowed by current authority, no final-integration review lifecycle is activated;
   - if REQUIRED/RECOMMENDED review is already GREEN, preserve it only when exact covered workstream content/behavior and the whole acceptance surface remain unchanged and affected compatibility verification is GREEN;
   - if REQUIRED/RECOMMENDED review state is null, do exactly one of:
     - prove an already-independent stronger review covers the identical refreshed immutable integrated subject and whole workstream acceptance surface, then reconcile the distinct manifest gate GREEN with exact `covered_by` evidence; for a one-Card micro-fix apply `MICRO_FIX.md#Workstream-final-integration-review`; or
     - freeze the exact refreshed integrated subject in manifest `review.subject`, set `review.state: pending`, clear stale `covered_by`, persist refresh evidence, and return through the router to the formal independent-review obligation;
   - if reconciliation materially changes the covered content/behavior or acceptance surface, any prior coverage is stale: persist the new exact manifest `review.subject`, set REQUIRED/RECOMMENDED review to `pending`, clear stale `covered_by`, persist reconciliation evidence and return through the router to the formal independent-review obligation;
   - target movement or changed commit ancestry alone is not sufficient reason to invalidate review.

Any concrete production worker that performs behavioral reconciliation is part of the implementation-owner set for that changed subject and cannot serve as its Tester. Codex Main records only semantic ownership; `codex_workflow` realizes an independent Tester.
6. Immediately before the actual merge/integration, read the target again. If it moved after the comparison/review decision, loop through this gate again.

File overlap alone never blocks this gate. A real dependency, incompatible authority, unresolved semantic conflict or unreconcilable integration conflict does.

Do not perform an unauthorized live/deployment write while satisfying this Git integration gate.

## Publication / PR verification

Verify as applicable:
- correct base/head branches and current integration target;
- branch-isolated integration refresh is current for the target actually being merged;
- any stacked parent dependency is satisfied for this exact integration path;
- expected PR head/publication state is correct;
- PR/publication artifact matches the owning acceptance state: accepted milestone state + cumulative handoff for normal milestone close, or the qualified micro-fix bounded Card/workstream acceptance + evidence for micro-fix close;
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

A small Main-owned closure/bookkeeping commit is allowed when required when it does not change the accepted behavioral subject.

### Branch-isolated workstream final integration

For a branch-isolated workstream:
- do not integrate until the refresh gate above is current and the manifest-owned final-integration review requirement is satisfied;
- integrate only into the manifest `integration_target`, or into the declared parent branch when intentionally using the legal child → parent path;
- when a child is folded into its parent, treat the parent's integrated subject as changed when the child adds covered behavior/content; the parent must perform its own refresh/review reconciliation before its later final integration;
- never record a child as independently integrated to main/default merely because it was merged into an unmerged parent;
- after final-target integration, reconcile durable manifest/result/PR state plus the selected Task Board/handoff as applicable to the actual Git result;
- ensure the terminal namespaced workstream package is present on the final integration target and read it back before source-branch deletion; use a closure-only target-side commit/PR when actual merge-result metadata could not be known before merge;
- keep the original workstream branch in manifest/Task Board identity as provenance even after deletion; do not rewrite terminal workstream identity to the target branch.

## Qualified micro-fix finalization

For a qualified micro-fix, after the refresh gate is current, any REQUIRED/RECOMMENDED manifest final-integration review gate is GREEN, and the actual final-target integration succeeds:

1. verify the final integration result/readback against the exact target used by the refresh gate;
2. reconcile the selected manifest `status/result/pr` to the actual integrated result;
3. reconcile the selected Task Board execution/result pointers needed for recovery without creating a milestone entry;
4. keep the bounded fix Card terminal and preserve its independent review/evidence history;
5. do not synthesize an `MXX` cumulative handoff solely for the micro-fix unless project authority separately requires one; when one is required for a branch-isolated micro-fix, use that workstream's namespaced handoff location;
6. verify the target-side terminal durable package before deleting the source branch;
7. return to the router. If the micro-fix workstream scope is complete and no further deterministic obligation exists, this is end of approved scope.

## Cumulative handoff

Canonical location is state-context-specific:

- legacy/default single-workstream context → `project-handoffs/MXX_HANDOFF.md`;
- branch-isolated workstream → `implementation/workstreams/<workstream-id>/handoffs/MXX_HANDOFF.md`.

The selected canonical Task Board owns the exact milestone `handoff` pointer. Independent workstreams may therefore each have their own `M01`, `M02`, etc. without filename collision.

`PROJECT.md -> Latest cumulative handoff` is only the legacy/default-context convenience pointer. Branch-isolated Close MUST NOT update it; the workstream's Task Board is the locator for its latest applicable handoff.

Record minimum continuation truth:
- completed checkpoint/final implementation head;
- achieved state;
- authority now in force by exact refs;
- concise acceptance/review/external-readback results + evidence pointers;
- only material exceptions/deferred items;
- next durable starting point and explicit gate.

Do not turn handoff into a duplicate Task Board/history dump.

## Source-branch deletion gate

Deleting a completed branch-isolated workstream branch is allowed only after:
- final-target integration succeeded and exact result/readback is known;
- any closure-only target-side reconciliation is complete;
- manifest status/result/PR and selected Task Board terminal checkpoint/result/handoff pointers match the actual integration outcome;
- every unique referenced workstream-owned Card/evidence/handoff/blocker artifact needed for recovery exists on the final integration target;
- no Card, Research, review, stacked-dependency or integration obligation remains active.

Read back the target copy before deletion. If any required durable state exists only on the source branch, branch deletion is blocked until it is preserved on the target. After deletion, terminal recovery follows `WORKSTREAMS.md#Integrated-terminal-workstream` and MUST NOT require the deleted branch.

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
3. return to `workflow/codex_only/ROUTER.md`;
4. let the router select execution preparation for the next approved milestone;
5. continue without requiring user “continue”.

Return strategic changes to the router for Planning / Project Definition / Research classification. Stop only for unresolved user/product authority, an explicit user/deployment/live-write authorization gate, a concrete runtime/access/input blocker, or end of approved scope. At a real human-facing stop, use root `CHATGPT.md#Real-stop-response-contract` plus `workflow/common/USER_STOP.md`; formal Codex-managed review alone is not such a stop.
## System verification and cutover

Independent system verification acts as its own gate when required.

Deployment, cutover and migration should be runbook- or Task-Card-driven rather than improvised from chat.

Runbooks/checklists do not automatically require OpenSpec unless they change a behavior contract.

Explicit deployment/live-write authorization remains a hard stop.
