# CUBC-M01 Milestone Acceptance — Terminal-unmerged Codex-only branch cleanup

Milestone: `CUBC-M01`
Result: `GREEN`
Accepted implementation subject: `4ead7a4a7c0ed13bc82a504a8b038dc20b788217`
Independent Card review: GREEN — `implementation/evidence/CUBC-M01-T01-review-01.md`
Integrated PR: #35
Merge commit: `3062786dea216296672bc059bbdc58320b6434cb`

## Integrated acceptance

Verified against the approved CUBC-M01 milestone contract, CUBC-M01-T01 Card contract, CUBC-REQ-001 through CUBC-REQ-008, the accepted terminal-unmerged branch-delete ADR, approved plan revision `CUBC-P1`, implementation evidence and the exact independent GREEN review.

GREEN:

- intentional terminal-unmerged Codex-only workstreams cannot delete their source branch while a live Card, Research, review, stacked dependency, integration or other branch-requiring obligation remains;
- terminal closure/history must be durable independently of the source ref before deletion, without integrating rejected/superseded implementation content merely to preserve history;
- the only cleanup target is the exact manifest-owned `WORKSTREAM.yaml.branch`;
- Codex Main owns the physical delete through authenticated `gh` after the safety and durability gates are GREEN;
- Recovery is idempotent: a surviving exact branch is deleted and read back absent; an already-absent exact branch is cleanup-complete and is never recreated;
- no `branch_cleanup`, `safe_to_delete`, cleanup registry, alias-ref lifecycle, CAS/lease state, schema extension or runtime worker/session authority was introduced;
- normal merged-workstream cleanup remains repository-owned automatic deletion with no new Codex-only fallback lifecycle;
- target-side terminal history preserves original manifest/Task Board branch provenance after source deletion.

## Verification and publication state

- The exact implementation subject passed REQUIRED independent review while current workflow `main` was `19f047f5a784a54abbaac1552b036e996b255f2a`; the subject was 0 commits behind that target.
- Commits after the reviewed subject and before merge changed only Task Board/review evidence and PR-binding bookkeeping; no workflow-contract behavior changed after GREEN.
- PR #35 was re-read before merge, was non-draft and mergeable against the same `main`; the feature branch remained 0 commits behind.
- GitHub reported no combined status checks for the exact reviewed subject or final pre-merge head; no CI-execution claim is made.
- PR #35 merged successfully as `3062786dea216296672bc059bbdc58320b6434cb`.
- Target-side readback confirmed PR #35 is closed/merged and the integrated Task Board/review evidence are present on `main`.
- Repository automatic merged-branch cleanup removed `feat/codex-only-unmerged-branch-cleanup` after merge; no Codex-only fallback deletion was used.

## Result

CUBC-M01 is GREEN and the approved `CUBC-P1` implementation scope is integrated into `main`. Remaining writes are closure-only durable state/index reconciliation and do not alter the independently reviewed workflow behavior.
