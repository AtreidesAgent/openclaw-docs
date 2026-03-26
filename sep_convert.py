#!/usr/bin/env python3
"""
SEP Transcript Converter
Converts raw sep-VIDEOID.txt files to structured .md files with YAML frontmatter.
Fetches title, date, and guest info via yt-dlp.
"""

import os
import re
import json
import subprocess
import sys
from pathlib import Path

CORPUS_DIR = Path.home() / ".openclaw-vault/Hawat/corpus/sep"
SHOW_NAME = "Smart Economy Podcast"
SOURCE = "youtube"
TYPE = "podcast-transcript"


def get_video_metadata(video_id: str) -> dict:
    """Fetch title, upload date, and uploader via yt-dlp."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "--print", "%(upload_date)s|%(title)s|%(uploader)s",
                "--skip-download",
                "--no-warnings",
                url,
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            print(f"  [WARN] yt-dlp failed for {video_id}: {result.stderr.strip()}")
            return {}

        line = result.stdout.strip()
        parts = line.split("|", 2)
        if len(parts) < 2:
            print(f"  [WARN] Unexpected yt-dlp output for {video_id}: {line!r}")
            return {}

        raw_date, title = parts[0], parts[1]
        uploader = parts[2] if len(parts) > 2 else ""

        # Convert YYYYMMDD -> YYYY-MM-DD
        date = ""
        if raw_date and len(raw_date) == 8 and raw_date.isdigit():
            date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"

        return {"title": title.strip(), "date": date, "uploader": uploader.strip()}

    except subprocess.TimeoutExpired:
        print(f"  [WARN] yt-dlp timed out for {video_id}")
        return {}
    except FileNotFoundError:
        print("[ERROR] yt-dlp not found. Is it installed and on PATH?")
        sys.exit(1)


def extract_guest(title: str) -> str:
    """Best-effort guest extraction from title using 'with [Name]' pattern."""
    match = re.search(r"\bwith\s+([A-Z][a-zA-Z\s\-'\.]+?)(?:\s*[|:\-,]|$)", title)
    if match:
        return match.group(1).strip()
    return ""


def convert_file(txt_path: Path) -> bool:
    """Convert a single .txt transcript to .md. Returns True if written, False if skipped."""
    # Extract video ID from filename: sep-VIDEOID.txt -> VIDEOID
    stem = txt_path.stem  # e.g. sep-H3YbnNtrN_c
    if not stem.startswith("sep-"):
        print(f"  [SKIP] Unexpected filename format: {txt_path.name}")
        return False

    video_id = stem[4:]  # strip "sep-"
    md_path = txt_path.with_suffix(".md")

    if md_path.exists():
        print(f"  [SKIP] Already exists: {md_path.name}")
        return False

    print(f"  [PROC] {txt_path.name} -> {md_path.name}")

    # Fetch metadata
    meta = get_video_metadata(video_id)
    title = meta.get("title", "")
    date = meta.get("date", "")
    guest = extract_guest(title) if title else ""
    link = f"https://www.youtube.com/watch?v={video_id}"

    # Read raw transcript
    raw_text = txt_path.read_text(encoding="utf-8")

    # Build frontmatter
    def yaml_str(val: str) -> str:
        # Wrap in quotes if value contains special chars
        if val and any(c in val for c in [':', '#', '[', ']', '{', '}', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'"]):
            escaped = val.replace('"', '\\"')
            return f'"{escaped}"'
        return f'"{val}"' if val else '""'

    frontmatter_lines = [
        "---",
        f"id: {video_id}",
        f"title: {yaml_str(title)}",
        f"date: {date}",
        f"show: {SHOW_NAME}",
        f"guest: {yaml_str(guest)}",
        f"link: {link}",
        f"source: {SOURCE}",
        f"type: {TYPE}",
        "---",
    ]
    frontmatter = "\n".join(frontmatter_lines)

    md_content = f"{frontmatter}\n\n## Raw Transcript\n{raw_text}\n"
    md_path.write_text(md_content, encoding="utf-8")
    return True


def main():
    if not CORPUS_DIR.exists():
        print(f"[ERROR] Corpus directory not found: {CORPUS_DIR}")
        sys.exit(1)

    txt_files = sorted(CORPUS_DIR.glob("sep-*.txt"))
    total = len(txt_files)
    print(f"Found {total} .txt files in {CORPUS_DIR}\n")

    written = 0
    skipped = 0
    errors = 0

    for i, txt_path in enumerate(txt_files, 1):
        print(f"[{i}/{total}] {txt_path.name}")
        try:
            result = convert_file(txt_path)
            if result:
                written += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  [ERROR] {e}")
            errors += 1

    print(f"\n--- Summary ---")
    print(f"  Written : {written}")
    print(f"  Skipped : {skipped}  (already existed)")
    print(f"  Errors  : {errors}")
    print(f"  Total   : {total}")


if __name__ == "__main__":
    main()
