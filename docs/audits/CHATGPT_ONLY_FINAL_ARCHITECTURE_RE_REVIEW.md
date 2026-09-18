# Fresh independent architecture/coherence re-review — ChatGPT-only final audit blockers

Date: 2026-09-18

- Workflow authority reconstructed from: `main@cec0b384af2436890c2ee7a6f395a1131ddae1c8`
- PR: `#26`
- Review branch: `fix/chatgpt-only-final-audit-blockers`
- Frozen semantic review subject: `c5552ad8be69b4648bb8c24b24219ba41b371baa`
- Review method: fresh repository-backed architecture/coherence review of the exact frozen subject. The start prompt, PR body, prior audit verdicts, remediation narrative and implementation self-validation were treated only as locators/history, not as proof.

Verdict: **GREEN**

## Subject freeze and diff coverage

GitHub reported the review branch HEAD as exactly `c5552ad8be69b4648bb8c24b24219ba41b371baa` at review start and again before evidence persistence.

The branch is based on current `main@cec0b384af2436890c2ee7a6f395a1131ddae1c8`, is 61 commits ahead and 0 behind, and the complete semantic diff contains 19 files:

- `README.md`
- `prompts/CHATGPT_START.md`
- `templates/PROJECT.md`
- `templates/RESEARCH.md`
- `templates/TASK_BOARD.yaml`
- `workflow/RESEARCH.md`
- `workflow/chatgpt_only/BRAINSTORMING.md`
- `workflow/chatgpt_only/DEFINITION.md`
- `workflow/chatgpt_only/EXECUTION.md`
- `workflow/chatgpt_only/EXECUTION_PREP.md`
- `workflow/chatgpt_only/PLANNING.md`
- `workflow/chatgpt_only/PLAN_REVIEW.md`
- `workflow/chatgpt_only/RECOVERY.md`
- `workflow/chatgpt_only/REPOSITORY.md`
- `workflow/chatgpt_only/RESEARCH.md`
- `workflow/chatgpt_only/REVIEW.md`
- `workflow/chatgpt_only/ROUTER.md`
- `workflow/chatgpt_only/STATE.md`
- `workflow/chatgpt_only/TASK_BOARD_TEMPLATE.yaml`

The full current `workflow/chatgpt_only/*` path was inspected in context, including unchanged close/context-health/Task-Card contracts, not only changed hunks.

## B-01 — review precedes Card done

**GREEN.**

The state machine now has one coherent terminal boundary:

- REQUIRED/RECOMMENDED implementation remains non-terminal while review is `pending | in_progress | red`;
- the implementation chat freezes the exact immutable subject as `review_state: pending` and stops before self-review;
- GREEN ends the reviewer role and returns through the router;
- an `in_progress + green` Card routes to Execution for exact-subject Post-review Card finalization;
- `done + pending|in_progress|red` is explicitly invalid;
- subject drift after GREEN cannot reuse the old verdict and must create a new review attempt;
- persisted RED is classified from durable evidence, and a correction already durably completed before a crash is not re-executed merely to rediscover continuation;
- if the corrected subject exists but the next pending review attempt was not frozen before crash, recovery routes to Execution reconciliation only to freeze that new exact review boundary.

No path was found that can legally mark a REQUIRED/RECOMMENDED Card `done` before GREEN.

## B-02 — durable Research lifecycle and crash/restart E2E

**GREEN.**

The policy-local Research record owns stable ID, `active | blocked | complete | consumed`, exact Origin role/subject, exact Return target, and reconciliation state/result. Pointer ownership is split deterministically:

- pre-execution Brainstorming / Definition / Planning / plan-review Research → `PROJECT.md → Active research obligation`;
- Execution Prep / implementation / recovery Research → Task Board `research_obligation`;
- implementation/recovery obligations are never mirrored into PROJECT.

The following required scenarios were traced across exact state-transition boundaries:

1. **completed Research → execution_resolution → execution:<subject> — PASS.**  
   Classifier rewrites only the Return target while keeping `Status: complete`, reconciliation pending and the Task Board pointer. Execution is then the final owner and must reconcile before consume/clear.

2. **completed Research → execution_resolution → execution_prep:<subject> — PASS.**  
   Same classifier rule; Execution Prep has an explicit idempotent final-target handler.

3. **completed R1 → execution_resolution → more Research R2 — PASS.**  
   The sole classifier-consumption exception is one durable Git transition that sets R1 reconciliation applied with exact R2 ref, consumes R1, creates R2 active and switches the Task Board pointer directly R1→R2.

4. **crash before classifier-to-R2 atomic transition — PASS.**  
   Recovery still sees R1 `complete` + pointer R1 and retries classification. No durable R2 exists and there is no lost pointer.

5. **crash after atomic R1-consumed / R2-active / pointer-switch transition — PASS.**  
   Recovery sees R2 active and cannot recreate R2 from R1.

6. **crash after durable final-target reconciliation but before Research consumed/pointer clear — PASS.**  
   Final target mutation and `Return reconciliation: applied` + exact result refs are one durable transition. Re-entry with `applied + complete` is consume/clear-only and must not replay target work.

