# Project Workflow Codex Plugin — Master Plan

Revision: `PWCP-P1`
Status: `approved`
Updated: `2026-09-20`
Review requirement: `RECOMMENDED`

## Authority

- Requirements: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md` R1
- Packaging decision: `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_PACKAGING.md`
- Activation decision: `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_ACTIVATION.md`
- Exploratory provenance: `brainstorming/PROJECT_WORKFLOW_CODEX_PLUGIN.md`
- Workstream: `implementation/workstreams/feature-project-workflow-codex-plugin/WORKSTREAM.yaml`
- Branch: `feat/project-workflow-codex-plugin`
- Integration target: `main`

## Goal

Deliver a per-repository Codex plugin for Project Workflow that:

- is packaged from this repository;
- keeps normal Project Workflow files as the only workflow authority;
- provides one concise explicit `$pw` Skill;
- keeps Project Workflow active in enabled repositories through a very small always-on bootstrap/reminder;
- preserves progressive disclosure;
- reuses qualified generic marketplace/update evidence;
- verifies and documents whether `#issue/#feature` remain the preferred intake syntax or whether the supported fallback must be `$pw issue/$pw feature`.

## Execution baseline

- Project Workflow already has a dedicated `workflow/codex_only/` policy namespace on `main`.
- The repository itself remains `execution_policy: chatgpt_only`.
- Git-backed Codex plugin/Skill distribution and Workstation marketplace refresh are treated as qualified platform baseline where unchanged.
- The feature is independent of currently unrelated workstreams and starts from base `cdaf47245e45836917b152904d70807bca355e7d`.
- Current-runtime plugin packaging, lifecycle-hook/trust behavior and directive reliability must be verified against the actual Codex runtime before implementation choices are frozen.

## Inherited invariants

1. Do not duplicate `workflow/codex_only/*` semantics into the Skill.
2. Do not create a separate plugin updater.
3. Do not silently affect repositories where the plugin is not enabled.
4. Do not preload the whole workflow tree to guarantee activation.
5. Do not create multiple alias Skills when one `$pw` wrapper with arguments suffices.
6. Keep exact Project Workflow routing through `PROJECT.md` and `workflow/CONTEXT_ROUTING.md`.
7. Treat current plugin-platform baseline evidence as reusable only where the mechanism is unchanged.

## Milestone M01 — Current-runtime plugin and activation contract

### Outcome

Establish and verify the smallest current Codex packaging/activation design that satisfies the accepted Definition before production packaging is implemented.

### Requirement ownership

- PWCP-REQ-001
- PWCP-REQ-003
- PWCP-REQ-004
- PWCP-REQ-005
- PWCP-REQ-006
- PWCP-REQ-007
- PWCP-REQ-014
- PWCP-REQ-015

### Planned work packages

1. Verify exact current portable-plugin layout accepted when the plugin source is this repository.
2. Verify how a plugin-owned Skill resolves its installed plugin root and reads sibling canonical workflow files.
3. Compare supported always-on candidates:
   - plugin lifecycle hooks;
   - minimal repository instruction/bootstrap surface;
   - smallest reliable combination.
4. Verify trust/review behavior for the selected activation candidate.
5. Define a bounded always-on context budget and prove the candidate does not load the workflow tree eagerly.
6. Verify enabled versus control-repository behavior.
7. Persist the selected concrete packaging/activation contract as implementation evidence; escalate to Definition only if a hard platform constraint contradicts the accepted same-repo/always-on architecture.

### Acceptance

- one concrete current-runtime packaging layout is proven;
- one concrete activation mechanism satisfies enabled-repo persistence and control-repo isolation;
- plugin-root → canonical workflow path resolution is proven;
- trust behavior is understood and testable;
- no Definition change is needed.

### JIT trigger

Execution Prep creates concrete Cards after checking the then-current Codex plugin/hook format and existing `newproject-skill`/marketplace baseline evidence.

## Milestone M02 — Same-repo plugin package and canonical wrapper

### Outcome

Implement the Project Workflow plugin package in this repository with one thin `$pw` Skill and no copied workflow policy.

### Dependencies

- M01 GREEN.

### Requirement ownership

- PWCP-REQ-001
- PWCP-REQ-002
- PWCP-REQ-003
- PWCP-REQ-010
- PWCP-REQ-011
- PWCP-REQ-013
- PWCP-REQ-015

### Planned work packages

1. Add the current-runtime plugin manifest/package structure to this repository.
2. Add one concise `pw` Skill whose only responsibilities are bootstrap/entry resolution and delegation to canonical Project Workflow routing.
3. Add the selected minimal activation/reminder implementation from M01.
4. Add/update marketplace metadata required to distribute this Git-backed plugin through the existing marketplace model.
5. Add deterministic path/update tests proving ordinary `workflow/codex_only/*` changes require no Skill edit.
6. Keep updater ownership in Workstation; add no plugin-local timer/updater.

### Acceptance

- plugin installs/enables through the accepted marketplace source;
- `$pw` is discoverable and routes into canonical Project Workflow;
- canonical workflow modules remain single-source;
- workflow-module update propagation works without changing the Skill when bootstrap semantics are unchanged;
- no plugin-local updater exists.

## Milestone M03 — Always-on lifecycle, intake UX and progressive-disclosure acceptance

### Outcome

Prove normal enabled-repository use is reliable and choose/document the shortest verified intake UX.

### Dependencies

- M02 GREEN.

### Requirement ownership

- PWCP-REQ-004
- PWCP-REQ-005
- PWCP-REQ-006
- PWCP-REQ-007
- PWCP-REQ-008
- PWCP-REQ-009
- PWCP-REQ-010
- PWCP-REQ-012
- PWCP-REQ-014

### Planned work packages

