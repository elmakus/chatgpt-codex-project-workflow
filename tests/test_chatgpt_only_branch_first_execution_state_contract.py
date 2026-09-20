from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    name: (ROOT / "workflow/chatgpt_only" / name).read_text(encoding="utf-8")
    for name in (
        "ROUTER.md",
        "EXECUTION_PREP.md",
        "EXECUTION.md",
        "STATE.md",
        "RECOVERY.md",
        "CLOSE.md",
        "MICRO_FIX.md",
        "TASK_CARDS.md",
        "TASK_CARD_TEMPLATE.md",
        "REPOSITORY.md",
        "REVIEW.md",
        "RESEARCH.md",
        "WORKSTREAMS.md",
        "TASK_BOARD_TEMPLATE.yaml",
        "WORKSTREAM_TASK_BOARD_TEMPLATE.yaml",
    )
}


class ChatGPTOnlyBranchFirstExecutionStateTests(unittest.TestCase):
    def test_execution_prep_never_scaffolds_root_default_board(self):
        prep = FILES["EXECUTION_PREP.md"]
        self.assertIn(
            "Root `implementation/TASK_BOARD.yaml` and "
            "`workflow/chatgpt_only/TASK_BOARD_TEMPLATE.yaml` are historical "
            "recovery/migration surfaces only and MUST NOT be scaffolded or selected",
            prep,
        )
        self.assertNotIn(
            "For legacy/default state, scaffold `implementation/TASK_BOARD.yaml`",
            prep,
        )
        self.assertIn("WORKSTREAM_TASK_BOARD_TEMPLATE.yaml", prep)

    def test_state_contract_requires_manifest_bound_workstream_board(self):
        state = FILES["STATE.md"]
        self.assertIn(
            "Historical root/default `implementation/TASK_BOARD.yaml` is "
            "recovery/migration input only; it MUST NOT be selected or mutated",
            state,
        )
        self.assertNotIn(
            "otherwise → legacy/default `implementation/TASK_BOARD.yaml`",
            state,
        )
        self.assertIn(
            "root/default `implementation/TASK_BOARD.yaml` selected or mutated "
            "as active state",
            state,
        )

    def test_historical_default_routes_through_migration_before_mutation(self):
        recovery = FILES["RECOVERY.md"]
        self.assertIn("## Historical root/default migration before mutation", recovery)
        self.assertIn(
            "migration itself outranks review, Research, Execution Prep and Execution",
            recovery,
        )
        self.assertIn(
            "This discovery is read-only with respect to root/default execution state",
            recovery,
        )
        self.assertIn(
            "Only after that readback is GREEN may the namespaced Task Board become "
            "the selected mutable execution state",
            recovery,
        )
        self.assertIn(
            "retry/recover the same deterministic migration identity without mutating "
            "the source root board",
            recovery,
        )

    def test_binding_mismatch_and_historical_selection_fail_closed(self):
        router = FILES["ROUTER.md"]
        workstreams = FILES["WORKSTREAMS.md"]
        self.assertIn(
            "route to Recovery before any further managed-change mutation",
            router,
        )
        self.assertIn(
            "must not fall back to the default board",
            router,
        )
        self.assertIn(
            "mismatched/null `execution_ref.branch` is inconsistent "
            "branch-isolated state",
            workstreams,
        )
        self.assertIn(
            "route to Recovery rather than falling back to the legacy/default board",
            workstreams,
        )

    def test_review_and_research_ownership_are_preserved(self):
        state = FILES["STATE.md"]
        research = FILES["RESEARCH.md"]
        self.assertIn(
            "Card/milestone `review_state/review_subject/review_evidence` remain "
            "unchanged and Task-Board-owned",
            state,
        )
        self.assertIn(
            "The manifest `review` block is reserved for a **workstream-level final "
            "integration review**",
            FILES["WORKSTREAMS.md"],
        )
        self.assertIn(
            "Execution Prep / implementation / recovery Research uses:",
            research,
        )
        self.assertIn(
            "selected canonical Task Board → `research_obligation`",
            research,
        )

    def test_micro_fix_refresh_and_terminal_recovery_remain_intact(self):
        micro = FILES["MICRO_FIX.md"]
        close = FILES["CLOSE.md"]
        recovery = FILES["RECOVERY.md"]
        self.assertIn(
            "normal selected-workstream `EXECUTION.md`, `STATE.md`, "
            "`REVIEW.md`, `RESEARCH.md` and `RECOVERY.md` semantics apply",
            micro,
        )
        self.assertIn("## Branch-isolated integration refresh gate", close)
        self.assertIn(
            "Post-merge closure recovery",
            recovery,
        )
        self.assertIn(
            "Never fall back to root `implementation/TASK_BOARD.yaml`",
            recovery,
        )

    def test_historical_artifacts_are_preserved_but_not_active(self):
        repository = FILES["REPOSITORY.md"]
        template = FILES["TASK_BOARD_TEMPLATE.yaml"]
        self.assertIn(
            "Historical root/default state remains readable for recovery and provenance",
            repository,
        )
        self.assertIn(
            "do not rewrite historical evidence/handoffs solely because the state model changed",
            repository,
        )
        self.assertIn(
            "Recovery/migration compatibility only: do NOT scaffold this template",
            template,
        )
        self.assertIn(
            "Historical root/default handoffs under `project-handoffs/` remain readable",
            FILES["CLOSE.md"],
        )

    def test_task_contract_surfaces_do_not_offer_root_default_active_state(self):
        self.assertIn(
            "Historical root/default `implementation/TASK_BOARD.yaml` is "
            "recovery/migration input only",
            FILES["TASK_CARDS.md"],
        )
        self.assertIn(
            "Historical root/default `implementation/TASK_BOARD.yaml` is "
            "recovery/migration input only",
            FILES["TASK_CARD_TEMPLATE.md"],
        )
        self.assertIn(
            "Sole authoritative mutable Card/milestone implementation + "
            "execution-review state for this workstream",
            FILES["WORKSTREAM_TASK_BOARD_TEMPLATE.yaml"],
        )

    def test_chatgpt_only_lifecycle_does_not_import_codex_only_modules(self):
        for name, text in FILES.items():
            self.assertNotIn(
                "workflow/codex_only/",
                text,
                msg=f"{name} imports Codex-only lifecycle semantics",
            )


if __name__ == "__main__":
    unittest.main()
