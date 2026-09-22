# Research — Pi runtime/harness compatibility for Project Workflow V2 before continuing M03

Date: `2026-09-22`
Research question: Determine, from current Pi upstream/docs/source plus proportional tracker/community evidence, whether Project Workflow V2 can keep M03 semantics runtime-neutral while adding Pi as a compatibility/runtime candidate, and what minimal Pi-side capabilities/package/extension layer are actually needed.

Research ID: `PWV2-M03-PI-R1`
Status: `active`
Origin role: `execution_resolution`
Origin subject: `M03-T04@implementation/workstreams/feature-common-preexecution-core/cards/M03-T04.md`
Return target: `execution_resolution:M03-T04@implementation/workstreams/feature-common-preexecution-core/cards/M03-T04.md`
Return reconciliation: `pending`
Return reconciliation result: `none`

## Scope

Bounded Research before any further M03 implementation. Do not assume Pi replaces Codex and do not remove existing Codex delivery/acceptance authority without a separate explicit user decision.

Investigate current Pi:
- installation/update; providers/models/model switching;
- sessions/resume/fork/compaction;
- interactive/headless/JSON/RPC/SDK surfaces;
- built-in tools and limitations;
- official extension model: TypeScript Extensions, Skills, Prompt Templates, Pi Packages, global/project-local install, lifecycle/events, custom tools/commands/UI, persistence/recovery, npm/git distribution and update;
- PWV2 capability mapping: bootstrap, progressive disclosure, durable-state recovery, sole semantic state owner, delegated implementation/subagents, fresh independent review, per-role provider/model selection without persisting runtime identity, sequential/parallel workers within one Card, Git/GitHub/PR/Issue readback, Research/web, MCP or alternatives, safety/permissions, compaction/handoff, future web UI/RPC separation;
- classify each capability as native Pi / official-example extension / existing third-party / custom small extension / unnecessary-or-outside-PW;
- compare current subagent/delegation implementations and choose among existing extension, minimal custom orchestration extension, or external RPC/SDK orchestration;
- evaluate a minimal auditable `pw for Pi` Pi Package while preserving canonical `workflow/` as the single semantic source;
- assess third-party package/extension security;
- determine M03 authority/plan impact and later Pi live-acceptance needs.

## Source strategy

Prefer official/upstream Pi documentation and source, then upstream issues/discussions, then comparable/third-party implementations and practical community evidence. Record conflicts and limitations explicitly.

## Findings

Research in progress.
