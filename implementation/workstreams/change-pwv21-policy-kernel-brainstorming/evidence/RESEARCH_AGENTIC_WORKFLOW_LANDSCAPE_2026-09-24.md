# Agentic Software-Development Workflow Landscape Review

Research date: 2026-09-24

Scope: mature agentic software-development methodologies, spec systems, coding-agent harnesses, orchestration/state engines, autonomous software-engineering products, and integrated products where a main/coordinator agent orchestrates specialized coding, testing, review, and repair work.

Purpose: determine whether mature existing systems already solve enough of this general development pattern that a custom workflow engine is unnecessary, and identify which functions remain genuinely worth keeping custom.

This document is research evidence only. It does not approve, supersede, or modify Project Workflow authority, planning, ADRs, task state, or architecture decisions.

## 1. Executive summary

The main conclusion is that a substantial portion of what used to justify a custom workflow engine has become commodity functionality by 2026.

Mature systems now provide, in different combinations:

- durable workflow state and resume;
- loops, conditional branches, human gates, and fan-out/fan-in;
- dependency-aware parallel execution;
- isolated or fresh coding agents;
- specialized review agents;
- bounded repair/re-review cycles;
- repository-resident specifications and plans;
- cross-agent task dispatch;
- hooks and lifecycle events;
- provider/runtime adapters.

GitHub Spec Kit is especially significant because it has evolved beyond a collection of specification prompts into a resumable workflow engine with gates, loops, conditional execution, fan-out/fan-in, persisted run state, reusable workflow steps, lifecycle events, and broad coding-agent integrations. Its integration catalog includes Pi directly, alongside Codex, Claude and other runtimes. Official references:
- https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md
- https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- https://github.com/github/spec-kit/blob/main/docs/index.md

At the generic orchestration layer, Microsoft Agent Framework and LangGraph already solve the low-level workflow problems that are difficult and expensive to implement correctly: explicit graph control flow, checkpointing, durable execution, resume after failure, concurrent branches, human intervention, and isolated agent/executor participants. Microsoft now positions Agent Framework rather than AutoGen as the current production-oriented direction for new Microsoft multi-agent work. Official references:
- https://learn.microsoft.com/en-us/agent-framework/workflows/
- https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints
- https://github.com/microsoft/agent-framework/releases
- https://github.com/microsoft/autogen/blob/main/README.md

At the development-methodology layer, Superpowers and BMAD provide surprisingly sophisticated software-development semantics. Superpowers has independently testable and reviewable task decomposition, fresh implementer/reviewer roles, and a bounded repair loop. BMAD has a structured planning/build/review pipeline, durable story contracts, deterministic sprint-planning machinery, external execution handoffs, and through the separate bmad-loop project, disposable coding sessions and bounded adversarial review. Official references:
- https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
- https://github.com/obra/superpowers/blob/main/docs/superpowers/plans/2026-07-15-sdd-fix-loop-redesign.md
- https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md
- https://github.com/bmad-code-org/bmad-loop

There is, however, no mature runtime-neutral product found in this review that combines all of the following as first-class semantics:

idea/discovery
→ durable definition
→ architecture
→ milestone hierarchy
→ JIT task materialization
→ fresh implementer
→ independent fresh reviewer
→ bounded repair/re-review
→ milestone review
→ final integration review

while also providing deterministic Git-backed legality/state, typed cross-runtime obligations/results, and the ability to continue unchanged across unrelated environments such as ChatGPT and Pi.

The practical implication is therefore not "replace Project Workflow V2.1 with product X", but it is also no longer defensible to implement every underlying primitive from scratch.

The strongest architecture emerging from the landscape is:

repository-native specification/workflow control plane
+ replaceable coding runtime
+ reusable development methodology
+ a very thin custom policy kernel

rather than a large bespoke workflow engine.

For a ChatGPT ↔ Pi environment, the most promising combination to prototype first is:

GitHub Spec Kit workflow/state infrastructure
+ Pi as implementation runtime
+ Superpowers-style fresh implementer/reviewer semantics
+ only the small custom policy needed for JIT Cards, typed obligation/result boundaries, and cross-runtime legality.

The strongest alternative is BMAD + bmad-loop. It comes closer to an integrated replacement, but bmad-loop is still explicitly pre-1.0/early beta and does not currently provide a first-party Pi adapter. Its adapter/plugin architecture makes a Pi integration plausible without maintaining a fork.

If runtime neutrality is not required, Kiro is the strongest all-in-one candidate found in this review because it combines durable Specs, requirements/design/tasks, dependency-wave parallelism, custom agents/subagents, hooks, and implementation validation in one product.

The biggest build-vs-adopt recommendation from this review is:

Do not add more generic scheduling, checkpointing, looping, fan-out, resume, provider-adapter, or basic review-loop machinery to a custom workflow until Spec Kit, Superpowers-on-Pi, BMAD/bmad-loop, and Kiro have been prototyped against the real requirements.

Those areas are now substantially commoditized.

## 2. Ecosystem taxonomy

The ecosystem contains several categories that must not be compared as if they solve the same problem.

### 2.1 Software-development methodology/workflow

Defines how software work should proceed and what sequencing or review discipline to apply.

Representative systems:
- obra/superpowers
- BMAD Method
- Get Shit Done (GSD)

These systems can define strong development semantics while having little or no generic durable scheduler.

### 2.2 Spec-driven development system

Makes requirements, specifications, plans, and task structures durable first-class artifacts.

Representative systems:
- GitHub Spec Kit
- OpenSpec
- Kiro Specs
- BMAD

### 2.3 Coding-agent harness

Provides an environment where a coding agent can inspect repositories, edit files, execute commands/tests, and possibly spawn more agents.

Representative systems:
- Claude Code
- OpenAI Codex
- OpenHands
- GitHub Copilot CLI/SDK
- SWE-agent / mini-swe-agent

### 2.4 Multi-agent orchestration framework

Provides delegation, routing, coordination, agent communication, and often graph/state abstractions.

Representative systems:
- Microsoft Agent Framework
- LangGraph
- CrewAI
- historically AutoGen
- MetaGPT

### 2.5 Autonomous software-engineering agent

Attempts to take a software-engineering goal or issue and carry it toward a completed implementation with substantial autonomy.

Representative systems:
- Devin
- OpenHands
- SWE-agent
- Codex coding agents
- Kiro autonomous agents

### 2.6 Workflow/state engine

Provides explicit state transitions, persistence, branches, loops, checkpoints, human gates, fan-out/fan-in, and resume.

Representative systems:
- current GitHub Spec Kit workflow engine
- Microsoft Agent Framework workflows
- LangGraph
- CrewAI Flows
- bmad-loop

### 2.7 Combination products

The strongest candidates span multiple categories.

Examples:
- GitHub Spec Kit: methodology + spec system + workflow/state engine.
- BMAD + bmad-loop: methodology + spec system + execution/state automation.
- Kiro: spec system + coding harness + autonomous agent + workflow capabilities.
- Claude Code / Codex / Copilot: coding harness + multi-agent/autonomous execution, but little imposed SDLC methodology.
- OpenHands: coding harness + autonomous software-engineering agent + runtime infrastructure.

This distinction is architecturally important. A generic multi-agent framework may replace runtime infrastructure without replacing a development methodology. A methodology may replace custom planning/review semantics while still requiring a separate runtime.

## 3. Broad candidate landscape

