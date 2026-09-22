# Research — Pi as a Project Workflow V2 runtime/harness candidate before M03

Date: `2026-09-22`
Research question: `Using current upstream and practical evidence, determine Pi's actual harness/runtime capabilities and extension model, classify the smallest mechanisms needed to run Project Workflow V2 well on Pi, evaluate subagent/delegation and a minimal pw-for-Pi package, and decide whether the accepted PWV2 Definition/ADRs/M03 plan can remain runtime-neutral without replanning while Codex stays the currently qualified runtime.`

## Durable continuation metadata — policy-activated only

Research ID: `PWV2-PI-R1`
Status: `consumed`
Origin role: `strategic_planning`
Origin subject: `PWV2-P1:M03-runtime-boundary-before-execution-prep`
Return target: `strategic_planning:PWV2-P1:M03-runtime-boundary-before-execution-prep`
Return reconciliation: `applied`
Return reconciliation result: `implementation/workstreams/feature-common-preexecution-core/evidence/M03-pi-preexecution-research-reconciliation-2026-09-22.md`

## Scope

Bounded pre-execution Research before any M03 Card/Execution Prep activation.

Investigated from current sources, prioritizing official/upstream Pi documentation and source, then upstream release/issues and proportionate third-party/community evidence:

1. Pi installation/update, providers/models/model switching, sessions/resume/fork/compaction, interactive/headless/JSON/RPC/SDK, and built-in tools/limits.
2. Official extension model: TypeScript Extensions, Skills, Prompt Templates, Pi Packages, global/project-local installation, lifecycle/event hooks, custom tools/commands/UI, persistence/recovery, npm/git distribution and updates.
3. Capability mapping for PWV2: bootstrap, progressive disclosure, durable recovery, sole semantic state owner, delegated implementation, independent fresh-context review, provider/model choice outside PW state, internal sequential/parallel workers, Git/GitHub/PR/Issue readback, Research/web, MCP/alternatives, permission/safety gates, compaction/handoff, and future web UI/RPC separation.
4. Subagent/delegation alternatives, minimal `pw for Pi`, third-party security, and impact on accepted PWV2 authority.

Explicit user constraint retained: researching Pi does **not** select Pi as the official V2 runtime, does not remove existing Codex delivery/acceptance, and does not authorize Definition/Strategic Plan edits unless evidence proves a real contradiction.

## Sources / evidence

### Primary / upstream

| Source | Class / weight | What it supports | Freshness / limitations |
|---|---|---|---|
| https://github.com/earendil-works/pi/releases/tag/v0.87.0 | official upstream / primary | Current Pi release, breaking changes, current session/extension boundary work | Released 2026-09-21; exact current release at Research time |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/README.md | official upstream / primary | Harness philosophy, install, models, tools, sessions, customization, modes | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/providers.md | official upstream / primary | OAuth/API-key providers, credentials, custom provider path | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/usage.md | official upstream / primary | Model/session commands, modes, package commands, project trust | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/sessions.md | official upstream / primary | Resume/fork/tree/clone persistence | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/compaction.md | official upstream / primary | Auto/manual compaction and branch summarization | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/extensions.md | official upstream / primary | TypeScript extension API, hooks, tools, commands, UI, state, tool interception | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/skills.md | official upstream / primary | Agent Skills, on-demand loading, global/project/package locations | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/prompt-templates.md | official upstream / primary | Prompt templates and locations | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/packages.md | official upstream / primary | Pi Packages, npm/git/local distribution, global/project scope, updates, package security | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/security.md | official upstream / primary | Process permissions, project trust, no built-in sandbox, containment guidance | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/json.md | official upstream / primary | JSON event stream mode | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/rpc.md | official upstream / primary | JSONL RPC over stdin/stdout for process/custom-UI integration | Version-pinned |
| https://github.com/earendil-works/pi/blob/v0.87.0/packages/coding-agent/docs/sdk.md | official upstream / primary | `AgentSession`, runtime/session replacement, programmatic model/tool control | Version-pinned |
| https://github.com/earendil-works/pi/tree/v0.87.0/packages/coding-agent/examples/extensions/subagent | official upstream example / strong prior art | Isolated child Pi processes, single/parallel/chain delegation, per-agent model/tools, abort/streaming | Explicitly example code, not a core supported subagent facility |

