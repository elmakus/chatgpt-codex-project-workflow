# Project Workflow V2 — Final Brainstorming Reconciliation

Date: 2026-09-22
Scope: common-preexecution-core@R1
Status: ready_for_definition
Promotion: explicit user authorization required
Production authority: none

## Purpose

This record is the clean Brainstorming output for Project Definition.

It reconciles the accepted conclusions from the staged comparison/grilling of current ChatGPT-only and Codex-only workflows plus the V2 delivery/bootstrap design.

Historical exploratory records remain useful evidence, but where they conflict with this record, this record represents the later accepted Brainstorming direction.

## Product shape

Project Workflow V2 is a **new clean repository** and one product.

It has:
- one canonical semantic workflow tree at `workflow/`;
- no production `workflow/chatgpt_only/`;
- no production `workflow/codex_only/`;
- no production `workflow/legacy/`;
- no redundant `workflow/v2/` inside the already-V2 repository.

The current `chatgpt-codex-project-workflow` repository remains historical/development reference after V2 becomes production-ready.

## One semantic workflow, two delivery surfaces

### Normal ChatGPT

User-owned ChatGPT Project Instructions state that the project uses `project_workflow_v2` and point to the V2 GitHub repository.

ChatGPT:
- obtains workflow instructions from that repository;
- reads the common V2 bootstrap/router;
- reads the project's durable state;
- follows the same common workflow semantics as Codex.

### Codex

Codex uses the installed plugin:
- plugin namespace: `pw`;
- Skill: `project_workflow_v2`;
- explicit entry: `$pw:project_workflow_v2`.

The plugin directly bundles the same canonical `workflow/` tree from the V2 repository.

Codex reads workflow semantics from the installed package root, not from the remote workflow repository during ordinary operation.

The Skill/SessionStart hook are thin bootstrap surfaces only. They do not duplicate workflow semantics.

Repository-local provisioning/pinning/enabling of plugins/MCPs/Skills belongs to the external `newproject-skill`, not Project Workflow V2.

## Context-economy / progressive disclosure

Especially for Codex:

```text
thin Skill / ChatGPT bootstrap
-> small common router
-> exact current workflow module
-> exact durable project state
-> exact authority/evidence refs
```

Rules:
- router acts as the semantic index/reference selector;
- no duplicate Skill `references/` policy tree;
- do not preload all workflow stages;
- neighboring stage modules are unread by default;
- docs/templates/migration are trigger-only;
- durable artifacts carry exact authority/evidence refs to avoid broad project scans;
- `SKILL.md` has no arbitrary line-count target, but contains only robust bootstrap/location/recovery instructions and no duplicated stage logic.

## Durable project contract

V2 project durable state declares the common Project Workflow V2 contract, conceptually:

```yaml
project_workflow: v2
```

Exact syntax belongs to Definition.

Do not persist:
- `execution_policy: chatgpt_only | codex_only`;
- current runtime/product identity;
- model/session/worker identity;
- workflow-source path selecting GitHub versus plugin.

ChatGPT and Codex may continue the same workstream across durable boundaries without state conversion.

## Runtime boundary

Project Workflow owns:
- semantic obligations;
- accepted authority/scope;
- lifecycle/correctness;
- Task Card state;
- review subjects/verdict/evidence;
- recovery truth;
- integration/close safety.

Runtime owns:
- concrete worker/session/model identity;
- worker catalogs;
- delegation lifecycle;
- internal worker topology/concurrency;
- concrete execution workspace realization.

Runtime identity does not choose different Project Workflow semantics.

## Project-Card execution topology

Exactly one Project Workflow Card executes at a time per selected workstream.

V2 does **not** carry:
- multi-Card Project Workflow parallel execution;
- batch/lane scheduler state;
- `parallel_safe` / `write_scope` / `exclusive_resources` as concurrency scheduler metadata;
- universal `active_execution` wrapper;
- ordinary `returned`;
- `transfer_ready`.

Runtime-internal implementation may use zero, one or many subagents, sequentially or concurrently, provided that this does not create multiple active Project Workflow Cards or competing shared-state writers.

## Main/coordinator and workers

When qualifying implementation worker capability exists:
- Main delegates Card implementation;
- worker implements/tests and returns result/evidence;
- worker does not finalize shared Project Workflow state;
- Main validates, reconciles, persists project truth and routes onward.

If worker result is bad while Card contract remains valid:
- Card stays `in_progress`;
- delegate correction/re-execution;
- do not use `blocked` unless a real unresolved blocker exists.

Main may perform:
- deterministic Git/state bookkeeping;
- exact integration/cherry-pick/merge operations that require no implementation judgment;
- lightweight inspection/proof/readback.

