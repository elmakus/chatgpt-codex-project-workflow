# M04-T01 Release Readiness and Acceptance Matrix — 2026-09-20

Card: `M04-T01 — Reconcile release documentation and full feature acceptance`
Plan revision: `PWCP-P3`
Current implementation subject before this evidence record: `59b0e56cc2a307cb512b60d26c7610dceebe8503`
Current runtime: `codex-cli 0.155.0-alpha.9.2`
Result: `GREEN`

## Release documentation

M04 added `docs/CODEX_PLUGIN.md` and linked it from `README.md`.

The guide records the accepted and verified contract:
- Git-backed marketplace source is this repository;
- plugin identity is `pw@project-workflow`;
- the single bundled Skill is `project-workflow`, explicitly invoked as `$pw:project-workflow`;
- user-level plugin state is kept disabled for opt-in behavior and an enabled repository supplies a repo-local `[plugins."pw@project-workflow"] enabled = true` override;
- normal Codex trust is a real prerequisite for the SessionStart hook, while `--dangerously-bypass-hook-trust` is identified only as a disposable-test mechanism, not normal setup;
- ordinary prompts in an enabled/trusted repository receive the bounded bootstrap automatically;
- `#feature <description>` / `#issue <description>` are the supported preferred intake forms on the accepted runtime;
- `$pw:project-workflow` remains the explicit general entry/recovery/debug path;
- Skill `feature` / `issue` arguments are not claimed as equivalent intake aliases on this runtime;
- the Skill/hook remain routing surfaces into workspace `PROJECT.md` plus canonical `workflow/CONTEXT_ROUTING.md`;
- marketplace refresh is owned by Codex/Workstation and the plugin has no updater.

Current-runtime help independently confirmed:
- `codex plugin marketplace add [OPTIONS] <SOURCE>` accepts `owner/repo` and `--ref <REF>`;
- `codex plugin add [OPTIONS] <PLUGIN[@MARKETPLACE]>`;
- `codex plugin marketplace upgrade [MARKETPLACE_NAME]` refreshes configured Git marketplace snapshots.

## M04 independent implementation checks

A fresh disposable clone of `feat/project-workflow-codex-plugin` at `59b0e56cc2a307cb512b60d26c7610dceebe8503` produced:

```text
python3 -m unittest discover -s tests -p "test_*.py"

..............
----------------------------------------------------------------------
Ran 14 tests in 0.022s

OK
```

Static package/drift audit:
- bundled Skill directories: exactly `["project-workflow"]`;
- Skill contains no copied `workflow/codex_only/ROUTER.md` or `workflow/chatgpt_only/ROUTER.md` policy path/body;
- SessionStart implementation contains no copied policy-specific router body;
- plugin surfaces contain no updater/timer/poller file;
- `docs/CODEX_PLUGIN.md` contains the accepted plugin identity, explicit Skill path, preferred `#feature/#issue` intake forms, repo-local enable/control configuration and canonical router reference;
- `README.md` links the plugin guide.

Using a new disposable `CODEX_HOME`, the same branch installed as a local marketplace on `codex-cli 0.155.0-alpha.9.2`:
- marketplace name: `project-workflow`;
- installed plugin: `pw@project-workflow`;
- version: `0.1.0`;
- native plugin readback: `installed: true`, `enabled: true`;
- direct installed SessionStart output: `hookEventName=SessionStart`, 573-character context for that temporary absolute path, references `PROJECT.md` and `workflow/CONTEXT_ROUTING.md`, and contains neither `codex_only` nor `chatgpt_only` policy bodies.

All M04 runtime writes were disposable under `/tmp`. No live Codex marketplace/plugin/config/trust state was changed.

## Requirement acceptance matrix

