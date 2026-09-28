# PWv2.2 typed Obligation/Result and material-input specification — M01-S01-T02

## Separation of subjects

| Subject | Required semantic content | Excluded |
|---|---|---|
| Obligation | type/version, exact owner/operation, authority refs, material inputs, acceptance identity, allowed write/effect envelope | model/provider/session/worker IDs as legality |
| Implementation subject | exact repository+commit plus bounded changed paths/blobs | acceptance verdict |
| Result | Card/obligation identity, immutable implementation subject, evidence refs, output/material facts | mutable status, self commit hash |
| Acceptance evidence | exact subject, acceptance contract, verdict/proof, independence where Review applies | implementation mutation or downstream choice |
| Runtime correlation | optional assignment/run/workspace/message data outside semantic state | freshness, routing, acceptance |

Portable interchange is typed JSON. Native field spelling/schema version is an implementation choice, but validation MUST reject unknown required discriminants, wrong primitive/container types and missing required exact identities before any canonical write.

## Exact artifact and dependency identity

An accepted artifact reference is `repository + immutable commit + repository-relative path + Git blob`. Validation proves repository identity, commit existence/reachability, object type=blob, `commit:path == blob`, rooted path safety and serving bytes when a worktree supplies bytes. Branch/URL/content digest/local file alone is insufficient.

An accepted dependency binds the exact predecessor Result artifact plus the exact authority/material properties it supplies and every required constituent verdict. DONE alone is insufficient. Multi-input consumption additionally binds compatibility of the exact Result set/order/subject.

## Material-input projection and freshness

Only inputs that determined legality/output/acceptance enter the material projection. Runtime correlation and unrelated repository changes are excluded.

Worked cases:
- Change an unrelated documentation blob: material projection unchanged → Result remains fresh.
- Change a consumed predecessor Result blob at the same path: exact identity differs → affected dependency is stale; unrelated Results remain valid.
- Change the sibling Result set after compatibility evidence: compatibility becomes stale for that composition only.
- Native policy update with unchanged implementation and a `revalidate` disposition: preserve Result identity and append exact revalidation evidence.
- Genuine re-execution or materially changed output: append a new immutable Result; never rewrite the prior Result.

Unknown dependency/property impact fails closed to Recovery or a sufficient larger revalidation; absence of a known edge is not proof of independence.

## Admission and validation failures — all no-write

| Failure | Required outcome |
|---|---|
| malformed JSON / wrong type / missing discriminator | reject before mutation |
| wrong repository | reject even if commit/path/blob exists elsewhere |
| nonexistent/unreachable commit | reject |
| path absent, traversal/alias/root escape, directory/non-blob | reject |
| right path + wrong blob / changed serving bytes | reject |
| predecessor DONE without exact accepted Result | dependency unsatisfied |
| required Review missing/stale/RED | dependency unsatisfied |
| unsupported/unbound/ambiguous native epoch | fail closed; no native routing |
| historical/legacy state | reject or route outside native semantics byte-identically; no normalization |
| runtime metadata changed | semantic legality/freshness unchanged |
| old compatibility + changed sibling set | reject composed consumption only |
| local-only implementation/Result | not accepted continuation truth |
| stale expected-old on publication | reject write, refetch/re-evaluate |
| uncertain external effect | UNKNOWN; no blind retry |

## Guarded publication

Read exact remote old ref/material inputs → assemble isolated candidate → validate complete diff/cross-file state → commit candidate → re-read target and compare expected-old → atomic Git ref transition → fetch/read back target commit/tree/artifact blobs → reconcile only the mechanically implied semantic state.

A race rejects the stale write. A lost response is resolved by target readback before retry. Local commit/hash construction never proves remote publication. Result content never embeds its own publishing commit hash; the coordinator binds Result path+commit+blob externally after publication.

## External effects

Before a non-Git effect, bind exact obligation, authorized target/operation, expected prior state, allowed effect envelope and stable non-secret request/idempotency ID where supported. Persist intent → attempt → target readback → known outcome. Unknown response remains UNKNOWN. Credentials/tokens/OTP never enter semantic evidence.

## Positive envelopes

Minimal semantic Obligation example:
```json
{"type":"execution_obligation","owner":"execution","authority":[{"repository":"R","commit":"40hex","path":"p","blob":"40hex"}],"material_inputs":[],"acceptance":{"kind":"task_card","id":"C"}}
```
This is illustrative field rationale, not a frozen native schema.

Minimal semantic Result example:
```json
{"type":"execution_result","card_id":"C","implementation":{"repository":"R","commit":"40hex"},"evidence":["workstream/evidence/e.md"],"outputs":[{"path":"o","blob":"40hex"}]}
```
Acceptance and publication identity are bound externally; runtime correlation is absent.

## Interface facts required downstream

S05 must expose exact locator/admission and guarded Git publication primitives without legacy normalization. S07 must expose immutable Result/dependency/material projection and revalidation evidence. S08 consumes exact material/write/effect claims for admission/fan-in. S09 binds Review attempts to exact immutable subjects and acceptance identities. Representation choices may change during bounded Prep only if these semantics remain intact.

## H01/H02 disposition

H01 is not assumed: exact-locator donor code is only a candidate; later reuse requires repository/path/object/serving-byte and import-graph verification. H02 is not assumed: no PWV21 kinds/rule IDs/schema registry or legacy reconcile defaults are imported. If reuse fails, implement the smallest native exact reader and retain the adversarial cases.
