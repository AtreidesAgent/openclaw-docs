---
title: "Asteroneo launches USDC bridge to Neo X EVM sidechain, establishes NeoUSD stablecoin"
date: 2024-09-05
url: https://neonewstoday.com/defi/asteroneo-launches-usdc-bridge-to-neo-x-evm-sidechain-establishes-neousd-stablecoin/
tags: [DeFi, General, Asteroneo, GAS, NUSD]
source: neonewstoday
---

# Asteroneo launches USDC bridge to Neo X EVM sidechain, establishes NeoUSD stablecoin

**Published:** Thu, 05 Sep 2024 02:15:03 +0000
**URL:** https://neonewstoday.com/defi/asteroneo-launches-usdc-bridge-to-neo-x-evm-sidechain-establishes-neousd-stablecoin/
**Tags:** DeFi, General, Asteroneo, GAS, NUSD

---

Asteroneo has pushed its USDC bridge live on the Neo X EVM sidechain, the first such bridge on the recently launched blockchain. Now, users can migrate USDC from the BNB Chain and mint NeoUSD on the Neo X chain.

The Asteroneo development team states that each NUSD token is collateralized by 1 USDC token on the BNB Chain. When migrating USDC from BNB Chain to Neo X, the USDC is locked on the BNB Chain bridge contract, and NUSD is minted on Neo X. When NUSD is bridged back to BNB Chain, it is then burnt on Neo X, and the USDC is released on BNB Chain. There is a 0.01% fee incurred by the user when migrating NUSD off Neo X and redeeming for USDC on BNB Chain, estimated to take place over 3 to 5 minutes.

Source: app.asteroneo.com

In an effort to increase the bridge’s security, Asteroneo purports to have implemented a simple, barebones structure to limit complicated processes and potential exploitations. The team states:

The bridge features an external multisignature wallet to secure the funds from attacks, a backend that tracks suspect actions, and a double database to keep all on-chain data and bridge TXs, in order to make sure we don’t run into any exploits. Each bridge transaction also has a specific nonce that is consumed on the other chain in order to avoid double spending.

To help keep NUSD pegged to US $1, Asteroneo has deployed an arbitrage bot. If the price of NUSD drops below $1, the bot (or a platform user) can use GAS to purchase NUSD and bridge to the BNB Chain to redeem for $1 worth of USDC. The bot/user can do this until the purchases of NUSD increase the price of NUSD to parity with $1.

However, the Asteroneo team believes that once the GAS-NUSD liquidity pool reaches a certain level, price stability will increase, and it will become more difficult to de-peg NUSD from its $1 target.

Goals for NUSD

The Asteroneo team anticipates the new bridge will facilitate various types of DeFi-related activity, such as simpler price discovery for tokens, LP pools with stablecoin pairs, trading opportunities, and initial DEX offerings and token launchpads.

Looking forward, the Asteroneo team intends to add support for more stablecoin offerings (i.e., USDT, DAI, and TUSD), add support for more than ten blockchain networks that users can bridge between, and integrate NUSD borrowing and lending through a collaboration with Intersect Finance.

Asteroneo has acknowledged that NUSD might lose its relevance at some point in the future, possibly because more entrenched stablecoins like USDC or USDT might see widespread support on Neo X, or Neo Global Development launches an official Neo X bridge. Should this become the case, the team plans to launch a stableswap feature that will allow users to exchange stablecoins. Asteroneo will cease LP rewards on associated pools and migrate the hypothetical rewards to potential USDC or USDT LPs in that potential timeline.

The full announcement can be found at the link below:

https://asteroneo.medium.com/nusd-bridge-is-coming-on-september-2nd-79271c899667

The post Asteroneo launches USDC bridge to Neo X EVM sidechain, establishes NeoUSD stablecoin appeared first on Neo News Today.