# M05-T02 — Workstream finalization semantics implementation evidence

Date: 2026-09-19

## Exact implementation subject

- Repository: `elmakus/chatgpt-codex-project-workflow`
- Branch: `fix/workstream-finalization-semantics`
- Subject: `8ff477b62e104f5a632a7f7546c3afa245bd953b`
- Integration target at freeze: `main@6b0445256b417f82431fb7b2704f56691eb4e7ae`
- Compare at freeze: branch ahead 24, behind 0

The exact subject above contains the workflow-semantic changes. Commits after this subject are allowed only for evidence/review/PR state unless a new semantic correction re-freezes a new subject.

## Implemented correction

The existing branch-isolated model is completed without changing its accepted core architecture:

1. workstream layout now includes a namespaced `handoffs/` directory;
2. branch-isolated cumulative handoffs canonically use `implementation/workstreams/<id>/handoffs/MXX_HANDOFF.md`;
3. root `project-handoffs/MXX_HANDOFF.md` and `PROJECT.md -> Latest cumulative handoff` are explicitly legacy/default-context conventions;
4. final-target integration must retain a terminal workstream package containing the manifest, selected Task Board and required workstream-owned contracts/evidence/handoffs;
5. source-branch deletion is gated on target-side closure/readback and absence of active obligations;
6. terminal `status: done` recovery may use the integration-target copy after source-branch deletion while preserving the original workstream branch as manifest/Task Board provenance;
7. root `implementation/TASK_BOARD.yaml` remains untouched by branch-isolated state unless the default context itself is explicitly selected;
8. long-lived pre-workstream branches receive a GREEN-boundary migration rule that namespaces only branch-owned post-divergence state, preserves shared historical root artifacts, restores target-side default board/latest-handoff semantics before merge, and retains genuine project-wide authority/source changes.

## Verification performed

### Scope/diff check

Compare `main...fix/workstream-finalization-semantics` at freeze:
- status: ahead;
- behind: 0;
- changed files are limited to ChatGPT-only finalization/recovery/repository contracts, handoff/project/workstream templates, README/changelog and this workstream's own durable state/contracts;
- no Codex/mixed/legacy execution-policy module was changed.

### Handoff collision check

Active ChatGPT-only modules/templates were scanned for the former unconditional global handoff convention.

Result: GREEN.

The remaining `project-handoffs/MXX_HANDOFF.md` references in changed active contracts are explicitly scoped to legacy/default context. Branch-isolated paths are namespaced under the selected workstream.

### Recovery/binding check

Result: GREEN.

- non-terminal state still requires the exact source workstream branch;
- manifest ↔ Task Board identity still requires exact `workstream_id` and original `execution_ref.branch`;
- integrated terminal `done` state has an explicit target-side recovery path after source-branch deletion;
- terminal recovery does not reinterpret root `implementation/TASK_BOARD.yaml` as the deleted workstream's state.

### Legacy migration compatibility check

Result: GREEN.

The migration rule explicitly distinguishes:
- branch-owned post-divergence state that must move/copy into the workstream namespace;
- shared historical root artifacts already present on target, which may remain referenced in place;
- target-owned root Task Board and project-global latest-handoff pointer, which the workstream merge must preserve;
- genuinely project-wide requirements/decisions/plans/source changes, which remain part of the integrated result.

This directly covers the class of repository where a long-running pre-workstream feature branch and current target branch both contain divergent root `implementation/TASK_BOARD.yaml` history.

### Template/readme coherence

Result: GREEN.

- `templates/PROJECT.md` scopes `Latest cumulative handoff` to legacy/default.
- `templates/HANDOFF.md` is selected-state-context aware.
- workstream templates preserve original branch identity after integration.
- README and changelog describe namespaced handoffs and terminal target-side recovery.

## Review requirement

REQUIRED.

Reason: the correction touches core durable-state ownership, branch deletion, recovery, migration and integration-finalization semantics. The implementing chat must not independently review this subject.
