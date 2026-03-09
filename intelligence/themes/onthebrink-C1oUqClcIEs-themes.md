# EP.683 - Keone Hon (Monad Foundation) - Blockchains Built to Scale

**Date:** January 2026 (estimated)
**Video ID:** C1oUqClcIEs
**Format:** Guest interview
**Disclosure:** Castle Island is an investor in Monad

---

## Episode Summary
Keone Hon, co-founder of Monad Foundation, discusses the rationale for building a new Layer 1 blockchain. With a background in high-frequency trading (HFT), Keone explains how Ethereum's limitations—12-second blocks, 12-minute finality, ~1 million transactions per day—prevent real-time financial markets. Monad achieves 400ms blocks, 800ms finality, and 1 billion transactions per day through parallel execution, pipelining, and optimized database architecture while maintaining decentralization.

---

## Themes

### #scaling - 1000x Ethereum Through Parallel Execution
Monad is a "re-architected version of Ethereum" rebuilt from scratch with HFT-style optimizations. Key technical improvements over Ethereum:
- **Block time:** 12 seconds → 400 milliseconds (30x faster)
- **Time to finality:** 12 minutes → 800 milliseconds (900x faster)
- **Daily throughput:** 1 million → 1 billion transactions (1000x)

**Core innovations:**
- **Parallel execution:** Transactions process simultaneously rather than sequentially
- **Asynchronous execution:** Consensus and execution are decoupled for efficiency
- **Pipelining:** Optimized processing pipeline similar to modern CPU architectures
- **Optimized database:** Purpose-built for blockchain state storage
- **New consensus mechanism:** Enables frequent blocks with fast finality

**EVM compatibility:** Monad maintains full Ethereum compatibility—"it is a rebuild from scratch of the Ethereum blockchain"—allowing existing Ethereum developers and tooling to migrate seamlessly.

### #DeFi - Real-Time Financial Markets
Hon argues that current blockchain latency creates real market inefficiencies. During volatile periods, "assets trading at different prices across exchanges" because settlement is too slow for arbitrageurs to keep markets aligned. Exchanges with 12-minute finality cannot support modern market making.

**Use cases unlocked by low latency:**
- Instant arbitrage across venues
- Real-time liquidity movement to demand
- Enterprise treasury management (seamless switching between yield-bearing instruments)
- Global price discovery for all assets

**Key insight:** "The latency of 12 minutes of finality or more is actually a significant impediment to allowing liquidity to move from place to place."

### #Bitcoin - Decentralization vs Performance Tradeoffs
Hon emphasizes that Monad chose the harder path of building a truly decentralized system rather than taking "shortcuts" that sacrifice decentralization for speed. Centralized solutions "can" switch off settlement during distress—"they can do that"—costing users their best trading moments.

**Composability:** Blockchains as "the underlying fabric that's keeping all of these different venues, different centralized exchange venues, different stores and so on all in sync with each other." Centralized systems fracture this fabric.

**Risk of custody:** Centralized exchanges engaging in "auto deleveraging"—closing user positions without authorization to "reduce the overall amount of leverage in the system." Hon: "I never authorized it."

### #institutional - HFT DNA Applied to DeFi
Hon's 10-year HFT quant background at a top firm drives Monad's architecture. HFT optimizations—pipelining, database tuning, consensus engineering—applied to blockchain for the first time. The team treats blockchain as trading infrastructure requiring institutional-grade performance.

**Team culture:** "High talent density" + "strong entrepreneurial culture"—enabling team members to eventually start their own companies. Keone: "We actually are really excited if people that are on our team right now someday leave us and start their own startup."

**Global organization:** Monad is now distributed globally with remote-first operations.

### #macro - Equal Access to Financial Tools
Hon's mission: give "everyone access to the same tools"—not just developed markets. Benefits of onchain finance:
- **Capital access:** Businesses globally can list on credible exchanges
- **Dollar access:** Stablecoins provide inflation hedge for emerging economies
- **24/7 markets:** Beyond geographic and timezone limitations

**Vision:** "It's giving people who have capital access to a broader set of investments and it's also giving people that maybe don't have as much capital... access to first of all dollars themselves in the form of dollar stable coins."

### #policy - Decentralization as Security
Hon argues decentralization matters precisely when users don't expect it—"it's true until it's not." Centralized systems have single points of failure vulnerable to:
- **Social engineering attacks:** Single operators can be compromised (Bybit exploit cited)
- **Individual discretion:** Human operators making "arbitrary decisions"
- **Auto deleveraging:** Exchanges inserting unauthorized orders

**Benefit of decentralized systems:** "All the rules are well defined ahead of time and there aren't corner cases and there isn't a human who can just make an arbitrary decision."

### #VC - Builder-First Ecosystem
Monad's "demo day" culture showcases ecosystem apps months before mainnet. Keone's first post-mainnet plan: "Just to try everything out and basically just get to be a fan of all of the products."

**Ecosystem apps mentioned:** Symphony (project highlighted via personal experience tweet)

---

## Notable Predictions
1. **Blockchains as settlement standard:** Successful blockchains will be "the base layer fabric that allows many different people to all coordinate in a shared global state"
2. **HFT techniques migrate:** Financial markets infrastructure optimization (from HFT) will reshape blockchain architecture
3. **User comfort threshold:** Success = "far more people being comfortable with using decentralized systems"
4. **Phased expansion:** Starting with DeFi primitives (perps, spot DEXs) then expanding to full commerce infrastructure

---

## Action Items / Research Leads
- Monitor Monad mainnet launch timing and initial TVL
- Compare Monad's latency claims vs. Solana/Sui/Other high-throughput chains
- Evaluate HFT-optimized consensus mechanisms (research MEV/ordering implications)
- Track "auto deleveraging" practices across perp DEXs vs. CEXs during volatility
- Assess team quality specifically: "brilliant but receptive" founder dynamic
- Research Symphony and other Monad ecosystem projects pre-launch
- Compare decentralization commitments: Monad vs. "fast but centralized" competitors

