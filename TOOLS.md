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
