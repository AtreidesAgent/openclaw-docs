# EP.695 - Wyatt & Jake Lynch (Castle Island) - Valuing DeFi Lending Protocols

**Date:** October 2025 (post-crash discussion)
**Video ID:** kQqgt6SxheQ
**Format:** Internal Castle Island discussion
**Guests:** Wyatt Lynch (Castle Island) & Jake Lynch (Castle Island)

---

## Episode Summary
Wyatt Lynch and Jake Lynch discuss their research report on valuing DeFi lending protocols, contextualized by the October 10, 2025 crypto crash. The episode focuses on why lending is crypto's "evergreen" business, the dangers of hidden leverage via "looping" strategies, the difference between TVL and actual revenue, and how to properly value lending protocols beyond superficial metrics.

---

## Themes

### #DeFi - Lending as "Evergreen" vs "Seasonal" Business
DeFi divides into two categories:
- **Settlement/Tokenization:** Instantaneous, time-of-use activities (swapping) — "very cyclical" with "DeFi summer" seasonality
- **Capital Formation:** Lending and launchpads — "evergreen" because users constantly seek yield on assets

**Why lending is durable:** Users want to turn "non-productive assets into productive assets." This need doesn't disappear with seasons or prices. It's analogous to stablecoin volume — persistent demand regardless of market conditions.

**DeFi stack taxonomy (from Jake):**
1. Settlement (L1s) → 2. Swapping → 3. Lending → 4. Strategies (vaults, staking) → 5. Asset management/custody

### #institutional - Valuation Metrics: Beyond TVL
The research piece challenged market valuation practices:

**TVL is the wrong metric:** "How many dollars you can put in a smart contract" vs. "how many dollars you take out of a smart contract" (loans/usage).

**Key example:** Morpho-Coinbase integration allowed borrowing against cbBTC — $1.5B in Bitcoin collateral with "exponential growth" and zero correlation with October's TVL crash.

**Better metrics for lending protocols:**
- Stablecoin availability on platform (USDC/USDT borrowable supply)
- Actual loan origination volume
- Interest revenue (not token emission revenue)
- Quality of collateral (vs. looping/vault strategies)

### #DeFi - The "Looping" Danger
Leading up to October 2025, a popular strategy emerged:
- Users deposit yield-bearing tokens (USDe, staked ETH, RWA lending receipts)
- Borrow stablecoins at high LTV
- Buy more yield-bearing tokens
- Re-deposit and re-borrow ("looping")
- Result: 10% yield → 25-30% levered yield

**Why this was scary:**
1. **Opacity:** "Virtually impossible to identify how levered a system is" — users could loop across multiple platforms/accounts
2. **Risk curve descent:** Yield strategies increasingly went "down the risk curve" — USDe basis trade "commodified" and wrapped in tokens, then deployed through vaults with "levels of obfuscation"
3. **Cross-contamination:** Elixir Event revealed vaults "cross-depositing into themselves" — spreading same risk across multiple funds

**Wyatt's analysis:** This looping strategy "is not what I would consider to be the bet on lending markets." It drove TVL but created systemic fragility.

### #macro - The October 10 Crash Anatomy
**Direct cause:** Poor liquidation of ~$60M USDe on Binance — dumped on order book not $60M deep, with Binance oracle tied to its own order book.

**Indirect cause:** Fear around USDe (6-8B of it "pushed into the big risk house in crypto"). Aave went so far as to "hard peg [USDe] to USDT" — extreme measure that proved necessary.

**Structural fragility:** Thin order books across altcoins — $200M market cap assets with $250K daily real depth. "You can only functionally trade $250,000 of the asset per day... the price of these assets are going to fall really fast."

**Wyatt's critique:** "Fundamental floor is not necessarily there for a lot of assets" — 95% candles on October 10 revealed structural weakness.

### #VC - Token Valuation & Fund Incentives
#### Fund Administration Issues
- **GPB vs GPA funds:** "Whether they want management fees or performance fees" — management fee funds incentivized to inflate NAV; performance fee funds incentivized to mark conservatively (high water mark constraint)

