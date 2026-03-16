---
title: "Neo ecosystem developers release sidechain bridge for Neo and Binance Chain interoperability"
date: 2020-03-21
url: https://neonewstoday.com/general/neo-ecosystem-developers-release-sidechain-bridge-for-neo-and-binance-chain-interoperability/
tags: [General, NEO]
source: neonewstoday
---

# Neo ecosystem developers release sidechain bridge for Neo and Binance Chain interoperability

**Published:** Sat, 21 Mar 2020 11:21:08 +0000
**URL:** https://neonewstoday.com/general/neo-ecosystem-developers-release-sidechain-bridge-for-neo-and-binance-chain-interoperability/
**Tags:** General, NEO

---

The team behind the NeoLogin project has released the SmartBNB protocol, which is intended to allow tokens on Binance Chain to use Neo smart contracts through the use of a cross-chain bridge. The protocol aims to leverage cross-chain interoperability to increase addressable markets for applications and tokens on both networks. The NeoLogin team is made up of co-founders Albert Acebrón (aka corollari), Salah Karim Abdelbaki (aka 0xsalah), and Thijs Maas.

Acebrón was also a guest on Episode 21 of the Neo News Today (NNT) podcast, where he discussed his move from Ethereum to Neo, his experiences in the ecosystem, how the NeoLogin non-custodial wallet solution operates, and more.

More recently, in a conversation with NNT, Acebrón iterated that the SmartBNB protocol has created the opportunity for Binance Chain-based tokens to run smart contracts via a decentralized sidechain bridge with Neo. SmartBNB was born of a proposal to the Binance Fellow program. Acebrón said:

“I met someone from Binance at a hackathon, and after talking a bit, they seemed to like my ideas around cross-chain systems. So, we kept in touch, and later I sent them the SmartBNB proposal, which they decided to fund.”

Neo is purportedly the first public blockchain that Binance Chain has integrated with to offer cross-chain smart contract functionality. Acebrón stated, “as far as I know [the SmartBNB protocol is] the only trustless way for tokens on Binance Chain to run smart contracts.”

How SmartBNB works

The SmartBNB protocol emulates a sidechain as it utilizes a token locking system to mint tokens, and a burn method to unlock tokens. Custodians are responsible for offering the collateral for a Neo-based smart contract. Once the smart contract is launched, custodians can “receive and safe keep tokens from SmartBNB users who want to port tokens from Binance Chain to Neo.”

There are almost no restrictions as to who can become a custodian; the only requirement is users deposit GAS as collateral.

Once the collateral is pegged on the Neo blockchain, Binance Chain users can send their BNB tokens to the custodian, where their assets will be stored. The custodian then mints tokens on the Neo blockchain and sends them to the Binance Chain user.

When the user is ready to redeem their tokens, they burn NEP-5 BNB, and the peg will unlock the BNB that was previously locked in Binance Chain.

If the custodian doesn’t return the BNB tokens to the Binance Chain user, their GAS-backed smart contract will be liquidated, and those funds distributed to the affected user.

Further information on its processes can be found on the SmartBNB protocol GitHub page.

Potential benefits to the Neo ecosystem

Building a sidechain to interact with Binance Chain carries with it a handful of potential benefits according to Acebrón. First, the size of the NEO market could increase by integrating with Binance Chain and gaining access to its decentralized exchange.

Second, through a potential increase in an addressable market, Neo-based dApps may increase their user base as they can gain access to Binance users and vice versa. Acebrón believes this could enable “multiple types of collateral for protocols like Alchemint, and more trading activity on Switcheo.”

Third, projects building on Binance Chain seeking to add smart contract functionality to their tokens “might also start building DeFi-based dApps on Neo in order to have access to [special mechanisms around their token],” according to Acebrón.

Though, he has higher hopes for the potential SmartBNB offers. He said:

“What I think might be the biggest game-changer: SmartBNB could become the biggest DeFi platform on Neo, as it allows users to lock GAS and get interest on that. Platforms such as these have seen huge usage in Ethereum (see Compound), and because of the way SmartBNB works, it means that GAS holders that choose to participate with their coins would get guaranteed returns (at the risk of getting slashed if they don’t follow the protocol).”

Barriers to widespread use

Acebrón also pointed out there might be factors that would limit the use and success he envisions for the SmartBNB contract.

NEO and GAS token holders may not wish to use the SmartBNB protocol because it could add additional layers of risk. For example, there could be a bug in the contract or an issue with the recipient blockchain. Additionally, to provide collateral for the SmartBNB protocol, users are required to run a node, which may deter non-technical participants.

BNB-based tokens and projects may also feel uncomfortable with the security model used in the protocol, as it requires users to trust both Neo and Binance Chain validators. Further, users are subject to the constant burn rate of the BNB token, which “means that users will have costs similar to those incurred when trading with leverage,” according to Acebrón.

And finally, a lack of use could stem from a shortage of demand for smart contract functionality with BNB tokens.

Looking forward

Currently, the SmartBNB contract is running on the Neo TestNet. At this time, Acebrón does not have an estimated launch date on MainNet in mind. He cited high costs of third-party audits and potential legal responsibility of an un-audited faulty contract on MainNet as current roadblocks.

Looking forward, he said, “we are finishing up some parts of the protocol as well as the node software. We are also asking for quotes on a security audit of it. Once we are done, we will market it heavily to projects building on Binance Chain and will encourage teams building on Neo to integrate SmartBNB into their projects.”

More information about the SmartBNB protocol can be found at the link below:

https://smartbnb.net/

The post Neo ecosystem developers release sidechain bridge for Neo and Binance Chain interoperability appeared first on Neo News Today.
