#!/usr/bin/env python3
"""
ctbw_pipeline.py — Crypto Talk and Blockchain Walk transcription pipeline

For each video_*.md stub in corpus/videos/ that doesn't already have a
corresponding ctbw-*.md file:
  1. Parse YouTube ID from stub filename
  2. Fetch title + publish date via yt-dlp --dump-json
  3. Download audio via yt-dlp
  4. Transcribe with WhisperX (large-v2, int8, ARM-safe)
  5. Build .md with YAML frontmatter + ## Raw Transcript
  6. Delete intermediate .mp3
  7. Send to Hawat for Analysis section enrichment
  8. Verify enrichment
  9. Telegram status report

Usage:
  # Full run (all unprocessed stubs)
  python3 ctbw_pipeline.py

  # Single video test run
  python3 ctbw_pipeline.py --vid 6jTrzXxudWw

Deploy:
  scp ctbw_pipeline.py dylansagent@admins-mac-mini.tailafbd64.ts.net:~/.openclaw/workspace-business/corpus/ctbw_pipeline.py
"""

import argparse
import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────

workspace      = Path.home() / '.openclaw/workspace-business'
vault          = Path.home() / '.openclaw-vault/Hawat/corpus'
stubs_dir      = vault / 'ctbw'
output_dir     = vault / 'ctbw'
audio_dir      = workspace / 'corpus/ctbw/audio'
log_dir        = workspace / 'intelligence/log'

WHISPERX_ENV   = Path.home() / '.pyenv/versions/3.11.9/envs/whisperx-env/bin/whisperx'
TELEGRAM_TARGET = '476753866'

# ─── Logging ──────────────────────────────────────────────────────────────────

log_dir.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=log_dir / 'ctbw_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# ─── Helpers ──────────────────────────────────────────────────────────────────

