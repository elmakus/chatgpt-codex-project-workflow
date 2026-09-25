# Source Index

This workspace is an out-of-band normalization layer only. The persisted aggregate reports are audit evidence, not accepted technical truth. No candidate below is confirmed or rejected by this initialization.

## Source A — canonical PWv2 swarm aggregate

- Repository: `elmakus/project_workflow_v2`
- Aggregate branch: `audit/pwv2-swarm-aggregate-1m60eainl90lrd0cfqufekjn`
- Aggregate metadata: `audits/swarm-aggregate/1m60eainl90lrd0cfqufekjn/META.toml`
- Aggregate report: `audits/swarm-aggregate/1m60eainl90lrd0cfqufekjn/CONSOLIDATED_REPORT.md`
- Exact audited PWv2 subject: `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`
- Population: 36 matching swarm branches were frozen; 34 completed valid independent audits were included and 2 branches were incomplete/empty.
- Counts: 164 original material findings; 27 candidate defect-class clusters; 15 classes independently reported by at least two audits; 12 singleton classes.
- What the population examined: broad canonical PWv2 behavior across routing precedence, immutable subject identity, review/result evidence, Planning/Premium, Research/Intake, Close/finalization, Task Board/JIT, malformed/stale state, path safety, bootstrap/helper parity and related negative-space behavior.
- Limitations: the aggregate performed no new product review and no technical confirmation/rejection. Many source reproducers were persisted but not executed in-session because exact-checkout/runtime access was constrained. Frequency is independent rediscovery only, not a validity threshold.

## Source B — M02R-T03 shadow aggregate

- Repository containing aggregate: `elmakus/chatgpt-codex-project-workflow`
- Aggregate branch: `audit/m02r-t03-shadow-aggregate-q9m2x7v4k8p1c6n3r5t0w2za`
- Aggregate report: `audits/m02r-t03-shadow-aggregate/q9m2x7v4k8p1c6n3r5t0w2za/CONSOLIDATED_REPORT.md`
- Exact audited consumer commit: `5b76ffe03259ff141afc6bfb5b7b546041a48b41`
- Exact audited result: `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/results/M02R-T03-R02.md`
- Exact audited result blob: `b357ba85d4975540f3ae87b05e73e3fcf8e0471a`
- Exact audited PWv2.1 implementation: `elmakus/project_workflow_v2@180cc0af3a9b56c8c2808827bf5548b8ae040608`
- Population: 4 already-completed independent out-of-band M02R-T03 shadow reviews.
- Counts: 12 original material findings; 4 clustered candidate defect classes; all 4 classes independently reported by at least two reviewers; no singleton class.
- What the population examined: the exact repaired M02R-T03 result/implementation, especially Final observation-history completeness, observation provenance, cleanup proof binding, and the RED historical-compatibility path.
- Limitations: S1 and S4 explicitly relied on static/code-path analysis because fresh local execution was unavailable; S2 did not independently execute a clean local clone; S3 stated no comparable execution limitation. The aggregate itself performed no new review or technical confirmation.

## Immutable-subject warning

Source A and Source B are not interchangeable populations. Source A audited canonical PWv2 commit `4fb4bfb7...`; Source B audited consumer result commit `5b76ffe0...` and PWv2.1 implementation commit `180cc0af...`. They are different immutable subjects with different scopes and dates. A cross-source overlap in the ledger means only that two aggregate classes make the same semantic defect-family claim; it does **not** mean evidence from one subject confirms the other.

No singleton, low-frequency, or later-milestone-looking finding was discarded during normalization.
