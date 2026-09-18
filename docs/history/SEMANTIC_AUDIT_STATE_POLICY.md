# Semantic Audit — Single Live State + Three Execution Policies

Date: 2026-09-18
Scope: workflow revision introducing Task Board-only mutable execution state, `codex_only`, mixed-only Capability Gate and fixed-policy multi-milestone continuation.

## Accepted design

1. `implementation/TASK_BOARD.yaml` is the sole mutable execution-state authority.
2. Milestone/Card files are contracts; handoffs summarize completed truth; `PROJECT.md` is high-level routing/policy only.
3. `execution_policy` has exactly three modes: `chatgpt_only | codex_only | mixed`.
4. Capability Gate runs only under `mixed`.
5. Capability invariant remains `ChatGPT capabilities ⊆ Codex capabilities`.
6. Fixed-policy missing capability is a blocker, not automatic rerouting/policy change.
7. Fixed executor may continue across GREEN milestone boundaries when next milestone is already approved and no strategic/user/authorization gate intervenes.
8. `codex_only` permits Codex Main to perform deterministic just-in-time prep for subsequent already-approved milestones without inventing strategic authority.
9. Independent review is implementation-independent rather than product-hard-coded.
10. Explicit deployment/live-write authorization remains a hard stop in every policy.

## Cross-document checks

- `CHATGPT.md`, repository contract and README agree on three policies and mixed-only Capability Gate.
- Shared execution, execution prep and review/handoff agree on fixed-policy cross-milestone continuation.
- ChatGPT/Codex adapters agree with shared routing semantics.
- Codex handoff/start prompt supports continuous `codex_only` orchestration and bounded `mixed` assignment.
- Task Board/GitHub State/Task Card contracts agree that mutable state lives only in Task Board.
- PROJECT/milestone/card/handoff templates no longer require synchronized live state copies.
- Master Plan template exposes explicit boundary/user authorization gate so automatic continuation cannot silently cross deployment/live-write decisions.
- Migration guidance preserves historical evidence while making Task Board authoritative for new execution state.

## Deliberate non-changes

- No Campaign/Multi-Milestone object was added. Fixed execution policy + approved Master Plan + Task Board already provide sufficient authority/continuation state.
- No generic scheduler/DAG engine was added.
- Existing bounded-parallel ownership/isolation model remains intact.
- OpenSpec policy and external `WRITE → READBACK → VERIFY` safety contract remain intact.
- Historical audits/evidence are not rewritten to pretend they were produced under this revision.

## Migration note

Projects already using old duplicated milestone/Card status fields need not rewrite completed history. At next safe boundary, stop updating duplicate state and treat Task Board as authoritative for all new execution changes.
