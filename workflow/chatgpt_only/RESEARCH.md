# ChatGPT-only Research

This module applies only after root routing has selected `execution_policy: chatgpt_only`.

## Goal

Produce source-grounded findings without conflating evidence with accepted intent, while making every cross-session Research continuation exactly recoverable.

## Durable record contract

Any Research obligation that may cross a role/session boundary must have one exact durable record **before** its origin role yields.

The record owns:

- `Research ID: <stable-id>`;
- `Status: active | blocked | complete | consumed`;
- `Origin role: brainstorming | project_definition | strategic_planning | plan_review | execution_prep | execution_resolution | other`;
- `Origin subject: <exact durable subject>`;
- `Return target: <exact role:subject>`;
- `Research question: <exact question>`;
- `Return reconciliation: pending | applied`;
- `Return reconciliation result: <exact durable result ref(s) | none>`.

New obligations start with `Status: active`, `Return reconciliation: pending`, and `Return reconciliation result: none`.

The shared `templates/RESEARCH.md` may be used for evidence structure, but this policy-local module exclusively owns ChatGPT-only continuation/routing semantics.

## Pointer ownership

Pre-execution Brainstorming / Project Definition / Strategic Planning / plan-review Research uses:

`PROJECT.md → Active research obligation`.

Execution Prep / implementation / recovery Research uses:

selected canonical Task Board → `research_obligation` (branch-isolated manifest-selected board, or legacy/default `implementation/TASK_BOARD.yaml`).

Never mirror an implementation/recovery Research obligation into `PROJECT.md`.

When the evidence gap originates from a branch-isolated workstream final-integration RED review, the RED review state remains manifest-owned but the Research continuation pointer still belongs only to that same workstream's validated selected Task Board. The Research record Origin subject must identify the exact manifest review subject/evidence. Never place that continuation in the default board or another workstream's board.

Keep the owning pointer through `Status: complete`. Normally clear it only after final-target reconciliation is durable and the record is `consumed`. The sole exception is the classifier-to-Research chain transition below: it consumes the completed classifier record and replaces the pointer with the next exact active Research record in one durable Git transition, so recovery never observes a gap or an unowned completed record.

## Status semantics

- `active` — Research is current.
- `blocked` — Research is current but concretely blocked.
- `complete` — findings are durable and the exact Return target owns continuation.
- `consumed` — final-target reconciliation is durable and the pointer may be cleared, or the classifier-to-Research chain transition has durably handed ownership to the next exact Research record.

Research cannot choose a different Return target from chat history.

## Final Return-target protocol

Every final owning Return target — Brainstorming, Project Definition, Strategic Planning, Execution Prep or Execution — MUST use this protocol.

1. Verify the owning pointer identifies the exact `complete` record and Origin/Return subjects match current durable state.
2. Read `Return reconciliation`.
3. If it is `applied`, verify `Return reconciliation result` still names the exact durable target result. Do **not** repeat target work. Perform only missing `Status: consumed` + pointer clear.
4. If it is `pending`, recover current target state first and perform only the required target-specific reconciliation.
5. In the **same durable Git transition** as the target mutation, set `Return reconciliation: applied` and `Return reconciliation result: <exact durable result ref(s)>`. Any new REQUIRED/RECOMMENDED pending review subject created by that reconciliation is part of this same durable result.
6. Only after the applied transition is durable, set `Status: consumed` and clear the owning pointer. This may be the same or a later safe commit.
7. A crash after step 5 but before step 6 is consume/clear-only recovery and must never replay target work.
8. Return through the router after consumption.

A stale `complete` pointer must never create another semantic revision, Definition mutation, exploratory update, Card reshape or review boundary after reconciliation was already applied.

## Intermediate execution-resolution classifier

`execution_resolution:<subject>` is not a final Return target.

It verifies Task Board pointer + subject and classifies findings. For an ordinary classification, it replaces `Return target` with the exact final owner and keeps `Status: complete`, `Return reconciliation: pending` and the Task Board pointer.

If classification itself proves more Research is needed, use this **classifier-to-Research chain transition** instead of pretending that a final owner already exists:
1. define the next exact Research record `R2` with a new stable Research ID, `Status: active`, `Origin role: execution_resolution`, the same exact affected durable subject as Origin, the exact next research question, `Return target: execution_resolution:<same affected subject>`, `Return reconciliation: pending`, and no reconciliation result yet;
2. in one durable Git transition, set the completed classifier record `R1` to `Return reconciliation: applied`, set `Return reconciliation result` to the exact `R2` record/pointer ref, set `R1 Status: consumed`, create `R2`, and replace Task Board `research_obligation` from `R1` to `R2`;
3. do not clear the pointer to `null` between records and do not leave `R1 complete` after the pointer has moved;
4. after that transition, route to Research for `R2`.

This is the only non-final-target consumption exception. The durable classifier result is the exact next Research obligation itself. A crash before the transition sees `R1 complete` and retries classification; a crash after it sees `R2 active` and must not recreate `R2`.

## Chained Research

Do not overwrite an active/complete pointer with a new question.

When a final target needs another Research obligation, reconcile the current findings first, then in one repository transition record the old reconciliation result, mark the old record consumed, create the next exact active record and replace the owning pointer. When `execution_resolution` itself needs more evidence before it can name a final owner, use the classifier-to-Research chain transition above. Recovery must always see either the old obligation or the new one.

## Authority boundary

Research is evidence, not accepted requirement/decision/plan authority.

If findings alter accepted product/system intent, route to Project Definition. If Definition remains valid and only execution strategy changes, route to Strategic Planning. Implementation-time facts inside accepted authority may flow to the current Card/OpenSpec/evidence.