def run_cmd(cmd, cwd=workspace, check=True, timeout=None):
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd,
            capture_output=True, text=True,
            check=check, timeout=timeout
        )
        logging.info(f"CMD OK: {cmd[:80]}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"CMD FAILED: {cmd[:80]} -> {e.stderr[:200]}")
        return None
    except subprocess.TimeoutExpired:
        logging.error(f"CMD TIMEOUT: {cmd[:80]}")
        return None


def send_telegram(message):
    subprocess.run(
        ['openclaw', 'message', 'send',
         '--channel', 'telegram',
         '--target', TELEGRAM_TARGET,
         '--message', message],
        cwd=workspace
    )


def fetch_video_metadata(vid):
    """Returns (episode_title, date_str) via yt-dlp --dump-json."""
    url = f'https://www.youtube.com/watch?v={vid}'
    try:
        result = subprocess.run(
            f"yt-dlp --dump-json '{url}'",
            shell=True, cwd=workspace,
            capture_output=True, text=True,
            check=True, timeout=30
        )
        data = json.loads(result.stdout)
        episode_title = data.get('title', '').strip()
        upload_date = data.get('upload_date', '')  # YYYYMMDD
        if upload_date and len(upload_date) == 8:
            date_str = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
        else:
            date_str = datetime.now().strftime('%Y-%m-%d')
            logging.warning(f"VID {vid}: No upload_date, using today")
        logging.info(f"VID {vid}: title='{episode_title}' date={date_str}")
        return episode_title, date_str
    except Exception as e:
        logging.error(f"VID {vid}: Metadata fetch failed: {e}")
        return '', datetime.now().strftime('%Y-%m-%d')


def build_md_content(vid, full_title, date_str, transcript_text):
    """Build .md content with YAML frontmatter + raw transcript."""
    safe_title = full_title.replace('"', "'")
    frontmatter = f"""---
title: "{safe_title}"
date: {date_str}
youtube_id: {vid}
guest: ""
source: ctbw
series: Crypto Talk and Blockchain Walk
---
"""
    body = f"## Raw Transcript\n\n{transcript_text.strip()}\n"
    return frontmatter + "\n" + body


ENRICHMENT_PROMPT = """I have a Crypto Talk and Blockchain Walk (CTBW) interview transcript file that needs a structured analysis section added.
CTBW is a walking interview series hosted by Dylan Grabowski at crypto conferences. Each episode features Dylan interviewing one guest while walking around the conference venue.
The file contains YAML frontmatter followed by a ## Raw Transcript section with flowing prose (no speaker labels — this is WhisperX transcription output, not diarized).

1. READ the full transcript carefully
2. EXTRACT the guest name from the transcript intro (usually "with [Name]" or "I'm here with [Name]" or similar walking interview opener) and UPDATE the guest field in the frontmatter
3. INSERT a structured analysis section AFTER the closing --- of the frontmatter and BEFORE the ## Raw Transcript header
4. Write the modified file back to disk

The analysis section format is exactly this:

---
## Analysis

### Summary
2-3 sentence overview of what this episode covered and its significance.

### Topics Covered
Structured list of main subjects discussed in order.

### Dylan's Takes & Opinions
Dylan's stated views, hot takes, predictions, and positions. Attribute clearly as opinion. Include direct evidence from the transcript.

### Guest Perspectives
Named guest and their key contributions, arguments, or positions. Always include this section — every CTBW episode has a guest.

### People & Projects Mentioned
Named individuals, companies, protocols, or projects — with brief context on who/what they are and why they were referenced.

### Recurring Themes
Macro-level ideas and narratives in this episode that likely appear across multiple CTBW episodes.

### Content Ideas & Future Topics
Anything Dylan mentioned wanting to cover, follow up on, or explore further.
---

Important rules:
- Preserve frontmatter EXACTLY as-is except UPDATE the guest field with the name you extract
- Preserve the ## Raw Transcript section and its content EXACTLY as-is
- Only INSERT the new analysis section between frontmatter and ## Raw Transcript
- Write directly back to the file on disk
- Do not spawn sub-agents. Process the file yourself directly."""


# ─── Main pipeline ────────────────────────────────────────────────────────────

def process_video(vid):
    log_prefix = f"VID {vid}: "
    audio_dir.mkdir(parents=True, exist_ok=True)

    # 1. Fetch metadata
    episode_title, date_str = fetch_video_metadata(vid)
    full_title = f"Crypto Talk and Blockchain Walk: {episode_title}" if episode_title else "Crypto Talk and Blockchain Walk"

    # 2. Download audio
    mp3_path = audio_dir / f'ctbw-{vid}.mp3'
    yt_cmd = (
        f"yt-dlp -f bestaudio --extract-audio --audio-format mp3 "
        f"-o '{mp3_path}' "
        f"'https://www.youtube.com/watch?v={vid}'"
    )
    run_cmd(yt_cmd, timeout=120)

    if not mp3_path.exists() or mp3_path.stat().st_size == 0:
        logging.error(log_prefix + "Audio download failed")
        send_telegram(f'FAILURE ctbw-{vid}: Audio download failed')
        return False

    logging.info(log_prefix + f"Audio downloaded: {mp3_path.stat().st_size} bytes")

    # 3. Transcribe with WhisperX
    txt_path = audio_dir / f'ctbw-{vid}.txt'
    whisper_cmd = (
        f"{WHISPERX_ENV} '{mp3_path}' "
        f"--model large-v2 "
        f"--language en "
        f"--compute_type int8 "
        f"--output_dir '{audio_dir}' "
        f"--output_format txt"
    )
    run_cmd(whisper_cmd, timeout=1800)  # 30 min max for long episodes

    if not txt_path.exists() or txt_path.stat().st_size == 0:
        logging.error(log_prefix + "Transcription failed — no .txt output")
        send_telegram(f'FAILURE ctbw-{vid}: Transcription failed')
        mp3_path.unlink(missing_ok=True)
        return False

    transcript_text = txt_path.read_text(encoding='utf-8')
    logging.info(log_prefix + f"Transcript: {len(transcript_text)} chars")

    # 4. Build .md
    md_filename = f'ctbw-{date_str}-{vid}.md'
    md_path = output_dir / md_filename
    md_content = build_md_content(vid, full_title, date_str, transcript_text)
    md_path.write_text(md_content, encoding='utf-8')

    if not md_path.exists() or md_path.stat().st_size == 0:
        logging.error(log_prefix + f".md write failed: {md_path}")
        send_telegram(f'FAILURE ctbw-{vid}: .md write failed')
        return False

    logging.info(log_prefix + f".md written: {md_path} ({md_path.stat().st_size} bytes)")

    # 5. Delete intermediates
    for tmp in [mp3_path, txt_path]:
        try:
            tmp.unlink()
            logging.info(log_prefix + f"Deleted: {tmp.name}")
        except OSError as e:
            logging.warning(log_prefix + f"Could not delete {tmp.name}: {e}")

    # Transcription complete — enrichment handled manually via Claude Code on MacBook
    logging.info(log_prefix + "SUCCESS — transcript written, ready for enrichment")
    send_telegram(f'SUCCESS ctbw-{vid}: {md_filename} written — ready for enrichment')
    return True




def get_unprocessed_vids():
    processed = set()
    for f in output_dir.glob('ctbw-*.md'):
        stem = f.stem
        # YouTube IDs are 11 chars; handle IDs with hyphens by checking stub filenames
        pass
    for stub in sorted(stubs_dir.glob('video_*.md')):
        vid = stub.stem.replace('video_', '')
        for f in output_dir.glob(f'ctbw-*-{vid}.md'):
            processed.add(vid)
    unprocessed = []
    for stub in sorted(stubs_dir.glob('video_*.md')):
        vid = stub.stem.replace('video_', '')
        if vid not in processed:
            unprocessed.append(vid)
    return unprocessed


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--vid', type=str)
    args = parser.parse_args()
    if args.vid:
        logging.info(f"Single video mode: {args.vid}")
        process_video(args.vid)
    else:
        vids = get_unprocessed_vids()
        logging.info(f"Batch mode: {len(vids)} unprocessed videos")
        print(f"Processing {len(vids)} videos: {vids}")
        if not vids:
            logging.info("Nothing to process")
            sys.exit(0)
        for vid in vids:
            process_video(vid)
    logging.info("Pipeline complete")
