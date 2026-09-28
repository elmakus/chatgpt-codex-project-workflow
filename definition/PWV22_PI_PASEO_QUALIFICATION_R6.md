# PWv2.2 Definition R6 — Pi/Paseo realization qualification

Status: IN PROGRESS
Definition subject: `pwv22-program@22 / R6`
Runtime subject: `elmakus/pi-unraid@fc7a470a7330839cbaf8eaf0c2914323981d6901`
Purpose: disposable-fixture evidence for Requirements 77-85. This evidence does not make runtime/session identity canonical workflow authority.

## Acceptance matrix

| Prototype | Purpose | Status |
| --- | --- | --- |
| P0 | bridge/config/tool-injection preflight | GREEN |
| P1 | native child/worktree baseline | GREEN |
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


## P0 — GREEN

Disposable fixture:
- container: `pwv22-r6-paseo`;
- frozen image: `pi-unraid:paseo-b4e0c1e7c276`;
- isolated home/projects/worktrees under `/mnt/user/appdata/pi-unraid/pwv22-r6-qual`;
- production `pi-unraid-paseo-1` config/state was not mutated.

Verified:
- Paseo `0.9.2`, Pi `0.87.1`, SpecPi `0.34.0`, pi-mcp-adapter `2.37.0`, Playwright `1.63.0`;
- `worktrees.root=/worktrees`;
- disposable config pins `daemon.mcp.enabled=true`, `daemon.mcp.injectIntoAgents=true`, `daemon.relay.enabled=false`;
- Pi provider reports Ready with one configured model;
- fresh Pi Main agent `d3c7ad0d-a3e8-47d0-8116-d64f153632dc` successfully invoked injected MCP tool `paseo_list_agents` without shell fallback.

Production drift discovered, not changed:
- live production config lacks persisted `daemon.mcp.enabled` and `daemon.mcp.injectIntoAgents`;
- live production `daemon.relay.enabled=true` although current repo configurator would pin false.

Disposition: configuration/readback gap only; no evidence for a new subagent runtime.

## P1 — GREEN

Fixture base: `c39e4ab9b91cc3edf990992ce4a4010f82395032`.

Main used injected Paseo MCP to create:
- same-workspace read-only child `1f5fd680-f551-432d-ae24-b329bd297f62`; it read exact `contract=v1` and made no Git mutation;
- worktree child A `adc48795-d27e-4326-8283-55d336d4410e`, branch `pwv22-p1-a`;
- worktree child B `2ea91b8d-54fc-4795-bc4d-b99dda29fd52`, branch `pwv22-p1-b`.

A and B were launched before either completed and ran concurrently. Both report the Main agent as `ParentAgentId`.

Independent Git readback inside the fixture:
- main checkout remains clean at the exact base;
- A merge-base = exact base, ahead by 1, changed only `a.txt`, final commit `b58b359d33afc7a05bcc958f1931b252f155767a`;
- B merge-base = exact base, ahead by 1, changed only `b.txt`, final commit `2e631804ddaeefd9ab1d2aa1b601fa4c3f98bd01`;
- Paseo reports separate worktree workspaces for A and B and local workspace for Main/read-only child.

Disposition: native Paseo is sufficient for parented child creation, same-workspace read-only delegation, concurrent isolated worktree mutation and exact result readback. No third-party Pi subagent extension is justified by P1.
