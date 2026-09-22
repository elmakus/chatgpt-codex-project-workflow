# M01-T02 — isolated pw / project_workflow_v2 feasibility evidence

Date: 2026-09-22
Card: `M01-T02`
Result: **GREEN**
Target: `elmakus/project_workflow_v2@feat/pwv2-m01-foundation`
Target result commit: `221e4e93c3df3fe006880f4ade5c250eb356c8e9`
Host: `codex-cli 0.155.0-alpha.9.2`

## Isolated installation and exact Skill discovery

The probe used disposable `CODEX_HOME=/tmp/pwv2-m01-t02-home` and local marketplace source `/tmp/pwv2-m01-t02-source`. Codex installed `pw@project-workflow-v2` version `0.1.0` into:

`/tmp/pwv2-m01-t02-home/plugins/cache/project-workflow-v2/pw/0.1.0`

With the exact input `$pw:project_workflow_v2 Return the router Probe response exactly.`, `codex debug prompt-input` exposed the namespaced Skill `pw:project_workflow_v2` from that installed cache. The disposable home intentionally contained no Codex credentials, so this feasibility probe did not reuse live authentication for a model-backed turn.

## Target ↔ installed-package identity

Git blob hashes from the installed cache exactly matched GitHub readback for the target commit:

- `.codex-plugin/plugin.json` — `23fa4fc94e0313aa9e95365d164e9328c0ddc67c`
- `.agents/plugins/marketplace.json` — `f290911db7866b34ae677b6707805abe5a05e0c6`
- `skills/project_workflow_v2/SKILL.md` — `2e460fec74f3712217d9c368965924f41fd96909`
- `hooks/hooks.json` — `d308931b657e9f082744f39e5cd5faba50ba5ef4`
- `hooks/session-start.py` — `cd029f769878ccfaf7d5407d022c8a2b718dedcc`
- `workflow/ROUTER.md` — `8bd62862a8ee9a6450b91fbd41b9237a754ef226`

The probe therefore exercised the target V2 package bytes rather than V1 or a stale alternate source.

## SessionStart and fail-closed behavior

Executing the installed SessionStart hook with its installed plugin root returned `PWV2_M01_SESSION_SENTINEL_4D2A` and the exact bundled `workflow/ROUTER.md` path.

Executing the same installed hook against a disposable root with no router returned a blocking package error and explicitly prohibited fallback to V1, runtime-specific policy, or reconstructed chat memory.

A final live-Codex readback found neither marketplace nor plugin `project-workflow-v2`, confirming the isolated probe did not replace/install into the live Codex home.

## Structural test boundary

The target result contains `scripts/test-plugin-probe.sh`, and `scripts/test.sh` invokes it when present. The checks cover the exact `pw` / `project_workflow_v2` package shape, hook/router sentinels, fail-closed marker, and absence of V1 fixed-policy trees.

No GitHub Actions run/status was registered at immediate readback for the result commit, so this evidence does not claim CI GREEN.

This is M01 feasibility evidence only. It does not discharge M05/L04/L05 delivery/update acceptance, install V2 into the user's live environment, or authorize adoption/custody transfer.
