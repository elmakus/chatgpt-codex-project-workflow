# ChatGPT-only delegated-worker semantic implementation audit

Date: 2026-09-18
Base: `main@23b8c368aea160566abdfd3fbc42bd0facb88bd4`
Subject branch: `feat/delegated-workers`
Implementer self-check: **GREEN — independent review still required**

## Scope

Audit the additive delegated-worker semantics introduced under `chatgpt_only`.

This is implementation evidence, not the REQUIRED independent review verdict.

## Preserved invariants

- normal ChatGPT remains the fixed Task Card executor;
- `implementation/TASK_BOARD.yaml` remains the sole mutable execution-state authority;
- fixed-policy execution still avoids capability inventory/preflight;
- REQUIRED/RECOMMENDED Independent Review remains a fresh normal ChatGPT chat;
- live/deployment authorization gates remain binding;
- existing Cards without delegated-worker authority retain ordinary behavior.

## New bounded semantics

- delegation is opt-in through stable Task Card authority;
- worker profiles are project-defined and backend-specific CLI detail stays outside generic workflow rules;
- worker calls are awaited rather than normally polled;
- raw worker logs/transcripts remain outside main context by default;
- parent-facing results are bounded/normalized and validated before use;
- delegated tester/verifier input is contract + resulting state rather than executor transcript by default;
- delegated workers are leaf workers by default;
- worker failure never advances the Card automatically;
- delegated tester/verifier evidence does not set or satisfy workflow `review_state`.

## Cross-file ownership

- `workflow/chatgpt_only/DELEGATED_WORKERS.md` — canonical delegated-worker runtime/authority contract.
- `ROUTER.md` — conditionally loads that contract only when preparation/execution needs it.
- `EXECUTION_PREP.md` + `TASK_CARDS.md` + template — author stable opt-in worker requirements without runtime preflight.
- `EXECUTION.md` — invokes/awaits worker at the concrete step and validates normalized result.
- `STATE.md` — preserves ChatGPT executor provenance and prevents a second worker-state authority.
- `README.md` — high-level user-facing model.
- `CHATGPT_ONLY_LOSSLESS_SEMANTIC_MATRIX.md` — records the additive semantic ownership.

## Forbidden drift checks

The implementation must contain no Muse-specific:
- command name;
- CLI flag;
- workstation path;
- model name;
- auth path.

Generic workflow authority must not depend on a particular delegated-worker backend.

## Required independent review focus

The fresh reviewer should specifically check:
1. no wording accidentally changes executor ownership from ChatGPT;
2. no delegated tester path weakens fresh ChatGPT Independent Review;
3. no polling/state-ledger semantics slipped in;
4. existing non-delegated Cards remain valid;
5. conditional context loading remains lean;
6. worker failure cannot silently satisfy Card completion.
