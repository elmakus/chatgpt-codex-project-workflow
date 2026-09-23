# M07-T03 — L04 ordinary model-backed Codex qualification blocker

Date: 2026-09-23
Status: BLOCKED
Candidate: `elmakus/project_workflow_v2@15978113e46abc8498ceaef594461c8613fcadb8`
Card: `M07-T03`

## Exact disposable setup

Authorized runtime: Tower `chatgpt-ce-workstation` container.

Real CLI:
- executable: `/opt/codex-desktop/resources/codex`;
- version: `codex-cli 0.155.0-alpha.9.2`.

Fresh isolated state:
- `CODEX_HOME=/tmp/pwv2-m07-l04-home`;
- disposable consumer: `/tmp/pwv2-m07-l04-consumer`;
- consumer source: `elmakus/test-pwv2@main`;
- consumer HEAD: `a31047259c92a7c6a6054a1b9bf618fc0f6ac69a`;
- consumer worktree stayed clean before and after the attempt.

The isolated home copied only the already-existing Codex authentication/configuration input from the prior disposable M05 home. No credential contents were read or recorded.

## Exact candidate package

The supported CLI marketplace operation was used with the immutable candidate SHA:

`codex plugin marketplace add elmakus/project_workflow_v2 --ref 15978113e46abc8498ceaef594461c8613fcadb8 --json`

Readback:
- marketplace: `project-workflow-v2`;
- marketplace Git HEAD: `15978113e46abc8498ceaef594461c8613fcadb8`;
- installed plugin: `pw@project-workflow-v2 0.2.1`;
- installed root: `/tmp/pwv2-m07-l04-home/plugins/cache/project-workflow-v2/pw/0.2.1`;
- installed `workflow/ROUTER.md` SHA-256: `29a5f65a1e8f83d158f4c3a18a6ffcd62ab7dc46a39251d041e22ae6e79cb1fc`;
- installed `skills/project_workflow_v2/SKILL.md` SHA-256: `5a8ccfa19d8d2596eede309c1c3a30f662b6d5e1dd326b0c203ddffab67e19ee`.

The live/default Codex home still contains no `project-workflow-v2` plugin path. Production installation state was not modified.

## Ordinary model-backed attempt

A normal model-backed `codex exec` was started in the disposable consumer with:
- exact `$pw:project_workflow_v2` entry;
- `--ephemeral`;
- `--sandbox read-only`;
- working directory set to the disposable `test-pwv2@main` clone;
- instructions to recover durable V2 state through bundled local authority and report the next semantic disposition without writes or remote workflow-policy fallback.

Runtime banner:
- model: `gpt-6-astra`;
- provider: `openai`;
- approval: `never`;
- sandbox: `read-only`;
- session: `01a0ce63-632c-75e2-afd8-1e3cc12837ff`.

The request reached the model-backed service but stopped before semantic execution with:

`You've hit your usage limit ... try again at Sep 26th, 2026 10:10 AM.`

The CLI exited with status 1 and produced no final model message. Therefore the missing M07 L04 semantic continuation is still not GREEN.

## Alternate-provider check

Before accepting the blocker, current workstation configuration was inspected only for non-secret provider-routing keys.

Observed live config:
- `model = "gpt-6-astra"`;
- no configured `model_provider` / custom provider block was present.

Tower also currently runs `codex-lb-clean`, but it is a separate container on Docker network `ibraproxy`, while `chatgpt-ce-workstation` is on `chatgpt-ce-workstation_default`. The workstation is not currently configured to use that container as its Codex model provider.

Creating a new provider/network/configuration path solely to make this acceptance test pass would change the runtime surface under test and is outside this Card. It is not treated as an existing supported fallback.

## Retained evidence and limitation

Unchanged-compatible M05 evidence still proves:
- exact Skill resolution;
- bundled local router authority;
- thin Skill/SessionStart package surface;
- missing-router fail-closed behavior;
- no V1 fallback;
- supported package update/readback.

This Card additionally proves that the exact M07 candidate can be installed by immutable SHA into a fresh isolated home and leaves the live installation untouched.

However the one missing requirement remains exactly what M07-T03 was created to prove: an ordinary model-backed semantic continuation. A package/install/debug result cannot substitute for it.

## Blocker

`runtime_usage_capacity`: the currently authenticated native Codex provider reports no remaining usable capacity until **2026-09-26 10:10** (product-reported local retry time).

M07-T03 must remain blocked and L04 non-GREEN until a qualifying model-backed run can complete. L06-L09 and first production acceptance are not claimed by this record.
