#!/usr/bin/env python3
"""Report formulaic English prose and high-confidence comment narration."""

from __future__ import annotations

import argparse
import dataclasses
import json
import pathlib
import re
import sys
from collections.abc import Iterable

ROOT = pathlib.Path(__file__).resolve().parent.parent
VOCABULARY_PATH = ROOT / "scripts" / "vocabulary.json"
PROSE_SUFFIXES = {".md", ".markdown", ".mdx", ".rst", ".txt"}
SOURCE_SUFFIXES = {
    ".c", ".cc", ".cpp", ".go", ".h", ".hpp", ".java", ".js", ".jsx",
    ".py", ".rs", ".sh", ".ts", ".tsx",
}
SKIP_DIRS = {".git", ".hg", ".svn", "__pycache__", "node_modules", "vendor"}
URL = re.compile(r"(?:https?://|mailto:)[^\s)>]+", re.IGNORECASE)
MARKDOWN_LINK = re.compile(r"!?\[[^\]\n]*\]\([^\n)]*\)|<https?://[^>\n]+>")
INLINE_CODE = re.compile(r"(`+)([^\n]*?)\1")
WORD = re.compile(r"\b[A-Za-z]+(?:['’-][A-Za-z]+)*\b")
PASSIVE = re.compile(
    r"\b(?:am|is|are|was|were|be|been|being)\s+"
    r"(?:(?:also|already|currently|not)\s+)?"
    r"(?:[A-Za-z]+ed|built|done|found|given|known|made|run|set|shown|written)\b",
    re.IGNORECASE,
)
CONTRAST = re.compile(
    r"\bnot\s+only\b[^.!?\n]{0,100}\bbut\s+also\b|"
    r"\b(?:it|this|that)\s+is\s+not\b[^.!?\n]{0,100}[,;:]\s*(?:it|this|that)\s+is\b",
    re.IGNORECASE,
)
CONCLUSION = re.compile(
    r"(?im)^[ \t]*(?:in\s+conclusion|in\s+summary|to\s+summari[sz]e|ultimately)\b[,:]?"
)
ABSTRACT = (
    "accessibility", "accuracy", "clarity", "efficiency", "flexibility",
    "maintainability", "performance", "reliability", "robustness", "scalability",
    "security", "simplicity", "usability",
)
TRIPLET = re.compile(
    rf"\b(?:{'|'.join(ABSTRACT)})\b\s*,\s*"
    rf"\b(?:{'|'.join(ABSTRACT)})\b\s*,?\s*(?:and|or)\s+"
    rf"\b(?:{'|'.join(ABSTRACT)})\b",
    re.IGNORECASE,
)
EMOJI = re.compile(
    "[\U0001F1E6-\U0001F1FF\U0001F300-\U0001FAFF\u2600-\u27BF]"
)


@dataclasses.dataclass(frozen=True, order=True)
class Finding:
    line: int
    code: str
    severity: str
    message: str
    sample: str = ""


class LintFailure(Exception):
    """The linter cannot read or validate its input."""


