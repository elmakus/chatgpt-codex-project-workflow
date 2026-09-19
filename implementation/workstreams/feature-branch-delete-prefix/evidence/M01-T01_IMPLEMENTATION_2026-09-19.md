# M01-T01 implementation evidence — source-branch-independent terminal cleanup

## Exact implementation subject

- Behavioral implementation head: `6441fa08a6a6e94fc568ec4804e12582e2adcd96`
- Refreshed implementation baseline: `main@92e9f162c3d2fe4b178b04f07edc439c12a33ce8`
- Card acceptance surface: `implementation/workstreams/feature-branch-delete-prefix/cards/M01-T01.md#Acceptance`
- Approved requirements: `requirements/CHATGPT_ONLY_BRANCH_CLEANUP.md` — BC-R1 through BC-R12
- Accepted decision: `decisions/ADR_CHATGPT_ONLY_AUTODELETE_MERGED_HEAD_BRANCHES.md`
- Approved plan: `planning/CHATGPT_ONLY_BRANCH_CLEANUP_MASTER_PLAN.md` — BC-R1 / M01

The independent review subject is the exact behavior-file blob set below together with the M01-T01 acceptance surface. Later review/state/evidence bookkeeping commits do not change this behavioral subject.

### Exact behavior-file blobs

- `workflow/chatgpt_only/WORKSTREAMS.md` — `ef10dd2e519e668c1fff7ea713068fe8eb471bdd`
- `workflow/chatgpt_only/CLOSE.md` — `e326d9dcda8239ba4a301ec986d5adfc5e6f87ca`
- `workflow/chatgpt_only/RECOVERY.md` — `e11c2c56c526412181a7261eb83fcafb6f3e1a9e`
- `workflow/chatgpt_only/STATE.md` — `82e1b1e9f33f28331d899ddf7661c0c2a1a28537`
- `workflow/chatgpt_only/ROUTER.md` — `40ff2c99ed5d738bff36a8e147d1108fb2b4a49d`
- `workflow/chatgpt_only/REPOSITORY.md` — `85584c87e73872215c4be5281924951ffe79829b`
- `workflow/chatgpt_only/WORKSTREAM_TEMPLATE.yaml` — `cca3d9ae50333803504e6ee742b0749a2c99c46d`
- `README.md` — `5977f6de32fc952c96b38b3f6106fbc2dc981d90`

## Implementation summary

The ChatGPT-only finalization/recovery contract now makes a branch-isolated source ref disposable immediately after successful final-target merge.

- Before merge, the exact merge subject carries the closure-ready namespaced workstream package and every unique recovery artifact already knowable.
- After merge, immediate GitHub deletion of the PR head is normal. Closure/recovery continues from the merge-result target-side package plus immutable PR/merge evidence; the source ref is never recreated for bookkeeping.
- A surviving merged branch or terminal unmerged branch uses only an optional manifest-local `branch_cleanup` fallback with exact original ref, verified HEAD and durable evidence.
- `safe_to_delete` is stale if the surviving ref HEAD moves.
- Terminal-unmerged cleanup history must be durable independently of the ref it authorizes deleting; normally a closure-only namespaced target-side package preserves metadata/history without integrating rejected/superseded implementation content.
- `delete/*`/same-SHA alias rename emulation is explicitly forbidden.
- Stacked children prove an integrated parent's dependency from target + exact Git/PR evidence and never require the deleted parent ref.
- Original manifest/Task Board source-branch identity remains provenance after deletion.
- Legacy/default and completed historical workstreams remain valid; no repository-wide migration is introduced.
- Repository automatic-head-delete configuration and physical fallback deletion remain separate external writes.

## Static/coherence verification

Baseline comparison `92e9f162... → 6441fa08...`: GREEN, 0 commits behind the refreshed baseline.

Changed behavioral workflow surfaces are limited to:
- `workflow/chatgpt_only/WORKSTREAMS.md`
- `workflow/chatgpt_only/CLOSE.md`
- `workflow/chatgpt_only/RECOVERY.md`
- `workflow/chatgpt_only/STATE.md`
- `workflow/chatgpt_only/ROUTER.md`
- `workflow/chatgpt_only/REPOSITORY.md`
- `workflow/chatgpt_only/WORKSTREAM_TEMPLATE.yaml`
- `README.md`

Other branch changes are this feature's durable brainstorming/Definition/planning/review/workstream/Card state. No `workflow/codex*` policy file changed.

Exact contract checks: GREEN.
- immediate merged-head disappearance is normal success;
- post-merge pre-terminal recovery exists and routes target-side;
- closure-ready package + knowable handoff state is required before final-target merge;
- fallback schema is workstream-local and exact-ref/head/evidence bounded;
- moved HEAD invalidates cleanup readiness;
- terminal-unmerged marker survives deletion independently of the ref;
- no alias rename path exists;
- stacked parent deletion is explicitly covered;
- legacy/default fallback remains intact;
- auto-delete configuration / physical deletion remain separate external operations;
- no mutable global cleanup registry was introduced;
- source branch fields remain provenance;
- no old active contract phrase still requires closure/readback before GitHub may delete the merged source branch.

GitHub reports no commit statuses and no pull-request-triggered workflow runs for the exact behavioral head; this workstream's required verification is therefore the durable contract/coherence audit above rather than an unreported CI result.

## Acceptance scenario audit

### A — merged PR with GitHub auto-delete

GREEN. Pre-merge Close requires the closure-ready namespaced package in the exact merge subject. If GitHub deletes the source head immediately after merge, Router/Workstreams/Recovery select the merge-result target-side package using immutable PR/merge evidence and Close completes result/readback without recreating the source ref.

### B — merged PR but branch survives

GREEN. Finalization succeeds independently of source-branch deletion. Only after terminal target-side readback/no-live-obligation checks may the exact surviving ref/head be recorded as `branch_cleanup.state: safe_to_delete`. A later cleanup actor must re-read HEAD before deleting; movement invalidates readiness.

### C — closed/superseded without merge

GREEN. Closed PR status alone is insufficient. Explicit terminal state, no live obligation, exact ref/head proof and a closure/history package durable independently of the source ref are required before `safe_to_delete`. Rejected/superseded implementation content is not merged merely to preserve metadata.

### D — stacked parent auto-deleted

GREEN. Parent branch/workstream fields remain provenance. Once parent content is proven on the child's integration target, the child reconciles against that target and runs the normal integration refresh; the deleted parent ref is not required.

### E — connector cannot rename/delete

GREEN. Workflow correctness ends at durable cleanup eligibility. It neither creates a second `delete/*` alias nor assumes ChatGPT can physically delete/rename refs. A cleanup-capable actor may later delete an exact verified surviving ref.

## BC-R1..BC-R12 coverage result

GREEN.

- BC-R1/2/4/5: closure-ready pre-merge durability + post-merge target-side recovery/reconciliation.
- BC-R3/10: GitHub auto-delete preferred when available; surviving branch remains successful via fallback.
- BC-R6/8: exact terminal `safe_to_delete` eligibility; closed PR alone never sufficient.
- BC-R7: alias-based rename explicitly forbidden.
- BC-R9: stacked parent deletion/reconciliation covered.
- BC-R11: legacy/default/historical compatibility preserved.
- BC-R12: Codex-only files/behavior outside this workstream and unchanged.

## Result

Implementation-owned verification: GREEN.

M01-T01 remains non-terminal until its RECOMMENDED independent Card review is GREEN. This evidence is implementation-owned and is not an independent verdict.
