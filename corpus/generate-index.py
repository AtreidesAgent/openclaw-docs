#!/usr/bin/env python3
"""
generate-index.py — Hawat corpus master index generator
Scans all corpus folders and writes a complete index.md Hawat can search.
Run manually or automatically at end of weekly-sync.sh.
"""

import os
import re
import json
import subprocess
from datetime import datetime
from pathlib import Path

CORPUS_DIR = Path.home() / ".openclaw-vault" / "Hawat" / "corpus"
SEP_DIR = CORPUS_DIR / "sep"
VIDEOS_DIR = CORPUS_DIR / "videos"
ARTICLES_DIR = CORPUS_DIR / "articles"
STREAMS_DIR = CORPUS_DIR / "streams"
PODCASTS_DIR = CORPUS_DIR / "podcasts"
INDEX_FILE = CORPUS_DIR / "index.md"

# ── HELPERS ───────────────────────────────────────────────

def slug_date(path):
    """Try to extract a YYYY-MM-DD date from a filename."""
    m = re.search(r'(\d{4}-\d{2}-\d{2})', path.name)
    return m.group(1) if m else "unknown"

def first_nonempty_line(path, max_lines=5):
    """Return the first non-empty line of a file."""
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f):
                line = line.strip()
                if line and not line.startswith("<!--"):
                    return line
                if i > max_lines:
                    break
    except Exception:
        pass
    return ""

def extract_md_field(path, field):
    """Extract a value from a markdown file by searching for '## Field' sections."""
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            content = f.read()
        # Look for the field as a header and grab the first bullet or line after it
        pattern = rf'##\s+{re.escape(field)}\s*\n(.*?)(?=\n##|\Z)'
        m = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if m:
            block = m.group(1).strip()
            # Return first bullet item or first line
            first = block.split('\n')[0].lstrip('-• ').strip()
            return first[:120]
    except Exception:
        pass
    return ""

def get_yt_metadata(video_id):
    """
    Use yt-dlp --dump-json to get title and upload_date for a YouTube video.
    Returns (title, date_str) or (None, None) on failure.
    Caches results in memory during this run to avoid duplicate calls.
    """
    if video_id in _yt_cache:
        return _yt_cache[video_id]
    try:
        result = subprocess.run(
            ["yt-dlp", "--dump-json", "--no-playlist",
             f"https://www.youtube.com/watch?v={video_id}"],
            capture_output=True, text=True, timeout=20
        )
        if result.returncode == 0 and result.stdout.strip():
            data = json.loads(result.stdout.strip().split('\n')[0])
            title = data.get("title", "")
            raw_date = data.get("upload_date", "")  # YYYYMMDD
            if raw_date and len(raw_date) == 8:
                date_str = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
            else:
                date_str = "unknown"
            _yt_cache[video_id] = (title, date_str)
            return title, date_str
    except Exception:
        pass
    _yt_cache[video_id] = (None, None)
    return None, None

_yt_cache = {}

# ── SECTION BUILDERS ──────────────────────────────────────

def build_sep_section():
    lines = ["## SEP Podcast (Smart Economy Podcast)\n"]
    lines.append(f"*Transcript files in `sep/`*\n")
    lines.append("| Episode | Title | Date | File |")
    lines.append("|---------|-------|------|------|")

    entries = []
    for f in sorted(SEP_DIR.glob("sep-*.txt")):
        video_id = f.stem.replace("sep-", "")
        size = f.stat().st_size
        suspect = " ⚠️" if size < 10000 else ""

        title, date_str = get_yt_metadata(video_id)
        if not title:
            # Fall back to first line of transcript, truncated
            snippet = first_nonempty_line(f)
            title = (snippet[:80] + "…") if len(snippet) > 80 else snippet or video_id
        if not date_str or date_str == "unknown":
            date_str = "unknown"

        entries.append((date_str, video_id, title, f.name, suspect))

    # Sort by date descending (unknown dates go to bottom)
    entries.sort(key=lambda x: x[0] if x[0] != "unknown" else "0000", reverse=True)

    for i, (date_str, video_id, title, fname, suspect) in enumerate(entries, 1):
        safe_title = title.replace("|", "–")[:80]
        lines.append(f"| {i} | {safe_title}{suspect} | {date_str} | `sep/{fname}` |")

    lines.append(f"\n*Total: {len(entries)} episodes*\n")
    return "\n".join(lines)


def build_videos_section():
    lines = ["## YouTube Videos (@GrabowskiDylan)\n"]
    lines.append(f"*Transcript files in `videos/`*\n")
    lines.append("| # | Title | Date | File |")
    lines.append("|---|-------|------|------|")

    entries = []
    for f in sorted(VIDEOS_DIR.glob("grabowski-*.txt")):
        video_id = f.stem.replace("grabowski-", "")
        title, date_str = get_yt_metadata(video_id)
        if not title:
            snippet = first_nonempty_line(f)
            title = (snippet[:80] + "…") if len(snippet) > 80 else snippet or video_id
        if not date_str or date_str == "unknown":
            date_str = "unknown"
        entries.append((date_str, video_id, title, f.name))

    entries.sort(key=lambda x: x[0] if x[0] != "unknown" else "0000", reverse=True)

    for i, (date_str, video_id, title, fname) in enumerate(entries, 1):
        safe_title = title.replace("|", "–")[:80]
        lines.append(f"| {i} | {safe_title} | {date_str} | `videos/{fname}` |")

    lines.append(f"\n*Total: {len(entries)} videos*\n")
    return "\n".join(lines)


