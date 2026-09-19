# Requirements — dedicated codex_only policy namespace

Revision: `CO-R1`
Status: `approved`
Updated: `2026-09-19`

## Goal / target state

Provide a complete dedicated `codex_only` Project Workflow policy namespace that preserves the mature project lifecycle of current `chatgpt_only` while adapting execution, independent review, recovery and bounded concurrency to the Codex Main + `codex_workflow` runtime model.

The repository `elmakus/chatgpt-codex-project-workflow` itself remains configured with `execution_policy: chatgpt_only`.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| CO-REQ-001 | `execution_policy: codex_only` MUST route to a dedicated `workflow/codex_only/...` namespace. | MUST | user / ADR-CODEX-NS-001 | accepted |
| CO-REQ-002 | `chatgpt_only` MUST continue routing only to `workflow/chatgpt_only/...`; the codex_only migration MUST NOT merge the two policy namespaces into one conditional execution core. | MUST | user / ADR-CODEX-NS-001 | accepted |
| CO-REQ-003 | Other accepted policies not migrated by this scope MUST remain on their existing legacy route until separately migrated. | MUST | user / ADR-CODEX-NS-001 | accepted |
| CO-REQ-004 | Controlled duplication between `chatgpt_only` and `codex_only` is allowed; extraction into `workflow/common/` is allowed only for genuinely policy-neutral semantics. | MUST | user / ADR-CODEX-NS-001 | accepted |
| CO-REQ-005 | The codex_only lifecycle MUST preserve semantic coverage for Intake, branch-isolated workstreams, manifest-selected Task Boards, legacy/default Task Board compatibility, Brainstorming, Research, Project Definition, Planning, Execution Prep/JIT, Task Cards, micro-fix, Research return, stacked workstreams, target/integration refresh, exact review subjects, durable recovery, Close/acceptance/publication and locator-only recovery. | MUST | user / ADR-CODEX-NS-001 | accepted |
| CO-REQ-006 | codex_only MUST preserve the absence of a repository-global mutable workstream scheduler. | MUST | user / ADR-CODEX-NS-001 | accepted |
| CO-REQ-007 | Project Workflow MUST own project semantics and durable project state: milestones, Task Cards, dependencies, accepted authority, acceptance, review requirement/subject/state/evidence, project-level parallel safety/ownership, workstream/lane/integration semantics and workflow stop/continuation boundaries. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-008 | `codex_workflow` MUST remain the runtime owner of concrete worker role realization, worker/profile/model/reasoning selection, worker lifecycle, session/resume, invocation mechanics, waiting, runtime recovery and worker-concurrency mechanics. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-009 | Project Workflow durable state and contracts MUST NOT own or require `session_id`, `invocation_id`, Muse leases, worker-resume protocol, concrete model/reasoning/profile selection or equivalent runtime-only identifiers/state. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-010 | `codex_workflow` MUST NOT become the owner of Project Workflow Task Board, router, accepted-authority or review state. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-011 | A Codex-managed independent reviewer that satisfies the Project Workflow review contract MUST be able to provide the formal Project Workflow independent verdict without a second mandatory normal-ChatGPT review. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-012 | Formal review independence MUST be defined by role/subject behavior, not by a required normal-ChatGPT session identity: the reviewer is distinct from the implementation owner for the exact subject, reviews an immutable exact subject against the same authority/acceptance surface, and does not mutate that subject while judging it. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-013 | For implementation review, Tester MUST NOT implement or perform production repair. RED findings MUST return through Codex Main to the owning Executor; the owning Executor produces any corrected implementation. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-014 | Every materially changed reviewable implementation MUST become a new immutable review subject and a distinct review attempt with preserved prior RED/GREEN evidence. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-015 | The same logically independent Tester MAY review a later exact subject when independence remains intact and runtime resume is safe. Project Workflow MUST NOT require a replacement merely because the subject changed. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-016 | When a prior worker cannot be safely resumed or its independence is compromised, runtime fail-closed replacement MAY be used without changing Project Workflow semantics; Project Workflow records project review state/evidence, not worker replacement mechanics. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-017 | codex_only MUST support bounded parallel Task Card execution inside one workstream while keeping serial execution as the default. | MUST | user / ADR-CODEX-PAR-001 | accepted |
| CO-REQ-018 | Strategic Planning MAY express candidate parallel/dependency structure, but MUST NOT by itself guarantee runtime-safe concurrency for future state. | MUST | user / ADR-CODEX-PAR-001 | accepted |
| CO-REQ-019 | Execution Prep/JIT MUST re-evaluate current-state parallel safety immediately before concurrent execution. | MUST | user / ADR-CODEX-PAR-001 | accepted |
| CO-REQ-020 | Parallel eligibility MUST require completed dependencies, explicit `parallel_safe`, disjoint mutable `write_scope`, no conflicting `exclusive_resources`, isolated mutable lane/worktree/equivalent workspace where concurrent local mutation exists, and a recoverable integration base. | MUST | user / ADR-CODEX-PAR-001 | accepted |
| CO-REQ-021 | Codex Main MUST remain the sole owner/writer of shared Project Workflow Task Board and integration state; worker lanes MUST NOT become independent owners of shared project state. | MUST | user / ADR-CODEX-PAR-001 | accepted |
| CO-REQ-022 | Bounded parallelism MUST use deterministic bounded ready-set/dependency semantics rather than an unbounded generic scheduler. | MUST | user / ADR-CODEX-PAR-001 | accepted |
| CO-REQ-023 | Lane/worktree isolation MUST apply to intra-workstream parallel local mutation as well as cross-workstream concurrent mutation. | MUST | user / ADR-CODEX-PAR-001 | accepted |
| CO-REQ-024 | Durable recovery MUST reconstruct project obligations and exact review subjects from repository state regardless of whether runtime resumes A1/B1 or replaces them with A2/B2. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-025 | Project-level execution provenance MAY identify project role/lane ownership needed for recovery, but MUST NOT encode runtime session/profile/model identities as project authority. | MUST | user / ADR-CODEX-RT-001 | accepted |
| CO-REQ-026 | The migration MUST inventory useful legacy Codex/shared properties and preserve their behavior where consistent with the new architecture: Codex Main accountability, continuous multi-milestone progression, bounded parallelism, Executor/Tester separation, strategic escalation, lane/worktree isolation, integration ownership, recovery and no capability-preflight policy switching. | MUST | user / ADR-CODEX-NS-001 | accepted |
| CO-REQ-027 | Existing legacy `workflow/codex/*`, shared `workflow/EXECUTION.md`, `workflow/contracts/*` and legacy routing MUST be treated as compatibility/evidence inventory, not copied as the architectural base. | MUST | user / ADR-CODEX-NS-001 | accepted |
| CO-REQ-028 | This feature MUST NOT change this repository's own accepted `execution_policy: chatgpt_only`. | MUST | user | accepted |