### Tracker/release evidence

- v0.87.0 contains breaking changes to `SessionManager`, extension event unions and context boundaries. This is evidence that a Pi-specific extension should pin/test against supported Pi versions rather than assume extension ABI/API stability indefinitely.
- v0.87.0 fixes extension/context issues linked to upstream issues #9789/#9822, showing extension-driven context editing is powerful but has real edge cases; PW durable state should therefore remain repo-owned rather than session-context-owned.

### Third-party subagent prior art

| Implementation | Weight | Useful evidence | Limitation for PWV2 default |
|---|---|---|---|
| https://pi.dev/packages/@pi-plugins/subagent | third-party, small/auditable candidate | Fresh headless Pi session, model override, cwd, separate subagent sessions; 0 runtime deps in catalog | Very small surface; shared filesystem, no documented parallel/worktree isolation; third-party process code |
| https://github.com/AgwaB/pi-subagent | third-party, focused candidate | Parallel fan-out, optional worktree/sandbox, durable artifacts/status, explicit authority ceilings | More machinery and native/platform constraints; own run/artifact lifecycle can overlap PW recovery if treated as semantic state |
| https://github.com/nicobailon/pi-subagents | third-party, mature/broad prior art | Native child AgentSessions/background runners, parallel agents, model/provider selection, worktrees, rich observability | Large orchestration/control plane with its own workflows/background state; excessive as a default PWV2 dependency unless a concrete need emerges |
| https://pi.dev/packages | package ecosystem / discovery only | Confirms many alternative subagent/MCP/web packages exist | Existence/download count is not trust or correctness evidence |

### Practitioner/community evidence

A current r/PiCodingAgent practitioner example uses Pi with specialized subagents, external model routing and MCP/web-search components and reports that orchestration configuration, model resolution, timeouts and subagent visibility require tuning. This is anecdotal supporting evidence only: it confirms composability and practical failure modes, not canonical behavior.

## Verified findings

### 1. Pi today as a coding harness

At Research time the canonical upstream is `earendil-works/pi`; current release is `v0.87.0` (2026-09-21), and the coding-agent package is `@earendil-works/pi-coding-agent`.

**Install / update**
- Official npm install: `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`; official installer script is also available.
- Pi itself does not require npm lifecycle scripts for normal install.
- Package management is first-class: `pi install`, `pi remove`, `pi list`, `pi update`, `pi update --all`, `--extensions`, `--models`, `--self`.
- npm packages can be version-pinned; git packages can be pinned to tag/commit. Global and project-local installs are distinct.

**Providers / models**
- Subscription/OAuth providers currently include ChatGPT Plus/Pro (Codex), Claude Pro/Max, GitHub Copilot, xAI, Meta Muse, OpenRouter and Radius; many API-key providers are built in.
- `/model`, Ctrl+L and scoped-model cycling switch models; CLI/RPC/SDK can select provider/model/thinking explicitly.
- `models.json` and custom-provider extensions cover local/proxy/custom providers.
- Concrete model/provider choice is naturally runtime/session configuration; Pi does not require that identity to become project semantic state.

**Sessions / recovery / compaction**
- Sessions are JSONL trees under `~/.pi/agent/sessions/`, organized by cwd.
- Native resume/new/tree/fork/clone/import/export are available. Tree navigation branches inside one session; fork/clone produce separate session files.
- Auto/manual compaction is native and append-only history remains available; branch summarization exists.
- v0.87.0 further separates raw history from projected model context via canonical context edits.
- Pi session durability is useful runtime continuity, but it is not a substitute for PW repository durability.

**Modes**
- Interactive TUI.
- Print/headless.
- JSON event stream.
- RPC over strict JSONL stdin/stdout.
- TypeScript SDK with `AgentSession` / `AgentSessionRuntime`.
These provide a clean future path to web/desktop/mobile presentation without changing workflow semantics.

