# Project Workflow V2 activation evidence — PWv2.1 Policy Kernel

Date: 2026-09-23
Status: ACTIVATED

## Authorized scope

Only the existing workstream `change-pwv21-policy-kernel-brainstorming` in `elmakus/chatgpt-codex-project-workflow` was migrated.

Definition was explicitly excluded from migration authorization.

## Source and staging

- Frozen V1 live source: `work/pwv21-policy-kernel-brainstorming@e2dd13b6a92cf14233a81a08ee86bcd5f5d84244`
- Source tree: `dd60e09f400c4a8a42523145d1e363d4b644c61a`
- Staged V2 migration commit: `fd462d6e7a34fb312ccb044ff0d954433eeae52a`
- Staged tree: `691f993a45d0588dbe0f32a42d58163775373cb5`
- Staged commit is exactly one commit ahead of the frozen source with that source as merge base/direct parent.

## Activation

The live branch was non-force fast-forwarded to the exact staged commit.

Immediate readback verified:
- V2 `PROJECT.md` blob `636ccd7b3c889d341be2c6ac96c6a552c54ca0af`;
- V2 `WORKSTREAM.toml` blob `6509c1dc59c946d17e20bd1df0e3e87f4e6dbde6`;
- V2 `INTAKE.toml` blob `99aedd6290c1f2709071ac7b9d379b9657b94832`;
- V2 `BRAINSTORM.toml` blob `e49fca0f39092b6074a948d9347704a13c0bdeed`;
- original V1 `WORKSTREAM.yaml`, `INTAKE.md` and Brainstorming Markdown retain their source blob identities;
- consumer `main` remained `7aa7512ead67a86256089d1af0171e2e655e700d`;
- Project Workflow V2 authority remained current `main@986affffb7ba816e260e48549bf56e198ed51c21`, tree `d357b57059cc73770ca85340226272bae29b76c1`.

## Recovered semantic state

- Intake: complete
- Brainstorm subject: `pwv21-policy-kernel@1`
- Brainstorm state: `ready_for_definition`
- Challenge audit: GREEN
- Promotion state: pending
- Definition: absent
- Research: absent
- Planning: absent
- Task Board/implementation: absent

Under the current canonical V2 router, this state deterministically recovers to the real stop:

`stop / definition_promotion / pwv21-policy-kernel@1`

No Definition authority was created or inferred.