- **Valuation policy:** Fifth Era forces massive discounts on illiquid assets (assets with 10% float, no volume) to avoid overpaying fees on unrealized marks

- **The liquid fund problem:** Annual fee crystallization means "your investors have to pay fees on that unrealized" mark if NAV inflated — creates misalignment

**Smart manager behavior:** "Mark conservatively" and only get paid "once that asset gets to a mature level where you can actually liquidate it safely."

### #Ethereum - Correlation to Rates & Macro
Lynch: "Crypto sits so far out on the risk curve that it is one macro trade" — "just by being in crypto, you have taken a macro outlook."

**The crypto paradox:** Crypto springs from disillusionment with monetary policy, yet "thrives when monetary policy is arguably problematic, reckless" — it's "essentially the short trader in the crew... only happy when everybody else is sad."

**Rates thesis:**
- **High rates:** Lending benefits from high borrow rates (basis trade yield spreads)
- **Low rates:** Lending benefits from volume uptick (more strategies become viable, swap fees recover)
- "In the high interest rate environment, they benefit from high interest rates. In the low interest rate environment, they benefit from low interest rates."

### #Bitcoin - CDPs as Persistent Use Case
**Most durable trade:** Bitcoin holders who want dollars without selling (taxes, ideology) borrow against BTC via CDPs (Collateralized Debt Positions).

**Coinbase-Morpho example:** cbBTC integration — $1.5B in Bitcoin collateral, grew exponentially, "not hindered at all" by October crash.

**Why this matters:** Unlike looping/vault strategies, this is "organic demand" — people who genuinely want to hold BTC while accessing spendable dollars.

### #DeFi - Sector Maturity & Discovery
Crypto undergoing "discovery" similar to early internet/traditional finance:
- **2021-2023:** User metrics and GitHub commits — "extremely gameable metrics"
- **2025:** Revenue metrics — "not gameable" because "somebody is paying that revenue"

**Figure example:** Traditional bank put out report comparing Figure to Coinbase and Circle — premature; market still figuring out valuation frameworks for crypto-securities.

**Sector consensus (emerging):** Clear taxonomy now exists (issuance → settlement → swapping → lending → strategies → asset management) — enables proper underwriting.

### #stablecoins - Liquidity Competition
**Stablecoins vs. altcoins:** "Stable coins, tokenized assets, and meme coins... are materially detrimental to altcoins from this liquidity perspective" — basic rates theory. When rates are low, speculation thrives; when rates rise, money flows to "safe" stablecoin yields vs. risky altcoins.

**The supply-demand dynamic:** "Supply of float that is out there for quality projects is so low and the demand for these safe assets is so high that you have premiums."

---

## Notable Predictions

1. **Lending protocol underpricing:** With 5-year horizon, lending protocols are "underpriced, but not categorically" — requires patience
2. **Looping unwind:** Vault/looping strategies revealed as fragile; "organic" lending (CDPs, BTC collateral) proves durable
3. **Revenue-based valuation:** Market shifting from TVL/user metrics to revenue/usage metrics — creates temporary mispricing opportunities
4. **Rates-driven recovery:** Lower rates → basis trade revival → lending volume recovery →DeFi summer return
5. **Token premium compression:** Liquid token market caps ($200M+) with thin order books ($250K real depth) will face continued repricing pressure

---

## Action Items / Research Leads

- Evaluate "quality of collateral" in major lending protocols (Aave, Compound, Morpho) — what % is organic (BTC/ETH) vs. looping/vault-derived?
- Track basis trade funds/wrapped strategies in lending pools — concentration risk in USDe-type assets
- Monitor Coinbase/Morpho cbBTC integration growth as proxy for durable BTC-collateralized lending demand
- Assess fifth-era style fund valuation policies: which funds mark conservatively vs. inflate NAV?
- Compare liquid token market caps to actual order book depth across top 100 tokens — identify structural fragility
- Track "high water mark" fund performance — which managers are aligned with LPs via performance fees vs. management fee extraction?
- Research Elixir Event aftermath — did cross-depositing vaults reform or persist?
- Evaluate lending protocol revenue vs. token emission revenue quality — which platforms have sustainable economics?

