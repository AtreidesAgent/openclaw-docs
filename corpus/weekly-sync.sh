#!/bin/bash
# Weekly corpus sync - all three sources
# Runs: Tue/Thu/Sat at 11:50 PM MT

set -e

CORPUS_DIR="/Users/dylansagent/.openclaw/workspace-business/corpus"
LOG_DIR="$CORPUS_DIR/log"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}-sync.log"

mkdir -p "$LOG_DIR"

echo "=== Corpus Sync Started: $(date) ===" >> "$LOG_FILE"

# 1. NNT Articles - fetch RSS pages 1-9 (incremental: only new items)
echo "[1/3] Fetching NNT RSS..." >> "$LOG_FILE"
cd "$CORPUS_DIR"
for page in $(seq 1 9); do
    curl -s "https://neonewstoday.com/author/dylan/feed/?paged=$page" \
        -o "$LOG_DIR/rss-page-${page}.xml" 2>/dev/null || true
done
python3 parse-articles-v2.py >> "$LOG_FILE" 2>&1

# 2. SEP Podcasts - Smart Economy playlist (last 30 days incremental)
echo "[2/3] Fetching SEP videos..." >> "$LOG_FILE"
python3 update-videos.py >> "$LOG_FILE" 2>&1

# 3. YouTube Channel - @GrabowskiDylan videos (last 30 days incremental)
echo "[3/3] Fetching YouTube channel videos..." >> "$LOG_FILE"
python3 update-channel-videos.py >> "$LOG_FILE" 2>&1

# 4. Regenerate master index (if script exists)
echo "[4/4] Regenerating master index..." >> "$LOG_FILE"
if [ -f "$CORPUS_DIR/generate-index.py" ]; then
    python3 "$CORPUS_DIR/generate-index.py" >> "$LOG_FILE" 2>&1
else
    echo "  NOTE: generate-index.py not found - skipping index regen" >> "$LOG_FILE"
fi

echo "=== Sync Complete: $(date) ===" >> "$LOG_FILE"

# Cleanup old logs (keep 30 days)
find "$LOG_DIR" -name "*.log" -mtime +30 -delete
