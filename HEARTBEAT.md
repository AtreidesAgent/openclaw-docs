# HEARTBEAT.md - Hawat Periodic Tasks

1. Current date/time: `date +%Y-%m-%d` (YYYY-MM-DD), `date +%H:%M` (HH:MM), TZ=America/Denver.
2. Read todos.json if it exists and check for any due tasks.
3. **Daily Briefing Write:** If today's crypto briefing has been compiled, append it to `~/.openclaw-vault/Streams/Daily Digital Download.md` using the format:
```
   ## Hawat Briefing — YYYY-MM-DD
   [briefing content]
```
   Do not overwrite previous days — always append. After writing, send a short Telegram message saying the briefing is ready in Obsidian.
4. If no action needed: HEARTBEAT_OK.
