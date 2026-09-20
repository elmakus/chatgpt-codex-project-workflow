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
