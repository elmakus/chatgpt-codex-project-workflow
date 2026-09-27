# M02Q-T29 Execution Prep — M02Q milestone F02 product compatibility

## Trigger and boundary

- Consumed predecessor: M02Q-T28 is DONE with fresh independent GREEN review.
- Trigger: `after-M02Q-T28`.
- Originating blocker: `M02Q-MR01-F02` from `evidence/M02Q-MILESTONE-R01_2026-09-27.md`.
- F02 is semantically split at the same product/consumer boundary already used by T26→T27: T29 owns only the reusable fail-closed product compatibility contract; the exact four-record consumer migration remains allocated to a downstream JIT trigger.
- F03, milestone re-review and M03 remain separate.

## Exact predecessor/result readback

- M02Q-T28 Result: `results/M02Q-T28.md@a1e7d6fff98e3cc7efce0bc97ff284dce4adf937:187eb7e5a990d5bf2558b81fb39d4a47bbce0856`.
- RF004 exact Task-Card acceptance foundation: `results/M02Q-T13.md@05904ad28c7b551a4d8a635d90c6aece39c82705:cea61d48c3fe0f927a420fb96024b42a509c5120`.
- Existing legacy-Result compatibility baseline: `results/M02Q-T26.md@04226fefd1e9e8d8a36d7d3239cba4396d4f0e12:dbe627dfbe342c2887facd325ba6b02ab910ff0c`.
- Product branch readback: `elmakus/project_workflow_v2:work/pwv21-policy-kernel` is exactly `5e403db8f82e3fa7b8c7dc12bb1904ff441dcaa3`.

## Why a product contract is required

The accepted product candidate intentionally allows path-only Task Card acceptance only inside the explicitly proved statusless legacy-Result path. T09–T12 are structured current-success Results, so their terminal GREEN reviews cannot legally reuse that exception. The exact composed milestone readback therefore fails at T09 with “review acceptance requires exact commit + blob Task Card identity”.

The four historical Review files themselves must remain immutable. A new append-only Board proof must therefore bind the existing exact review-attempt locator to the exact Task Card bytes visible at that immutable review commit, and the product must verify that proof rather than rewriting acceptance fields or weakening RF004.

## Sizing / topology

T29 is one independently useful product invariant: a narrowly scoped compatibility verifier plus router/state composition for immutable historical structured-Result Review acceptance. The consumer inventory/mutation is independently implementable only after this product contract is GREEN and is allocated to `after-M02Q-T29`.

No F03 consumed-trigger migration, milestone review, or M03 work is included.