def load_vocabulary() -> list[dict[str, object]]:
    try:
        data = json.loads(VOCABULARY_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise LintFailure(f"cannot load {VOCABULARY_PATH}: {error}") from error
    entries = data.get("entries") if isinstance(data, dict) else None
    if not isinstance(entries, list):
        raise LintFailure(f"{VOCABULARY_PATH}: 'entries' must be a list")
    required = {"term", "category", "replacement", "advisory"}
    for index, entry in enumerate(entries, 1):
        if not isinstance(entry, dict) or set(entry) != required:
            raise LintFailure(
                f"{VOCABULARY_PATH}: entry {index} must contain {sorted(required)}"
            )
        if entry["category"] not in {"ai-tell", "filler", "jargon"}:
            raise LintFailure(f"{VOCABULARY_PATH}: entry {index} has an invalid category")
        if not isinstance(entry["advisory"], bool):
            raise LintFailure(f"{VOCABULARY_PATH}: entry {index} has a non-boolean advisory field")
        if not all(isinstance(entry[key], str) and entry[key] for key in required - {"advisory"}):
            raise LintFailure(f"{VOCABULARY_PATH}: entry {index} has an empty text field")
    return entries


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def blank_span(chars: list[str], start: int, end: int) -> None:
    for index in range(start, end):
        if chars[index] not in "\r\n":
            chars[index] = " "


def mask_markdown(text: str) -> str:
    """Mask code, links, and URLs while preserving offsets and newlines."""
    chars = list(text)
    in_fence: tuple[str, int] | None = None
    offset = 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^[ \t]{0,3}(`{3,}|~{3,})", line)
        if in_fence is None and marker:
            token = marker.group(1)
            in_fence = (token[0], len(token))
            blank_span(chars, offset, offset + len(line))
        elif in_fence is not None:
            blank_span(chars, offset, offset + len(line))
            closing = re.match(rf"^[ \t]{{0,3}}{re.escape(in_fence[0])}{{{in_fence[1]},}}\s*$", line.rstrip("\r\n"))
            if closing:
                in_fence = None
        offset += len(line)
    masked = "".join(chars)
    chars = list(masked)
    for pattern in (INLINE_CODE, MARKDOWN_LINK, URL):
        snapshot = "".join(chars)
        for match in pattern.finditer(snapshot):
            blank_span(chars, match.start(), match.end())
    return "".join(chars)


def sample_at(text: str, start: int, end: int) -> str:
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    if line_end < 0:
        line_end = len(text)
    return text[line_start:line_end].strip()[:120]


def vocabulary_findings(text: str, checked: str, entries: list[dict[str, object]]) -> list[Finding]:
    findings: list[Finding] = []
    for entry in entries:
        term = str(entry["term"])
        pattern = re.compile(rf"(?<![A-Za-z0-9_-]){re.escape(term)}(?:s|d|ing)?(?![A-Za-z0-9_-])", re.IGNORECASE)
        for match in pattern.finditer(checked):
            severity = "advisory" if entry["advisory"] else "error"
            category = str(entry["category"]).replace("-", "_")
            findings.append(Finding(
                line_number(text, match.start()),
                f"vocabulary.{category}",
                severity,
                f"replace '{match.group(0)}': {entry['replacement']}",
                sample_at(text, match.start(), match.end()),
            ))
    return findings


def sentence_findings(text: str, checked: str) -> list[Finding]:
    findings: list[Finding] = []
    for match in PASSIVE.finditer(checked):
        findings.append(Finding(
            line_number(text, match.start()), "sentence.passive", "advisory",
            "name the actor and use active voice when the actor matters",
            sample_at(text, match.start(), match.end()),
        ))
    for match in re.finditer(r"[^.!?\n]+(?:[.!?]+|$)", checked):
        words = WORD.findall(match.group(0))
        clauses = len(re.findall(r"[,;:]|\b(?:and|but|because|although|while|which|that)\b", match.group(0), re.IGNORECASE))
        if len(words) > 35 or (len(words) > 24 and clauses >= 4):
            findings.append(Finding(
                line_number(text, match.start()), "sentence.long", "advisory",
                f"split this sentence; it has {len(words)} words and {clauses} clause markers",
                sample_at(text, match.start(), match.end()),
            ))
    for match in CONTRAST.finditer(checked):
        findings.append(Finding(
            line_number(text, match.start()), "sentence.contrast", "advisory",
            "replace the contrast template with the concrete distinction",
            sample_at(text, match.start(), match.end()),
        ))
    for match in TRIPLET.finditer(checked):
        findings.append(Finding(
            line_number(text, match.start()), "sentence.triplet", "advisory",
            "replace the abstract triplet with defined or measured results",
            sample_at(text, match.start(), match.end()),
        ))
    for match in CONCLUSION.finditer(checked):
        findings.append(Finding(
            line_number(text, match.start()), "sentence.conclusion", "error",
            "delete the recap template and end on the last new fact or action",
            sample_at(text, match.start(), match.end()),
        ))
    return findings


def markdown_findings(text: str, checked: str) -> list[Finding]:
    findings: list[Finding] = []
    lines = checked.splitlines()
    original_lines = text.splitlines()
    bold_starts: list[int] = []
    for index, line in enumerate(lines):
        if re.match(r"^\s*(?:[-*+]\s+)?\*\*[^*\n]+\*\*\s*[:—-]", line):
            bold_starts.append(index)
        heading = re.match(r"^\s{0,3}#{1,6}\s+(.+)$", line)
        if heading and EMOJI.search(heading.group(1)):
            findings.append(Finding(
                index + 1, "markdown.emoji_heading", "error",
                "remove the Emoji and name the task or subject",
                original_lines[index].strip()[:120],
            ))
    for current, following in zip(bold_starts, bold_starts[1:]):
        between = lines[current + 1:following]
        if not any(part.strip() and not part.lstrip().startswith(("-", "*", "+")) for part in between):
            findings.append(Finding(
                following + 1, "markdown.bold_wall", "advisory",
                "replace repeated bold leads with plain prose, a table, or descriptive headings",
                original_lines[following].strip()[:120],
            ))
    dash_lines = [index for index, line in enumerate(lines) if "—" in line]
    for index in dash_lines:
        count = lines[index].count("—")
        if count > 1:
            findings.append(Finding(
                index + 1, "markdown.em_dash", "advisory",
                "replace repeated em dashes with punctuation or separate sentences",
                original_lines[index].strip()[:120],
            ))
    if len(dash_lines) >= 3:
        index = dash_lines[2]
        findings.append(Finding(
            index + 1, "markdown.em_dash", "advisory",
            "reduce em-dash density across nearby prose",
            original_lines[index].strip()[:120],
        ))
    return findings


def source_comments(text: str, suffix: str) -> list[tuple[int, str]]:
    comments: list[tuple[int, str]] = []
    marker = r"#" if suffix in {".py", ".sh"} else r"//"
    for index, line in enumerate(text.splitlines()):
        match = re.match(rf"^\s*{marker}\s*(.+?)\s*$", line)
        if match and not (suffix == ".sh" and index == 0 and line.startswith("#!")):
            comments.append((index, match.group(1)))
    return comments


def comment_findings(text: str, suffix: str) -> list[Finding]:
    lines = text.splitlines()
    findings: list[Finding] = []
    for index, comment in source_comments(text, suffix):
        next_line = ""
        for candidate in lines[index + 1:]:
            if candidate.strip():
                next_line = candidate.strip()
                break
        if not next_line:
            continue
        normalized = comment.rstrip(".").strip()
        patterns = (
            (re.fullmatch(r"increment (?:the )?([A-Za-z_]\w*)", normalized, re.IGNORECASE), r"{name}\s*\+=\s*1\b"),
            (re.fullmatch(r"set (?:the )?([A-Za-z_]\w*)", normalized, re.IGNORECASE), r"{name}\s*="),
            (re.fullmatch(r"call (?:the )?([A-Za-z_]\w*)", normalized, re.IGNORECASE), r"{name}\s*\("),
            (re.fullmatch(r"return (?:the )?(?:result|value)", normalized, re.IGNORECASE), r"return\b"),
        )
        repeated = False
        for match, code_pattern in patterns:
            if not match:
                continue
            name = re.escape(match.group(1)) if match.lastindex else ""
            if re.search(code_pattern.format(name=name), next_line, re.IGNORECASE):
                repeated = True
                break
        if repeated:
            findings.append(Finding(
                index + 1, "comment.narration", "error",
                "delete the comment; the next statement already says this",
                lines[index].strip()[:120],
            ))
    return findings


def lint_text(path: pathlib.Path, text: str, entries: list[dict[str, object]]) -> list[Finding]:
    suffix = path.suffix.lower()
    if suffix in SOURCE_SUFFIXES:
        return comment_findings(text, suffix)
    checked = mask_markdown(text) if suffix in {".md", ".markdown", ".mdx"} else text
    findings = vocabulary_findings(text, checked, entries)
    findings.extend(sentence_findings(text, checked))
    if suffix in {".md", ".markdown", ".mdx"}:
        findings.extend(markdown_findings(text, checked))
    return sorted(set(findings))


def input_files(paths: Iterable[str]) -> list[pathlib.Path]:
    files: set[pathlib.Path] = set()
    for raw in paths:
        if raw == "-":
            continue
        path = pathlib.Path(raw)
        if not path.exists():
            raise LintFailure(f"input does not exist: {raw}")
        if path.is_dir():
            for candidate in path.rglob("*"):
                if any(part in SKIP_DIRS for part in candidate.parts):
                    continue
                if candidate.is_file() and candidate.suffix.lower() in PROSE_SUFFIXES | SOURCE_SUFFIXES:
                    files.add(candidate)
        elif path.is_file():
            files.add(path)
        else:
            raise LintFailure(f"input is not a regular file or directory: {raw}")
    return sorted(files)


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="files, directories, or - for standard input")
    parser.add_argument(
        "--fail-level", choices=("error", "advisory"), default="error",
        help="lowest severity that produces exit status 1 (default: error)",
    )
    parser.add_argument(
        "--stdin-filename", default="stdin.md",
        help="filename used to select rules for standard input",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    try:
        entries = load_vocabulary()
        files = input_files(arguments.paths)
        results: list[tuple[str, Finding]] = []
        if "-" in arguments.paths:
            text = sys.stdin.read()
            stdin_path = pathlib.Path(arguments.stdin_filename)
            results.extend((arguments.stdin_filename, finding) for finding in lint_text(stdin_path, text, entries))
        for path in files:
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                raise LintFailure(f"cannot read {path}: {error}") from error
            results.extend((str(path), finding) for finding in lint_text(path, text, entries))
    except LintFailure as error:
        print(f"writing-lint: {error}", file=sys.stderr)
        return 2

    for path, finding in results:
        sample = f": {finding.sample}" if finding.sample else ""
        print(
            f"{path}:{finding.line}: {finding.severity} [{finding.code}] "
            f"{finding.message}{sample}"
        )
    if not results:
        print("No findings.")

    if arguments.fail_level == "advisory":
        return 1 if results else 0
    return 1 if any(finding.severity == "error" for _, finding in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
