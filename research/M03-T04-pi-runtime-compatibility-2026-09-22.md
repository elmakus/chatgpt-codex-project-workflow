# Research — Pi runtime/harness compatibility for Project Workflow V2 before continuing M03

Date: `2026-09-22`
Research question: Determine, from current Pi upstream/docs/source plus proportional tracker/community evidence, whether Project Workflow V2 can keep M03 semantics runtime-neutral while adding Pi as a compatibility/runtime candidate, and what minimal Pi-side capabilities/package/extension layer are actually needed.

Research ID: `PWV2-M03-PI-R1`
Status: `complete`
Origin role: `execution_resolution`
Origin subject: `M03-T04@implementation/workstreams/feature-common-preexecution-core/cards/M03-T04.md`
Return target: `execution_resolution:M03-T04@implementation/workstreams/feature-common-preexecution-core/cards/M03-T04.md`
Return reconciliation: `pending`
Return reconciliation result: `none`

## Scope and authority boundary

This is bounded implementation/recovery Research opened after durable readback showed M03 already active: M03-T01..T03 were complete and M03-T04 was in progress. The Research therefore does **not** pretend to have happened before M03 began.

The user explicitly has **not** decided that Pi replaces Codex as the official V2 runtime. Existing Codex delivery/bootstrap/acceptance authority remains in force. This Research may establish Pi as a compatibility/runtime candidate only; it does not by itself amend Definition, ADR-PWV2-002, M05 delivery or M07 ChatGPT/Codex live acceptance.

## Source strategy and weighting

Primary/upstream evidence:
- Pi documentation: https://pi.dev/docs/latest
- Quickstart / usage / providers / models:
  - https://pi.dev/docs/latest/quickstart
  - https://pi.dev/docs/latest/usage
  - https://pi.dev/docs/latest/providers
  - https://pi.dev/docs/latest/models
- Sessions / compaction:
  - https://pi.dev/docs/latest/sessions
  - https://pi.dev/docs/latest/compaction
  - https://pi.dev/docs/latest/session-format
- Extensions / Skills / Prompt Templates / Packages:
  - https://pi.dev/docs/latest/extensions
  - https://pi.dev/docs/latest/skills
  - https://pi.dev/docs/latest/prompt-templates
  - https://pi.dev/docs/latest/packages
  - https://pi.dev/docs/latest/settings
- RPC / SDK:
  - https://pi.dev/docs/latest/rpc
  - https://pi.dev/docs/latest/sdk
- Security: https://pi.dev/docs/latest/security
- Upstream repository: https://github.com/earendil-works/pi
- Official subagent example:
  - https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/subagent
  - https://github.com/earendil-works/pi/blob/main/packages/coding-agent/examples/extensions/subagent/README.md
  - https://github.com/earendil-works/pi/blob/main/packages/coding-agent/examples/extensions/subagent/index.ts

Upstream tracker evidence:
- embedded-host limitation in official subagent example: https://github.com/earendil-works/pi/issues/9872
- request for first-class child spawn API (rejected after triage): https://github.com/earendil-works/pi/issues/7808
- project-agent trust behavior in subagent example: https://github.com/earendil-works/pi/issues/8261
- core capability-policy proposal: https://github.com/earendil-works/pi/issues/9043
- request for built-in permission profiles/package hashes: https://github.com/earendil-works/pi/issues/8802
- custom-tool confirmation / prompt-injection concern: https://github.com/earendil-works/pi/issues/9228
- global resource isolation concern: https://github.com/earendil-works/pi/issues/6517

Community/package prior art was treated as implementation evidence, not authority:
- https://pi.dev/packages/%40agwab/pi-subagent
- https://pi.dev/packages/%40pi-plugins/subagent
- https://pi.dev/packages/pi-subagents
- https://pi.dev/packages/%40tintinweb/pi-subagents
- https://pi.dev/packages/pi-web-access
- https://pi.dev/packages/pi-permission-modes
- https://pi.dev/packages/pi-sandbox
- Reddit discussions on Pi subagents / minimal extension setups were used only as anecdotal evidence that experienced users often prefer small auditable local extensions over large plugin stacks.

No source conflict affects the central conclusion. Package-catalog snapshots can lag on exact package versions/download counts; therefore those volatile numbers are not authority and are omitted from the compatibility decision.

## 1. Current Pi coding-harness behavior

