# M01 Milestone Acceptance — dedicated namespace foundation and semantic parity inventory

Milestone: `M01`
Result: `GREEN`
Accepted implementation subject: `8ded26f50275ab04e35a07438ca1abd2836901c2`

## Integrated acceptance

Verified against `planning/CODEX_ONLY_MASTER_PLAN.md#M01--dedicated-namespace-foundation-and-semantic-parity-inventory`, approved `CO-R1`, the accepted codex_only ADRs, the GREEN M01-T01 matrix review, and the GREEN M01-T02 foundation review.

GREEN:

- the accepted baseline matrix maps exactly 22 current `chatgpt_only` lifecycle owners into 22 dedicated `workflow/codex_only/` owners and records all nine required legacy-property dispositions;
- the reviewed M01 foundation contains exactly those 22 policy-local files and the implementation range changes no other production/workflow path;
- the namespace does not depend on another policy namespace, legacy Codex routing, the shared execution core or shared execution contracts as runtime authority;
- Project Workflow versus `codex_workflow` ownership is explicit, with no required runtime session/invocation/model/profile/lease identity in project schemas;
- formal review foundation preserves immutable exact subjects, durable verdict/evidence and reviewer non-repair while leaving exact provenance/state/recovery mechanics to M02;
- execution/preparation/workstream foundation preserves serial default and Codex Main-owned shared state while leaving bounded ready-set/lane/JIT mechanics to M03;
- root `workflow/CONTEXT_ROUTING.md` and the entire `workflow/chatgpt_only/` tree remain identical to workflow `main`;
- root `PROJECT.md` remains `execution_policy: chatgpt_only`;
- root routing is not cut over in M01.

## Evidence

- M01-T01 independent review: `implementation/workstreams/feature-codex-only-policy/evidence/M01-T01-review-01.md`
- M01-T02 implementation evidence: `implementation/workstreams/feature-codex-only-policy/evidence/M01-T02.md`
- M01-T02 independent review: `implementation/workstreams/feature-codex-only-policy/evidence/M01-T02-review-01.md`
- baseline matrix: `docs/audits/CODEX_ONLY_M01_BASELINE_MATRIX.md`

## Result

M01 is GREEN. The dedicated namespace foundation is ready for M02 project/runtime-boundary, formal-review, state and recovery work. No cross-branch integration or publication occurs at this milestone checkpoint.
