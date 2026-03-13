#!/bin/bash
# weekly-sync.sh — Hawat corpus sync
# Runs: Tue/Thu/Sat at 11:50 PM MT via cron:
#   50 23 * * 2,4,6 /bin/bash /Users/dylansagent/.openclaw-vault/Hawat/corpus/weekly-sync.sh

set -euo pipefail

# ── CONFIG ────────────────────────────────────────────────
CORPUS_DIR="$HOME/.openclaw-vault/Hawat/corpus"
SEP_DIR="$CORPUS_DIR/sep"
VIDEOS_DIR="$CORPUS_DIR/videos"
LOG_DIR="$CORPUS_DIR/log"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}-sync.log"
MIN_TRANSCRIPT_BYTES=10000   # Flag transcripts smaller than this as suspect

# ── SETUP ─────────────────────────────────────────────────
mkdir -p "$LOG_DIR" "$SEP_DIR" "$VIDEOS_DIR"

log() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG_FILE"; }
log_section() { echo "" >> "$LOG_FILE"; log "══ $* ══"; }
die() { log "ERROR: $*"; exit 1; }

[ -d "$CORPUS_DIR" ] || die "Corpus dir not found: $CORPUS_DIR"

log "=== Corpus Sync Started: $(date) ==="
log "Corpus root: $CORPUS_DIR"
cd "$CORPUS_DIR"

# ── 1. NNT ARTICLES ───────────────────────────────────────
log_section "1/4 Fetching NNT articles"
for page in $(seq 1 9); do
    curl -s --max-time 30 \
        "https://neonewstoday.com/author/dylan/feed/?paged=$page" \
        -o "$LOG_DIR/rss-page-${page}.xml" 2>/dev/null || {
        log "  WARNING: Failed to fetch RSS page $page — skipping"
    }
done

if [ -f "$CORPUS_DIR/parse-articles-v2.py" ]; then
    python3 parse-articles-v2.py >> "$LOG_FILE" 2>&1 \
        && log "  Articles: done" \
        || log "  WARNING: parse-articles-v2.py exited with errors"
else
    log "  WARNING: parse-articles-v2.py not found — skipping articles"
fi

# ── 2. SEP PODCAST (playlist, incremental) ────────────────
log_section "2/4 Fetching SEP podcast transcripts"
SEP_BEFORE=$(ls "$SEP_DIR"/sep-*.txt 2>/dev/null | wc -l | tr -d ' ')

if [ -f "$CORPUS_DIR/update-videos.py" ]; then
    python3 update-videos.py >> "$LOG_FILE" 2>&1 \
        && log "  update-videos.py: done" \
        || log "  WARNING: update-videos.py exited with errors"
else
    log "  WARNING: update-videos.py not found — skipping SEP sync"
fi

SEP_AFTER=$(ls "$SEP_DIR"/sep-*.txt 2>/dev/null | wc -l | tr -d ' ')
NEW_SEP=$(( SEP_AFTER - SEP_BEFORE ))
log "  SEP transcripts: $SEP_AFTER total (+$NEW_SEP new)"

# Fix permissions on any newly downloaded SEP files
chmod 644 "$SEP_DIR"/sep-*.txt 2>/dev/null || true

# Warn about suspect (tiny) SEP transcripts
SMALL_SEP=$(find "$SEP_DIR" -name "sep-*.txt" -size -${MIN_TRANSCRIPT_BYTES}c 2>/dev/null)
if [ -n "$SMALL_SEP" ]; then
    log "  WARNING: Suspect small SEP transcripts (may need re-fetch):"
    echo "$SMALL_SEP" | while read f; do
        SIZE=$(wc -c < "$f" | tr -d ' ')
        log "    ⚠️  $(basename $f) — ${SIZE} bytes"
    done
fi

# ── 3. YOUTUBE CHANNEL (@GrabowskiDylan, incremental) ─────
log_section "3/4 Fetching YouTube channel transcripts"
VID_BEFORE=$(ls "$VIDEOS_DIR"/grabowski-*.txt 2>/dev/null | wc -l | tr -d ' ')

if [ -f "$CORPUS_DIR/update-channel-videos.py" ]; then
    python3 update-channel-videos.py >> "$LOG_FILE" 2>&1 \
        && log "  update-channel-videos.py: done" \
        || log "  WARNING: update-channel-videos.py exited with errors"
else
    log "  WARNING: update-channel-videos.py not found — skipping channel sync"
fi

VID_AFTER=$(ls "$VIDEOS_DIR"/grabowski-*.txt 2>/dev/null | wc -l | tr -d ' ')
NEW_VID=$(( VID_AFTER - VID_BEFORE ))
log "  Video transcripts: $VID_AFTER total (+$NEW_VID new)"

# Fix permissions on any newly downloaded video files
chmod 644 "$VIDEOS_DIR"/grabowski-*.txt 2>/dev/null || true

# Warn about suspect (tiny) video transcripts
SMALL_VID=$(find "$VIDEOS_DIR" -name "grabowski-*.txt" -size -3000c 2>/dev/null)
if [ -n "$SMALL_VID" ]; then
    log "  WARNING: Suspect small video transcripts:"
    echo "$SMALL_VID" | while read f; do
        SIZE=$(wc -c < "$f" | tr -d ' ')
        log "    ⚠️  $(basename $f) — ${SIZE} bytes"
    done
fi

# ── 4. REGENERATE MASTER INDEX ────────────────────────────
log_section "4/4 Regenerating master index"
if [ -f "$CORPUS_DIR/generate-index.py" ]; then
    python3 "$CORPUS_DIR/generate-index.py" >> "$LOG_FILE" 2>&1 \
        && log "  Index regenerated ✓" \
        || log "  WARNING: generate-index.py exited with errors"
else
    log "  NOTE: generate-index.py not found — skipping index regen"
fi

# ── SUMMARY ───────────────────────────────────────────────
echo "" >> "$LOG_FILE"
log "=== Sync Summary ==="
log "  SEP transcripts:   $SEP_AFTER files"
log "  Video transcripts: $VID_AFTER files"
log "  New this run:      +$NEW_SEP SEP, +$NEW_VID videos"
log "=== Sync Complete: $(date) ==="

# ── CLEANUP ───────────────────────────────────────────────
find "$LOG_DIR" -name "*.log" -mtime +30 -delete 2>/dev/null || true
find "$LOG_DIR" -name "rss-page-*.xml" -mtime +7 -delete 2>/dev/null || true
