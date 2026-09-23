# M07-T06 — manual Codex handoff for L08 N-CAPABLE

Status: READY FOR USER-MEDIATED LIVE RUN  
Owning Card: `M07-T06`  
Qualification: `L08 — N-CAPABLE live RED/correction/GREEN topology`

## Exact workflow candidate

- repository: `elmakus/project_workflow_v2`
- commit: `15978113e46abc8498ceaef594461c8613fcadb8`
- candidate must be used exactly; do not substitute current main or modify candidate semantics.

## Durable consumer fixture

- repository: `elmakus/test-pwv2`
- branch: `feat/m07-l08-topology-n`
- required entry HEAD: `7a2cf09bf505ba62e0ecfc32385429b9fe77e7d8`
- selected workstream: `implementation/workstreams/topology-n/WORKSTREAM.toml`
- Task Board: `implementation/workstreams/topology-n/TASK_BOARD.toml`
- Card: `implementation/workstreams/topology-n/cards/M01-T01.md`
- authority: `requirements/TOPOLOGY_N_L08.md`
- pending review: `implementation/workstreams/topology-n/reviews/M01-T01-R01.toml`
- S1 result commit: `da4f4b2b4c9ed975b4a82deb5d8fae87536bda8f`
- S1 result blob: `7cc3c960b0109ebe6957b8509c41b50b2899ad2a`
- S1 product commit: `263f5c3d84faa548a3d9197e9e66b2b01058bca8`
- `topology-n.txt` S1 blob: `4f49a94bb5f910f83aa95c3cc1972374fca82c29`
- exact S1 bytes: `topology-n: BAD\n`

## Runtime constraint

Use only:
- provider: `codex-lb-clean`
- model: `gpt-6-sol`
- reasoning effort: `low`

If the top-level session or native delegated children cannot be kept on that model/effort, stop and report the mismatch. Do not fall back to another model/provider.

## Qualification invariants

This must be one top-level Codex invocation with genuine native delegated model contexts.

Required semantic progression:

`S1 BAD -> independent R01 RED -> delegated bounded correction -> S2 GOOD -> independent later GREEN -> post-review finalization -> same Card DONE`

Hard constraints:
- one Project Workflow Card only: `M01-T01`;
- no shell-launched second Codex CLI as fake delegation;
- no self-simulated reviewer/executor;
- reviewers and delegated corrector must be genuinely separate native child/delegated model contexts;
- Main/coordinator is the only writer/reconciler of Project Workflow durable state under `implementation/workstreams/topology-n/`;
- delegated corrector may modify only `topology-n.txt`;
- preserve R01 append-only after RED; create a later review attempt for S2 rather than overwriting R01;
- exact S2 bytes must be `topology-n: GOOD\n`;
- independent S2 reviewer must not materially produce or repair S2;
- GREEN is not a user stop; finalize the Card in the same top-level invocation;
- do not write runtime/model/session/worker identity into canonical Project Workflow state;
- push the completed branch so GitHub contains all immutable evidence.

## Ready-to-copy prompt

Use Project Workflow V2 from `elmakus/project_workflow_v2` at exact commit `15978113e46abc8498ceaef594461c8613fcadb8`.

This is the live M07 L08 N-CAPABLE qualification. Treat repository state and the exact candidate as authority; this prompt is only a locator and execution request.

Consumer repo:
`elmakus/test-pwv2`

Branch:
`feat/m07-l08-topology-n`

Required entry HEAD:
`7a2cf09bf505ba62e0ecfc32385429b9fe77e7d8`

Selected workstream:
`implementation/workstreams/topology-n/WORKSTREAM.toml`

Start from `PROJECT.md`, then reconstruct the selected workstream and route from its durable state. Verify the branch is exactly at the required entry HEAD before any mutation. If it is not, stop and report the mismatch rather than rebasing or repairing it.

Use only the currently configured `codex-lb-clean` provider with model `gpt-6-sol` and reasoning effort `low` for the top-level session and every native delegated model context. Do not fall back to another model/provider. If that constraint cannot be satisfied, stop and report it.

Execute L08 as one top-level invocation using genuine native multi-agent/delegated capability. Do not launch another Codex CLI through the shell and do not simulate child roles yourself.

The entry state intentionally has one active Card, `M01-T01`, and pending review `M01-T01-R01` over immutable S1. The exact product S1 is `topology-n: BAD\n`.

Required progression:
1. Use a genuinely separate native reviewer context to review the exact frozen S1 result subject. It must independently conclude RED against the Card/authority.
2. Main records that RED append-only in R01 and keeps the same Card active.
3. Main delegates the bounded correction to a genuinely separate native executor/corrector context. That child may modify only `topology-n.txt`, changing its complete bytes to exactly `topology-n: GOOD\n`. The child must not edit Task Board, result, review or other Project Workflow state.
4. Main validates the returned correction, commits/freeze-reconciles exact S2, updates the semantic Card result, and creates the next append-only pending review attempt for S2.
5. Use a separate genuinely independent native reviewer context for exact S2. That reviewer must not have materially produced or repaired S2. It must independently conclude GREEN against the same Card/authority.
6. Main records GREEN, reruns the production router, follows `post_review_finalization`, and finalizes the same Card to terminal DONE in this same top-level invocation. Do not stop merely because RED or GREEN was produced.
7. Validate exact final bytes, Git commit/blob identities, append-only RED then GREEN review history, one-Card invariant, Task Board terminal state, production-router terminal routing, clean worktree, and absence of runtime/model/session/worker identity from canonical state.
8. Push the completed `feat/m07-l08-topology-n` branch to GitHub.

Do not modify the Project Workflow candidate to make the test pass. Do not create additional Project Workflow Cards. Do not touch the completed `user-setting-persistence-restart` workstream inherited from main.

At the end, return a concise evidence report containing:
- final branch HEAD;
- S2 product commit and `topology-n.txt` blob;
- S2 result commit/blob;
- R01 RED record path and frozen subject;
- later GREEN review record path and frozen subject;
- final Task Board revision/status;
- confirmation that correction and both reviews used genuine native delegated contexts;
- confirmation that only Main wrote Project Workflow durable state;
- confirmation that the branch was pushed and the worktree is clean.
