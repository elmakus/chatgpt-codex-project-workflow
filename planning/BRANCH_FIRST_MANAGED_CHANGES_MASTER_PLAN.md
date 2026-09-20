# Master Plan — branch-first managed changes

Revision: `BF-R1`
Status: `draft`
Updated: `2026-09-20`
Independent plan review: `RECOMMENDED`

> Planning organizes the approved Definition in `requirements/BRANCH_FIRST_MANAGED_CHANGES.md`. ADR-BF-001 through ADR-BF-003 remain authoritative.

## 1. Accepted target / canonical inputs

- Requirements: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` — Revision R1, `approved`
- Accepted decisions:
  - `decisions/ADR_BRANCH_FIRST_MANAGED_CHANGE_LIFECYCLE.md` (ADR-BF-001)
  - `decisions/ADR_WORKSTREAM_LOCAL_ROUTING_STATE.md` (ADR-BF-002)
  - `decisions/ADR_POLICY_LOCAL_BRANCH_FIRST.md` (ADR-BF-003)
- Brainstorming provenance: `brainstorming/branch-first-managed-changes.md`
- Workstream: `implementation/workstreams/feature-branch-first-managed-changes/WORKSTREAM.yaml`
- Integration target baseline: `main` at workstream creation commit `808084a4c7989715f7ee4889a31bce28f778d597`

## 2. Execution baseline

Current workflow main has:
- migrated policy namespaces for both `chatgpt_only` and `codex_only`;
- branch-isolated workstream manifests/Task Boards and target-refresh/terminal-package semantics in both policies;
- explicit `#issue` / `#feature` intake that creates branches before downstream work;
- legacy/default root `implementation/TASK_BOARD.yaml` fallback still presented as a valid state context in both fixed policies;
- root `PROJECT.md` active exploratory and pre-execution Research pointers;
- policy-neutral `workflow/common/*` limited to genuinely shared contracts;
- current project instance itself still carrying historical legacy/default Task Board pointers on `main`.

Implementation must convert the fixed-policy active paths to branch-first-only without removing historical compatibility evidence or importing one policy's lifecycle semantics into the other.

## 3. Inherited constraints / non-goals / invariants

- `main` / integration target is integrated truth only.
- Every new managed change uses branch → PR → merge, including trivial changes.
- Read-only exploration may occur before a workstream exists.
- Natural-language change authorization must trigger generic workstream creation/recovery without requiring markers.
- `#issue` / `#feature` remain supported shortcuts.
- Legacy/default state remains readable only for recovery/migration; it is never a new-work destination.
- Workstream-local mutable lifecycle state must not use root `PROJECT.md` as a global registry.
- Terminal workstream packages remain on the integration target.
- No new shared cross-policy lifecycle module.
- Preserve ChatGPT-only fresh-chat review semantics.
- Preserve Codex-only Codex Main / worker / bounded-batch semantics.
- Preserve stacked dependency, target refresh, PR integration and source-branch-deletion safety.
- Do not rewrite completed historical evidence merely to normalize layout.
- `workflow/legacy/*` for policies not yet migrated is outside the meaning of “legacy/default mode” in this scope and is not removed solely by this change.

## 4. Milestones

### M01 — branch-first state model and generic managed-change entry contracts

**Outcome:** workflow contracts have one branch-first new-work model, one neutral generic managed-change entry, and workstream-local pre-execution routing state.

**Requirement ownership:** REQ-BF-001..011, REQ-BF-015..017.

**Dependencies:** none.

**Acceptance / checkpoint:**
- both fixed-policy workstream manifest schemas can represent a neutral generic managed change and the active pre-execution routing pointers needed for Brainstorming/Research/Definition/Planning recovery;
- deterministic generic branch/workstream naming exists for unclassified changes (planned default: `kind: change`, branch `work/<slug>`; explicit issue/feature naming remains unchanged);
- policy routers recognize clear natural-language managed-change authorization before any integration-target mutation and route to create/recover the branch-isolated workstream;
- read-only requests do not create branches merely for asking/analysis;
- exact existing workstream locators recover instead of duplicating work;
- active fixed-policy contracts no longer describe legacy/default root Task Board as a valid destination for new work;
- root `PROJECT.md` target contract contains integrated project-level navigation only; active exploratory/pre-execution Research ownership is moved to selected workstream state;
- genuinely policy-neutral integration-target/branch-first invariant is reconciled in `workflow/common/AUTHORITY.md` only if needed; no common Intake/Workstreams/lifecycle module is created.

