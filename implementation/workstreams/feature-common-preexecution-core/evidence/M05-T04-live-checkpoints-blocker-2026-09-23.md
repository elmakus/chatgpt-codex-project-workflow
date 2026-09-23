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
