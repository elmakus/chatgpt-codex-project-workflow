# Definition R3 completeness audit — PWv2.1 policy kernel

Date: 2026-09-24  
Definition subject: `pwv21-policy-kernel@3`  
Promoted Brainstorming source: `elmakus/chatgpt-codex-project-workflow@e883bf29ad7d2e3dd1e3ec1d62408c4e597c60b6:brainstorming/PWV21_POLICY_KERNEL.md@51494b79be9ffba5dfc8108f2bc1bf01f1c68a02`

## Verdict

**GREEN**

The promoted R3 exploratory delta is fully represented in accepted Definition authority. No unresolved user/product/strategy choice and no additional Research need remains before Strategic Planning.

## Mechanical coverage

- Requirement table rows: **137**
- Unique requirement IDs: **137**
- Range: `PWV21-REQ-001..137`
- Missing IDs: **0**
- Duplicate requirement table IDs: **0**
- Accepted ADRs registered for the workstream: **8**
- ADR IDs: `ADR-PWV21-001..008`

## R3 promoted-choice coverage

- Q1 Card semantic right-sizing: covered by REQ-128..130 and ADR-PWV21-006.
- Q2 hybrid discovery/closure lifecycle: covered by revised REQ-061, REQ-108..114, REQ-137 and ADR-PWV21-004.
- Q2 discovery accounting: 5/4/3 now counts genuinely new material defect-class discovery epochs, not every fresh-review invocation.
- Q2 per-class breaker: default 3 failed repair→closure-verification rounds before Main convergence/root-cause analysis.
- Q3 architecture: existing thin Git-backed PW policy/authority architecture preserved; no migration to an external control plane and no generic runtime/scheduler expansion.
- Q4 Worker discipline: covered by REQ-131..132 and ADR-PWV21-008; falsification/test-first where meaningful, minimum implementation, YAGNI, bounded refactor, non-absolute DRY.
- Q5 late oversized-Card discovery: covered by REQ-130 and ADR-PWV21-006; Worker reports topology evidence and remaining unaccepted scope returns to Execution Prep rather than self-authorizing topology changes.
- Q6 load-bearing finding semantics: covered by REQ-133..134 and ADR-PWV21-004.
- Q6a durable advisory reconciliation/cleanup: covered by REQ-135..136 and ADR-PWV21-004.
- No fixed small/medium/large project classes introduced.
- No generic LOC/file/token/wall-clock Card limit introduced.
- PWv2.1 wall-clock/performance tuning remains outside this R3 quality correction.

## Exact authority blobs audited

- `requirements/PWV21_POLICY_KERNEL.md` — blob `6f85eb367e4497b2c43d1075db15daece40cfd81`
- `decisions/ADR_PWV21_POLICY_KERNEL.md` — blob `0662b970d80e8b76df79e4dbd458d190ce6d4402`
- `decisions/ADR_PWV21_ORCHESTRATION_CONTRACT.md` — blob `051f8fc3f68773349a1fcad39fcf1c60d3157532`
- `decisions/ADR_PWV21_PARALLEL_CARDS.md` — blob `437388345d7136cdcdf241bf3ca6aa1016ddb1c0`
- `decisions/ADR_PWV21_REVIEW_LIFECYCLE.md` — blob `e5f578d08a4aaf0b14fec33cd7133074887c6ba8`
- `decisions/ADR_PWV21_RECOVERY_MIGRATION_HANDOFF.md` — blob `fbaaaedac492ff9e2dbf4db9f8e86b3376df2023`
- `decisions/ADR_PWV21_DECOMPOSITION_FIDELITY.md` — blob `615a442671f55a66ecc849f2a5385d298eb62eb0`
- `decisions/ADR_PWV21_LIVE_VALIDATION.md` — blob `6adbbef4a40f6005ec09e1a3f73289e256f44b12`
- `decisions/ADR_PWV21_EXECUTION_DISCIPLINE.md` — blob `3a6d8324a26bdca17ed294e5398c242815d7862c`

## Historical and downstream consistency

- M01/M02 remain truthful terminal history and are not reopened.
- P4 remains truthful historical approved planning state for Definition R2, but is prospectively stale if Definition R3 is accepted.
- P4 Premium C must not be consumed as the continuation path for R3.
- M03 remains unmaterialized.
- A new material Strategic Planning cycle is required after Definition R3 Premium A is satisfied.

## Completeness conclusion

Definition R3 has complete durable requirements/decision authority for the promoted R3 choices. The next legal workflow boundary is Premium A before material Strategic Planning.