Substantive implementation/debugging/testing is delegated when qualifying worker capability exists.

A runtime genuinely lacking delegated implementation capability may execute directly for portability.

## Research / diagnosis evidence model

V2 preserves and strengthens the V1 external-prior-art rule.

Research and diagnosis are **not** limited to official documentation or the project's current runtime/source.

Use the smallest evidence path sufficient for the exact question, but every Research/diagnosis performs a proportional prior-art check across relevant source classes. The check is always present; only its depth varies with the problem. Relevant source classes include, as applicable:
- official/upstream documentation and source;
- the project's actual code/runtime/configuration/evidence;
- upstream GitHub issues, discussions and public issue trackers;
- release notes/changelogs and known bug reports;
- practical community reports such as Reddit, technical forums, Q&A/discussion threads and other relevant public practitioner sources.

The purpose is not to copy an internet solution blindly. The agent should use external practice to:
- discover known failure modes and edge cases;
- find existing workarounds or established patterns;
- avoid reinventing already-solved mechanisms;
- compare the agent's proposed solution against how others handled the same or analogous problem;
- identify tradeoffs or compatibility concerns that local reasoning alone may miss.

Source weight remains explicit:
- primary/upstream evidence outranks anecdotal/community evidence when they conflict;
- community consensus/popularity is not itself authority;
- practical reports may reveal real-world behavior that official docs omit;
- materially conflicting evidence must be surfaced, not silently averaged away;
- anecdotal/community findings should be checked against stronger evidence when practical.

This is mandatory-but-proportional, not an exhaustive web crawl. A trivial/local problem may need only a very small prior-art check; a complex or ecosystem-sensitive problem may require a broader one. Stop when enough source-grounded evidence exists to answer the exact question and compare meaningful alternatives.

During adaptive Brainstorming, agent-findable facts remain agent-owned: use Research/prior-art investigation before asking the user to decide around facts that can be established independently.

## YAGNI / proportional design

V2 preserves the global V1 YAGNI invariant ("You Aren't Gonna Need It").

Prefer the least-complex solution that fully satisfies all current accepted requirements, decisions, constraints, invariants and verified evidence.

Do not add speculative:
- abstractions;
- generality/extensibility;
- configuration;
- dependencies/infrastructure;
- compatibility paths;
- future-proofing

solely for hypothetical future needs.

Every material increase in complexity needs a concrete current justification from accepted authority, verified evidence, an existing contract/constraint or demonstrated current reuse/variation.

YAGNI does **not** mean "fewest lines" and does not permit weakening current correctness, security, testing, maintainability/refactoring, compatibility, migration, observability or other applicable quality obligations.

Prefer an existing fitting mechanism when it cleanly satisfies current authority. New machinery is valid when current requirements/evidence justify it.

## Brainstorming interaction model

Adaptive grilling is the default method for **every V2 Brainstorming scope**.

No `#grill` command is required or supported as a separate active workflow mode.

When Brainstorming is active:
- discover the current decision frontier;
- ask only genuine user/product/strategic decisions;
- number material questions;
- include a recommendation for each;
- research agent-findable facts independently rather than asking the user;
- continue through thematic rounds while further questioning has meaningful expected decision value;
- perform a final challenge/discovery pass before declaring Brainstorming complete;
- allow the user to stop questioning explicitly at any time, while preserving unresolved material blockers.

A simple scope may complete after a short round; a complex scope may require many rounds. There is no fixed question/round quota.

### Intake interaction

`#feature` enters discovery/Brainstorming by default.

`#issue` is **diagnosis-first, discussion-before-implementation**.

The `#issue` directive authorizes diagnosis/intake, not automatic implementation. After enough read-only diagnosis exists to explain the problem and propose a repair direction, Project Workflow enters a mandatory short adaptive-Brainstorming alignment with the user **before any implementation mutation**.

This applies even when the issue appears to qualify as a micro-fix.

The first alignment round must present, at minimum:
- what the diagnosis/root cause currently appears to be;
- the proposed intended end state / repair behavior;
- material safety, compatibility or side-effect considerations that are already knowable;
- the assistant's recommended repair direction;
- the smallest genuine user decision needed before implementation.

There must be at least one user response after that diagnosis/proposal boundary. The original `#issue` message alone never authorizes implementation continuation.

If the user wants explanation, challenges safety, changes the desired outcome or exposes additional choices, continue adaptive grilling until the intended result is sufficiently agreed.

Only after that user alignment may Intake classify a direct micro-fix fast path when all of these are concretely true:
- root cause and intended behavior are concrete;
- the user has accepted/authorized the bounded repair direction after diagnosis;
- change is bounded and low strategic risk;
- no accepted requirement/architecture/product decision must change;
- acceptance can be stated directly;
- no substantial migration/deployment strategy is needed.