| Requirement | Result | Exact acceptance/evidence |
| --- | --- | --- |
| PWCP-REQ-001 — same-repository package | GREEN | M02 acceptance + M02-T01 package evidence prove repository-root marketplace/plugin packaging. |
| PWCP-REQ-002 — canonical workflow authority, no duplicated policy | GREEN | M02 acceptance; M04 static drift audit confirms the thin Skill/bootstrap still contain no policy-specific router copy. |
| PWCP-REQ-003 — one explicit `$pw:project-workflow` Skill | GREEN | M01 naming-delta evidence proves native `pw:project-workflow` discovery and real explicit invocation; M02 package + M04 audit confirm exactly one bundled Skill. |
| PWCP-REQ-004 — always-on enabled-repository invariant | GREEN | M03-T01 lifecycle evidence: ordinary enabled-repository prompt returned `PW_ACTIVE` without explicit Skill invocation. |
| PWCP-REQ-005 — bounded progressive-disclosure bootstrap | GREEN | M03 evidence proves bounded bootstrap/routing traces; M04 installed hook readback remains bounded and policy-neutral. |
| PWCP-REQ-006 — fresh/resume/compaction lifecycle | GREEN | M03 evidence records fresh `PW_ACTIVE`, resumed `PW_RESUME_ACTIVE`, native ContextCompaction and post-compaction `PW_COMPACT_ACTIVE`; independent M03 review GREEN. |
| PWCP-REQ-007 — disabled repository unaffected | GREEN | M03 matched control returned `PW_INACTIVE`; independent review reproduced native enabled=true versus control enabled=false isolation. |
| PWCP-REQ-008 — preserve `#issue/#feature` when reliable | GREEN | M03 current-runtime route probes reached canonical Intake for both directives; M03 acceptance selects them as preferred syntax. |
| PWCP-REQ-009 — one-Skill fallback architecture if directive reliability fails | GREEN | Accepted ADR-PWCP-002 defines fallback only when directive reliability is not demonstrated; M03 demonstrated directive reliability, so fallback is not activated. The package still exposes only one Skill and no duplicate issue/feature aliases. |
| PWCP-REQ-010 — explicit general entry/recovery path | GREEN | M01 real invocation proves `$pw:project-workflow`; M03 preserves it as the explicit general entry/recovery path and M04 documents that contract. |
| PWCP-REQ-011 — Git-backed marketplace/update, no plugin updater | GREEN | M02 Git-backed install evidence + M04 current CLI help/readback; static audit finds no plugin updater/timer/poller. |
| PWCP-REQ-012 — reuse qualified generic platform evidence | GREEN | M01–M03 evidence explicitly reuses unchanged generic marketplace/update results while directly verifying PWCP-specific deltas. |
| PWCP-REQ-013 — canonical workflow update propagates without Skill edit | GREEN | M02 deterministic update-propagation test + Git/install hash readback prove same-root workflow propagation while Skill hash remains unchanged. |
| PWCP-REQ-014 — explicit deterministic trust behavior | GREEN | M01 proves SessionStart is absent without trust/bypass and present with isolated bypass; M03 preserves trust semantics; M04 docs require normal trust and reject bypass as normal setup. |
| PWCP-REQ-015 — activation routes through workspace `PROJECT.md` / selected policy router | GREEN | M02 Skill/bootstrap contract and M03 progressive-disclosure traces prove workspace `PROJECT.md` → canonical `workflow/CONTEXT_ROUTING.md` → selected policy route. |

No requirement has an unresolved acceptance gap.

## Exact predecessor evidence

- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-acceptance-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-runtime-contract-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-T01-p3-naming-delta-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M02-acceptance-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M02-T01-plugin-package-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M03-acceptance-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M03-T01-lifecycle-intake-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M03-T01-independent-review-2026-09-20.md`

## Remaining workstream gate

This Card intentionally does not perform final target reconciliation or issue the workstream final-integration verdict. After Card finalization, M04 Close must:
1. refresh this workstream against current `main`;
2. rerun affected verification after any reconciliation;
3. freeze the exact refreshed integrated subject in the manifest-owned `RECOMMENDED` review gate unless exact stronger independent coverage of the whole refreshed workstream is proven;
4. obtain fresh independent review before final integration.
