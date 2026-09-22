# Research — Pi as a Project Workflow V2 runtime/harness candidate before M03

Date: `2026-09-22`
Research question: `Using current upstream and practical evidence, determine Pi's actual harness/runtime capabilities and extension model, classify the smallest mechanisms needed to run Project Workflow V2 well on Pi, evaluate subagent/delegation and a minimal pw-for-Pi package, and decide whether the accepted PWV2 Definition/ADRs/M03 plan can remain runtime-neutral without replanning while Codex stays the currently qualified runtime.`

## Durable continuation metadata — policy-activated only

Research ID: `PWV2-PI-R1`
Status: `active`
Origin role: `strategic_planning`
Origin subject: `PWV2-P1:M03-runtime-boundary-before-execution-prep`
Return target: `strategic_planning:PWV2-P1:M03-runtime-boundary-before-execution-prep`
Return reconciliation: `pending`
Return reconciliation result: `none`

## Scope

Bounded pre-execution Research before any M03 Card/Execution Prep activation.

Investigate from current sources, prioritizing official/upstream Pi documentation and source, then upstream issues/discussions and proportionate practitioner/community evidence:

1. Pi installation/update, providers/models/model switching, sessions/resume/fork/compaction, interactive/headless/JSON/RPC/SDK, and built-in tools/limits.
2. Official extension model: TypeScript Extensions, Skills, Prompt Templates, Pi Packages, global/project-local installation, lifecycle/event hooks, custom tools/commands/UI, persistence/recovery, npm/git distribution and updates.
3. Capability mapping for PWV2: bootstrap, progressive disclosure, durable recovery, sole semantic state owner, delegated implementation, independent fresh-context review, provider/model choice outside PW state, internal sequential/parallel workers, Git/GitHub/PR/Issue readback, Research/web, MCP/alternatives, permission/safety gates, compaction/handoff, and future web UI/RPC separation.
4. Classify each capability as native Pi, official/example extension sufficient, suitable existing audited third-party package, own small extension, or unnecessary/outside Project Workflow.
5. Compare subagent/delegation implementations and choose among existing extension, own minimal orchestration extension, or external RPC/SDK orchestration without designing a speculative framework.
6. Evaluate a minimal `pw for Pi` Pi Package while keeping canonical `workflow/` as the sole semantic truth; compare with Codex plugin delivery without assuming structural parity.
7. Assess third-party extension/package security given process/system privileges and prefer a minimal auditable set.
8. Reconcile findings against accepted Definition/ADRs/PWV2-P1 M03: identify what remains runtime-neutral, any actual contradiction requiring Definition/Planning change, whether Codex can stay currently qualified while Pi is a compatibility candidate, and later Pi live-acceptance tests.

Explicit constraint from current user authority: researching Pi does **not** select Pi as the official V2 runtime, does not remove existing Codex delivery/acceptance, and does not authorize Definition/Strategic Plan edits unless evidence proves a real contradiction.

## Sources / evidence

Pending current-source research.

## Verified findings

Pending.

## Repository/current-state findings

At Research start, M02 is durably done; no M03 Card or Execution Prep state exists. Accepted PWV2 authority already separates Project Workflow semantics from concrete runtime worker/session/model topology and M03 explicitly forbids adding a runtime role catalog, model preference, worker adapter API or persisted invocation schema.

## Assumptions / uncertainties

- `Pi` refers to the current Pi coding-agent/harness upstream to be identified and verified from official sources rather than assumed from memory.
- Exact Pi extension/package APIs and available third-party implementations are unknown until source-grounded verification completes.

## Alternatives

Pending evidence.

## Analysis

Pending evidence.

## Recommendation, if requested

Pending evidence.

## Project Definition candidates

None at Research start. Research must return to the recorded Strategic Planning subject for classification before any accepted authority changes.