## Constraints

- Current Project Workflow `main` is the lifecycle reference baseline.
- `codex_workflow` release `v1.1.17-private.12` at source commit `d285aa1a271258052d23e3a2d3b585117fc1e862` is verified runtime capability evidence, not Project Workflow authority.
- The old `feat/bounded-parallel-task-cards` branch is evidence only; it is not a parent dependency for this scope.
- The new policy must remain recoverable from durable repository authority without requiring transcript state or runtime worker/session identifiers.

## Non-goals

- Changing this repository's own execution policy.
- Migrating every other legacy policy in the same scope.
- Creating a new large shared `fixed_policy_core` or equivalent abstraction layer.
- Moving worker runtime/session/model/profile selection into Project Workflow.
- Moving Project Workflow Task Board/router/review state into `codex_workflow`.
- Requiring a second normal-ChatGPT independent review after a qualifying Codex-managed formal review.
- Building an unrestricted generic DAG scheduler.
- Preserving legacy implementation mechanisms merely because they exist.
- Freezing exact runtime invocation APIs, Muse session schema or model/profile configuration in Project Workflow requirements.

## Global invariants

1. Policy namespaces do not import policy-specific execution semantics from each other.
2. Project authority/state and worker runtime state remain separate ownership domains.
3. Exact review subjects are immutable per attempt.
4. A formal reviewer does not repair the subject it is reviewing.
5. Shared Project Workflow Task Board/integration state has one project-level owner: Codex Main.
6. Parallel Task Cards are opt-in and JIT-proven safe; absence of proof means serial execution.
7. Runtime reuse/replacement never changes the meaning of Project Workflow review state.
8. No project-level policy switch occurs because of runtime capability/preflight convenience.

