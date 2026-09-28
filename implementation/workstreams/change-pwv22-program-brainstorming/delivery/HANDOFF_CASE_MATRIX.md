# Universal handoff case matrix

| Direction | Remote | Local slot | Effect | Expected |
|---|---|---|---|---|
| ChatGPT→ChatGPT | equal | clean/none | known | reconstruct exact obligation |
| ChatGPT→Pi | equal | clean/none | known | reconstruct exact obligation |
| Pi→ChatGPT | equal | clean/none | known | reconstruct exact obligation |
| Pi→Pi | equal | clean/none | known | reconstruct exact obligation |
| any | moved | any | known | discard stale launch assumption; reconstruct current state |
| any | missing/wrong repo/path | any | known | fail closed |
| any | equal | dirty/local-only | known | preserve/inspect residue; remote remains continuation truth |
| any | equal | duplicate same-branch slots | known | reject duplicate; reconcile to one slot |
| any | equal/moved | dirty | UNKNOWN | target readback first; no blind reset/disposal |
| any | race after refresh | any | known | expected-old publication rejects; refetch/re-evaluate |

Hidden receiver prerequisites are forbidden. Installed compatible package may bootstrap tooling, otherwise canonical Git fallback; both must resolve the same semantic authority. Helper-authoritative receipts are invalid.
