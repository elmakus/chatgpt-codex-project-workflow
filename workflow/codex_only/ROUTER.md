# Codex-only Router

This router applies only after root `workflow/CONTEXT_ROUTING.md` selects project `execution_policy: codex_only`.

Once here, stay inside:
- `workflow/common/*` for genuinely policy-neutral rules;
- `workflow/codex_only/*` for Intake/Brainstorming/Research/Definition plus planning/execution/review/state/recovery.

Do not load legacy/shared execution trees or another policy directory.

## Bootstrap

1. Read `workflow/common/AUTHORITY.md` and project root `PROJECT.md`.
2. An explicit current `#issue` / `#feature` operator directive routes to `INTAKE.md` before unrelated mutable execution state.

An intentional current `#grill` directive is **not** Intake and does not receive new-workstream operator-directive precedence. Resolve normal workstream/exploratory state first. Only the Brainstorming route may consume `#grill`, and only for an already active Brainstorming scope; it must not create or recover a workstream or exploratory scope.

3. Clear natural-language authorization for a **new managed repository change** (for example implement/apply/adopt repository or project changes) routes to `INTAKE.md` before any change-specific durable write when the request is not already an exact continuation/handoff of an existing workstream/PR/manifest. Read-only inspect/compare/analyze requests remain branch-free. Generic intake uses neutral `kind: change`; do not guess `issue` versus `feature`.
4. Otherwise resolve an explicitly/current-branch selected branch-isolated workstream through `WORKSTREAMS.md`; validate manifest identity before trusting its Task Board.
5. Resume `intake.state: active` before later work. A completed `micro_fix` Intake with no Task Board routes directly to Execution Prep + `MICRO_FIX.md`.
6. When implementation/review/recovery state exists, resolve exactly one canonical branch-isolated Task Board. Branch-isolated binding mismatch is Recovery. If only historical root/default state exists, treat it as recovery/migration input and route to Recovery before further managed-change mutation; do not use it as a normal mutable fallback.
7. Resolve the current Card/milestone review attempt from the selected Task Board's `review.current_attempt`. An integrated member of the exact unresolved `parallel.current_batch` may have only a frozen `pending` attempt; that attempt is deferred until batch closure. Any `in_progress | red | green` verdict on such an unresolved member is inconsistent and routes to Recovery.
8. Historical root `PROJECT.md` exploratory/Research pointers without an exact migrated workstream are recovery/migration input only and route to Recovery before further managed mutation.
9. Then route the highest applicable obligation:
   - inconsistent durable state -> Recovery;
   - non-deferred REQUIRED/RECOMMENDED current review attempt `pending | in_progress` -> Independent review;
   - Task Board `research_obligation` `active | blocked` -> Research; `complete` -> exact Return target;
   - non-deferred current review attempt `red` -> RED corrective classification in `REVIEW.md`;
   - `in_progress` Card whose current attempt is `green` -> Execution post-review finalization;
   - exact current M03 batch `prepared | running | integrating | blocked` or member `returned` -> Execution/Recovery for that batch before deferred member review;
   - other existing `in_progress | blocked` Card -> Execution/Recovery;
   - selected manifest final-integration review `pending | in_progress | red` -> Review/corrective handling;
   - selected branch-isolated workstream intentionally terminal without final integration/merge, with terminal closure/delete unfinished -> Close/Recovery using exact manifest branch + target-side closure history;
   - terminal qualified micro-fix in unfinished workstream -> Close;
   - selected manifest `routing.research_obligation` -> validate exact pre-execution Research record; `active | blocked` routes to Research and `complete` routes to its exact Return target; consumed/stale contradiction routes to Recovery until reconciliation is verified;
   - conflicting Task Board `research_obligation` and manifest `routing.research_obligation` active/blocked/complete obligations -> Recovery; implementation/recovery Research is Task-Board-owned and pre-execution Research is manifest-owned;
   - selected manifest `routing.plan_review` -> validate the exact plan-review record; `pending | in_progress` routes to Independent plan review, while `green | red` routes to Planning for deterministic verdict consumption/correction; explicit fresh-session locator mismatch is Recovery;
   - selected manifest `routing.exploratory_scope` with no higher obligation -> validate/read the exact exploratory record and route to Brainstorming/promotion or Project Definition according to the exact durable promotion state;
   - deterministic READY set -> Execution Prep; M03 JIT may freeze one finite compatible batch, otherwise serial Execution;
   - milestone/workstream Close when prerequisites hold;
   - Planning/Definition/Research when accepted authority requires it.
