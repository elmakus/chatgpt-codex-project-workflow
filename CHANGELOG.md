# CHANGELOG

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
- Current workflow `main` supersedes old prompts, memory and ZIP snapshots when they conflict.
- `brainstorming != decision` is now explicit and enforced by the project authority hierarchy.

### Preserved v2.1 execution contracts

- GitHub execution states and milestone lifecycle.
- Task Card model and Definition of Done.
- `result_commit`, `result_pr` and `evidence` requirements for done cards.
- milestone `checkpoint`, `implementation_head`, acceptance evidence and cumulative handoff.
- selective, just-in-time OpenSpec.
- Refresh Gate.
- strategic ChatGPT ↔ Codex blocker protocol with matching `request_id` and `DECISION FOR CODEX:`.
- branch/PR, failure recovery, dependency, requirement coverage, fresh-context and anti-overengineering rules.

### Codex orchestration

- Added an explicit modular contract for bounded multi-agent delegation and event-driven coordination.
- Routine polling/progress chatter is prohibited; normal completion uses the standard completion path and push messages are reserved for material events.

### Migration safety

- Added `MIGRATION_AUDIT_v2.1_to_v3.md`, mapping every v2.1 source file and significant contract.
- Added `SEMANTIC_AUDIT_v3.md` as the second whole-workflow semantic and cross-document consistency audit.

## v2.1

Historical baseline changes retained from the v2.1 bundle:

1. Single implementation repository became the default canonical home for code plus Task Board, cards, evidence, OpenSpec and handoffs.
2. Split-repo was allowed only with an exact ownership map; migration was permitted only at a green milestone boundary.
3. Every done card required `result_commit`, `result_pr` when applicable and `evidence`.
4. Milestones gained an explicit lifecycle and, after a green gate, required `execution_status: done`, checkpoint, `implementation_head`, handoff and acceptance evidence.
5. Canonical cumulative handoff was standardized as `docs/project-handoffs/MXX_HANDOFF.md`.
6. A normative GitHub State Contract was added.
7. `current.md` was clarified as an optional local checkpoint, not durable truth.
8. Strategic messaging gained `request_id`; responses required a matching ID plus `DECISION FOR CODEX:`.
9. Branch/PR/finalization and recovery policy were tightened.
10. Safe legacy split-repo migration after a milestone was documented.

v3 supersedes the v2.1 repository-path/default-topology details with the one-project-one-repository-from-brainstorming model, while retaining the execution-state semantics.

## v2

Historical baseline changes retained from the bundle:

1. Direct strategic Codex Desktop ↔ normal ChatGPT channel.
2. GitHub as durable source of truth.
3. Structured `DECISION FOR CODEX:` marker.
4. Separate decision and execution state.
5. OpenSpec JIT + Task Cards + cumulative handoffs.