| Candidate | Classification | What it mainly solves | 2026 assessment |
| --- | --- | --- | --- |
| GitHub Spec Kit | methodology + spec-driven system + workflow/state engine | SDD, repository artifacts, workflows, gates/loops/fan-out, integrations | Top-tier candidate; active and rapidly maturing. See https://github.com/github/spec-kit/blob/main/docs/index.md and https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md |
| BMAD Method | methodology + spec-driven system | product-development lifecycle from planning through build/review | Top-tier methodology; current v6 line has formalized planning/build/review machinery. See https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md |
| bmad-loop | coding harness/orchestration + workflow/state engine | disposable coding sessions, story state, verify/review loops | Architecturally relevant but explicitly early beta/pre-1.0. See https://github.com/bmad-code-org/bmad-loop |
| obra/superpowers | methodology + execution workflow | brainstorming, planning, fresh task agents, review, bounded repair | Top-tier execution methodology; active and directly supports Pi. See https://github.com/obra/superpowers/releases |
| Get Shit Done (GSD) | methodology + spec/work planning + orchestration pattern | context-engineered research/planning/execution/verification | Influential architecture but repository archived June 2026. See https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md |
| OpenSpec | spec-driven system | durable repository specs/design/tasks/change archive | Strong specification layer, not an orchestrator. See https://github.com/Fission-AI/OpenSpec/blob/main/README.md |
| Kiro | spec system + coding harness + autonomous agent + workflow | requirements/design/tasks, agents, subagents, dependency-wave execution | Strongest integrated commercial candidate for this use case. See https://kiro.dev/docs/specs/ |
| Microsoft Agent Framework | multi-agent framework + workflow/state engine | durable multi-agent graphs, checkpoints, HITL, concurrency | Top-tier runtime substrate and Microsoft successor direction to AutoGen. See https://learn.microsoft.com/en-us/agent-framework/workflows/ |
| LangGraph | multi-agent/workflow framework + workflow/state engine | explicit state graphs, checkpointing, durable resume, subgraphs, HITL | Mature orchestration substrate; no built-in SDLC semantics. See https://github.com/langchain-ai/langgraph/blob/main/libs/checkpoint/README.md |
| CrewAI | multi-agent framework + workflow/state engine | manager/worker crews and persistent event-driven flows | Mature generic orchestrator; SDLC must be authored by the user. See https://docs.crewai.com/en/learn/hierarchical-process and https://docs.crewai.com/en/concepts/flows |
| OpenHands | coding-agent harness + autonomous SWE agent | software-agent runtime, workspaces, cloud/local execution, SDK | Strong execution layer, weaker full-lifecycle methodology. See https://github.com/OpenHands/software-agent-sdk |
| Claude Code | coding harness + multi-agent/autonomous execution | coding, isolated subagents, teams, worktrees, project coordinator | Excellent execution environment, strongly Claude-coupled. See https://code.claude.com/docs/id/features-overview and https://claude.com/blog/projects-redesigned |
| OpenAI Codex / Agents API | coding harness + multi-agent/autonomous execution | durable coding sessions, subagents, sandbox, context recovery | Powerful managed runtime; not itself an SDLC methodology. See https://developers.openai.com/api/docs/guides/agents-api/overview |
| GitHub Copilot Agents / SDK | coding harness + multi-agent/autonomous execution | specialized agents, code review, isolated contexts, cloud/local sessions, hooks | Strong execution/review platform, coupled to GitHub/Copilot. See https://docs.github.com/en/copilot/responsible-use/agents |
| Devin | autonomous SWE product + integrated workflow | planning, coding, testing, PRs, parallel sessions, review | Serious all-in-one commercial option with proprietary workflow/state semantics. See https://docs.devin.ai/ |
| MetaGPT | methodology + multi-agent framework + autonomous SWE pattern | PM/architect/engineer roles and SOP-driven collaboration | Historically influential; weaker durable workflow/state story than newer systems. See https://github.com/FoundationAgents/MetaGPT/blob/main/README.md |
| SWE-agent / mini-swe-agent | coding harness + autonomous SWE agent | focused issue-solving agent loop | Strong worker/runtime research tooling, not full development lifecycle. See https://github.com/SWE-agent/SWE-agent/blob/main/docs/index.md |
| AutoGen | multi-agent framework | conversational multi-agent framework | Maintenance-mode direction for existing systems; new Microsoft work points to Agent Framework. See https://github.com/microsoft/autogen/blob/main/README.md |
| OpenAI Symphony | coding orchestration reference architecture + workflow/controller | issue tracker to isolated workspaces to agents to dependency DAG | Highly relevant architectural reference, but explicitly engineering preview/reference implementation, not a maintained standalone product. See https://github.com/openai/symphony/blob/main/README.md |

## 4. Deep analysis of strongest candidates

### 4.1 GitHub Spec Kit

#### Lifecycle

Representative lifecycle:

idea/problem
→ optional idea assessment/research
→ specify
→ clarify/checklists
→ plan
→ analyze
→ tasks
→ implement
→ converge
→ repeat implementation as necessary
→ completion

The current workflow engine can place gates, shell verification, branches, loops, parallel fan-out and fan-in around that core lifecycle.

Official evidence:
- https://github.com/github/spec-kit/blob/main/docs/index.md
- https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md

#### Coordinator/orchestration model

Modern Spec Kit workflows are declarative multi-step pipelines rather than only prompt conventions.

Current workflow control structures include:
- command/prompt steps;
- shell steps;
- initialization;
- human gates;
- conditionals;
- switch-style branching;
- while/do-while style loops;
- fan-out;
- fan-in.

Workflow state is persisted and resumable.

Source:
https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md

#### State model

There are two relevant layers:

1. Durable development artifacts such as specifications, plans, and tasks in the repository.
2. Persisted workflow-run state and logs used by the workflow engine.

This is materially stronger than a prompt-only development workflow.

A caveat is that resume precision is not equivalent to a fully transactional workflow kernel at every nested point. Current architecture documentation has described resume semantics where the enclosing workflow step or nested block may be replayed rather than continuing from an exact arbitrary nested instruction boundary.

Source:
https://github.com/github/spec-kit/blob/main/workflows/ARCHITECTURE.md

#### Task decomposition

Standard Spec Kit generally creates a task plan before implementation. It can structure tasks into phases and dependencies, but JIT materialization of only the exact next implementation Card is not its central/default planning model.

This leaves room for a thin custom policy if JIT decomposition is important.

#### Fresh-context/subagent behavior

Fresh worker identity is not itself a first-class Spec Kit semantic. The workflow decides what step runs next; the selected runtime/integration determines whether that step runs in a new agent/session/context.

Therefore Spec Kit is best understood as a control plane, not as the complete worker-isolation policy.

#### Testing and review

Useful verification stages include:
- clarification;
- checklists;
- cross-artifact analysis;
- convergence checking between implementation and intended specification/plan/task state.

Source:
https://github.com/github/spec-kit/blob/main/templates/commands/converge.md

A strict invariant such as implementer A → independent fresh reviewer B → repair by A → bounded re-review is not the default built-in lifecycle. It can be authored using workflows and an appropriate runtime.

#### Resumability

Strong. Workflow execution state is persisted and resume is explicitly supported. Human approval gates can stop and later continue execution.

Source:
https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md

#### Provider/runtime coupling

Low compared with provider-native products.

Current integrations cover many coding systems, including Pi, Codex, Claude, and others.

Source:
https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md

The event/integration layer also maps lifecycle events to host-specific mechanisms, reducing the need for workflow code to hard-code one agent host.

#### Extensibility

Strong:
- workflows;
- extensions;
- presets;
- reusable steps;
- integrations;
- lifecycle events.

A permanent fork should normally not be necessary.

#### Replacement potential

Could plausibly replace:
- much of specification/Definition structure;
- planning artifact structure;
- generic workflow-state persistence;
- gates;
- loops;
- branching;
- fan-out/fan-in;
- generic resume mechanics;
- substantial integration plumbing.

Would not automatically replace:
- JIT Card policy;
- strict fresh implementer/reviewer invariants;
- typed obligation/result contracts across heterogeneous runtimes;
- exact milestone/Card legality semantics;
- bounded independent-review policy.

Conclusion: strongest candidate for replacing the generic workflow engine/control-plane portion while retaining only differentiated Project Workflow policy.

### 4.2 BMAD Method + bmad-loop

BMAD and bmad-loop should be considered together but not conflated. BMAD is the methodology/specification process; bmad-loop is a separate automation/runtime layer.

#### Lifecycle

Representative current flow:

idea
→ discovery/research/product planning
→ PRD
→ architecture/UX as appropriate
→ epics/stories
→ implementation readiness
→ sprint planning
→ story specification
→ build
→ verify
→ adversarial review
→ repair/re-review
→ commit
→ retrospective / next story or epic

BMAD's recent v6 changes formalized sprint planning, implementation, and code-review machinery.

Source:
https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md

#### Coordinator/orchestration model

BMAD itself remains methodology-heavy.

bmad-loop supplies a concrete controller roughly shaped as:

select story
→ fresh developer session
→ verify
→ fresh/adversarial reviewer
→ repair if necessary
→ commit
→ select next story

Source:
https://github.com/bmad-code-org/bmad-loop

#### State model

BMAD uses durable repository artifacts for stories, planning output, and sprint state.

