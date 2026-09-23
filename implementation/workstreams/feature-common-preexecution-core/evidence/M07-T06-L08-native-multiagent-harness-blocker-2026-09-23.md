# M07-T06 — L08 N-CAPABLE live topology harness blocker

Date: 2026-09-23
Status: BLOCKED
Candidate: `elmakus/project_workflow_v2@15978113e46abc8498ceaef594461c8613fcadb8`

## Required live oracle

L08 requires one actual capable top-level V2 invocation to preserve S1 `topology-n: BAD\n` with independent RED, delegate a bounded correction to S2 `topology-n: GOOD\n`, obtain independent GREEN on S2, and finalize the same Card without an artificial verdict-only stop.

A direct/no-capability simulation is not accepted.

## Runtime capability readback

Real Codex build:
- executable: `/opt/codex-desktop/resources/codex`;
- version: `0.155.0-alpha.9.2`.

Effective feature state in the exact isolated test `CODEX_HOME`:
- `multi_agent = true` (stable);
- `multi_agent_v2 = false`.

The installed Codex binary contains the native collaboration surface:
- `CollabAgentToolCall`;
- `spawnAgent`;
- `sendInput`;
- `closeAgent`;
- native subagent lifecycle hooks.

Therefore the runtime is not rejected as inherently no-capability.

All intended model-backed L08 calls are constrained to the user-authorized provider/model profile:
- provider: existing `codex-lb-clean` Responses API;
- model: `gpt-6-sol`;
- reasoning effort: `low`.

## Exact candidate and disposable fixture

Exact candidate installation in the disposable test home:
- marketplace Git HEAD: `15978113e46abc8498ceaef594461c8613fcadb8`;
- plugin: `pw@project-workflow-v2 0.2.1`;
- `multi_agent=true`.

A clean local V2 fixture was prepared with one active Card and exact S1 state:
- fixture branch: `feat/topology-n`;
- fixture entry HEAD: `4eeaf9b61446139ab4cd00d529631e39f20cef91`;
- S1 implementation commit: `e8989c8ab2439ce58760a22a5c03f7416c290101`;
- S1 `topology-n.txt` blob: `4f49a94bb5f910f83aa95c3cc1972374fca82c29`;
- exact S1 content: `topology-n: BAD\n`;
- frozen S1 semantic-result commit: `1f3fbad3d2571b44599b1c178406b2403e00c079`;
- frozen S1 result blob: `e6cffae653903b4e58aad684ec1f4f37b88ef0f8`;
- one pending independent review attempt `M01-T01-R01`;
- stable Card requires genuine native delegated correction, separate native independent review contexts, one-Card state ownership, exact S2 GOOD oracle, and same-invocation post-GREEN finalization.

The fixture itself was created cleanly and had no uncommitted changes before the attempted live invocation.

## Sandbox diagnosis

The normal `chatgpt-ce-workstation` container cannot run Codex's bubblewrap sandbox:
- as user `codex`: namespace creation denied;
- as root: namespace creation denied.

Host/container readback:
- host `user.max_user_namespaces = 513498`;
- workstation is not privileged and has no added capabilities;
- Docker default security profile prevents the nested namespace path needed by bwrap.

A disposable container from the same workstation image was tested without host/project mounts:
- `--security-opt seccomp=unconfined` alone: bwrap still denied;
- `--cap-add SYS_ADMIN --security-opt seccomp=unconfined`, without `--privileged`: `BWRAP_RC=0`.

A dedicated disposable L08 container was then prepared with:
- only `CAP_SYS_ADMIN`;
- unconfined seccomp;
- exact fixture mount;
- isolated test `CODEX_HOME`;
- exact candidate plugin;
- read-only mount of the existing codex-lb key;
- effective `multi_agent=true`.

This setup permits a real `workspace-write` Codex sandbox without changing the host or production workstation configuration.

## Blocking platform boundary

The final model-backed command was intentionally specified with:
- normal `codex exec`;
- `--sandbox workspace-write`;
- no `--dangerously-bypass-approvals-and-sandbox`;
- disposable container/workspace only;
- exact `gpt-6-sol` / low profile.

Before the Docker/Codex process started, the ChatGPT Remote Desktop execution layer rejected the request with its own safety block. Earlier attempts to run the topology fixture through non-interactive and interactive write-capable Codex sessions were likewise rejected before Codex execution.

This outer safety boundary must not be bypassed by hiding the same operation in another shell/script path.

## Verdict

L08 remains BLOCKED, not RED and not GREEN.

The blocker is `live_harness_write_execution_unavailable`: the underlying Codex runtime exposes native multi-agent capability and a sandbox-capable disposable container can be prepared, but the currently authorized Remote Desktop tool surface will not launch the required write-capable model session.

Per M07.P3, no direct execution, synthetic child, multiple top-level calls, or no-capability fixture may substitute for N-CAPABLE evidence.

L09 and production acceptance are not claimed while this active Card is blocked.
