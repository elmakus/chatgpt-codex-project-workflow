# CHANGELOG

## Unreleased — branch-first managed changes

- Migrated both fixed policies (`chatgpt_only` and `codex_only`) to a branch-first managed-change model: read-only exploration may remain branch-free, but natural-language authorization creates or recovers an exact branch-isolated workstream before the first durable change-specific write.
- Kept `#issue` / `#feature` as optional shortcuts and retained proportional micro-fix handling while requiring every managed change, including trivial ones, to integrate through branch → pull request → merge.
- Moved active exploratory, pre-execution Research and plan-review routing out of root `PROJECT.md` and into the selected workstream manifest plus exact pointed records; implementation/recovery Research remains selected-Task-Board-owned.
- Reclassified historical root/default Task Boards and cumulative handoffs as recovery/provenance input only for the migrated fixed policies; live historical obligations migrate deterministically to an exact branch-isolated workstream before further mutation.
- Preserved policy-local review/orchestration semantics: fresh normal-ChatGPT review boundaries for `chatgpt_only`, Codex Main/Tester and bounded-batch semantics for `codex_only`, plus existing target-refresh and terminal source-branch-deletion safety.
- Added integrated documentation/dogfood regression coverage so README, root project navigation, templates, bootstrap prompts and fixed-policy routing continue to express the branch-first invariant.


## Unreleased — dedicated codex_only policy namespace

- Added a complete dedicated `workflow/codex_only/` namespace and explicit root routing for `execution_policy: codex_only`, while keeping `chatgpt_only` isolated and non-migrated accepted policies on legacy routing.
- Kept Project Workflow project authority/state separate from `codex_workflow` runtime mechanics: Codex Main owns shared Task Board/integration state while worker/session/model/profile/invocation/resume/concurrency realization remains runtime-owned.
- Added immutable-subject, role-based independent review with Tester non-repair, RED → owning-Executor correction, reviewer reuse/replacement transparency, and no mandatory second normal-ChatGPT review after a qualifying Codex-managed verdict.
- Added serial-default bounded parallel Task Cards with current-state JIT safety proof, isolated local mutation, finite frozen batches, deterministic Main-owned integration and repository-first recovery.
- Completed policy-local Intake, Brainstorming, Research, Definition, Planning/plan review, micro-fix, default/branch-isolated workstreams, stacked dependencies, target refresh, final-integration review, Close and terminal target-side recovery semantics.
- Added M01–M05 migration/audit evidence, compatibility checks against current `main`, and final integration-readiness guidance.

## Unreleased — ChatGPT-only branch-isolated workstreams and intake

- Added branch-isolated `chatgpt_only` workstreams with stable manifests and per-workstream Task Boards while preserving legacy/default `implementation/TASK_BOARD.yaml` projects without forced migration.
- Scoped serial execution to one `in_progress` Card per selected Task Board so independent workstreams may progress concurrently on distinct branches and mutable state.
- Added explicit `#issue` and `#feature` intake; issue intake classifies independent versus genuine parent-only stacked dependencies before branch creation, while feature intake preserves the user-owned Definition-promotion gate.
- Added a bounded micro-fix path that can skip a full Master Plan without dropping durable acceptance/evidence or fresh independent review.
- Kept Card/milestone review state Task-Board-owned and added a distinct manifest-owned final-integration review gate for behavioral workstreams.
- Added local worktree/equivalent checkout isolation for concurrent local mutation, with remote-only GitHub execution exempt.
- Added stacked-parent dependency provenance, legal child integration paths and a final integration refresh gate with affected verification, textual/semantic conflict checks and exact-subject review preservation/invalidation.
- Fresh-session handoffs now use the smallest canonical workstream pointer: selected Task Board for Card/milestone review and selected manifest for workstream final-integration review, without prompt-state duplication.
- Added final architecture/coherence regression coverage across legacy mode, concurrent workstreams, issue/feature intake, micro-fix, same-workstream recovery, stacked integration, target refresh, review isolation and fresh-session continuation.
- Completed finalization semantics for branch-isolated workstreams: milestone handoffs are workstream-namespaced, project-global latest-handoff/root Task Board remain legacy/default-only, terminal state must survive on the integration target before source-branch deletion, and completed workstreams can recover from the target-side durable package after deletion.
- Added bounded migration rules for long-lived pre-workstream branches so branch-owned Task Board/cards/evidence/handoffs are namespaced at a GREEN boundary without overwriting the integration target's unrelated root legacy/default state.


