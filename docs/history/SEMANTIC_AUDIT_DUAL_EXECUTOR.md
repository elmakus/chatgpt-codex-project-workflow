# Semantic Audit — Dual-Executor Project Workflow

**Status:** GREEN AFTER CORRECTIVE FIX — requires independent re-review  
**Audit date:** 2026-09-11  
**Baseline `main`:** `3374232680a9b8a3de440e08257e003bdd706cee` (v3.0.3 behavior)  
**Original frozen candidate:** `9bddfd1069a3cfca5d67eadba2b08391e7889aa1`  
**Corrective functional state audited here:** `66203365af6086a73faba54a20473768a74ebb64`

## 1. Corrective audit note

The original semantic audit marked the dual-executor branch GREEN but did **not** detect one real merge-blocking contradiction in runtime capability handling.

Independent review found that shared contracts could re-apply `workflow/chatgpt/CAPABILITY_GATE.md` after an already-assigned executor discovered a missing capability. That permitted a nonsensical Codex → ChatGPT fallback path.

This file supersedes the original capability-routing finding. The rest of the original audit remains valid unless contradicted below.

## 2. Correct capability model

Project routing now states the invariant:

`ChatGPT capabilities ⊆ Codex capabilities`

Consequences:

1. ChatGPT Capability Gate is a **pre-assignment routing mechanism**.
2. If ChatGPT has the required capability + evidence path, ChatGPT may execute the card.
3. If ChatGPT lacks the capability and `execution_policy = mixed`, the card may be assigned to Codex.
4. If Codex later discovers that a required capability is missing, there is no meaningful fallback to ChatGPT.
5. Runtime capability failure after assignment is therefore:

   `STOP → persist blocker/evidence → USER ACTION REQUIRED → user provides capability → resume same card/executor`

6. Runtime capability failure does not automatically invoke the ChatGPT Capability Gate and does not automatically change executor.

This correction does not add a new state, router, capability database, scoring model or fallback abstraction.

## 3. Corrective finding F-01 — PASS AFTER FIX

### Original conflict

At candidate `9bddfd1069a3cfca5d67eadba2b08391e7889aa1`:

- `workflow/EXECUTION.md` instructed a blocked executor to re-apply project policy through `workflow/chatgpt/CAPABILITY_GATE.md` before executor change;
- `workflow/contracts/GITHUB_STATE.md` similarly told missing-capability cards to re-apply the ChatGPT Capability Gate;
- `workflow/contracts/TASK_CARDS.md` did not clearly distinguish pre-assignment routing from runtime capability failure.

This contradicted the capability-superset architecture when the already-assigned executor was Codex.

### Corrective implementation

#### `workflow/EXECUTION.md` — PASS

Now states:

- the capability-superset invariant;
- Capability Gate is pre-assignment only;
- runtime missing capability stops affected work safely;
- exact missing MCP/access/credential/runtime/tool/test/readback/evidence capability is persisted;
- card becomes `blocked` when contract cannot be met;
- `USER ACTION REQUIRED` names the smallest concrete capability/access/configuration needed;
- the same card resumes with the same assigned executor after the user provides the capability;
- Codex runtime failure must not invoke `workflow/chatgpt/CAPABILITY_GATE.md` or fall back to ChatGPT.

Failure recovery now preserves the same runtime-blocker semantics.

#### `workflow/contracts/GITHUB_STATE.md` — PASS

Blocked-card semantics now explicitly separate:

- **before assignment:** ChatGPT Capability Gate may route according to project policy;
- **after assignment/start:** missing capability is a runtime blocker, not a routing event.

For Codex runtime failure:

- blocker/evidence is persisted;
- `USER ACTION REQUIRED` is surfaced;
- same Codex card resumes after capability is supplied;
- ChatGPT Capability Gate is not re-applied;
- Codex → ChatGPT fallback is explicitly invalid under the capability-superset invariant.

A corresponding invalid-state invariant was added for accidental Codex runtime fallback to ChatGPT.

#### `workflow/contracts/TASK_CARDS.md` — PASS

Now explicitly distinguishes:

- ChatGPT Capability Gate before assignment;
- runtime capability failure after assignment.

It records the capability-superset invariant and requires Codex runtime capability failure to become durable `BLOCKED / USER ACTION REQUIRED`, followed by continuation of the same Codex card after the user provides the missing capability.

#### `workflow/chatgpt/CAPABILITY_GATE.md` — PASS

The existing gate now explicitly records the same invariant and its lifecycle boundary:

- the gate belongs to normal ChatGPT before card assignment;
- it may route ChatGPT → Codex under `mixed`;
- it is not a runtime fallback mechanism;
- if Codex verifies at runtime that a required capability is absent, the assigned Codex card blocks and waits for user-provided capability rather than falling back to ChatGPT.

No new routing outcome was added.

## 4. Architecture regression checks

### A. One workflow repository — PASS

No second ChatGPT workflow repo, Codex workflow repo, shared-core repo or capability registry was introduced.

### B. Execution policy — PASS

Exactly two project policies remain:

- `chatgpt_only`;
- `mixed`.

New projects default to `chatgpt_only`; changing to `mixed` requires explicit user decision.

### C. Capability Gate outcomes — PASS

The only routing outcomes remain:

- `EXECUTE IN CHATGPT`;
- `HANDOFF TO CODEX` under `mixed`;
- `BLOCKED`.

