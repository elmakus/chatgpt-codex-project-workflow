# M07-T06 — L08 N-CAPABLE live qualification

Date: 2026-09-23
Status: GREEN
Candidate: `elmakus/project_workflow_v2@15978113e46abc8498ceaef594461c8613fcadb8`

## Entry

Consumer repository: `elmakus/test-pwv2`
Branch: `feat/m07-l08-topology-n`
Durable entry HEAD: `7a2cf09bf505ba62e0ecfc32385429b9fe77e7d8`

The user supplied only repository/workflow locators. Expected RED/correction/GREEN routing was not described in the start prompt.

## Live result

One top-level Codex invocation reconstructed the V2 state and used its configured delegated subagent harness for the bounded roles.

Observed durable sequence:
- `7df92c424cf1e97435e6d94550b51be7191dcd6f` — independent R01 RED on frozen S1;
- `5a0d5043248d034a50cceccb2921d14f0f9fa6fe` — delegated bounded correction of only `topology-n.txt`;
- `c92602770b090a7be9040c89b60b6e5330dcf250` — Main reconciled/froze S2 semantic result;
- `9b544df7aa08b52d8ee4b07742701aea764bb607` — R02 pending exact S2 subject;
- `38cb92a9fcbb26b11b2a871bcb646700b46540fa` — independent R02 GREEN;
- `5b2c058d02acd76e282465dce692c70a3f590930` — same Card finalized to `done`.

The delegated reviewer, corrector and later reviewer were separate subagent contexts supplied through the Codex runtime's configured worker harness. Project Workflow does not require a particular provider/model/worker implementation; `workflow/EXECUTION.md` leaves realization to the runtime and requires delegated capability, bounded context and a valid return path.

## Exact oracle and state

Final product subject:
- implementation commit: `5a0d5043248d034a50cceccb2921d14f0f9fa6fe`;
- `topology-n.txt` blob: `3a446f6d934b2e63c0466e9f7b2bb596fa416268`;
- exact bytes: `topology-n: GOOD\n`.

Final semantic result:
- result commit: `c92602770b090a7be9040c89b60b6e5330dcf250`;
- result blob: `84b94415c722bddd2f3abdf18e141f5ea915b11d`.

Final Task Board:
- revision: 3;
- Card `M01-T01`: `done`;
- ordered review attempts: R01 RED, R02 GREEN.

R01 remains bound to the immutable S1 result; R02 is bound to the immutable S2 result. The correction commit changed only `topology-n.txt`. Main performed durable Project Workflow reconciliation/finalization; delegated workers did not finalize the board.

The final worktree was clean.

## Close boundary

After Card finalization the production router continued to Close. The local branch was six commits ahead of origin, but the execution environment did not allow push/PR/merge. This does not invalidate L08: M07.P3 requires the RED -> delegated correction -> GREEN -> same-invocation finalization topology. Close integration remains a separate downstream obligation of the disposable consumer project.

## Verdict

L08 N-CAPABLE: GREEN.

The prior blocker/non-qualifying notes are historical harness observations and are superseded for L08 qualification by this runtime-neutral interpretation, which matches the exact candidate's execution/review contracts and the user's intended acceptance criterion.
