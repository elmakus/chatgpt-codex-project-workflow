# V1 -> V2 workstream migration provenance

Status: LIVE / ACTIVATED

## Exact V1 source

- Repository: `elmakus/chatgpt-codex-project-workflow`
- Source branch: `work/pwv21-policy-kernel-brainstorming`
- Source commit: `e2dd13b6a92cf14233a81a08ee86bcd5f5d84244`
- Source tree: `dd60e09f400c4a8a42523145d1e363d4b644c61a`
- Integration target rollback/reference point: `main@7aa7512ead67a86256089d1af0171e2e655e700d`
- V1 `PROJECT.md` blob: `bf18884cd4e3746bb858ee0f86335e5fd1610b81`
- V1 `WORKSTREAM.yaml` blob: `c79b8ac9b2346dc8450ad13e9771f6018441da1f`
- V1 `INTAKE.md` blob: `f13fa2e93b9cc6996f91132e48535b3f90281bbd`
- Brainstorming evidence `brainstorming/PWV21_POLICY_KERNEL.md` blob: `2e35a3cc2aeeb8f1bd950de0e1da324615db99b2`

The immutable source commit remains the historical V1 state after activation.

## Reconstituted semantic boundary

The exact source establishes:

- Intake complete;
- exploratory scope `pwv21-policy-kernel@1`;
- Brainstorming `ready_for_definition`;
- completion/challenge audit GREEN;
- Definition promotion authorization pending;
- no active Research locator;
- no Definition;
- no accepted workstream requirements, decisions or plan;
- no Task Board, implementation state or workstream review obligation.

The V2 `challenge_audit = "green"` field is a schema-compatible representation of the completed source Brainstorming audit. It is not new product authority.

No exploratory content was promoted by this migration. The exact source Brainstorming Markdown/blob above remains semantic exploration evidence for later Definition if the user separately authorizes promotion.

## V2 package used for activation

- Authority repository: `elmakus/project_workflow_v2`
- Main commit at validation/activation: `986affffb7ba816e260e48549bf56e198ed51c21`
- Main tree at validation/activation: `d357b57059cc73770ca85340226272bae29b76c1`

Operational authority remains current `elmakus/project_workflow_v2@main`; these exact refs make the migration event auditable and are not an ongoing project pin.

## Activation

- Staging branch: `migration/pwv21-policy-kernel-pwv2-staging`
- Exact staged commit: `fd462d6e7a34fb312ccb044ff0d954433eeae52a`
- Exact staged tree: `691f993a45d0588dbe0f32a42d58163775373cb5`
- Staged commit direct parent: `e2dd13b6a92cf14233a81a08ee86bcd5f5d84244`
- Live branch activation: non-force fast-forward of `work/pwv21-policy-kernel-brainstorming` from `e2dd13b6a92cf14233a81a08ee86bcd5f5d84244` to `fd462d6e7a34fb312ccb044ff0d954433eeae52a`.
- Consumer integration target remained unchanged at `main@7aa7512ead67a86256089d1af0171e2e655e700d`.
- Immediate readback verified V2 PROJECT/WORKSTREAM/INTAKE/BRAINSTORM blobs and unchanged V1 evidence blobs.

## Live-owner boundary

The live workstream branch is now the sole mutable Project Workflow V2 owner for this workstream. The staging branch is migration evidence only and must not be treated as a second workflow owner.

Any reverse transition would require separate explicit verified migration handling; do not blindly roll back after V2 activation.
