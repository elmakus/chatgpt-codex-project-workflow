# M02-T01 Independent Review — Attempt 1

Card: `M02-T01`
Verdict: `RED`
Reviewed subject: `1a8b2c358abc18d69d045c0b73d4a74c27c9baae`
Implementation base inspected: `02945ab80110e743566a1dbf9e6309368a2f9c05`
Workflow-main baseline verified: `03035876f3283d33e8a10ff43265f5be21a27a06`

## Authority checked

- `implementation/cards/M02-T01.md`
- `planning/CHATGPT_ONLY_MULTI_WORKSTREAM_MASTER_PLAN.md#M02--intake-route-issue--feature`
- requirements R2, R4, R5, R7, R11, R12, R13, R14 and R15
- accepted `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
- accepted M01 dependency handoff + GREEN review
- implementation evidence `implementation/evidence/M02-T01.md`
- exact four-file implementation range `02945ab8...1a8b2c35`

## Independent checks

- verified current workflow `main` still equals the implementation baseline recorded by M02 evidence;
- inspected the complete M02 range, which changes only `INTAKE.md`, `ROUTER.md`, `WORKSTREAMS.md` and `WORKSTREAM_TEMPLATE.yaml`;
- traced explicit `#issue` / `#feature` precedence before unrelated Task Board review/execution state;
- traced ordinary no-marker fallback and active-intake recovery before Task Board interpretation;
- checked branch/workstream identity, collision handling, default-vs-stacked parent criteria, feature promotion-gate preservation, manifest/Task Board ownership boundaries and foreign-policy isolation;
- GitHub reports no combined status checks and no pull-request workflow runs for the frozen subject, so this review makes no CI-execution claim.

## Blocking finding M02-REV-01 — issue diagnosis ordering is internally contradictory

The accepted M02 authority requires issue intake to be diagnostic/reproduction-first when practical before base/dependency selection. Requirement R4 orders problem establishment before base selection, and the approved M02 plan explicitly calls for `diagnostic/reproduction-first when practical`.

The frozen `workflow/chatgpt_only/INTAKE.md` does not deterministically preserve that order:

- `Common intake flow` step 4 chooses the exact integration target/base;
- step 6 creates the branch;
- only step 8 enters the route-specific intake;
- then `Issue intake` step 1 establishes/reproduces the problem, step 2 discovers dependency evidence, and step 3 selects the base again.

A conforming executor can therefore follow the common numbered flow literally and choose/create the issue workstream from a base before the issue-specific diagnostic evidence that is supposed to justify independent-versus-stacked selection. The later issue-specific list then repeats base/workstream selection after those actions have already happened.

This contradicts the implementation evidence claim that M02 is diagnosis/reproduction-first and leaves two incompatible orderings in the canonical intake contract.

## Required bounded remediation

Make the common/issue flow unambiguous so that for `#issue`:
1. establish/reproduce the problem when practical;
2. discover the dependency evidence needed for classification;
3. select independent versus stacked base;
4. only then create/recover the workstream branch + durable active intake state;
5. continue classification/materialization.

Feature intake may keep its own discovery-before-base ordering. Avoid duplicating two numbered flows that can be followed in conflicting sequences.

No accepted requirement, ADR, milestone strategy or user authority needs to change; this is a bounded L1/L2 contract correction inside M02-T01 scope.

## Verdict

RED.

The exact subject is rejected until the ordering ambiguity above is corrected and the corrected subject is frozen for a fresh independent re-review.
