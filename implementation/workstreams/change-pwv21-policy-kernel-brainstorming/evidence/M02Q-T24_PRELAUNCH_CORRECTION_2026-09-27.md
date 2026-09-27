# M02Q-T24 prelaunch contract correction

Candidate launch refresh rejected the newly materialized T24 stable Card because its Included scope used the literal placeholder-like text `<card_id>`. The canonical Task Card parser treats angle-bracket text as unresolved authority and fails closed.

No T24 implementation mutation occurred. The semantic scope is unchanged: the phrase is rewritten to plain resolved prose, "the exact Card-ID prefix followed by a hyphen". Because the T23 consumed handoff proof binds the T24 Card blob, Task Board consumed_proof must be refreshed to the corrected exact Card identity before launch.
