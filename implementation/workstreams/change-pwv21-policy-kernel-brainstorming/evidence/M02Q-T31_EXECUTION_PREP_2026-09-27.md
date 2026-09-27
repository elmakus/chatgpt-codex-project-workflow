# M02Q-T31 Execution Prep — F03 historical JIT consumed-proof migration

## Trigger and predecessor

- Trigger: `after-M02Q-T30`.
- M02Q-T30 is DONE after fresh independent R01 GREEN.
- Exact dependency Result: `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/results/M02Q-T30.md@e05352154fb24448abd1b05f87ef91693a8e80f0:609c10f0beb9126f10b5c53de8676fbc0b6339c3`.
- RF014 semantic dependency Result: `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/results/M02Q-T20.md@af5dd7469c7ba9271b8b94101e159fb2489ca902:de4d4909d2f796a8c35a5d2a9b9df522abfd51f8`.
- Accepted product verifier/router: `elmakus/project_workflow_v2@a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f`.
- Immutable pre-migration consumer Board: `b4da01b7715cfa39743b7f35b6d05022ce0e5049:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/TASK_BOARD.toml@c388e19cacf687f3f02a143a7c17eb3c0a799db3`.
- Stable T31 Card: `2b43a0dbc1e5ce2bd5b9642ff5e65c7c011380ca:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/cards/M02Q-T31.md@06c59f9df110058a5efec44e9cb01adc119fe3ab`.

## Exact source inventory

Direct TOML readback of the source Board yields:

- total JIT triggers: 39;
- consumed triggers: 38;
- consumed triggers already carrying `consumed_proof`: 5;
- consumed triggers lacking proof: 33;
- one waiting trigger: `after-M02Q-T30`.

The exact 33 missing-proof set is:

- `after-M01-T01`;
- `after-M02-T01`;
- `after-M02R-T01` through `after-M02R-T12`;
- `after-M02Q-T01` through `after-M02Q-T19`.

The five existing proof-bearing triggers are `after-M02Q-T20`, `after-M02Q-T24`, `after-M02Q-T26`, `after-M02Q-T28`, and `after-M02Q-T29`; T31 must not alter them.

## Causal downstream mapping

The accepted RF014 verifier does not accept an arbitrary later Card. It requires the downstream Task Card to consume the predecessor's exact Result, unless another durable trigger-resolution/handoff binding exists. Direct immutable Task Card readback proves the exact mapping:

- `after-M01-T01 -> M02-T01`;
- `after-M02-T01 -> M02R-T01`;
- `after-M02R-T01 -> M02R-T02`, continuing one-by-one through `after-M02R-T12 -> M02R-T13`;
- `after-M02Q-T01 -> M02Q-T02`, continuing one-by-one through `after-M02Q-T19 -> M02Q-T20`.

All 33 downstream Task Cards declare the predecessor Result with the same exact path+commit+blob owned by the source Board. This was checked directly rather than inferred from Board ordering.

## Proof locator strategy

For the 33 historical downstream Cards, their current stable bytes are already present at the immutable source Board commit `b4da01b7715cfa39743b7f35b6d05022ce0e5049`. T31 may therefore use that one ancestor commit as the exact proof commit while preserving each Card's own exact blob:

| Downstream range | Exact current/source blob rule |
|---|---|
| `M02-T01` | `3e56fec00abd68fb51d464843983879aa0f4ffb4` |
| `M02R-T01..T13` | exact blobs from the source commit tree, each unchanged/current |
| `M02Q-T02..T20` | exact blobs from the source commit tree, each unchanged/current |

The full 33-blob mapping is mechanically derived from the source commit tree during implementation. Each proof path is exactly `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/cards/<downstream>.md`.

## Scope boundary

T31 owns only the append-only F03 proof migration. Historical trigger `id`, `after_card`, `state`, and `condition` remain byte-for-byte semantically unchanged apart from adding the nested proof table. Historical Task Card/Result/Review files are not rewritten.

The separately known legacy semicolon Evidence-refs/composed-final-serving defect remains outside T31. After T31 Card-level completion, a separate JIT obligation must own that correction before any fresh M02Q Milestone re-review; M03 remains blocked.
