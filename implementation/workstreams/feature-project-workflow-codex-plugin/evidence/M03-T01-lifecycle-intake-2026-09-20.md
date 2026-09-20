# M03-T01 Lifecycle / Isolation / Intake Evidence — 2026-09-20

Card: `M03-T01 — Verify always-on lifecycle, isolation and intake UX`
Plan revision: `PWCP-P3`
Production package subject under test: `6e16ba11293bbdb7bbc8d96167e8280273d77304`
Current runtime: `codex-cli 0.155.0-alpha.9.2`
Execution result: `GREEN`

## Isolation and trust setup

All M03 runtime verification used disposable state under `/tmp/pwcp-m03-run-Yl5fbv`.

The exact M02 production package was checked out at `6e16ba11293bbdb7bbc8d96167e8280273d77304`. A disposable `CODEX_HOME` installed `pw@project-workflow`, kept the plugin globally disabled, and enabled it only from the enabled repository's trusted repo-local `.codex/config.toml`. A matched trusted control repository had no local enable override.

Native plugin readback reported:
- enabled repository: `pw@project-workflow` installed and `enabled: true`;
- control repository: the same installed plugin with `enabled: false`.

The disposable home initially had no model authentication. Existing workstation ChatGPT authentication material was copied into the disposable home without reading or printing its contents; `codex login status` then reported `Logged in using ChatGPT`. No live marketplace/plugin/config/trust state was changed.

For hook execution, runtime probes used `--dangerously-bypass-hook-trust` only inside this disposable, already-vetted acceptance environment. Persistent trust behavior remains the M01 accepted contract.

## Fresh-session always-on activation and control isolation

Enabled repository, ordinary prompt, no explicit Skill invocation:

```text
thread_id=01a0be30-95ac-7173-aaa8-7a70ca6661d2
PW_ACTIVE
```

Matched control repository, same ordinary prompt:

```text
PW_INACTIVE
```

This proves the same installed package activates automatically only where the repository-level plugin enablement applies.

## Resume lifecycle

The exact enabled thread was resumed through the native current-runtime CLI:

```text
codex exec resume ... 01a0be30-95ac-7173-aaa8-7a70ca6661d2 ...
PW_RESUME_ACTIVE
```

The resumed thread retained the Project Workflow invariant.

## Compaction lifecycle

Current App Server schema/readback exposes native `thread/resume` and `thread/compact/start`.

The enabled thread was resumed through App Server and `thread/compact/start` was issued for the same thread. The persisted rollout contains a completed native compaction item:

```text
type=ContextCompaction
id=01a0be33-0be6-7e90-b913-a48cd933d9ce
started_at_ms=1789897411558
completed_at_ms=1789897429002
```

A first turn after that completed compaction contains a fresh `hooks.additional_context` developer item with the Project Workflow bootstrap, including:
- Project Workflow enabled for this workspace;
- read workspace `PROJECT.md` first;
- then read canonical `workflow/CONTEXT_ROUTING.md`;
- follow only the selected execution policy;
- load route modules, durable state, authority and evidence progressively;
- `$pw:project-workflow` remains an explicit entry/recovery path;
- the SessionStart reminder is not workflow policy.

That post-compaction turn returned:

```text
PW_COMPACT_ACTIVE
```

The same thread rollout contains four `hooks.additional_context` occurrences across the exercised lifecycle, including the post-compaction bootstrap.

## Progressive disclosure

The production SessionStart bootstrap remains bounded (569 characters in direct installed-hook readback) and contains routing guidance rather than copied workflow policy. It references workspace `PROJECT.md` and canonical `workflow/CONTEXT_ROUTING.md`, and contains neither the `codex_only` nor `chatgpt_only` policy body.

Runtime probe traces show the model loading:
1. workspace `PROJECT.md`;
2. canonical `workflow/CONTEXT_ROUTING.md`;
3. the selected `workflow/codex_only/ROUTER.md`;
4. route-specific modules only when the probe requires them.

The host Skill registry exposes one `pw:project-workflow` Skill path/description; it does not preload the Skill body or canonical workflow tree into SessionStart context.

## Intake UX comparison

Read-only route probes ran in the disposable enabled repository. Because this host's bundled bubblewrap produced `pivot_root: Invalid argument` when a model attempted file reads under `read-only` sandbox, only the route-inspection probes used `danger-full-access` inside the disposable no-remote repository. Each probe explicitly forbade writes. Before and after probes, `git status --porcelain` remained exactly:

```text
?? .codex/
?? PROJECT.md
```

Those are the pre-existing test-repository setup files; no additional mutation appeared.

Observed routing:

| Input form | Current-runtime result |
| --- | --- |
| `#feature PWCP_M03_FEATURE_PROBE ...` | `ROUTE_INTAKE_FEATURE` |
| `$pw:project-workflow feature PWCP_M03_FEATURE_PROBE ...` | `ROUTE_OTHER` |
| `#issue PWCP_M03_ISSUE_PROBE ...` | `ROUTE_INTAKE_ISSUE` |
| `$pw:project-workflow issue PWCP_M03_ISSUE_PROBE ...` | `ROUTE_OTHER` |

The explicit-Skill feature probe was recognized as using the `project-workflow` Skill and entered the canonical router, but its `feature` argument is not equivalent to the router's explicit `#feature` operator directive. The same distinction holds for `issue`.

### Supported convention selected by M03 evidence

Per PWCP-REQ-008/009:
- supported/preferred new-feature intake: `#feature <description>`;
- supported/preferred issue intake: `#issue <description>`;
- `$pw:project-workflow` remains the explicit general entry/recovery path;
- do **not** document `$pw:project-workflow feature ...` or `$pw:project-workflow issue ...` as equivalent intake syntax on this current runtime.

M04 documentation/release reconciliation should carry this evidence-based convention forward.

## Package regression

Exact production package subject:

```text
HEAD=6e16ba11293bbdb7bbc8d96167e8280273d77304
python3 -m unittest discover -s tests -p "test_*.py"

..............
----------------------------------------------------------------------
Ran 14 tests in 0.023s

OK
```

Generic marketplace/update behavior remains covered by accepted M01/M02 evidence and was not redundantly re-certified beyond the isolated install/readback needed for M03.

## Result

`GREEN`.

M03-T01 implementation/verification evidence satisfies the Card acceptance surface. The user-facing intake choice is now evidence-based and deterministic. Because the Card requires/recommends independent review, this implementation session must freeze an immutable M03-T01 subject and hand it to a fresh reviewer before Card finalization.
