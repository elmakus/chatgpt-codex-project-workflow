# M01-T05 — cumulative M01 acceptance evidence

Date: 2026-09-22
Card: `M01-T05`
Result before independent review: **GREEN / review pending**
Target repository: `elmakus/project_workflow_v2`
Target branch: `feat/pwv2-m01-foundation`
Frozen target commit: `f1f4ed87875877529da6dc954e785d6373de7930`
Frozen target tree: `595a84ea2fcea446567ba7eff6f11474d6a33d29`
Target parent: `24bf91ce25f4a06a59b1cc674078094e69f57a35`

## Acceptance surface

This evidence evaluates the exact target commit above against:

- `implementation/workstreams/feature-common-preexecution-core/cards/M01-T05.md`;
- approved `planning/PROJECT_WORKFLOW_V2_MASTER_PLAN.md` §5 M01, §6 automated validation mapping and §7 JIT/risk register;
- M01-owned/supporting PWV2 requirements named by the Card;
- ADR-PWV2-001..006 where applicable to M01;
- accepted GREEN predecessor results M01-T01 through M01-T04;
- the S2 Execution Prep guidance recorded in `handoffs/EXECUTION_PREP_ENTRY_2026-09-22.md`.

This is deterministic M01 acceptance only. It does not claim L01-L09, M02+ lifecycle completeness, M05 delivery/update acceptance, migration, production adoption or custody transfer.

## Exact target readback

Immediately before freezing this acceptance subject, GitHub readback reported:

- `feat/pwv2-m01-foundation` HEAD = `f1f4ed87875877529da6dc954e785d6373de7930`;
- commit tree = `595a84ea2fcea446567ba7eff6f11474d6a33d29`;
- commit message = `feat(M01): add minimal obligation router`;
- combined commit status contained no registered status records.

No CI PASS is claimed from the empty combined-status response.

The local validation checkout fetched the same remote branch and proved local HEAD = remote HEAD before testing. The worktree was clean both before and after the suite.

## Cumulative deterministic validation

Executed against the exact frozen target commit:

`sh scripts/test.sh`

GREEN:
- preserved M01-T02 package/probe structural checks;
- state-envelope production validator and 8/8 state tests;
- production obligation router and 8/8 router tests;
- M01 baseline checks.

Executed independently as cumulative Python discovery:

`python3 -m unittest discover -v`

Result: **16/16 PASS**.

Additional deterministic checks:

- `python3 -m compileall -q tools tests` — PASS;
- removal of generated `__pycache__` followed by clean-tree verification — PASS;
- `git diff --check` — PASS;
- final `git status --porcelain` empty — PASS.

The tests invoke the production `tools/state_contract.py` validators and production `tools/router.py`; they do not use a parallel test-only workflow interpreter.

## A01-A04 M01 foundation mapping

### A01 — progressive disclosure foundation

GREEN foundation evidence:
- the production router read-set test requires only package router → project `PROJECT.md` → exact selected manifest → exact Task Board → current Card;
- unrelated migration material, templates and untrusted Issue text are excluded from the positive read set;
- future lifecycle owners are identified but explicitly unavailable until their owning milestones rather than being preloaded or guessed.

Full later lifecycle progressive-disclosure behavior remains with its owning milestones.

### A02 — no legacy routing foundation

GREEN foundation evidence:
- target has no `workflow/chatgpt_only` or `workflow/codex_only` semantic policy tree;
- production state validation rejects `execution_policy` and prohibited runtime/model/session/worker/scheduler-style state;
- equivalent durable state routes identically under different runtime/model/session environment noise;
- unimplemented routes fail closed rather than falling back to V1.

### A03 — binding / fail-closed foundation

GREEN foundation evidence:
- wrong workstream ID and wrong original branch fail validation;
- wrong-class, missing and cross-workstream locators fail validation;
- path escape, missing selection and ambiguous selection route to the M01 Recovery boundary;
- no root/default Task Board fallback is used.

### A04 — one-Card foundation

GREEN foundation evidence:
- the production state validator rejects a Task Board with more than one `in_progress` Card;
- no Project-Card scheduler/lane mechanism is required or introduced.

Full delegation/execution behavior remains M03-owned.

## Applicable V1 disposition / DROP evidence

M01 proves or preserves the applicable negative boundaries without reintroducing dropped V1 machinery:

- no fixed product-policy semantic trees;
- no canonical `execution_policy`;
- no runtime/model/session/worker identity as workflow authority;
- no `active_execution`, lane/batch/scheduler state or Context Health lifecycle in canonical state;
- no mutable global workstream registry or second construction Task Board;
- no ordinary fallback to root/default mutable state;
- no test-only semantic workflow engine.

The state validator provides executable negative checks for prohibited policy/runtime/scheduler keys. Router fixtures provide executable fail-closed and runtime-neutral routing checks. Repository tree/readback supplies non-code evidence for absence of a competing construction Task Board and global registry.

Fixture-local `implementation/workstreams/sample-workstream` paths are disposable test data only and are never target construction authority.

## Feasibility-probe preservation after T03/T04

The accepted T02 feasibility result remains empirical feasibility evidence, not M05/L04/L05 acceptance.

A diff from T02 result commit `221e4e93c3df3fe006880f4ade5c250eb356c8e9` to the frozen M01 commit over:

- `.codex-plugin`;
- `.agents`;
- `skills`;
- `hooks`;
- `scripts/test-plugin-probe.sh`

returned no changed paths. Therefore T03/T04 did not alter the package metadata, Skill identity, hook implementation or probe script that produced the T02 isolated-host result.

The current `hooks/session-start.py` was additionally executed against the frozen working tree:
- with the real package root it emitted bounded SessionStart bootstrap context pointing to the current bundled `workflow/ROUTER.md`;
- with a disposable package root lacking that router it emitted the required blocking/fail-closed package error.

No live user plugin/config/trust state was mutated by T05.

## Deferred obligations

Not accepted by this M01 evidence:

- full Intake/Brainstorming/Research/Definition/Planning semantics (M02);
- full execution/delegation/review/recovery semantics (M03);
- Close/integration/terminal recovery (M04);
- production delivery/update propagation and L01-L05 (M05);
- bounded V1 migration (M06);
- full A01-A17 plus L06-L09 qualification/adoption/custody transfer (M07).

## Review freeze

The implementation context found no deterministic M01 failure requiring a target code change.

The immutable implementation subject for independent M01 review is therefore:

- target repository: `elmakus/project_workflow_v2`;
- target commit: `f1f4ed87875877529da6dc954e785d6373de7930`;
- target tree: `595a84ea2fcea446567ba7eff6f11474d6a33d29`;
- acceptance contract: exact `M01-T05` Card plus the authority slice named above;
- acceptance evidence: this exact file/blob once persisted.

The implementing chat does not issue the required independent verdict.
