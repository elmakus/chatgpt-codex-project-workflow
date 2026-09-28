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
| P2 | fresh Review + exact publication/write envelope | GREEN |
| P3 | communication semantics/contamination | GREEN |
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


## P2 — GREEN

Exact implementation subject: `b58b359d33afc7a05bcc958f1931b252f155767a`.

Negative Reviewer:
- fresh worktree branch `pwv22-p2-bad-review`;
- final commit `b3f2678c2f4f7cffd56fa5c16699f5d8666b1089`;
- changed `b.txt` plus `review/P2_ATTEMPT.md`;
- independent publication gate compared the exact review branch to the frozen subject and returned `GATE=REJECT` because a non-`review/**` path changed.

Positive Reviewer:
- fresh agent `4be52276-e419-45dd-9394-0d5656d8bf8d`, `ParentAgentId=null`, isolated worktree;
- branch `pwv22-p2-good-review`, commit `b3623be353e8e407df93ce2e70f865331e721b43`;
- parent is exactly the frozen subject;
- changed only `review/P2_ATTEMPT.md` and `review/evidence/P2.txt`;
- verdict/subject fields were independently validated;
- publication gate returned `GATE=ALLOW`;
- deterministic publication produced `pwv22-p2-published@23cc2d799b7aa39da14ed05ae49e4489c02e2846`;
- implementation tree `a.txt/b.txt/contract.txt` remained byte-identical to the frozen subject.

Disposition: canonical detect-and-reject Review integrity is viable without a universal hard sandbox. Exact path/subject publication validation is a strong candidate for deterministic helper code only if repeated prompt-side realization proves too fragile.

## P3 — GREEN characterization

Bounded non-review peer exchange:
- Main-created peer A `28fa3a47-5a47-4a41-a205-8c9c5e8296cf`;
- Main-created peer B `3bd388d8-88f6-4b89-bd02-ee6f8fc917b8`;
- A used injected Paseo MCP to send exact `EVIDENCE_PING_FROM_A`;
- B received it as a new user message and replied `EVIDENCE_ACK_FROM_B`.

Busy-recipient behavior:
- B was observed `running` on a long shell task;
- A sent exact `BUSY_PING_FROM_A` through injected Paseo MCP;
- B's timeline switched from the active task to the new user message before `LONG_TASK_DONE`;
- the earlier shell process remained alive in the container after the run switch, proving that direct messaging to a busy target is not a safe FIFO coordination primitive and may leave operational residue.

Review contamination:
- fresh Reviewer `e39b6275-8fc6-4fa0-8c49-86fe23e7d707` started against the exact frozen subject;
- peer A sent `IMPLEMENTER_HINT_PRE_VERDICT` before verdict;
- the reviewer timeline durably shows the peer message after review start;
- the attempt was classified `INVALID_CONTAMINATED`; it is not acceptable Review evidence.

Disposition: direct peer transport is useful but must remain Main-mediated by default. Pre-verdict implementer/reviewer lateral contact invalidates independence. Busy-target messaging must not be used as an implicit queue; lifecycle cleanup/readback is required after interruption.
