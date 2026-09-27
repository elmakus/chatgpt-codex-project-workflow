# M02Q-T28 Execution Prep — milestone RED F01 orphan T23 Board audit

M02Q-MILESTONE-R01 is terminal RED and identifies F01 as a current-state referential-integrity defect: the mutable Task Board still carries sizing/topology audit state bound to M02Q-T23 even though T23 was deliberately returned by late-oversize handling and is not a live Card.

Recovery classification is bounded correction inside accepted P7 authority. The correction does not change milestone strategy, product authority, or the immutable T23 Card/evidence history.

This Card removes only the orphan live Board audit state. F02 structured T09-T12 acceptance migration and F03 historical consumed-trigger proof migration remain separate downstream corrections. M03 stays blocked.

Topology is simple: one Board referential-integrity invariant, no cross-RF merge, no historical rewrite, and one independently falsifiable outcome.
