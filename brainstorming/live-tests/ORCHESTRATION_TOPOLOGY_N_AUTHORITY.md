# Orchestration-topology continuity authority — N

Accepted semantic target for both runtime realizations:

- final durable result MUST be exact `topology-n: GOOD\n`;
- an initial reviewed subject `topology-n: BAD\n` MUST receive RED;
- bounded correction from BAD to GOOD is authorized;
- corrected subject MUST be frozen as a new immutable review attempt;
- the context/realization that materially performs the correction MUST NOT independently review the corrected subject;
- the corrected subject MUST receive independent GREEN before terminal finalization;
- after GREEN, deterministic finalization MUST continue without an artificial user stop;
- RED itself is not a user stop when bounded correction is authorized;
- independence is per exact reviewed subject, not per whole coordinating invocation/chat;
- canonical Project Workflow state/evidence MUST remain runtime-neutral.

The two experiment variants differ only in realization topology:

1. capable-coordinator variant: a coordinating invocation with qualifying independent-context capability may realize the complete RED -> correction -> independent re-review -> GREEN -> finalization chain in one user invocation;
2. fresh-context variant: when the current normal ChatGPT context itself performs the correction, it must stop only at the new independent-review boundary; the next fresh independent-review context may consume GREEN and continue deterministic finalization in that same chat.

A common semantic contract must permit both realizations without changing the durable obligation model.
