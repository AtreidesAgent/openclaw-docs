#!/bin/bash
# hawat-corpus-index.sh
# Generates ~/.openclaw-vault/Hawat/corpus/indices/corpus-index.md
# Runs nightly at 1am MT via jobs.json
# No model required — pure shell, reads existing .md files
#
# Covers: sep/, CCBB/, streams/, articles/, ctbw/
# Summaries: pulled from ## Summary subsection under ## Analysis (podcasts/streams)
#            pulled from first 3-4 sentences of article body (articles/)
#            blank if neither found

VAULT="$HOME/.openclaw-vault/Hawat/corpus"
INDICES="$VAULT/indices"
OUTPUT="$INDICES/corpus-index.md"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M")

mkdir -p "$INDICES"

# ── Helpers ────────────────────────────────────────────────────────────────────

# Extract a YAML frontmatter field value by key
fm_field() {
    local file="$1" key="$2"
    awk -v key="$key" '
        /^---$/ { if (++fence == 2) exit }
        fence == 1 && $0 ~ "^"key": " {
            sub("^"key": ", "")
            gsub(/^["'"'"']|["'"'"']$/, "")
            print
            exit
        }
    ' "$file"
}

# Extract first 3-4 sentences from article body (after frontmatter)
article_summary() {
    local file="$1"
    # Skip frontmatter block, grab first non-empty paragraph, limit to ~400 chars
    awk '
        /^---$/ { if (++fence == 2) { body=1; next } }
        body && /^#/ { next }
        body && NF > 0 {
            line = line " " $0
            sentences++
            if (sentences >= 4) exit
        }
        body && NF == 0 && length(line) > 0 { exit }
    ' "$file" | sed 's/^ //' | cut -c1-400
}

# Extract summary from ## Analysis section.
# CCBB format: ### Summary subsection under ## Analysis
# SEP format:  content sits directly under ## Analysis (no subsection)
analysis_summary() {
    local file="$1"
    local result
    # Try ### Summary first (CCBB)
    result=$(awk '
        /^## Analysis/ { in_analysis=1; next }
        in_analysis && /^### Summary/ { in_summary=1; next }
        in_summary && /^##/ { exit }
        in_summary && NF > 0 { print; found=1 }
        in_summary && NF == 0 && found { exit }
    ' "$file" | head -3 | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-400)
    # Fall back to direct content under ## Analysis (SEP)
    if [ -z "$result" ]; then
        result=$(awk '
            /^## Analysis/ { in_analysis=1; next }
            in_analysis && /^##/ { exit }
            in_analysis && NF > 0 { print; found=1 }
            in_analysis && NF == 0 && found { exit }
        ' "$file" | head -3 | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-400)
    fi
    echo "$result"
}

# Escape pipe characters for markdown table cells
esc() { echo "$1" | sed 's/|/\\|/g'; }

# ── Begin output ───────────────────────────────────────────────────────────────

{
echo "# Hawat Corpus Index"
echo "Generated: $TIMESTAMP  "
echo ""

# ── SEP ───────────────────────────────────────────────────────────────────────
SEP_DIR="$VAULT/sep"
SEP_FILES=("$SEP_DIR"/sep-*.md)
SEP_COUNT=${#SEP_FILES[@]}

echo "## Smart Economy Podcast (SEP) — $SEP_COUNT episodes"
echo ""
echo "| Date | Title | Guest | Summary | File |"
echo "|------|-------|-------|---------|------|"

for f in $(ls -r "$SEP_DIR"/sep-*.md 2>/dev/null); do
    date=$(fm_field "$f" "date")
    title=$(fm_field "$f" "title")
    guest=$(fm_field "$f" "guest")
    summary=$(analysis_summary "$f")
    fname=$(basename "$f")
    echo "| ${date:-unknown} | $(esc "$title") | $(esc "${guest:-—}") | $(esc "$summary") | \`$fname\` |"
done

echo ""

# ── CCBB ──────────────────────────────────────────────────────────────────────
CCBB_DIR="$VAULT/CCBB"
CCBB_FILES=("$CCBB_DIR"/*.md)
CCBB_COUNT=${#CCBB_FILES[@]}

echo "## Castle Island (CCBB) — $CCBB_COUNT episodes"
echo ""
echo "| Date | Title | Guest | Summary | File |"
echo "|------|-------|-------|---------|------|"

for f in $(ls -r "$CCBB_DIR"/*.md 2>/dev/null); do
    date=$(fm_field "$f" "date")
    title=$(fm_field "$f" "title")
    guest=$(fm_field "$f" "guest")
    summary=$(analysis_summary "$f")
    fname=$(basename "$f")
    echo "| ${date:-unknown} | $(esc "$title") | $(esc "${guest:-—}") | $(esc "$summary") | \`$fname\` |"
done

echo ""

# ── Streams ───────────────────────────────────────────────────────────────────
STREAMS_DIR="$VAULT/streams"
STREAMS_FILES=("$STREAMS_DIR"/*.md)
STREAMS_COUNT=${#STREAMS_FILES[@]}

echo "## Daily Digital Download (streams) — $STREAMS_COUNT episodes"
echo ""
echo "| Date | Title | Summary | File |"
echo "|------|-------|---------|------|"

for f in $(ls -r "$STREAMS_DIR"/*.md 2>/dev/null); do
    date=$(fm_field "$f" "date")
    title=$(fm_field "$f" "title")
    summary=$(analysis_summary "$f")
    fname=$(basename "$f")
    echo "| ${date:-unknown} | $(esc "$title") | $(esc "$summary") | \`$fname\` |"
done

echo ""

# ── Articles ──────────────────────────────────────────────────────────────────
ARTICLES_DIR="$VAULT/articles"
ARTICLES_COUNT=$(ls "$ARTICLES_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')

echo "## NNT Articles — $ARTICLES_COUNT articles"
echo ""
echo "| Date | Title | Summary | File |"
echo "|------|-------|---------|------|"

for f in $(ls -r "$ARTICLES_DIR"/*.md 2>/dev/null); do
    date=$(fm_field "$f" "date")
    title=$(fm_field "$f" "title")
    summary=$(article_summary "$f")
    fname=$(basename "$f")
    echo "| ${date:-unknown} | $(esc "$title") | $(esc "$summary") | \`$fname\` |"
done

echo ""

# ── Videos ───────────────────────────────────────────────────────────────────
VIDEOS_DIR="$VAULT/ctbw"
VIDEOS_COUNT=$(ls "$VIDEOS_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')

echo "## Conference Interviews (ctbw) — $VIDEOS_COUNT files"
echo ""
echo "| Date | Title | Guest | Summary | File |"
echo "|------|-------|-------|---------|------|"

for f in $(ls -r "$VIDEOS_DIR"/*.md 2>/dev/null); do
    date=$(fm_field "$f" "date")
    title=$(fm_field "$f" "title")
    guest=$(fm_field "$f" "guest")
    summary=$(analysis_summary "$f")
    fname=$(basename "$f")
    echo "| ${date:-unknown} | $(esc "$title") | $(esc "${guest:-—}") | $(esc "$summary") | \`$fname\` |"
done

echo ""

# ── Footer ────────────────────────────────────────────────────────────────────
TOTAL=$(( SEP_COUNT + CCBB_COUNT + STREAMS_COUNT + ARTICLES_COUNT + VIDEOS_COUNT ))
echo "---"
echo "_Total corpus entries: $TOTAL — index auto-generated by hawat-corpus-index.sh_"

} > "$OUTPUT"

echo "[hawat-corpus-index] Done. Written to $OUTPUT"
