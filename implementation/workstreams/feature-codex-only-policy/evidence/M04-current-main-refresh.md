# M04 current-main refresh assessment

Date: 2026-09-19
Workstream: `feature-codex-only-policy`
Frozen M04 implementation subject: `48a56cbd5554b1378fa3727449bfce94e2f7f1df`
Workflow/target main assessed: `d64d8c1d7f05ce2a2584ffcb3ade4634263bbc95`
Merge base: `6b0445256b417f82431fb7b2704f56691eb4e7ae`

## Why this refresh was required

After the Codex-only workstream began, `main` added the independent ChatGPT-only workstream-finalization correction. The change defines namespaced branch-isolated milestone handoffs, target-side terminal durable packages, source-branch deletion safety, terminal recovery after branch deletion, and bounded migration for long-lived pre-workstream branches.

This assessment checks whether that target evolution invalidates M01-M03, requires an M04 semantic correction before independent review, or changes the required M05/final-integration work.

## Current-main delta classification

The post-base `main` semantic change is concentrated in ChatGPT-only branch-isolated finalization/recovery plus shared documentation/templates. No new policy-neutral common execution contract or new lifecycle owner file was added.

The current `workflow/chatgpt_only/` namespace still has 22 owner files and `workflow/codex_only/` still has the same 22-file owner surface.

## M01-M03 impact

### M01

No re-open is required.

- namespace filename parity remains 22/22 against current main;
- no new policy-owner module was added by the main change;
- historical M01 review/evidence remains valid for its immutable subject;
- current semantic drift is a later lifecycle/finalization concern already inside M04/M05 authority.

### M02

No re-open is required.

Current Codex-only Review/State/Recovery contracts still preserve immutable exact review subjects, semantic implementation-owner/reviewer roles, Tester independence/non-repair, append-only prior attempts and no mandatory second normal-ChatGPT review.

The current-main finalization correction does not redefine those review/runtime-boundary invariants.

### M03

No re-open is required.

Current Codex-only Execution Prep/Execution/State/Recovery still preserve serial default, JIT finite compatible batches, frozen integration base/member order, disjoint write/resource proof, Main-only shared-state/integration writes, same-member retry, terminal launched-batch reconciliation and post-batch review-drain rules.

The current-main finalization correction changes workstream terminal packaging/recovery, not the bounded internal Card-batch model.

## M04 compatibility with the new main semantics

The frozen M04 subject already contains the relevant new terminal-workstream semantics:

- branch-isolated handoffs are namespaced under `implementation/workstreams/<id>/handoffs/`;
- root `project-handoffs/` and `PROJECT.md -> Latest cumulative handoff` are legacy/default-context conventions;
- final-target integration must preserve/read back the terminal namespaced workstream package;
- closure-only target-side reconciliation is allowed when actual integration-result metadata becomes known only after merge;
- source-branch deletion is gated on target readback and absence of active obligations;
- terminal `done` recovery may use the integration-target copy after source-branch deletion while preserving the original workstream branch as provenance;
- long-lived legacy branches receive the bounded GREEN/safe-boundary migration rule;
- no Codex-only contract imports ChatGPT-only/legacy/shared execution ownership.

Two textual differences from current ChatGPT-only modules are not semantic gaps:

- Codex-only Execution Prep does not contain a generic prior-handoff read rule at all, so it does not accidentally authorize the project-global latest-handoff pointer for branch-isolated work;
- Codex-only State does not contain the old unconditional source-branch recovery rule that required the ChatGPT-only correction. Terminal recovery ownership is explicit in Codex-only Workstreams/Recovery/Repository.

The Codex-only workstream Task Board template does not repeat the new provenance comment beside `execution_ref.branch`, but the normative Workstreams contract explicitly requires that value to remain the original workstream branch after integration. This is a documentation-level omission, not a contradictory state rule.

Conclusion: no M04 implementation correction is required solely because of the assessed main change. The pending independent review may continue against the existing frozen M04 implementation subject, using this refresh evidence in addition to the original M04 evidence.

## M05 / final-integration impact

The current Master Plan already authorizes the required adaptation through M05 P1/P3/P4/P5, so no Master Plan revision or Definition re-open is required.

M05 JIT preparation must explicitly include current-target compatibility checks for:

1. terminal namespaced handoff/package/recovery semantics introduced on main;
2. cross-policy regression against the then-current `main`;
3. merged-result semantic inspection, not only textual conflict detection;
4. reconciliation of project-global files whose workstream copy is stale relative to target state;
5. final target readback before source-branch deletion.

A concrete semantic conflict is already proven for future integration: a trial merge of the current feature branch with current `main` is textually conflict-free, but the merged `PROJECT.md` would select the feature branch's old Codex-only workstream status/authority pointers instead of the current target's global project status. M05 target refresh must preserve/reconcile the target-owned global project state while retaining Codex-only feature authority in its proper durable artifacts.

The target-side README and shared PROJECT/HANDOFF template updates are not feature-side changes from the merge base, so normal Git integration retains them. The root `PROJECT.md` is the material shared-state reconciliation item.

## Routing conclusion

- M01: keep accepted/done.
- M02: keep accepted/done.
- M03: keep accepted/done.
- M04-T01: keep current frozen implementation subject and pending independent-review gate.
- M05: after M04 closes GREEN, JIT-decompose an explicit current-main compatibility/final-integration refresh obligation under the already-approved M05 authority before final review/integration.
