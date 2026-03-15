#!/usr/bin/env python3
"""
YouTube channel video fetcher - @GrabowskiDylan videos
Fetches new videos from the channel with transcripts
"""
import os, re, json, subprocess
from datetime import datetime, timezone, timedelta

CORPUS_DIR = "/Users/dylansagent/.openclaw-vault/Hawat/corpus"
VIDEOS_DIR = os.path.join(CORPUS_DIR, "videos")
LOG_DIR = os.path.join(CORPUS_DIR, "log")
YT_DIR = os.path.join(CORPUS_DIR, "youtube")

# Dylan's YouTube channel
CHANNEL_ID = "UCRf7T6ccMKKgI2tGb6hr8eQ"

def get_existing_videos():
    """Get set of existing video IDs from channel videos only"""
    existing_ids = set()
    
    if not os.path.exists(VIDEOS_DIR):
        return existing_ids
    
    for fname in os.listdir(VIDEOS_DIR):
        if fname.startswith('channel_') and fname.endswith('.md'):
            m = re.match(r'channel_(\w+)\.md', fname)
            if m:
                existing_ids.add(m.group(1).upper())
        
    return existing_ids

def fetch_channel_videos():
    """Fetch video IDs from channel (last 50 videos)"""
    url = f"https://www.youtube.com/channel/{CHANNEL_ID}/videos"
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--playlist-end", "50",
        "--print", "%(id)s",
        url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        ids = [vid.upper() for vid in result.stdout.strip().split('\n') if vid.strip()]
        return ids
    except Exception as e:
        print(f"Error fetching channel: {e}")
        return []

def get_video_info(video_id):
    """Get video metadata"""
    url = f"https://www.youtube.com/watch?v={video_id}"
    cmd = [
        "yt-dlp", "--skip-download", "--simulate",
        "--print", "%(title)s|%(upload_date)s|%(channel)s|%(duration)s",
        "-o", "/dev/null",
        url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        parts = result.stdout.strip().split('|')
        if len(parts) >= 2:
            title = parts[0]
            upload = parts[1]
            channel = parts[2] if len(parts) > 2 else ""
            duration = parts[3] if len(parts) > 3 else ""
            
            date = ""
            if upload and len(upload) == 8:
                try:
                    dt = datetime.strptime(upload, "%Y%m%d")
                    date = dt.strftime("%Y-%m-%d")
                except:
                    pass
            
            return {
                'id': video_id, 
                'title': title, 
                'pubDate': date, 
                'channel': channel, 
                'duration': duration
            }
    except Exception as e:
        pass
    return None

def get_transcript(video_id):
    """Download transcript/subtitles for video"""
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    cmd = [
        "yt-dlp", "--skip-download",
        "--write-auto-sub", "--write-sub",
        "--sub-lang", "en", "--sub-format", "vtt",
        "-o", f"{YT_DIR}/%(id)s.%(ext)s",
        url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        # Check for subtitle files
        for ext in ['.en.vtt', '.en-US.vtt', '.en-gb.vtt', '.vtt']:
            vtt_path = os.path.join(YT_DIR, f"{video_id}{ext}")
            if os.path.exists(vtt_path):
                return vtt_path
        return None
    except Exception as e:
        return None

def clean_vtt_content(vtt_path):
    """Extract clean text from VTT file"""
    try:
        with open(vtt_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        lines = []
        seen = set()
        
        for line in content.split('\n'):
            line = line.strip()
            if re.match(r'^WEBVTT', line): continue
            if re.match(r'^Kind:', line): continue
            if re.match(r'^Language:', line): continue
            if re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3}', line): continue
            line = re.sub(r'<[^>]+>', '', line)
            line = line.strip()
            if line and line not in seen:
                lines.append(line)
                seen.add(line)
        
        return ' '.join(lines)[:3000]
    except:
        return ""

def generate_overview(transcript):
    """Generate brief overview from transcript"""
    if not transcript or len(transcript) < 50:
        return "(Transcript not available)"
    sentences = [s.strip() for s in transcript.split('.') if len(s.strip()) > 20]
    if sentences:
        return '. '.join(sentences[:3]) + '.' if len(sentences) >= 3 else sentences[0] + '.'
    return transcript[:200] + "..."

def update_corpus():
    """Main update workflow"""
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    os.makedirs(YT_DIR, exist_ok=True)
    
    existing_ids = get_existing_videos()
    print(f"Loaded {len(existing_ids)} existing channel videos")
    
    # Fetch videos from channel
    all_ids = fetch_channel_videos()
    print(f"Found {len(all_ids)} videos on channel")
    
    # Filter to new videos
    new_ids = [vid for vid in all_ids if vid not in existing_ids]
    print(f"{len(new_ids)} new videos to process")
    
    if not new_ids:
        print("No new videos found.")
        return []
    
    # Process last 30 days only
    cutoff = datetime.now(timezone.utc) - timedelta(days=30)
    processed = []
    
    for vid in new_ids:
        info = get_video_info(vid)
        if not info or not info['pubDate']:
            continue
        
        vid_date = datetime.strptime(info['pubDate'], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        if vid_date < cutoff:
            print(f"Skipping old video: {info['title'][:50]}... ({info['pubDate']})")
            continue
        
        print(f"Processing: {info['title'][:50]}...")
        
        # Get transcript
        vtt_path = get_transcript(vid)
        transcript = clean_vtt_content(vtt_path) if vtt_path else ""
        overview = generate_overview(transcript)
        
        # Create markdown
        fname = f"channel_{vid}.md"
        fpath = os.path.join(VIDEOS_DIR, fname)
        
        md = f"""---
title: "{info['title'].replace('"', '\\"')}"
date: {info['pubDate']}
url: https://www.youtube.com/watch?v={vid}
tags: [channel, blockchain]
source: youtube_channel
---

# {info['title']}

**Published:** {info['pubDate']}
**Channel:** {info['channel']}
**Duration:** {info['duration']}

## Overview

{overview}

## Transcript

{transcript if len(transcript) < 2000 else transcript[:2000] + "..."}

---
*Corpus updated {datetime.now().isoformat()}*
"""
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(md)
        
        processed.append({
            'id': vid, 
            'title': info['title'], 
            'date': info['pubDate'],
            'source': 'channel'
        })
        print(f"  Saved: videos/{fname}")
    
    # Save log
    log_path = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}-channel-update.json")
    with open(log_path, 'w') as f:
        json.dump({'new_videos': len(processed), 'videos': processed}, f, indent=2)
    
    print(f"\nCreated {len(processed)} new channel video entries")
    return processed

if __name__ == "__main__":
    update_corpus()
