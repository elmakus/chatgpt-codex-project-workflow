# Core oracle observation convention

Expected answers are derived from pinned R7 authority before any production adapter is consulted. Each case has a stable case ID, requirement references, explicit input facts and a normalized expected semantic observation. The checker validates corpus structure and selected negative mutants only; it never imports or calls a production/donor router/kernel.

Adapters may later translate real host/product observations into this test-only normalized shape, but they MUST NOT rewrite expected answers to match production. A changed production stub therefore cannot change this corpus. Host-specific observation mechanics belong to S16/S17.

Observation classes include exact next owner, accepted/no-write, freshness, Review eligibility, external UNKNOWN/retry prohibition and Close completeness. Absence of an observed field is not interpreted as success.