A qualified micro-fix may then bypass full Project Definition / Strategic Planning and route directly to Execution Prep, but it never bypasses the diagnosis + user-alignment Brainstorming boundary.

If diagnosis exposes material product/architecture decisions or meaningful alternative outcomes, the same adaptive Brainstorming simply continues rather than silently choosing a solution.

## Execution Prep

Execution Prep:
- materializes all currently well-defined useful Cards;
- may leave genuinely predecessor-dependent exact scope as JIT work;
- may create/split/merge/reorder/refine not-yet-started Cards inside accepted planning authority;
- does not invent strategic authority;
- allows multiple READY Cards but execution selects only one at a time;
- has no state between READY and `in_progress`.

Immediately before execution, current truth is refreshed/revalidated.

## Execution and recovery

Normal Card lifecycle remains simple:
- deterministic READY selection;
- persist `in_progress`;
- refresh current state/authority;
- execute/delegate;
- persist result/tests/evidence;
- run required review;
- finalize;
- return to router.

Recovery:
- reconstructs from durable state;
- checks whether an exact completed result already exists before rerunning;
- reuses/reconciles accepted durable work rather than repeating it;
- handles uncertain external effects through readback first;
- fails closed if an effect cannot safely be established rather than duplicating it.

No Context Health project mechanism exists in V2. Normal chat/runtime replacement relies on durable recovery.

## Independent implementation/final-integration review

Use one generic append-only exact-subject review-attempt model for Card/milestone/final-integration review.

Principles:
- REQUIRED and activated RECOMMENDED are blocking gates;
- independence is per exact subject;
- a context that materially produced/repaired the subject cannot independently review it;
- reviewer judges only and does not repair while acting reviewer;
- GREEN is durable and reusable when exact complete coverage remains valid;
- RED evidence remains immutable for the failed subject;
- corrected implementation creates a new subject/attempt;
- runtime reviewer identity/telemetry is non-canonical;
- review is proportional rather than automatic on every Card.

Normal behavior/code workstreams retain at least one independent final-integration review gate unless stronger exact coverage already satisfies it.

## Strategic Planning premium-model block

Strategic Planning is the highest-leverage reasoning phase and has deliberate human-facing model-selection boundaries.

### Premium stop A

After Project Definition is complete and before material Strategic Planning:
- hard stop;
- recommend the best currently available model;
- do not automatically begin Planning.

### Stage 5 — Strategic Planning

The best available model creates/materially revises the Master Plan.

Every new or materially revised Master Plan requires Independent Plan Review.

Only truly mechanical/editorial changes that do not alter strategy, milestone structure, requirement coverage or accepted gates may use no plan review.

### Premium stop B

After the exact Master Plan subject is durably frozen:
- hard stop;
- planner must not launch an internal subagent/worker to perform Stage-6 Plan Review;
- user moves to a fresh independent context using the best available model.

### Stage 6 — Independent Plan Review

Fresh best-model context performs independent review of the exact frozen plan.

### Premium stop C

After GREEN is durably consumed and the reviewed plan revision is approved:
- hard stop;
- tell the user the premium planning/review block is complete;
- recommend switching to a lighter/cheaper model;
- do not continue directly into Execution Prep from the premium review context.

Any later **material** re-entry into Strategic Planning repeats the full A -> Planning -> B -> Plan Review -> C block.

Qualified micro-fixes that legitimately bypass Master Planning also bypass the premium planning block, but only after the mandatory issue diagnosis + user-alignment Brainstorming boundary.

These premium boundaries outrank ordinary automatic continuation and survive Recovery.

Do not hard-code a current model product name into canonical workflow semantics. Use capability/tier-neutral language such as "best available model".

## Close / integration

Before final integration/publication:
- resolve exact workstream/target;
- refresh current target truth;
- satisfy stacked/parent topology;
- compare with last validated target baseline;
- reconcile the smallest authorized difference;
- rerun affected verification;
- decide independent review coverage only after refresh;
- reread target immediately before mutation when needed.

Target movement alone does not invalidate GREEN when:
- exact covered workstream content/behavior is unchanged;
- acceptance surface is unchanged;
- affected compatibility verification is GREEN.

Material behavior/content/acceptance change creates a new review subject.

Publication/external mutation uses:
`ACTION -> READBACK -> VERIFY EXPECTED STATE -> EVIDENCE`.

Deployment/live-write alone does **not** create a user authorization hard stop. Only an explicit accepted authorization gate does.

## Durable closure / branch cleanup

