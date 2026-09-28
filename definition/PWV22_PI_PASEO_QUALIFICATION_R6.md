# PWv2.2 Definition R6 — Pi/Paseo realization qualification

Status: IN PROGRESS
Definition subject: `pwv22-program@22 / R6`
Runtime subject: `elmakus/pi-unraid@fc7a470a7330839cbaf8eaf0c2914323981d6901`
Purpose: disposable-fixture evidence for Requirements 77-85. This evidence does not make runtime/session identity canonical workflow authority.

## Acceptance matrix

| Prototype | Purpose | Status |
| --- | --- | --- |
| P0 | bridge/config/tool-injection preflight | IN PROGRESS |
| P1 | native child/worktree baseline | PENDING |
| P2 | fresh Review + exact publication/write envelope | PENDING |
| P3 | communication semantics/contamination | PENDING |
| P4 | lifecycle/cancel/archive/cleanup | PENDING |
| P5 | Main restart + lost notification + stale generation fencing | PENDING |
| P6 | explicit finite parallel fixture + serial fan-in + integrated compatibility | PENDING |

## P0 — initial live readback

Observed on the currently running Tower container `pi-unraid-paseo-1` before any disposable-fixture mutation:
- image: `pi-unraid:paseo-b4e0c1e7c276`;
- Paseo `0.9.2`;
- Pi `0.87.1`;
- Playwright `1.63.0`;
- image contract pins SpecPi `0.34.0` and pi-mcp-adapter `2.37.0`;
- mounts include persistent `/home/paseo`, `/projects` and `/worktrees`;
- live `worktrees.root = /worktrees`;
- live config does not currently persist `daemon.mcp.enabled` or `daemon.mcp.injectIntoAgents`;
- live `daemon.relay.enabled = true`, while current repo `scripts/configure-paseo-runtime.sh` would pin it false.

Interpretation: version/worktree substrate matches the frozen runtime subject, but live persisted configuration has drift and does not yet prove required Paseo-tool injection. Remaining P0 and P1-P6 must run in a disposable fixture rather than silently mutating the production Paseo home.
