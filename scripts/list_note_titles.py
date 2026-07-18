"""List the frontmatter titles of all Markdown notes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = PROJECT_ROOT / "notes"
TITLE_PATTERN = re.compile(r"^title:\s*(.*?)\s*$", re.MULTILINE)
SUMMARY_PATTERN = re.compile(
    r"^##\s+(?:一句话结论|摘要|内容摘要)\s*$\n(.*?)(?=^##\s|\Z)",
    re.MULTILINE | re.DOTALL,
)


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def read_tags(frontmatter: str) -> list[str]:
    """Return tags from a simple YAML list without requiring a YAML package."""
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("tags:"):
            continue

        inline_value = line.partition(":")[2].strip()
        if inline_value.startswith("[") and inline_value.endswith("]"):
            return [
                unquote(tag)
                for tag in inline_value[1:-1].split(",")
                if tag.strip()
            ]

        tags: list[str] = []
        for item_line in lines[index + 1 :]:
            match = re.match(r"^\s+-\s+(.+?)\s*$", item_line)
            if match is None:
                break
            tags.append(unquote(match.group(1)))
        return tags

    return []


def read_search_fields(note_path: Path) -> tuple[str, list[str], str]:
    """Return a note's title, tags, and summary."""
    text = note_path.read_text(encoding="utf-8-sig")

    if not text.startswith("---"):
        raise ValueError("missing YAML frontmatter")

    try:
        frontmatter = text.split("---", 2)[1]
    except IndexError as error:
        raise ValueError("unclosed YAML frontmatter") from error

    match = TITLE_PATTERN.search(frontmatter)
    if match is None or not match.group(1):
        raise ValueError("missing title field")

    title = unquote(match.group(1))
    tags = read_tags(frontmatter)
    summary_match = SUMMARY_PATTERN.search(text.split("---", 2)[2])
    summary = summary_match.group(1).strip() if summary_match else ""
    return title, tags, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="列出 notes/ 中的笔记标题，可搜索标题、标签和摘要。"
    )
    parser.add_argument(
        "keyword",
        nargs="?",
        help="只输出标题、标签或摘要中包含该关键词的笔记（英文不区分大小写）",
    )
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    args = parse_args()

    if not NOTES_DIR.is_dir():
        print(f"error: notes directory not found: {NOTES_DIR}", file=sys.stderr)
        return 1

    errors: list[str] = []
    for note_path in sorted(NOTES_DIR.glob("*.md")):
        try:
            title, tags, summary = read_search_fields(note_path)
            searchable_text = "\n".join((title, *tags, summary)).casefold()
            if args.keyword is None or args.keyword.casefold() in searchable_text:
                print(title)
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"{note_path.name}: {error}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
