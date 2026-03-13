#!/bin/bash
# audit-corpus.sh — One-time audit of Hawat corpus health
# Run manually: bash audit-corpus.sh
# Reports gaps, suspect files, permission issues, and index staleness

CORPUS_DIR="$HOME/.openclaw-vault/Hawat/corpus"
SEP_DIR="$CORPUS_DIR/sep"
VIDEOS_DIR="$CORPUS_DIR/videos"
REPORT="$CORPUS_DIR/audit-$(date +%Y-%m-%d).txt"

echo "=====================================================" | tee "$REPORT"
echo "  Hawat Corpus Audit — $(date)"                        | tee -a "$REPORT"
echo "=====================================================" | tee -a "$REPORT"

# ── 1. SEP TRANSCRIPTS ────────────────────────────────────
echo ""                                                       | tee -a "$REPORT"
echo "── SEP Podcast Transcripts (sep/) ──────────────────" | tee -a "$REPORT"

SEP_COUNT=$(ls "$SEP_DIR"/sep-*.txt 2>/dev/null | wc -l | tr -d ' ')
echo "  Total .txt files found: $SEP_COUNT"                  | tee -a "$REPORT"

# Files suspiciously small (under 10 KB — likely failed downloads)
echo ""                                                       | tee -a "$REPORT"
echo "  Suspect files (< 10 KB, likely incomplete):"         | tee -a "$REPORT"
SMALL=$(find "$SEP_DIR" -name "sep-*.txt" -size -10k)
if [ -z "$SMALL" ]; then
    echo "    None found ✓"                                   | tee -a "$REPORT"
else
    echo "$SMALL" | while read f; do
        SIZE=$(wc -c < "$f")
        echo "    ⚠️  $(basename $f) — ${SIZE} bytes"         | tee -a "$REPORT"
    done
fi

# Permission inconsistencies
echo ""                                                       | tee -a "$REPORT"
echo "  Files with restrictive permissions (should be 644):" | tee -a "$REPORT"
BADPERM=$(find "$SEP_DIR" -name "sep-*.txt" ! -perm 644)
if [ -z "$BADPERM" ]; then
    echo "    None found ✓"                                   | tee -a "$REPORT"
else
    echo "$BADPERM" | while read f; do
        PERM=$(stat -f "%Sp" "$f")
        echo "    🔒 $(basename $f) — $PERM"                  | tee -a "$REPORT"
    done
    echo ""                                                   | tee -a "$REPORT"
    echo "  → Fix with: chmod 644 $SEP_DIR/sep-*.txt"        | tee -a "$REPORT"
fi

# ── 2. VIDEO TRANSCRIPTS ──────────────────────────────────
echo ""                                                       | tee -a "$REPORT"
echo "── YouTube Video Transcripts (videos/) ─────────────" | tee -a "$REPORT"

TXT_COUNT=$(ls "$VIDEOS_DIR"/grabowski-*.txt 2>/dev/null | wc -l | tr -d ' ')
echo "  Total grabowski .txt transcripts: $TXT_COUNT"        | tee -a "$REPORT"

# Orphaned .md stubs — stubs with no matching .txt transcript
echo ""                                                       | tee -a "$REPORT"
echo "  Orphaned .md stubs (stub exists but no .txt):"       | tee -a "$REPORT"
ORPHAN_FOUND=0
for stub in "$VIDEOS_DIR"/video_*.md "$VIDEOS_DIR"/podcast_*.md; do
    [ -f "$stub" ] || continue
    # Extract video ID from stub filename (video_XXXX.md or podcast_XXXX.md)
    VID_ID=$(basename "$stub" .md | sed 's/^video_//;s/^podcast_//')
    # Check for corresponding transcript
    if [ ! -f "$VIDEOS_DIR/grabowski-${VID_ID}.txt" ] && \
       [ ! -f "$SEP_DIR/sep-${VID_ID}.txt" ]; then
        echo "    ⚠️  $(basename $stub) → no transcript for ID: $VID_ID" | tee -a "$REPORT"
        ORPHAN_FOUND=1
    fi
done
[ $ORPHAN_FOUND -eq 0 ] && echo "    None found ✓"          | tee -a "$REPORT"

