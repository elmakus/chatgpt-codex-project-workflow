# PWv2.2 Definition R6 — Pi/Paseo realization qualification

Status: COMPLETE — GREEN
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
| P4 | lifecycle/cancel/archive/cleanup | GREEN |
| P5 | Main restart + lost notification + stale generation fencing | GREEN |
| P6 | explicit finite parallel fixture + serial fan-in + integrated compatibility | GREEN |

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


## P4 — GREEN

Disposable worktree child `b73d1b11-9474-4d78-a562-757f82a0317f`:
- modified `contract.txt` without committing, then entered `sleep 120`;
- coordinator waited until both `Status=running` and dirty Git state were observed;
- `paseo stop` returned one stopped agent and the agent became idle;
- no `sleep 120` process remained after stop;
- dirty `contract.txt` remained in the worktree at the original exact base;
- `paseo archive` changed the agent to `closed/Archived=true`;
- the dirty worktree remained present after archive.

Cross-workspace descendant behavior:
- archiving Main `d3c7ad0d-a3e8-47d0-8116-d64f153632dc` did not cascade-close P1 worktree child `adc48795-d27e-4326-8283-55d336d4410e`;
- the child remained unarchived and its `ParentAgentId` became null/detached.

Disposition: normal cleanup can use stop -> readback -> archive while preserving uncertain/dirty worktrees. Parent cleanup must explicitly enumerate/reconcile descendants; parent archive is not a cascade guarantee. No custom lifecycle daemon is justified, but bounded cleanup/readback logic is required.


## P5 — GREEN

### Lost-Main recovery without replay

Generation-1 authority:
- exact authority commit `c4ea4949ff8d0a8b519e77e0e90bd86bd0485043`;
- `authority.json`: generation 1, assignment `P5-result`, expected branch `pwv22-p5-result`.

Old Main `1dcbfb87-3254-45f5-b639-85be4c0b7d5c` launched worktree child `31f0d831-5e8a-4271-b857-098dc915baf7`. Old Main was archived while the child remained active; the child survived and detached from the archived parent. The old Main therefore could not be relied on to consume the eventual completion notification.

The child later committed:
- branch `pwv22-p5-result`;
- commit `2d6db3d888f1465005fd2044e22a129f55b72d25`;
- exact result `generation=1`.

Fresh replacement Main `cfd8ab39-206c-4b8f-b863-e9bd320be94c`, with no prior P5 transcript, reconstructed the assignment from Git authority + Paseo + the expected branch and returned `recovered_without_replay=true` with the exact durable result commit. It did not create or rerun a worker.

Correlation pitfall: its first agent-ID correlation selected the archived Main when filtering by the local workspace rather than the result worktree. Exact Git recovery was still correct. Any production helper should correlate by assignment/expected branch/workspace metadata rather than a broad cwd query.

### Late stale-result fence

A second stale test was bound to:
- generation-2 authority commit `eabdadf61a834cf3d0206c07e340c6759e6c2234`;
- branch `pwv22-p5-stale2`.

While the result-producing `sleep 90` process was still running and the branch still equaled the generation-2 base, main authority advanced to generation 3 at `a3a51aa1dedf6e873ae7f86441757562eed21f5c`.

The old worker later produced:
- commit `1af786f17693ca953d279bd302d68af5623aa5fc`;
- parent `eabdadf61a834cf3d0206c07e340c6759e6c2234`;
- `stale2.txt = generation=2`.

Deterministic fence:
- current authority = generation-3 commit;
- result parent = generation-2 commit;
- result is not an ancestor of current main;
- outcome: `FENCE=STALE_REJECT`, with no merge.

Fresh evaluator `dc3c199b-7ba4-4575-a522-23332dcb4fe5` independently reconstructed the same facts and returned verdict `STALE`.

Disposition: PW/Git + native Paseo evidence are sufficient for restart recovery and stale-result rejection without a separately durable orchestration journal/state machine. Exact assignment correlation and generation/authority fencing are strong candidates for a thin deterministic PW/Pi helper because correctness should not depend on an LLM choosing the right agent query.


## P6 — GREEN

### Explicit admission characterization

Synthetic admission classifier produced:
- disjoint write pair -> `ALLOW`;
- overlapping write pair -> `SERIALIZE`;
- shared external-effect resource -> `SERIALIZE`;
- disjoint semantic seam -> `ALLOW_REQUIRES_INTEGRATED_COMPAT`.

This confirms that worktree disjointness is not itself parallel legality.

### Positive serial fan-in