### Installation and updating

Verified current installation paths:
- npm: `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`;
- Linux/macOS installer: `curl -fsSL https://pi.dev/install.sh | sh`.

Pi has a package-aware update surface:
- `pi update` updates Pi;
- `pi update --extensions` reconciles configured Pi packages;
- `pi update <source>` updates one package;
- `pi update --models` refreshes model catalogs;
- `pi update --all` combines supported update classes.

Pi Packages install from npm, git/URL or local path. Versioned npm specs and git tag/commit refs are pinnable. Personal package declarations live in global settings; `--local` writes the declaration into project-local `.pi/settings.json` and loads it only after project trust.

### Providers, models and model switching

Pi natively supports multiple subscription/OAuth and API-key providers, including ChatGPT/Codex, Claude, GitHub Copilot, xAI, Muse, OpenRouter and others. Custom OpenAI-compatible/local providers can be described in `models.json`; custom API/OAuth behavior can be implemented as an extension provider.

Model selection is runtime-native:
- interactive `/model` / Ctrl+L;
- scoped model cycling;
- CLI `--provider`, `--model`, `--thinking`, `--models`;
- extension/SDK access to the active model, provider registry and thinking level.

Model/thinking changes are recorded in Pi session history and restored when a Pi session resumes. They therefore belong naturally to **runtime state**, not Project Workflow canonical state.

### Sessions, resume, fork and compaction

Pi sessions are persistent JSONL trees by default. Native controls include:
- `pi -c` / `--continue`;
- `pi -r` / `--resume`;
- `--session <path|id>`;
- `--fork <path|id>`;
- `/tree`, `/fork`, `/clone`, `/new`;
- `--no-session` for ephemeral runs.

Compaction is native and persists structured summaries while retaining the underlying session history. Automatic compaction and `/compact` are runtime context-management mechanisms. A Project Workflow continuation must still recover exact authority/state from the repository rather than treating a Pi session summary as project truth.

### Interactive, print/JSON, RPC and SDK

Pi exposes four useful control surfaces:
- normal interactive TUI;
- one-shot/print mode and structured JSON event mode;
- long-lived JSONL RPC over stdin/stdout;
- in-process TypeScript SDK using `createAgentSession()`.

RPC is suitable for language-independent/process-isolated hosts and future web/desktop frontends. The SDK is suitable for Node/Bun hosts requiring direct typed access. Both use the same underlying session/agent mechanisms; neither needs to become Project Workflow semantics.

### Built-in tools

Pi's built-in tool set includes `read`, `bash` (and `powershell` on Windows), `edit`, `write`, `grep`, `find`, and `ls`; the default core set is read/bash/edit/write.

Important limitation: these tools execute with the permissions of the Pi process. Pi intentionally does not provide a built-in OS sandbox or comprehensive per-call approval policy.

## 2. Official extension/resource model

### TypeScript Extensions

Extensions are in-process TypeScript/JavaScript modules. They can:
- register model-callable tools;
- register slash commands, shortcuts and CLI flags;
- intercept/transform/block lifecycle events and tool calls;
- modify prompt/tool activation;
- register model providers;
- render TUI status/widgets/components;
- persist Pi-session metadata via `appendEntry()`;
- react to session start/shutdown, model selection, compaction, context, tool and agent lifecycle.

Pi uses `jiti`, so local TypeScript extensions do not require a separate compile step.

Global auto-discovery: `~/.pi/agent/extensions/`.
Project-local auto-discovery: `.pi/extensions/`, after project trust.
Explicit paths and package-managed resources are also supported.

### Skills

Pi implements Agent Skills. A Skill has `SKILL.md` plus optional scripts/references/assets. At startup the agent sees only compact Skill metadata; full instructions are read on demand. This is a direct native fit for PWV2 progressive disclosure.

Skills may be global, project-local or package-distributed. They are instructions/capability resources, not a suitable canonical state store.

### Prompt Templates

Markdown prompt templates become slash commands. They are useful for explicit operator conveniences but contain no executable lifecycle behavior and should not duplicate workflow semantics.

### Pi Packages

A Pi Package may bundle extensions, skills, prompts and themes in one npm/git/local distribution. A `package.json` `pi` manifest can explicitly enumerate resources.

Packages are installable globally or project-locally and can be pinned. They are therefore the natural distribution unit for a future thin `pw for Pi`.