10. After a current batch closes, its frozen member reviews are no longer deferred. Drain review/finalization/correction in canonical Task Board order before unrelated implementation.
11. Read only the chosen route's required artifacts and exact authority slice.
12. Continue deterministic authorized role transitions until a real strategic/product decision, explicit live/deployment authorization, concrete unremediable runtime/input blocker, context-hygiene boundary, or end of approved scope.

Fixed `codex_only` never changes execution policy because a runtime realization or concurrency path is unavailable. Runtime loss is recovered/resumed/replaced from durable project state; unsafe parallelism falls back to serial execution when the Card remains executable.

## Fresh-session entry semantics

A fresh-session handoff target is a **recovery/entry locator only**. It identifies the first obligation to recover; it does not narrow the approved project scope to one role, one verdict, one Card or one milestone.

After the located obligation completes:
- persist its durable result/state;
- return to this router;
- continue all deterministic authorized role transitions under the normal protocol below;
- stop only when durable state reaches a real workflow boundary.

Do not interpret wording such as `Kontynuuj`, `Punkt wejścia`, a review target, a Card ID or a milestone ID as an implicit instruction to reply immediately after that obligation. Only explicit user/project authority can deliberately narrow the approved scope.

## Role-transition protocol

A route module owns only its current role.

When that role finishes:
1. persist the durable state/evidence produced by the role;
2. re-evaluate the applicable durable state (plan-review record, selected Task Board and selected manifest review state as applicable) + accepted authority;
3. return to this router;
4. if durable state/current phase already owns a real stop — including a root `CHATGPT.md#Real-stop-response-contract` boundary or the `codex_only` Brainstorming → Project Definition promotion gate below — handle that stop first and do not run a separate hygiene handoff;
5. only when a deterministic authorized next role exists, perform the context-health trigger check below;
6. select the next legal route;
7. load that route's module(s);
8. continue in the same coordinating context without a user-facing stop when context health remains CONTINUE.

The same coordinating context may therefore move across deterministic role transitions when no real boundary intervenes, for example:

```text
PROJECT DEFINITION → PLANNING → EXECUTION_PREP → EXECUTION
PLAN_REVIEW → PLANNING → EXECUTION_PREP → EXECUTION
REVIEW → EXECUTION_PREP → EXECUTION → CLOSE → EXECUTION_PREP → EXECUTION
```

The first line begins only after Project Definition has been legally entered. For a new exploratory `codex_only` scope, Brainstorming/Research cannot enter Project Definition until the user-owned promotion gate below is satisfied. Once Definition is entered, `Definition Complete = GREEN → Planning` remains deterministic. When Planning creates a REQUIRED/RECOMMENDED independent plan-review gate, Codex Main freezes the exact plan subject and routes to `PLAN_REVIEW`; `codex_workflow` realizes an independent Tester. A qualifying verdict returns to this router without a mandatory normal-ChatGPT stop.

Role identity is per obligation, not permanent for the whole chat.

A Tester that completed its verdict has completed that review role. If the same concrete worker later contributes production to a changed subject, it joins that subject's implementation-owner set and cannot independently review that exact subject.

Only a real boundary from root `CHATGPT.md#Real-stop-response-contract` or an explicit policy-specific boundary defined by this router ends the turn.

## Brainstorming → Project Definition promotion gate

Under `codex_only`, the first transition from exploratory Brainstorming into Project Definition for a definition scope is **user-owned**.

Brainstorming may reach `ready_for_definition`, but that state is only a recommendation that formalization is now possible. It is not permission to start Definition.

The active exploratory scope is discovered from the selected workstream manifest `routing.exploratory_scope`. That locator identifies the exact brainstorming record used for recovery and MUST pass `WORKSTREAMS.md` locator validation before use. The record carries a stable `Scope ID`, `Revision`, and `Definition promotion subject`; the manifest does not mirror those fields.

Before entering Project Definition from an exploratory Brainstorming/Research path, require one of:
- an explicit current user instruction to promote the current scope into Project Definition; or
- durable `Definition promotion authorization: user_authorized` in the manifest-pointed brainstorming record, with `Definition promotion subject` exactly matching that record's current `<scope-id>@<revision>`.

A durable `user_authorized` value without an exact matching promotion subject is stale/insufficient and must not authorize Definition.

