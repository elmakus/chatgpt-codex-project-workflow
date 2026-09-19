# Feature Intake — Branch deletion-ready prefix

- Workstream ID: `feature-branch-delete-prefix`
- Kind: `feature`
- Integration target: `main`
- Base: `elmakus/chatgpt-codex-project-workflow@d64d8c1d7f05ce2a2584ffcb3ade4634263bbc95`
- Classification: independent
- Parent workstream: none
- Status: complete

## Operator intent

Add ChatGPT-only workflow instructions for terminal merged/closed branches so agents no longer leave ambiguous stale branch names behind. When a branch is proven safe for removal, its branch name should receive a `delete/` prefix (for example `feat/x` → `delete/feat/x`) so humans and later cleanup automation can distinguish deletion-ready branches from active work.

Apply this feature to the current `chatgpt_only` policy first. Do not modify `feat/codex-only-policy` as part of this workstream; the Codex-only branch will later port the accepted rule separately.

## Pre-creation discovery

- Current authoritative workflow baseline is `main`.
- No existing branch or PR matching this exact feature was found.
- Existing `feat/codex-only-policy` is related only as a future consumer of the accepted policy; this feature does not require parent-only Codex state.
- Current ChatGPT-only finalization already defines when a source branch is safe to delete after integration, but it does not define a durable deletion-ready naming transition. Existing repository history also contains manually prefixed `delete/*` branches, demonstrating the desired operational convention without making it normative.

## Base/dependency classification

Independent workstream based directly on current `main`.

- `parent_workstream: null`
- `parent_branch: null`
- `parent_dependency: null`

## Feature discovery path

This is a workflow-policy feature, not a micro-fix. Preserve the normal feature exploratory lifecycle.

Exploration covered:
- exact eligibility gate for applying `delete/`;
- merged/integrated terminal branches versus intentionally closed/superseded unmerged branches;
- rename/move semantics preserving exact source HEAD identity;
- collision/idempotency behavior for `delete/<old-name>`;
- ChatGPT-only finalization/close/repository policy surfaces;
- explicit boundary that this workstream does not port the rule into Codex-only policy.

## Downstream materialization

- Canonical Brainstorming record: `brainstorming/BRANCH_DELETE_PREFIX.md`
- Scope/revision: `branch-delete-prefix@R1`
- Brainstorming status: `ready_for_definition`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`
- `PROJECT.md -> Active exploratory scope` points to that exact record.

Next route: ChatGPT-only Brainstorming promotion gate.
