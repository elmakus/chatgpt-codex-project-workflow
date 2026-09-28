# M02-S08-T01-R05 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@2210767ae5cefdf8d9a6fd98b22d868f4f26b04a:25434a4a266b2a889354866f43c33e0bb74e5af4`

Exact implementation subject: `elmakus/project_workflow_v2@d27ad6bec471cca1cf1923f51ee5f632f9e9d6a8`; `tools/pwv22_parallel.py` blob `9a1118f133acf2b78777b65372a8ca48b4a91ed0`; `tests/test_pwv22_parallel.py` blob `fcc0f96bc3af7701c2c020aa4750eb3e5ff19d21`.

## Finding

The R04 repair correctly stops consuming caller-provided admission membership/revocation material, but its replacement exact-binding contract is not realizable by a normal Git artifact.

`accepted_admission()` reads an admission artifact by `admission_ref`, parses that artifact, and then requires `a["subject"] == admission_ref`. The exact identity includes repository, commit, path and the artifact's own Git blob SHA. Therefore the serialized admission artifact must contain its own final blob SHA while that embedded SHA itself contributes to the bytes whose SHA Git computes. It also embeds the commit containing that blob, creating the same circular publication problem at commit level.

The focused tests do not construct or read a real Git admission artifact. `DURABLE_ADMISSIONS` instead maps the synthetic identity `ADM` to an in-memory `admission()` object that already contains the same synthetic `ADM`, so the circularity is hidden by the fixture.

As a result, the Card's explicit finite exact admission cannot be durably instantiated under the implementation's own contract, so the acceptance property is not satisfied despite closing the R04 spoofing path.

## Required correction

Bind admission semantics to immutable durable bytes without requiring the artifact to contain its own Git identity. For example, let the external exact artifact locator identify/read the admission payload, while the payload contains the finite admission ID/cards/revocations and any non-self-referential subject needed by the accepted design; bind the GREEN acceptance artifact to that external exact locator (or to a separately hashable semantic subject), not to a self-referential locator embedded in the same bytes.

Add a test that creates/reads an actually hashable immutable admission payload and proves the exact locator binds those bytes, while fabricated membership/revocation and stale/non-durable acceptance still fail closed. Preserve the R03/R04 protections, conservative conflict serialization, one-mutator enforcement, exact ordered sibling Results and compatibility rejection.