Exact sibling Results:
- A `b58b359d33afc7a05bcc958f1931b252f155767a`;
- B `2e631804ddaeefd9ab1d2aa1b601fa4c3f98bd01`;
- common base `c39e4ab9b91cc3edf990992ce4a4010f82395032`.

Dedicated Paseo integration agent `b873451c-06c6-4915-8dce-22033ba703fc` was the single mutating integration owner. It applied A then B in the frozen order, with no manual conflict repair or reorder.

Combined candidate:
- branch `pwv22-p6-integration`;
- final commit `a80d77a948d7f346c60a3475d663e3ec950996cf`;
- changed only `a.txt` and `b.txt`;
- `a.txt` ends `child-a`;
- `b.txt` ends `child-b`;
- `contract.txt` remains exactly `contract=v1`.

Fresh read-only integrated-compatibility verifier `15e66a91-5742-43fe-8691-06e53e8abe88` ran against the exact combined commit, made zero commits/mutations and returned `GREEN`.

### Semantic-conflict negative case

Two sibling Results were constructed from the same exact base with disjoint write sets:
- producer `be3b7d3fd9dbcfb85b362eaf9a3bc2f44f3e3e39` adds `producer.txt: api=2`;
- consumer `8738ef82ffea30531fd209eb7758126e0a461305` adds `consumer.txt: expects=1`.

Dedicated integration agent `b6f286fa-effa-4963-97e5-050cf965d27a` cherry-picked producer then consumer cleanly with no Git conflict. Combined commit:
- `45de8f2c7bde2cc40f019d305dd88fb0aa847efe`;
- changed only `producer.txt` and `consumer.txt`.

Fresh read-only compatibility verifier `4e074665-db52-4f44-be38-e394d00d5dcf` made no mutation and returned:
- `verdict=RED`;
- producer API = 2;
- consumer expects = 1.

Disposition: one serial integration mutator may be a dedicated Paseo subagent, but exact admitted Results/order/scope remain Main/PW authority. A clean Git fan-in never substitutes for integrated semantic compatibility.

## Integrated R6 architecture disposition

P0-P6 falsified the need for a separate subagent runtime while proving a small deterministic semantic helper boundary.

### Selected realization

**Native Paseo + Pi + explicit configuration/skills + thin reconstructible PW/Pi helper.**

Native Paseo owns:
- managed agents and parentage;
- workspaces/worktrees;
- concurrent child execution;
- direct messaging transport;
- status/activity;
- stop/archive lifecycle;
- provider/model execution mechanics.

The thin helper owns only deterministic, reconstructible mechanics:
- materialize exact assignment/authority/generation fences from current PW/Git authority;
- correlate assignment -> expected branch/workspace/agent without treating runtime IDs as semantic truth;
- validate exact result ancestry/subject/output contract;
- reject stale/late outputs;
- validate Review Attempt/evidence publication paths and frozen subject;
- implement explicit finite parallel admission checks from accepted PW claims;
- freeze/validate deterministic fan-in order and exact sibling Result set;
- validate integrated-compatibility subject binding;
- perform bounded stop -> readback -> archive and explicit descendant cleanup/readback.

The helper MUST NOT own a durable semantic queue, journal, Task Board, scope decisions, strategy, acceptance, or a second recovery truth. Deleting helper-local state must leave recovery possible from PW/Git plus native Paseo evidence.

### Rejected/escalation-only mechanisms

- third-party Pi subagent extension: **not justified** by P0-P6; native spawn/worktree/parent/lifecycle mechanics passed;
- full dedicated orchestration-runtime: **not justified**; P5 proved recovery and stale rejection without a separate durable journal/state machine;
- hard per-agent sandbox: **not required** by current owner policy; P2 proved canonical detect-and-reject publication integrity.

### Required production realization delta

The production `pi-unraid` configuration path must, during later implementation/Planning:
- durably pin and read back `daemon.mcp.enabled=true`;
- durably pin and read back `daemon.mcp.injectIntoAgents=true`;
- preserve explicit desired relay policy/readback;
- extend the existing Paseo/Pi regression harness rather than adding another runtime service.

No production runtime/config mutation was performed by this qualification.

### P7 disposition

P7 is **NOT REQUIRED** for Definition R6 because R6 does not claim universal hard physical prevention. If a future exact obligation requires hard prevention, that obligation must add and prove the appropriate OS/provider/filesystem/network/credential boundary.

## Qualification conclusion

All required P0-P6 evidence is GREEN. The selected architecture is smaller than the prior orchestration-runtime while preserving the required PW semantics. No unresolved technical unknown from this qualification requires another owner/product decision before Definition completion.
