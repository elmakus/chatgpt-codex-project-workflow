# M04-T05 — Cumulative M04 acceptance and immutable review freeze

Date: 2026-09-22
Card: `M04-T05`
Target repository: `elmakus/project_workflow_v2`
Target branch: `feat/pwv2-m04-integration-close`
Exact implementation commit: `f40250fa2fe88477df3f03c26adfeb2d8024581b`
Exact implementation tree: `90d5ebb7480dbc2eeab633a518bce221f09c7a45`
Target PR: `#4`, open draft, base `main`, head read back as the exact implementation commit.
M04-T05 Card blob: `61ae9578d0df1eb7dbb4f0030d638fa846e2f6aa`

## Cumulative M01-M04 verification

The exact implementation commit was checked without mutation.

GitHub readback:
- push Actions run `35768949267`: PASS;
- pull-request Actions run `35768955381`: PASS;
- PR #4 head: `f40250fa2fe88477df3f03c26adfeb2d8024581b`;
- PR #4 base: `main`;
- target branch HEAD: same exact commit.

Repository checks on exact detached commit:
- `sh scripts/test.sh`: PASS;
- state: 28/28 PASS;
- router: 39/39 PASS;
- execution: 4/4 PASS;
- review: 1/1 PASS;
- recovery: 2/2 PASS;
- Close + fork-lineage: 28/28 PASS;
- full `python3 -m unittest discover -s tests -v`: 102/102 PASS;
- `python3 -m compileall -q tools tests`: PASS;
- `git diff --check`: PASS;
- clean-tree check `git status --porcelain`: PASS.

The local deterministic verification was executed on the connected Tower against a fresh clone checked out at the exact immutable commit. Runtime/device identity is observational evidence only and is not part of workflow routing, state or provenance.

## M04 acceptance coverage

The cumulative surface includes the required M04 cases:
- A06 external-effect uncertain-write/readback and no blind retry;
- A08 unchanged semantic coverage with target movement and compatible GREEN reuse;
- A09 material content/behavior/acceptance change creating a new review subject;
- A10 target-side recovery and cleanup independent of source-ref survival;
- A16 trigger-only fork lineage, numeric private lanes/order, immutable history and native latest alias identity;
- target-race pre-mutation reread;
- stronger review coverage reuse;
- stacked dependency integration paths;
- ordinary Close negative read set excluding the fork-lineage module;
- all-terminal Cards routing to Close rather than directly to a stop;
- end-of-approved-scope only after durable completion;
- deployment/live-write alone not creating a human gate while explicit accepted authorization still does;
- tracker closing linkage only on the final scope-completing default-branch path and accepted-completion-only fallback closure.

No actual fork tag, release, deployment, upstream sync, branch deletion, PR merge or production adoption was performed by this Card.

## Freeze disposition

Cumulative deterministic acceptance is GREEN on one exact immutable target.

A fresh independent semantic review is still required before M04-T05 can become terminal. The review must bind this exact implementation commit/tree, this exact M04-T05 Card blob and this acceptance-evidence blob. Any material target change invalidates the frozen subject and requires a new attempt.
