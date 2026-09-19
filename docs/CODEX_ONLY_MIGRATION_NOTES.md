# codex_only migration notes

The dedicated `codex_only` Project Workflow policy is implemented under `workflow/codex_only/`.

## Routing

A project selects `codex_only` only through its accepted `PROJECT.md -> execution_policy`. Root `workflow/CONTEXT_ROUTING.md` dispatches that policy directly to `workflow/codex_only/ROUTER.md`.

The route may read genuinely policy-neutral `workflow/common/*`, but migrated execution semantics must not fall back to `workflow/chatgpt_only/*`, `workflow/codex/*`, `workflow/legacy/*` or `workflow/contracts/*`.

Other accepted policies remain on legacy routing until separately migrated.

## Project Workflow versus runtime ownership

Project Workflow owns durable requirements, decisions, milestones, Cards, review subjects/verdicts/evidence, project-level lane/integration semantics and stop/continuation boundaries.

Codex Main is the sole shared Task Board/integration-state writer. `codex_workflow` owns concrete worker/session/model/profile/reasoning/invocation/wait/resume/replacement/concurrency mechanics.

Runtime identifiers are not Project Workflow authority and must not be required durable keys.
## Review and execution

Formal independent review is defined by immutable exact subject plus semantic role independence. Tester does not repair production. RED returns to the owning Executor; a corrected implementation becomes a new exact review subject. A qualifying Codex-managed verdict does not require a second normal-ChatGPT review.

Serial execution remains valid by default. Bounded parallel Cards are opt-in and require current-state JIT proof of completed dependencies, explicit `parallel_safe`, disjoint mutable `write_scope`, non-conflicting `exclusive_resources`, isolated mutable local workspaces where applicable, and one recoverable integration base.

Codex Main integrates returned lane results in frozen order and preserves immutable result/integration provenance.

## Workstreams and final integration

Legacy/default `implementation/TASK_BOARD.yaml` remains valid when no branch-isolated workstream is selected. Branch-isolated workstreams bind one `WORKSTREAM.yaml` to exactly one Task Board and keep final-integration review manifest-owned.

Stacked children retain real parent-dependency provenance and use only legal child-to-parent or parent-first-to-target paths.

Before final integration, Close refreshes against the current target, checks textual and semantic conflicts, reruns affected verification, and preserves an existing review only when the exact covered workstream behavior/content plus acceptance surface remain unchanged.

The final target must retain the namespaced durable workstream package needed for terminal recovery before the source branch may be deleted.
## Migration safety

Do not delete the legacy/shared Codex execution tree merely because `codex_only` is now migrated; remaining policies may still depend on legacy routing.

Do not switch an existing project to `codex_only` implicitly. Changing `execution_policy` requires accepted project/user authority.

For branch-isolated feature integration, target-owned global project metadata must be reconciled during the current-target refresh. A textually clean Git merge is not sufficient evidence of semantic compatibility.

This feature repository itself remains configured with `execution_policy: chatgpt_only`.