Recent BMAD work introduced more machine-readable story contracts and deterministic planning/build handoff behavior. bmad-loop adds its own durable run state over those artifacts.

This approaches the desired pattern of recovery from durable authority rather than chat history.

#### Task decomposition

Primary hierarchy is approximately:

project
→ epic
→ story
→ implementation work

This is more product/story oriented than a Milestone → JIT Card hierarchy.

Most story structure is planned before execution, although implementation detail can be refined near execution.

#### Fresh-context/subagent behavior

Strong when using bmad-loop. Development and review can be performed by distinct disposable coding-agent sessions.

Source:
https://github.com/bmad-code-org/bmad-loop

#### Testing and review

One of the strongest candidates.

BMAD has explicit code-review workflows, and bmad-loop adds adversarial review cycles with a configurable maximum. Current documentation describes a bounded cycle rather than permitting endless RED → fix → review loops.

Sources:
- https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md
- https://github.com/bmad-code-org/bmad-loop

#### Resumability

Strong in concept and implemented through durable files/state, but the automation layer remains young and should be tested under crash/recovery conditions before becoming foundational.

#### Provider/runtime coupling

BMAD supports multiple development environments.

bmad-loop supports several major coding runtimes/CLIs. Pi is not currently a built-in first-party adapter in the reviewed setup documentation.

Source:
https://github.com/bmad-code-org/bmad-loop/blob/main/docs/setup-guide.md

The adapter/plugin model is specifically designed to be extensible without requiring a permanent fork.

Source:
https://github.com/bmad-code-org/bmad-loop/blob/main/docs/FEATURES.md

#### Extensibility

Good. Out-of-tree adapters and profiles make a Pi integration plausible.

#### Maturity caveat

BMAD itself is mature and actively maintained. bmad-loop explicitly presents itself as early beta/pre-1.0 and should be treated as a promising but still moving runtime.

#### Replacement potential

Closest candidate to replacing both methodology and execution semantics.

Adoption would require accepting:
- BMAD's epic/story worldview;
- its artifact structure;
- a comparatively young automation runtime;
- Pi adapter work.

Conclusion: strongest broad substitute, but higher migration/adoption cost and more runtime maturity risk than Spec Kit plus a proven execution methodology.

### 4.3 obra/superpowers

#### Lifecycle

Representative lifecycle:

brainstorm
→ design
→ human approval
→ implementation plan
→ task implementer
→ self-test/self-review
→ independent reviewer
→ repair/re-review
→ next task
→ final merge-range review
→ finish

Sources:
- https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md

#### Coordinator/orchestration model

A parent/coordinator dispatches bounded implementation tasks to task agents and then dispatches independent review.

The coordinator is not expected to simply do all coding itself.

#### State model

Durable code and plans live in Git, but orchestration legality remains more skill/prompt driven than in a transactional workflow engine such as Spec Kit, Agent Framework, or LangGraph.

This is its major architectural weakness for deterministic recovery.

#### Task decomposition

Very strong.

Superpowers explicitly drives plans toward small, independently implementable/testable/reviewable units.

Source:
https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md

Its semantics are close to the useful decomposition principle that if two parts can reasonably pass/fail review independently, they should not be one opaque implementation unit.

#### Fresh-context/subagent behavior

Strong when the host supports real subagents.

Implementer and reviewer are distinct roles/agents.

The current repair design also has explicit escalation:
- early repair rounds can return to the original implementer;
- repeated failures can escalate to a fresh implementer or stronger context/model;
- repair is bounded rather than allowed to cycle forever.

Source:
https://github.com/obra/superpowers/blob/main/docs/superpowers/plans/2026-07-15-sdd-fix-loop-redesign.md

#### Testing and review

Very strong.

Implementation includes testing and self-review, followed by independent task review, with broader final review after the task set.

Source:
https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md

#### Resumability

Moderate rather than excellent.

Git provides durable implementation history, but workflow legality is not primarily a machine-enforced persistent state machine.

This distinction is important because host behavior can still skip or weaken an intended gate if integration semantics are imperfect.

Example current issue evidence:
https://github.com/obra/superpowers/issues/2372

#### Provider/runtime coupling

Good. Superpowers supports multiple hosts and currently includes Pi support.

Sources:
- https://github.com/obra/superpowers/releases
- https://github.com/obra/superpowers/blob/main/skills/using-superpowers/references/pi-tools.md

Pi may require an optional subagent package for richer worker isolation; otherwise behavior can degrade toward same-session execution.

#### Extensibility

Skill/plugin oriented and generally usable without a permanent fork.

#### Replacement potential

Could plausibly replace much of:
- implementation-plan semantics;
- task right-sizing;
- implementer/reviewer separation;
- repair escalation;
- final code-review semantics.

It cannot by itself replace a deterministic durable workflow/state kernel.

Conclusion: strongest existing component for task/Card execution and review semantics.

### 4.4 Kiro

#### Lifecycle

Representative lifecycle:

idea
→ requirements
→ design
→ task graph
→ dependency analysis
→ independent tasks execute in waves
→ implementation/testing
→ validation against the spec
→ PR/human review

Source:
https://kiro.dev/docs/specs/

#### Coordinator/orchestration model

Kiro combines:
- IDE/CLI/web execution;
- custom agents;
- subagents;
- hooks;
- task lifecycle integration;
- parallel task execution.

Tasks can be arranged by dependencies and independent tasks can run concurrently in waves.

#### State model

Specifications are durable repository artifacts, commonly under .kiro/specs. Runtime/session state is also managed by the product.

This is less runtime-neutral than a design where Git artifacts alone are canonical workflow authority.

#### Task decomposition

Requirements → design → tasks is first-class. Tasks are generally generated before execution and dependency relationships drive concurrency.

This is a task-DAG model rather than a JIT Card model.

#### Fresh-context/subagent behavior

Subagents are available, but public Kiro workflow semantics do not impose the same mandatory fresh implementer/fresh reviewer identity contract as Superpowers or bmad-loop.

#### Testing and review

Hooks can run around lifecycle/tool/file events, including pre-action and post-action checks. Kiro can validate implementation against its Spec.

Sources:
- https://kiro.dev/docs/specs/
- https://kiro.dev/docs/hooks/

Independent adversarial review with an explicitly bounded repair policy is less central.

#### Resumability

Repository Specs plus product-managed sessions provide practical persistence, but the durable legality model is more product-managed than Git-authoritative.

#### Provider/runtime coupling

High. Kiro is vertically integrated and proprietary.

#### Extensibility

Good inside the Kiro ecosystem through hooks, steering, custom agents, and subagents.

#### Replacement potential

If runtime neutrality is not required, Kiro could eliminate more custom infrastructure than most other single products.

Gains:
- integrated specs;
- supported task graph;
- concurrency;
- subagents;
- hooks;
- implementation environment;
- UI/CLI/cloud surfaces.

Losses:
- runtime neutrality;
- exact Git-authoritative workflow legality;
- strong mandatory fresh-review semantics;
- exact custom Milestone/Card semantics;
- provider independence.

Conclusion: best all-in-one control experiment.

### 4.5 Microsoft Agent Framework

#### Lifecycle

Agent Framework intentionally supplies no fixed SDLC. A custom software workflow could be modeled as:

DiscoveryExecutor
→ RequirementsExecutor
→ human gate
→ ArchitectureExecutor
→ decomposition
→ parallel ImplementationExecutors
→ testing
→ review
→ repair loop
→ integration

#### Coordinator/orchestration model

Very strong.

Supports explicit workflows composed from agents/executors, sequential and concurrent execution, handoffs, group collaboration, and human interaction.

Source:
https://learn.microsoft.com/en-us/agent-framework/workflows/

#### State model

Excellent for runtime state.

Checkpoints can capture executor state, pending messages, external requests, and shared workflow state.

Source:
https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints

Durable Task integration can checkpoint around agent calls and resume failed workflows without necessarily replaying already-completed work.

Source:
https://learn.microsoft.com/en-us/azure/durable-task/sdks/durable-agents-microsoft-agent-framework

#### Task decomposition

Whatever the application programs. Agent Framework does not determine what a correctly sized software implementation task should be.

#### Fresh-context/subagent behavior

Can be implemented cleanly using isolated agents/executors/threads, but the policy is authored by the application.

#### Testing/review

Fully expressible, not prepackaged as an SDLC methodology.

#### Resumability

Excellent and one of the clearest reasons not to write a low-level workflow engine from scratch.

