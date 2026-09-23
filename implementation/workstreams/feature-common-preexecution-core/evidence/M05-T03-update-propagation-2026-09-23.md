# M05-T03 — Semantic package update propagation and readback evidence

Date: 2026-09-23
Card: `M05-T03`
Target: `elmakus/project_workflow_v2@feat/pwv2-m05-delivery`
Accepted implementation subject: `fbd208c1c26eef2a227ea90aced05fd8ac32a9a4`
Tree: `66a57d7abb53b87fde528352bba06e511cb5df1e`
Pre-update package subject: `b9e57e8ba385efc780a7d18fe6b370b278b9e73c`
PR: `elmakus/project_workflow_v2#5`

## JIT installer contract

Current official OpenAI plugin packaging guidance and the real installed Codex runtime were checked on 2026-09-23.

Real runtime:
- Codex CLI: `0.155.0-alpha.9.2`
- executable: `/opt/codex-desktop/resources/codex` inside the authorized `chatgpt-ce-workstation` container
- supported commands confirmed from runtime help:
  - `codex plugin marketplace add <source> --ref <ref>`
  - `codex plugin marketplace upgrade [marketplace]`
  - `codex plugin add PLUGIN@MARKETPLACE`

The propagation test used only disposable `CODEX_HOME=/tmp/pwv2-m05-t03-home`. The live Codex home was not used for installation/update.

## Baseline install

From target subject `b9e57e8ba385efc780a7d18fe6b370b278b9e73c`:
- marketplace `elmakus/project_workflow_v2 --ref feat/pwv2-m05-delivery` added as `project-workflow-v2`;
- `pw@project-workflow-v2` installed as version `0.2.0`;
- installed root: `/tmp/pwv2-m05-t03-home/plugins/cache/project-workflow-v2/pw/0.2.0`.

Baseline SHA-256:
- `workflow/ROUTER.md`: `3478278803ff6c81e74f5b27c1d30d95a3904377232c801f60defa4027ccc02b`
- `skills/project_workflow_v2/SKILL.md`: `5a8ccfa19d8d2596eede309c1c3a30f662b6d5e1dd326b0c203ddffab67e19ee`
- `hooks/session-start.py`: `8426d8a1f8eb8d8ccce3f4afabb80a3a7d2a1585ecff289ba3b66a8f4359366c`
- `.codex-plugin/plugin.json`: `655b19e00c9ec6d82ad68d8486d155291517948b79b974babbf340fcd43e0f39`

## Harmless canonical semantic probe update

The canonical router probe response changed from `PWV2_M01_ROUTER_SENTINEL_7C91` to `PWV2_M05_UPDATE_SENTINEL_92AF`.

Only delivery metadata needed for a new install identity was updated from package version `0.2.0` to `0.2.1`. Skill and SessionStart bytes were intentionally unchanged.

No project patch pin, updater daemon, remote-policy runtime fetch or alternate semantic tree was added.

## Supported update and fresh readback

In the same isolated home:
1. `codex plugin marketplace upgrade project-workflow-v2 --json` completed with no errors.
2. `codex plugin add pw@project-workflow-v2 --json` installed version `0.2.1`.
3. `codex plugin list` showed exactly one enabled source: `pw@project-workflow-v2 0.2.1` from the isolated `project-workflow-v2` marketplace.
4. Installed cache contained only version directory `0.2.1`.
5. Fresh installed router readback returned `Probe response: PWV2_M05_UPDATE_SENTINEL_92AF`.
6. Fresh SessionStart returned the exact bundled `0.2.1/workflow/ROUTER.md` path and local-router bootstrap context.
7. Fresh `codex debug prompt-input` resolved `pw:project_workflow_v2` from `r1/pw/0.2.1/skills/project_workflow_v2/SKILL.md`.

Updated SHA-256:
- `workflow/ROUTER.md`: `894efa9c664bf52977a9c82a5fe96d8d9a5f4402d4f05ade9413547e93df514f`
- `skills/project_workflow_v2/SKILL.md`: `5a8ccfa19d8d2596eede309c1c3a30f662b6d5e1dd326b0c203ddffab67e19ee` — unchanged
- `hooks/session-start.py`: `8426d8a1f8eb8d8ccce3f4afabb80a3a7d2a1585ecff289ba3b66a8f4359366c` — unchanged
- `.codex-plugin/plugin.json`: `9ec08599b349d1a7ae049e535fac16771c6b22d7d6be15ce5f5b108a57716aa7` — version metadata changed

## Control / isolation readback

After the isolated test, live Codex marketplace/plugin readback (with `CODEX_HOME` unset) found no `project-workflow-v2` marketplace and no `pw@project-workflow-v2` installation: `PWV2_LIVE_CONTROL_ABSENT`.

The disposable home emitted only the expected warning that PATH helper aliases are not created under `/tmp`; marketplace add/upgrade and plugin install all completed successfully.

No consumer project durable state, existing obligation or review subject was converted or mutated by the package update.

## Repository verification

Exact target `fbd208c1c26eef2a227ea90aced05fd8ac32a9a4`:
- GitHub Actions run `35814931203`: PASS.
- `sh scripts/test.sh`: PASS.
- Codex delivery suite: 9/9 PASS.
- State: 28/28 PASS.
- Router: 39/39 PASS.
- Execution: 4/4 PASS.
- Review: 1/1 PASS.
- Recovery: 2/2 PASS.
- Close/fork/ChatGPT/Codex combined: 42/42 PASS.
- Draft PR #5 read back open/mergeable with exact head `fbd208c1c26eef2a227ea90aced05fd8ac32a9a4`.

## Acceptance disposition

M05-T03: GREEN / DONE.

This is L05-ready propagation evidence. Real ChatGPT/Codex surface checkpoints and any live user-owned delivery actions remain M05-T04 scope.
