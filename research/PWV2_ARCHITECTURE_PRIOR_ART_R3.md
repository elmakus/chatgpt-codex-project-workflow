# Research — PWv2.1 vs Orchestration Runtime prior-art split

Date: 2026-09-23
Research question: Re-evaluate pi-fabric, Laya/System One, Dagu, rpiv-todo and pi-extensible-workflows under the corrected architecture boundary where Project Workflow owns governance/policy and a separate rebuilt orchestration runtime owns worker execution.

## Durable continuation metadata — chatgpt_only

Research ID: pwv2-architecture-prior-art-r3
Status: active
Origin role: brainstorming
Origin subject: pwv2-architecture-prior-art@R3
Return target: brainstorming:pwv2-architecture-prior-art@R3
Return reconciliation: pending
Return reconciliation result: none

## Scope

Produce a new synthesis rather than merely relabel R2.

Required outputs:
1. explicit responsibility boundary between Project Workflow v2.1 and the replacement orchestration layer;
2. source-by-source re-evaluation of all five prior-art families;
3. current codex_workflow responsibility audit as legacy baseline only;
4. candidate improvements grouped into:
   - PWv2.1;
   - Orchestration Runtime;
   - Shared interface contract;
   - Reject / no material benefit;
5. context/determinism/recovery/review/failure-mode analysis;
6. validation experiments;
7. corrections to R1/R2 ownership/classification.

Do not implement or promote architecture choices.