## Unreleased — locator-only fresh-chat continuation

- Fresh normal-ChatGPT handoffs are now explicitly recovery/entry locators rather than bounded one-role task contracts.
- Completing the role named in a handoff no longer permits a user-facing status response unless the policy router confirms a real workflow stop.
- The common user-stop contract forbids prompt inflation with review/audit checklists, prior findings, remediation branches, test inventories, implementation summaries and other recoverable telemetry.
- Nonstandard review/audit scope that cannot be reconstructed from existing authority must be persisted durably first; the fresh prompt points to that artifact.
- `workflow/common/USER_STOP.md` is the single canonical owner of fresh-session prompt formatting; `prompts/CHATGPT_FRESH_SESSION.md` is now a convenience pointer rather than a duplicate template.
- Independent review, RED same-turn remediation, milestone continuation and Context Health FRESH all use the same locator-only continuation semantics.

## Unreleased — user-owned Brainstorming promotion

- Under `chatgpt_only`, Brainstorming may become `ready_for_definition` but cannot enter Project Definition until the user explicitly promotes the current scope.
- The active brainstorming record persists a stable scope ID, revision, exact promotion subject and `Definition promotion authorization: pending | user_authorized`; `PROJECT.md` points to that record while the exploratory/Definition scope is active so fresh-chat recovery is deterministic.
- Promotion authorization applies only to the exact authorized scope/revision; material exploratory change before Definition begins creates a new revision and resets authorization.
- Research completion does not count as implicit promotion from an exploratory scope.
- Once Project Definition has been explicitly authorized for the current scope, bounded Research ↔ Definition loops do not repeatedly ask for promotion; reopening open-ended Brainstorming resets the gate.
- `Definition Complete = GREEN → Planning` remains deterministic and automatic when planning is in scope.

## Unreleased — Definition/Planning audit corrections

- Removed `chatgpt_only`-specific workflow paths from the shared `templates/MASTER_PLAN.md`; shared templates now point only to policy-neutral/common routing and let the selected policy namespace provide planning/execution modules.
- Removed milestone ownership from canonical Requirements. Requirement → milestone → planned-work-package/JIT coverage now lives only in the Master Plan; concrete Task Card mapping remains Execution Prep responsibility.
- Restored the earlier independent-plan-review semantics: new/materially revised plans use independent review when practical, with a fresh ChatGPT plan reviewer under `chatgpt_only`.
- Added `workflow/chatgpt_only/PLAN_REVIEW.md`; mutable plan-review state lives outside the frozen Master Plan subject under `planning/reviews/<plan-revision>.md`.
- Narrowed old `L3/user decision` stop wording: plan-only replans route automatically to Planning when accepted Project Definition remains valid; only unresolved strategic/product choices that require user authority are user stops.
- Marked the prior Definition/Planning GREEN self-audit as superseded; the corrective package later completed a fresh independent GREEN re-review and was merged via PR #22.

## Unreleased — Project Definition before Planning

- Added policy-neutral `workflow/common/DEFINITION.md` between Brainstorming/Research and strategic Planning.
- Project Definition now owns promotion of accepted intent/evidence into canonical `requirements/` and `decisions/`; Brainstorming and Research no longer write planning authority directly.
- ChatGPT-only Planning now consumes an already-approved Definition and owns only execution organization: Master Plan milestones, dependencies, planned work packages, requirement coverage, acceptance/checkpoints, migration/verification strategy and JIT triggers.
- Missing/contradictory product/system intent routes back to Definition; missing evidence routes to Research; plan-only milestone/sequence changes remain Planning-owned.
- Requirements no longer require an owner milestone during Definition. Planning assigns milestone/work-package-or-JIT coverage; Execution Prep creates concrete Task Cards before implementation.
- Master Plan template now distinguishes planned work packages from executable Task Cards and points only to the active `chatgpt_only`/common workflow modules.
- New-project initialization now follows Brainstorming/Research → Definition → Planning → Execution Prep rather than letting planning implicitly define product intent.

