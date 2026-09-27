# M02Q-T24 Execution Prep — residual RF006 compatibility

T23's durable pending late-oversize return preserves 42/48 Review identity records and exposes two separable residual outcomes. Execution Prep keeps them split:

1. `rf006-legacy-full-attempt-id-compatibility` — product-side RF006 correction, owned by M02Q-T24.
2. `rf006-consumer-review-identity-completion` — consumer Board exact-locator completion after T24, allocated to `after-M02Q-T24`.

The first outcome can be GREEN and independently useful while the consumer completion remains RED, so one combined Card would violate semantic right-sizing. T24 contains one RF006 compatibility invariant only. The split preserves the P7 RF006 seam, adds no cross-RF merger, does not absorb Milestone Review and does not materialize M03.

Topology risk for T24 is simple: the residual anchor sizing audit explicitly allocates the second outcome to a real downstream JIT, leaving only one invariant family in T24. No fresh topology challenge is required.

Launch authority is exact T11/T12 RF006 results plus the durable T23 late-oversize evidence. Product baseline is `ae3d2d303fde8ee67dcfa24342549e96c0cf1d13`.