def build_articles_section():
    lines = ["## Articles (Neo News Today)\n"]
    lines.append(f"*Markdown files in `articles/`*\n")
    lines.append("| Title | Date | File |")
    lines.append("|-------|------|------|")

    entries = []
    missing = []
    for f in sorted(ARTICLES_DIR.glob("*.md")):
        if f.name == "index.md":
            continue
        if not f.exists():
            missing.append(f.name)
            continue

        # Try to get title and date from frontmatter or first heading
        title = ""
        date_str = "unknown"
        try:
            with open(f, encoding="utf-8", errors="ignore") as fh:
                content = fh.read(2000)
            # frontmatter title
            m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
            if m:
                title = m.group(1).strip()
            # frontmatter date
            m = re.search(r'^date:\s*["\']?(\d{4}-\d{2}-\d{2})', content, re.MULTILINE)
            if m:
                date_str = m.group(1)
            # fallback: first # heading
            if not title:
                m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                if m:
                    title = m.group(1).strip()
            # fallback: first non-empty line
            if not title:
                title = first_nonempty_line(f)
        except Exception:
            pass

        if not title:
            title = f.stem
        entries.append((date_str, title[:100], f.name))

    entries.sort(key=lambda x: x[0] if x[0] != "unknown" else "0000", reverse=True)

    for date_str, title, fname in entries:
        safe_title = title.replace("|", "–")
        lines.append(f"| {safe_title} | {date_str} | `articles/{fname}` |")

    lines.append(f"\n*Total: {len(entries)} articles*")

    if missing:
        lines.append(f"\n> ⚠️ {len(missing)} files listed in index but not found on disk.")

    lines.append("")
    return "\n".join(lines)


def build_streams_section():
    lines = ["## Live Streams (Daily Digital Download)\n"]
    lines.append(f"*Markdown files in `streams/`*\n")
    lines.append("| Date | Topics | File |")
    lines.append("|------|--------|------|")

    entries = []
    for f in sorted(STREAMS_DIR.glob("*.md")):
        if f.name == "index.md":
            continue
        date_str = slug_date(f)
        # Grab first topic bullet as summary
        topics_snippet = extract_md_field(f, "Topics Covered")
        if not topics_snippet:
            topics_snippet = first_nonempty_line(f)
        entries.append((date_str, topics_snippet[:100], f.name))

    entries.sort(key=lambda x: x[0] if x[0] != "unknown" else "0000", reverse=True)

    for date_str, topics, fname in entries:
        safe_topics = topics.replace("|", "–")
        lines.append(f"| {date_str} | {safe_topics}… | `streams/{fname}` |")

    lines.append(f"\n*Total: {len(entries)} streams*\n")
    return "\n".join(lines)


def build_podcasts_section():
    files = [f for f in PODCASTS_DIR.glob("*") if f.name != "index.md" and f.is_file()]
    lines = ["## Podcasts (External / Guest Appearances)\n"]
    if not files:
        lines.append("*No podcast files indexed yet. Add `.md` files to `podcasts/`.*\n")
    else:
        lines.append("| Title | Date | File |")
        lines.append("|-------|------|------|")
        for f in sorted(files):
            title = first_nonempty_line(f) or f.stem
            date_str = slug_date(f)
            lines.append(f"| {title[:80]} | {date_str} | `podcasts/{f.name}` |")
        lines.append(f"\n*Total: {len(files)} podcasts*\n")
    return "\n".join(lines)


# ── MAIN ──────────────────────────────────────────────────

def main():
    print(f"[generate-index] Starting index generation...")
    print(f"[generate-index] Corpus: {CORPUS_DIR}")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    sections = []
    sections.append(f"# Hawat Corpus Index\n")
    sections.append(f"*Generated: {now}*\n")
    sections.append(f"*This index is auto-generated by `generate-index.py`. Do not edit manually.*\n")
    sections.append("---\n")

    print("[generate-index] Building SEP section (fetching YouTube metadata)...")
    sections.append(build_sep_section())

    print("[generate-index] Building videos section...")
    sections.append(build_videos_section())

    print("[generate-index] Building articles section...")
    sections.append(build_articles_section())

    print("[generate-index] Building streams section...")
    sections.append(build_streams_section())

    print("[generate-index] Building podcasts section...")
    sections.append(build_podcasts_section())

    # Write index
    output = "\n---\n".join(sections)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"[generate-index] Done. Index written to {INDEX_FILE}")

    # Quick summary
    sep_count = len(list(SEP_DIR.glob("sep-*.txt")))
    vid_count = len(list(VIDEOS_DIR.glob("grabowski-*.txt")))
    art_count = len(list(ARTICLES_DIR.glob("*.md")))
    stream_count = len(list(STREAMS_DIR.glob("*.md")))
    print(f"[generate-index] Summary: {sep_count} SEP | {vid_count} videos | {art_count} articles | {stream_count} streams")


if __name__ == "__main__":
    main()