**Planned work packages:**
- reconcile `workflow/CONTEXT_ROUTING.md`, root `CHATGPT.md`/Codex start/bootstrap surfaces as required for the new entry invariant;
- extend ChatGPT-only and Codex-only `WORKSTREAM_TEMPLATE.yaml` / workstream contracts with neutral kind/naming and pre-execution routing ownership;
- redefine legacy/default fallback as recovery/migration-only;
- establish generic managed-change entry semantics in each policy-local Intake/Router contract;
- define root `PROJECT.md` integrated-truth contract and exact workstream-local pointer ownership.

**JIT trigger:** repository-wide reference inventory of active-path uses of `implementation/TASK_BOARD.yaml`, `Active exploratory scope`, `Active research obligation`, explicit-marker-only Intake language and legacy/default fallback before Task Card split.

**Planning re-evaluation trigger:** current fixed-policy routing cannot express generic branch-first entry without a structural phase split beyond Intake/Router/Workstreams.

**Definition re-open trigger:** implementing generic entry requires user-visible mandatory syntax/classification or permits direct managed writes to the integration target.

### M02 — ChatGPT-only lifecycle migration

**Outcome:** `chatgpt_only` runs the complete managed-change lifecycle on the selected workstream branch from discovery through integration, with no new-work root/default fallback.

**Requirement ownership:** REQ-BF-002..009, REQ-BF-011..014, REQ-BF-016..017 plus ChatGPT-only part of REQ-BF-015.

**Dependencies:** M01 checkpoint.

**Acceptance / checkpoint:**
- Brainstorming/Research/Definition/Planning/plan-review recovery obtains active workstream-local pointers from the selected manifest/records rather than root `PROJECT.md`;
- explicit promotion to Definition remains user-owned, but authorization is recovered from the workstream-local exploratory record;
- pre-execution Research return ownership is workstream-local and crash-safe;
- Execution Prep always materializes a workstream Task Board and never creates/selects root `implementation/TASK_BOARD.yaml` for new work;
- an encountered historical/default board is classified as migration/recovery input and further mutation occurs only after safe workstream migration;
- micro-fix remains proportionate while still branch/PR-only;
- independent plan review and implementation/final-integration review keep existing fresh-chat independence semantics on the exact branch;
- target refresh + terminal durable package still permit source-branch deletion without losing recovery.

**Planned work packages:**
- update `ROUTER.md`, `INTAKE.md`, `WORKSTREAMS.md`, `REPOSITORY.md`;
- update Brainstorming/Research/Definition/Planning/Plan Review pointer ownership and fresh-session locator rules;
- update Execution Prep/State/Recovery/Close/Micro-fix where they still assume default board or project-global pre-execution pointers;
- migrate templates/prompts specific to ChatGPT-only;
- add focused static/behavioral validation for generic intake, no-default-new-work and workstream-local recovery.

**JIT trigger:** after M01, use the actual reference graph to split pointer-owner changes from execution-state migration where independent.

**Planning re-evaluation trigger:** ChatGPT-only fresh-review boundaries require a different durable locator architecture than the selected manifest can support.

**Definition re-open trigger:** preserving review independence requires root mutable project state or permits direct target writes.

### M03 — Codex-only lifecycle migration

**Outcome:** `codex_only` uses the same branch-first product invariant while preserving Codex Main ownership and policy-specific concurrency/review mechanics.

**Requirement ownership:** REQ-BF-002..009, REQ-BF-011..014, REQ-BF-016..017 plus Codex-only part of REQ-BF-015.

**Dependencies:** M01 checkpoint; may proceed after M02 contract lessons are known, but must not import ChatGPT-only modules.

**Acceptance / checkpoint:**
- generic natural-language managed-change entry creates/recovers a Codex-only workstream before durable change mutation;
- pre-execution Brainstorming/Research/Definition/Planning routing is workstream-local rather than root-`PROJECT.md` mutable state;
- no new work selects the root legacy/default Task Board;
- existing legacy/default state is recovery/migration-only;
- Codex Main remains sole shared workstream Task Board/integration-state writer;
- bounded M03-style Card concurrency semantics (where currently authorized) remain intact within a selected workstream and do not weaken branch isolation;
- independent Tester semantics remain exact-subject based and policy-local;
- target refresh, terminal target-side package and Codex-only branch-deletion semantics remain GREEN.

**Planned work packages:**
- update Codex-only `ROUTER.md`, `INTAKE.md`, `WORKSTREAMS.md`, `REPOSITORY.md`;
- update pre-execution lifecycle modules and Research ownership;
- update Execution Prep/State/Recovery/Close and Codex handoff/bootstrap surfaces;
- update templates/prompts and focused validations without referencing ChatGPT-only lifecycle modules.

**JIT trigger:** inspect Codex-only-specific default-board/pointer references plus batch/review/cleanup contracts after M01 schema is stable.