#### Provider/runtime coupling

Lower than provider-native coding products. Agent Framework is intended as a multi-provider framework and supports interoperability mechanisms.

Wrapping Pi still requires an adapter/executor layer.

#### Extensibility

Excellent.

#### Replacement potential

Can replace:
- generic workflow engine;
- runtime checkpoints;
- parallel scheduling;
- retries;
- human interruption/resume;
- agent dispatch;
- much observability/runtime machinery.

Cannot replace:
- SDLC semantics;
- task sizing rules;
- definition/planning artifact policy;
- review policy;
- Git authority model.

Conclusion: strong substrate if intentionally building a workflow product, but less useful if the objective is to avoid owning custom workflow semantics at all.

### 4.6 LangGraph / LangChain agent workflows

#### Lifecycle

No prescribed SDLC. The framework provides arbitrary state graph execution:

state graph
→ nodes
→ branches/subgraphs
→ interrupts
→ checkpoints
→ resume

#### Coordinator/orchestration model

Graph-native rather than development-methodology-native.

Subgraphs can model specialist agents or isolated sub-workflows.

#### State model

Very strong.

Checkpointing supports durable execution, retry, human intervention, time travel, memory, and restart/resume. Persistent production backends can be used instead of in-memory state.

Source:
https://github.com/langchain-ai/langgraph/blob/main/libs/checkpoint/README.md

#### Task decomposition

User-defined.

#### Fresh-context/subagent behavior

Independent agents can be nodes or subgraphs, but LangGraph does not define software-task size or reviewer identity semantics.

#### Testing/review

Custom graph policy.

#### Resumability

One of the core strengths.

Current issue activity also demonstrates how complex crash consistency and checkpoint ordering can be in a real state engine, reinforcing the cost of reimplementing this functionality.

Example:
https://github.com/langchain-ai/langgraph/issues/8234

#### Provider/runtime coupling

Low.

#### Extensibility

Excellent, but largely by writing application code.

#### Replacement potential

Excellent replacement for a homemade orchestration runtime, poor replacement for a software-development methodology.

Conclusion: if Project Workflow deliberately remains a custom domain workflow product, LangGraph is plausible substrate; if the goal is to stop building workflow machinery, higher-level systems should be tested first.

### 4.7 Claude Code multi-agent/subagent workflows

#### Lifecycle

Claude Code does not impose a complete discovery-to-release lifecycle.

Relevant runtime pattern:

main session/coordinator
→ delegate bounded work to isolated subagent/team member
→ worker operates in separate context/worktree
→ result returned
→ coordinator integrates/reviews
→ continue

Anthropic's Projects/team direction extends this toward parallel full coding sessions under a project coordinator.

Sources:
- https://code.claude.com/docs/id/features-overview
- https://claude.com/blog/projects-redesigned

#### Coordinator/orchestration model

Relevant mechanisms include:
- subagents controlled by a parent;
- agent teams/project coordination where workers are more autonomous;
- shared task structures;
- worktree isolation.

#### State model

Strong within the runtime, but canonical state is not purely repository state.

#### Task decomposition

Coordinator or human defined. There is no mandatory project → milestone → Card hierarchy.

#### Fresh-context/subagent behavior

Strong. Subagents can have dedicated prompts, permissions, tools, and isolated contexts. Worktrees provide additional code-level isolation.

#### Testing/review

Reviewer agents are straightforward to instantiate, but independent review and bounded repair are capabilities rather than universal workflow invariants.

#### Resumability

Good within Claude's own session/runtime model.

#### Provider/runtime coupling

Very high: Anthropic/Claude.

#### Extensibility

Strong through subagents, skills, hooks, MCP, and SDK capabilities.

#### Replacement potential

Could replace a sophisticated coding orchestrator if Claude is accepted as the runtime. It does not naturally provide a runtime-neutral workflow authority.

### 4.8 OpenAI Codex / Agents API

#### Lifecycle

No mandatory SDLC. Representative orchestration:

root agent
→ analyze goal
→ delegate bounded work to independent-context subagents
→ subagents modify/test in managed environment
→ root collects results
→ optionally delegate review/remediation
→ final result

Sources:
- https://developers.openai.com/api/docs/guides/agents-api/overview
- https://developers.openai.com/api/docs/guides/agents-api/multi-agent

#### Coordinator/orchestration model

Current public OpenAI agent facilities support multi-agent delegation and parallel workers with focused contexts.

#### State model

Managed durable agent sessions around the Codex harness provide continuation and context management.

This removes considerable runtime infrastructure for an OpenAI-centric system but does not make Git the sole canonical workflow authority.

#### Task decomposition

Agent-driven rather than governed by a fixed SDLC hierarchy.

#### Fresh-context/subagent behavior

Strong. Subagents can receive bounded independent contexts.

#### Testing/review

Independent reviewer and remediation agents can be constructed naturally, but a standard bounded software-review protocol is not the built-in methodology.

OpenAI documentation also distinguishes dynamic multi-agent delegation from a deliberately modeled deterministic graph.

Source:
https://developers.openai.com/api/docs/guides/responses-multi-agent

#### Resumability

Strong as managed service infrastructure.

#### Provider/runtime coupling

High.

#### Extensibility

Strong through APIs/SDKs, but Pi interoperability requires an explicit external adapter.

#### Replacement potential

Can eliminate much OpenAI-specific orchestration runtime code, but cannot serve as a provider-neutral canonical authority if Pi and unrelated runtimes remain equal execution targets.

## 5. Additional significant candidates

### 5.1 OpenSpec

OpenSpec is a strong lightweight specification authority.

Representative flow:

proposal
→ specs/design/tasks
→ implementation
→ archive
→ accepted change becomes canonical specification

Source:
https://github.com/Fission-AI/OpenSpec/blob/main/README.md

Strengths:
- durable repository artifacts;
- human-readable Markdown;
- change-oriented workflow;
- machine-consumable CLI output.

It does not supply:
- worker scheduling;
- fresh implementation agents;
- reviewer assignment;
- repair loops;
- full runtime state.

Conclusion: useful spec layer, naturally paired with a separate orchestrator.

### 5.2 CrewAI

CrewAI is relevant mainly as runtime substrate.

Its Flows support branches, loops, and persistent state. Its hierarchical process supplies a manager agent that delegates work and validates outcomes.

Sources:
- https://docs.crewai.com/en/concepts/flows
- https://docs.crewai.com/en/learn/hierarchical-process

It does not impose software-development task sizing, review semantics, or a complete SDLC. Those must be authored by the application.

Conclusion: can host a custom workflow cleanly but does not itself remove the need to define one.

### 5.3 OpenHands

OpenHands has evolved into a substantial agent platform with SDK, local/ephemeral workspaces, and cloud execution infrastructure.

Source:
https://github.com/OpenHands/software-agent-sdk

Strengths:
- execution runtime;
- workspace isolation;
- local/cloud flexibility;
- agent SDK.

The reviewed material provides less evidence of a strongly opinionated discovery → specification → decomposition → independent review lifecycle.

Conclusion: strong execution layer, weaker complete methodology.

### 5.4 GitHub Copilot Agents / code review

Copilot now functions as an agent platform rather than only editor completion.

Relevant capabilities include:
- custom agents/subagents;
- isolated contexts;
- parallel task agents;
- code-review/security/research specialists;
- cloud coding agents;
- lifecycle hooks.

Sources:
- https://docs.github.com/en/copilot/responsible-use/agents
- https://docs.github.com/en/copilot/concepts/agents/code-review

The missing piece is a complete portable development-state authority outside the Copilot/GitHub ecosystem.

### 5.5 Devin

Devin is a commercial all-in-one autonomous engineering environment.

Capabilities include:
- autonomous implementation;
- planning;
- testing;
- PR generation;
- parallel sessions;
- delegated/child work;
- review workflows.

Source:
https://docs.devin.ai/

It may eliminate substantial operational burden, but workflow/state semantics are proprietary. This is a poor fit if inspectable deterministic repository recovery and runtime portability are hard requirements.

### 5.6 Get Shit Done (GSD)

GSD is important prior art despite its archived status.

Its architecture demonstrates that several supposedly unusual concepts already existed in mature community workflows:
- thin coordinator;
- fresh context per worker;
- research/planning before implementation;
- dependency waves;
- planner/checker separation;
- bounded revision attempts;
- durable planning artifacts.