A workstream is not closed merely because code merged.

Before source-branch disappearance can be considered safe:
- preserve/read back sufficient target-side durable lifecycle/result/review evidence for recovery;
- ensure no live Card/Research/review/integration obligation still needs the source branch.

GitHub automatic branch deletion after merge is a valid cleanup realization:
- if exact branch is already absent, cleanup is complete;
- never recreate it for cleanup.

If a still-existing branch is proven safe and current capability can delete it:
- delete exact branch and verify absence.

If deletion is unavailable:
- retain only a minimal exact `safe_to_delete` fallback;
- later capable cleanup revalidates exact ref/head before deletion.

Deterministic closure-only lifecycle bookkeeping after merge does not create a new implementation/review subject if it cannot change accepted content/behavior.

Each milestone retains a minimal cumulative recovery checkpoint/handoff even when continuation is immediate.

## Router / automatic continuation

Default:
> Continue automatically whenever the next legal obligation is deterministic and already authorized.

Do not stop merely because:
- Intake ended;
- Research returned;
- a role/module ended;
- ordinary GREEN review completed;
- Card completed;
- milestone completed;
- Recovery succeeded.

Real human stops:
- unresolved user/product authority;
- explicit accepted authorization gate;
- concrete non-remediable access/runtime/input blocker;
- true end of approved scope;
- explicit user-requested stop;
- premium stops A/B/C.

At true end of approved scope:
- persist/report completion;
- do not invent another milestone/workstream;
- do not require a workflow "what next?" prompt.

## Delivery maintenance invariant

There is one semantic source:

```text
edit canonical Project Workflow V2 workflow/
-> commit/publish V2 repository
-> update installed Codex plugin
-> plugin now carries the same updated workflow/
```

Normal workflow semantic changes do not require parallel edits to Skill/hook/plugin policy.

Skill/hook/manifest changes occur only when bootstrap/package behavior itself changes.

The user already maintains plugin freshness operationally; V2 does not add workflow-version pinning machinery merely for this concern.

## Legacy migration boundary

Legacy V1 projects may receive bounded one-time migration tooling.

Migration:
- may read prior `execution_policy` and historical state as input;
- converts/project-reconciles into common V2 durable state;
- does not create permanent V1 semantic paths inside the new V2 `workflow/`.

Normal V2 routing never depends on legacy policy namespaces.

## Explicitly superseded exploration

The following prior Brainstorming directions are historical only and MUST NOT be promoted into Definition:
- Project Workflow multi-Card parallel execution;
- universal/multi-member `active_execution`;
- `prepared` / `transfer_ready` execution lifecycle;
- batch/lane/frozen-member scheduling;
- durable runtime/orchestration binding;
- durable `execution_policy: chatgpt_only | codex_only`;
- Project Workflow Context Health/FRESH lifecycle;
- product-specific reviewer/executor identities in canonical state;
- unconditional deployment/live-write user hard stop;
- planner-spawned internal Stage-6 Plan Review;
- permanent duplicated ChatGPT-only/Codex-only semantic trees;
- separate plugin-maintained semantic copy of Project Workflow.

## Completion / challenge audit

The accepted V2 direction is internally coherent at Brainstorming level:

- one semantic state machine;
- runtime-portable durable state;
- simple serial Project-Card lifecycle;
- runtime-owned internal subagent realization;
- delegated implementation where available;
- exact-subject independent review;
- premium top-model planning + independent plan-review block;
- automatic continuation outside real/premium stops;
- target-refresh/integration/readback safety;
- durable closure independent of source branch;
- one product delivered through GitHub to ChatGPT and through a thin plugin package to Codex;
- context-efficient progressive disclosure.

Counterfactual challenge results:
- preserving separate ChatGPT/Codex semantic workflows would recreate the duplication V2 is intended to remove;
- using runtime self-detection would be less reliable than bootstrap-owned instruction-source selection;
- preserving Project-Card parallel machinery would add substantial state after the user explicitly removed that requirement;
- duplicating workflow policy in the Skill would create a second product and consume Codex context;
- pinning every project to an exact workflow revision would add operational machinery the user does not currently need;
- skipping fresh top-model Plan Review would weaken the highest-leverage quality gate the user explicitly wants;
- replaying review merely because target SHA moved would add cost without a changed reviewed subject.

No unresolved material product/architecture choice remains in Brainstorming.

## Promotion gate

Brainstorming is **ready for Project Definition**, but not promoted.

Project Definition MUST NOT begin until the user explicitly authorizes promotion of this completed Brainstorming subject.

When promoted, Definition should use this record as the primary clean input and consult earlier records only for evidence/provenance, not to re-import superseded directions.
