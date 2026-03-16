---
title: "The evolution of GAS in the Neo N3 blockchain ecosystem"
date: 2021-04-19
url: https://neonewstoday.com/general/the-evolution-of-gas-in-the-neo-n3-blockchain-ecosystem/
tags: [General, GAS, NEO]
source: neonewstoday
---

# The evolution of GAS in the Neo N3 blockchain ecosystem

**Published:** Mon, 19 Apr 2021 16:10:03 +0000
**URL:** https://neonewstoday.com/general/the-evolution-of-gas-in-the-neo-n3-blockchain-ecosystem/
**Tags:** General, GAS, NEO

---

A unique characteristic of Neo is its dual token model. NEO serves as the governance token and is indivisible, while GAS serves as the utility token for the Neo network and is divisible to the eighth decimal.

Among the many changes in Neo’s new N3 version is an increasingly important role for GAS. Not only do the use cases for the token expand, but the conditions for it to be useful are also much more favorable.

On Neo Legacy, GAS is used as payment for network resources, deploying smart contracts, and other on-chain services.

However, a combination of issues such as GAS being a UTXO asset, an inflexible fee pricing structure, and user access to free transactions means that GAS has never really been used to its fullest potential.

While all of the GAS use cases found in Neo Legacy remain in N3, this article will outline some of the biggest changes to GAS along with its increased utility.

Token supply

On Neo Legacy, GAS is gradually released into the network each block from a 100 million total supply, distributed over 22 years through a decaying-rate algorithm. This means that less GAS is produced per block over time until all 100 million are released.

In N3, GAS no longer has a total supply cap and is distributed at a fixed inflationary rate of 5 GAS per block. This number was chosen because it is the current rate of GAS generation at this stage of decay in Neo Legacy.

However, a deflationary element has also been introduced in N3, similar to Ethereum’s EIP-1559, where GAS spent on transaction fees are burned. This differs from Neo Legacy, where system fees are pooled and distributed to NEO holders.

In Neo Legacy, GAS was intended to be a means of transfer, but its model incentivizes saving GAS as opposed to spending. The unused GAS issue is compounded by NEO black holes (i.e., lost addresses with NEO or NEO sent to a burn address) accumulating unclaimable GAS that will never enter the network. N3 mitigates this issue through an unlimited supply of new GAS that can outpace the rate of that lost in forgotten wallets or burn addresses.

Since there will be no limit to the amount of GAS created, users are incentivized to use the token as a means of transfer. In N3, the 10 free GAS per contract execution is removed, and GAS is required to pay for each network and system fee.

Removal of 10 free GAS

On the Neo Legacy network, the first 10 GAS spent on system fees in a transaction are waived. System call fees vary in price depending on the functionality being used.

The most costly fees include 5,000 GAS for creating a global (or UTXO) asset, 1,000 GAS for registering a validator, and between 100 to 1,000 GAS for creating a contract, depending on the need for contract storage or dynamic invocation.

These costs are permanently embedded in the NeoVM coupled with the Neo blockchain. The 10 GAS subsidy was designed to cover most of the smaller system fees. Examples include system calls to the blockchain ranging from 0.1 or 0.2 GAS, or OpCode instruction fees ranging from 0.001 to 0.02 GAS.

The 10 GAS waiver ensures a user can send NEO, GAS, or NEP-5 assets on the network without incurring a cost unless opting to pay for priority. It also encourages developers to write efficient contracts, as keeping execution costs below 10 GAS effectively means users are able to use their applications for free.

The GAS fee waiver no longer exists in N3. However, the pricing model is more variable and responsive to the user’s needs of the blockchain and accompanying services. With a decoupled virtual machine in N3, system fees can be modified by the new Neo Council, elected by token holders, without impacting the blockchain state.

Pricing mechanism change

The pricing fee changes in N3 make Neo more affordable for developers. On Neo Legacy, GAS prices to deploy smart contracts have acted as a barrier to entry. Neo hopes that lower GAS costs in N3 may spur new project development.

N3 has a much more extensive fee structure than its predecessor, with the majority of the fees drastically lowered. The cost reductions are possible because of pricing scheme changes at the smart contract level. Examples of price reductions from Neo Legacy to N3 include:

- Smart contract deployment: 1,000 GAS to 10 GAS

- Runtime.checkwitness(): 0.2 GAS to 0.003 GAS