**Planning re-evaluation trigger:** branch-first migration conflicts with Codex Main integration ownership or existing bounded-batch invariants.

**Definition re-open trigger:** correct Codex-only behavior would require a different user-facing branch-first rule than ChatGPT-only.

### M04 — migration, documentation, dogfood and integrated regression closure

**Outcome:** repository documentation, templates, examples and the workflow repository's own project state consistently use the branch-first-only model; integrated validation is GREEN.

**Requirement ownership:** all REQ-BF-001..017, with primary ownership for REQ-BF-010, REQ-BF-013, REQ-BF-016 and documentation/absence acceptance.

**Dependencies:** M02 and M03 checkpoints.

**Acceptance / checkpoint:**
- README, policy router, prompts/templates and active workflow docs contain no statement that legacy/default is a normal new-work option under either fixed policy;
- root `PROJECT.md` template/contract no longer requires active workstream-local exploratory/Research pointers;
- generic entry examples cover the motivating flow: read-only upstream/fork comparison → “use Project Workflow to introduce these changes” → automatic workstream branch before durable Definition/Planning writes;
- explicit `#issue` / `#feature` examples remain valid shortcuts;
- trivial-change path demonstrates branch/PR integration without requiring unnecessary full Master Planning;
- current workflow repository dogfoods the resulting model: this workstream's terminal namespaced package is retained on `main`, historical root legacy/default artifacts are preserved only as history, and root project navigation no longer advertises legacy/default as active state;
- repository-wide scans find no active fixed-policy fallback that can create/select new root default state;
- all available validation/check suites are GREEN;
- final target refresh is performed against current `main`; semantic/text conflicts are reconciled inside accepted authority;
- final integration is through PR only, with the required final-integration review gate and target-side terminal package/readback before source branch cleanup.

**Planned work packages:**
- README/CHANGELOG/docs/prompt/template reconciliation;
- migration/recovery guidance for existing root/default state;
- static reference/contract scans;
- run all repository validation available after implementation;
- reconcile this repository's own `PROJECT.md` and terminal workstream package for the new invariant.

**JIT trigger:** final changed-file/reference scan after M02/M03 to define residual docs/tests/migration cards.

**Planning re-evaluation trigger:** integrated scan reveals a hidden active-path dependency that changes milestone sequencing but not Definition.

**Definition re-open trigger:** migration would require deleting historical evidence or allowing an exception to branch/PR-only managed changes.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Planned work package / JIT |
|---|---|---|
| REQ-BF-001 | M01/M04 | integration-target invariant + absence scan |
| REQ-BF-002 | M01/M02/M03 | generic entry and branch-before-write routing |
| REQ-BF-003 | M01 | read-only versus managed-change transition |
| REQ-BF-004 | M01/M02/M03 | optional markers + natural-language intake |
| REQ-BF-005 | M01 | neutral workstream kind/naming |
| REQ-BF-006 | M01/M02/M03 | full-lifecycle workstream routing |
| REQ-BF-007 | M01/M02/M03/M04 | default-state recovery/migration-only conversion |
| REQ-BF-008 | M01/M02/M03/M04 | root PROJECT integrated-truth contract |
| REQ-BF-009 | M01/M02/M03 | manifest-local mutable routing |
| REQ-BF-010 | M04 | canonical root artifact merge semantics/docs |
| REQ-BF-011 | M01/M04 | PR-only integration across all change sizes |
| REQ-BF-012 | M02/M03/M04 | preserve target refresh/conflict verification |
| REQ-BF-013 | M02/M03/M04 | retain terminal package |
| REQ-BF-014 | M02/M03/M04 | source-branch cleanup safety |
| REQ-BF-015 | M01/M02/M03 | policy-local realization + narrow common invariant |
| REQ-BF-016 | M01/M04 | bootstrap/adoption branch-first |
| REQ-BF-017 | M01/M02/M03/M04 | durable recovery without transcript |

Potential OpenSpec candidates: manifest pre-execution routing schema and generic managed-change entry/legacy-migration state transitions. Resolve JIT in Execution Prep; do not create OpenSpec solely for prose-only changes.

## 6. Dependency / execution order

`M01 → (M02, M03 policy-local migrations) → M04`.

M02 and M03 share the M01 state model but remain policy-local. Under the current `chatgpt_only` executor, concrete Cards execute serially within this selected workstream even if policy-local implementation packages are conceptually independent.

## 7. Migration / rollback strategy

