# MEMORY.md — Hawat's Long-Term Memory

*Distilled from daily logs. Last updated: 2026-03-15*

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
- **corpus/** — Personal work library (NNT articles, SEP podcasts, YouTube videos)
- **synthesis/** — Hybrid content (explicitly requested only)
- No commingling unless directed

---

## Active Systems
- **Daily Crypto Market Briefing**: `intelligence/daily/YYYY-MM-DD.md`
- **Friday On The Brink fetch**: Weekly Roundup episodes only
- **SEP backfill**: Processing transcript → themes in `intelligence/themes/`
- **Cron updates**: corpus-my-work uses `venice/grok-4-1-fast` (default is now `mor-gateway/minimax-m2.5`)

---

## Job Search Context
- Dylan actively seeking: Ecosystem Growth Lead, DevRel, Partner Success, Content/Media, Community, DAO Operations, Grants, Policy
- Check inbox for LinkedIn/Indeed alerts; scan for relevant crypto/Web3 roles
- Target employers: EF, Polygon, Chainlink, Alchemy, Coinbase, Uniswap, Hedera, protocol companies

---

## ToDo (From 2026-03-13)
- Investigate: why news sources (coindesk, cointelegraph, thedefiant) not linking properly in Daily Digital Download briefings — check cron payloads and append logic in `~/.openclaw-vault/Streams/Daily Digital Download.md`

---

*Next review: 2026-03-22*