### Persistence/recovery

Pi extension state can be stored in branch-following tool-result details, extension entries in the session, custom messages, or external storage. For PWV2, none of these should become the semantic state owner. Project Workflow durable recovery remains repository/Task-Board/workstream based.

## 3/4. Capability map for PWV2 on Pi

| PWV2 capability | Classification | Evidence-based realization |
|---|---|---|
| Thin Project Workflow bootstrap | **Native Pi + thin own package resource** | A small Skill or command can locate/read canonical `workflow/`; no second semantic copy. |
| Progressive disclosure of workflow modules | **Native Pi** | Skills are metadata-first/on-demand; read tools and a small router can load exact modules/refs. |
| Durable recovery in a new Pi session | **Native Pi + PW repo semantics** | Pi sessions resume natively, but authoritative recovery is still the project repo. No Pi-specific PW state needed. |
| One semantic state owner | **PWV2, not Pi extension state** | Main/coordinator remains sole Task Board/manifest reconciler. Child runtime state is non-canonical. |
| Delegated implementation/subagents | **Official example proves capability; likely own small audited extension for PWV2** | Upstream example spawns isolated Pi subprocesses; see section 5. |
| Fresh independent reviewer/context | **Native session/process primitives + small delegation layer** | Separate Pi process/session can receive exact immutable review subject without parent conversational history. |
| Different providers/models for Main/worker/reviewer | **Native Pi** | CLI/model runtime supports exact provider/model selection; upstream subagent definitions support model override/inheritance. Keep choice outside PW state. |
| Sequential/parallel workers inside one Card | **Official example / small extension** | Upstream subagent example supports single, chain and bounded parallel children. PW still exposes one active Card. |
| Git operations | **Native Pi shell + external git CLI** | `bash` can invoke `git`; no PW-specific extension required. |
| GitHub PR/Issue operations + readback | **External `gh`/purpose-built tool; not PW semantics** | Use `gh` through shell when installed/authenticated or a separately audited tool. Preserve write→readback→verify semantics in PW. |
| Research/web access | **Not core; separate optional audited tool/package** | Pi core intentionally stays minimal. `pi-web-access` is capable but broad; do not bundle it into `pw` by default. |
| MCP | **Not required for PWV2** | Pi intentionally does not put MCP in core. Use a direct extension/CLI/SDK for a concrete service; add an MCP adapter only when a real integration requires it. |
| User permission/safety gates | **Official examples for soft gates; OS isolation for real boundary** | `tool_call` interception, permission-gate/protected-path examples; project trust gates project resources. These are not an OS sandbox. |
| Sandbox for unattended/untrusted work | **Outside PW semantics; OS/container or audited sandbox extension** | Pi upstream explicitly recommends container/VM/micro-VM/policy sandbox for real isolation. |
| Compaction/handoff | **Native Pi + PW durable recovery** | Pi compaction/tree summaries manage runtime context; PW restart reads repo state and exact refs. |
| Future web UI | **Native RPC/SDK** | Keep UI/process hosting outside canonical workflow; Pi RPC/SDK already expose suitable integration surfaces. |
| Runtime telemetry/model/session IDs in PW state | **Unnecessary / prohibited** | Existing PWV2 REQ-004/006/037 explicitly keeps these non-canonical. |

## 5. Subagent/delegation layer

### Upstream official example

Pi deliberately does not put subagents in core, but the repository ships a concrete extension example:
- each delegated task runs in a separate Pi process and isolated context;
- child invocation uses JSON/headless mode;
- agent definitions can choose tools and model, or inherit parent model/thinking;
- single, sequential chain and bounded parallel modes exist;
- parent receives structured streamed/final results;
- project-local agents are intentionally trust-sensitive.

This proves that PWV2's needed topology is natural on Pi without adding subagent semantics to PW state.

It is still an **example**, not a stable first-class child-agent API. Upstream issue #9872 shows that its child-invocation heuristic can misbehave when Pi is embedded under another host/web process. Issue #7808 proposed a first-class child-spawn API because SDK-based in-process setup is currently more verbose/subtle; that proposal was rejected after triage. Therefore copying the example wholesale as a long-term production dependency would be too optimistic.

### Third-party implementations

#### `@agwab/pi-subagent`

