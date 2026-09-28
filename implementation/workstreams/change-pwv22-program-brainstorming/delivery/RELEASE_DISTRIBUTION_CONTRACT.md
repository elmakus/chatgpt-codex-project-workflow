# Official release and distribution provenance contract — M01-S04-T01

## Release identity without self-hash cycles
Candidate content is frozen by exact source tree/content manifest first. External tests/Reviews bind that frozen subject. Official publication then creates an immutable release ref/tag/package mapping whose publication identity is bound externally by target readback; candidate content never embeds its own future commit hash. Candidate branch, version string or package filename alone is never official provenance. Native admission requires exact official release identity plus compatibility with the lineage's single native epoch.

## Required package inventory categories
Semantic policy/workflow modules; schemas/contracts; production validators/router; shared behavioral fixtures; required-host adapters/skills/bootstrap; Pi package/helper when applicable; provenance/compatibility manifest; deterministic test launcher/instructions. Secrets, runtime sessions and a second state store are forbidden.

## Compatibility/fallback truth table
| Installed package | Provenance | Compatible | Git fallback | Outcome |
|---|---|---:|---:|---|
| exact official | valid | yes | any | use package; exact release |
| tampered/wrong | invalid | any | yes | reject package; verified Git |
| missing | n/a | n/a | yes | verified Git |
| incompatible | valid | no | yes | reject package; compatible Git |
| unusable | any | any | no | fail closed |
| old-epoch rollback | valid | no | any | reject; Recovery/forward correction |
| legacy consumer | any | any | any | reject native admission; no normalization |

## Release blockers
MUST-semantic, Recovery, required-host, provenance/tamper, unresolved current-release finding, stale/unknown required evidence or final-acceptance failure blocks publication. Historical backward compatibility is not required.

## pi-unraid-owned distribution interface
Owner returns exact artifact/release pin, source/config/stack version, install/update/rollback attempt, MCP enabled+injection readback, explicit desired relay policy+readback, target prior/post state and known/UNKNOWN outcome. Extend existing distribution/regression mechanism; no package-local updater. H06 remains unproved until fresh owner inspection.

## Owner/effect separation
Package build/mutation, distribution source change, live install/config, official release/tag and consumer integration/auto-tag are separate effect domains with separate accepted target/expected-old/attempt/readback authority. No prose implies live authorization.
