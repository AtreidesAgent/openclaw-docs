#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import feedparser
import logging
from pathlib import Path

# Setup
workspace = Path.home() / '.openclaw/workspace-business'
raw_dir = workspace / 'intelligence/weekly/transcripts/raw'
clean_dir = workspace / 'corpus/sep'
themes_dir = workspace / 'intelligence/themes'
log_dir = workspace / 'intelligence/log'
log_dir.mkdir(parents=True, exist_ok=True)
clean_script = workspace / 'clean_vtt.py'

logging.basicConfig(
    filename=log_dir / 'scrape_sep.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def run_cmd(cmd, cwd=workspace, check=True, timeout=None):
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, check=check, timeout=timeout)
        logging.info(f"CMD: {cmd} -> SUCCESS")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"CMD: {cmd} -> FAILED: {e.stderr}")
        return None
    except subprocess.TimeoutExpired:
        logging.error(f"CMD: {cmd} -> TIMEOUT")
        return None

# 1. Fetch RSS
rss_url = 'https://www.youtube.com/feeds/videos.xml?playlist_id=PLSSG0GCRt4pxxVye5Mi4dWx8n73wWx5mu'
feed = feedparser.parse(rss_url)
video_ids = [entry['yt_videoid'] for entry in feed.entries]
logging.info(f"Playlist: {len(video_ids)} videos")

# 2. Existing
existing = set()
for f in clean_dir.glob('sep-*.txt'):
    vid = f.stem.split('-', 1)[1]
    existing.add(vid)
logging.info(f"Existing cleaned: {len(existing)}")

new_ids = [vid for vid in video_ids if vid not in existing]
logging.info(f"New episodes: {len(new_ids)}: {new_ids}")

if not new_ids:
    logging.info("No new episodes")
    sys.exit(0)

# Ensure dirs
for d in [raw_dir, clean_dir, themes_dir]:
    d.mkdir(parents=True, exist_ok=True)

for vid in new_ids:
    log_prefix = f"VID {vid}: "
    
    # 3. Download VTT
    url = f'https://www.youtube.com/watch?v={vid}'
    vtt_file = raw_dir / f'sep-{vid}.en.vtt'
    yt_cmd = f"yt-dlp --write-auto-sub --sub-lang en --sub-format vtt --skip-download --restrict-filenames -o '{raw_dir / 'sep-%(id)s.%(ext)s'}' '{url}'"
    run_cmd(yt_cmd)
    
    vtt_path = raw_dir / f'sep-{vid}.en.vtt'
    if not vtt_path.exists():
        logging.error(log_prefix + "No VTT downloaded")
        subprocess.run(['openclaw', 'message', 'send', '--channel', 'telegram', '--target', '476753866', '--message', f'FAILURE sep-{vid}: No VTT'], cwd=workspace)
        continue
    
    # 4. Clean
    txt_path = clean_dir / f'sep-{vid}.txt'
    clean_cmd = f"python3 '{clean_script}' --input '{vtt_path}' --output '{txt_path}'"
    run_cmd(clean_cmd, timeout=60)
    
    # Robust check
    if not txt_path.exists():
        logging.error(log_prefix + "TXT file not created")
        subprocess.run(['openclaw', 'message', 'send', '--channel', 'telegram', '--target', '476753866', '--message', f'FAILURE sep-{vid}: Clean - no TXT'], cwd=workspace)
        continue
    
    try:
        size = txt_path.stat().st_size
        if size == 0:
            logging.error(log_prefix + "TXT file empty (0 bytes)")
            subprocess.run(['openclaw', 'message', 'send', '--channel', 'telegram', '--target', '476753866', '--message', f'FAILURE sep-{vid}: Clean - empty TXT'], cwd=workspace)
            continue
        logging.info(log_prefix + f"TXT OK ({size} bytes)")
    except OSError as e:
        logging.error(log_prefix + f"TXT stat failed: {e}")
        subprocess.run(['openclaw', 'message', 'send', '--channel', 'telegram', '--target', '476753866', '--message', f'FAILURE sep-{vid}: Clean - stat error'], cwd=workspace)
        continue
    
    # 5. Theme extraction
    theme_path = themes_dir / f'sep-{vid}_themes.md'
    msg = f"Extract exactly 9 substantive, distinct themes from '{txt_path}' (SEP episode). Write to '{theme_path}'. Match On The Brink format: # sep-{vid}_themes.md then numbered list."
    agent_cmd = f"openclaw agent --agent hawat --message '{msg}'"
    run_cmd(agent_cmd)
    
    # 6. Wait 6 min
    logging.info(log_prefix + "Waiting 6min for themes...")
    time.sleep(360)
    
    # 7/8. Check
    if theme_path.exists() and theme_path.stat().st_size > 400:
        logging.info(log_prefix + "SUCCESS")
        subprocess.run(['openclaw', 'message', 'send', '--channel', 'telegram', '--target', '476753866', '--message', f'SUCCESS sep-{vid}: {theme_path}'], cwd=workspace)
    else:
        logging.error(log_prefix + "FAILURE: No/invalid theme file")
        subprocess.run(['openclaw', 'message', 'send', '--channel', 'telegram', '--target', '476753866', '--message', f'FAILURE sep-{vid}: Theme missing/small ({theme_path})'], cwd=workspace)

logging.info("Script complete")