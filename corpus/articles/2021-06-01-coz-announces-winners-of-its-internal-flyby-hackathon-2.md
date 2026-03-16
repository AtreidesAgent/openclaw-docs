---
title: "COZ announces winners of its internal Flyby hackathon"
date: 2021-06-01
url: https://neonewstoday.com/general/coz-announces-winners-of-its-internal-flyby-hackathon/
tags: [Development, Events, General, COZ, GAS, NEO]
source: neonewstoday
---

# COZ announces winners of its internal Flyby hackathon

**Published:** Tue, 01 Jun 2021 19:23:30 +0000
**URL:** https://neonewstoday.com/general/coz-announces-winners-of-its-internal-flyby-hackathon/
**Tags:** Development, Events, General, COZ, GAS, NEO

---

COZ has announced the winners of its recent internal hackathon, Flyby. COZ held the event as a friendly competition designed to test its N3 tools prior to the Neo Frontier Launchpad event.

Seven teams made up of frontend, backend, non-technical roles competed in the Flyby hackathon over the course of eight days. As part of Flyby, participants identified missing documentation, found bugs in SDKs and tools, and explored new aspects of the updated Neo platform.

At the end of the event, each team delivered a presentation of their project and voted on the top three dApps.

The unanimous first-place project was called Crypsydra, a streaming payments service which made use of a Python smart contract compiled with Boa, alongside a Neon.js-based web app. The tool allows users to create a stream within its smart contract, funded with GAS, which is distributed to another party over a specified amount of time. The amount of available GAS that can be withdrawn from the contract increases every second until 100% is reach at the end of the stream time.

Crypsydra frontend

Streamed payments have various potential applications. For example, if a freelance contractor was hired for a job expected to take six weeks, the employer could create a stream that distributes the agreed upon compensation over that timeframe. If the contractor is failing to meet obligations part way through, the stream can be cancelled and the remaining GAS withdrawn by the employer.

Joe Stewart, one of the Crypsydra team members and Special Projects developer at COZ, is a long time developer within the Neo ecosystem. Stewart was one of the winners of the first ever public COZ dApp competition with his Neo Smart IoT project. He was responsible for authoring Neo’s NFT standard, along with the MCT Token, HashPuppies, and more. Speaking on his experience building on N3, Stewart said:

We were able to build a working N3 dApp in a single week because the quality of tooling for N3 is much better than Neo2. As someone who has been writing smart contracts on Neo since 2017, I can truly appreciate how much faster the development and testing cycle is; it’s like night and day. The improvements in neo3-boa have really sped up the debugging process for my smart contracts and eliminated a lot of the frustration of developing on Neo2.

Crypsydra also integrated COZ’s WalletConnect 2.0 proof of concept. WalletConnect is a popular open source protocol for connecting decentralized applications to mobile wallets using QR code scanning or deep linking. COZ intends to implement WalletConnect for N3 into the Neon Wallet and provide an SDK for other projects to use in their own applications. COZ is also aiming to have a lightweight web version of a WalletConnect compatible wallet available for use by the start of the Frontier development phase.

Two projects tied for second place, BetOnFlyby and Neo Voting Statistics.

Neo Voting Statistics focused on providing a governance information and voting portal. A testing environment was setup to provide a source of voting data, consisting of an 8-node neo-cli private network which was saturated with voting transactions simulated with Neon.js. Chain data related to governance, such as votes or registration of new candidates was parsed on the backend using Mamba, COZ’s Python SDK.

Neo Voting Statistics frontend

A React-based frontend provided an interface to view the gathered information about candidates, validators, and their voter distribution, intended to help voters become more informed on the entities they vote for with their NEO. The project was delivered with a UI exhibiting graphs of total votes, committee overview, registered candidates, and a preview voting page.

BetOnFlyby is a betting pool dApp conceptualized when discussing which teams were most likely to win the COZ Flyby hackathon. The prototype included a page where humorous images would flash on the screen whenever there is a smart contract invocation. Betting pools created in the contract would grant access to a web page where players can bet a fixed amount on a team, though it could be extended to support any betting scenarios. The platform also collects a house take of 5% on each bet, which remains within the smart contract. Potential future expansions could include using the Oracle service to obtain information about who won the bet from a trusted source.

BetOnFlyby frontend

Other notable solutions that came from the hackathon included a GAS calculator for smart contract invocation cost estimations in N3, a strategy game that uses NFTs for land and tokens for items, and more.

COZ co-founder, Tyler Adams, noted the progress of development in the Neo ecosystem since the first hackathons in 2017:

The level of project maturity arising from the Flyby hackathon is an attestation to the substantial improvements in the developer experience between the early days of Neo and now. In one week, we had multiple COZ teams deliver projects which were more mature than many of the fully staffed and funded initiatives in the Neo Legacy ecosystem. Our tools are sharper and our team is far more experienced. The majority of issues encountered during the event were documentation related and will be mitigated in short order.

Looking forward, COZ will use the lessons learned from the Flyby hackathon to help developers during the Neo Frontier Launchpad event.

The GitHub repositories of the winning teams can be found below:

Crypsydra

https://github.com/east-side-cryps/crypsydra-contract

https://github.com/east-side-cryps/crypsydra-web

Neo Voting Statistics

https://github.com/ixje/neo-voting

https://github.com/ixje/neo-voting-backend

BetOnFlyby

https://github.com/simplitech/Flyby-Team-6

The post COZ announces winners of its internal Flyby hackathon appeared first on Neo News Today.
