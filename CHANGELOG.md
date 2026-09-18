# CHANGELOG

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