- All implementation remains on `feat/branch-first-managed-changes`; `main` is unchanged until PR merge.
- Preserve existing historical root `implementation/TASK_BOARD.yaml`, root handoffs and completed evidence unless a safe migration explicitly moves active state.
- Existing projects encountered with legacy/default active state are recovered, then migrated to a new branch-isolated workstream before further managed-change mutation.
- Do not silently reinterpret historical default-state records as a workstream.
- Maintain deterministic idempotent recovery when branch creation succeeds but workstream state persistence partially fails.
- Rollback before integration is branch/commit based; final integration uses existing target-refresh and review gates.

## 8. System verification strategy

Verification is layered:
1. focused contract/reference checks after M01;
2. ChatGPT-only route/recovery scenarios after M02;
3. Codex-only route/recovery/concurrency scenarios after M03;
4. repository-wide active-path static scans for forbidden new-work fallback/pointer language;
5. prompt/template consistency checks;
6. any existing repository validation/CI scripts discovered during Execution Prep;
7. final target refresh against current `main`;
8. independent Card/milestone/final-integration review as required by policy.

Key scenario matrix:
- read-only comparison does not create a branch;
- subsequent natural-language authorization creates branch/workstream before durable change state;
- explicit `#issue` and `#feature` still work;
- generic change uses neutral identity without guessing;
- trivial change still PR-merges;
- legacy/default input routes to migration/recovery, not new execution;
- active pre-execution recovery works from workstream manifest/records, not root mutable pointers;
- merged terminal package supports recovery after source branch deletion.

## 9. Data integrity / idempotency / security strategy

- Exact branch/workstream identity must be recovered before mutation.
- Generic intake collision handling remains deterministic.
- No mutable global workstream registry.
- Partial branch/state creation must be recoverable without duplicate workstreams.
- Legacy migration must preserve historical provenance and unrelated workstream state.
- PR-only integration and target refresh protect the integrated truth boundary.
- Terminal cleanup requires target-side durable readback.

## 10. Explicit authorization boundaries

The user has authorized implementation of this workflow redesign.

No direct integration-target writes are authorized by that approval. Final repository integration must occur through a pull request and merge.

Repository-hosting configuration changes such as enabling GitHub branch protection/rulesets are not required by this plan and would be a separate external configuration action if later desired.

## 11. JIT / deferred decomposition map

- M01 Cards: materialize from the exact router/intake/workstream/template/reference graph.
- M02 Cards: materialize after M01 from ChatGPT-only pointer/default-board reference inventory.
- M03 Cards: materialize after M01 from Codex-only pointer/default-board and concurrency/reference inventory.
- M04 Cards: materialize after M02/M03 from integrated diff, stale-reference scan and discovered validation commands.

Do not create speculative future Cards whose scope depends on predecessor inventories.

## 12. Fresh-context boundaries

This new material Master Plan requires independent review. The authoring chat must stop after freezing BF-R1 and its review record.

Later fresh ChatGPT review boundaries follow normal `chatgpt_only` review and Context Health rules.

## 13. Pre-implementation planning audit

- Definition Complete: GREEN; requirements R1 approved, ADR-BF-001..003 accepted, no open user/product questions.
- False assumptions / P0-P1 risks: broad stale references to default-board and PROJECT-owned pre-execution pointers; policy-local differences; bootstrap edge cases; generic-intent ambiguity. Each has explicit milestone/verification coverage.
- Milestone boundaries/order: M01 freezes shared product/state model, M02/M03 perform policy-local realization, M04 closes migration/docs/integration.
- Dependency completeness: GREEN; policy migrations depend on M01 state contract.
- Outcome-level acceptance: explicit for all milestones.
- Requirement coverage: REQ-BF-001..017 fully mapped.
- Migration/rollback: preserves historical state, forces active legacy migration before mutation, branch-local rollback before PR.
- System verification: scenario matrix + policy-local checks + integrated scan/target refresh.
- Data integrity/idempotency/security: duplicate prevention, partial-creation recovery, target readback and branch-deletion safety covered.
- Authorization gates: implementation authorized; direct target writes prohibited; PR-only integration explicit.
- OpenSpec boundaries: schema/state-machine candidates identified for JIT.
- Overengineering/premature detail: no speculative Task Card IDs or exact file edit list frozen before reference inventory.
- Remaining blockers: none.

## 14. Workflow references

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref used to author this plan: current `main` plus this branch's approved Definition
- Policy: `chatgpt_only`
- Workstream: `implementation/workstreams/feature-branch-first-managed-changes/WORKSTREAM.yaml`
- Project Definition authority: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` + ADR-BF-001..003
- Plan review lifecycle: `workflow/chatgpt_only/PLAN_REVIEW.md`

The Master Plan is not the live task tracker. Mutable execution state will be created only after plan approval through workstream-local Execution Prep.
