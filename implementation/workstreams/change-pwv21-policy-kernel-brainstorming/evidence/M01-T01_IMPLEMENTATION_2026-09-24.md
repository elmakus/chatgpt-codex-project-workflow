# M01-T01 implementation evidence — PWv2.1 policy kernel core

Date: 2026-09-24
Card: `M01-T01`
Target repository: `elmakus/project_workflow_v2`
Target branch: `work/pwv21-policy-kernel`
Exact implementation commit:
`17b9cda3f50f0873b96ddbc8fea4ffc4941f2b93`
Baseline:
`986affffb7ba816e260e48549bf56e198ed51c21`

## Implemented bounded M01 surface

The exact target commit adds and integrates the M01 mechanical-policy kernel
without implementing M02-M07 semantics.

Changed surface from the exact baseline:

- `policy/mechanical_policy.json`
- `schemas/POLICY_REGISTRY.schema.json`
- `scripts/test-policy-kernel.sh`
- `scripts/test.sh`
- `tests/test_policy_kernel.py`
- `tests/test_router.py`
- `tools/policy_kernel.py`
- `tools/router.py`
- `workflow/POLICY_KERNEL.md`
- `workflow/ROUTER.md`

The branch is 6 commits ahead and 0 behind its exact baseline; the final
implementation subject is the single exact commit above.

## M01 acceptance readback

- Registry is versioned and deliberately small: fixed named predicates,
  exact canonical input paths, precedence metadata, fixed outcomes, and
  semantic projection text; it is not an arbitrary-expression DSL.
- Registry/schema/rule/outcome shapes are closed and unknown vocabulary or
  unsupported versions fail closed.
- Registry and implementation predicate vocabularies must match exactly.
- Kernel extracts only declared canonical inputs, is stateless/read-only,
  and repeated evaluation over the same inputs is deterministic.
- `workflow/POLICY_KERNEL.md` is generated from the registry and exact
  projection drift fails closed.
- Registered predicates are wired into the existing production router rather
  than creating a second routing engine; unregistered semantic routing stays
  owned by existing workflow modules/router logic.
- Typed Obligation compilation, Result validation and reconciliation seams
  are explicitly present but reject use until M02 instead of being
  implemented early.
- Existing progressive-disclosure tests were updated only for the two small
  checked package artifacts loaded after exact workstream selection.

Exact readback blobs at the implementation commit include:

- `tools/policy_kernel.py@776c9f7f891e128d41d09631606414b2e9b442ec`
- `policy/mechanical_policy.json@29dd21950c70f9515e216e3d2e7900268c5c31dd`
- `workflow/POLICY_KERNEL.md@cc4caea401c1efba6ae0c5521f0661c4a943eaea`
- `schemas/POLICY_REGISTRY.schema.json@7e01f80667e27dcbfeb89d16bfaa83878ddbf335`
- `tools/router.py@a41911664a793f3b0fca6ebfd687bf2b4a34a3b9`
- `tests/test_policy_kernel.py@216fd5d65a2662bac2583dce3d39536b562c743c`

## Verification

GitHub Actions workflow `test`, run #340 / ID `35933206958`, for exact
head SHA `17b9cda3f50f0873b96ddbc8fea4ffc4941f2b93` completed with conclusion
`success`.

The `Run repository checks` step completed successfully. It executes
`sh scripts/test.sh`, which includes the new policy-kernel checks plus the
existing state, router, execution, review, recovery, close, delivery,
migration, unittest-discovery, Python compile, diff-check and repository
cleanliness gates.

Implementation evidence is GREEN. Formal independent Card review remains
required by the Card contract and is not satisfied by this implementation
evidence.
