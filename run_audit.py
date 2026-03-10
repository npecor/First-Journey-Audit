#!/usr/bin/env python3
"""Generate a paste-ready landing page audit prompt."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

MAX_VISIBLE_TEXT_CHARS = 6000
MAX_LINK_TEXTS = 20


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def fetch_html(url: str) -> str:
    response = requests.get(url, timeout=20, headers={"User-Agent": "First-Journey-Audit"})
    response.raise_for_status()
    return response.text


def clean_text_items(items: list[str], limit: int) -> list[str]:
    seen: set[str] = set()
    cleaned: list[str] = []
    for item in items:
        text = " ".join(item.split())
        if not text or text in seen:
            continue
        seen.add(text)
        cleaned.append(text)
        if len(cleaned) >= limit:
            break
    return cleaned


def extract_page_snapshot(html: str) -> dict[str, object]:
    soup = BeautifulSoup(html, "html.parser")

    for tag_name in ["script", "style", "noscript", "svg"]:
        for tag in soup.find_all(tag_name):
            tag.decompose()

    title = ""
    if soup.title and soup.title.string:
        title = " ".join(soup.title.string.split())

    h1s = clean_text_items([tag.get_text(" ", strip=True) for tag in soup.find_all("h1")], 5)
    h2s = clean_text_items([tag.get_text(" ", strip=True) for tag in soup.find_all("h2")], 10)

    button_and_link_texts = clean_text_items(
        [tag.get_text(" ", strip=True) for tag in soup.find_all(["button", "a"])],
        MAX_LINK_TEXTS,
    )

    visible_text = " ".join(soup.stripped_strings)
    visible_text = " ".join(visible_text.split())
    if len(visible_text) > MAX_VISIBLE_TEXT_CHARS:
        visible_text = visible_text[:MAX_VISIBLE_TEXT_CHARS].rsplit(" ", 1)[0] + " ..."

    return {
        "title": title,
        "h1s": h1s,
        "h2s": h2s,
        "button_and_link_texts": button_and_link_texts,
        "visible_text": visible_text,
    }


def format_list(label: str, items: list[str]) -> str:
    if not items:
        return f"{label}:\n- None found"
    return f"{label}:\n" + "\n".join(f"- {item}" for item in items)


def build_prompt(url: str, snapshot: dict[str, object], rubric: str, expert_prompt: str, notes: str | None) -> str:
    parts = [
        "AUDIT TASK",
        f"Evaluate this landing page URL: {url}",
        "",
        "AUDIT RUBRIC",
        rubric,
        "",
        "AUDITOR INSTRUCTIONS",
        expert_prompt,
        "",
        "PAGE SNAPSHOT",
        f"Title: {snapshot['title'] or 'None found'}",
        format_list("H1s", snapshot["h1s"]),
        format_list("H2s", snapshot["h2s"]),
        format_list("Button and link texts", snapshot["button_and_link_texts"]),
        "Visible page text:",
        snapshot["visible_text"] or "None found",
    ]

    if notes:
        parts.extend(["", "OPTIONAL ONBOARDING NOTES", notes])

    return "\n".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a landing page and print a structured audit prompt.",
        usage="python3 run_audit.py <url> [--notes path/to/notes.txt]",
    )
    parser.add_argument("url", help="Landing page URL to audit")
    parser.add_argument("--notes", help="Optional path to a local onboarding notes text file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base_dir = Path(__file__).resolve().parent

    try:
        rubric = read_text(base_dir / "rubric.md")
        expert_prompt = read_text(base_dir / "prompt.md")
        notes = read_text(Path(args.notes).expanduser()) if args.notes else None
        html = fetch_html(args.url)
        snapshot = extract_page_snapshot(html)
    except FileNotFoundError as exc:
        print(f"Error: file not found: {exc.filename}", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"Error: failed to fetch URL: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Error: could not read file: {exc}", file=sys.stderr)
        return 1

    print(build_prompt(args.url, snapshot, rubric, expert_prompt, notes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
