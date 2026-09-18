# MXX-TYY — <title>

- Milestone: `MXX`

> This file is a stable Task Card contract. Mutable execution/review/result state lives only in `implementation/TASK_BOARD.yaml`.

## Authority slice

- Master Plan / milestone contract: `<exact section/path>`
- Requirements: `<IDs/paths>`
- Accepted decisions: `<IDs/paths>`
- Relevant OpenSpec: `<path | none>`
- Accepted dependency results: `<refs | none>`

If this Card was created JIT from predecessor evidence, include that exact accepted result in the Authority slice. Do not create the Card before its scope is sufficiently knowable.

### Must preserve

List every applicable invariant, accepted behavior/architecture choice, failure semantic, compatibility rule, external-write boundary or other constraint that can change implementation or acceptance.

### Must not / rationale that must travel

Include only when omission could reasonably cause a different implementation choice.

Delegation may reduce context volume, not authoritative constraints. A downstream executor/reviewer must either receive every applicable constraint explicitly or read the exact referenced authority before acting. Summary text never overrides exact authority.

## Dependencies

- `<MXX-T.. | predecessor result | none>`

## Outcome

...

## Scope

### Included

...

### Excluded

...

## Acceptance

...

## Required tests / checks

...

## Optional execution hints

- Priority: `HIGH | MEDIUM | LOW`
- Complexity: `HIGH | MEDIUM | LOW`
- Phase: `<phase>`
- Expected/relevant code locations:
  - `<path>`

Delete optional fields that add no value.

## External write/readback needs

`none` or exact target + required persisted-state verification.

## Independent review

`REQUIRED | RECOMMENDED | OPTIONAL` plus rationale when material.

## Contract overrides

Record only card-specific overrides to workflow-standard execution/blocker/evidence/DoD rules. Do not copy standard workflow text.