Examples of sufficient user intent include “przejdź do Definition”, “formalizuj wymagania/decyzje”, or another unambiguous instruction to leave exploration and begin Project Definition. Mere agreement with an individual idea, answering a brainstorming question, or asking for more research is not phase-promotion authority.

When Brainstorming is ready but promotion is not authorized:
1. persist the useful brainstorming state;
2. ensure selected manifest `routing.exploratory_scope` points to that exact record;
3. set `Status: ready_for_definition`, `Definition promotion authorization: pending`, and `Definition promotion subject: none`;
4. do **not** enter Project Definition or Planning;
5. treat this as a policy-specific real user stop;
6. use `workflow/common/USER_STOP.md` and ask only whether to continue brainstorming/research or promote the current scope into Project Definition.

When the user explicitly authorizes promotion:
1. ensure the current exploratory record and its selected-manifest `routing.exploratory_scope` locator are persisted;
2. persist `Definition promotion authorization: user_authorized` plus `Definition promotion subject: <scope-id>@<revision>` before entering Definition;
3. route to Project Definition;
4. continue normally from there.

If substantive exploratory scope changes after authorization but before Definition begins, increment/change the brainstorming revision and reset authorization to `pending` with promotion subject `none`. Never carry authorization across a materially changed revision.

Research completion does not bypass this gate. If Research was entered from an unpromoted exploratory scope, return to Brainstorming/promotion handling rather than entering Definition automatically.

The authorization applies only to the exact promoted scope/revision. Once Definition has begun, keep the active exploratory pointer/record available so bounded Research ↔ Definition recovery for that same promoted subject does not require repeated authorization. If Definition deliberately returns to open-ended Brainstorming because the product/problem space has materially reopened, create a new brainstorming revision (or a new scope when appropriate) and reset authorization to `pending` with promotion subject `none`.

When Definition Complete becomes GREEN, the exploratory promotion obligation is complete. Clear selected manifest `routing.exploratory_scope` only after the Definition result is durable and the locator no longer represents active exploratory/Definition recovery, then continue to Planning.

This gate does **not** apply to `Definition Complete = GREEN → Planning`; that transition remains deterministic and automatic when planning is in scope.

## Context-health trigger check

Do not load context-health machinery after every role by default.

Before starting the next substantial obligation at a safe durable boundary, ask whether the accumulated chat may now materially increase the risk of stale-state carryover, authority confusion or omission.

If there is no concrete signal, continue without loading another module.

If there is a concrete signal — for example materially superseded state in the transcript, major role/authority-area transition, large irrelevant diagnostic/tool history, or uncertainty reconstructing current truth from the conversation — read:

`workflow/codex_only/CONTEXT_HEALTH.md`

Then obey its decision:
- `CONTEXT_HEALTH: CONTINUE` → select/load the next route now;
- `CONTEXT_HEALTH: FRESH` → do not start the next obligation; perform the context-hygiene user stop.

Never use coordinator context hygiene as a substitute for formal independent review. Tester context/resume/replacement is runtime-owned; coordinator hygiene is evaluated only at a safe durable project boundary.

## Research return ownership and crash recovery

For any `complete` Research record, the exact current `Return target` owns continuation and the owning pointer remains until durable consumption.

- `execution_resolution:<subject>` is the only intermediate classifier. Ordinarily it refines the exact final Return target while keeping `Status: complete`, `Return reconciliation: pending`, and the Task Board pointer. If classification itself requires more evidence, it instead uses the explicit classifier-to-Research chain transition in `RESEARCH.md`.
- Every final target — Brainstorming, Project Definition, Strategic Planning, Execution Prep or Execution — MUST follow `workflow/codex_only/RESEARCH.md#Final Return-target protocol`.
- Final target mutation and `Return reconciliation: applied` + exact result refs are persisted in the same durable Git transition.
- If a crash occurs after that transition but before `consumed`/pointer-clear, re-entry is consume/clear-only; target work must not be replayed.
- Normally only the final owning Return target consumes/clears. The sole exception is classifier-to-Research chaining, where `execution_resolution` atomically records `R1` reconciliation as the exact new `R2` obligation, consumes `R1`, creates `R2 active`, and switches the Task Board pointer in the same durable Git transition.

Research never selects a different route by itself; only the authorized classifier may refine a Return target.

## Routes

### Intake

