# MF-T01 implementation evidence — 2026-09-20

## Subject

Behavioral implementation subject:

- base: `main@808084a4c7989715f7ee4889a31bce28f778d597`
- implementation head: `e0d4beebb466f70e87ad0d4f2aa209c80e55f74f`
- branch: `fix/chatgpt-only-context-health-bounce`

The behavioral subject includes:

- `workflow/chatgpt_only/ROUTER.md`
- `workflow/chatgpt_only/CONTEXT_HEALTH.md`
- `docs/audits/CHATGPT_ONLY_CONTEXT_HEALTH_GATE.md`
- `tests/test_chatgpt_only_context_health_contract.py`

Workstream Intake/Card/Task Board/manifest files are durable workflow state, not additional product behavior.

## Implemented behavior

- Removed ordinary role/authority-area change as a standalone Router trigger example.
- Router now requires affirmative harmful-context evidence before loading Context Health.
- A role, milestone, phase, workstream or authority-area transition is explicitly non-signal by itself.
- A chat started from a context-hygiene handoff requires new concrete degradation accumulated after recovery before another hygiene-trigger can be considered.
- Context Health now defaults to `CONTINUE` when the exact next obligation/authority is deterministically recoverable and there is no affirmative evidence that the transcript is harmful.
- Existing strong stale/superseded-state and authority-confusion signals remain.
- Regression audit now covers the reported short-session fresh-handoff bounce and preserves provenance of the original independent gate audit.

## Verification

### Exact branch readback assertions

PASS — 11/11 exact assertions against branch files through GitHub readback:

1. Router contains explicit transition-non-signal rule.
2. Old `major role/authority-area transition` trigger wording is absent.
3. Router contains affirmative harmful-context default.
4. Context Health contains deterministic-durable-state → `CONTINUE` rule.
5. Old different-authority soft-signal wording is absent.
6. Fresh-handoff anti-bounce section exists.
7. Strong hard-risk signals remain present.
8. Audit contains short-recovery anti-bounce scenario.
9. Audit says authority/source-area difference alone continues.
10. Audit explicitly does not self-issue the current independent verdict.
11. Python unittest regression artifact exists.

### Repository-wide ChatGPT-only consistency scan

PASS — no occurrence of either removed transition-only trigger formulation across `workflow/chatgpt_only/*.md`:

- `major role/authority-area transition`
- `the next obligation uses a substantially different authority/source area than the work just completed`

### Python regression harness

PASS — `tests/test_chatgpt_only_context_health_contract.py` contains 6 unittest cases. The native Python harness ran all 6 cases successfully against the same contract snippets asserted from the exact branch state:

```text
Ran 6 tests in 0.000s
OK
```

The native container could not clone GitHub directly because outbound DNS to `github.com` was unavailable. Therefore the exact branch was verified through GitHub connector readback, while the Python harness execution used the read-back contract snippets. This limitation is explicit rather than represented as a full checkout execution.

### Diff-scope readback

PASS — `main...fix/chatgpt-only-context-health-bounce` is ahead from the exact base with no behind commits at implementation freeze. Behavioral changes are limited to the two ChatGPT-only context-health contracts, their regression audit and the new regression test; remaining changed paths are namespaced workstream state.

## External writes

None.

## Review boundary

MF-T01 is behavior-changing workflow policy text and carries `RECOMMENDED` independent review. The implementing chat must freeze this exact subject and hand it to a fresh reviewer before terminal Card completion.
