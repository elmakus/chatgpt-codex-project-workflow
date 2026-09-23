# M05-T04 — real-surface checkpoint status and user-run blocker

Date: 2026-09-23
Card: `M05-T04`
Candidate: `elmakus/project_workflow_v2@fbd208c1c26eef2a227ea90aced05fd8ac32a9a4`
Candidate tree: `66a57d7abb53b87fde528352bba06e511cb5df1e`
Package: `pw@project-workflow-v2 0.2.1`
PR: `elmakus/project_workflow_v2#5`

## Status by live checkpoint

### L01 — BLOCKED on required user-run ChatGPT Android surface

Not executed.

The accepted validation matrix requires a normal ChatGPT Android Project whose user-owned Project Instructions point to `elmakus/project_workflow_v2` and whose disposable consumer repository has a valid V2 `PROJECT.md`. The user must start the nontrivial `#feature` interaction so the actual Android bootstrap/grilling behavior is observed.

This cannot be replaced by repository tests or by this V1-controlled construction chat.

### L02 — BLOCKED on required user-run ChatGPT Android interaction

Not executed.

The accepted scenario intentionally requires:
1. symptom-only `#issue`;
2. read-only diagnosis;
3. a subsequent user safety/question response instead of repair authorization;
4. only later explicit aligned repair authorization.

The human-response boundary is the subject of the test, so an agent cannot synthesize the required user responses and claim live GREEN.

### L03 — BLOCKED behind L02 live flow

Not executed.

The same disposable issue flow must reach real GitHub integration so an intermediate PR remains non-closing, the final scope-completing PR carries closing linkage, merge/default-branch Issue state is read back, and recovery creates no duplicate Issue.

GitHub mechanics are agent-operable after the live L02 flow exists, but the accepted combined scenario is not yet instantiated.

### L04 — PARTIAL real Codex evidence; final invocation still user-surface pending

Real installed Codex CLI `0.155.0-alpha.9.2` was exercised with isolated `CODEX_HOME=/tmp/pwv2-m05-t03-home`.

Observed:
- `codex debug prompt-input` with exact `$pw:project_workflow_v2` resolved `pw:project_workflow_v2` from `r1/pw/0.2.1/skills/project_workflow_v2/SKILL.md`;
- installed SessionStart located the exact bundled `0.2.1/workflow/ROUTER.md`;
- the only installed candidate source was `/tmp/pwv2-m05-t03-home/plugins/cache/project-workflow-v2/pw/0.2.1`;
- no `workflow/chatgpt_only` or `workflow/codex_only` legacy route directory existed;
- a safe disposable broken-package copy with no router returned:
  `BLOCKING Project Workflow V2 plugin-package error: canonical bundled router is missing ... Do not fall back to V1 ...`.

Deterministic T02 coverage also proves router-only SessionStart read set, path containment/source mismatch failure, thin Skill/hook, package byte preservation and startup/resume/compaction parity.

Not yet proven on the required live model-backed V2 project invocation:
- actual ordinary Skill execution following bundled router -> exact current module/durable refs progressively.

Therefore L04 is not labeled GREEN yet.

### L05 — GREEN on actual supported Codex CLI update path

Reuses exact M05-T03 evidence:
`implementation/workstreams/feature-common-preexecution-core/evidence/M05-T03-update-propagation-2026-09-23.md`.

Actual isolated Codex update:
- baseline `0.2.0`;
- supported `plugin marketplace upgrade project-workflow-v2`;
- supported `plugin add pw@project-workflow-v2`;
- installed `0.2.1`;
- canonical router SHA-256 changed and `PWV2_M05_UPDATE_SENTINEL_92AF` was read back;
- Skill SHA-256 remained `5a8ccfa19d8d2596eede309c1c3a30f662b6d5e1dd326b0c203ddffab67e19ee`;
- SessionStart SHA-256 remained `8426d8a1f8eb8d8ccce3f4afabb80a3a7d2a1585ecff289ba3b66a8f4359366c`;
- fresh SessionStart/debug input resolved the updated local `0.2.1` package;
- live control installation remained absent/unmodified.

This is real product/runtime evidence, not simulator-only GREEN.

## Automated regression on candidate

GitHub Actions `35814931203` on candidate `fbd208c1c26eef2a227ea90aced05fd8ac32a9a4`: PASS.

Affected deterministic suites remain GREEN, including A01/A02 foundations and package/read-set/path/trust coverage. A17 full cumulative disposition remains a later M07 qualification owner; this Card does not relabel incomplete system qualification.

## Real blocker / next required input

The remaining M05-T04 acceptance cannot be completed without the required user-driven product-surface interactions:
- ChatGPT Android L01;
- ChatGPT Android + GitHub combined L02/L03;
- final ordinary model-backed Codex L04 invocation in a disposable V2 project.