## Unreleased — ChatGPT context health gate

- Added `workflow/chatgpt_only/CONTEXT_HEALTH.md` for qualitative session-health evaluation at safe durable boundaries.
- Completed ChatGPT-only Cards now return through the policy router before another Card starts, allowing context-health evaluation without creating a user-visible status stop.
- Existing real stops have priority: pending fresh review, L3/user decision, authorization gate, concrete runtime/access/input blocker or end of approved scope suppresses a separate hygiene handoff.
- A pending REQUIRED/RECOMMENDED independent review remains the preferred natural fresh-context reset.
- Context health uses no fixed token, turn, Card or milestone-count threshold.
- `CONTEXT_HEALTH: FRESH` is permitted only after the current obligation is fully persisted and the exact next obligation is recoverable from durable repository state.
- Added a context-hygiene fresh-chat variant to the common normal-ChatGPT user-stop contract.

## Unreleased — router-owned role transitions and explicit review none

- ChatGPT-only role completion is no longer treated as an implicit user-visible checkpoint. REVIEW, EXECUTION_PREP, EXECUTION, CLOSE and RECOVERY persist their result and return to the policy router, which selects the next legal role.
- A chat may therefore begin as an independent reviewer and later become an executor/closer in the same turn; once it implements a new reviewable subject, it is the implementing chat for that subject and must stop for a fresh independent reviewer.
- Removed `OPTIONAL` independent review from active ChatGPT-only contracts. Cards now use `REQUIRED | RECOMMENDED | none`.
- REQUIRED and RECOMMENDED are both real independent-review gates once recorded. `none` creates no review state; a later explicit review request first promotes it to RECOMMENDED.
- Added `workflow/common/USER_STOP.md` as the shared normal-ChatGPT real-stop response contract: concise result/meaning/next step, explicit `USER ACTION REQUIRED:` only when needed, `No action required.` at completed scope, and an immediate branch-aware `NEW CHAT START PROMPT` for fresh-chat handoffs.
- Intermediate status-only responses between deterministic legal role transitions are prohibited.

## Unreleased — lossless ChatGPT-only gap closure

- Re-audited the policy split against the exact pre-split checkpoint instead of relying on the earlier scenario-level audit.
- Restored omitted policy-neutral brainstorming/research/OpenSpec semantics under `workflow/common/`.
- Restored ChatGPT-only planning, repository, state, session-continuity, high-risk review, publication and cutover semantics that had been over-compressed during the first split.
- Added explicit execution-policy invariants: policy changes require an explicit user decision; a brand-new project defaults to `chatgpt_only` unless the user explicitly selects another accepted policy.
- Added safe reconciliation for legacy ChatGPT-only concurrent-card metadata while keeping the new active ChatGPT-only model serial.
- Added a full lossless semantic matrix mapping pre-split rules to new owners, policy exclusions or explicit supersessions.
- Marked the earlier post-switch audit as superseded for lossless-proof purposes; its historical routing/isolation findings remain preserved.

## Unreleased — policy-first routing and isolated chatgpt_only namespace

- `workflow/CONTEXT_ROUTING.md` is now a small execution-policy dispatcher rather than the full multi-policy route map.
- Added `workflow/chatgpt_only/` with isolated planning, execution preparation, Task Card, state, execution, review, close/publication, recovery and repository contracts.
- Added policy-neutral `workflow/common/` authority, brainstorming, research and OpenSpec modules.
- `chatgpt_only` execution now selects exactly one READY project Card at a time and does not load alternate-executor, pre-assignment routing or project-card concurrency semantics.
- Preserved the previous router unchanged at `workflow/legacy/CONTEXT_ROUTING.md` for policies not yet migrated.
- Existing shared execution/contracts and other executor-specific modules remain unchanged in this phase; no legacy deletion occurs before the remaining policy migrations.
- Simplified normal ChatGPT start/Project Instructions templates to point at the live policy router instead of duplicating policy semantics.
- Preserved fresh-review independence, RED same-turn bounded remediation, automatic continuation, JIT refinement, milestone close/publication and recovery semantics in the new ChatGPT-only path.

