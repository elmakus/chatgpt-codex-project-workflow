# Semantic Audit — Lean Documentation + Authority Preservation

Date: 2026-09-18
Base: `main@c5f70349ce58670e2bc20fac6724ba8382ad669a`
Audited implementation subject: `docs/lean-authority-preservation@c6cec5f06491d43b3b0849c1c30fbb068882d94b`
Verdict: **GREEN**

## Scope

Audit the workflow changes that:
1. reduce documentation duplication;
2. make separate milestone files optional JIT extensions;
3. reduce mandatory Task Card boilerplate;
4. allow simple cards to use Task Board test summaries without standalone evidence files;
5. shorten cumulative handoffs;
6. preserve high-quality planner intent through downstream orchestration/review;
7. archive historical workflow audits/migration reports outside repository root.

## Semantic checks

### GREEN — Project truth and live state

- `implementation/TASK_BOARD.yaml` remains the sole mutable execution-state authority.
- `PROJECT.md` remains high-level routing/policy only.
- No live executor/status/result state was moved into Master Plan, milestone or Task Card contracts.

### GREEN — Milestone contract compaction

- An approved Master Plan milestone subsection is now the default milestone contract.
- `implementation/milestones/MXX.md` is optional and created JIT only when it adds material execution/acceptance detail.
- An optional milestone file extends rather than replaces/weaker-summarizes approved planner authority.
- Existing project milestone files remain valid; migration is forward-looking and does not require deletion/rewrite churn.

### GREEN — Task Card compaction

- Mandatory card core is limited to identity/milestone, dependencies, exact authority slice, bounded outcome/scope, acceptance/tests, and material constraints/gates.
- Priority, complexity, phase, code-location hints, capabilities and parallel metadata are optional unless useful.
- Workflow-standard Refresh Gate / blocker / Definition of Done semantics are inherited rather than copied into every card.

### GREEN — Authority Preservation / no-loss delegation

- Progressive disclosure is explicitly **lossless by authority, selective by context**.
- A coordinator may reduce context volume but may not drop an implementation-shaping authoritative constraint.
- Each downstream executor/reviewer either receives the applicable constraint explicitly or must read the exact durable authority reference.
- Material planner rationale is preserved when omitting it could reasonably cause a different implementation choice.
- Summary/paraphrase never outranks exact requirements, accepted decisions or approved-plan authority.
- Executor and independent reviewer evaluate the same applicable authority slice.
- The rule constrains project information transfer only; it does **not** merge Project Workflow with `codex_workflow` or duplicate Codex internal orchestration mechanics.

### GREEN — Evidence compaction

- Simple reproducible cards may close with exact result pointers + precise Task Board `tests_summary` and `evidence: null`.
- Standalone evidence remains expected for:
  - integrated milestone acceptance;
  - REQUIRED/RECOMMENDED independent review;
  - baseline/authorized exceptions;
  - material external writes/readback/reconciliation;
  - complex multi-stage verification;
  - explicit contract requirements.
- Milestone acceptance evidence remains mandatory for terminal GREEN milestone state.

### GREEN — Handoff compaction

- Cumulative handoff remains mandatory milestone continuation context, but no longer requires boilerplate inventories of changed files/APIs/schema sections.
- It preserves checkpoint/head, achieved state, durable authority now in force, verification/review pointers, material exceptions, and next durable starting point.
- Optional technical details are included only when they materially affect continuation.

### GREEN — Existing review and execution semantics preserved

- `chatgpt_only` required/recommended review still requires fresh normal ChatGPT review after implementing chat stops at `pending`.
- `codex_only` still uses independent reviewer worker/session without returning to ChatGPT solely for independence.
- `mixed` remains the only policy using Capability Gate.
- Fixed-policy capability preflight remains prohibited.
- Explicit deployment/live-write authorization gates remain hard stops.
- Automatic fixed-policy multi-milestone continuation semantics remain unchanged.

### GREEN — Repository hygiene

- Historical migration and semantic-audit reports were content-preservingly relocated to `docs/history/`.
- Repository root now contains active entrypoints/CHANGELOG plus workflow directories rather than historical audit clutter.
- `docs/history/README.md` explicitly marks archived reports as historical evidence, not current authority.

## Contradiction found and corrected during audit

`workflow/contracts/GITHUB_STATE.md` still required a standalone evidence path for every DONE card and described milestone files as universally present. It was corrected to match the new optional-evidence and default-Master-Plan milestone semantics.

## Migration assessment

No repository-wide migration of existing projects is required.

At the next safe execution-prep/state edit:
- legacy Task Boards may add explicit milestone `contract` pointers;
- newly prepared work uses lean JIT artifact rules;
- existing milestone/evidence/handoff artifacts remain valid durable history/contracts.

## Final assessment

**GREEN.** Documentation volume is reduced without reducing the amount of authoritative implementation-shaping information available to later orchestrators, workers or reviewers.
