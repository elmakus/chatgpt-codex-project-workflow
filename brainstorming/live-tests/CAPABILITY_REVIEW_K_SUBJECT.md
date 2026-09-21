# Capability-first Review live-test subject K

Status: approved synthetic review/correction authority

## S1 — intentionally defective subject

Canonical result commit:
`f72d08ae5d4aa8faf06dcedb586bc1618887200c`

Reviewed path:
`brainstorming/live-tests/review-k/result.txt`

Current S1 content:
`review-k: BAD\n`

Accepted requirement:
`review-k: GOOD\n`

R01 MUST therefore be RED if it correctly reviews S1.

## Authorized bounded correction

After durable R01 RED, correction is authorized to change only:

`brainstorming/live-tests/review-k/result.txt`

to exact content:

`review-k: GOOD\n`

The correction produces a new exact canonical subject S2.

## R02 acceptance

R02 reviews only S2.

GREEN only if:
- S2 has exact accepted content;
- R01 remains immutable RED with its original S1 subject/evidence;
- R02 is a distinct appended attempt with a new immutable subject;
- the realization reviewing R02 is independent from the realization/context that produced S2;
- no subject mutation occurs during review.

## Final state

After R02 GREEN:
- Card remains eligible for deterministic finalization against S2;
- prior R01 history must remain addressable and unchanged.