## Unreleased — reviewer auto-remediation and global ChatGPT control surface

- Normal ChatGPT human-facing output rules now live in the global `CHATGPT.md` bootstrap, so independent reviewers use the same concise control-surface behavior as executors.
- A `chatgpt_only` RED independent review is no longer an automatic user stop when corrective work is bounded, deterministic, authorized and unblocked.
- The fresh reviewer chat persists RED, switches into normal ChatGPT execution in the same turn, performs remediation, verifies/persists the corrected result, freezes the new exact subject as `review_state: pending`, then stops before self-review.
- That final response includes the branch-aware ready-to-copy fresh-chat prompt for independent re-review.
- The reviewer must not end the turn merely to announce that remediation is next; it stops earlier only for a real strategic/user/authorization/runtime blocker.

## Unreleased — lean executor runtime and runtime-discovered tools

- Added `workflow/contracts/TASK_EXECUTION.md` as the small shared runtime contract for already-defined Task Cards.
- Normal serial ChatGPT/Codex execution no longer requires the full Task Card authoring contract or full GitHub State contract.
- `TASK_CARDS.md` now owns authoring/decomposition/parallel metadata; runtime readiness/Refresh/DoD/result semantics moved to `TASK_EXECUTION.md`.
- `GITHUB_STATE.md` remains the extended coordinator/parallel/review/milestone/recovery state contract and is conditional for ordinary serial execution.
- Slimmed `workflow/EXECUTION.md` into the common execution loop with explicit conditional routes for parallel, JIT, review, close and recovery.
- Slimmed `workflow/chatgpt/EXECUTION.md` to ChatGPT-specific runtime/session/human-control behavior.
- Preserved Codex Main, worker, bounded-parallel, JIT and independent-review semantics in `workflow/codex/*`; ChatGPT simply no longer loads them.
- Project Workflow no longer enumerates executor tool catalogs in active runtime instructions. ChatGPT/Codex use their actual runtime and surface a blocker only when a concrete required operation cannot proceed.
- Mixed-policy Capability Gate remains pre-assignment routing and is not changed by this refactor.

## Unreleased — deterministic context read sets

- Slimmed `CHATGPT.md` into a true bootstrap/router instead of duplicating execution-policy and milestone-continuation semantics owned by phase modules.
- `workflow/CONTEXT_ROUTING.md` now defines per-route **REQUIRED**, **CONDITIONAL**, and **DO NOT READ BY DEFAULT** context sets.
- Pending independent review remains a global routing priority.
- Review-only ChatGPT sessions no longer load execution/planning/Codex modules by default; `TASK_CARDS`, `GITHUB_STATE`, `OPENSPEC`, and `PROJECT_REPOSITORY` are loaded only on explicit triggers.
- Compact authority precedence now lives in the router, so ordinary tasks do not need to read the full Project Repository Contract merely to determine authority order.
- Full `PROJECT_REPOSITORY.md` remains conditional for authority conflict, topology, legacy migration, layout/state-ownership ambiguity, or detailed branch-policy cases.

## Unreleased — branch-aware fresh-ChatGPT prompts

- Every fresh-ChatGPT start prompt now includes the exact active project/implementation branch, including `main` when applicable.
- Branch is treated as a routing locator rather than noisy execution telemetry.
- Exact HEAD/SHA remains omitted when recoverable from durable state.

## Unreleased — concise human-facing ChatGPT control summaries

- Normal ChatGPT status responses are now treated as a human control surface rather than an execution-telemetry dump.
- Default user-facing output explains what happened/what errors were found, what it means and what happens next.
- Commit/review SHAs, blob IDs, branch/HEAD pointers, evidence paths, raw Task Board fields, changed-file lists and long test inventories are hidden by default but remain exact in durable state.
- Exact technical identifiers are shown when the user asks, must act on them, or debugging/recovery/blocker handling materially requires them.
- This UX rule applies to ChatGPT→user communication only; Codex/worker/reviewer/internal agent communication remains free to carry the full technical detail required by workflow contracts.

