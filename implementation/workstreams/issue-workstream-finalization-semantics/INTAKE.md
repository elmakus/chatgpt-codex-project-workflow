# Issue Intake — Workstream finalization semantics

- Workstream ID: `issue-workstream-finalization-semantics`
- Kind: `issue`
- Integration target: `main`
- Base: `elmakus/chatgpt-codex-project-workflow@6b0445256b417f82431fb7b2704f56691eb4e7ae`
- Classification: independent
- Parent workstream: none
- Status: complete

## Operator intent

Resolve the ambiguity in ChatGPT-only branch-isolated workstream finalization so a finished workstream can be integrated to the target branch, its branch can be safely deleted, and its durable Task Board, milestone handoffs, evidence and recovery history remain unambiguous without colliding with other workstreams that also use milestone IDs such as M01/M02.

The concrete workstation repository is evidence that exposes the ambiguity; the solution must remain general and workflow-level.

## Diagnosis

Current `main` establishes branch-isolated manifests and workstream Task Boards, and explicitly preserves workstream-specific state as durable history unless a future archival policy is added.

However, the finalization surface is incomplete:

1. `workflow/chatgpt_only/CLOSE.md` still defines the cumulative handoff canonical location globally as `project-handoffs/MXX_HANDOFF.md`.
2. `templates/PROJECT.md` still exposes one project-wide `Latest cumulative handoff` pointer without defining how it behaves when independent workstreams each have their own M01/M02.
3. The workflow says a branch-isolated workstream remains durable/recoverable, but it does not explicitly require the terminal manifest/Task Board/evidence/handoff state to be present on the final integration target before deleting the source branch.
4. The migration guidance preserves legacy/default projects but does not fully define how to integrate a long-lived branch that started before branch-isolated layout, mutated root `implementation/TASK_BOARD.yaml`, and must not overwrite the integration target's own legacy/default board.
5. Existing workstream layout namespaces cards/evidence/blockers but does not namespace milestone handoffs, creating a collision path across independent workstreams.

## Existing authority/evidence

- `requirements/CHATGPT_ONLY_MULTI_WORKSTREAM_INTAKE.md` R2, R3, R12 and R15.
- `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`.
- `workflow/chatgpt_only/WORKSTREAMS.md`.
- `workflow/chatgpt_only/REPOSITORY.md`.
- `workflow/chatgpt_only/CLOSE.md`.
- `workflow/chatgpt_only/STATE.md`.
- `templates/PROJECT.md` and `templates/HANDOFF.md`.
- Concrete compatibility test: a repository may have a current target-side legacy/default root Task Board while an older long-lived feature branch also carries divergent root Task Board history.

## Base/dependency classification

This issue is present on current workflow `main`; it does not require unmerged state from `feat/codex-only-policy` or any other active workstream. It is therefore an independent workstream based directly on current `main`.

## Path classification

The initial diagnosis considered reopening Project Definition because the missing rules affect durable state ownership. Authority reconciliation against the already-approved multi-workstream scope proves that no new product/system intent is required:

- R2 already requires durable, isolated workstream identity/state;
- R3 preserves the legacy/default root board;
- R12 requires transcript-independent durable recovery;
- R15 requires safe migration rather than implicit reinterpretation;
- the accepted ADR makes branch-isolated state durable history and rejects global mutable workstream state;
- approved M05 explicitly owns templates, migration and regression closure.

Therefore the missing finalization/namespace rules are a corrective completion of already-approved M05 authority, not a new Definition choice.

- Path: normal corrective continuation
- Next route: `execution_prep:M05-T02`
- Materialized downstream state: `implementation/workstreams/issue-workstream-finalization-semantics/TASK_BOARD.yaml`
- Card: `implementation/workstreams/issue-workstream-finalization-semantics/cards/M05-T02.md`

## Boundaries

Included:
- terminal durable state after branch-isolated integration;
- canonical handoff/evidence namespace;
- role of root `implementation/TASK_BOARD.yaml`;
- role of `PROJECT.md -> Latest cumulative handoff`;
- safe source-branch deletion;
- bounded migration rule for pre-workstream legacy branches.

Excluded:
- workstation-specific cleanup itself;
- a mutable global workstream registry;
- rewriting already-completed historical evidence solely for cosmetic consistency;
- changes to Codex/mixed execution policy.

## Resolved classification

The collision-free canonical convention to implement is workstream-local handoff ownership under the same workstream namespace as its Task Board/cards/evidence. Legacy/default global handoffs remain valid in place. This is an implementation-level completion of the accepted branch-isolation model, not a new global registry or product-level choice.
