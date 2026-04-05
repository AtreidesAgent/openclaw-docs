# MEMORY.md — Hawat's Long-Term Memory

*Distilled from daily logs. Last updated: 2026-04-05*

---

## Infrastructure & Setup
- **Local model config** requires explicit allowlist registration (`agents.defaults.models`)
- Gateway restart may revert config — verify post-restart
- Cron/heartbeat tasks need explicit `--model` assignment and `--timeout-seconds` for Ollama
- Small local models + web tools = prompt injection risk in fallback position
- **Verification protocol**: always run `ls`/`cat` on reported files before trusting completion

---

## Workspace Structure
- **intelligence/** — Public crypto intel (On The Brink transcripts, daily briefings, theme analysis)
- **corpus/** — Personal work library (NNT articles, SEP episodes, CTBW interviews, guest interviews, CCBB spaces, DDD streams)
- **synthesis/** — Hybrid content (explicitly requested only)
- No commingling unless directed

### Corpus folder map
- `corpus/articles/` — 1,730+ NNT articles (YAML frontmatter, date-slugged filenames)
- `corpus/sep/` — Smart Economy Podcast transcripts (format: `sep-YYYY-MM-DD-{vid}.md`)
- `corpus/ctbw/` — Crypto Talk and Blockchain Walk walking interviews + `video_*.md` stubs
- `corpus/interviews/` — Dylan's guest appearances on other shows (`YYYY-MM-DD-show-name.md`)
- `corpus/CCBB/` — Crypto Coffee & Blockchain Beer X Spaces transcripts
- `corpus/podcasts/` — Castle Island On The Brink transcripts + themes
- `corpus/streams/` — Daily Digital Download livestream overviews
- `corpus/indices/` — Generated corpus index (`corpus-index.md`) — Hawat's retrieval layer
- `corpus/analysis/` — OTB vs DDD signal comparisons

---

## Active Systems
- **Daily Crypto Market Briefing**: `intelligence/daily/YYYY-MM-DD.md`
- **Friday On The Brink fetch**: Weekly Roundup episodes only → `corpus/podcasts/`
- **SEP pipeline**: `scrape-sep-weekly` cron (Thursdays 9am MT) — fetches new episodes, writes `sep-YYYY-MM-DD-{vid}.md` to `corpus/sep/`. Enrichment (Analysis section) done manually via Claude Code on MacBook.
- **CTBW pipeline**: `ctbw_pipeline.py` — manual run when new CTBW episodes published. Transcribes via WhisperX, writes to `corpus/ctbw/`. Activate `whisperx-env` first.
- **Interviews pipeline**: `interviews_pipeline.py` — manual run from manifest file. Handles YouTube and X broadcast URLs. Writes to `corpus/interviews/`.
- **Corpus index**: `hawat-corpus-index.sh` — runs nightly at 1am MT, writes `corpus/indices/corpus-index.md`
- **Cron updates**: `corpus-my-work` handles articles + CTBW channel stubs only (SEP removed). Default model: `mor-gateway/minimax-m2.5`

---

## Job Search Context
- Dylan actively seeking: Ecosystem Growth Lead, DevRel, Partner Success, Content/Media, Community, DAO Operations, Grants, Policy
- Check inbox for LinkedIn/Indeed alerts; scan for relevant crypto/Web3 roles
- Target employers: EF, Polygon, Chainlink, Alchemy, Coinbase, Uniswap, Hedera, protocol companies
- * For fit assessment and outreach, always load:
  * `memory/EXPERTISE-MAP` — skills, opinions, content domains, target roles
  * `memory/CAREER-ACTIVITY` — panels, speaking, advocacy, conferences, grants

---

*Next review: 2026-04-12 — For market intel, read newsletters/ folder directly.*