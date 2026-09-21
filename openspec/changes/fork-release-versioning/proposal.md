# Proposal — fork release versioning

## Why

Project Workflow currently verifies publication state without a canonical rule for release versions of downstream forks. Fork-local releases can therefore consume upstream-looking versions and obscure the exact upstream baseline.

## Change

Introduce one policy-neutral downstream-fork release-lineage contract using `v<upstream-version>-private.<N>`, require exact upstream repo/tag/SHA provenance, preserve legacy releases, select the private lane explicitly, and make every supported publication route defer to that common contract.

The contract is implemented by `M01-T01` under approved `FRV-P2`.

## Non-goals

- no historical retagging/deletion or release rewriting;
- no automatic upstream synchronization;
- no change to publication authorization/signing/checksum gates;
- no use of `private` as release-quality metadata;
- no change to this repository's independent-project auto-patch tag workflow merely because it increments ordinary SemVer;
- no runtime parser/state service unless existing source later proves one necessary.


## M02 extension — fork-channel ordering and moving aliases

### Why

The accepted `vX.Y.Z-private.N` identity and per-baseline next-release counter are already integrated, but downstream current/update-channel consumers still need one explicit cross-baseline resolver contract. Generic SemVer precedence is intentionally different from the fork's canonical channel semantics and can select an upstream-only or legacy tag instead of a canonical private release.

Some publication surfaces also support a native moving alias such as `latest`; its semantics must be bounded without weakening immutable version identity.

### Change

Extend the same policy-neutral fork-release contract so that:

- baseline-local next-release selection and cross-baseline current/update selection are distinct operations;
- cross-baseline candidates are exact canonical `vX.Y.Z-private.N` releases only;
- candidates are ordered numerically by `(X, Y, Z, N)`, independently of generic SemVer precedence;
- upstream-only, legacy upstream-looking, malformed and other non-canonical tags are excluded;
- a native moving `latest` alias is optional channel metadata only;
- when used, `latest` points to the newest accepted stable canonical fork release under the project's release-quality policy;
- immutable/versioned references remain available and the alias identifies the same released artifact/content;
- no synthetic canonical Git release/tag such as `vlatest` is created.

This M02 extension remains contract/test/documentation work in Project Workflow. It does not add runtime release infrastructure or directly mutate downstream repositories.
