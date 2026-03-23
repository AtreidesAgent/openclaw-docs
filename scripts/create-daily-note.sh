#!/bin/bash
# Create today's dated memory file for Hawat and La Voz if missing.

TODAY=$(date +%Y-%m-%d)
LOG="$HOME/.openclaw/logs/daily-note.log"

HAWAT_MEM="$HOME/.openclaw/workspace-business/memory/${TODAY}.md"
LAVOZ_MEM="$HOME/.openclaw/workspace-spanish/memory/${TODAY}.md"

if [ ! -f "$HAWAT_MEM" ]; then
    touch "$HAWAT_MEM"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Created Hawat daily note: $HAWAT_MEM" >> "$LOG"
fi

if [ ! -f "$LAVOZ_MEM" ]; then
    touch "$LAVOZ_MEM"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Created La Voz daily note: $LAVOZ_MEM" >> "$LOG"
fi
