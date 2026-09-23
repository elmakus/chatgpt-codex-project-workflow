# M05-T02 — Codex plugin package and thin local bootstrap evidence

Date: 2026-09-23
Card: `M05-T02`
Target: `elmakus/project_workflow_v2@feat/pwv2-m05-delivery`
Accepted implementation subject: `b9e57e8ba385efc780a7d18fe6b370b278b9e73c`
Tree: `75d69e7ada54021a923e13b4d57ee954323c6d2d`
Base / M04 integrated predecessor: `674fb970913c393cfc6ed82a5ef67dda8b8713b7`
PR: `elmakus/project_workflow_v2#5`

## Implemented contract

- Productionized the installed Codex package as `pw` version `0.2.0` with Skill `project_workflow_v2` and accepted invocation `$pw:project_workflow_v2`.
- Kept the Skill as a locator/bootstrap only: it points at the installed package root and bundled `workflow/ROUTER.md`, then delegates exact durable recovery and progressive disclosure to the canonical router.
- Hardened SessionStart so configured `PLUGIN_ROOT` must identify the same installed root that contains the executing hook.
- The bundled router must exist, stay path-contained inside the installed package root, be readable and carry the minimal V2 router identity markers; otherwise bootstrap fails closed.
- Successful SessionStart emits only a bounded local-router locator/recovery instruction. Failure explicitly forbids fallback to V1, another package/source, remote workflow policy, runtime-specific policy or reconstructed chat memory.
- Startup/resume/compaction inputs share the same thin local bootstrap and do not create canonical runtime/session state or a Context Health lifecycle.
- No second workflow tree was introduced under the Skill/hook. The marketplace exposes exactly one local `pw` source.

## Verification

Exact target `b9e57e8ba385efc780a7d18fe6b370b278b9e73c`:

- GitHub Actions run `35814595279`: PASS.
- `sh scripts/test.sh`: PASS.
- Codex delivery suite: 9/9 PASS, including package identity/single-source, Skill thinness, byte-preserving canonical `workflow/` payload hash comparison, SessionStart router-only read set, bounded hook command/trust, startup/resume/compaction parity, missing/malformed router fail-closed, router symlink/path escape rejection and `PLUGIN_ROOT` source mismatch rejection.
- State suite: 28/28 PASS.
- Router suite: 39/39 PASS.
- Execution suite: 4/4 PASS.
- Review suite: 1/1 PASS.
- Recovery suite: 2/2 PASS.
- Close/fork/ChatGPT/Codex combined suite: 42/42 PASS.
- Unique Python suites represented by the full repository checks: 116 tests; the 9 Codex-delivery tests are intentionally also exercised by the package shell probe.

## Readback

- Target branch `feat/pwv2-m05-delivery` read back at exact HEAD `b9e57e8ba385efc780a7d18fe6b370b278b9e73c` and tree `75d69e7ada54021a923e13b4d57ee954323c6d2d`.
- Draft PR #5 is open/mergeable from the exact target branch to `main@674fb970913c393cfc6ed82a5ef67dda8b8713b7`.
- M01 feasibility evidence remains the real isolated-host proof that `pw:project_workflow_v2` resolves from installed package bytes. This Card productionizes that package contract; supported installer update/readback remains M05-T03 and live installed-product qualification remains M05-T04.
- No live user Codex installation or project provisioning was mutated by this Card.

## Acceptance disposition

M05-T02: GREEN / DONE.

Policy reroute after reconciliation: return to the current-main ChatGPT-only router; M05-T03 becomes the next dependency-satisfied deterministic obligation.
