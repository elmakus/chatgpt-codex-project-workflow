# Specification — codex_only bounded parallel Card safety

## Requirement: serial remains the default

A selected Task Board with no active parallel batch and Cards without explicit `parallel_safe: true` MUST remain valid and executable serially.

### Scenario: no parallel metadata

Given multiple READY Cards without explicit parallel opt-in, the router selects deterministic serial execution and does not synthesize a parallel batch.

## Requirement: planning does not certify execution-time safety

Planning MAY describe candidate overlap/dependencies, but Execution Prep MUST re-evaluate current repository/runtime safety immediately before forming a batch.

### Scenario: stale planning candidate

Given a plan marked two packages as candidate-parallel but current write scopes overlap, JIT keeps them serial.

## Requirement: explicit compatible eligibility

A Card MAY join a parallel batch only when dependencies are complete, `parallel_safe: true`, `write_scope` is finite and valid, scopes are pairwise disjoint, `exclusive_resources` do not conflict, isolated mutable workspaces are available, and one exact recoverable integration base exists.

### Scenario: compatible Cards

Two dependency-ready Cards with disjoint normalized scopes, no resource conflicts and available isolated workspaces are frozen into one finite batch from the same exact base.

### Scenario: unsafe candidate

A Card with missing opt-in, overlapping scope, conflicting resource, unavailable isolation or unrecoverable base remains eligible for ordinary serial execution but is excluded from the batch.

## Requirement: deterministic finite batch

Execution Prep MUST construct the batch deterministically from READY Cards in canonical Task Board order, freeze membership before launch and MUST NOT refill it dynamically.

### Scenario: later Card becomes ready

A Card that becomes READY after B01 was frozen cannot be appended to B01. It may run serially or join a later newly frozen batch after B01 resolves.

## Requirement: one shared-state writer

Codex Main MUST be the only writer of selected Task Board and shared integration state. Worker lanes MUST return result/evidence and MUST NOT mutate shared coordination artifacts.

### Scenario: lane attempts shared-state write

A returned lane diff touching the live Task Board, workstream manifest or shared integration bookkeeping is rejected from integration even if a broad path claim would otherwise include that file.

## Requirement: runtime identity is not project state

Batch/lane IDs, exact Git base/result refs and evidence MAY be durable project state. Concrete worker/session/model/profile/invocation/lease/resume/worktree-path identity MUST NOT be required project state.

### Scenario: worker replacement

A concrete worker is lost while L02 is in progress and no durable result exists. Runtime may replace it while Project Workflow keeps the same B01/L02 identity.

## Requirement: returned results are bounded and integrated by Main

Main MUST validate each returned result against the frozen base, Card write scope, reserved-state prohibition and required evidence before integrating. Integration MUST follow frozen member order.

### Scenario: scope escape

A lane returns a commit changing a file outside its write scope. Main preserves result/evidence for diagnosis, marks the affected member/batch blocked and does not integrate it.

### Scenario: partial integration interruption

L01 is integrated and L02 is returned when Main is interrupted. Recovery keeps L01 integrated, does not rerun L02, and resumes validation/integration of L02.

## Requirement: lane history survives integration

Returned and integrated refs/evidence MUST remain recoverable after batch completion; a completed batch is not rewritten into a different membership/base.

### Scenario: later batch

After B01 completes, `current_batch` becomes null. B01 remains durable history and a later compatible set receives B02.

## Requirement: M02 review semantics remain intact

A reviewable parallel Card MUST enter ordinary M02 review only after its exact Main-integrated result is durable. Runtime concurrency MUST NOT alter review attempt identity or permit Tester production repair.

### Scenario: integrated review subject

Main integrates L02 to exact shared-branch commit S2, records S2 as the Card result, then freezes the Card review attempt for S2. Later unrelated commits do not rewrite that historical subject.
