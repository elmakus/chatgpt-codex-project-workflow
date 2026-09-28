# PWv2.2 preparation contract — identity, material inputs and publication

Status: bounded Execution Prep refinement of approved P2, not a native schema or a new workflow owner.
Applies only where a Card names this artifact. R7 and P2 prevail on conflict.
Authority: `requirements/PWV22_PROGRAM_R7.md` requirements 1, 3–13, 17, 28–40, 55–62, 72, 94; `planning/PWV22_PROGRAM_MASTER_PLAN_P2.md` §§2–4,6. Exact identities are repeated in each consuming Card.

## Known interface invariants

1. An accepted artifact identity is the tuple **repository, immutable commit, repository-relative path, Git blob**. A branch, URL, status, content digest alone or local file is insufficient. Prove both object existence/type and `commit:path == blob` in the declared repository. Verify the commit is reachable from the canonical published ref used for acceptance. Prove current bytes as well if the serving operation reads a worktree. A valid object in the wrong repository does not satisfy the tuple.
2. Reject missing/dangling/non-blob identities, path traversal/aliasing and escaped rooted reads. Donor path-hardening APIs are candidates, not automatic native compatibility. Malformed/legacy/unbound/unsupported input produces no canonical write. Do not infer a native epoch from directory names or convert legacy state during routing.
3. A consumed dependency names an exact accepted predecessor Result, its authority/property/material inputs, and any required constituent verdict. DONE is not proof. Multi-input consumption also needs explicit compatibility of the exact composed set/subject. A changed sibling set invalidates that compatibility assertion, not every unrelated Result.
4. Only inputs that actually determine legality/output/acceptance participate in freshness. Runtime metadata and unrelated changes cannot invalidate or authorize work. An unchanged implementation under native revalidation keeps its Result identity; append new exact acceptance evidence. Actual changed/re-executed output yields a new Result, preserving history.
5. Obligation/Result interchange is typed JSON and runtime-neutral. Distinguish input subject, implementation subject, Result artifact and acceptance evidence. Runtime correlation may exist outside semantic state. A boolean success, shape-valid payload or claimed hash does not prove tests, authority, publication or readback.
6. Official provenance is resolved before ordinary native routing; one applicable epoch per active lineage. Candidate fixture trust is isolated from official admission. No mixed-epoch mode, legacy migration, self-adoption or downgrade is authorized.

## Guarded Git publication transaction

Read exact remote old ref and material inputs -> assemble isolated candidate -> validate complete cross-file state and allowed diff -> commit candidate -> re-read target/guard against expected old -> publish one atomic ref transition -> fetch/read back target commit/tree/artifact blobs -> reconcile only the mechanically implied state.

A race before publication rejects the stale write and causes refetch/re-evaluation. Local commit creation is not acceptance. Multi-file transitions must not expose half a Board/Card/Result/Review update. After a lost response, observe target before retrying; if the exact intended commit is already published, recover without replay. Unexpected/ambiguous state is Recovery, not force-overwrite. A fast-forward push from the verified head can be additionally guarded by an explicit expected-old lease; never use a lease to discard other history.

Write scope is per exact obligation: producer implementation, independent Review attempt/evidence, deterministic finalizer, integration mutator and effect owner are distinct. Verify the entire diff, not just an allowlisted new file; deletions/renames/symlink changes count. No reviewer implementation mutation or pre-verdict author contact can be accepted through a narrow publication gate.

## External-effect companion contract

Git publication does not undo deployment/API/message/database effects. Before any such effect, bind obligation, authorized target/operation, expected prior state, allowed effect envelope and non-secret operation/request ID when available. Persist intent -> attempt -> target readback -> known outcome. Uncertain response or conflicting evidence is UNKNOWN; no blind retry or worktree deletion can erase it. Readback must distinguish expected effect, no effect, unexpected effect and uncertainty. Credentials, tokens and pairing material are never evidence artifacts.

## Current-governor preparation representation

This consumer still uses current V2, not the candidate native schema:

- Board statuses/revision, Card Markdown fields and `waiting -> satisfied -> consumed` triggers use the current governor.
- In a materialized **planned** Card, `Dependencies: none` means **no accepted predecessor Results exist yet**, not that required future predecessors are waived. Its Launch bindings section enumerates the exact producer seams and acceptance gates. It is non-executable until Execution Prep replaces `none` with every accepted `result-path@commit:blob`, verifies the DONE Board bindings, and refreshes/publishes/read-backs the unstarted contract under expected-old protection.
- Binding an already specified input to a later immutable Result is bounded refinement, not JIT decomposition. It must not change scope, acceptance, review or effect envelope. Such Cards are real stable contracts, not placeholders.
- If the actual future Result changes substantive interface, scope, dependency identity choice or write/effect surface beyond that envelope, do not launch by filling hashes. Reclassify in Execution Prep or return to Research/Planning/Definition as appropriate.
- READY Cards in this prepared snapshot have no predecessor Results and require none. They consume exact accepted authority (and, for donor qualification, already published external donor evidence). External donor evidence is not a fictitious same-Board DONE predecessor.
- A trigger's `after_card` is an existing ancestor anchor required by the current schema, never a substitute for **all** facts in its condition. Re-anchor to actual producing Cards as they materialize; satisfy only after the full condition and required reviews are read back. Never create placeholder producer Cards to satisfy the schema.

## Required falsification families for consuming Cards

Wrong repository; right path/wrong blob; same-path changed bytes; nonexistent commit; directory instead of blob; traversal/backslash/symlink escape; local-only Result; remote move between fetch and push; two writers from one old revision; crash before commit/before push/after push-before-notification; unrelated input change versus materially changed input; DONE without Result; valid Result with stale constituent Review; changed sibling set with old compatibility; unknown effect before cleanup; unchanged implementation revalidated without new Result; historical state rejected byte-identically.

## Deliberately not fixed here

Native owner filenames, complete JSON field names/enums, schema version, rule registry architecture, hash algorithm beyond existing Git object identity, helper language/APIs, package inventory and release target are S01/S03/S04/S05 or later outputs. Do not present donor `PWV21-K*`, `pwv2_execution_*`, registry schema version 1, legacy result derivation or tracker APIs as native law. The invariants above constrain those choices without manufacturing their future accepted Results.
