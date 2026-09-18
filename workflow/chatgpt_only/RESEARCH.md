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

`implementation/TASK_BOARD.yaml → research_obligation`.

Never mirror an implementation/recovery Research obligation into `PROJECT.md`.

Keep the owning pointer through `Status: complete`. Clear it only after final-target reconciliation is durable and the record is `consumed`.

## Status semantics

- `active` — Research is current.
- `blocked` — Research is current but concretely blocked.
- `complete` — findings are durable and the exact Return target owns continuation.
- `consumed` — final-target reconciliation is durable and the pointer may be cleared.

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

It verifies Task Board pointer + subject, classifies findings, replaces `Return target` with the exact final owner, and keeps `Status: complete`, `Return reconciliation: pending` and the Task Board pointer.

If classification itself proves more Research is needed, atomically retire the completed record and install one exact next `active` implementation-owned Research record/pointer. Never leave a gap.

## Chained Research

Do not overwrite an active/complete pointer with a new question.

When a final target needs another Research obligation, reconcile the current findings first, then in one repository transition record the old reconciliation result, mark the old record consumed, create the next exact active record and replace the owning pointer. Recovery must always see either the old obligation or the new one.

## Authority boundary

Research is evidence, not accepted requirement/decision/plan authority.

If findings alter accepted product/system intent, route to Project Definition. If Definition remains valid and only execution strategy changes, route to Strategic Planning. Implementation-time facts inside accepted authority may flow to the current Card/OpenSpec/evidence.