## Unreleased — automatic fresh-ChatGPT start prompts

- Whenever workflow requires or recommends a fresh normal ChatGPT chat, the same response must include a fenced copy-paste-ready `NEW CHAT START PROMPT`.
- Fresh-chat prompts are routing-only: project repo, exact continuation target, durable start pointer and repo-recovery instruction.
- Durable SHAs, test summaries, evidence prose and implementation details are not duplicated into the prompt when recoverable from repository state.
- Users no longer need to separately ask for a prompt after a fresh-session recommendation or mandatory independent-review handoff.

## Unreleased — delegated JIT planning and role/model separation

### Roles

- Project Workflow now defines strategic planner, execution orchestrator/JIT planner, executor/worker and independent reviewer as **roles**, not model identities.
- No named model or reasoning level is required by workflow contracts; model/session selection remains a user/runtime concern.
- Strategic replan returns to the strategic-planning role, not necessarily the original planning model/session.

### Incremental planning

- Future Task Cards no longer need to be pre-created when their real scope materially depends on predecessor evidence.
- Placeholder cards with unknowable “whatever the previous step reveals” scope are explicitly discouraged.
- Execution orchestrators may create/split/merge/reorder/replace not-yet-started cards and complete JIT milestone detail from durable predecessor evidence without returning to the original planner.
- Added L1 execution detail, L2 JIT decomposition/refinement and L3 strategic replan boundaries.
- L2 authority is bounded by accepted requirements, frozen architecture/decisions, invariants, milestone outcome and explicit authorization gates.
- Known strategic ambiguity cannot be hidden as deferred decomposition.

## Unreleased — lean documentation and authority-preserving delegation

### Documentation footprint

- Approved Master Plan milestone subsections are now the default milestone contracts.
- Separate `implementation/milestones/MXX.md` files are optional JIT extensions created only when they add material execution/acceptance detail.
- Task Cards now have a smaller mandatory core; priority, complexity, phase, code-location hints and similar metadata are optional when they improve execution.
- Simple reproducible cards may close with exact result pointers + Task Board `tests_summary`; standalone evidence remains expected for milestone acceptance, required/recommended independent review, baseline exceptions, material external writes/readback, complex multi-stage verification or explicit contract requirements.
- Cumulative handoffs are compact continuation summaries rather than mandatory inventories of files/APIs/schema sections.

### Authority preservation

- Added the project-level rule **lossless by authority, selective by context**.
- Task Cards identify exact authority slices and must preserve every applicable implementation-shaping constraint.
- Downstream execution/review packages either carry applicable constraints explicitly or require exact durable authority reads.
- Planner rationale must survive when dropping it could reasonably lead to a different implementation choice.
- Executor and independent reviewer evaluate against the same applicable authority slice; summaries/paraphrases never outrank exact durable authority.

### Repository hygiene

- Historical migration and semantic-audit reports moved out of repository root into `docs/history/`; current root remains focused on active workflow entrypoints and changelog.

## Unreleased — runtime capability discovery and explicit independent-review handoff

### Fixed-policy capabilities

- `chatgpt_only` and `codex_only` no longer perform capability preflight/inventory/checklists during Execution Prep or Refresh Gate.
- Fixed-policy execution starts directly after the normal state/contract Refresh Gate; capability becomes workflow state only when a concrete required operation cannot proceed.
- Codex may self-remediate ordinary non-secret local tooling/dependency gaps when its environment permits and accepted security/reproducibility constraints allow it.
- User-provided MCP/credential/token/account permission/privileged access is requested only when concretely needed and unavailable.
- A user may explicitly change `execution_policy` after a runtime blocker; Task Board is reconciled before blocked work is reassigned. Policy/executor never changes automatically.

### Independent review

- Added durable Task Board review fields: `review_state`, `review_subject`, `review_evidence`.
- Under `chatgpt_only`, a chat that implemented a REQUIRED/RECOMMENDED review subject must freeze/persist the exact subject and stop at `review_state: pending`; the user starts a fresh normal ChatGPT chat for the independent review.
- A fresh ChatGPT reviewer may continue later deterministic work after GREEN; if it implements a new reviewable subject, another fresh chat is required for that later independent review.
- Under `codex_only`, Codex Main obtains an independent reviewer worker/session without a user handoff solely for reviewer independence.
- When `codex_workflow` is installed/enabled, it remains authoritative for internal Codex execute/review-worker routing, roles/models, lifecycle, delegation and runtime recovery; Project Workflow owns exact subject, review requirement, durable verdict/evidence and acceptance state.

