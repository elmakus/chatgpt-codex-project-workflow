# Brainstorming handoff — common-preexecution-core ready for Definition gate

Date: 2026-09-21
Workstream: `feature-common-preexecution-core`
Branch: `feat/common-preexecution-core`
Canonical exploratory authority: `brainstorming/COMMON_PREEXECUTION_CORE.md`
Cross-cutting audit: `brainstorming/CROSS_CUTTING_AUDIT_COMMON_PREEXECUTION_CORE.md`
Scope: `common-preexecution-core@R1`
Brainstorming status: `ready_for_definition`
Definition promotion authorization: `pending`
Definition promotion subject: `none`

## Brainstorming conclusion

The target V2 architecture is sufficiently resolved for formal Definition.

Chosen direction:
- one common semantic Project Workflow router/state machine;
- thin runtime/surface realization adapters only;
- no separate ChatGPT/Codex lifecycle schemas;
- one common branch-first workstream manifest;
- one common Task Board schema;
- capability-first independent-context realization;
- neutral `active_execution` for serial or concurrent execution;
- append-only review attempts for Card, milestone and workstream final-integration gates;
- semantic-only review evidence;
- mandatory authoritative-state refresh on new-context/takeover/recovery entry;
- expected-base/CAS publication;
- no stronger stale-coordinator lease/fencing primitive unless V2 evidence later requires one;
- no durable Codex runtime-policy binding in new V2 work;
- capability-first branch cleanup: direct deletion when available, optional `safe_to_delete` fallback when physical deletion is unavailable;
- runtime topology freedom preserved: capable one-shot orchestration and normal ChatGPT fresh-review boundaries remain valid realizations of the same common obligations.

## Evidence checkpoint

Live tests:
- F/G/H/I: cross-runtime execution/takeover matrix supports neutral execution-state direction;
- J: terminal GREEN review can be consumed later without replay;
- K: append-only RED -> repair -> re-review lifecycle works; V1 wrapper contamination exposed;
- L: authoritative-state refresh PASS;
- M: semantic-only independent-review evidence PASS;
- N-CAPABLE / N-CHATGPT: deliberately deferred until V2 exists and are retained as implementation validation scenarios.

Cross-cutting V1 audit covered:
- ROUTER;
- RECOVERY;
- WORKSTREAMS;
- CLOSE;
- active workstream/Task Board templates;
- branch-first/context-health/orchestration regression tests.

## V2 migration direction

1. Define common schemas/contracts without switching production routing.
2. Add bounded migration/readers for existing policy-local durable state.
3. Move semantic lifecycle modules into `workflow/common/*`.
4. Replace policy-local review/execution state with append-only review + `active_execution`.
5. Commonize Workstreams/Close/Recovery and branch cleanup capability fallback.
6. Switch bootstrap/routing to common semantics plus thin runtime/surface adapters.
7. Run the full V2 validation matrix, including deferred N.
8. Retire policy-local semantic copies only after parity is proven.

## Current real stop

Do not enter Project Definition automatically.

The next legal transition requires explicit user authorization to promote exact scope:

`common-preexecution-core@R1`

If authorized:
- persist `Definition promotion authorization: user_authorized`;
- persist `Definition promotion subject: common-preexecution-core@R1`;
- enter Project Definition.

If not authorized:
- remain in Brainstorming;
- optionally reopen Research/Brainstorming only if the user introduces a new material design question.

No production workflow module has been changed by this Brainstorming work.
