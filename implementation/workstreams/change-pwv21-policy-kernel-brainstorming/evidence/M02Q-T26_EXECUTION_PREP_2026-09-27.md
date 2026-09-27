# M02Q-T26 Execution Prep — OBL-M02Q-03 legacy Result compatibility

Current durable consumer state after M02Q-T25 R02 GREEN and post-review/JIT reconciliation reaches canonical Recovery at DONE M01-T01 because its immutable historical Result predates structured `Result status: success`. This is the exact durable OBL-M02Q-03 recorded before Milestone Review.

Fresh inventory on the current consumer Board finds 23 DONE Result artifacts without structured status. All 23 retain terminal GREEN review history; two legacy Results (M02R-T01 and M02R-T02) also use semicolon-separated evidence references that the current parser treats as one dangling path. Rewriting terminal Result bytes is forbidden by OBL-M02Q-03 and REQ-098/100/101.

Execution Prep splits the obligation into two independently falsifiable outcomes. M02Q-T26 owns the reusable product compatibility/provenance mechanism and its regression surface. The consumer-side 23-record append-only migration is retained on `after-M02Q-T26` and will be materialized only after T26 is DONE/GREEN. This permits the mechanism to be independently reviewed before it is used to mutate consumer state.

The mechanism must remain explicit and fail-closed: no success inference from result prose, no broad acceptance of statusless current Results, and no weakening of RF001. Existing exact GREEN Review binding remains the acceptance proof; the new migration record only proves that the statusless serialization is genuinely historical and immutable. M03 remains unmaterialized.
