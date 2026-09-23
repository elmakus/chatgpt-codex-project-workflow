# M07-T03 — full ordinary model-backed Codex L04 qualification

Date: 2026-09-23
Verdict: GREEN
Candidate: `elmakus/project_workflow_v2@15978113e46abc8498ceaef594461c8613fcadb8`

## Runtime and provider

Real runtime:
- Codex CLI `0.155.0-alpha.9.2`;
- custom provider id `codex-lb`;
- provider endpoint: existing `codex-lb-clean` API through Tower host gateway;
- model: `gpt-6-sol`;
- reasoning effort: `low`.

The custom provider used Codex's supported user-level provider contract (`base_url`, `env_key`, `wire_api = "responses"`). The API key was read only inside the disposable process environment and was not written to evidence or printed.

## Exact candidate package

Disposable `CODEX_HOME=/tmp/pwv2-m07-l04-home`.

Supported marketplace installation was pinned to the immutable candidate:
- marketplace source: `elmakus/project_workflow_v2`;
- marketplace Git HEAD: `15978113e46abc8498ceaef594461c8613fcadb8`;
- installed plugin: `pw@project-workflow-v2 0.2.1`;
- installed root: `/tmp/pwv2-m07-l04-home/plugins/cache/project-workflow-v2/pw/0.2.1`;
- installed router SHA-256: `29a5f65a1e8f83d158f4c3a18a6ffcd62ab7dc46a39251d041e22ae6e79cb1fc`;
- installed Skill SHA-256: `5a8ccfa19d8d2596eede309c1c3a30f662b6d5e1dd326b0c203ddffab67e19ee`.

Live/default Codex home remained without a `project-workflow-v2` installation.

## Disposable consumer

Consumer: fresh clone of `elmakus/test-pwv2@main`.
Exact HEAD: `a31047259c92a7c6a6054a1b9bf618fc0f6ac69a`.

The invocation used `$pw:project_workflow_v2`, was ephemeral, and was instructed to recover the existing completed workstream without mutations or remote workflow-policy fallback.

The workstation kernel does not permit the CLI's unprivileged bubblewrap namespace. A first model-backed run therefore proved provider/model selection and correct fail-closed behavior but could not read the router. The qualifying rerun disabled the CLI sandbox only inside this disposable consumer. Pre/post `git status` were both clean and the prompt explicitly prohibited mutations. No production project or live plugin state was changed.

## Model-backed semantic continuation

Runtime banner on the qualifying run:
- model: `gpt-6-sol`;
- provider: `codex-lb`;
- reasoning effort: `low`;
- session: `01a0ce6f-4dae-7642-8322-30f25ca09279`.

Observed progressive semantic path:
1. exact bundled local `workflow/ROUTER.md`;
2. consumer `PROJECT.md`;
3. only workstream `user-setting-persistence-restart`;
4. exact `WORKSTREAM.toml`;
5. `TASK_BOARD.toml` revision 12;
6. bundled `workflow/CLOSE.md`;
7. exact review/result/Close handoff refs.

The production router helper was then executed from the exact installed package with the selected workstream and returned:

- disposition: `route`;
- obligation: `close`;
- owner module: `workflow/CLOSE.md`;
- reason: all current Cards are terminal;
- read set: bundled router + `PROJECT.md` + exact workstream manifest + tracker + Task Board.

The model continued through Close evidence and verified:
- merge result on `main`: `a31047259c92a7c6a6054a1b9bf618fc0f6ac69a`;
- reviewed application blob on target: `1f7118be9360cf8cac8e0f7c12cfb15c15e3d6d9`;
- M03-T01-R01 verdict GREEN;
- tracker binds Issue #2 and final PR #3;
- complete target-side workstream package exists;
- source branch is absent in the disposable clone's refs;
- consumer stayed clean.

The model's own `gh` binary had no GitHub authentication, so it conservatively reported `continue Close reconciliation` rather than claiming Issue closure. That is correct fail-closed behavior. L03 separately established the exact post-merge Issue #2 closure and dedup readback through the authorized GitHub surface.

## L04 verdict

GREEN.

The missing M07 L04 requirement is satisfied: an ordinary real model-backed Codex invocation using the exact M07 candidate followed the installed local V2 Skill/router progressively into the consumer's actual durable semantic state and produced the correct current obligation without V1 fallback, remote workflow-policy fetch, state conversion or mutation.

The earlier native-provider usage-capacity blocker remains preserved as historical evidence:
`implementation/workstreams/feature-common-preexecution-core/evidence/M07-T03-L04-model-backed-blocker-2026-09-23.md`.

This record does not claim L06-L09 or adoption.