# .txt transcripts with no matching .md stub (informational)
echo ""                                                       | tee -a "$REPORT"
echo "  grabowski .txt files missing a .md stub:"            | tee -a "$REPORT"
NOSTUB_FOUND=0
for txt in "$VIDEOS_DIR"/grabowski-*.txt; do
    [ -f "$txt" ] || continue
    VID_ID=$(basename "$txt" .txt | sed 's/^grabowski-//')
    if [ ! -f "$VIDEOS_DIR/video_${VID_ID}.md" ]; then
        echo "    ℹ️  grabowski-${VID_ID}.txt — no stub (fine, stubs are optional)" | tee -a "$REPORT"
        NOSTUB_FOUND=1
    fi
done
[ $NOSTUB_FOUND -eq 0 ] && echo "    None found ✓"          | tee -a "$REPORT"

# Small video transcripts
echo ""                                                       | tee -a "$REPORT"
echo "  Suspect video files (< 3 KB):"                       | tee -a "$REPORT"
SMALL_V=$(find "$VIDEOS_DIR" -name "grabowski-*.txt" -size -3k)
if [ -z "$SMALL_V" ]; then
    echo "    None found ✓"                                   | tee -a "$REPORT"
else
    echo "$SMALL_V" | while read f; do
        SIZE=$(wc -c < "$f")
        echo "    ⚠️  $(basename $f) — ${SIZE} bytes"         | tee -a "$REPORT"
    done
fi

# ── 3. OTHER CORPUS FOLDERS ───────────────────────────────
echo ""                                                       | tee -a "$REPORT"
echo "── Other corpus folders ─────────────────────────────" | tee -a "$REPORT"
for DIR in articles podcasts streams indices; do
    COUNT=$(find "$CORPUS_DIR/$DIR" -type f 2>/dev/null | wc -l | tr -d ' ')
    echo "  $DIR/: $COUNT files"                              | tee -a "$REPORT"
done

# ── 4. INDEX FRESHNESS ────────────────────────────────────
echo ""                                                       | tee -a "$REPORT"
echo "── Index freshness ──────────────────────────────────" | tee -a "$REPORT"
INDEX="$CORPUS_DIR/index.md"
if [ -f "$INDEX" ]; then
    INDEX_AGE=$(( ( $(date +%s) - $(stat -f %m "$INDEX") ) / 86400 ))
    echo "  index.md last modified: ${INDEX_AGE} days ago"   | tee -a "$REPORT"
    [ $INDEX_AGE -gt 7 ] && \
        echo "  ⚠️  Index is stale — run weekly-sync.sh to regenerate" | tee -a "$REPORT"
    [ $INDEX_AGE -le 7 ] && echo "  ✓ Index is fresh"        | tee -a "$REPORT"
else
    echo "  ⚠️  index.md not found at $INDEX"                 | tee -a "$REPORT"
fi

# ── 5. SYNC SCRIPT HEALTH ─────────────────────────────────
echo ""                                                       | tee -a "$REPORT"
echo "── Sync script health ───────────────────────────────" | tee -a "$REPORT"
for script in weekly-sync.sh update-videos.py update-channel-videos.py \
              parse-articles-v2.py generate-index.py; do
    if [ -f "$CORPUS_DIR/$script" ]; then
        echo "  ✓ $script exists"                             | tee -a "$REPORT"
    else
        echo "  ✗ $script MISSING"                            | tee -a "$REPORT"
    fi
done

# ── 6. QUICK FIX OFFER ────────────────────────────────────
echo ""                                                       | tee -a "$REPORT"
echo "── Recommended fixes ────────────────────────────────" | tee -a "$REPORT"
echo "  1. Fix permissions:  chmod 644 $SEP_DIR/sep-*.txt"   | tee -a "$REPORT"
echo "  2. Re-fetch small files: check sep-hLSSQkQU_mc.txt"  | tee -a "$REPORT"
echo "     yt-dlp --write-auto-sub --sub-lang en --skip-download \\" | tee -a "$REPORT"
echo "       --convert-subs txt -o '$SEP_DIR/sep-%(id)s.%(ext)s' \\" | tee -a "$REPORT"
echo "       'https://www.youtube.com/watch?v=hLSSQkQU_mc'"  | tee -a "$REPORT"
echo "  3. Run weekly-sync.sh to pull any missing content"   | tee -a "$REPORT"
echo ""                                                       | tee -a "$REPORT"
echo "=====================================================" | tee -a "$REPORT"
echo "  Audit complete. Report saved to:"                    | tee -a "$REPORT"
echo "  $REPORT"                                             | tee -a "$REPORT"
echo "=====================================================" | tee -a "$REPORT"