**Built-in tools**
- Default model tools are `read`, `write`, `edit`, `bash` (PowerShell on Windows); `grep`, `find`, `ls` are available as read-only built-ins but not necessarily in the default allowlist.
- Tool allowlists/exclusions and no-tool modes are configurable.
- There is no core semantic GitHub, browser/web-search or MCP requirement/tool. `bash` can invoke `git`, `gh`, curl/tooling when installed; extensions can add purpose-built tools.

### 2. Official Pi extension/resource model

**TypeScript Extensions**
- Auto-discovered globally from `~/.pi/agent/extensions/` and project-locally from `.pi/extensions/` after project trust.
- Can register tools, commands, shortcuts, flags, custom TUI, providers, intercept/block/modify tool calls, modify context/system transcript, customize compaction and append session entries.
- Useful lifecycle hooks include `project_trust`, `session_start` (startup/reload/new/resume/fork), before-switch/fork/shutdown, compaction/tree hooks, `model_select`, thinking-level selection, agent/turn lifecycle, `context`, `context_with_system`, `tool_call`/tool-result hooks.
- Extension state may be stored/reconstructed through session entries, but PW semantic state should not be moved there.

**Skills**
- Pi implements the Agent Skills standard.
- Skills load descriptions initially and full instructions on demand, making them a strong native progressive-disclosure primitive.
- Global/project/package locations are supported; direct `/skill:name` invocation exists.

**Prompt Templates**
- Markdown snippets with slash-command expansion; global/project/package/CLI locations.
- Appropriate for convenience entry prompts, not for owning semantic workflow.

**Pi Packages**
- Bundle extensions, skills, prompts and themes; distribution through npm, git or local paths.
- Global install is default; `-l` writes project-local package settings. Trusted project settings can auto-install missing project packages.
- npm/git pins support reproducibility. Package manifests can filter/enable exact resources.
- Package install resolves runtime dependencies with npm; that is part of the supply-chain attack surface.

### 3. PWV2 capability classification on Pi

| PWV2 capability | Classification | Minimal realization |
|---|---|---|
| Bootstrap Project Workflow | **official/native resource primitives sufficient** | Thin Agent Skill (optionally one convenience prompt) that locates the canonical packaged/project `workflow/` router; no semantic copy in the Skill |
| Progressive disclosure | **native Pi** | Skill on-demand loading + exact file reads; do not preload the workflow tree into AGENTS/SYSTEM |
| Durable recovery after new session | **PW-owned / native Pi assists** | Repository Task Board/manifest remains truth; `session_start` may only rediscover/re-enter it; Pi resume/fork is convenience |
| One semantic state owner | **must remain outside runtime orchestration** | Main alone reconciles/writes PW state; workers never own Task Board/manifest |
| Delegated implementation/subagents | **own small extension recommended for qualification** | Small audited extension derived from upstream example; generic isolated child contexts, bounded tools/model/cwd, normalized result |
| Independent reviewer / fresh context | **same small extension + native sessions** | Spawn a separate clean child session/process that did not produce subject; otherwise use existing fresh-chat fallback |
| Different provider/model for Main/worker/reviewer | **native Pi/runtime config** | Explicit child session model/provider or inherited parent; never persist concrete identity in PW state |
| Sequential/parallel workers within one Card | **upstream example proves extension suffices** | Single/parallel/chain child execution; initially allow mutating parallelism only with explicit filesystem isolation |
| Git operations | **native shell/tooling** | `git` through bash; no PW-specific Git engine required |
| GitHub PR/Issue/readback | **native shell + external CLI sufficient when available** | `gh` via bash or later small purpose-built tool; preserve PW ACTION→READBACK→VERIFY→EVIDENCE semantics |
| Research/web access | **not core; optional audited Skill/extension/external tool** | Add only a vetted search/browser capability actually needed; no mandatory web package in `pw` |
| MCP | **not needed by PWV2 by default** | Treat MCP as optional runtime connectivity for a concrete integration lacking a simpler supported path |
| Permission/safety gates | **official extension hooks sufficient for UX gates; OS isolation for real boundary** | `tool_call` confirmation/path protection for accidental writes; container/VM/micro-VM/worktree/credential restriction for strong isolation |
| Context compaction/handoff | **native Pi + PW durable state** | Pi compaction/tree for runtime context; PW handoff/evidence remains repo-owned |
| Future web UI / remote control | **native RPC/SDK boundary** | Build/use separate presentation/client later; do not put web/RPC topology into PW semantic state |

