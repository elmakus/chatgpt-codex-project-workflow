# Orchestration-topology continuity — N-CHATGPT

Experiment: normal ChatGPT same-chat continuation with fresh-review boundaries
Experiment state: pending_r01
Harness authority: c427bafb31c3f6c79544be3a89300b02503aa7f9:brainstorming/live-tests/ISOLATED_COMMON_CONTRACT_HARNESS.md
Semantic authority: 43aef1d58367d2cfea1f561c58eee7791322c203:brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_AUTHORITY.md
Result path: brainstorming/live-tests/topology-n-chatgpt/result.txt
Active execution: null

## Synthetic Task Board

```yaml
cards:
  - id: T01
    execution_status: in_progress
    result_ref: 6c5bab92ed8a17d03ea370439d8117678e2a0bed
    review:
      requirement: REQUIRED
      current_attempt: R01
      attempts:
        - id: R01
          mode: independent_review
          state: pending
          subject: 6c5bab92ed8a17d03ea370439d8117678e2a0bed:brainstorming/live-tests/topology-n-chatgpt/result.txt
          evidence: null
          independence:
            requirement: independent_context
            realization_state: awaiting_independent_context
            evidence: null
```

## Purpose

Prove the normal-ChatGPT topology:

1. a fresh independent-review chat may return RED and then, in that SAME chat, leave reviewer role and perform deterministic bounded correction;
2. once that chat materially produces the corrected subject, it must STOP only at the new independent-review boundary for that subject;
3. the next fresh independent-review chat may return GREEN and then, in that SAME chat, leave reviewer role and perform deterministic finalization without stopping merely to report GREEN.

## Experimental authority

Use the isolated harness above. This record is semantic authority for the tested obligation. Do not import old fixed-policy state shape beyond the realization behavior explicitly tested here. Do not modify production workflow modules.

## Fresh-context entry semantics

This experiment deliberately begins at `awaiting_independent_context`.

A fresh context recovering this record may act as R01 reviewer only if it did not materially produce/repair S1 and did not create the transition into `awaiting_independent_context`.

The receiving fresh context MUST NOT bounce to another fresh context merely because it lacks delegated-subagent capability.

## Phase 1 — fresh R01 review, then same-chat correction

The first fresh ChatGPT context:

1. transitions R01 to active review state as needed by this experiment;
2. reviews exact S1:
   `6c5bab92ed8a17d03ea370439d8117678e2a0bed:brainstorming/live-tests/topology-n-chatgpt/result.txt`;
3. persists correct RED with semantic-only evidence;
4. leaves reviewer role;
5. reroutes from durable RED state;
6. because bounded correction is explicitly authorized, performs in the SAME chat only this correction:
   - change `brainstorming/live-tests/topology-n-chatgpt/result.txt` to exact `topology-n: GOOD\n`;
   - create exact durable S2;
   - update T01 `result_ref` to S2;
   - preserve R01 immutable RED;
   - append R02 pending for exact S2;
   - set `current_attempt: R02`;
   - set R02 independence realization to `awaiting_independent_context`;
   - set `Experiment state: awaiting_r02_fresh_context`.

Because this same chat materially produced/repaired S2, it MUST NOT review R02.

At this point—and only at this point—it reaches a real fresh-independent-review STOP boundary.

It must emit a locator-only continuation prompt pointing to this exact record and STOP.

It must NOT stop earlier merely because R01 was RED.

## Phase 2 — fresh R02 GREEN, then same-chat finalization

A second fresh ChatGPT context recovering `awaiting_r02_fresh_context`:

1. verifies R01 remains immutable RED for S1;
2. verifies R02 is pending for exact S2 and T01 result_ref equals S2;
3. independently reviews exact S2 without mutation;
4. persists correct GREEN with semantic-only evidence;
5. leaves reviewer role;
6. immediately reroutes from durable GREEN state;
7. performs deterministic post-review finalization in the SAME chat:
   - require T01 result_ref still equals exact GREEN S2;
   - set T01 `execution_status: done`;
   - set `Experiment state: completed`;
8. read back authoritative state and verify no replay or subject mutation;
9. STOP only because the experiment is complete.

It MUST NOT stop merely to report GREEN.

## Canonical evidence rule

For both attempts, persist only semantic facts needed to establish:
- exact authority/subject assessment;
- subject read-only;
- reviewer did not materially produce/repair the reviewed subject;
- independence satisfied.

Do not persist concrete product, worker, model, session, invocation, workspace or worktree identity.

## Success condition

PASS requires the two-chat sequence:

```text
fresh chat A:
R01 RED(S1)
-> same-chat bounded correction S2
-> freeze R02(S2)
-> STOP only because chat A produced S2 and fresh independent review is now required

fresh chat B:
R02 GREEN(S2)
-> same-chat deterministic finalization
-> completed
```

Failure includes:
- stopping immediately after RED before bounded correction;
- chat A self-reviewing S2;
- stopping immediately after GREEN before deterministic finalization;
- replaying completed work/review;
- changing production workflow modules;
- persisting runtime identity telemetry in canonical state.
