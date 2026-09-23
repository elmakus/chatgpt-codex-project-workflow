# M06 V1 -> V2 bounded migration technical contract

Status: accepted JIT technical contract for approved `PWV2-P2 / M06`.

## Supported source classes

Only these real V1-derived classes are recognized:

1. `chatgpt_workstream_yaml_v1` — branch-isolated `WORKSTREAM.yaml` + `TASK_BOARD.yaml`, represented by `feature-common-preexecution-core` before V2 custody transfer.
2. `codex_workstream_yaml_v1` — branch-isolated `WORKSTREAM.yaml` + `TASK_BOARD.yaml`, represented by `feature-codex-only-policy` on V1 `main`.
3. `legacy_root_yaml_v1` — historical root `implementation/TASK_BOARD.yaml` without a selected branch-local manifest, represented by current V1 `main`; this may contain mixed historical policy-owned milestones/cards.

Anything outside the finite field/status shapes exercised by these classes is unsupported and fails closed. Migration input is read-only; source repo/ref/commit/blob identity is retained as provenance.

## Dry-run contract

Dry run:
- performs no source or destination mutation;
- validates exact source identity and source-class shape;
- emits deterministic destination paths, normalized V2 owner mapping, outstanding obligations, review disposition and explicit blocked reasons;
- rejects unknown schema/fields that can affect semantics, ambiguous authorization/subject, source racing against the supplied identity, unresolved external effects and more than one active/in-progress Project Card;
- never selects a winner from concurrent V1 Cards;
- never treats historical root state as a V2 live destination.

## Semantic mapping

- workstream identity, branch, base/created-from, parent/dependency/integration provenance and accepted authority are preserved when exact;
- stable Card scope/contracts remain locators; mutable status/result/review state maps into the V2 Task Board/append-only review-attempt owners;
- V1 completed results remain results to reconcile, never a new workflow state;
- accepted result/evidence pointers are preserved as source provenance and normalized result records when exact;
- a V1 review verdict is reusable only when exact immutable subject plus semantic independence can be proven. Otherwise a terminal V1 verdict is not invented/reused: conversion creates a pending V2 review obligation and retains the old verdict as provenance;
- pending/RED review history remains durable and ordered;
- unresolved Research/premium authorization/external-effect obligations remain outstanding obligations;
- V1 scheduler/runtime/policy fields (`execution_policy`, runtime/model/session/worker identity, batch/lane/scheduler, `active_execution`, `returned`, `transfer_ready`) are never copied into canonical V2 state;
- removal of scheduler fields is legal only after source concurrency is already quiesced/serialized; migration itself never performs that choice.

## Destination and provenance

Generated live V2 state is limited to the common V2 schema (`WORKSTREAM.toml`, `TASK_BOARD.toml`, workstream-local results/reviews/evidence locators as applicable).

Read-only migration provenance is kept outside normal semantic routes under the destination workstream's `migration/` directory. Ordinary V2 routing never loads V1 readers or migration provenance.

## Apply / idempotency / recovery

Apply requires all of:
- a GREEN dry-run for the exact source identity;
- explicit migration/adoption authorization supplied to the apply operation;
- a destination that is absent or already bound to the identical migration record.

Apply uses a staging directory plus exact migration record/readback before activation. The destination is promoted atomically only after generated state validates. Repeated apply with the same source fingerprint and output fingerprint is a verified no-op. A different source or destination fingerprint conflicts and fails closed.

Crash/restart must be safe at least:
- before record creation;
- after record creation but before destination promotion;
- after promotion before caller acknowledgement;
- during external-effect reconciliation.

An interrupted external effect is read back before retry; unknown occurrence blocks. Unactivated staged output may be rolled back without rewriting source or published history. Activated destination history is forward-repaired, never silently rewritten.

## Rehearsal boundary

M06 applies only to disposable cloned fixtures. Real-project migration remains optional here and requires its own explicit authorization. Production adoption/cutover remains M07-gated.

No permanent V1 interpreter, dual-write compatibility layer, remote migration service or legacy semantic route is added to canonical `workflow/`.