### 4. Subagent/delegation decision

Pi deliberately does not ship subagents as a core feature, but the **official upstream subagent example already proves the necessary extension primitives**:
- separate child Pi process and isolated context;
- JSON structured streaming;
- per-agent tools and model, with inheritance when omitted;
- single, sequential chain and bounded parallel execution;
- abort propagation and usage/result collection;
- default user-level agent definitions and guarded project-local agent loading.

For PWV2, the best fit before any official Pi qualification is:

**Preferred target: a small PW-owned Pi orchestration extension, derived/audited against the official example, rather than adopting a large third-party multi-agent framework or making an external RPC service the default.**

Why:
1. M03 needs only child-context launch, authority/tool/model/cwd bounds, sequential/parallel fan-out, independent reviewer contexts, abort/result normalization and a valid return path.
2. The upstream example already demonstrates most of that with little code.
3. Large packages such as `pi-subagents` add background jobs/workflows/missions/observability/control state that risks becoming a second workflow/control plane.
4. Focused third-party packages are useful prior art/spikes but still execute privileged code and should not become a default dependency without audit.
5. An external RPC/SDK orchestrator is technically valid, but today would add another long-lived service/process boundary without a current semantic need. It becomes attractive later if the same runtime service must power web/mobile/remote clients.

**Important boundedness:** do not implement this Pi extension as part of M03 common semantics now. M03 should define/test the runtime-neutral delegation contract; the Pi runtime adapter/package should be a later compatibility/qualification slice once Pi is installed and the user chooses to pursue it.

For a future minimal adapter:
- one generic delegation tool is enough initially;
- child role/model/tool identity remains runtime config/telemetry, never PW state;
- a mutating implementation worker may use the normal workspace when serial;
- parallel mutating children require separate worktrees or stronger isolation; read-only parallel children can safely share a checkout;
- Main alone validates result/evidence and writes Task Board/manifest;
- reviewer child must be a fresh semantic context that did not produce/repair the reviewed exact subject;
- runtime child session/artifact identifiers may aid recovery but are noncanonical telemetry.

### 5. Minimal `pw for Pi` Pi Package

A Pi Package is worthwhile **if/when Pi is actually qualified as a supported PWV2 runtime**, because it gives the same desirable operational property as the Codex plugin: install/update one thin runtime package while keeping one canonical semantic tree.

Recommended minimum:
1. **Thin Skill** such as `project-workflow-v2`:
   - bootstrap only;
   - locate project identity and exact durable state;
   - enter the small canonical router;
   - rely on exact `workflow/` files rather than restating policy.
2. **Direct canonical workflow payload**:
   - package the same canonical `workflow/` content from `project_workflow_v2`;
   - it may be ordinary package files read by the Skill/extension; it does not need to masquerade as a Pi Skill per module.
3. **Optional small runtime extension**:
   - session-start recovery convenience;
   - generic delegated child contexts / independent reviewer contexts;
   - minimal tool/permission hooks only where they add concrete value;
   - no Project Workflow semantic state database and no copied router logic.
4. **Prompt template only if useful for UX**, not required if the Skill is already ergonomic.

Do **not** bundle a broad third-party extension suite, MCP server collection, web UI, scheduler or model router into the default `pw` package.

This mirrors the **principle** of the Codex plugin (thin runtime-specific bootstrap + direct canonical semantics), not its exact structure. Pi's native Skill/Extension/Package lifecycle is different; there is no reason to reproduce Codex SessionStart/plugin wiring 1:1.