Source:
https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md

The repository was archived in 2026, so it should not become a new foundational dependency.

### 5.7 MetaGPT

MetaGPT popularized the "software company as cooperating roles" model:

requirement
→ product manager
→ architect
→ project manager
→ engineer

Source:
https://github.com/FoundationAgents/MetaGPT/blob/main/README.md

It remains influential conceptually, but its durable workflow/recovery model is less compelling than current Spec Kit, Agent Framework, or LangGraph for the specific problem here.

### 5.8 SWE-agent / mini-swe-agent

Representative lifecycle:

issue
→ inspect repository/environment
→ edit
→ run tests
→ produce solution

Source:
https://github.com/SWE-agent/SWE-agent/blob/main/docs/index.md

Excellent as worker/runtime research and focused autonomous coding, but deliberately narrower than a complete project-development lifecycle.

### 5.9 AutoGen

AutoGen remains important historically, but current Microsoft direction matters more than past popularity.

Microsoft's current repository/documentation directs new work toward Agent Framework while AutoGen is maintained for existing users.

Source:
https://github.com/microsoft/autogen/blob/main/README.md

Conclusion: do not select AutoGen for a new architecture merely because it is historically famous.

### 5.10 OpenAI Symphony

Symphony is architecturally important even though it should not be treated as an adoptable production product.

Architecture:
- external issue tracker/control plane;
- authoritative coordinator;
- isolated workspaces per issue;
- dependency graph;
- coding agents;
- monitoring/restart;
- human review.

Sources:
- https://github.com/openai/symphony/blob/main/README.md
- https://github.com/openai/symphony/blob/main/SPEC.md
- https://openai.com/index/open-source-codex-orchestration-symphony/

OpenAI explicitly presents Symphony as a reference/engineering preview rather than a maintained standalone product.

Its architectural significance is that separation between durable control-plane state and disposable worker execution is now established prior art.

## 6. Lifecycle capability matrix

Legend:
- Strong = first-class/current capability.
- Partial = available but runtime-dependent, optional, or straightforward extension.
- No = not supplied as a normal first-class semantic.

| System | Discovery | Requirements/spec | Architecture | Structured decomposition | Coordinator | Fresh workers | Dependency/parallel execution | Durable state/resume | Human gates | Independent review | Bounded repair | Higher-level/final review | Provider portability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Spec Kit | Partial | Strong | Strong | Strong | Strong | Partial | Strong | Strong | Strong | Partial | Partial | Partial | Strong |
| BMAD + bmad-loop | Strong | Strong | Strong | Strong | Strong | Strong | Partial/Strong | Strong | Strong | Strong | Strong | Strong | Strong/Partial |
| Superpowers | Strong | Partial | Partial | Strong | Strong | Strong | Partial | Partial | Strong | Strong | Strong | Strong | Strong |
| Kiro | Strong | Strong | Strong | Strong | Strong | Strong | Strong | Partial/Strong | Strong | Partial | Partial | Partial | No |
| Microsoft Agent Framework | No | No | No | No | Strong | Strong | Strong | Strong | Strong | Partial | Partial | Partial | Strong |
| LangGraph | No | No | No | No | Strong | Strong | Strong | Strong | Strong | Partial | Partial | Partial | Strong |
| Claude Code | No | No | No | Partial | Strong | Strong | Strong | Partial/Strong | Partial | Partial | No/Partial | Partial | No |
| Codex / Agents API | No | No | No | Partial | Strong | Strong | Strong | Strong | Partial | Partial | No/Partial | Partial | No |
| GitHub Copilot Agents | No | Partial | No | Partial | Strong | Strong | Strong | Partial | Partial | Strong | No/Partial | Partial | No/Partial |
| OpenHands | No | No | No | Partial | Strong | Partial/Strong | Partial | Partial | Partial | Partial | No | No/Partial | Strong/Partial |

The important pattern is that methodology/spec systems are strong across the development-lifecycle columns, while generic orchestration frameworks are strong across state/runtime columns.

No single open, runtime-neutral product dominates both halves.

## 7. Maturity assessment

### GitHub Spec Kit

Status: very active in 2026.

Maturity signals:
- extensive documentation;
- workflow engine;
- many integrations/extensions;
- large open-source community.

Caution:
- workflow engine capabilities are still evolving;
- nested resume semantics are not equivalent to a fully transactional state machine at every instruction boundary.

Sources:
- https://github.com/github/spec-kit/blob/main/docs/index.md
- https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md

### BMAD Method

Status: very active v6 line.

Maturity signals:
- increasingly deterministic artifacts/scripts;
- explicit story contracts;
- structured planning/build/review workflows;
- substantial community.

Caution:
- large methodology surface increases adoption/migration cost.

Source:
https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md

### bmad-loop

Status: active, early beta/pre-1.0.

Maturity signals:
- explicit state machine;
- adapters;
- disposable sessions;
- bounded review loops.

Caution:
- breaking changes and edge cases should be expected before 1.0.

Source:
https://github.com/bmad-code-org/bmad-loop

### Superpowers

Status: very active.

Maturity signals:
- detailed development/review semantics;
- multiple runtime integrations;
- explicit bounded repair design.

Caution:
- some guarantees are host-enforced rather than enforced by a separate transactional workflow kernel.

Sources:
- https://github.com/obra/superpowers/releases
- https://github.com/obra/superpowers/issues/2372

### Kiro

Status: active managed product.

Maturity signals:
- integrated specs, agents, hooks, subagents, task scheduling.

Caution:
- proprietary/runtime lock-in.

Source:
https://kiro.dev/docs/

### Microsoft Agent Framework

Status: active 1.x-era development in 2026.

Maturity signals:
- Microsoft-backed;
- checkpoint model;
- durable task integration;
- designated successor direction to AutoGen.

Sources:
- https://github.com/microsoft/agent-framework/releases
- https://learn.microsoft.com/en-us/agent-framework/workflows/

### LangGraph

Status: active and broadly used.

Maturity signals:
- production-oriented checkpoint model;
- persistent state backends;
- established graph abstractions.

Caution:
- checkpoint/recovery semantics are intrinsically complex and continue to receive edge-case fixes.

Sources:
- https://github.com/langchain-ai/langgraph/releases
- https://github.com/langchain-ai/langgraph/issues/8234

### CrewAI

Status: active.

Maturity signals:
- large ecosystem;
- manager/delegation model;
- persistent Flows.

Caution:
- SDLC semantics remain custom application logic.

Source:
https://docs.crewai.com/

### OpenHands

Status: actively developed.

Maturity signals:
- SDK/runtime/workspace architecture;
- local/cloud execution.

Caution:
- more execution platform than deterministic end-to-end SDLC methodology.

Source:
https://github.com/OpenHands/software-agent-sdk

### Claude Code

Status: mature coding runtime with newer coordinator/team/project capabilities.

Maturity signals:
- strong tooling;
- isolated contexts/subagents;
- worktrees;
- agent/team support.

Caution:
- provider coupling and newer coordinator-layer semantics.

Sources:
- https://code.claude.com/docs/id/features-overview
- https://claude.com/blog/projects-redesigned

### OpenAI Codex / Agents API

Status: actively evolving 2026 managed agent infrastructure.

Maturity signals:
- durable agent sessions;
- multi-agent support;
- Codex harness;
- managed environment.

Caution:
- newer API surface and high OpenAI coupling.

Sources:
- https://developers.openai.com/api/docs/guides/agents-api/overview
- https://developers.openai.com/api/docs/guides/agents-api/multi-agent

### GSD

Status: archived.

Value:
- important prior art.

Recommendation:
- study architecture; do not make it a new foundational dependency.

Source:
https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md

### AutoGen

Status: maintenance-oriented relative to new Microsoft Agent Framework work.

Recommendation:
- use only for compatibility/existing systems; do not make it the default choice for new work.

Source:
https://github.com/microsoft/autogen/blob/main/README.md

## 8. Project Workflow V2.1 decomposition against the landscape

This section compares the independently researched landscape with the supplied Project Workflow V2.1 characteristics.

The current custom system roughly includes:
- Brainstorming;
- Definition;
- Strategic Planning;
- plan review;
- milestones;
- JIT Card materialization;
- independent Card Review;
- Milestone Review;
- final integration review;
- durable Git-backed state;
- deterministic continuation/recovery;
- typed execution obligation/result boundary;
- runtime-neutral design intended to switch between ChatGPT and Pi/orchestration runtime;
- fresh implementer/reviewer concepts;
- bounded review/repair convergence;
- separation between workflow legality and runtime scheduling.

