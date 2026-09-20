# MF-T01 — Tighten ChatGPT-only Context Health anti-bounce semantics

- Milestone: `micro-fix`

> This file is a stable Task Card contract. Mutable execution/review/result state lives only in the selected canonical Task Board.

## Authority slice

- Master Plan / milestone contract: `none — qualified micro-fix under R6 + implementation/workstreams/issue-context-health-bounce/INTAKE.md`
- Requirements: `implementation/workstreams/issue-context-health-bounce/INTAKE.md`
- Accepted decisions: `none`
- Relevant OpenSpec: `none`
- Accepted dependency results: `none`

### Must preserve

- Context Health remains a qualitative safety mechanism rather than a token/turn/time/Card/milestone counter.
- Evaluation remains safe-boundary-only and must not interrupt active Cards, reviews, state transitions or in-flight external operations.
- Existing genuine hard-risk signals remain valid: materially superseded/contradictory transcript state, difficulty distinguishing durable truth from transient history, or substantial reconstruction burden that is already cleaner in durable state.
- Independent-review fresh-chat boundaries and other real stops retain priority over hygiene handoffs.
- Durable repository truth remains authoritative over stale chat narrative.
- No fixed numeric minimum/maximum session duration or work-count threshold is introduced.

### Must not / rationale that must travel

- Do not treat a role, milestone, phase, workstream or authority-area transition as a standalone trigger or standalone justification for `FRESH`.
- Do not allow a chat started from a context-hygiene handoff to bounce immediately to another hygiene handoff merely because the recovered obligation completed or the next obligation differs.
- Do not weaken Context Health so far that concrete harmful transcript degradation is ignored.

## Dependencies

- `none`

## Outcome

ChatGPT-only Context Health reacts to actual accumulated context degradation rather than normal workflow topology changes, preventing short-session fresh-chat bounce loops while retaining safe resets when concrete material context risk exists.

## Scope

### Included

- Tighten `workflow/chatgpt_only/ROUTER.md` trigger semantics.
- Tighten `workflow/chatgpt_only/CONTEXT_HEALTH.md` decision semantics and add explicit anti-bounce behavior.
- Update `docs/audits/CHATGPT_ONLY_CONTEXT_HEALTH_GATE.md` regression scenarios.
- Add a zero-dependency automated regression test for the durable contract text.

### Excluded

- Codex-only Context Health behavior.
- Independent-review fresh-chat policy.
- Fixed timers/token thresholds.
- Changes to execution policy, Task Board semantics, Definition/Planning authority or unrelated workstreams.

## Acceptance

1. Router text explicitly says ordinary role/milestone/phase/workstream/authority-area transitions are not by themselves a concrete Context Health trigger.
2. Router loads Context Health only on affirmative evidence of harmful accumulated context, not simply because the next authority/source area differs.
3. Context Health explicitly requires new concrete degradation in the current chat before a hygiene-started session may return `FRESH` at a later durable boundary.
4. If the exact next obligation/authority is deterministically recoverable from durable state and there is no affirmative evidence that the transcript is harmful, decision defaults to `CONTINUE`.
5. Existing hard-risk signals and safe-boundary protections remain present.
6. Audit scenarios cover the reported short recovered-session bounce and a legitimate later degradation case.
7. Automated regression test passes against repository state and detects reintroduction of transition-only trigger wording.

## Required tests / checks

- `python -m unittest tests/test_chatgpt_only_context_health_contract.py`
- Semantic readback of changed Router / Context Health / audit text.
- Repository-wide ChatGPT-only consistency scan for conflicting context-health trigger guidance.
- Diff-scope check: only this workstream state, the two workflow contracts, the context-health audit and the regression test may change behaviorally.

## External write/readback needs

`none`

## Independent review

`RECOMMENDED` — this changes normal ChatGPT workflow behavior and should receive a fresh independent semantic review before terminal completion.

## Contract overrides

None.
