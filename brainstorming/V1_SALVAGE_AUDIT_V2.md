# V1 Salvage Audit for Project Workflow V2

Date: 2026-09-22
Scope: common-preexecution-core@R1
Status: resolved
Production authority: none

## Purpose

Identify useful cross-cutting V1 mechanisms that were not the primary subject of the Stage 1-11 reconciliation, so V2 neither loses proven behavior nor blindly copies specialized machinery.

## Candidate 1 — one project = one repository

V1 invariant:
- project repository is durable project truth from exploration through implementation/close;
- a second planning/state/control repository is exceptional and requires a concrete technical reason + explicit user decision.

Recommendation: **retain in V2 core**.

This is semantic durability, not new-project provisioning. The external `newproject-skill` may create/provision repositories, but V2 should still define where project truth lives after creation.

## Candidate 2 — branch-first, manifest-bound workstreams

V1 proven behavior:
- one branch-isolated workstream per managed change;
- stable workstream identity;
- exact branch + durable manifest;
- workstream-local Task Board/evidence/handoffs;
- no correctness dependency on a mutable global workstream registry;
- stacked child only when it genuinely requires unmerged parent-only state;
- integration refresh against current target before final integration;
- terminal state survives source-branch deletion.

Recommendation: **retain in V2 core**, simplified using already accepted V2 serial-Card/runtime-neutral semantics.

This appears fundamental to durable recovery and safe multiple-workstream operation.

## Candidate 3 — selective OpenSpec / technical-contract freeze

V1 common OpenSpec is intentionally selective.

Normally useful for:
- behavior/API/schema/state contracts;
- retry/idempotency/reconciliation semantics;
- migrations;
- security-sensitive behavior;
- cross-package architecture;
- external side-effect semantics;
- complex changes where freezing a technical contract reduces ambiguity.

Normally skipped for:
- simple unambiguous bugs;
- docs/research;
- mechanical CI/refactors.

Recommendation: **retain as trigger-only optional module**, not as a normal-router preload and not as mandatory ceremony.

Resolved: V2 preserves the semantic mechanism as a selective, tool-neutral technical-contract module; OpenSpec is a supported realization when it adds material value beyond the Task Card.

## Candidate 4 — fork release versioning

V1 has a specialized downstream-fork release rule such as `vX.Y.Z-private.N` and lineage-aware baseline handling.

Recommendation: **do not make this generic V2 core semantics**.

Two reasonable options:
- retain it as a trigger-only optional module for projects durably declared as downstream forks; or
- move release-version policy to project-local authority/templates outside generic Project Workflow.

It should never load for ordinary non-fork work.

## Candidate 5 — locator-only fresh-context handoff UX

V1 has a strong human-facing contract:
- when a fresh ChatGPT context is genuinely required, provide a ready-to-copy `NEW CHAT START PROMPT`;
- prompt contains only project repo, exact branch/workstream, entry obligation and smallest durable pointer;
- durable repository state contains review scope/evidence/details;
- previous chat narrative is not required;
- named entry obligation is a locator, not a session-scope boundary;
- after the role completes, router continues until next real stop.

Recommendation: **retain in V2** for the intentional fresh-context boundaries:
- premium stop B -> Stage-6 fresh independent plan reviewer;
- any ChatGPT-surface implementation review that genuinely requires a fresh independent context because internal independent realization is unavailable;
- other explicit future fresh-context gates.

Remove only the obsolete Context Health handoff variant.

## Candidate 6 — external mutation readback

Already present in the V2 reconciliation, but confirm as retained:
- write/action success alone is insufficient when resulting state can be independently read back;
- use action -> readback -> expected-state verification -> evidence;
- uncertain interrupted side effect -> readback before retry.

Recommendation: retain in core.

## Candidate 7 — Task Card contract separate from mutable execution state

V1 distinguishes:
- stable Card = authority/scope/acceptance/tests;
- mutable Task Board = status/result/review/recovery state.

Recommendation: retain. It supports clean exact-subject review, JIT refinement and recovery without rewriting contracts just to mirror execution status.

## Candidate 8 — V1 mechanisms already intentionally discarded

Do not carry forward:
- `execution_policy: chatgpt_only | codex_only`;
- duplicated fixed-policy semantic trees;
- Context Health/FRESH lifecycle;
- Project-Card parallel batches/lanes/concurrency scheduler metadata;
- durable Codex orchestration binding/runtime identity;
- universal `active_execution` / `transfer_ready`;
- automatic `#issue -> repair` without user alignment;
- planner-spawned Stage-6 review;
- unconditional deployment/live-write authorization stop;
- separate plugin-maintained policy copy.

## Material decisions — resolved

1. Retain one-project-one-repository as a V2 invariant?
2. Retain branch-first manifest-bound workstreams as the normal managed-change model?
3. Retain selective OpenSpec explicitly, or generalize it to a tool-neutral optional technical-contract module?
4. Retain fork release versioning as trigger-only optional V2 module, or leave release versioning entirely project-local?
5. Retain locator-only ready-to-copy fresh-chat handoff UX at the explicit fresh-context gates?

Recommendations:
1. yes;
2. yes;
3. retain the semantic mechanism but make the core tool-neutral, with OpenSpec as an optional realization unless existing project compatibility argues for keeping the name;
4. trigger-only optional module;
5. yes.


## User decisions — salvage round

Accepted:
1. retain **one project = one repository** as a V2 invariant;
2. retain **branch-first, manifest-bound workstreams** as the normal managed-change model;
4. retain **fork release versioning** as a trigger-only optional V2 module for projects durably declared as downstream forks;
5. retain **locator-only ready-to-copy fresh-chat handoff UX** at explicit fresh-context gates; remove only obsolete Context Health handoff behavior.

Accepted:
3. Preserve the technical-contract/OpenSpec mechanism **selectively**: every implementation change gets an explicit bounded Task Card/fix contract; a separate OpenSpec-style artifact is created only when it adds material behavior/design-contract value beyond that Card. This is the chosen recommendation because mandatory duplicate OpenSpec for trivial fixes would violate YAGNI/context economy. Core semantics should remain tool-neutral enough that OpenSpec is a supported realization rather than a second authority layer.

## New V2 repository

The user created the new production-target repository:

`elmakus/project_workflow_v2`

Verified via GitHub on 2026-09-22:
- repository exists;
- visibility: private;
- default branch: `main`;
- repository is currently empty.

Do not populate it until the active V1-hosted Brainstorming/Definition/Planning authority reaches the legal execution boundary.


## GitHub Issue tracker decision

For GitHub-hosted managed projects with Issues capability:
- `#issue` and `#feature` create or recover an official GitHub Issue tracker after duplicate/recovery checks;
- tracker creation is bookkeeping, not implementation authorization;
- tracker may begin with reported symptom/feature goal and be refined as diagnosis/Brainstorming settles target behavior;
- workstream durable state stores the exact tracker reference;
- intermediate PRs do not close the issue unless they complete the whole accepted scope;
- final default-branch integration PR uses a closing keyword such as `Closes #N` / `Fixes #N` when appropriate;
- Close verifies issue state after merge and may explicitly close only after accepted scope is durably complete when auto-close is unavailable/disabled.

Applies analogously to both `#issue` and `#feature`.


## Completion

All salvage decisions are resolved. The authoritative disposition summary is `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md`.
