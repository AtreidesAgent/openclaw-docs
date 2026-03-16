#!/usr/bin/env python3
"""
YouTube video transcript fetcher for SEP playlist
"""
import os, re, json, subprocess
from datetime import datetime, timezone

CORPUS_DIR = "/Users/dylansagent/.openclaw-vault/Hawat/corpus"
VIDEOS_DIR = os.path.join(CORPUS_DIR, "sep")
LOG_DIR = os.path.join(CORPUS_DIR, "log")

SEP_PLAYLIST = "PLSSG0GCRt4pxxVye5Mi4dWx8n73wWx5mu"
YT_DIR = os.path.join(CORPUS_DIR, "youtube")

os.makedirs(VIDEOS_DIR, exist_ok=True)
os.makedirs(YT_DIR, exist_ok=True)

def get_existing_videos():
    existing = set()
    if not os.path.exists(VIDEOS_DIR):
        return existing
    for fname in os.listdir(VIDEOS_DIR):
        if fname.startswith('sep-') and fname.endswith('.txt'):
            m = re.match(r'sep-([\w-]+)\.txt$', fname)
            if m:
                existing.add(m.group(1))
    return existing

def fetch_playlist():
    url = f"https://www.youtube.com/playlist?list={SEP_PLAYLIST}"
    cmd = ["yt-dlp", "--flat-playlist", "--print", "%(id)s", url]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        ids = [vid.strip() for vid in result.stdout.strip().split('\n') if vid.strip()]
        return ids
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_video_info(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    cmd = ["yt-dlp", "--skip-download", "--simulate",
           "--print", "%(title)s|%(upload_date)s",
           url]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        parts = result.stdout.strip().split('|')
        title = parts[0] if parts else ""
        upload = parts[1] if len(parts) > 1 else ""
        date = ""
        if upload and len(upload) == 8:
            date = f"{upload[:4]}-{upload[4:6]}-{upload[6:8]}"
        return {'id': video_id, 'title': title, 'pubDate': date}
    except Exception as e:
        return None

def get_transcript(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    cmd = ["yt-dlp", "--skip-download", "--write-auto-sub", "--write-sub",
           "--sub-lang", "en", "--sub-format", "vtt",
           "-o", f"{YT_DIR}/%(id)s.%(ext)s", url]
    try:
        subprocess.run(cmd, capture_output=True, timeout=120)
        for ext in ['.en.vtt', '.vtt']:
            vtt_path = os.path.join(YT_DIR, f"{video_id}{ext}")
            if os.path.exists(vtt_path):
                return vtt_path
    except Exception as e:
        pass
    return None

def clean_vtt(vtt_path):
    try:
        with open(vtt_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        lines = []
        seen = set()
        for line in content.split('\n'):
            line = line.strip()
            if re.match(r'^WEBVTT', line):
                continue
            if re.match(r'^Kind:', line):
                continue
            if re.match(r'^Language:', line):
                continue
            if re.match(r'^\d{2}:\d{2}:\d{2}', line):
                continue
            line = re.sub(r'<[^>]+>', '', line)
            if line and line not in seen:
                lines.append(line)
                seen.add(line)
        return '\n'.join(lines)
    except:
        return ""

def update_corpus():
    existing = get_existing_videos()
    print(f"Loaded {len(existing)} existing SEP transcripts")
    
    all_ids = fetch_playlist()
    print(f"Found {len(all_ids)} videos in playlist")
    
    new_ids = [vid for vid in all_ids if vid not in existing]
    print(f"{len(new_ids)} new videos to process")
    
    if not new_ids:
        print("No new videos found")
        return
    
    processed = []
    for vid in new_ids:
        info = get_video_info(vid)
        if not info:
            continue
        print(f"Processing: {info['title'][:50]}...")
        
        vtt_path = get_transcript(vid)
        if vtt_path:
            transcript = clean_vtt(vtt_path)
            fname = f"sep-{vid}.txt"
            fpath = os.path.join(VIDEOS_DIR, fname)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(f"Title: {info['title']}\n")
                f.write(f"Date: {info['pubDate']}\n")
                f.write(f"URL: https://www.youtube.com/watch?v={vid}\n")
                f.write(f"Transcript:\n\n")
                f.write(transcript)
            processed.append(vid)
            print(f"  Saved: {fname}")
        else:
            print(f"  No transcript available")
    
    log_path = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}-sep-update.json")
    with open(log_path, 'w') as f:
        json.dump({'new': len(processed), 'videos': processed}, f, indent=2)
    print(f"Created {len(processed)} new transcripts")

if __name__ == "__main__":
    update_corpus()