## Unreleased — policy-fixed execution and single live-state authority

### Execution state

- Made `implementation/TASK_BOARD.yaml` the sole authoritative mutable execution-state record.
- Milestone and Task Card files are now stable scope/acceptance/test contracts rather than status/result mirrors.
- `PROJECT.md` is now explicitly high-level project routing/policy only; current milestone/card/executor/branch/HEAD/checkpoint/OpenSpec/blocker state belongs in Task Board.
- Cumulative handoffs remain completed-milestone summaries, not live trackers.
- Removed the requirement to synchronize `execution_status`, executor and result pointers between Task Board and Task Card files.

### Execution routing

- Added third execution policy: `codex_only`.
- `chatgpt_only` and `codex_only` are fixed-executor modes and no longer run Capability Gate.
- Capability Gate is now explicitly `mixed`-only.
- Preserved routing invariant `ChatGPT capabilities ⊆ Codex capabilities`.
- Missing capability under fixed policy is a blocker for the fixed executor; policy never changes automatically.

### Multi-milestone continuation

- GREEN milestone boundaries are no longer automatic routing/user stops under fixed execution policy.
- ChatGPT under `chatgpt_only` and Codex Main under `codex_only` may continue automatically into the next already-approved milestone after normal close/handoff + just-in-time execution prep + fresh Refresh Gate.
- Explicit strategic/product/architecture decisions, user/deployment/live-write authorization gates, missing capability/evidence and end of approved scope remain hard stops.
- Under `mixed`, new execution assignments continue to route through Capability Gate.
- No separate Campaign or scheduler abstraction was added; approved Master Plan + Task Board + existing milestone gates are sufficient.

### Review

- Independent review is now defined by independence from implementing worker/session rather than hard-coded to normal ChatGPT.
- `chatgpt_only` uses fresh independent ChatGPT review when required/recommended; `codex_only` may use a distinct Codex reviewer/worker/session; `mixed` follows the accepted independent review contract.

## Unreleased — dual-executor architecture

### Execution routing

- Replaced the hard-coded `ChatGPT plans → Codex executes` model with `ChatGPT manages project → Capability Gate selects ChatGPT or Codex executor`.
- Added project-level `execution_policy: chatgpt_only | mixed`.
- Added a lightweight ChatGPT Capability Gate with three outcomes: `EXECUTE IN CHATGPT`, `HANDOFF TO CODEX`, or `BLOCKED`.
- Explicitly scoped Project Workflow to normal ChatGPT chat + Codex; ChatGPT Work is not used by this workflow.
- Made the execution core executor-neutral and added thin ChatGPT/Codex execution adapters.
- Added optional Task Card capability requirements for external, unusual or routing-significant work and executor provenance for active work.
- Added the shared external-write rule `WRITE → READBACK → VERIFY` when readback materially validates the resulting state.
- Added independent-review tiers: required for high-risk work, recommended for major architecture/refactors, optional for simple changes.
- Added an optional competing research-path pattern for A/B/Hybrid evaluation without making it a mandatory lifecycle stage.
- Added optional `bounded_parallel` Task Card execution while preserving serial as the default.
- Parallel project cards now require completed dependencies, explicit `parallel_safe`, bounded non-overlapping `write_scope`, no shared `exclusive_resources`, isolated mutable lanes and coordinator-owned Task Board/integration state.
- Added a project `parallel_card_limit` ceiling and deterministic compatible-ready-set selection without introducing a generic DAG engine or shadow scheduler.
- Codex Main may map compatible project Task Cards to isolated `codex_workflow` workers while remaining responsible for project-level lane state, integration, post-integration verification and card completion.

### Progressive disclosure

