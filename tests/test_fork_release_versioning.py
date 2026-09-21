"""Deterministic regression checks for the common fork-release versioning contract."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMON = ROOT / "workflow/common/FORK_RELEASE_VERSIONING.md"
PUBLICATION_SURFACES = (
    ROOT / "workflow/chatgpt_only/CLOSE.md",
    ROOT / "workflow/codex_only/CLOSE.md",
    ROOT / "workflow/REVIEW_AND_HANDOFF.md",
)
README = ROOT / "README.md"
AUTO_PATCH = ROOT / ".github/workflows/auto-patch-tag.yml"

PRIVATE_TAG = re.compile(
    r"^v(?P<baseline>[0-9]+\.[0-9]+\.[0-9]+)-private\.(?P<n>[1-9][0-9]*)$"
)


def canonical_private_key(tag: str) -> tuple[int, int, int, int] | None:
    match = PRIVATE_TAG.fullmatch(tag)
    if not match:
        return None
    x, y, z = (int(part) for part in match.group("baseline").split("."))
    return (x, y, z, int(match.group("n")))


def current_canonical_private(tags: list[str]) -> str | None:
    candidates = [(key, tag) for tag in tags if (key := canonical_private_key(tag))]
    if not candidates:
        return None
    return max(candidates)[1]


def next_private_version(baseline: str, tags: list[str]) -> str:
    revisions: list[int] = []
    for tag in tags:
        match = PRIVATE_TAG.fullmatch(tag)
        if match and match.group("baseline") == baseline:
            revisions.append(int(match.group("n")))
    return f"v{baseline}-private.{max(revisions, default=0) + 1}"


class ForkReleaseVersioningContractTest(unittest.TestCase):
    def test_first_private_release(self) -> None:
        self.assertEqual(next_private_version("5.0.8", ["v5.0.8"]), "v5.0.8-private.1")

    def test_numeric_gap_and_multi_digit_increment(self) -> None:
        tags = ["v5.0.8-private.2", "v5.0.8-private.10"]
        self.assertEqual(next_private_version("5.0.8", tags), "v5.0.8-private.11")

    def test_baseline_reset_and_isolation(self) -> None:
        tags = ["v5.0.8-private.99", "v5.0.9", "v5.0.13"]
        self.assertEqual(next_private_version("5.0.9", tags), "v5.0.9-private.1")
        tags.append("v5.0.9-private.3")
        self.assertEqual(next_private_version("5.0.9", tags), "v5.0.9-private.4")

    def test_legacy_and_malformed_tags_do_not_enter_counter(self) -> None:
        tags = [
            "v5.0.8",
            "v5.0.9",
            "v5.0.13",
            "v5.0.8-private.0",
            "v5.0.8-private.foo",
            "v5.0.7-private.40",
        ]
        self.assertEqual(next_private_version("5.0.8", tags), "v5.0.8-private.1")

    def test_canonical_channel_numeric_private_order(self) -> None:
        tags = ["v1.1.18-private.4", "v1.1.18-private.10"]
        self.assertEqual(current_canonical_private(tags), "v1.1.18-private.10")

    def test_canonical_channel_cross_baseline_order(self) -> None:
        tags = [
            "v1.1.17-private.99",
            "v1.1.18-private.10",
            "v1.1.19-private.1",
        ]
        self.assertEqual(current_canonical_private(tags), "v1.1.19-private.1")

    def test_upstream_only_semver_winner_is_not_channel_candidate(self) -> None:
        tags = ["v1.1.18", "v1.1.18-private.4"]
        self.assertEqual(current_canonical_private(tags), "v1.1.18-private.4")

    def test_noncanonical_tags_are_excluded_from_channel(self) -> None:
        tags = [
            "v1.1.18",
            "v1.1.20",
            "v1.1.19-private.0",
            "v1.1.19-private.foo",
            "v1.1.19-private.2-extra",
            "legacy-v9",
            "v1.1.18-private.10",
        ]
        self.assertEqual(current_canonical_private(tags), "v1.1.18-private.10")

    def test_common_contract_contains_required_semantics(self) -> None:
        text = COMMON.read_text(encoding="utf-8")
        required = (
            "exact upstream repository",
            "exact upstream version/tag",
            "exact upstream commit SHA",
            "max(N) + 1",
            "Generic highest-SemVer selection",
            "MUST NOT rewrite, delete, retag",
            "prerelease",
            "automatic upstream synchronization",
            "Canonical fork-channel ordering across baselines",
            "(X, Y, Z, N)",
            "wrapped with ad-hoc exceptions",
            "Optional moving `latest` alias",
            "newest accepted **stable** canonical fork release",
            "same released artifact/content identity",
            "synthetic canonical Git tag/release such as `vlatest`",
        )
        for needle in required:
            self.assertIn(needle, text)

    def test_all_publication_surfaces_reference_one_common_contract(self) -> None:
        reference = "workflow/common/FORK_RELEASE_VERSIONING.md"
        for path in PUBLICATION_SURFACES:
            text = path.read_text(encoding="utf-8")
            self.assertIn(reference, text, path.as_posix())
            self.assertNotIn("max(N) + 1", text, path.as_posix())

    def test_readme_points_to_canonical_contract(self) -> None:
        self.assertIn(
            "workflow/common/FORK_RELEASE_VERSIONING.md",
            README.read_text(encoding="utf-8"),
        )

    def test_repo_local_auto_patch_tagger_is_not_rewired(self) -> None:
        text = AUTO_PATCH.read_text(encoding="utf-8")
        self.assertNotIn("FORK_RELEASE_VERSIONING", text)
        self.assertIn("Create next SemVer patch tag", text)


if __name__ == "__main__":
    unittest.main()
