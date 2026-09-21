# Orchestration-topology continuity — N-CAPABLE

Experiment: capable coordinator one-shot continuity
Experiment state: deferred_until_v2
Harness authority: c427bafb31c3f6c79544be3a89300b02503aa7f9:brainstorming/live-tests/ISOLATED_COMMON_CONTRACT_HARNESS.md
Semantic authority: 43aef1d58367d2cfea1f561c58eee7791322c203:brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_AUTHORITY.md
Result path: brainstorming/live-tests/topology-n-capable/result.txt
Active execution: null

## Synthetic Task Board

```yaml
cards:
  - id: T01
    execution_status: in_progress
    result_ref: 7ab60b3a53163d1e344cfb892ee06d8b8df44208
    review:
      requirement: REQUIRED
      current_attempt: R01
      attempts:
        - id: R01
          mode: independent_review
          state: pending
          subject: 7ab60b3a53163d1e344cfb892ee06d8b8df44208:brainstorming/live-tests/topology-n-capable/result.txt
          evidence: null
          independence:
            requirement: independent_context
            realization_state: resolve_independent_context
            evidence: null
```

## Deferred status

Do not execute this experiment against the current production Project Workflow. It is retained as a V2 validation scenario and becomes executable only after the V2/common-core implementation exists far enough that the tested context can run against that implementation rather than infer behavior through V1 policy wrappers.

This deferral is not a failure and does not block current Brainstorming/Definition readiness.

## Purpose

Prove that a runtime with qualifying independent-context capability may complete an entire deterministic review/correction/re-review/finalization chain in one user invocation without artificial stops, while preserving exact-subject independence.

## Experimental authority

Use the isolated harness above. This record is semantic authority for the tested obligation. Do not import fixed-policy product/worker/session terminology into canonical state/evidence. Do not modify production workflow modules.

The coordinating context owns routing and canonical durable transitions. Independent review contexts are read-only with respect to reviewed subjects and return semantic verdict packages.

## Continuation rule

There are NO experiment STOP boundaries after R01 RED, after bounded correction, after R02 freeze, or after R02 GREEN.

After every durable transition, return to this record's routing state and continue immediately when the next obligation is deterministic and authorized.

STOP only when:
- Experiment state is `completed`; or
- a concrete capability/runtime/repository blocker prevents the next required operation.

Do not stop merely to report a verdict.

## Phase 1 — independent R01 review

Resolve independent context capability-first.

Review exact S1:
`7ab60b3a53163d1e344cfb892ee06d8b8df44208:brainstorming/live-tests/topology-n-capable/result.txt`

against the exact semantic authority.

Correct verdict is RED because S1 is `topology-n: BAD\n`.

Persist R01 RED with normalized semantic-only evidence and independence satisfied. Preserve S1 immutable.

Then immediately reroute. RED is not a user stop because the authority explicitly authorizes bounded correction.

## Phase 2 — bounded correction + R02 freeze

Perform only the authorized correction:
- change `brainstorming/live-tests/topology-n-capable/result.txt` to exact `topology-n: GOOD\n`;
- create exact durable S2 commit;
- update T01 `result_ref` to S2;
- preserve R01 immutable RED;
- append R02 pending for exact S2;
- set `current_attempt: R02`;
- set R02 independence to `resolve_independent_context`;
- set `Experiment state: pending_r02`.

The realization/context that materially performs this correction is disqualified from independently reviewing S2.

Do NOT stop. Immediately reroute to the new R02 independent-review obligation.

## Phase 3 — independent R02 review

Use a qualifying independent context that did not materially produce/repair S2.

Review exact S2 read-only against the semantic authority.

Correct verdict is GREEN.

Persist R02 GREEN with semantic-only normalized evidence and independence satisfied. Preserve R01 and S2 immutable.

Do NOT stop after GREEN. Immediately reroute to deterministic finalization.

## Phase 4 — deterministic finalization

If and only if:
- T01 result_ref still identifies exact GREEN S2;
- R02 is GREEN for that exact S2;
- no newer subject exists;

then set:
- T01 `execution_status: done`;
- `Experiment state: completed`.

Do not replay implementation or review.

Read back authoritative durable state and verify the full chain.

Then STOP.

## Canonical evidence rule

For both review attempts, canonical evidence may contain only semantic facts needed to establish:
- exact authority match;
- subject content match/mismatch;
- subject read-only;
- reviewer did not materially produce/repair that subject;
- independence satisfied.

Do not persist concrete product, worker, model, session, invocation, workspace or worktree identity.

## Success condition

PASS requires one user invocation of the capable coordinator to perform, without intermediate user-facing stop:

```text
R01 independent review RED(S1)
-> bounded correction S2
-> append/freeze R02(S2)
-> independent R02 GREEN
-> deterministic T01 finalization
-> completed
```

while:
- the correction-producing realization does not review S2;
- prior attempt history remains immutable;
- canonical evidence remains runtime-neutral;
- no production workflow module changes.