Strongest focused candidate found for a later audit/pilot:
- one focused `subagent` tool;
- parallel fan-out;
- sandbox/worktree controls;
- durable artifacts and async status;
- intentionally scoped smaller than full orchestration suites.

Tradeoffs: non-trivial trusted code/dependencies and POSIX assumptions; native Windows is not supported. It should be source-audited before installation.

#### `@pi-plugins/subagent`

Very small conceptual surface:
- fresh headless Pi session;
- prompt/model/cwd override;
- separate child sessions inspectable later;
- zero ordinary package dependencies in the current catalog entry.

Tradeoff: it explicitly warns that children can edit the same files as Main; it does not by itself solve mutating parallel-worker worktree isolation.

#### `pi-subagents` and `@tintinweb/pi-subagents`

Feature-rich and widely used: background jobs, multiple agent types, steering, workflows, UI/fleet concepts and broader orchestration.

For PWV2 **today**, these are larger than the current requirement. They create a bigger trusted code/configuration surface and introduce runtime concepts PWV2 deliberately does not need to persist. Community discussion also shows a recurring preference for locally audited minimal extensions when simple delegation is enough.

### Subagent decision for PWV2

**Preferred direction: write/own a small auditable Pi orchestration extension, based on upstream-supported primitives and the official example, rather than adopting a large orchestration framework or moving Project Workflow orchestration into RPC/SDK now.**

Minimum behavior:
1. spawn a fresh isolated Pi child for one bounded role/task;
2. explicit model/provider override with inheritance as fallback;
3. explicit tool allowlist, with reviewer/scout read-only by default;
4. bounded sequential and parallel fan-out inside the single active PW Card;
5. cancellation and structured result/evidence return;
6. Main remains the only writer of Task Board/manifest/PW state;
7. no scheduler, durable worker registry, model/session IDs or runtime topology in PW state;
8. mutating parallel workers require isolated Git worktrees/working copies;
9. project-local agent definitions are disabled by default unless trusted/explicitly enabled;
10. no assumption that child process/session survival is the PW recovery mechanism.

Start with subprocess/headless Pi because the official example proves the path and it is simple to audit. Do **not** create a general orchestration framework. If future web/RPC embedding makes subprocess invocation awkward, the Pi-side implementation can later move to SDK/RPC while preserving the same Project Workflow semantics. That future host change is not a reason to add an adapter abstraction to PWV2 now.

## 6. `pw for Pi` Pi Package

Creating a Pi Package is worthwhile **as a delivery/bootstrap compatibility surface**, not as another workflow implementation.

Recommended minimal shape:

```text
pw-for-pi/
├── package.json
├── skills/
│   └── project-workflow-v2/
│       └── SKILL.md             # thin entry/bootstrap only
├── extensions/
│   └── pw-runtime.ts            # small optional lifecycle/delegation adapter
└── workflow/                    # exact packaged bytes from canonical V2 workflow/
```

Rules:
- canonical source remains the V2 repository `workflow/`;
- package build/release copies/packages those exact files, just as the accepted Codex plugin packages the same canonical workflow;
- the Skill/bootstrap only locates the package root/router and initiates exact durable recovery; it does not restate stage semantics;
- the extension, if present, owns only Pi runtime behavior: loading/recovery assistance, delegation primitives and optional soft safety hooks;
- Pi session metadata may record UX/runtime details, but never becomes Project Workflow state;
- GitHub/web/sandbox/MCP packages remain separate optional runtime dependencies rather than being transitively bundled into `pw`.

This is analogous to the accepted Codex plugin principle ("thin bootstrap + same canonical workflow"), but the Pi package should use Pi-native package/Skill/extension mechanisms rather than copy Codex SessionStart/plugin structure 1:1.

## 7. Security assessment

Pi's security model materially affects package choice:

- extensions execute arbitrary code with the same OS permissions as Pi;
- packages may install runtime dependencies and Skills may instruct the agent to execute code;
- project trust controls whether project resources load; it is explicitly **not a sandbox**;
- built-in tools can read/write/run commands with process permissions;
- prompt injection from repository/tool/web content remains an expected local-agent risk.

