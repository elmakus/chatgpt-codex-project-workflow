# M03-T01 Independent Review 03

Card: `M03-T01`
Exact review subject: `c571e1d3516dae53ef76bdff855e9563009b0081`
Verdict: **RED**

## Authority reviewed

- `implementation/workstreams/feature-codex-only-policy/cards/M03-T01.md`
- `requirements/CODEX_ONLY_POLICY.md` — CO-REQ-017..025
- `planning/CODEX_ONLY_MASTER_PLAN.md#M03--bounded-parallel-task-cards-and-jit-safety`
- accepted namespace/runtime/parallel ADRs
- accepted M02 checkpoint/handoff and M02 review invariants
- `openspec/changes/codex-only-m03-bounded-parallel-safety/`
- prior M03 RED evidence `M03-T01-review-01.md` and `M03-T01-review-02.md`
- exact subject `c571e1d3516dae53ef76bdff855e9563009b0081` and implementation range `43c234e59e6db081a0b3dbf7efd9ae16948e0553..c571e1d3516dae53ef76bdff855e9563009b0081`

## Independence

This fresh reviewer chat did not implement the exact reviewed subject. The subject remained immutable during review; only review lifecycle state/evidence is written after the subject.

## Independent checks

GREEN:

- RED-01 prepared-batch unwind is explicit and restores batch-owned Card readiness before clearing `current_batch`.
- RED-02 active-batch review deferral is coherent: integrated member review stays pending while the batch is current; post-batch repair does not rewrite original lane/integration provenance.
- Exact M03 implementation diff is clean under `git diff --check` and contains no conflict markers.
- M03 does not modify root `workflow/CONTEXT_ROUTING.md`, `workflow/chatgpt_only/*` or root `PROJECT.md` relative to its implementation base; root project policy remains `execution_policy: chatgpt_only`.
- Modified codex_only contracts contain no active dependency on `workflow/chatgpt_only/*`, `workflow/codex/*`, `workflow/legacy/*` or `workflow/contracts/*`.
- Required templates contain no forbidden runtime-identity/scheduler schema keys in active YAML.
- The reviewer environment did not provide a YAML parser, so parser-based YAML validation was not independently re-claimed.

## Finding

### RED-03 — post-launch blocked batch has no deterministic recovery transition

The contracts define fail-closed blocking after launch for a returned result that escapes `write_scope` / touches reserved state and for a material integration conflict. They also allow lane failure/blocker return. Those paths preserve evidence and route to Recovery, but no contract defines the state transition that resolves the already-launched blocked batch.

Reachable example:

1. B01 contains T1 and T2; both lanes have launched from frozen base S0.
2. Main integrates T1 to S1 and freezes T1 review pending/deferred.
3. T2 is returned, but validation finds scope escape. Main marks T2/B01 blocked and preserves the returned result.
4. `current_batch` must remain B01 because the pre-launch abandonment path is explicitly illegal after launch.
5. Recovery can classify “correction” or “serial fallback”, but STATE/EXECUTION/RECOVERY do not define how a blocked launched member may receive a corrected result, how its state returns to the integration path, or how B01 may be terminally reconciled/cleared while preserving T1 and any returned siblings.
6. Clearing `current_batch` directly would leave a non-integrated T2 `in_progress/blocked`, which does not qualify for the completed-batch review-drain exception. Reusing the prepared-batch unwind is forbidden. The state machine therefore has no deterministic legal continuation.

The same gap applies to a post-launch material integration conflict: evidence is preserved and Recovery is selected, but the exact batch/member transition after bounded correction is unspecified.

This fails the Card's included scope for conflict/failure fallback and interruption recovery, weakens the M03 acceptance requirement for deterministic recoverability, and conflicts with CO-REQ-024 repository-first reconstruction/continuation.

## Required correction

Define one canonical post-launch blocked-batch reconciliation rule across State, Execution, Router, Recovery, OpenSpec and scenario audit that:

1. preserves already-integrated and already-returned sibling results and the frozen member order/base;
2. defines whether an affected launched member is corrected/re-realized under the same batch member or is terminally superseded by an explicit durable batch outcome;
3. defines the exact allowed state transitions and result/evidence lineage for that correction;
4. defines when a blocked batch may leave `current_batch` without creating an invalid multi-`in_progress` state;
5. never uses the pre-launch abandonment/reset path after runtime-active work;
6. keeps Main as the only shared-state writer and does not rerun successful members.

A bounded same-member retry from the original frozen base is one possible design if its old failed result/evidence remains durably preserved; another design is acceptable if it is equally deterministic and recoverable.