## External contracts / dependencies

### codex_workflow

Project Workflow may rely on `codex_workflow` being able to realize distinct logical worker roles and independent review, including resume/replacement behavior, but it does not standardize the runtime's internal session or invocation schema.

Verified baseline evidence:
- `elmakus/codex_workflow`
- `v1.1.17-private.12`
- source `d285aa1a271258052d23e3a2d3b585117fc1e862`
- release includes stateful Muse logical worker sessions and fail-closed reservation/resume handling.

If a future runtime cannot satisfy a required Project Workflow contract, the project enters the normal blocker/recovery/authority path; it does not silently change execution policy.

## Data integrity / idempotency / security constraints

- Main-owned writes to Task Board/integration state must remain recoverable and deterministic.
- Concurrent worker results must be attributable to their project Card/lane before integration.
- Parallel integration must not discard lane evidence/results merely to serialize the final state.
- Review RED evidence remains durable after repair and later GREEN.
- Runtime-only identifiers must not become required durable Project Workflow identity keys.

## Acceptance-level requirements

The feature is Definition-complete only if Planning can organize work that proves all of the following:

1. Root routing explicitly distinguishes `chatgpt_only`, `codex_only`, and remaining legacy policies without policy-specific cross-imports.
2. `workflow/codex_only/` contains a complete policy-local lifecycle sufficient for a project to execute without falling back to legacy shared execution contracts for migrated semantics.
3. ChatGPT-only behavior remains intact and isolated.
4. The codex_only contracts contain no Project Workflow ownership of `session_id`, `invocation_id`, Muse leases, model/profile/reasoning selection or worker-resume protocol.
5. Formal independent review can execute the logical sequence Executor A1 → independent Reviewer/Tester B1 → RED → owning Executor repair → new exact subject → independent full recheck → GREEN, with same logical Tester reuse allowed when still independent and safe.
6. No rule requires a second normal-ChatGPT review after that qualifying formal review.
7. A serial codex_only workstream remains valid with no parallel metadata enabled.
8. Parallel candidate Cards cannot run concurrently unless JIT safety checks pass for dependencies, `parallel_safe`, `write_scope`, `exclusive_resources`, workspace isolation and integration recoverability.
9. Unsafe/overlapping candidates deterministically remain or become serial without losing project state.
10. Codex Main is the only writer/owner of shared Task Board and integration state during parallel execution.
11. Fresh/recovered Project Workflow state remains correct whether runtime resumes or replaces logical workers.
12. Legacy/default Task Board compatibility and branch-isolated workstream selection remain supported.
13. Useful legacy Codex behavior is either represented in the new policy semantics or explicitly shown non-applicable/rejected.
14. This repository's root `execution_policy` remains `chatgpt_only`.

## Definition completeness

- Target state and MUST requirements are explicit.
- Namespace architecture, Project Workflow/runtime ownership, independent review semantics and bounded-parallel safety are captured in accepted ADRs.
- No unresolved user/product choice can materially alter milestone architecture.
- Remaining exact schema/file-edit details are implementation/planning decisions constrained by this definition.

## Downstream coverage

Planning must map every `CO-REQ-*` requirement to at least one milestone/work package or exact JIT trigger before execution begins.
