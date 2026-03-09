---
title: "Polaris feature: Feedio – a decentralized price feed platform"
date: 2022-08-23
url: https://neonewstoday.com/defi/polaris-feature-feedio-a-decentralized-price-feed-platform/
tags: [DeFi, General, Feedio, GAS, NEO]
source: neonewstoday
---

# Polaris feature: Feedio – a decentralized price feed platform

**Published:** Tue, 23 Aug 2022 22:10:07 +0000
**URL:** https://neonewstoday.com/defi/polaris-feature-feedio-a-decentralized-price-feed-platform/
**Tags:** DeFi, General, Feedio, GAS, NEO

---

Feedio is a decentralized price feed platform that reduces the complexity of retrieving prices of various assets via blockchain. Instead of performing oracle calls, dApps subscribe to the service and avoid expensive onchain processes. Feedio aggregates data from multiple sources to provide real-time price information through its smart contracts.

Feedio was submitted to the Polaris Launchpad by Kinshuk Kar (also known by the handle Durneja on Twitter and Discord) and Pompita Sarkar (aka Sooperminion on Twitter). The team is familiar with Neo N3, having won an Excellence Award in the 2021 Frontier Launchpad for its Impel project. Impel used Neo to reward users for completing exercise challenges verified by the Strava fitness application. Though it received an Excellence Award, Derneja and Sarkar did not continue the project.

The Feedio team was inspired to built its Polaris project by oracle services in other blockchain ecosystems. In a conversation with NNT, Durneja said:

The inspiration behind Feedio was the Neo oracle mechanism as well as the Chainlink ecosystem. For blockchain-based solutions to succeed, they have to have a way to connect with the offchain world to enable real-world use-cases. In terms of what Feedio ultimately achieves, I would like it to become a go-to toolbox of solutions on top of which DeFi apps can be successfully built. It would take care of all the standard and critical needs that most DeFi apps require, like real-time pricing information. This would allow DeFi app builders to exclusively focus on building their unique value proposition and innovate for millions of users to onboard.

Feedio aggregates price data from independent API providers such as CoinMarketCap, Binance, and CoinGecko, and publishes it onchain. Multiple API sources increase the reliability of price feeds as there is no dependency on a single source provider.

Alongside aggregating centralized price feeds, Feedio also built a bridge-like protocol that retrieves data from the Chainlink decentralized oracle service. Chainlink enables smart contracts to securely interact with services that exist outside of blockchain networks. The data from Chainlink is then normalized against the other price providers to enhance the reliability of the reported data.

Source: Feedio

While its development team will maintain a collection of price feeds, Feedio was designed to allow anyone to establish a service using their own price data sets. The Feedio demonstration from the Polaris Demo Days included price feeds for NEO, GAS, BTC, ETH, and MATIC.

The onus is on the data aggregator to ensure the validity of its prices and should include information about the strength of their sources, such as reliability, uptime, and other metrics. When a new feed is established, Feedio will write that data to a common aggregator contract on behalf of the data provider.

The Feedio team received an Excellence Award and a multiplier of 1.5x in the recent Neo Polaris Launchpad, rewarding the team with an equivalent of US $12,000 in prizes.

Why is an onchain price feed provider necessary?

Oracle services can be expensive, especially when used on an ongoing basis. For example, it costs 0.1 GAS to make an oracle call on the Neo N3 network. When this cost is passed onto the user of a dApp that must make several oracle calls, it becomes a barrier to adoption.

In contrast, Feedio offers a subscription service to access its platform. Each subscription is represented as an NFT, incorporating an expiry timestamp that removes access to Feedio’s feed. The NFT subscriptions can be renewed and extended using GAS.

Each NFT subscription costs 30 GAS per month. Durneja estimates the monthly expense to run Feedio is approximately 650 GAS, requiring a minimum of 23 dApps to use its service to run at breakeven.

Post-Polaris

Since the Polaris Launchpad, Durneja has fixed bugs and issues found in the Feedio platform during the hackathon. Moving forward, the Feedio developers intend to focus on higher frequency API feeds.

The new service will integrate one-second price updates, but the information will not be published onchain. The high-frequency HTTP API service will run in parallel with the onchain service. The team initially planned to publish price feed data onchain at a 60-second cadence, but the frequency will likely decrease to reduce operating costs.

Looking forward, Durneja intends to release a Feedio whitepaper at some point in Q4 2022.

To learn more about Feedio, visit the link below:

https://feedio.xyz/

The post Polaris feature: Feedio – a decentralized price feed platform appeared first on Neo News Today.