1. End-to-end enabled-repository test: ordinary prompt enters Project Workflow without explicit `$pw`.
2. Fresh-session and supported resume/compaction tests.
3. Control-repository test proving no accidental activation without plugin enablement.
4. Progressive-disclosure evidence showing the always-on path loads only bootstrap/router/current-route context rather than the full workflow tree.
5. Comparative intake tests:
   - `#feature <goal>` vs `$pw feature <goal>`;
   - `#issue <problem>` vs `$pw issue <problem>`.
6. Select the documented user convention from evidence:
   - prefer `#feature/#issue` when reliably equivalent;
   - otherwise document `$pw feature/$pw issue`.
7. Verify `$pw` remains a valid general explicit entry/recovery path.
8. Reuse generic marketplace/install/updater evidence by exact reference and run only Project Workflow-specific delta tests.

### Acceptance

- always-on behavior is reliable over the tested lifecycle;
- recurring context remains bounded;
- intake syntax decision is evidence-based and durably documented;
- control repo is unaffected;
- generic platform evidence is reused rather than redundantly recreated.

## Milestone M04 — Integrated acceptance and release readiness

### Outcome

Produce one reviewed, integration-ready Project Workflow plugin subject whose package, usage contract and acceptance evidence are internally consistent.

### Dependencies

- M01–M03 GREEN.

### Requirement ownership

- all PWCP requirements.

### Planned work packages

1. Reconcile final usage/install documentation with the tested syntax and trust behavior.
2. Run the complete feature acceptance matrix from the approved requirements.
3. Verify no stale duplicate workflow semantics exist in Skill/bootstrap files.
4. Run final integration refresh against current `main`.
5. Freeze the exact workstream-level final integration subject.
6. Obtain the required/recommended independent implementation/final-integration review under normal workstream review rules.
7. Integrate only after review and target-refresh gates are GREEN.

### Acceptance

- every PWCP requirement has exact evidence;
- documented commands match verified runtime behavior;
- package contains one canonical workflow authority path;
- final subject passes required/recommended review and integration refresh.

## Requirement coverage

| Requirement | Owner milestone(s) | Execution path |
|---|---|---|
| PWCP-REQ-001 | M01, M02 | runtime packaging verification → package implementation |
| PWCP-REQ-002 | M02, M04 | thin wrapper implementation → drift audit |
| PWCP-REQ-003 | M01, M02 | naming/layout verification → one Skill |
| PWCP-REQ-004 | M01, M03 | activation contract → lifecycle E2E |
| PWCP-REQ-005 | M01, M03 | context-budget contract → disclosure evidence |
| PWCP-REQ-006 | M01, M03 | lifecycle capability verification → resume/compaction E2E |
| PWCP-REQ-007 | M01, M03 | opt-in contract → control-repo E2E |
| PWCP-REQ-008 | M03 | directive comparison |
| PWCP-REQ-009 | M03 | fallback comparison/documentation |
| PWCP-REQ-010 | M02, M03 | explicit Skill implementation + E2E |
| PWCP-REQ-011 | M02 | marketplace packaging; no updater |
| PWCP-REQ-012 | M03, M04 | evidence-reference audit + delta suite |
| PWCP-REQ-013 | M02, M04 | update propagation test |
| PWCP-REQ-014 | M01, M03 | trust contract + lifecycle acceptance |
| PWCP-REQ-015 | M01, M02 | routing verification + wrapper implementation |

## Verification strategy

- Prefer deterministic repository/runtime tests over model-only narrative evidence.
- Where Codex behavior itself must be proven, use bounded end-to-end sessions with exact prompts and durable result evidence.
- Include at least one enabled test repository and one control repository without plugin enablement.
- Record context-loading evidence sufficient to show progressive disclosure behavior without relying on estimated token counts as workflow state.
- Reuse generic marketplace/updater acceptance by exact evidence pointer where applicable.
- Any change to the exact current-runtime mechanism after a reviewed subject requires refreshed affected verification.

## Migration / rollback

No project-state migration is required.

The plugin is opt-in per repo. During development, rollback is removal/disablement of the plugin package/marketplace entry or reversion of the workstream branch before integration. Existing Project Workflow repository semantics remain usable independently of the plugin package.

## Security / trust

- Treat plugin hooks or equivalent executable activation surfaces as privileged code requiring explicit review/trust according to the current Codex runtime.
- Keep hook/bootstrap scripts minimal and deterministic.
- Do not introduce new credentials for Project Workflow activation.
- Do not execute update logic from the Skill/hook; marketplace refresh remains Workstation-owned.

## OpenSpec boundary

Create/refine OpenSpec during Execution Prep only if the concrete activation/package implementation introduces a behavior/API/state contract that benefits from executable specification. Do not create speculative OpenSpec solely to mirror this plan.

## Pre-implementation planning audit

- Approved Definition is complete and internally consistent.
- Same-repo packaging, canonical-source and one-Skill choices are frozen.
- Exact current-runtime hook/instruction substrate is intentionally deferred to M01 evidence and bounded by accepted outcomes.
- No user/product choice remains that changes milestone architecture.
- Requirement coverage is complete.
- Control-repo isolation and trust behavior are explicitly covered.
- Update propagation and evidence reuse are explicit acceptance paths.
- No migration/data-loss or credential boundary is introduced.
- The plan avoids duplicating generic plugin certification.

Planning audit result: `GREEN`.

## Independent plan review

- Review requirement: `RECOMMENDED`
- Reason: this is a new Master Plan spanning plugin packaging, lifecycle activation, trust behavior and end-to-end workflow routing; independent review is practical.
- Review record: `planning/reviews/PWCP-P1.md`
- Plan remains `draft` until the exact subject receives GREEN independent review.
