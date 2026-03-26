#!/usr/bin/env python3
"""
generate-index.py — Hawat Corpus Index Generator
Generates a searchable index of the SEP corpus.
Reads sep-*.md files and extracts metadata from YAML frontmatter.

Called by: weekly-sync.sh (Tue/Thu/Sat 11:50pm)
Output: corpus/indices/sep-index.md

CHANGELOG:
- Updated to index sep-*.md instead of sep-*.txt
- Reads title/date/guest from YAML frontmatter instead of raw text scraping
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

# ── Paths ──────────────────────────────────────────────────────────────────────
CORPUS_DIR = Path.home() / ".openclaw-vault/Hawat/corpus/sep"
INDICES_DIR = Path.home() / ".openclaw-vault/Hawat/corpus/indices"
OUTPUT_FILE = INDICES_DIR / "sep-index.md"

# ── YAML frontmatter parser ────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter fields from a markdown file string."""
    meta = {}
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return meta
    block = match.group(1)
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        meta[key] = val
    return meta


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    if not CORPUS_DIR.exists():
        print(f"[ERROR] SEP corpus directory not found: {CORPUS_DIR}")
        sys.exit(1)

    INDICES_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(CORPUS_DIR.glob("sep-*.md"))
    total = len(md_files)
    print(f"Indexing {total} SEP .md files from {CORPUS_DIR}")

    entries = []
    errors = []

    for md_path in md_files:
        try:
            text = md_path.read_text(encoding="utf-8")
            meta = parse_frontmatter(text)

            video_id = meta.get("id", md_path.stem.removeprefix("sep-"))
            title    = meta.get("title", "")
            date     = meta.get("date", "")
            guest    = meta.get("guest", "")
            link     = meta.get("link", f"https://www.youtube.com/watch?v={video_id}")

            entries.append({
                "filename": md_path.name,
                "id":       video_id,
                "title":    title,
                "date":     date,
                "guest":    guest,
                "link":     link,
            })
        except Exception as e:
            errors.append((md_path.name, str(e)))
            print(f"  [WARN] Could not parse {md_path.name}: {e}")

    # Sort by date descending (empty dates go last)
    entries.sort(key=lambda e: e["date"] or "0000-00-00", reverse=True)

    # ── Write index ────────────────────────────────────────────────────────────
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# SEP Corpus Index",
        f"Generated: {now}  ",
        f"Episodes indexed: {len(entries)}  ",
        "",
        "| Date | Title | Guest | File | Link |",
        "|------|-------|-------|------|------|",
    ]

    for e in entries:
        date    = e["date"]  or "unknown"
        title   = e["title"] or e["id"]
        guest   = e["guest"] or "—"
        fname   = e["filename"]
        link    = e["link"]
        # Escape pipes in cell values
        title_s = title.replace("|", "\\|")
        guest_s = guest.replace("|", "\\|")
        lines.append(f"| {date} | {title_s} | {guest_s} | `{fname}` | [▶]({link}) |")

    if errors:
        lines += [
            "",
            "## Parse Errors",
            f"{len(errors)} file(s) could not be parsed:",
        ]
        for fname, err in errors:
            lines.append(f"- `{fname}`: {err}")

    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Index written to {OUTPUT_FILE}")
    print(f"  Indexed : {len(entries)}")
    print(f"  Errors  : {len(errors)}")


if __name__ == "__main__":
    main()
