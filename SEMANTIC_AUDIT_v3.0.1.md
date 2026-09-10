# Semantic Audit — v3.0.1

## Scope

v3.0.1 changes only the boundary between Project Workflow and the separately installed owner `codex_workflow`, plus release snapshot automation.

The v2.1 → v3.0.0 migration audit remains historical evidence for the original migration. This audit checks that removing duplicated Codex runtime mechanics from Project Workflow does not remove project-level obligations.

## Authority split

| Domain | Authority | Result |
|---|---|---|
| Project lifecycle and context routing | `elmakus/chatgpt-codex-project-workflow:main` | PASS |
| Requirements / accepted strategic decisions | canonical project repository artifacts | PASS |
| Task Cards / selective JIT OpenSpec / Refresh Gate | Project Workflow + project repo | PASS |
| GitHub execution state / evidence / milestone close / handoff | Project Workflow + project repo | PASS |
| ChatGPT ↔ Codex strategic blocker correlation/persistence | Project Workflow | PASS |
| Internal Codex worker/runtime orchestration when enabled | installed owner `codex_workflow` | PASS |

## Preserved project-facing semantics

The following remain explicit in Project Workflow after the split:

- Main remains accountable for the current Task Card outcome, integration, tests/acceptance, durable Git state, escalation and result evidence.
- Delegation does not transfer Task Card accountability.
- Worker completion alone cannot mark a Task Card `done`.
- Workers/subagents cannot independently rewrite product requirements, frozen strategic architecture, milestone acceptance criteria or strategic decisions.
- Strategic changes still route through the correlated ChatGPT ↔ Codex blocker protocol.
- The anti-overengineering rule still prohibits building shadow project workflow/task-state infrastructure without a concrete project need.
- Project recovery and milestone completion semantics remain unchanged.

## Removed duplication

Project Workflow no longer defines concrete Codex runtime mechanics such as worker roles/models, Companion lifecycle, wait/event/message behavior, polling/silence policy, concurrency or worker-runtime recovery. Those belong to the installed/enabled `codex_workflow` and may evolve there without creating a second stale copy here.

This is an authority relocation, not removal of the user's runtime workflow.

## Version automation

The persistent GitHub Actions workflow:

- runs only on pushes to `main`;
- creates an annotated SemVer tag on the exact pushed commit;
- is idempotent if the commit is already SemVer-tagged;
- increments only the patch component of the highest existing SemVer tag;
- refuses to move an existing next tag during normal operation;
- leaves major/minor bumps explicit.

## Result

**PASS.** No Project Workflow lifecycle/state/authority/acceptance/recovery semantic was lost. Codex runtime implementation details now have one canonical home instead of being duplicated across two workflow repositories.