### 8.1 Commodity functionality already solved well elsewhere

#### Generic workflow execution

The following primitives are mature elsewhere:
- persisted runtime state;
- checkpoints;
- resume;
- retries;
- conditionals;
- loops;
- fan-out/fan-in;
- parallel workers;
- human gates.

Systems:
- GitHub Spec Kit workflows;
- Microsoft Agent Framework;
- LangGraph;
- CrewAI Flows.

Conclusion: building another generic workflow engine for these features is reinvention unless existing engines demonstrably fail a specific required invariant.

#### Fresh specialized workers

Mature elsewhere:
- disposable implementation contexts;
- specialized reviewers;
- parallel coding workers;
- worktree/workspace isolation;
- coordinator/worker separation.

Systems:
- Superpowers;
- bmad-loop;
- Claude Code;
- Codex;
- Copilot;
- OpenHands.

Conclusion: basic subagent dispatch should not be reimplemented as custom infrastructure.

#### Dependency-aware scheduling

Solved elsewhere by:
- Kiro task dependency waves;
- Spec Kit fan-out/fan-in;
- GSD dependency waves;
- generic graph/DAG workflow engines.

Conclusion: a custom DAG scheduler needs an unusually strong justification.

#### Repository-resident specs and plans

Mature in:
- Spec Kit;
- OpenSpec;
- BMAD;
- Kiro.

Conclusion: "durable plans/specifications in Git" is useful but no longer differentiating.

#### Basic review/repair loops

Superpowers and BMAD/bmad-loop already implement sophisticated versions.

Superpowers in particular includes escalation after repeated review failures and a terminal bound rather than allowing an endless RED loop.

Source:
https://github.com/obra/superpowers/blob/main/docs/superpowers/plans/2026-07-15-sdd-fix-loop-redesign.md

Conclusion: implement → review → repair → re-review is commodity as a general pattern.

#### Runtime adapters

Spec Kit's integration catalog and bmad-loop's adapter model demonstrate that runtime adapters can be extension points rather than core workflow code.

Sources:
- https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- https://github.com/bmad-code-org/bmad-loop/blob/main/docs/FEATURES.md

Conclusion: hard-coded runtime plumbing should be minimized.

### 8.2 Functionality likely adaptable from existing systems

#### Brainstorming → Definition → Strategic Planning

The overall pattern is common:
- BMAD provides a rich front-half lifecycle;
- Spec Kit provides a lighter spec/plan/task model;
- OpenSpec provides durable spec/change artifacts.

The exact distinction among Brainstorming, Definition, and Strategic Planning can remain project policy without requiring a bespoke runtime.

#### Milestone → Card hierarchy

Existing equivalents:
- BMAD epic → story;
- Spec Kit phase → task;
- Kiro task graph;
- Symphony issue → child/dependency issue.

The labels are not inherently differentiating.

What may remain important is when lower-level units are materialized.

#### Milestone Review / final integration review

Can be modeled through:
- Superpowers final merge-range review;
- BMAD epic/sprint-level evaluation;
- workflow-stage reviewer agents;
- fan-in verification after parallel implementation.

The exact ceremony can be retained as policy without requiring custom scheduling infrastructure.

#### ChatGPT ↔ Pi split

More feasible with existing components than in earlier generations.

Spec Kit directly supports Pi and stores semantic development artifacts in the repository.

Source:
https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md

A planning/review environment can therefore operate over durable artifacts while Pi performs implementation.

The remaining missing piece is a clean protocol specifying who may authorize transitions and how a runtime reports results. That is much smaller than a complete workflow engine.

### 8.3 Genuinely differentiated/useful custom semantics

These are the areas that do not appear fully solved as a package by current mature products.

#### A. JIT Card materialization under durable higher-level planning

Most systems plan a large portion of their task/story set before implementation.

A policy of:
- approve milestone-level intent/invariants;
- materialize only the exact next independently executable Card when execution reaches it;
- bind it against the latest accepted upstream results;

is not a common first-class off-the-shelf behavior.

This can justify custom policy.

#### B. Typed execution obligation/result boundary

A model where:
- workflow authority emits a typed runtime-neutral obligation;
- a runtime fulfills it;
- the runtime returns a typed semantic result;
- the workflow separately validates/accepts the result;

is more explicit than the common "send a prompt to a worker and inspect its output" model.

Generic agent frameworks have typed state, but do not provide this software-development contract by default.

This appears worth preserving if cross-runtime execution is central.

#### C. Runtime-independent workflow legality

The distinction:

workflow authority decides whether a transition is legal;
runtime scheduler decides how an already-authorized obligation executes

is architecturally valuable.

Related control-plane/data-plane patterns exist elsewhere, including Symphony, but this separation is not universally enforced by development products.

Source:
https://github.com/openai/symphony/blob/main/SPEC.md

#### D. Strong Git-authoritative recovery across heterogeneous runtimes

Spec Kit and BMAD/bmad-loop come close.

What remains unusual is requiring a completely different coordinator/model/runtime to recover all legally relevant continuation state from durable repository authority without depending on the previous chat/session/runtime.

This is a meaningful portability property.

#### E. Combined fresh agents + bounded convergence + runtime neutrality

Superpowers has strong fresh-agent and bounded-repair semantics.
bmad-loop has disposable sessions and bounded review.
Spec Kit has broad runtime integration and durable workflow state.

No reviewed system combines all three as strongly and explicitly as the described Project Workflow design.

The combination rather than any individual feature is differentiated.

## 9. Explicit reinvention analysis

Project Workflow V2.1 appears to be reinventing mature functionality if it independently implements the following as generic infrastructure:

| Area | Mature alternatives |
| --- | --- |
| Generic state-machine execution | Spec Kit workflows, Microsoft Agent Framework, LangGraph, CrewAI Flows |
| Persisted checkpoints | Agent Framework, LangGraph, Spec Kit |
| Human pause/resume | Spec Kit, Agent Framework, LangGraph |
| Generic loop/retry machinery | Spec Kit, Agent Framework, LangGraph |
| Generic fan-out/fan-in | Spec Kit, Agent Framework, LangGraph |
| Dependency-wave scheduling | Kiro, GSD, generic DAG engines |
| Fresh coding contexts | Superpowers, bmad-loop, Claude, Codex, Copilot |
| Independent review agents | Superpowers, BMAD, Copilot |
| Repair/re-review mechanics | Superpowers, BMAD/bmad-loop |
| Bounded review loops | Superpowers, bmad-loop |
| Git-resident specifications | Spec Kit, OpenSpec, BMAD, Kiro |
| Multi-provider integration | Spec Kit, Agent Framework, LangGraph |
| Agent-runtime adapter abstraction | Spec Kit, bmad-loop |
| Lifecycle hooks | Kiro, Copilot, Spec Kit event/integration layer |
| Worktree/workspace isolation | Claude, bmad-loop, Symphony, OpenHands and other coding harnesses |

The fact that PWv2.1 may use these primitives in a distinctive way does not make the primitives themselves worth reimplementing.

## 10. Explicit gap analysis: where existing products do not solve the same problem

The following remain defensible custom semantics:

1. JIT implementation-unit materialization rather than generating the entire low-level plan up front.
2. Strong task-size legality based on independent testability/reviewability.
3. Explicit typed obligation/result protocol independent of model, provider, or coding CLI.
4. Canonical workflow authority that survives runtime/model changes and does not depend on conversation state.
5. Mandatory fresh implementer and reviewer as workflow invariants, not merely optional capabilities.
6. Bounded repair convergence encoded as policy, including escalation and a true blocked state.
7. Multiple review levels such as Card, Milestone, and final integration with distinct scopes.
8. Cross-runtime continuation where ChatGPT may plan/review and Pi may implement without either runtime becoming sole state owner.
9. Strong separation between legal workflow transitions and runtime scheduling policy.

No current serious candidate reviewed here provides all nine together.

This justifies retaining some custom policy semantics, not necessarily a large custom workflow runtime.

## 11. Architecture options

### Option A: adopt one product mostly unchanged

Best candidate: Kiro.

Representative architecture:

Kiro Specs
→ Kiro task graph
→ Kiro agents/subagents
→ hooks/testing
→ validation
→ PR/review