Runtime Codex capability failure is **not** a fourth routing outcome. It is ordinary blocked-card execution state plus `USER ACTION REQUIRED`.

### D. ChatGPT full-executor semantics — PASS

ChatGPT may execute when the current normal ChatGPT chat actually has all required capabilities, tests/checks and evidence/readback path.

### E. Codex specialized-executor semantics — PASS

Codex may receive work under `mixed` for missing ChatGPT capability, material repo/runtime advantage or explicit approved assignment.

The correction does not make Codex the default for all technical work.

### F. ChatGPT Work exclusion — PASS

Project Workflow still uses normal ChatGPT chat + Codex only. ChatGPT Work is not an executor, routing target, fallback, capability provider, dependency or migration target.

## 5. Progressive disclosure regression checks

### ChatGPT path — PASS

`CHATGPT.md → PROJECT.md → CONTEXT_ROUTING → shared phase module → ChatGPT-specific module only when applicable`

### Codex path — PASS

`CODEX_START → PROJECT.md → CONTEXT_ROUTING → shared execution/contracts → workflow/codex/*`

Codex still does not automatically load `CHATGPT.md` or `workflow/chatgpt/*`.

The corrective change does not require Codex to load the ChatGPT Capability Gate during runtime failure; it explicitly forbids doing so.

## 6. v3 execution-semantics regression checks

Still preserved:

- card states `planned | ready | in_progress | blocked | done | superseded` — PASS;
- separate decision state — PASS;
- milestone lifecycle and GREEN semantics — PASS;
- Task Board as durable execution index — PASS;
- executor provenance — PASS;
- result pointers/evidence/tests summary before `done` — PASS;
- Definition of Done coupling — PASS;
- dependency blocking — PASS;
- deterministic READY progression — PASS;
- Refresh Gate — PASS;
- JIT OpenSpec — PASS;
- integrated milestone acceptance — PASS;
- RED corrective work — PASS;
- cumulative handoff/checkpoint/implementation HEAD — PASS;
- durable failure recovery — PASS;
- optional `current.md` remains non-authoritative — PASS;
- strategic `request_id` + `DECISION FOR CODEX:` behavior remains available where configured — PASS;
- `codex_workflow` remains authority only for internal Codex runtime orchestration — PASS.

## 7. New-semantics regression checks

Still preserved:

- optional `required_capabilities` only where materially useful — PASS;
- executor provenance — PASS;
- `WRITE → READBACK → VERIFY EXPECTED STATE → EVIDENCE` — PASS;
- independent-review tiers — PASS;
- optional Path A / Path B / Hybrid pattern — PASS;
- no new research lifecycle states — PASS;
- no capability registry/database — PASS;
- no executor scoring — PASS;
- no generic scheduler — PASS.

## 8. Runtime capability scenarios

### Scenario A — ChatGPT has capability

`mixed` or `chatgpt_only` + ChatGPT has work/test/evidence path → `EXECUTE IN CHATGPT`.

**PASS.**

### Scenario B — ChatGPT lacks capability, mixed project

Capability Gate may route card to Codex.

**PASS.**

### Scenario C — ChatGPT lacks capability, chatgpt_only project

Card remains BLOCKED until user supplies capability or explicitly changes project policy.

**PASS.**

### Scenario D — Codex discovers missing MCP/access/credential/runtime/tooling

Required behavior:

`BLOCKED → durable blocker/evidence → USER ACTION REQUIRED → user supplies missing capability → same Codex card resumes`

No ChatGPT fallback and no ChatGPT Capability Gate re-entry.

**PASS AFTER CORRECTIVE FIX.**

### Scenario E — session recovery while Codex card is capability-blocked

Recovery reads durable blocker/card/executor state and continues the same Codex card once the missing capability exists.

**PASS AFTER CORRECTIVE FIX.**

## 9. Scope of corrective change

Functional corrective commit:

`66203365af6086a73faba54a20473768a74ebb64`

Files changed by the corrective semantic fix only:

- `workflow/EXECUTION.md`;
- `workflow/contracts/GITHUB_STATE.md`;
- `workflow/contracts/TASK_CARDS.md`;
- `workflow/chatgpt/CAPABILITY_GATE.md`.

No production lifecycle redesign, new abstraction, new execution state, new policy or unrelated cleanup was introduced.

## 10. Audit limitations

This remains a semantic/document-contract audit, not an executable formal proof.

It can verify that normative workflow text is internally consistent at the audited commit. It cannot prove that every future ChatGPT or Codex runtime will obey those instructions.

No automated CI/test suite, end-to-end project migration, live ChatGPT→Codex execution, or capability-provisioning integration test is claimed by this audit.

Independent re-review should inspect the corrective diff directly against frozen candidate `9bddfd1069a3cfca5d67eadba2b08391e7889aa1` and verify that no other fallback wording remains in normative execution contracts.

## 11. Conclusion

**GREEN AFTER CORRECTIVE FIX, PENDING INDEPENDENT RE-REVIEW.**

The merge-blocking capability contradiction identified by independent review is corrected in functional state `66203365af6086a73faba54a20473768a74ebb64`.

The previous GREEN finding was incomplete because it failed to distinguish pre-assignment ChatGPT routing from post-assignment Codex runtime capability failure.

No merge to `main` is part of this audit.
