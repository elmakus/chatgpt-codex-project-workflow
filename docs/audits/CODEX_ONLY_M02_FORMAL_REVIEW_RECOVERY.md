# Codex-only M02 — formal review and recovery scenario audit

Scope: M02 project/runtime boundary, formal independent review state, owning-Executor repair and runtime-decoupled recovery.

Authority:
- `requirements/CODEX_ONLY_POLICY.md` — CO-REQ-007..016, CO-REQ-024..025
- `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
- `planning/CODEX_ONLY_MASTER_PLAN.md#M02--projectruntime-boundary-formal-independent-review-state-and-recovery`
- `openspec/changes/codex-only-m02-formal-review-state/specs/formal-review-state.md`

## Canonical scenario

### 1. Implementation S1

Project state:

```yaml
implementation_owner_role: executor
review:
  requirement: RECOMMENDED
  current_attempt: R01
  attempts:
    - id: R01
      state: pending
      subject: S1
      reviewer_role: tester
      evidence: null
```

Runtime may map the project `executor` role to logical worker A1, but A1/session/model/profile identity is not Project Workflow state.

### 2. Independent review R01

Runtime supplies independent Tester B1. Main verifies independence and persists R01 `in_progress`. B1 reviews the complete S1 authority/acceptance surface and does not mutate production.

RED result:

```yaml
- id: R01
  state: red
  subject: S1
  reviewer_role: tester
  evidence: <R01-red-evidence>
```

R01 remains durable and immutable.

### 3. Owning-Executor repair

Main routes the bounded correction to the project's owning `executor` role. Tester B1 is not the repair owner.

The runtime may resume A1 or fail closed to a replacement Executor realization; Project Workflow state remains `implementation_owner_role: executor`.

Corrected production becomes exact subject S2.

### 4. New attempt R02

Main appends rather than overwrites:

```yaml
review:
  requirement: RECOMMENDED
  current_attempt: R02
  attempts:
    - id: R01
      state: red
      subject: S1
      reviewer_role: tester
      evidence: <R01-red-evidence>
    - id: R02
      state: pending
      subject: S2
      reviewer_role: tester
      evidence: null
```

R01 remains directly addressable.

### 5. Full independent recheck

When independence remains intact and runtime resume is safe, the same logical Tester B1 may realize R02. Otherwise `codex_workflow` may fail closed to replacement B2.

Both runtime paths have the same Project Workflow meaning:

- R02 is the same project attempt regardless of B1/B2 runtime realization;
- reviewer replacement does not create R03;
- the Tester performs a full applicable review of S2, not only the prior RED finding.

GREEN result:

```yaml
- id: R02
  state: green
  subject: S2
  reviewer_role: tester
  evidence: <R02-green-evidence>
```

Main may then perform post-review Card finalization if the finalized result still equals S2.

## Recovery matrix

| Durable boundary | Runtime condition | Required Project Workflow continuation |
| --- | --- | --- |
| R01 pending | B1 never started / lost | Keep R01/S1; safely realize an independent Tester; full review S1. |
| R01 in_progress | B1 session lost | Keep R01/S1; resume or replace runtime Tester; full review S1; no new attempt. |
| R01 RED durable | A1 unavailable | Preserve R01; runtime may replace Executor realization for the same project `executor` role; perform bounded repair once. |
| S2 durable, R02 missing | Main interrupted before freeze | Verify S2; append exactly one R02 pending; do not redo repair. |
| R02 in_progress + complete exact verdict evidence | Main interrupted before state write | Verify evidence identifies R02/S2 exactly; reconcile verdict, otherwise full re-review R02/S2. |
| R02 GREEN durable | B1/B2 runtime lost | Do not replay review; finalize only if result still equals S2. |
| Production changed after GREEN | any | Prior GREEN does not cover changed subject; append a new attempt when review still applies. |

## Independence / ownership assertions

- Codex Main is the sole shared Task Board/integration writer.
- Executor owns production implementation/repair, not shared state.
- Tester owns review judgment only, not production repair or shared state.
- Independence is a semantic requirement checked before `in_progress`; it is not represented by a required runtime identifier.
- Same logical Tester reuse is legal only while independence remains intact.
- Runtime replacement is fail-closed and transparent to Project Workflow semantics.
- A qualifying Codex-managed verdict needs no second normal-ChatGPT review.

## Forbidden Project Workflow state

Required schemas must not contain runtime identity/lifecycle keys such as:

- `session_id`
- `invocation_id`
- worker/model/profile/reasoning identifiers
- Muse lease/reservation IDs
- resume tokens/protocol state

M02 also must not introduce M03-owned `parallel_safe`, `write_scope`, `exclusive_resources`, compatible-ready-set, lane/worktree or bounded-parallel scheduling fields.

## Static verification contract

M02 verification must prove:

1. default and branch-isolated Task Board templates expose `implementation_owner_role` plus review requirement/current-attempt/attempt-list/subject/state/reviewer-role/evidence;
2. no forbidden runtime identity appears as a required schema key;
3. no M03 parallel field appears as a schema key;
4. `workflow/CONTEXT_ROUTING.md` and `workflow/chatgpt_only/` are unchanged versus current `main`;
5. root `PROJECT.md` remains `execution_policy: chatgpt_only`;
6. M02 changed contracts contain no active dependency on another policy namespace or legacy/shared execution contracts;
7. `git diff --check` and merge-conflict-marker scan are GREEN.

YAML parser validation should be reported only if an actual parser is available.
