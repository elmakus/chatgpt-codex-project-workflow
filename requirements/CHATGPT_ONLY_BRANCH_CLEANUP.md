# ChatGPT-only Branch Cleanup Requirements

Revision: BC-R1
Status: approved
Updated: 2026-09-19
Scope ID: branch-delete-prefix
Execution policy affected: chatgpt_only

## Goal / target state

Make terminal branch cleanup deterministic without keeping source branches alive merely for post-merge bookkeeping.

For normal GitHub PR integration, the source workstream branch must be disposable immediately after merge so GitHub repository-level automatic head-branch deletion can be used safely.

Branches that terminate without merge, or merged branches that survive because automatic deletion is unavailable or blocked, must use a durable fallback cleanup marker rather than synthetic delete/* alias branches.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| BC-R1 | Before final merge, every unique workstream artifact required for terminal recovery MUST already be included in the merge subject or otherwise durably available from the integration target or immutable GitHub PR/merge state. | MUST | user-approved R3 direction | accepted |
| BC-R2 | Post-merge close/readback MUST NOT require the source workstream branch to still exist. | MUST | user-approved R3 direction | accepted |
| BC-R3 | When a GitHub repository supports automatic deletion of merged PR head branches, the normal ChatGPT-only merged-PR path SHOULD use that repository capability rather than preserving or renaming terminal source branches. | MUST | ADR_CHATGPT_ONLY_AUTODELETE_MERGED_HEAD_BRANCHES | accepted |
| BC-R4 | A merged source branch disappearing immediately after merge MUST be treated as normal success, not as missing recovery state. | MUST | ADR_CHATGPT_ONLY_AUTODELETE_MERGED_HEAD_BRANCHES | accepted |
| BC-R5 | Post-merge verification MUST use the integration target plus immutable PR/merge metadata and target-side durable package. If final merge-result metadata cannot be known pre-merge, it MUST be reconciled by a target-side closure-only change without recreating the source branch. | MUST | user-approved R3 direction | accepted |
| BC-R6 | A terminal branch that is intentionally closed or superseded without merge, or a merged branch that survives automatic deletion, MUST be eligible for an explicit durable safe_to_delete fallback only after terminal recovery no longer depends on that branch and no live workstream obligation remains. | MUST | user-approved R3 direction | accepted |
| BC-R7 | ChatGPT-only MUST NOT emulate branch rename by creating a second branch/ref at the same commit. Creating delete/<original> while retaining <original> is forbidden as cleanup marking. | MUST | connector limitation + user incident | accepted |
| BC-R8 | A closed PR alone MUST NOT prove deletion safety. Terminal workstream state, exact branch/head evidence and recovery durability MUST govern fallback cleanup eligibility. | MUST | user-approved R3 direction | accepted |
| BC-R9 | Stacked children MUST remain recoverable and integrable when a merged parent branch is automatically deleted. Parent branch names remain provenance only; dependency satisfaction is proven from the integration target and exact Git evidence, followed by the existing integration refresh/reconciliation gate. | MUST | existing stacked-workstream authority | accepted |
| BC-R10 | If automatic deletion is unsupported, disabled or blocked by repository rules, integration MUST remain successful when the workstream is otherwise terminal; the surviving source branch is handled by fallback cleanup state rather than by weakening finalization or recreating refs. | MUST | resilience requirement | accepted |
| BC-R11 | Existing projects and historical workstreams MUST remain valid. No repository-wide migration or historical branch rename is required merely to adopt this contract. | MUST | backward compatibility | accepted |
| BC-R12 | Codex-only policy changes are outside this workstream. The accepted semantics may be ported later by the separate Codex-only workstream. | MUST | explicit user direction | accepted |

## Constraints

- GitHub repository settings are external repository configuration, not durable project-state authority.
- The currently available ChatGPT GitHub connector may not expose repository-setting mutation or Git-ref deletion/rename.
- Workflow correctness must therefore not depend on ChatGPT being able to delete or rename a branch itself.
- Current independent review, integration refresh, durable-state and terminal-recovery gates remain in force unless explicitly changed by these requirements.

## Non-goals

- creating delete/* marker branches;
- forcing physical deletion of every historical branch during this feature;
- changing Codex-only policy in this workstream;
- making a mutable global branch-cleanup registry;
- treating PR state alone as branch cleanup authority;
- requiring post-merge source-branch survival.

## Global invariants

1. Durable terminal recovery never depends on a branch that GitHub may automatically delete after merge.
2. Branch cleanup cannot make review/integration obligations disappear early.
3. The workstream manifest and selected Task Board remain durable authority; GitHub branch existence is runtime/repository state.
4. Cleanup marking never creates an additional Git ref.
5. A fallback safe_to_delete state is granted only after the exact branch/head has passed terminal safety checks.
6. Source branch deletion does not erase workstream provenance: the original branch name remains historical identity where current contracts already require it.

## External contracts / dependencies

- GitHub PR merge behavior and repository-level automatic deletion of merged head branches.
- GitHub branch protection/rulesets may prevent deletion of some refs.
- Exact PR number, merge commit/result and target ref are immutable/readable evidence inputs for post-merge reconciliation.

## Data integrity / idempotency / security constraints

- Re-running post-merge reconciliation after the source branch has disappeared must be idempotent.
- A surviving branch must never be force-renamed or force-overwritten merely to satisfy cleanup naming.
- If a fallback cleanup record points to a branch whose HEAD no longer matches its verified head, cleanup readiness is stale and must be revalidated.
- If an accidental delete/* duplicate and original branch both exist, the workflow must treat them as separate refs and reconcile them explicitly; same-SHA coincidence is not permission to guess.

## Acceptance-level requirements

### A — normal merged PR with auto-delete

- Workstream durable package and final reviewed subject are ready before merge.
- PR merges to the integration target.
- GitHub deletes the head branch automatically.
- Post-merge readback/reconciliation completes from target-side state and PR/merge metadata.
- Terminal recovery remains complete without the source branch.

### B — merged PR but branch survives

- PR merges successfully.
- Repository setting/rules leave the source branch present.
- Post-merge close still succeeds from target-side state.
- Exact surviving ref/head is recorded as safe_to_delete only after terminal safety is proven.
- No delete/* alias is created.

### C — closed/superseded without merge

- Workstream has explicit durable terminal closure/supersession.
- No live Card/Research/review/integration/recovery obligation remains.
- Required unique evidence/history exists independently of the branch.
- Exact branch/head may be marked safe_to_delete.
- Closed PR status alone is insufficient.

### D — stacked parent auto-deleted

- Parent workstream merges and its source branch disappears.
- Child keeps parent branch/workstream fields as provenance.
- Child proves required parent content is now present on its integration target.
- Child runs normal refresh/reconciliation and proceeds without needing the deleted parent ref.

### E — connector cannot delete/rename

- ChatGPT reaches terminal cleanup eligibility.
- It persists exact durable cleanup state/evidence.
- It does not create replacement refs.
- A later cleanup-capable actor may physically delete the branch.

## Definition completeness

GREEN.

- target state and all material MUST requirements are explicit;
- merged and non-merged terminal paths are distinguished;
- connector limitations do not change correctness;
- stacked-workstream behavior is covered;
- backward compatibility and Codex-only boundary are explicit;
- no unresolved user/product choice remains that can materially change planning.

## Downstream coverage

Planning must cover:
- terminal package/finalization ordering changes;
- workstream/manifest fallback cleanup schema;
- Close/Repository/Workstreams/Recovery semantics;
- GitHub auto-delete repository-setting guidance and capability fallback;
- regression scenarios for immediate post-merge branch disappearance and surviving/manual-cleanup branches.
