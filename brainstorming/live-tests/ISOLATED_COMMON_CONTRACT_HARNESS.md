# Isolated common-contract live-test harness

Status: experimental Brainstorming support only
Scope: common-preexecution-core@R1
Production authority: none

## Purpose

This harness isolates capability-first live tests of the proposed common Project Workflow contract from the currently active fixed-policy workflow implementation.

It does not modify or supersede production workflow modules. It applies only when an exact live-test record explicitly opts into this harness.

## Authority boundary

For an opted-in experiment:

1. Current Project Workflow `main` remains authoritative for safe repository/bootstrap mechanics, Git integrity, branch ownership, durable writes and explicit STOP handling.
2. The exact durable live-test record is the semantic authority for the tested obligation.
3. If `workflow/chatgpt_only/*` or `workflow/codex_only/*` conflicts with the experiment record about product identity, worker/role names, state shape, realization mechanics or obligation routing, the exact live-test record wins only inside that experiment.
4. Do not import fixed-policy product/worker/session/model/worktree terminology into experiment state or evidence unless the live-test record explicitly requires it.
5. Repository/project safety rules remain in force. Experimental authority never permits mutation outside the paths explicitly authorized by the live-test record.

## Entry / recovery precondition

Before selecting the legal experiment phase in a new context, takeover or recovery entry:

1. resolve the exact repository, workstream and authoritative branch/ref named by the experiment;
2. refresh the authoritative durable source;
3. establish the exact current authoritative head;
4. reconcile or validate any local checkout against that head;
5. read the experiment record from authoritative durable state;
6. only then select the legal obligation.

A fresh chat/context is not proof of fresh repository state.

If local state is behind or diverged:
- do not execute a phase implied only by stale local state;
- preserve unresolved owned local work when it exists and reconcile it first;
- fail closed when safe reconciliation cannot be proven.

## Publication / race rule

Every mutable experiment transition is published from the exact durable base the actor actually routed from.

If publication loses a race:
- refresh authoritative state;
- reread the exact experiment record;
- reroute from the new durable state;
- never blindly retry the stale phase.

A failed write caused by concurrent advancement is not evidence that the stale phase was legal.

## Runtime-neutral evidence rule

Canonical Project Workflow experiment state/evidence may persist semantic facts required for recovery or correctness, including:
- exact immutable subject/ref;
- whether independence was semantically satisfied;
- whether the reviewer materially produced/repaired the subject;
- whether review was read-only;
- exact authoritative/local Git refs when those refs are themselves part of the tested correctness property.

Canonical evidence MUST NOT persist concrete product, worker-role, model, session, invocation or worktree identity merely to prove independence or realization.

Runtime-owned diagnostic logs may contain such telemetry, but it is not canonical Project Workflow authority.

## STOP rule

The exact live-test record owns its experiment-specific STOP boundaries. A STOP exists for observability of the experiment and does not imply that production routing must stop at the analogous state.

## Reusable prompt prefix

Use current Project Workflow only for safe repository/bootstrap mechanics.

This is an isolated live test of the proposed common contract. For the tested obligation, the exact durable live-test record is the authoritative semantic contract and overrides conflicting `workflow/chatgpt_only/*` or `workflow/codex_only/*` semantics only inside this experiment. Do not import product/worker names, state shape or realization behavior unless the live-test record requires them.

Before routing, refresh the exact authoritative branch/ref, establish its current head, reconcile/validate local state against it, and then read the durable experiment record. If a publication race is lost, refresh and reroute; do not blindly retry the stale phase.