- Storage.get(): 0.1 GAS to 0.01 GAS

N3’s pricing model implements a new adjustable approach.

The new model relies on a base execution fee, defined as the execution time for the most basic OpCode, NOP, expressed in GAS. Each other instruction fee is defined as a coefficient that is applied to that base fee depending on its relative execution time. These execution times are compiled from a table derived using two different VM implementations, in C# and Go, to provide fair estimates across different software.

A key benefit of the new design is the ease of adjusting system fee prices if the market value of GAS changes.

As each fee is denominated as a coefficient of a single base fee, only that base fee alone needs to be adjusted. Reducing the base fee by a factor of 10 will automatically scale this price reduction across all other system fees.

The base fee adjustment can be made by the Neo Council, providing a decentralized mechanism for the network to adjust to GAS volatility and remain competitively priced.

Voting/governance incentive

Historically, NEO holders have received GAS distributions just for taking custody of NEO tokens in a private wallet. While this is still true in N3, NEO holders will need to take an active interest in the platform’s governance process to receive the maximum amount of available GAS.

Neo’s new dynamic on-chain governance mechanism is touted by Da Hongfei as the most “important and sophisticated” change in the ecosystem. Under the new model, NEO holders will elect a Neo Council consisting of 21 members that will be responsible for overseeing network upgrades, fees, assigning infrastructural roles (i.e., NeoFS inner-rings, oracle nodes, StateRoot validators) and more.

Any individual, organization, or entity can apply to be a council member directly on the blockchain, making registration permissionless. A fee of 1,000 GAS must be paid to register as a candidate. Of the 21 council members, the top seven with the most votes will become consensus nodes responsible for producing blocks.

On Neo Legacy, 100% of newly minted GAS is distributed directly to token holders simply for holding NEO. In N3, this will drop to 10%, with 80% being awarded to users who have voted for a Neo Council member. The final 10% will be distributed to Neo Council members as a reward for their work.

NeoFS payments

The NeoFS distributed, decentralized object storage system offers hardware providers the opportunity to rent out unused storage in exchange for GAS.

Potential use cases for NeoFS include private data storage for users, dApps and content delivery networks, data exchange for small to medium-sized enterprises, unstructured IoT data, NFT content and metadata storage, and fixed document storage.

GAS payments are used in NeoFS for various network operations. Examples include exchanging assets, depositing and withdrawing GAS, and maintaining account balances for GAS circulating in the network.

Following the N3 TestNet launch in March 2021, NeoFS was deployed and became available for all users. Now that a TestNet version of NeoFS is live on Neo N3, Neo SPCC aims to launch an N3 and NeoFS-based CDN to attract larger network participants, such as data centers and ISP companies, to provide storage capacity.

Oracle payments

N3 offers a native oracle network integrated into the blockchain. Oracles enable smart contracts to obtain data from external sources, making it available for use by blockchain applications.

The native oracle network offers support for general applications and broad uses such as making calls to URL links and accessing NeoFS distributed storage.

Each oracle request carries a fee of 0.5 GAS and each verification 0.01 GAS. Like other pricing changes in N3, these fees can be adjusted via future governance processes.

GAS as a native contract asset

Lastly, GAS (and NEO) in N3 exist as native contracts and no longer use the unspent transaction output (UTXO) model. This allows the tokens to more easily be used by smart contracts and dApps.

A UTXO is an amount of cryptocurrency that remains on an address after a transaction is executed. UTXOs are continually processed and are stored on a blockchain as inputs to be used for future transactions, requiring large amounts of storage and computational resources.

UTXO’s on Neo Legacy made it extremely difficult to use NEO or GAS in smart contracts. Various wrapped versions of NEO and GAS were created on Neo Legacy to solve this issue. Examples include Flamingo Finance using nNEO, Alchemint using sNEO, and others converting GAS to cGAS.  However, the experience is not ideal, as wrapped NEO does not accrue GAS for the original owner, and users need to convert the asset back and forth depending on their needs.

Ultimately, this prevented GAS from being widely adopted as a token for payments within dApps, the way one might see ETH utilized on Ethereum.

Moving forward, N3 features the contract-based account model for NEO and GAS that is currently used by NEP-5 tokens. All Neo N3 assets are created using smart contracts, allowing all transaction types to be simplified and making GAS easy to integrate into applications.

The post The evolution of GAS in the Neo N3 blockchain ecosystem appeared first on Neo News Today.