Qualitative assessment:

| Dimension | Assessment |
| --- | --- |
| Implementation effort | Low |
| Ongoing maintenance | Low |
| Vendor lock-in | High |
| ChatGPT ↔ Pi portability | Low |
| Operational reliability | High relative to DIY |
| Custom code | Very low |
| Fidelity to PWv2.1-specific semantics | Medium-low |

Gained:
- supported integrated platform;
- specs;
- task graph;
- dependency-aware concurrency;
- subagents;
- hooks;
- development runtime;
- UI/CLI/cloud surfaces.

Lost:
- runtime-neutral authority;
- typed cross-runtime handoff;
- strict Git-authoritative legality;
- exact fresh reviewer/bounded convergence policy;
- JIT Card semantics.

Use this option when minimizing maintenance is more important than provider independence.

### Option B: methodology + generic orchestrator

Examples:
- Superpowers + Microsoft Agent Framework;
- Superpowers + LangGraph.

Representative architecture:

development methodology/policy
→ generic durable orchestrator
→ worker runtimes
→ independent reviewers/testers
→ durable results/state

Qualitative assessment:

| Dimension | Assessment |
| --- | --- |
| Implementation effort | Medium-high |
| Ongoing maintenance | Medium |
| Lock-in | Low |
| Portability | High |
| Correctness/reliability | High if implemented carefully |
| Custom code | Medium-high |

Strength:
- mature runtime primitives;
- excellent portability;
- avoids reimplementing checkpointing/concurrency.

Weakness:
- still requires substantial custom mapping of software-development policy into executable graph/state logic.

Use this architecture only if a higher-level spec/workflow product proves insufficient.

### Option C: spec/workflow system + separate coding runtime

Best candidate combination:
- GitHub Spec Kit as durable control plane;
- Pi as coding runtime;
- optionally Superpowers for execution/review semantics.

Representative architecture:

Spec Kit repository authority
→ specification/plan
→ workflow chooses authorized implementation unit
→ Pi executes
→ independent review/test path
→ result returned
→ workflow records/validates transition
→ next unit

Qualitative assessment:

| Dimension | Assessment |
| --- | --- |
| Implementation effort | Medium |
| Ongoing maintenance | Low-medium |
| Lock-in | Low |
| ChatGPT ↔ Pi portability | High |
| Correctness/reliability | Potentially high |
| Custom code | Low-medium |
| Fidelity to PWv2.1-specific semantics | High |

This is the strongest overall fit.

Spec Kit can own:
- durable specs/plans;
- workflow run state;
- gates;
- loops;
- fan-out/fan-in;
- broad integrations;
- generic resume.

Pi can own:
- actual code execution.

Superpowers can own:
- implementation-task sizing guidance;
- fresh implementer/reviewer discipline;
- repair escalation;
- bounded convergence;
- final code review.

A thin custom layer can own only:
- milestone/Card legality;
- JIT Card materialization;
- typed obligation/result schema;
- cross-runtime authority rules;
- any review semantics not covered cleanly elsewhere.

A fork should usually not be necessary.

### Option D: BMAD + bmad-loop + Pi adapter

Representative architecture:

BMAD discovery/PRD/architecture
→ epics/stories
→ sprint/story authority
→ bmad-loop
→ fresh development session
→ verify
→ fresh adversarial review
→ bounded repair
→ completion

Qualitative assessment:

| Dimension | Assessment |
| --- | --- |
| Implementation effort | Medium |
| Ongoing maintenance | Medium |
| Lock-in | Low-medium |
| Portability | High after Pi adapter |
| Correctness/reliability | Promising but automation runtime still beta |
| Custom code | Low-medium |
| Fidelity to target lifecycle | High |

Gained:
- complete methodology;
- durable planning/story state;
- fresh worker sessions;
- review loops;
- bounded convergence;
- human gates;
- clean adapter seam.

Required custom work:
- Pi adapter;
- mapping current Milestone/Card semantics if they are retained;
- typed obligation/result compatibility if desired.

Main risk:
- bmad-loop maturity.

### Option E: thin custom policy/state layer around mature components

Representative architecture:

small PW policy kernel
→ durable repository authority
→ existing workflow/state engine
→ runtime adapter
→ Pi / Codex / Claude / other worker
→ reusable review methodology
→ typed result
→ policy validates transition

Qualitative assessment:

| Dimension | Assessment |
| --- | --- |
| Implementation effort | Medium |
| Ongoing maintenance | Low-medium |
| Lock-in | Low |
| Portability | Very high |
| Correctness/reliability | High if boundaries are narrow |
| Custom code | Low-medium |
| Preservation of differentiated semantics | Very high |

This option preserves only the parts that are genuinely differentiating:
- JIT materialization;
- legal-state policy;
- typed obligation/result boundary;
- cross-runtime recovery/authority;
- multi-level review policy where needed.

Everything else should be delegated to mature components.

This is the strongest long-term target if no single product passes all prototype tests.

### Option F: fully custom workflow/state engine

Representative architecture:

custom Project Workflow policy
+ custom state engine
+ custom scheduler
+ custom adapters
+ custom review/repair
+ custom persistence/resume
+ custom runtime integration

Qualitative assessment:

| Dimension | Assessment |
| --- | --- |
| Implementation effort | Very high |
| Ongoing maintenance | Very high |
| Lock-in | Low |
| Portability | Potentially very high |
| Correctness/reliability | Entirely dependent on bespoke engineering |
| Custom code | Very high |

This is justified only where existing engines cannot satisfy required semantics after prototype testing.

It should not be the default merely because PWv2.1 already exists.

## 12. Main architectural answer

The market does not point cleanly to one all-in-one product for a runtime-neutral ChatGPT ↔ Pi workflow.

The strongest observed composition is:

repository-native specification/workflow control plane
+ replaceable coding runtime
+ reusable development methodology
+ minimal domain-policy kernel

This is a refinement of "spec/workflow system + separate coding runtime".

It keeps control-plane authority independent while treating coding agents as replaceable execution resources.

## 13. Practical implications for ChatGPT ↔ Pi

The key architectural requirement is that neither ChatGPT nor Pi should need to own the canonical workflow state.

A viable split is:

ChatGPT:
- discovery;
- research synthesis;
- planning;
- architecture/review;
- policy-level decisions where authorized.

Repository control plane:
- durable specs;
- plans;
- execution eligibility;
- typed obligations/results;
- review outcomes;
- continuation state.

Pi:
- implementation execution;
- task-local tests;
- worker subagents;
- repair implementation.

Independent reviewer runtime:
- may be Pi, another coding runtime, or another model;
- must consume durable task/authority context rather than hidden implementer chat history.

Spec Kit is relevant because Pi is already an explicit supported integration and its principal semantic artifacts live in the repository.

Superpowers is relevant because it already targets Pi and supplies strong implementer/reviewer semantics.

The remaining adapter work should ideally be only:
- translate authorized obligation into the worker invocation;
- capture structured result;
- attach evidence;
- return control to the repository authority.

That is substantially smaller than building a new scheduler/checkpoint/runtime system.

## 14. Prototype shortlist before further custom workflow expansion

### Prototype 1: GitHub Spec Kit + Pi

Highest priority because it tests whether the largest amount of custom infrastructure can disappear.

Test:
- specification;
- planning;
- task generation;
- human gate;
- workflow interruption;
- kill all sessions/processes;
- resume from durable state;
- parallel/fan-out work;
- verification/converge;
- completion.

Verify specifically:
- clean-clone recovery;
- what state exists outside Git;
- nested-loop resume behavior;
- Pi dispatch control;
- ability for a different coordinator to continue;
- whether workflow status can be reconstructed without chat history.

Source for Pi integration:
https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md

### Prototype 2: Superpowers on Pi with real subagents

Test:

coordinator
→ fresh implementer
→ implementation/tests
→ fresh reviewer
→ RED
→ same implementer repair
→ repeated RED
→ escalation/fresh implementer
→ terminal GREEN or blocked

Goal:
determine whether PWv2.1 still needs to own Card-level execution/review/convergence machinery.

Sources:
- https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- https://github.com/obra/superpowers/blob/main/docs/superpowers/plans/2026-07-15-sdd-fix-loop-redesign.md

### Prototype 3: BMAD + bmad-loop

Use a currently supported execution runtime first.

