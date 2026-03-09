---
title: "O3 Labs and Switcheo discuss ongoing development and preparation for Neo3 in recent AMA"
date: 2020-10-28
url: https://neonewstoday.com/general/o3-labs-and-switcheo-discuss-ongoing-development-and-preparation-for-neo3-in-recent-ama/
tags: [General, NEO, O3, SWTH]
source: neonewstoday
---

# O3 Labs and Switcheo discuss ongoing development and preparation for Neo3 in recent AMA

**Published:** Wed, 28 Oct 2020 23:40:34 +0000
**URL:** https://neonewstoday.com/general/o3-labs-and-switcheo-discuss-ongoing-development-and-preparation-for-neo3-in-recent-ama/
**Tags:** General, NEO, O3, SWTH

---

O3 Labs is building infrastructure for Neo3 and Switcheo discusses progress on its derivatives exchange in recently held Ask Me Anything.

On October 28th, O3 Labs and Switcheo held an AMA on Switcheo’s official Discord channel. Switcheo CEO, Ivan Poon, and O3 Labs community managers, Caroline and Sophy, joined the AMA to discuss their projects.

Poon fielded questions about Switcheo developmental updates, upcoming staking and liquidity pool rewards documentation, upcoming trading features, and a potential hackathon.

Sophy and Caroline referenced recent infrastructure development on O3 products to prepare for Neo3, cross-chain protocol development, and Ledger support issues.

The full transcript can be found below:

Q1: The community is asking for more regular updates on development, like weekly or biweekly reports. Often people keep speculating on what is coming, but we never have the real information and full picture. Any plans to do this? 

Ivan: No. For those that have followed us from the start, we used to do this. It’s extremely draining on the team, and basically a waste of time.

In real engineering, the update of what was done in a weekly / bi-weekly sprint on a high (non-technical) level is just: “same as last week.” New, innovative, hard stuff takes time to build.

What ends up going in is just fluff by me or the marketing team. We also get pushed to give launch targets, which is basically all downside and no upside: it lets competing protocols know what we are doing, and we get FUD whenever we miss targets. In real engineering, launch dates are also notoriously hard to get right (just look at ETH 2.0).

Personal opinion: most projects that do this just want to comfort bagholders. Legit projects just ship.

TLDR: Does AAPL give weekly updates? I think we should be moving forwards, not backward.

Q2: What is the timeframe for the Demex launch? Is it happening in 2020? Will there be another testing round before launch? What is the progress made so far, what is still in the pipeline? 

Ivan: We were ready for launch in October 2020, but decided to combine some later features, like the automated-market maker, into phase one. There are no more “testing rounds,” the trading engine is working as expected.

Our beta is constantly running at beta-app.dem.exchange. Tokens can be minted at @the_tradehub_bot.

Q3: It was announced several months ago that Binance pool is joining TradeHub as a validator; when do you expect them to join?

Ivan: No idea. We need to ping them on that again.

Q4: Is the one page, six pager ever coming out to the public?

Ivan: Maybe, it was formatted for private consumption, to be honest. I haven’t had time to clean it up into a blog post with a standard most people that are familiar with my writing would recognize.

Q5: Any plans for a new developer dApp contest?

Ivan: It will be far more involved than a simple contest.

Q6: When will we find out why TradeHub withdrawals began earlier than intended (phase 0.5)?

Ivan: This week, I think.

Q7: Will Switcheo support Neo3?

Ivan: We will.

Q8: Where will the SWTH from the “coin base” or “block reward” come from? Team holdings?

Ivan: Inflation by either an increase in the SWTH supply, or dilution of all other holders.

Q9: Are there any plans to have the SWTH token listed in other exchanges?

Ivan: Yeah.

Q10: Can you share details on the current O3 and Switcheo partnership?

Sophy: There will be a direct connection with Switcheo in the O3 Wallet, and we hope to have deeper collaborations moving forward.

Ivan: Maybe O3 can support the Switcheo TradeHub protocol for staking and trading natively together with BTC and ETH.

Q11: Can we expect a native Bitcoin bridge on TradeHub by the end of year timeframe?

Ivan: Most likely. It’s one of the active development/top priority things right now. For now, WBTC and tBTC seem like pretty good alternatives, though.

Q12: Will Ethereum non-custodial aggregators (like 1inch) be able to direct trades to Switcheo’s AMM?

Ivan: Most likely not. One idea is to make the Switcheo Exchange an aggregator that can wrap and use layer two protocols and AMMs.

This is because aggregators are themselves layer one smart contracts. They won’t do cross-chain actions and are wrapped around other layer one smart contracts.

So, Switcheo Exchange -> simple swap mode, Demex -> pro CLOB mode. I think that makes more sense product-wise.

Q13: Both liquidity pools and SWTH stakers will receive rewards from trades done on Switcheo AMM?

Ivan: Yes. LPs earn by staking their LP tokens, and SWTH by staking SWTH. Rewards will come from trade commissions, transaction fees, and inflation.

LPs will earn more as makers for trades are done on their pair and matched against the AMM.

Q14: What is the trade commission? And how is it split between SWTH stakers and LPs?

Ivan: The default is 20 basis points, which can be set by protocol later on.

The answer to that is shown in the following screenshot:

Source: Ivan Poon

We will release a more readable version of the screenshot when we are launching.

Q15: What new features will the O3 Wallet bring to users?

Caroline: I would like to say many extraordinary functions are coming next month. As I said above, we will support more assets such as ETH and BTC and provide cross-chain services between them. Yeah, stay tuned. It’s coming.

Q16: Recently, many wallets focus on developing dApps to attract users, so what kind of dApp platforms will the O3 team focus on?

Caroline: For dApps, we are definitely working on this area though we already have more than 20 dApps from the Neo ecosystem. We have entertainment dApps such as Blocklords, FTW, and Blockchain Cuties, as well as finance dApps such as O3 Swap, Switcheo, and Nash.

Check your favorite dApp on the Discover page of the O3 Wallet. We are also exploring some valuable dApps on the Ethereum chain recently to serve our users better.

Q17: Could you share the main focus of the O3 team and what the tech team is working on right now?

Sophy: We have recently been focusing on supporting ETH, BTC, and the Neo3 TestNet.

Q18: Why can’t I sign the transaction on Switcheo using Ledger with an O3 connection?

Caroline: When encountering Ledger issues, we always suggest users turn off the Ledger and restart it first. Also, make sure to download the latest version of the O3 Wallet.

Due to Ledger’s original design, it has physical limitations that only allow a small amount of UTXOs when sending tokens. O3 Labs has released the “UTXO manager” to assist Ledger users. You can find details and solutions here:

https://medium.com/o3-labs-o3-wallet/things-you-should-know-before-getting-a-ledger-5d5545d80673

Q19: Will the O3 Wallet support Neo3?

Caroline: O3 will fully support all of Neo3’s modules. Right now, we are preparing the wallet-related infrastructures and the desktop version of the O3 Wallet. Our goal is to first offer support for Neo3 TestNet in early November 2020.

We will go with Neo3 synchronously when the TestNet officially debuts for the public.

Note: Some edits have been made for formatting and readability.

The post O3 Labs and Switcheo discuss ongoing development and preparation for Neo3 in recent AMA appeared first on Neo News Today.