# Acceptance Evidence — <card or milestone>

> Create this standalone artifact only when durable evidence needs more than Task Board `tests_summary` + exact result pointers. It is expected for integrated milestone acceptance, REQUIRED/RECOMMENDED independent review, baseline/authorized exceptions, material external writes/readback, complex multi-stage verification, or an explicit contract requirement.

- Date: `<YYYY-MM-DD>`
- Subject: `<MXX-TYY | MXX>`
- Executor: `<chatgpt | codex | mixed milestone>`
- Branch: `<branch>`
- Tested HEAD: `<sha>`
- Result: `GREEN | RED | ACCEPTED_BASELINE_EXCEPTION`
- Authority slice reviewed: `<exact refs>`

## Acceptance criteria checked

| Criterion | Result | Evidence |
|---|---|---|
| ... | pass/fail | ... |

## Exact tests / checks

| Command / review | Result | Notes |
|---|---|---|
| ... | ... | ... |

## Authority preservation / deviations

- Applicable must-preserve constraints satisfied: ...
- Material deviation/conflicting evidence: `none | ...`

## OpenSpec verification

`none` or exact verification.

## External writes / readback / reconciliation

`none` or exact write target, readback method and verified state.

## Independent review

`required/recommended/optional`, reviewer/session evidence and result where applicable.

## Known exceptions

...

## Conclusion

...