Read:
- `workflow/codex_only/INTAKE.md`;
- `workflow/codex_only/WORKSTREAMS.md`;
- the explicit current `#issue` / `#feature` directive, clear current natural-language authorization for a new managed change, or the exact active intake record from the selected workstream manifest;
- project `PROJECT.md`;
- only repository branch/PR/workstream/source/runtime evidence needed to establish identity, reproduce/diagnose when practical, choose base/dependency and materialize the smallest legal downstream route.

For a new intake trigger, do not load an unrelated active Task Board merely because it is the current/default execution state. Intake discovers relevant workstreams without adopting their mutable state. Read-only analysis without managed-change authorization does not create a workstream.

When Intake completes, it must first materialize the canonical durable state owned by the selected downstream route, then set its manifest intake state complete, return to this router and continue. A completed intake is not a user/session stop by itself.

### Brainstorming

Read:
- `workflow/codex_only/BRAINSTORMING.md`;
- the exact record referenced by selected manifest `routing.exploratory_scope` when that locator exists;
- the exact `complete` Research record referenced by selected manifest `routing.research_obligation` when its Return target is this Brainstorming subject;
- otherwise the current brainstorming material needed to establish/create the manifest locator;
- only accepted constraints already relevant.

### Research

Read:
- `workflow/codex_only/RESEARCH.md`;
- the exact record referenced by selected manifest `routing.research_obligation` for pre-execution Research when that locator exists;
- otherwise the exact Task Board `research_obligation` pointer when Research was triggered from active execution/recovery;
- the exact research question/material;
- only relevant accepted requirements/decisions/source state.

The durable research record owns its `Status`, Origin subject and Return target. Do not infer the return role from chat history.

### Project Definition

Read:
- `workflow/codex_only/DEFINITION.md`;
- current user/product goal and explicit accepted choices;
- the exact record referenced by selected manifest `routing.exploratory_scope` when Definition was entered through the promotion gate and the locator is still active;
- the exact `complete` Research record referenced by selected manifest `routing.research_obligation` when its Return target is this Project Definition subject;
- the exact `complete` record referenced by Task Board `research_obligation` when its final Return target is this Project Definition subject;
- relevant brainstorming conclusions;
- relevant verified research/evidence;
- existing requirements/decisions when redefining accepted authority;
- only current source/external baseline needed to constrain the definition.

Do not load Planning or execution modules merely to define product/system intent.


### Repository / project initialization

Read:
- `workflow/codex_only/REPOSITORY.md`;
- `workflow/common/AUTHORITY.md`;
- existing `PROJECT.md` when present;
- only project artifacts needed for topology/layout/state-ownership/legacy-migration or detailed Git/branch questions.

Use this route for:
- new project initialization;
- repository topology/layout;
- split-repository questions;
- detailed branch policy;
- state-ownership ambiguity;
- legacy repository/state migration.

### Strategic planning

Read:
- `workflow/codex_only/PLANNING.md`;
- approved canonical requirements;
- accepted decisions;
- the exact `complete` Research record referenced by selected manifest `routing.research_obligation` when its Return target is this Strategic Planning subject;
- the exact `complete` record referenced by Task Board `research_obligation` when its final Return target is this Strategic Planning subject;
- only verified research/baseline that the accepted definition or plan actually references;
- current approved plan when replanning.

Planning assumes Project Definition is complete. If requirements/strategic decisions are missing or contradictory, return to Project Definition instead of silently deciding them.

Read Task Board/current handoff only when planning/replanning an active project. Do not load execution files merely to organize strategy.

### Independent plan review

Read:
- `workflow/codex_only/PLAN_REVIEW.md`;
- selected workstream manifest + validated `routing.plan_review` locator;
- exact `planning/reviews/<plan-revision>.md` record;
- exact immutable Master Plan review subject;
- approved canonical requirements;
- accepted decisions;
- relevant Definition authority;
- only research/baseline/source evidence materially referenced by the plan.

Read Task Board/current handoff only when reviewing a replan whose correctness materially depends on active execution state.

Do not load the planning-session narrative as review evidence.

### Execution preparation / JIT refinement

Read:
- `workflow/codex_only/EXECUTION_PREP.md`;
- `workflow/codex_only/WORKSTREAMS.md` when the current execution context is branch-isolated;
- `workflow/codex_only/TASK_CARDS.md`;
- current milestone/plan authority, or exact completed micro-fix Intake + `MICRO_FIX.md` when that direct path is selected;
- Task Board when implementation state exists;
- exact predecessor evidence needed by current decomposition;
- the exact `complete` record referenced by Task Board `research_obligation` when its final Return target is this Execution Prep subject.

