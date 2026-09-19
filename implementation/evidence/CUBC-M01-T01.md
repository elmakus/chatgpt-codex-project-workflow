# CUBC-M01-T01 implementation evidence

Status: GREEN
Card: CUBC-M01-T01
Plan: CUBC-P1
Authority: CUBC-R1 + ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE

## Implemented contract surface

- `workflow/codex_only/WORKSTREAMS.md`
  - target-side terminal-unmerged history/recovery path;
  - durable closure package before deletion;
  - exact `WORKSTREAM.yaml.branch` as sole cleanup target;
  - Codex Main authenticated-`gh` deletion after existing safety gates;
  - no separate cleanup lifecycle/state.
- `workflow/codex_only/CLOSE.md`
  - explicit intentional terminal-unmerged Close shape;
  - ordered durable-package → readback → exact-ref delete → absence-readback sequence;
  - unchanged repository-owned merged cleanup path.
- `workflow/codex_only/RECOVERY.md`
  - idempotent branch-exists/delete versus branch-absent/complete recovery;
  - no ref recreation or heuristic target selection.
- `workflow/codex_only/ROUTER.md`
  - deterministic route for unfinished terminal-unmerged closure/delete.
- `workflow/codex_only/REPOSITORY.md`
  - terminal-unmerged target-side history remains recoverable after source deletion.

No WORKSTREAM schema change was required.

## Requirement audit

- CUBC-REQ-001: GREEN — intentional terminal-unmerged Close requires Codex Main to delete the exact manifest branch after safety/durability gates.
- CUBC-REQ-002: GREEN — live Card, Research, review, stacked-dependency, integration and other branch-requiring obligations block deletion.
- CUBC-REQ-003: GREEN — target comes only from exact manifest `branch`; prefix/naming/PR heuristics are explicitly forbidden.
- CUBC-REQ-004: GREEN — physical deletion is explicitly Main-owned through authenticated `gh`.
- CUBC-REQ-005: GREEN — Recovery deletes a surviving exact branch and treats an already-absent branch as completed cleanup without recreation.
- CUBC-REQ-006: GREEN — no separate cleanup lifecycle/field/registry is introduced.
- CUBC-REQ-007: GREEN — merged workstreams remain repository-auto-delete only; no Codex-only merged fallback was added.
- CUBC-REQ-008: GREEN — lifecycle action/state remains Codex Main-owned; runtime worker/session identity is not required durable state.

## Scenario audit

1. Terminal superseded/unmerged + all safety gates GREEN → namespaced target-side closure/history is persisted/read back → exact manifest branch deleted by Main through authenticated `gh` → absence read back: GREEN.
2. Interruption after durable closure before deletion → Recovery sees exact branch exists → completes delete/readback: GREEN.
3. Interruption after deletion → Recovery sees exact branch absent → no-op success, no recreation: GREEN.
4. Live stacked/dependency or other branch-requiring obligation → deletion blocked: GREEN.
5. Normal merged path → repository automatic deletion remains owner; no new Codex-only fallback lifecycle: GREEN.
6. Rejected/superseded implementation content → not merged merely to preserve cleanup history: GREEN.

## Regression / invariant audit

- Branch comparison against current `main`: ahead-only, `behind_by: 0` at verification time.
- `branch_cleanup` under inspected `workflow/codex_only/` contract/template/state surface: absent.
- `safe_to_delete` under inspected `workflow/codex_only/` contract/template/state surface: absent.
- No cleanup registry, alias-ref, branch-prefix cleanup heuristic or CAS/lease protocol introduced.
- `WORKSTREAM_TEMPLATE.yaml` unchanged.
- Existing integrated-terminal recovery remains intact and explicitly separate from terminal-unmerged recovery.
- No OpenSpec required; behavior is owned by the workflow Markdown lifecycle contracts.

## Verification limits

This Card changes repository workflow contracts only. No live branch was deleted and no external repository setting was changed as part of verification.
