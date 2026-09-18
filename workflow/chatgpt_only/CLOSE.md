# ChatGPT-only Milestone Close / Publication

This module owns integrated milestone acceptance, publication verification, cumulative handoff and automatic next-milestone continuation.

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

## Publication / PR verification

Verify as applicable:
- correct base/head branches;
- PR/publication artifact matches accepted milestone state;
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
1. update Task Board/current milestone;
2. load `EXECUTION_PREP.md`;
3. prepare next deterministic Card(s);
4. run fresh Refresh Gate;
5. execute without requiring user “continue”.

Stop only for real strategic/user/authorization/runtime blocker or end of approved scope.