Read `workflow/codex_only/MICRO_FIX.md` when the exact selected Intake route is `micro_fix`.

Read `workflow/common/OPENSPEC.md` only when current preparation marks/reconciles an OpenSpec-relevant contract.

### Execution

Read:
- `workflow/codex_only/EXECUTION.md`;
- `workflow/codex_only/STATE.md`;
- `workflow/codex_only/WORKSTREAMS.md` when the current execution context is branch-isolated;
- Task Board;
- current milestone/Card, or bounded micro-fix Card + completed Intake record;
- exact authority slice;
- only source/runtime/evidence needed for that card;
- the exact `complete` record referenced by Task Board `research_obligation` when its final Return target is this Execution subject.

Read `workflow/common/OPENSPEC.md` only when the current card references/requires it.

### Independent review

Read:
- `workflow/codex_only/REVIEW.md`;
- `workflow/codex_only/STATE.md`;
- `workflow/codex_only/WORKSTREAMS.md` when the reviewed subject belongs to a branch-isolated workstream;
- exact active branch;
- the exact review owner: selected Task Board for Card/milestone review, or selected manifest for workstream final-integration review;
- selected Task Board when implementation/corrective state exists;
- exact immutable review subject;
- reviewed Card/milestone contract, or exact workstream final-integration authority/acceptance surface;
- `workflow/codex_only/MICRO_FIX.md` when the subject is a qualified micro-fix;
- the same authority slice that governed implementation;
- required review evidence;
- actual subject/source/runtime needed to judge it.

Do not load implementing-session narrative as review evidence and do not inspect another workstream Task Board.

### Milestone close / publication / workstream integration

Read:
- `workflow/codex_only/CLOSE.md`;
- `workflow/codex_only/STATE.md`;
- `workflow/codex_only/WORKSTREAMS.md` when branch-isolated;
- Task Board;
- for normal milestone close: milestone contract + required Card/review evidence;
- for qualified micro-fix close: exact completed micro-fix Intake + bounded fix Card + `MICRO_FIX.md` + required Card review evidence, with no milestone contract required;
- selected manifest final-integration review state when branch-isolated;
- intended final branch/state and current integration target.

### Strategic blocker

Read only:
- exact blocker/evidence;
- current Card/milestone contract;
- smallest requirements/decision/research/source slice needed to classify it.

If this route is the exact `execution_resolution:<subject>` Return target of a completed implementation/recovery Research record:
1. verify that Task Board `research_obligation` still points to that record and that its Origin/Return subjects match the affected durable Card/blocker state;
2. classify the findings against current durable authority;
3. if classification identifies an exact final owning role/subject, persist that classification by replacing the record's Return target with that final owner while keeping `Status: complete`, `Return reconciliation: pending`, and keeping Task Board `research_obligation`;
4. for that ordinary final-owner case, return through this router; the pointer now deterministically routes to the final target and the classifier does **not** mark the record `consumed`;
5. if classification instead proves that more evidence is needed before any final owner can be named, do not invent or persist a final Return target; use the classifier-to-Research chain transition in `RESEARCH.md`.

Then:
- bounded L1/L2 correction inside accepted authority → refine Return target to Execution Prep or Execution;
- if accepted product/system intent or a strategic decision must change → refine Return target to Project Definition;
- if accepted definition remains valid but milestone sequencing/plan must change → refine Return target to Strategic planning;
- if more evidence is still needed before either can be decided → in one durable Git transition persist `R1 Return reconciliation: applied` with exact `R2` ref, set `R1 Status: consumed`, create `R2 Status: active`, and switch Task Board `research_obligation` directly from `R1` to `R2`; then route to Research. Never expose `R1 complete` after moving the pointer and never expose a null-pointer gap.

Do not continue affected work until the owning authority is resolved.

### Recovery

Read:
- `workflow/codex_only/RECOVERY.md`;
- `workflow/codex_only/INTAKE.md` only when historical root/default migration must recover/create workstream identity, target/base or dependency topology;
- selected manifest when branch-isolated;
- selected Task Board;
- exact active branch/HEAD/runtime;
- affected in-progress/blocked/Card-review/workstream-review state;
- referenced contracts/evidence.

After recovery, route to the recovered obligation above.

## Human-facing behavior

Use the global normal-ChatGPT control-surface rules from root `CHATGPT.md`.

Do not end a turn merely to announce deterministic work that this route already authorizes. Continue first; respond at a real review/user/authorization/runtime/strategic/end-of-scope boundary.
