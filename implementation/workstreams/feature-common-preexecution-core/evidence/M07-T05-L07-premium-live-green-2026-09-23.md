# M07-T05 — L07 premium A/B/C live context-switch qualification

Date: 2026-09-23
Verdict: GREEN
Candidate: `elmakus/project_workflow_v2@15978113e46abc8498ceaef594461c8613fcadb8`

## Historical real user-driven sequence

Consumer: `elmakus/test-pwv2`
Workstream: `user-setting-persistence-restart`

The original Android/Premium flow contains genuine user-driven premium progression and a fresh independent Plan Review:
- Premium A was satisfied at commit `85209dfcb11df7eb5252ba91091af68adbf24ded`;
- P1 was materialized/frozen and Premium B became due;
- a fresh normal ChatGPT Project context performed independent Plan Review R01;
- R01 GREEN was consumed at `58726640bd842a4391ba757e6f1b0a0f214dd913`;
- Premium C became due for the same exact immutable P1 subject;
- Premium C was satisfied at `1aebab2db12fb02f6de12723b9e6e5539c305e76`;
- only after C satisfaction did Execution Prep materialize, at `551456ff445527c41f38f4e027ab37e0ef72a819`.

Final durable Planning state preserves A/B/C as satisfied for the exact P1 subject and contains no runtime/model/session identity.

## Immutable restart snapshots

Four real historical snapshots were used, without synthesizing approvals:
- A due: `9c31e834b23fc9184bf4adfd44c1a5bebb9af592`;
- B due: `7c6c235aa8a8946f7571898860a0fb0b5bf8090f`;
- C due after GREEN review: `58726640bd842a4391ba757e6f1b0a0f214dd913`;
- C satisfied: `1aebab2db12fb02f6de12723b9e6e5539c305e76`.

Each snapshot was checked in a separate detached disposable worktree.

## Actual model-backed restart probes

Every new probe used:
- real Codex CLI `0.155.0-alpha.9.2`;
- exact M07 plugin candidate installed in the isolated `CODEX_HOME`;
- provider `codex-lb-clean`;
- model `gpt-6-sol`;
- reasoning effort `low`;
- a fresh `codex exec --ephemeral` context;
- no state mutation, V1 fallback or remote workflow-policy fetch.

### A snapshot

Session: `01a0ce76-280c-7af2-9dfd-226195bc7e1b`.

Recovered:
- disposition: Premium A stop;
- owner: `workflow/DEFINITION.md`;
- durable cause: Definition GREEN, completeness GREEN, `premium_a = "due"`.

### B snapshot

Session: `01a0ce76-e672-7190-92d5-48fbd18d57e7`.

Production router readback returned:
- disposition: `stop`;
- obligation: `premium_B`;
- owner: `workflow/PLANNING.md`;
- exact frozen P1 subject: `elmakus/test-pwv2@c66ffe7729989b488291914dcc632b4e1331c082:planning/USER_SETTING_PERSISTENCE_PLAN.md@f2a1891bb2f3c769cd9dc452aae7869acf1a3bc7`;
- reason: fresh independent best-available review context required.

The historical real Plan Review R01 was performed in a fresh independent ChatGPT Project context and records `materially_produced_or_repaired_subject = false`.

### C snapshot

Session: `01a0ce77-84cb-7a31-99e1-fac1a07492b8`.

Recovered:
- disposition: Premium C stop;
- owner: `workflow/PLANNING.md`;
- exact R01 verdict: GREEN;
- `premium_a = satisfied`;
- `premium_b = satisfied`;
- `premium_c = due`;
- B/C bound to the same immutable P1 subject.

### Post-C snapshot

Session: `01a0ce77-f7cb-75f3-936d-1213959b3377`.

Recovered:
- obligation: Execution Prep;
- owner: `workflow/EXECUTION_PREP.md`;
- A/B/C all satisfied;
- exact Plan Review R01 still GREEN for the same P1 subject;
- no premium gate was spuriously re-presented.

## Mutation/readback

All four detached worktrees remained clean. The probes only read immutable historical consumer state and the exact installed M07 candidate.

## L07 verdict

GREEN.

The real V2 premium lifecycle demonstrates A -> Planning -> B -> fresh independent GREEN review -> C -> Execution Prep. Fresh contexts recover A/B/C from durable state, and the current model/provider identity does not participate in semantic routing. New live probes were restricted to `gpt-6-sol` with low reasoning through `codex-lb-clean`.