- Codex no longer loads `CHATGPT.md` or ChatGPT-specific execution instructions.
- ChatGPT loads Codex handoff rules only when actually handing work to/from Codex.
- Moved the Codex runtime boundary contract under `workflow/codex/`.
- Removed the monolithic ChatGPT↔Codex responsibility contract whose old role split is no longer valid.

### Migration

- Added a safe transition rule for projects with execution already in progress under v3.0.3: finish/recover bounded in-flight work under its frozen workflow revision and adopt `execution_policy` at the next clean GREEN boundary.
- Added a reusable short ChatGPT Project Instructions bootstrap.

## v3.0.3

### Execution-prep handoff UX

- ChatGPT execution prep must now finish with an explicit `EXECUTION PREP COMPLETE:` handoff instead of leaving the user to infer how to start Codex.
- Every completed prep must include `CODEX SESSION RECOMMENDATION: FRESH` or `CODEX SESSION RECOMMENDATION: CONTINUE EXISTING`, a short reason, a copy-paste-ready `CODEX START PROMPT:`, and the smallest concrete `USER ACTION:`.
- `FRESH` is the default at a clean new-milestone boundary after a GREEN checkpoint; `CONTINUE EXISTING` is preferred when prep extends the same active milestone and the existing Codex context remains useful and current.
- A fresh-session recommendation is explicitly context-hygiene guidance, not a product decision or authorization gate.
- Added a reusable execution-prep start-prompt template that points Codex to durable repository routers/kickoffs and preserves automatic deterministic Task Card progression.

## v3.0.2

### Explicit continuation status

- Codex user-visible execution checkpoints must now state unambiguously whether execution is continuing automatically, user action is required, a fresh session is only recommended, or the milestone is complete.
- A routine GREEN Task Card no longer permits a neutral status-only ending that can be mistaken for a request to intervene; deterministic READY-card progression remains automatic.
- Added standard markers: `NEXT ACTION:`, `USER ACTION REQUIRED:`, `SESSION HANDOFF RECOMMENDED:` and `MILESTONE COMPLETE:`.
- Fresh-session recommendations must distinguish context hygiene/recovery from real product or authorization gates and include a durable continuation pointer.

## v3.0.1

### Authority boundary

- Clarified that `elmakus/chatgpt-codex-project-workflow` is authoritative for project lifecycle/process, durable project state, Task Cards, selective JIT OpenSpec, acceptance/evidence, strategic escalation and cumulative handoffs.
- Clarified that, when the owner's `codex_workflow` is installed and enabled, its installed instructions are authoritative for internal Codex runtime orchestration such as worker roles/models, Companion lifecycle, delegation mechanics, wait/event/message behavior, polling/silence and worker-runtime recovery.
- Replaced the duplicated runtime-orchestration rules in `workflow/contracts/CODEX_ORCHESTRATION.md` with a thin integration/boundary contract.
- Preserved project-level delegation accountability: worker completion is not Task Card completion, Main still owns integration/acceptance/evidence, and workers cannot independently rewrite strategic/product authority.
- Project Workflow no longer needs to read or reproduce the remote `elmakus/codex_workflow` repository during ordinary project work.

### Version snapshots

- Added a persistent GitHub Actions workflow that automatically creates the next annotated SemVer patch tag for each push to `main`.
- `main` remains canonical authority; tags are immutable historical snapshots.
- Major/minor version changes remain explicit; automatic tagging increments only the patch component from the highest existing SemVer tag.

## v3

v3 reorganizes the v2.1 workflow without intentionally losing its execution semantics.

### Project truth and repository model

- A project repository now exists from the first brainstorming session.
- **ONE PROJECT = ONE REPOSITORY** is the default from idea through implementation and handoff.
- The workflow repository stores workflow only; there are no central project workspaces.
- Project knowledge is explicitly separated into brainstorming, decisions, research, requirements, planning, implementation, project handoffs and OpenSpec.
- Root `PROJECT.md` is the small project context router and authority index.
- A split-repository project is an exception requiring technical justification and an explicit user decision; legacy topology changes still occur only at a green milestone boundary.

### Context and authority

- Added phase-aware progressive context routing.
- `CHATGPT.md` is a small global router rather than a copy of the complete workflow.