7. **correction completed before crash — PASS.**  
   Recovery/review classification explicitly checks current durable state and does not repeat a correction whose failing condition is already reconciled. Execution final-return logic likewise recognizes already-durable correction/result/review evidence and only closes missing reconciliation state.

8. **pending/in_progress/green/red review coexisting with stale-complete Research pointer — PASS.**  
   Pending/in-progress review keeps priority. For GREEN/RED, stale completed Research is reconciled/consumed before later Card finalization/correction classification. A matching downstream review state is explicit evidence that old Research-return correction already crossed its review boundary and must not be replayed.

9. **chained Research with a final owning Return target — PASS.**  
   The current record is reconciled first, then the old record is consumed and the next exact active record replaces the owning pointer atomically. Recovery always sees either the old obligation or the new one.

10. **all final Return-target consumption boundaries — PASS.**  
    Brainstorming, Project Definition, Strategic Planning, Execution Prep and Execution all explicitly invoke the same final-target protocol: verify exact pointer/subjects, inspect reconciliation state before mutation, persist target result + applied marker atomically, then consume/clear only after that transition is durable.

11. **Execution Prep → Research handoff before role yield — PASS.**  
    Execution Prep initializes a minimal policy-local Task Board when necessary, creates the exact Research record and persists Task Board `research_obligation` in the same durable transition before returning to the router.

The requested classifier invariants all hold:

- no null-pointer gap;
- no two simultaneously active Research obligations on a legal chain transition;
- no `R1 complete` after pointer switch to R2;
- no legal R2 recreation after crash/restart once the switch is durable;
- `execution_resolution` cannot consume a completed record except for the one explicitly defined classifier-to-Research chain transition.

## B-03 — policy isolation

**GREEN.**

Lifecycle/routing semantics for ChatGPT-only Brainstorming, Research and Project Definition are policy-local:

- `workflow/chatgpt_only/BRAINSTORMING.md`
- `workflow/chatgpt_only/RESEARCH.md`
- `workflow/chatgpt_only/DEFINITION.md`
- `workflow/chatgpt_only/ROUTER.md`
- `workflow/chatgpt_only/REPOSITORY.md`

A structural scan of every `workflow/common/*` file found **zero** occurrences of:

- `chatgpt_only`
- `Active research obligation`
- `research_obligation`
- `execution_resolution`
- `Return reconciliation`
- the ChatGPT-only Research lifecycle tuple
- `Definition promotion authorization`

Thus common remains policy-neutral and does not create ChatGPT-only continuation state for legacy/mixed/codex-only routes.

A structural scan of every `workflow/chatgpt_only/*` file found **zero** imports/fields for:

- Capability Gate;
- `bounded_parallel` / `parallel_card_limit`;
- lane/write-scope/exclusive-resource scheduling;
- `workflow/legacy`;
- `workflow/codex`;
- shared `workflow/EXECUTION.md`;
- shared `workflow/contracts/TASK_EXECUTION.md`.

The ChatGPT-only Task Board scaffold is serial-only and policy-local.

### Shared template / README regression check

`templates/RESEARCH.md` exposes optional continuation metadata only when the selected policy explicitly requires it and explicitly states that the shared template does not create routing semantics. Its ChatGPT-only pointer paragraph is descriptive and says pointer ownership/lifecycle are defined by the selected policy route, not by the template.

`workflow/RESEARCH.md` explicitly prevents legacy routes from adopting PROJECT/Task-Board Research pointers merely because the shared template exposes those optional fields.

`templates/PROJECT.md` likewise marks Active research obligation as policy-activated and tells legacy/other-policy routes without that contract to keep it `none`.

README documents the migrated ChatGPT-only ownership while preserving legacy/other-policy semantics until those namespaces migrate.

No policy-isolation regression was found.

## Regression audit

The complete active ChatGPT-only path was checked for interaction with:

- Brainstorming → explicit Definition promotion;
- Definition GREEN → Planning;
- plan-review lifecycle;
- JIT L1/L2 refinement boundaries;
- exactly-one-`in_progress` serial execution;
- review independence;
- Context Health precedence;
- milestone close/publication;
- automatic deterministic continuation;
- recovery without prior transcript authority.

No new blocking contradiction was found.

## CI / executable-test note

GitHub reports no combined status checks and no pull-request workflow runs for `c5552ad8be69b4648bb8c24b24219ba41b371baa`.

This verdict therefore makes no CI-execution claim. It is a fresh independent static architecture/coherence review plus logical state-machine/crash-restart E2E analysis of the exact frozen semantic subject.

## Independent verdict

**GREEN for frozen semantic subject `c5552ad8be69b4648bb8c24b24219ba41b371baa` against current workflow authority `main@cec0b384af2436890c2ee7a6f395a1131ddae1c8`. B-01, B-02 and B-03 are coherent on the reviewed subject, all requested Research crash/restart scenarios pass, and no new blocking regression was found.**

This file is evidence only. Persisting it after the frozen subject does not change the reviewed workflow semantics.
