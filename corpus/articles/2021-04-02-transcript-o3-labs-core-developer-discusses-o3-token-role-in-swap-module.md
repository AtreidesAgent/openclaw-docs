---
title: "Transcript: O3 Labs core developer discusses O3 token role in Swap module"
date: 2021-04-02
url: https://neonewstoday.com/general/transcript-o3-labs-core-developer-discusses-o3-token-role-in-swap-module/
tags: [General, Interviews, FLM, NEO]
source: neonewstoday
---

# Transcript: O3 Labs core developer discusses O3 token role in Swap module

**Published:** Fri, 02 Apr 2021 15:20:33 +0000
**URL:** https://neonewstoday.com/general/transcript-o3-labs-core-developer-discusses-o3-token-role-in-swap-module/
**Tags:** General, Interviews, FLM, NEO

---

The O3 Swap aggregator service will offer a new O3 token to incentivize users, liquidity providers, early adopters, and community contributors. O3 Labs core developer, Blue, recently participated in an AMA to discuss Swap’s processes, the O3 token, and next steps.

O3 Swap is a proprietary cross-chain protocol that aggregates liquidity sources across various non-custodial exchanges. It is designed to let users exchange tokens in a permissionless manner with a single click.

The Swapping module will utilize a four-layer structure that serves as a central point for various blockchain networks, market liquidity, settlement, and applications. Blue noted, “This structure ensures integrity and symmetry of the information in markets with liquidity.”

In the AMA, Blue announced the new O3 token and its role in the Swap’s economic model, yielding holders a portion of the Swap module’s fees. The O3 token can only be acquired in the following three ways:

- Through early participation in product testing and community contributions

- As trade mining rewards for using O3 Swap

- By providing liquidity to cross-chain pools 

O3 Labs released a lite paper with more information about the O3 token and plans to host an AMA to discuss the economic model in further detail.

The full transcript can be found below: 

Matt: Hi, everyone. Welcome to O3 Live on the official Telegram channel! I’m Matt, the communications specialist from the O3 team.

 Let’s welcome our guest, Blue, the core developer of O3 Labs.

Blue: Hey guys! Thanks for having me. I’m the tech leader at O3 Labs, and today I’ll be discussing O3 Swap. 

O3 Swap is a proprietary cross-chain aggregation protocol built by O3 Labs. The mission of O3 Swap is to provide consumers access to cryptocurrency-based financial services, allowing them to exchange or ‘swap’ various digital assets within their O3 Wallet.

Matt: So basically, to swap one coin for another?

Blue: Simply put, we solve the problem of mobility fragmentation on different networks.

Users can swap assets of different networks and connect to different non-custodial exchanges.

Matt: What are the primary features of O3 Swap?

Blue: First, it offers liquidity aggregation. Users can exchange assets at the lowest rate and via the most efficient trading route — this is achieved by connecting their own decentralized wallets.

Second, O3 Swap is a cross-chain exchange service. We implement all proven and possible cross-chain solutions onto the market with our aggregation protocol. With this, we can achieve cross-chain transactions. Users can freely exchange multi-chain assets with one click.

Third, O3 Swap is permissionless and offers anti-censorship swapping. In any environment, anyone can access the O3 Swap without permission and a KYC review. 

Matt: What’s the layer structure of O3 Swap? How does the design achieve these features?

Blue: O3 Swap uses a four-layer structure: network layer, market liquidity, settlement layer, and application layer. 

Source: O3 Labs

This structure ensures the integrity and symmetry of the information in markets with liquidity. As a result, the user has a safe and efficient trading environment.

From the image above, we can see that the wallet, swap, and payment are all at the top layer, built on the networks and protocols. 

Matt: Take us through the process of swapping out coins.

Blue: Okay, let me go over the O3 Swap running logic. 

Source: O3 Labs

Let’s take an example of a token swap between Binance Smart Chain and Huobi ECO Chain (BETH to HUSD). Our swap function will exchange BETH to BUSD automatically via non-custodial exchanges that are built on BSC. Then BUSD will be exchanged for HUSD via our cross-chain pool. Finally, you will receive the HUSD in your HECO wallet.

The O3 Relayer is the agent of the user and the contract on the chain. Depending on the different users’ needs, the O3 Relayer can find the best exchange rate through the O3 Swap.

