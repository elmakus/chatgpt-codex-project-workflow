#!/usr/bin/env python3
"""Minimal non-mutating H002 reproducer against an exact PWv2 checkout."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: repro_h002.py /path/to/project_workflow_v2")
    pw = Path(sys.argv[1]).resolve()
    sys.path.insert(0, str(pw))
    from tools.router import select_route  # type: ignore

    with tempfile.TemporaryDirectory(prefix="h002-") as td:
        project = Path(td) / "consumer"
        write(project / "PROJECT.md", """+++
project_workflow = "v2"
project_id = "h002-repro"
repository = "owner/repo"
workstream_root = "implementation/workstreams"
+++
# H002 temporary consumer fixture
""")
        ws = "implementation/workstreams/sample-workstream"
        write(project / f"{ws}/WORKSTREAM.toml", """workstream_id = "sample-workstream"
kind = "change"
branch = "work/h002"
integration_target = "main"
created_from = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
authority = [{ class = "authority", path = "requirements/REQUIREMENTS.md" }]

[brainstorm]
class = "brainstorm"
path = "implementation/workstreams/sample-workstream/BRAINSTORM.toml"

[definition]
class = "definition"
path = "implementation/workstreams/sample-workstream/DEFINITION.toml"
""")
        write(project / f"{ws}/BRAINSTORM.toml", """workstream_id = "sample-workstream"
scope_id = "scope-stop"
revision = 1
state = "promoted"
challenge_audit = "green"
explicit_user_stop = true
promotion_state = "authorized"
promotion_subject = "scope-stop@1"
""")
        write(project / f"{ws}/DEFINITION.toml", """workstream_id = "sample-workstream"
source_scope_subject = "scope-stop@1"
revision = "R1"
state = "active"
completeness_audit = "pending"
premium_a = "not_due"
decisions = []

[requirements]
class = "authority"
path = "requirements/REQUIREMENTS.md"
""")
        routed = select_route(project, [f"{ws}/WORKSTREAM.toml"], package_root=pw)
        print(routed.disposition, routed.obligation, routed.subject, routed.owner_module, sep=" | ")
        return 0 if (routed.disposition, routed.obligation) == ("route", "definition") else 1


if __name__ == "__main__":
    raise SystemExit(main())
