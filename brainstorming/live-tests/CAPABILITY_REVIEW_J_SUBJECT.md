# Capability-first Review live-test subject J

Status: approved synthetic review authority

## Exact implementation subject

Canonical result commit:
`a23712266f36ae70cda129a9b3242c6391b50b49`

Reviewed path:
`brainstorming/live-tests/review-j/result.txt`

Required exact content:
`review-j: accepted\n`

## Review acceptance

GREEN only if:
- the exact reviewed artifact at the exact canonical result commit matches the required content;
- no reviewed subject mutation occurs during review;
- independence from the producing realization/context is verified semantically;
- concise durable verdict evidence is produced.

RED if any of those conditions fails.

## Finalization acceptance

After a durable GREEN attempt:
- implementation must not be replayed;
- review must not be replayed;
- Card may become done only if its current canonical result still exactly equals the GREEN subject.
