# EP.677 - Pbj (Perpl) - Perp DEX & Monad

**Date:** January 2026 (estimated)
**Video ID:** Lg8Sj6ycky4
**Format:** Guest interview

---

## Episode Summary
Pbj, founder of Perpl (Purple), discusses building a perpetual futures exchange on Monad. The episode covers the dominance of perp trading in crypto (90% of volume), Hyperliquid's strategic success, the rationale for building on an EVM L1 vs app chains, and what competitive features differentiate a new entrant in the crowded DEX market.

---

## Themes

### #DeFi - Perpetuals as Crypto PMF "Killer App"
Perpl represents Perps as one of only two crypto products with "definitive product market fit" (the other being stablecoins). Pbj argues perps solve real trader needs: leverage without maturity/expiration, consolidated liquidity (vs fragmented options), simplicity for retail ("5x leverage = 5x return"), and hedging capabilities. "Orders of magnitude" more trading volume happens via derivatives than spot—Binance sees 90/10 derivatives vs spot, and this aligns with TradFi where futures markets dwarf equities.

**Key insight:** Perps are the "foreign exchange" and "stock market" primitives necessary for any L1 ecosystem to establish financial activity. "If you're starting a new L1, you need the perp exchange, you need a spot exchange... these primitives have to be there in the beginning for any other type of activity to kickstart."

### #institutional - The Hyperliquid Playbook
Pbj deconstructs Hyperliquid's success as a case study in timing and execution: launched post-FTX when users tired of custodian risk; focused relentlessly on product ("just worked" vs "failed transactions or gas bikes or MetaMask signing"); used market making background to build central order book + HLP (passive LP that "shortcircuited the need for market makers"); eventually pivoted from single-app chain to sidecar EVM to escape "glass ceiling."

**Notable:** Hyperliquid captured 10-15% of Binance's volume as a single DEX, proving DEXs can compete with CEXs on product alone.

### #scaling - Monad vs Solana vs App Chains
Perpl chose Monad because:
1. **EVM dominance:** "EVM has become the JavaScript of blockchain technology" — assets, dev support, infrastructure
2. **Fast without centralization:** Other "fast EVMs" achieve speed by centralizing; Monad "did not take any shortcuts" — rebuilt firmware, overhauled database
3. **Gas efficiency for market makers:** Making maker post/cancel operations extremely gas-efficient is critical for attracting professional market makers
4. **Composability:** Building on a general purpose L1 vs app chain enables "Apple Pay" style interoperability — users don't need to bridge assets to different ecosystems

**Solana comparison:** Acknowledged Solana's "incredible" ecosystem (Jupiter, Phoenix, Camino) but noted SVM's "completely new programming language" creates friction. Monad's EVM compatibility removes that barrier while achieving similar throughput.

### #payments - Stablecoin Integration & Trading Infrastructure
Perps depend on stablecoins as margin/collateral. The discussion emphasizes that sophisticated trading requires stablecoin infrastructure: "you just need two different prices for this whole thing to work for the funding rate to be calibrated." Stablecoins are the "banking system" primitive alongside perps as the "foreign exchange."

**Emerging opportunity:** Basis trading — using staked tokens as collateral to hedge price exposure while maintaining future airdrop/points eligibility. Example: stake Kaito, use as collateral for 1x short perp, get "unlimited liquidation price" because positions are perfectly hedged.

### #macro - Global Capital Market Expansion
Pbj argues for eventual expansion to equities and real-world assets: "if those people [in India, Nigeria, China] could somehow get exposure to [US equities] that's just a lot bigger capital base." 24/7 onchain trading with global access represents TAM expansion beyond traditional geographic/timezone limitations.

**Challenge:** Weekend trading of real-world assets requires winding down markets — protocols like Superstate doing primary issuance on-chain may bridge this gap.

### #VC - Community-Led Bootstrapping
Perpl's go-to-market strategy emphasizes leveraging Monad's "incentivized community, their day one users" before attracting external traders. The "hunger for perps" on crypto Twitter and genuine product demand means "there's already a hunger... there's a ton of interest" — suggesting less need for artificial incentives and more focus on product features.

### #Bitcoin - Asset Expansion & Oracle Infrastructure
The path from majors (BTC, ETH) to long-tail assets is "race to the bottom" on listing speed. Eventually any asset with "oracle and market makers willing to quote" can trade. Hyperliquid's HIP-3 "allow anybody to like deploy per markets" points to permissionless market creation.

---

## Notable Predictions
1. **DEX/CEX parity:** "The gap between centralized exchanges and decentralized exchanges is going down significantly"
2. **Perp dominance holds:** Market structure stays 80-90% derivatives / 10-20% spot as TAM grows
3. **EVM wins again:** New L1s will prioritize EVM compatibility over novel VMs due to developer/asset infrastructure moats
4. **Basis trading native:** Advanced DeFi products enabling hedge-while-staked will become standard features
5. **Mobile onboarding:** New retail enters via mobile-first wallets ("PVP.trade people, Axiom wallet traders") while professionals stay desktop

---

## Action Items / Research Leads
- Monitor Monad mainnet launch timing and initial dApp traction
- Track Hyperliquid's continued market share vs Binance
- Evaluate Purple/Perpl's "hidden liquidity" and "iceberg orders" feature differentiation
- Assess Fireblocks integration for institutional hedge vault capabilities
- Research basis trading demand — tokens with points/airdrop mechanics that users want to hedge
- Compare Monad's "no shortcuts" approach vs other fast-EVM chains' centralization tradeoffs
- Monitor mobile wallet trading adoption (PVP.trade, Axiom) vs desktop retention