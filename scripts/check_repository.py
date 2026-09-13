#!/usr/bin/env python3
"""Validate the writing-skill repository through one command."""

from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
from collections.abc import Callable

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINTER = ROOT / "scripts" / "writing_lint.py"
REFERENCES = [
    ROOT / "references" / name
    for name in (
        "vocabulary.md",
        "sentences.md",
        "readme.md",
        "docs.md",
        "comments.md",
        "commit-pr-issue.md",
    )
]
READMES = [ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "README.zh-TW.md"]
REQUIRED = [
    ROOT / "SKILL.md", *READMES, ROOT / "LICENSE", LINTER,
    ROOT / "scripts" / "vocabulary.json", *REFERENCES,
]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class CheckFailure(Exception):
    """A repository invariant failed."""


def run_linter(paths: list[pathlib.Path], fail_level: str = "error") -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(LINTER), "--fail-level", fail_level]
    command.extend(str(path.relative_to(ROOT)) for path in paths)
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)


def check_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    if missing:
        raise CheckFailure(f"missing required files: {', '.join(missing)}")


def check_frontmatter_and_limits() -> None:
    skill_lines = (ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines()
    if len(skill_lines) > 250:
        raise CheckFailure(f"SKILL.md has {len(skill_lines)} lines; limit is 250")
    if len(skill_lines) < 4 or skill_lines[0] != "---" or skill_lines[3] != "---":
        raise CheckFailure("SKILL.md must start with three-line YAML frontmatter")
    if skill_lines[1] != "name: writing-skill":
        raise CheckFailure("SKILL.md frontmatter name must be writing-skill")
    description = skill_lines[2]
    for term in ("English", "Markdown", "chinese-skill"):
        if term not in description:
            raise CheckFailure(f"SKILL.md description must mention {term}")
    sections = [index for index, line in enumerate(skill_lines) if line.startswith("## ")]
    if len(sections) > 12:
        raise CheckFailure(f"SKILL.md has {len(sections)} sections; limit is 12")
    for position, start in enumerate(sections):
        end = sections[position + 1] if position + 1 < len(sections) else len(skill_lines)
        if end - start - 1 > 20:
            raise CheckFailure(f"SKILL.md section on line {start + 1} exceeds 20 lines")
    for path in REFERENCES:
        count = len(path.read_text(encoding="utf-8").splitlines())
        if count > 200:
            raise CheckFailure(f"{path.relative_to(ROOT)} has {count} lines; limit is 200")


def check_sources_and_links() -> None:
    markdown_files = [ROOT / "SKILL.md", *READMES, *REFERENCES, *sorted((ROOT / "examples").glob("*.md"))]
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        if path in REFERENCES:
            source = text.partition("## Sources")[2]
            if not source or "https://" not in source:
                raise CheckFailure(f"{path.relative_to(ROOT)} needs a Sources section with URLs")
        for match in LINK.finditer(text):
            target = match.group(1).strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).resolve().exists():
                raise CheckFailure(f"{path.relative_to(ROOT)} links to missing file {local}")


def check_vocabulary() -> None:
    try:
        data = json.loads((ROOT / "scripts" / "vocabulary.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise CheckFailure(f"vocabulary.json is invalid: {error}") from error
    entries = data.get("entries") if isinstance(data, dict) else None
    if not isinstance(entries, list) or not entries:
        raise CheckFailure("vocabulary.json must contain a non-empty entries list")
    categories = {entry.get("category") for entry in entries if isinstance(entry, dict)}
    if categories != {"ai-tell", "filler", "jargon"}:
        raise CheckFailure(f"vocabulary.json categories are incomplete: {sorted(categories)}")


def check_self_lint() -> None:
    result = run_linter([ROOT / "README.md", ROOT / "SKILL.md", *REFERENCES])
    if result.returncode != 0:
        detail = (result.stdout + result.stderr).strip()
        raise CheckFailure(f"repository prose lint failed:\n{detail}")


def check_examples() -> None:
    before = sorted((ROOT / "examples").glob("*before*.md"))
    after = sorted((ROOT / "examples").glob("*after*.md"))
    if len(before) != 3 or len(after) != 3:
        raise CheckFailure("examples must contain three before files and three after files")
    for path in [*before, *after]:
        count = len(path.read_text(encoding="utf-8").splitlines())
        if count > 40:
            raise CheckFailure(f"{path.relative_to(ROOT)} has {count} lines; limit is 40")
    result = run_linter(before)
    if result.returncode != 1:
        detail = (result.stdout + result.stderr).strip()
        raise CheckFailure(f"before examples must produce non-advisory findings:\n{detail}")
    seen = {path.name for path in before if path.name in result.stdout}
    if len(seen) != len(before):
        raise CheckFailure("each before example must produce a finding")
    result = run_linter(after, fail_level="advisory")
    if result.returncode != 0 or result.stdout.strip() != "No findings.":
        detail = (result.stdout + result.stderr).strip()
        raise CheckFailure(f"after examples must produce no findings:\n{detail}")


def run_check(name: str, check: Callable[[], None]) -> None:
    check()
    print(f"PASS {name}")


def main() -> int:
    checks = (
        ("required files", check_required_files),
        ("frontmatter and line limits", check_frontmatter_and_limits),
        ("sources and local links", check_sources_and_links),
        ("vocabulary schema", check_vocabulary),
        ("repository prose lint", check_self_lint),
        ("example controls", check_examples),
    )
    try:
        for name, check in checks:
            run_check(name, check)
    except (CheckFailure, OSError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    print("All repository checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