### 6. Security assessment

- Pi runs with the permissions of the launching user.
- Project trust controls loading of project resources; **it is explicitly not a sandbox**.
- Extensions are arbitrary TypeScript with process/system privileges.
- Skills can instruct arbitrary actions and may ship executable helpers.
- Pi Package installation may run dependency installation; third-party dependency chains are part of the trust surface.
- A malicious extension cannot be made safe merely by a PW prompt or tool-confirmation hook.

Therefore:
- prefer zero or one small audited runtime extension over a package collection;
- pin versions/commits during qualification;
- inspect source and dependency lock/material before promotion;
- treat download counts/community popularity as discovery signals only;
- for unattended/untrusted workers use OS/container/VM/micro-VM boundaries, least credentials and restricted network;
- retain PW authorization/readback/evidence gates regardless of runtime sandboxing.

### 7. Practical community/tracker observations

The upstream release cadence and breaking extension/session changes show that Pi integration tests must be version-aware. Third-party orchestration projects have also needed fixes around model resolution/background execution, and practitioner setups report configuration/timeout/observability tuning. These are reasons to keep the adapter narrow and acceptance-tested, not reasons to move runtime metadata into PW state.

No credible evidence was found that PWV2 needs a runtime-level scheduler/control database, permanent MCP dependency or a second semantic state owner to work on Pi.

## Repository/current-state findings

At Research start and completion:
- M02 is durably complete and integrated.
- No M03 Card or Execution Prep state existed when this Research was opened.
- Accepted authority already separates Project Workflow semantics from concrete runtime worker/session/model topology:
  - PWV2-REQ-004 forbids runtime/model/session/worker identity as canonical PW state.
  - PWV2-REQ-006 assigns concrete worker/session/model topology and orchestration to the runtime.
  - PWV2-REQ-024 permits zero/one/many runtime subagents inside one Card.
  - PWV2-REQ-025 requires Main to delegate when a qualifying delegated context exists while retaining state/authority/reconciliation.
  - PWV2-REQ-027 permits direct execution when a runtime genuinely lacks delegation.
  - ADR-PWV2-004 says the same explicitly.
- PWV2-P1 M03 JIT explicitly forbids adding a runtime role catalog, model preference, worker-adapter API or persisted invocation schema to Project Workflow.
- ADR-PWV2-002 and PWV2-REQ-008..012 still make Codex the currently accepted/qualified plugin delivery surface. This Research does not supersede them.

## Assumptions / uncertainties

- Pi's extension API is active and fast-moving; v0.87.0 introduced breaking session/extension changes one day before this Research. Any future adapter needs a supported-version matrix or exact qualification pin.
- Core public auth documentation stores credentials by provider and does not establish a canonical multi-account-per-provider selection mechanism. Multi-account packages exist, but this is runtime convenience and not required to keep M03 semantic contracts correct.
- Pi does not currently supply a core browser/web-search or MCP client contract. Those capabilities depend on optional tools/skills/extensions/external programs.
- No Pi installation/live runtime was available in this workstream during Research, so this is source-level feasibility/architecture evidence, not Pi live acceptance.
- Third-party package behavior was not trusted solely from popularity; representative packages were used only as prior art and must be audited before installation.

## Alternatives

### A. Adopt a large existing subagent framework

Pros: rich functionality immediately, mature workflows, background jobs, observability.
Cons: much larger privileged dependency surface and overlapping orchestration/durable state; high risk of importing a second control plane.

**Not recommended as PWV2 default.** Keep as prior art or an optional operator choice.

### B. Adopt a focused existing subagent package

Pros: fast trial; some packages are deliberately small.
Cons: still third-party privileged code; either too little isolation for full PW needs or introduces its own run/artifact state.

**Good for an installation spike after audit, not the canonical PWV2 runtime contract.**

### C. Write a small PW-specific Pi extension from the upstream example

Pros: exact fit to M03 runtime boundary, minimal/auditable, preserves Main as sole state owner, easy to keep runtime identity noncanonical.
Cons: small maintenance burden against Pi API changes.