Test:
- durable recovery;
- story selection;
- fresh implementer;
- fresh reviewer;
- bounded review cycles;
- crash during implementation;
- crash during review;
- cross-model reviewer;
- external CLI handoff.

Only after proving the semantics should a Pi adapter be implemented.

Source:
https://github.com/bmad-code-org/bmad-loop/blob/main/docs/FEATURES.md

### Prototype 4: Kiro as the all-in-one control experiment

Run the same representative feature through Kiro and measure what custom behavior is genuinely missing.

Purpose:
quantify the engineering burden that disappears if runtime neutrality is surrendered.

This prevents overvaluing custom architecture merely because it is more flexible.

## 15. What should not be prototyped first

### Microsoft Agent Framework / LangGraph

Not because they are weak. They are strong.

They answer:

"What should a custom workflow engine be built on?"

rather than:

"Can the workflow engine be avoided?"

They should be evaluated only after higher-level systems fail required prototype scenarios.

### AutoGen

For new Microsoft-oriented work, Agent Framework is the current direction.

Source:
https://github.com/microsoft/autogen/blob/main/README.md

### GSD

Study as prior art only because it is archived.

Source:
https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md

### Symphony

Study as reference architecture only because OpenAI explicitly presents it as an engineering preview/reference implementation rather than a maintained standalone product.

Sources:
- https://github.com/openai/symphony/blob/main/README.md
- https://openai.com/index/open-source-codex-orchestration-symphony/

## 16. Prototype acceptance criteria

All candidates should be tested against the same failure-oriented scenarios.

### State/recovery

Kill every chat/process/runtime.

Starting only from:
- repository;
- workflow's documented durable state store;
- clean tool installation;

determine whether the system knows exactly what may legally happen next.

### Cross-runtime portability

Perform planning/review in one environment and implementation in another.

Target scenario:

ChatGPT planning/review
↔ durable authority
↔ Pi implementation

No hidden session context should be necessary for correctness.

### Agent independence

Verify experimentally whether reviewer context is genuinely independent rather than simply a fresh prompt layered over implementer history.

### Review convergence

Force multiple material findings.

Confirm:
- findings are tracked;
- repair is bounded;
- repeated RED eventually escalates;
- the system can enter a blocked state;
- it does not silently loop forever.

### Task isolation

Construct an intentionally oversized implementation unit.

Check whether the system:
- detects the problem;
- splits it;
- preserves dependencies;
- avoids later merging independently reviewable work back into one opaque unit.

### Parallelism

Run independent units concurrently and verify:
- workspace/repository isolation;
- correct fan-in;
- deterministic failure handling.

### Auditability

For every completed transition, answer from durable evidence:
- what was requested?
- which agent/runtime executed it?
- what changed?
- what tests ran?
- what did the reviewer find?
- what authorized the next state?

## 17. Recommended action before more PWv2.1 workflow machinery is built

A temporary architecture freeze on new generic workflow-engine functionality is justified until three primary questions are tested.

### Question 1

Can GitHub Spec Kit replace the generic durable workflow/state/control-plane layer while PW-specific semantics become a small extension or wrapper?

If yes, substantial custom runtime machinery should be removed or never built.

### Question 2

Can Superpowers on Pi replace Card-level execution, testing, fresh review, and bounded repair?

If yes, those semantics should be consumed rather than duplicated.

### Question 3

Does BMAD + bmad-loop provide enough of both methodology and automation that even the remaining custom policy is no longer worth carrying?

If yes, adoption may be preferable despite migration cost.

Only after those tests should Microsoft Agent Framework, LangGraph, or additional custom workflow-kernel engineering become the default direction.

## 18. Final build-vs-adopt assessment

The 2026 landscape does not support the conclusion that a fully bespoke Project Workflow engine is necessary.

It also does not support the opposite conclusion that one mature runtime-neutral product already implements the entire desired architecture.

### Clearly commoditized functionality

- workflow-state persistence;
- checkpoints/resume;
- loops/gates;
- fan-out/fan-in;
- dependency scheduling;
- worker isolation;
- fresh subagents;
- code-review agents;
- bounded repair loops;
- Git-based specs;
- multi-runtime adapters;
- lifecycle hooks;
- generic parallel orchestration.

Continuing to build these from scratch is largely reinvention.

### Plausibly differentiated functionality

- JIT Card materialization;
- task-size legality tied to independent reviewability;
- typed runtime-neutral obligation/result contracts;
- deterministic workflow legality independent of runtime scheduling;
- Git-first recovery across unrelated agent environments;
- mandatory fresh implementer/reviewer semantics;
- multi-level Card → Milestone → integration review;
- one portable policy that can survive ChatGPT ↔ Pi ↔ future runtimes.

Those semantics may justify a custom policy kernel.

They do not justify a custom generic workflow runtime unless existing engines fail concrete prototype tests.

## 19. Recommended target architecture for experimentation

The highest-value prototype target is:

GitHub Spec Kit as durable spec/workflow infrastructure
+ Pi as one replaceable executor
+ Superpowers-style task/review semantics
+ a small Project Workflow policy kernel only for differentiated rules.

BMAD + bmad-loop should be evaluated alongside it as the closest broader replacement.

Kiro should be used as the all-in-one control comparison.

If those prototypes succeed, the custom Project Workflow should become smaller rather than more sophisticated: a portable policy/authority layer sitting on mature external machinery instead of a complete custom workflow engine.

## 20. Official-source index

Primary sources used to support material claims in this report:

### GitHub Spec Kit
- https://github.com/github/spec-kit/blob/main/docs/index.md
- https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md
- https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- https://github.com/github/spec-kit/blob/main/workflows/ARCHITECTURE.md
- https://github.com/github/spec-kit/blob/main/templates/commands/converge.md

### obra/superpowers
- https://github.com/obra/superpowers/releases
- https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- https://github.com/obra/superpowers/blob/main/docs/superpowers/plans/2026-07-15-sdd-fix-loop-redesign.md
- https://github.com/obra/superpowers/blob/main/skills/using-superpowers/references/pi-tools.md
- https://github.com/obra/superpowers/issues/2372

### BMAD
- https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md
- https://github.com/bmad-code-org/bmad-loop
- https://github.com/bmad-code-org/bmad-loop/blob/main/docs/setup-guide.md
- https://github.com/bmad-code-org/bmad-loop/blob/main/docs/FEATURES.md

### Get Shit Done
- https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md

### OpenSpec
- https://github.com/Fission-AI/OpenSpec/blob/main/README.md

### Kiro
- https://kiro.dev/docs/specs/
- https://kiro.dev/docs/hooks/
- https://kiro.dev/docs/

### Microsoft Agent Framework / AutoGen
- https://learn.microsoft.com/en-us/agent-framework/workflows/
- https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints
- https://learn.microsoft.com/en-us/azure/durable-task/sdks/durable-agents-microsoft-agent-framework
- https://github.com/microsoft/agent-framework/releases
- https://github.com/microsoft/autogen/blob/main/README.md

### LangGraph
- https://github.com/langchain-ai/langgraph/blob/main/libs/checkpoint/README.md
- https://github.com/langchain-ai/langgraph/releases
- https://github.com/langchain-ai/langgraph/issues/8234

### CrewAI
- https://docs.crewai.com/en/concepts/flows
- https://docs.crewai.com/en/learn/hierarchical-process

### OpenHands
- https://github.com/OpenHands/software-agent-sdk
- https://github.com/OpenHands/software-agent-sdk/releases

### Claude Code
- https://code.claude.com/docs/id/features-overview
- https://claude.com/blog/projects-redesigned

### OpenAI Codex / Agents
- https://developers.openai.com/api/docs/guides/agents-api/overview
- https://developers.openai.com/api/docs/guides/agents-api/multi-agent
- https://developers.openai.com/api/docs/guides/responses-multi-agent

### GitHub Copilot Agents
- https://docs.github.com/en/copilot/responsible-use/agents
- https://docs.github.com/en/copilot/concepts/agents/code-review

### Devin
- https://docs.devin.ai/

### MetaGPT
- https://github.com/FoundationAgents/MetaGPT/blob/main/README.md

### SWE-agent
- https://github.com/SWE-agent/SWE-agent/blob/main/docs/index.md

### OpenAI Symphony
- https://github.com/openai/symphony/blob/main/README.md
- https://github.com/openai/symphony/blob/main/SPEC.md
- https://openai.com/index/open-source-codex-orchestration-symphony/
