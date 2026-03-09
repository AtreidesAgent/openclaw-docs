---
title: "Offchain scaling project Trinity complete crowd sale"
date: 2018-01-15
url: https://neonewstoday.com/general/offchain-scaling-project-trinity-hold-crowd-sale/
tags: [General, TNC]
source: neonewstoday
---

# Offchain scaling project Trinity complete crowd sale

**Published:** Mon, 15 Jan 2018 21:27:13 +0000
**URL:** https://neonewstoday.com/general/offchain-scaling-project-trinity-hold-crowd-sale/
**Tags:** General, TNC

---

On January 14, 2018, Trinity launched their token sale on the NEO platform, announcing their official public donation address at 12:00 am (Beijing/CST). Trinity is an off-chain scaling scheme to be built on top of NEO, which seeks to achieve real-time payments, low transaction fees, scalability, and privacy protection for NEO assets.

The fundraising goal of $20 million USD was met the same day the token sale launched. At 12:45 am (Beijing/CST) the Trinity State’s Channel team had announced the public sale ended. The team was able to achieve their fundraising goal quickly, though there were some issues with the launch, particularly in regards to confirmation times on the blockchain.

After the public sale launched, the NEO network block time confirmations had slowed to 24 minutes and 12 seconds for Block 1,816,382, and to 11 minutes and 46 seconds for Block 1,816,383, with just 16 transactions occurring on each block.

What happened that slowed the block confirmation times?

The token sale used the application programming interface (API) of the Neon wallet. The Neon wallet infrastructure has the ability to handle such an increase in activity, but needs to be ramped up in order to actually do so. The API that serves the needed vouts for transactions is centralized, and can quickly become a bottleneck if not scaled properly. Without ample notice, the token sale wasn’t using properly scaled API, an issue that could have been solved with a little more communication and preparation.

When the API went down, a lot of transactions failed. With the increase in failed transactions, users attempted to resubmit transactions. City of Zion (Coz) has speculated the resubmitted transactions by the thousands of investors seeking to gain access to the token sale caused a lot of double spend logic to trigger. The double spend triggers led to many rejected transactions, and long block times in blocks 1,816,382 and 1,816,383.

The NEO blockchain itself, had actually performed well prior to the API scaling issue, and afterwards. Block 1,816,381 took 58 seconds to confirm, and Block 1,816,384 took 23 seconds to confirm. The following blocks confirmation times continued to remain under 60 seconds.

This issue might have been briefly touched upon in  CoZ’s Weekly Report #25 Development Update. Listed under ‘other,’ CoZ stated they’re looking into initial design of load balanced systems for CoZ nodes and APIs to handle increasing load from token presales.

The post Offchain scaling project Trinity complete crowd sale appeared first on Neo News Today.