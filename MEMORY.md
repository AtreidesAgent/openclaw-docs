# MEMORY.md — Hawat's Long-Term Memory

*Distilled from daily logs. Last updated: 2026-03-22*

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

## Week of March 16-20, 2026 — Key Distillations

### SEC/CFTC Guidance Released (Historic)
- First clear framework listing 15 tokens as commodities: BTC, ETH, SOL, XRP, ADA, LINK, DOGE, AVAX, DOT, XLM, HBAR, LTC, BCH, SHIB
- Tokens can "graduate" out of security status via decentralization
- Does not replace Howey test but clarifies SEC application
- Industry called this the rule change they wanted for years

### AI Layoff Wave Hitting Crypto
- Messari CEO stepped down, firm going AI-first
- Block cut 40% citing AI productivity gains
- Cango (BTC miner) reported $453M loss, pivoting to AI infrastructure
- Crypto.com cut ~180 people citing AI
- Clear signal: companies choosing AI over headcount

### TradFi Adoption Accelerating
- Mastercard acquiring BVNK ($1.8B)
- PayPal PYUSD expanding to 68 new markets
- Moody's launched credit ratings on Canton Network
- NASDAQ approved for tokenized trade settlements
- Coinbase launched BTC yield fund on Base
- Ledger opening NYC institutional office
- **Theme**: RWA + stablecoins = killer use case. Institutions buying while crypto Twitter stays bearish.

### DAO Tooling Dying
- Tally (governance platform for Uniswap/Arbitrum) shutting down after 5 years, $8M raised
- Regulatory clarity eliminates need for decentralized governance tooling
- DAO participation problems (low turnout, slow decisions, no incentive) never solved
- "It's not early anymore. We're in the middle innings."

### Watch List
- **Clarity Act**: Market structure bill stalled on stablecoin yield; needs laws that survive 2028 admin
- **AI Payments**: X402 (~28k daily volume) vs Visa/Mastercard on existing rails; winner undecided but blockchain-native version (Coinbase) competing

---

## ToDo (From 2026-03-13)
- ~~Investigate: why news sources not linking properly in Daily Digital Download briefings~~ — Covered in 3/20 weekly: investigate cron payloads and append logic

---

*Next review: 2026-03-29*