Therefore:
- do not install a broad stack of third-party packages merely because the catalog exists;
- prefer own small extension or a narrowly scoped package whose source and dependency tree are audited;
- pin npm versions or git commits/tags for qualification;
- keep web, MCP and sandbox integrations separate so they can be audited/enabled only when needed;
- for untrusted/unattended work, use actual OS/container/VM isolation and minimum credentials;
- a regex permission-gate extension is a useful guardrail, not a security boundary;
- review-oriented subagents should have read-only tools by construction when possible;
- mutating child agents should not share one mutable checkout concurrently.

Upstream issues #9043/#8802/#9228 independently reinforce that richer capability/permission policy is an ecosystem concern rather than a currently complete core boundary.

## 8. Impact on current PWV2 authority and M03

### M03 may remain completely runtime-neutral

The accepted authority already says:
- PWV2-REQ-004: runtime/product/model/session/worker identity is not canonical PW state;
- PWV2-REQ-006: PW owns semantic lifecycle/state; runtime owns concrete worker/session/model topology and orchestration;
- PWV2-REQ-022..027: one PW Card at a time, but runtime may use zero/one/many subagents, and a runtime lacking delegation may execute directly;
- PWV2-REQ-035/037: reviewer independence is semantic; concrete runtime identity remains non-canonical;
- ADR-PWV2-004 explicitly moves implementation topology to the runtime;
- PWV2-P1 M03 JIT explicitly says not to add a runtime role catalog, model preference, worker-adapter API or persisted invocation schema.

Pi fits this authority. Nothing in the Pi evidence forces M03 semantic changes.

### No Definition or Strategic Plan change is required now

The evidence creates no contradiction with current Definition/Plan. M03-T01..T03 do not need to be reopened. M03-T04 can continue after Research reconciliation.

Existing Codex-specific delivery authority remains valid and intentionally untouched:
- PWV2-REQ-007..012 / ADR-PWV2-002 still define ChatGPT + Codex delivery;
- M05 still requires the accepted Codex `pw:project_workflow_v2` packaging/update path;
- M07 still requires the accepted ChatGPT↔Codex portability/live topology tests.

Pi is currently a **new compatibility/runtime candidate**, not a replacement or newly accepted official delivery product.

If the user later explicitly chooses to make Pi an officially supported third runtime, or to replace Codex, that would be a real Definition-level product/delivery decision because the accepted target explicitly names ChatGPT/Codex delivery and associated M05/M07 acceptance. That future choice must not be inferred from this Research.

### Later Pi live acceptance when installation is ready

A Pi compatibility qualification should prove, without replacing existing Codex tests:
1. install + provider authentication/model selection on the actual host;
2. `pw for Pi` package install/update and exact packaged canonical `workflow/` byte/source readback;
3. thin bootstrap enters exact router without preloading/repeating semantics;
4. fresh Pi session recovers the same workstream/Task Board obligation from durable repo only;
5. resume/fork/compaction does not alter semantic recovery;
6. model/provider changes for Main/worker/reviewer do not enter PW state;
7. one Main delegates a bounded worker result and alone reconciles shared state;
8. sequential and parallel child execution remains inside one PW Card; mutating parallel workers are checkout-isolated;
9. exact fresh/independent reviewer context can issue RED/GREEN under the existing semantic-independence contract;
10. worker/session loss after a durable result does not cause replay;
11. git/GitHub write→readback→verify works through the chosen runtime tools;
12. Research/web capability works through the explicitly selected audited runtime integration;
13. project trust + package pinning + sandbox/permission realization behaves fail-closed for the intended deployment;
14. the same semantic run is controllable through ordinary Pi and, later, RPC/SDK/web host without changing PW durable state.

These should initially be recorded as Pi compatibility evidence, not retroactively substituted for existing L01-L09/Codex acceptance.

## Conclusion

Pi is technically a strong fit for PWV2 precisely because Pi keeps runtime composition extensible and PWV2 already keeps semantic workflow/state runtime-neutral.

The current evidence supports:
- **keep Codex as the currently accepted/qualified delivery target;**
- **treat Pi as a compatibility/runtime candidate;**
- **do not change Definition or Strategic Plan now;**
- **continue M03-T04 under existing authority;**
- build/test a thin `pw for Pi` package later, with canonical `workflow/` packaged directly and only a minimal Pi-specific bootstrap/delegation extension;
- prefer a small owned/audited orchestration extension over a broad third-party orchestration suite;
- keep web/MCP/GitHub/sandbox tooling modular and outside Project Workflow semantics.

This satisfies the Research question without creating a new runtime decision the user has not made.
