# MEMORY.md — Hawat's Long-Term Memory

*Distilled from daily logs. Last updated: 2026-03-29*

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
- * For fit assessment and outreach, always load:
  * `memory/EXPERTISE-MAP` — skills, opinions, content domains, target roles
  * `memory/CAREER-ACTIVITY` — panels, speaking, advocacy, conferences, grants

---

## Week of March 22-28, 2026 — Quiet Week

- Week was largely quiet. No major SEC/regulatory developments following the 3/16 guidance
- Saturday briefing on 3/28 delivered without issues — beat focus: AI agents, regs, majors/L2s, instros
- No action items or breaking developments logged

---

## Previous: SEC/CFTC Historic Guidance (Week of March 16-20)

### SEC/CFTC Guidance Released
- First clear framework listing 15 tokens as commodities: BTC, ETH, SOL, XRP, ADA, LINK, DOGE, AVAX, DOT, XLM, HBAR, LTC, BCH, SHIB
- Tokens can "graduate" out of security status via decentralization
- Industry called this the rule change they wanted for years

### AI Layoff Wave Hitting Crypto
- Messari CEO stepped down, firm going AI-first
- Block cut 40% citing AI productivity gains
- Cango (BTC miner) reported $453M loss, pivoting to AI infrastructure
- Crypto.com cut ~180 people citing AI

### TradFi Adoption Accelerating
- Mastercard acquiring BVNK ($1.8B)
- PayPal PYUSD expanding to 68 new markets
- Moody's launched credit ratings on Canton Network
- NASDAQ approved for tokenized trade settlements
- Coinbaes launched BTC yield fund on Base
- Ledger opening NYC institutional office

### DAO Tooling Dying
- Tally shutting down after 5 years, $8M raised
- Regulatory clarity eliminates need for decentralized governance tooling

### Watch List
- **Clarity Act**: Market structure bill stalled on stablecoin yield
- **AI Payments**: X402 vs Visa/Mastercard — winner undecided

---

*Next review: 2026-04-05*