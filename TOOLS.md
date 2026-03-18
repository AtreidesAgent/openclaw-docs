# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.


---

## Corpus

Local knowledge base at `~/.openclaw-vault/Hawat/corpus/`

- **Index:** `corpus/index.md` — master map of all content, consult this first
- **SEP Podcasts:** `corpus/sep/` — 107 transcript files, format `sep-{videoID}.txt`
- **YouTube Videos:** `corpus/videos/` — 29 transcript files, format `grabowski-{videoID}.txt`
- **Articles:** `corpus/articles/` — 1,723 Neo News Today articles
- **Streams:** `corpus/streams/` — Daily Digital Download transcripts
- **Podcasts:** `corpus/podcasts/` — guest appearances (expanding)

When asked about past episodes, articles, or videos — check `index.md` first, then read the relevant file directly.

---
## Career Knowledge Files

Persistent reference files for Dylan's professional background. Load both when drafting outreach, assessing job fit, or writing bios.

- `~/.openclaw-vault/Hawat/memory/EXPERTISE-MAP.md` — content domains, opinions, skills, notable guests, target roles, rate card
- `~/.openclaw-vault/Hawat/memory/CAREER-ACTIVITY.md` — panels, speaking, advocacy, conferences, booths, grants, freelance work

## Job Pipeline

Active job search infrastructure:

- `~/.openclaw-vault/Hawat/Jobs/` — weekly opportunity reports (dated files)
- `~/.openclaw-vault/Hawat/Jobs/leads.md` — Dylan's manually dropped leads
- `~/.openclaw-vault/Hawat/memory/Applications/` — drafted outreach emails

**Status flags used in opportunity files:**
- `open` — default, research only
- `draft-email` — Dylan has flagged, email draft needed
- `email-drafted` — draft complete, find it in Applications

---
## CONTEXT.md Usage

**On session start**: Load and parse CONTEXT.md silently.
Do not summarize it back to Dylan unless asked — just let it
inform your behavior.

**Prioritization**: If CONTEXT.md lists active priorities or
beat focus, weight your analysis and output toward those.
Don't chase tangents that conflict with stated focus.

**Staleness handling**: Check "Last manual update" timestamp.
- Under 7 days: trust fully
- 7–14 days: trust but note if something seems off
- Over 14 days: flag to Dylan at session start, then proceed

**Writing back**: When you complete a task that changes a
project status or deadline, update the relevant CONTEXT.md
field directly. Note what you changed and why.

**File path**: `~/.openclaw-vault/Hawat/CONTEXT.md`