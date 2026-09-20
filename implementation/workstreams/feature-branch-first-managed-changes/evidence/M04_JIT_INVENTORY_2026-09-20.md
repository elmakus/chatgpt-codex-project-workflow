# M04 JIT inventory — integrated closure residuals

Date: 2026-09-20
Milestone: `M04 — migration, documentation, dogfood and integrated regression closure`
Plan revision: `BF-R3`

## Predecessor state

- M01 GREEN: branch-first state model, generic managed-change entry and integrated-root boundary.
- M02 GREEN: ChatGPT-only lifecycle is workstream-local; historical root/default execution state is migration-only.
- M03 GREEN: Codex-only lifecycle is workstream-local; historical root/default execution state is migration-only.
- Both fixed-policy implementations preserve policy-local review/recovery semantics and branch → PR → merge integration.

## Residual inventory

The final branch readback identifies bounded closure work rather than another lifecycle redesign.

### Must reconcile

1. `README.md`
   - still describes root `implementation/TASK_BOARD.yaml` as an active ChatGPT-only mutable authority/fallback;
   - still says existing projects may continue in legacy/default single-workstream mode;
   - still places active exploratory/pre-execution Research routing in root `PROJECT.md`;
   - needs branch-first generic-entry/trivial-change examples and historical-migration wording consistent with M01–M03.

2. Root `PROJECT.md`
   - still carries `Active exploratory scope` / `Active research obligation` mutable-routing fields;
   - still names root `implementation/TASK_BOARD.yaml` as current Task Board;
   - still says this repository actively uses the legacy/default state model;
   - needs to become the dogfood integrated-project index while retaining historical root Task Board/handoff navigation only as history/recovery.

3. `CHANGELOG.md`
   - current ChatGPT-only workstream entry says legacy/default projects are preserved without forced migration;
   - add a new branch-first managed-change entry that records the fixed-policy target model and makes the later change explicit without rewriting historical release notes.

4. Integrated regression/absence checks
   - add focused repository tests over README/root PROJECT/template/bootstrap/router surfaces so the fixed policies cannot regress to root/default new-work routing or root PROJECT mutable pre-execution ownership;
   - preserve mixed/non-migrated legacy routing where still intentionally policy-scoped.

### Already coherent; validate, do not redesign

- `templates/PROJECT.md`;
- `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md`;
- `prompts/CHATGPT_START.md`;
- Codex-only portion of `prompts/CODEX_START.md`;
- `workflow/CONTEXT_ROUTING.md`;
- `workflow/common/AUTHORITY.md`;
- migrated `workflow/chatgpt_only/*` and `workflow/codex_only/*` lifecycle contracts from M02/M03.

## JIT decomposition

One bounded implementation Card is sufficient because the residuals share one acceptance surface and no predecessor-dependent implementation split remains:

- `M04-T01 — Reconcile repository dogfood, documentation and integrated branch-first regressions`.

Final target refresh, manifest-owned final-integration review, PR/merge and target-side terminal reconciliation remain Close-owned and are deliberately excluded from the Card.