Swapping is the core exchange mechanism of the system. It receives users’ requests from the relayer and achieves liquidity settlement by smart contracts.

The aggregator identifies liquidity sources on the market and determines the best trading rates and routes for users. 

The cross-chain asset transaction pool is built based on the Poly Network protocol and realizes the free exchange of assets across chains.

O3 Swap relies on these formations to function.

Matt: What will be the process of earning the O3 Swap token? Will this token be called O3?

Blue: Yes, the token will be called O3. The O3 Swap Token is an application token issued by O3 Swap. In the economic model of the O3 Swap, there are three ways to earn O3.

First, to receive airdrops through early participation in product testing and community contributions.

Second, to receive trade mining rewards by using O3 Swap.

Third, to provide liquidity to cross-chain pools and earn O3 rewards.

Matt: When will the O3 Labs community be able to participate and earn O3?

Blue: At first, users can participate in trading mining, and they’ll receive O3 as a reward after trading on O3 Swap. 

Matt: O3 Swap users can expect to earn O3 in Q2 2021, maybe April or May.

Blue: According to the amount of O3 purchased each time, O3 will be distributed for trade mining rewards according to the initial default 1:1. The time of rewards settled and distributed depends on the block time period.

Q1: Which coins or tokens are included in the O3 Swap?

Blue: O3 Swap will support Ethereum, Neo, Binance Smart Chain, Huobi ECO Chain, and other network assets.

Q2: Will users receive more O3 based on the value of the trade, or a set number (i.e., one O3 token) per trade?

Blue: Good question! The formula for trade mining is as follows:

- MiningRewardsO3 = BuybackO3 * 100%

The initial ratio defaults to 100%, meaning that for every O3 buyback, the system releases one O3 token for trade mining. The distribution percentage can be determined by DAO proposal voting in future functionality.

Q3: What role will FLM play on O3 in the future?

Blue: Flamingo is our partner. We will support FLM trading, and users can trade Flamingo assets on O3 Swap. 

Q4: What steps are O3 Labs taking to prevent smart contract vulnerabilities that have been exhibited in the DeFi space?

Blue: We will get a professional organization to do a contract audit and introduce a vulnerability finding reward. 

Q5: How can users receive airdrops?

Blue: We will airdrop for several ways: 

- Part of users and supporters of O3 Wallet

- Early users of O3 Swap

- Holders of partner project tokens, such as NEO

- Community contributions

Though, we recommend downloading O3 Wallet and using O3 Swap.

Q6: How does O3 Swap solve liquidity issues with non-custodial exchanges?

Blue: The O3 Swap aggregator helps users to connect most of the leading non-custodial exchanges. O3 Swap does not utilize its own AMM pool.

Furthermore, we designed an incentive mechanism for users who provides liquidity in cross-chain pools. We will reduce transaction fees and reward O3 tokens to those users.

Q7: Who has partnered with O3 recently for future projects?

Blue: O3 Labs have obtained investment from some top investment institutions and well-known exchanges, and we will further cooperate with them, but we cannot make it public at present. Stay tuned!

As for the future plan, we will focus on how to simplify the transaction process. We will also cooperate with some excellent Layer Two projects, so that users can complete cross-chain transactions more conveniently.

Q8: What are the innovations and advantages of O3 Swap compared to others?

Blue: There are three competitive advantages of O3 Swap compared to other non-custodial exchanges on the market.

First, O3 is the first DeFi project to build a cross-chain trading pool. The pool will allow for the open exchange of major assets which span multiple blockchain networks, and provide a unified token mining experience for multi-chain assets. There is a low risk and a high return.

Second, combined with liquidity aggregation and trade mining, we will collect the best trading rate and routes for users. We will save time and cost for our users!

Third, O3 Swap has a rather innovative economic model where we will share the earnings from O3 Swap with O3 traders and holders. It should attract more and more people to participate on our platform.

Q9: What is the total supply of the O3 token?

Blue: The total supply is 100 million, and the mechanism of distribution will be explained in the forthcoming lite paper. 

Matt: We will have another AMA about O3 token economics very soon, so you’ve got to stay tuned.

We hope you guys got some insight into our newest project in this session.

Thank you!

Note: Some edits have been made for formatting and readability.

The full AMA can be found at the link below: https://t.me/O3Community/30016 

The post Transcript: O3 Labs core developer discusses O3 token role in Swap module appeared first on Neo News Today.