# <CARD-ID> — <title>

- Milestone: `<MXX>`

> Stable Codex-only Task Card contract. Mutable execution/review/result/batch state belongs only to the selected manifest-bound workstream Task Board. Historical root/default `implementation/TASK_BOARD.yaml` is recovery/migration input only.

## Authority slice

- Master Plan / milestone: `<exact-ref>`
- Requirements: `<exact-ref(s)>`
- Accepted decisions: `<exact-ref(s)>`
- Relevant OpenSpec: `<exact-ref-or-none>`
- Accepted dependency results: `<exact-ref(s)-or-none>`

### Must preserve

- <implementation-shaping invariant>

## Dependencies

- <CARD-ID or none>

## Outcome

<bounded achieved state>

## Scope

### Included

- <work>

### Excluded

- <non-goal>

## Acceptance

- <testable acceptance>

## Required tests / checks

- <check>

## Parallel safety

```yaml
parallel_safe: false
write_scope: []
exclusive_resources: []
```

Leave `parallel_safe: false` unless current Card authority can bound every repository mutation and resource claim. These fields are JIT inputs only; Execution Prep must still prove current compatible eligibility before concurrency.

## External write/readback needs

<none or exact write/readback contract>

## Independent review

`REQUIRED | RECOMMENDED | none`

## Contract overrides

none