**Preferred compatibility implementation when Pi qualification begins.**

### D. External RPC/SDK orchestration layer

Pros: clean process/service boundary and natural future web/mobile/remote control surface.
Cons: adds another service/lifecycle/control surface before it is needed.

**Defer. Reconsider when remote/web hosting is a concrete requirement.**

## Analysis

Pi is unusually well aligned with PWV2's accepted runtime-neutral architecture because Pi itself treats orchestration as an extension concern. The key capabilities PWV2 needs before/around M03 — isolated child contexts, model/tool selection, lifecycle hooks, fresh sessions, parallel extension work, structured JSON/SDK integration and recovery hooks — are available without changing Project Workflow state schemas.

The important design consequence is **not** to make M03 Pi-aware. The current M03 contract is already the correct abstraction boundary: it describes what Main/worker/reviewer semantics must hold and explicitly refuses to prescribe runtime adapter/model/session schema. Pi can later realize that boundary through a thin package/extension; Codex can realize it through its current mechanisms.

The Pi research therefore strengthens the accepted architecture instead of contradicting it.

## Recommendation

1. **Keep PWV2 Definition, ADRs and PWV2-P1 M03 unchanged now.**
2. **Keep Codex as the currently accepted/qualified runtime/delivery surface.**
3. Treat Pi as a **compatibility/runtime candidate**, not a replacement decision.
4. Execute M03 as runtime-neutral common semantics exactly as planned.
5. Once the user's Pi installation is ready, open a bounded Pi compatibility/qualification slice:
   - first live-test native Pi + official example/minimal prototype;
   - then implement a small `pw for Pi` package only to the extent live evidence requires;
   - avoid a large third-party orchestration framework by default.
6. Defer external RPC/SDK orchestration and web UI integration until remote/web operation is a concrete requirement.

## Candidate Pi live acceptance tests after installation

These are compatibility candidates, not additions to current accepted L01-L09 yet:

1. Thin Pi bootstrap loads the same canonical `workflow/` bytes/semantics and fails closed when router/authority is missing.
2. Progressive disclosure loads only bootstrap/router/current module/exact state/authority rather than injecting the full workflow.
3. New session/resume/fork/compaction reconstructs PW continuation from repository durable state, not chat/session memory.
4. Main on one provider/model delegates an implementation worker on another provider/model without persisting either identity into PW state.
5. Worker cannot finalize shared Task Board/manifest; Main normalizes/validates/persists the result.
6. Two internal read-only/test workers may run concurrently while exactly one PW Card remains active; any concurrent mutating workers use isolated worktrees.
7. A separate clean reviewer context that did not produce the subject reviews the exact immutable subject; self-review is rejected/falls back to the existing fresh-context boundary.
8. Parent/runtime restart after a completed worker result reconciles durable result/evidence without replay.
9. GitHub Issue/PR write uses `gh` or selected tool with PW write→readback→verify→evidence and ambiguous-effect no-retry behavior.
10. Permission/path gates work for interactive UX; strong isolation test uses container/VM/worktree boundary and restricted credentials.
11. Selected web/Research capability returns source-grounded evidence; optional MCP absence does not break ordinary PW routing.
12. Interactive and RPC/SDK entry produce the same semantic route/state decisions.
13. Pi Package version/update test proves canonical workflow update propagation without duplicate semantic copies and handles a pinned/stale package deterministically.
14. Only if later Definition explicitly promotes Pi to supported/official runtime: add cross-runtime continuity acceptance involving Pi alongside the currently required ChatGPT/Codex path.

## Project Definition candidates

None requiring promotion now.

Potential future Definition change **only after explicit user authority**:
- add Pi to the set of officially supported/qualified runtime delivery surfaces;
- define any additional Pi-specific bootstrap/package acceptance obligations;
- expand cross-runtime acceptance beyond currently required ChatGPT/Codex continuity.

Until that decision exists, Pi remains compatibility evidence and a future qualification candidate, while existing Codex delivery/acceptance authority remains intact.
