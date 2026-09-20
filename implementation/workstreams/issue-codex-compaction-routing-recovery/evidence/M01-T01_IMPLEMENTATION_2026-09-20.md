# M01-T01 implementation evidence — 2026-09-20

## Exact subject

- Card: `M01-T01 — Establish orchestration binding schema and recovery kernel`
- Review subject / implementation result: `319b034ebd3d5afd8643b755e00ab8d7987a0f34`
- Execution-start state commit: `9cf53a4e7feb454bf0d2c211cf4ebc466b89b0f8`
- Branch: `fix/codex-compaction-routing-recovery`

## Implemented scope

- Created JIT OpenSpec at `openspec/changes/codex-orchestration-context-recovery/`.
- Added `workflow/codex_only/ORCHESTRATION_KERNEL.md`.
- Added exactly `runtime_owner`, `policy_ref`, and `contract_fingerprint` under manifest `orchestration`.
- Defined workstream-local ownership, no-mirroring, binding validity and pre-schema-versus-invalid distinction in `WORKSTREAMS.md`.
- Narrowed `STATE.md` so opaque manifest policy/profile selection is the only permitted profile-related durable state while concrete runtime identity remains forbidden.
- Did not wire Intake/Recovery/dispatch paths; those remain M01-T02 scope.
- No `workflow/chatgpt_only/*` file changed in this Card.

## Verification

Verification was run from a fresh checkout of exact subject `319b034ebd3d5afd8643b755e00ab8d7987a0f34`.

- `python3 -m unittest tests.test_codex_only_continuous_orchestration_contract` → GREEN, 8/8.
- `python3 -m unittest discover -s tests -p 'test_*.py'` → GREEN, 78/78.
- `git diff --check 9cf53a4e7feb454bf0d2c211cf4ebc466b89b0f8..319b034ebd3d5afd8643b755e00ab8d7987a0f34` → GREEN.
- T01 static audit → GREEN:
  - template orchestration block contains exactly the three approved fields;
  - kernel contains non-durable latch, same-version re-bind, bounded read-set, role-agnostic gate and fail-closed semantics;
  - old blanket `worker/session/model/profile/...` prohibition is absent and replaced by the scoped opaque-selection exception;
  - Workstreams contains the orchestration ownership/schema boundary and pre-schema distinction;
  - no `workflow/chatgpt_only/*` path changed.

## External effects

Repository branch writes only. No deployment/live-system mutation.