No production project adoption or live plugin installation has been performed to bypass this gate.


## Continuation attempt — 2026-09-23

The blocked Card was resumed under the current Project Workflow router to exhaust agent-operable work before returning to the user.

### L04 model-backed invocation attempt

A disposable V2 consumer project was created from the candidate's own valid router fixture under `/tmp`; no production project or live plugin installation was modified.

The isolated installed candidate remained `pw@project-workflow-v2 0.2.1`. The real Codex CLI `0.155.0-alpha.9.2` was invoked with exact `$pw:project_workflow_v2` in the disposable V2 project.

Observed before the runtime stop:
- the Skill resolved successfully;
- the model-backed agent explicitly entered `pw:project_workflow_v2`;
- its first workflow-policy read attempted the exact bundled local `/tmp/pwv2-m05-t03-home/plugins/cache/project-workflow-v2/pw/0.2.1/workflow/ROUTER.md`;
- no remote workflow-policy fetch or V1 fallback was observed;
- the isolated home initially lacked model authentication; a temporary copy of the existing Codex login credential was used only inside the disposable `/tmp` home, leaving the live Codex plugin state unchanged;
- the read-only sandbox command itself hit the workstation's unavailable unprivileged bubblewrap namespace, after which the invocation reached the account service but could not continue because the authenticated Codex account reported a usage-limit stop: retry available at **2026-09-26 10:10** local product-reported time.

This is a concrete runtime/access blocker for completing the final model-backed L04 evidence in this environment. It does not invalidate the already-GREEN L04 package-resolution, SessionStart, local-source, missing-router fail-closed or no-V1 evidence, but L04 remains PARTIAL rather than GREEN until one ordinary model-backed run completes.

### Remaining real user boundary

Even if L04 runtime capacity becomes available, M05-T04 still cannot become GREEN without the accepted user-driven ChatGPT Android scenarios:
- L01;
- L02, with L03 continuing from that real issue flow.

Therefore the Card remains BLOCKED and M05-T05 must not start.


## Live ChatGPT Android evidence — L01 and L02 progression

Consumer repository: `elmakus/test-pwv2`.

### L01 — GREEN

Observed on the normal ChatGPT Android Project surface with the canonical V2 Project Instructions:
- `#feature` created/recovered exactly one workstream `feature-completion-summary`;
- branch `feat/feature-completion-summary` was created;
- GitHub Issue #1 was created once and tracker readback is verified;
- workflow entered adaptive Brainstorming without `#grill`;
- the user received a material numbered product question with a recommendation and alternatives;
- after the user's answer, the Brainstorming challenge audit became GREEN;
- durable state reached `ready_for_definition` with `promotion_state = pending`;
- implementation did not begin and the workflow stopped at the user-owned Definition-promotion boundary.

Exact consumer branch readback during verification: `feat/feature-completion-summary@a961ff0c3a93a5f42241b9d8caf1e960cd932cba`.

### L02 — human-control boundary GREEN; downstream continuation in progress

Observed on a separate normal ChatGPT Android chat in the same Project:
- symptom-only `#issue` created/recovered one workstream `user-setting-persistence-restart`, branch `fix/user-setting-persistence-restart`, and GitHub Issue #2;
- diagnosis remained read-only because the consumer default branch had no application implementation; no false code-level root cause was asserted;
- the required prior-art Research was materialized and reconciled before alignment;
- the first exact repair subject was `repair:user-setting-persistence-across-restart:v1`;
- instead of authorizing, the user asked a safety/side-effects question;
- durable Intake classified that response as `concern`, with `response_observed = true` and `alignment_state = pending`; implementation remained forbidden;
- the concern routed to Brainstorming rather than being misread as repair authorization;
- the user accepted a safer non-destructive scope; the repair subject changed to `repair:user-setting-persistence-nondestructive:v2`, stale v1 prior-art was replaced by fresh exact v2 prior-art, and Brainstorming revision 2 reached GREEN;
- the user separately authorized Definition promotion for `safe-user-setting-persistence@2`; this did not authorize the repair;
- only after the distinct explicit user message authorizing `repair:user-setting-persistence-nondestructive:v2` did Intake become complete with `alignment_state = authorized` and exact matching `alignment_subject`;
- Definition then materialized as R1/GREEN with `premium_a = due`.

Exact consumer issue-workstream branch readback after authorization: `fix/user-setting-persistence-restart@9c31e834b23fc9184bf4adfd44c1a5bebb9af592`.
GitHub Issue #2 remains open, as expected before final integration/Close.

This proves the critical L02 regression boundary: post-diagnosis user discussion, concern and Definition promotion were all kept distinct from implementation authorization. The combined L02/L03 scenario continues through Planning/Execution/PR/Close so that implementation-start timing and final Issue closure can also be observed.
