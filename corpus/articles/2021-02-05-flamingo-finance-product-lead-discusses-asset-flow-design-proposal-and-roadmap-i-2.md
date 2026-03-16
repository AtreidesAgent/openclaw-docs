---
title: "Flamingo Finance product lead discusses asset flow design proposal and roadmap in AMA"
date: 2021-02-05
url: https://neonewstoday.com/general/flamingo-finance-product-lead-discusses-asset-flow-design-proposal-and-roadmap-in-ama/
tags: [DeFi, General, Interviews, FLM, GAS, NEO]
source: neonewstoday
---

# Flamingo Finance product lead discusses asset flow design proposal and roadmap in AMA

**Published:** Fri, 05 Feb 2021 01:08:50 +0000
**URL:** https://neonewstoday.com/general/flamingo-finance-product-lead-discusses-asset-flow-design-proposal-and-roadmap-in-ama/
**Tags:** DeFi, General, Interviews, FLM, GAS, NEO

---

Flamingo Finance product lead, Yuan Gao, participated in an Ask Me Anything to discuss the second Flamingo Improvement Proposal that was recently put to the vote. The AMA took place on the #general channel of the official Flamingo Discord. 

Flamingo Finance is a DeFi module under incubation by Neo Global Development, which offers cross-chain assets swapping and yield from liquidity pools. 

In the AMA, Gao provided an overview of lessons learned since launch, upcoming changes to the asset flow model, Flamingo’s roadmap for the first half of 2021, and answered questions from the community. He also urged FLM token holders throughout the AMA to vote on the second FIP, which concludes at 8:00 a.m. (UTC) on Feb. 8, 2021.

The full transcript can be found below:

Adam: Hi everyone! Thanks for joining us for the special AMA session.

With us today is Yuan Gao, product lead for Flamingo, who just finished his dinner. Welcome!

It’s been more than four months since Flamingo launched in Sep. 2020. Can you brief us on the latest development status of Flamingo so far?

Yuan: I believe everyone here is already familiar with Flamingo. The main purpose for Neo Global Development to incubate this project is to build a solid foundation of DeFi infrastructure within the Neo ecosystem.

With that in mind, Flamingo is not designed as a single protocol, but as a protocol cluster. It aims to provide users with a low-friction, highly integrated DeFi experience. At present, we have launched several main components:

- Flamincome: the ERC-20 asset gateway and yield aggregator on Ethereum

- Wrapper: the on-chain asset cross-chain component

- Swap: AMM-based non-custodial exchange

- Vault: asset management and staking

- Vote: The MVP of on-chain governance

In all, we have built up some essential building blocks for DeFi on Neo: cross-chain, exchange, asset management, and governance.

Thanks to the overwhelming support from every one of you, Flamingo has achieved some pretty good results since its launch. For example, cross-chain assets have exceeded US $1 billion; the highest TVL has exceeded $2 billion; and, Swap has created more than $20 million in transaction fees for liquidity providers.

On the other hand, we have also encountered some problems and setbacks such as front-end congestion due to excessive traffic on the first day of launch, and asset price deviation due to complex mechanisms. The Flamingo team has been actively and prudently solving these problems.

In Q1 and Q2 of 2021, we have several goals:

- Restructure the asset structure of the entire Flamingo system (including the Ethereum side and the Neo side) to ensure the price pegging mechanism and provide a competitive, low friction, upgradeable and compatible asset circulation environment.

- Launch the on-chain perpetual contract trading component, which will eventually expand into a derivative platform that can trade any asset in the future.

- Exploration and expansion, including new components, project cooperation, and the possibility of deployment on multiple chains.

Adam: Thanks for such a comprehensive summary of where we came from and where we are heading.

You have mentioned that we have faced some problems and setbacks, I believe many community members also would Iike to know more about what went south, and what the team has been doing to solve those issues.

Yuan: Many challenges indeed.

During launch, the team underestimated the level of participation. Once Mint Rush was turned on, the concurrency in the first few minutes reached close to 100,000, which put tremendous pressure on wallets, node services and front-ends, and resulted in a less ideal user experience.

The team has been working with NeoLine, O3, and ONTO wallets quite often to complete a lot of scalability and optimization work. In addition, a dynamic node service cluster and front-end protection mechanisms were also established. With all these efforts, the capacity to handle large traffic is much improved.

Secondly, and probably the most complained about issue is the asset price deviation.

Flamingo’s asset synthesization mechanism is rather complicated. It includes multiple synthesis and cross-chain operations, and the concept of non-transferable CDP (Collateralized Debt Positions).

Although it guarantees the pegging of the asset value from the mechanism, it introduces a relatively large friction to asset’s liquidity and arbitrage, and we have witnessed price deviations between cross-chain assets and original assets in Swap.

And that’s the fundamental motivation behind FIP #2 to solve this problem once for all. 

Next let’s talk about Perp – the on-chain perpetual contract trading component that we are currently developing and testing.

This is still a very cutting-edge field, there is not a mature solution in the market so far. We are facing many intertwined problems:

- Risk control mechanism

- Price convergence mechanism

- Devising a robust algorithm based liquidity adjustment mechanism

Through the Perp Trading Competition that concluded not long ago, we found a lot of problems. The team is currently adjusting and optimizing on various aspects. In the later stage, we hope that after several rounds of similar tests, we will go online again on the premise of ensuring maximum security and user experience.

Adam: Thank you! FIP #2 is something the community has been talking about a lot recently.  Many community members have voted, while some are still unclear what will be changed and how those changes will affect the users. Would you take this opportunity to explain everything in FIP #2? What is the proposed asset flow?

Yuan: Sure, I think this part is quite important. The goals of FIP #2 include:

- Minimize the friction of asset flows, reduce arbitrage costs, and ensure the value-pegging of cross-chain assets

- Reduce users’ cognitive costs, provide the most concise user experience

- Try to be future-proof to ensure the compatibility and scalability of the asset system

Therefore, we have reconstructed the current asset system circulating in Flamingo and Flamincome. Now, users will only need to remember three assets: x-, y-, and f- assets.

Here is a graph to help to understand the new asset mechanism.

Source: Flamingo Finance

X-assets refer to the synthetic assets cross-chain from Ethereum to Neo through Flamincome as a gateway. Currently, it mainly includes several mainstream assets: WBTC, WETH, USDT.

Y-asset is an interest-earning asset with leverage. Similar to assets in other yield aggregators such as YFI, users can deposit assets and the contract will automatically select the best yield strategy.

The difference is that the staked assets behind x-assets will also participate in yield farming. This part of the yield will be shared by the holder of the y-assets.

This mechanism leads to the biggest advantage of holding y-assets: the return of y-assets is inherently higher than that of any other yield aggregators. By this way, we are trying to integrate the asset cross-chain and yield boosting.

The f-asset is a type of aggregated synthetic asset in the Flamingo platform. Assets derived from the same original collateral can be 1:1 converted into f-assets.

Let me give an example. We have the x-assets, which I just mentioned, and the existing pn-assets, as well as other cross-chain assets that we may support in the future, such as p-assets (directly via Poly Network), all of these assets can all be converted 1:1 to f-assets.

The significance of f-assets is to ensure that the future upgrades and changes in the asset system will not have an excessive impact on the current Swap transaction pair, and will make future protocol upgrades and optimizations more compatible and sustainable.

In order to improve the user experience, x-assets will be an intermediate asset that are “invisible” to most users. Users can directly obtain f-assets through Wrapper as a one-stop asset cross-chain solution, and vice versa.

This is the main bulk of FIP #2.

Adam: How is the voting for FIP#2 going?

Yuan: Looking good! The majority of vote have favored the proposal.

The details of FIP #2 can be found at https://docs.flamingo.finance/governance-proposals/fip-2.

We need five million votes as the minimum threshold to pass the proposal.

You can vote at flamingo.finance/vote.

The vote will end at 8:00 a.m. (UTC) on Feb. 8, 2021.

Please vote!

Adam: A few more days to go! Let’s get it passed! So, according to the proposal, new assets will be introduced. How can we migrate our current assets? Which assets will be affected?

Yuan: There will be two phases.

Phase One: by the end of February, the team will complete the protocol and front-end upgrades of Flamincome and Flamingo, and start the migration of WETH;

Phase Two: Two weeks later. We will complete migration of WBTC and USDT.

For new users, holders of WBTC, USDT and WETH can freely deposit those assets for y-assets in Flamincome for yield, or cross-chain to Neo to generate f-asset, then to participate in Swap liquidity provision for transactions.

The current pn-assets will be gradually replaced by f-assets in stages, so the rewards scheme of FLP staking in Vault will also be gradually replaced. Please pay attention to the migration arrangement.

Holders of pn-assets can directly convert assets into f-assets (one-way) 1:1 in Wrapper.

The holders of n-asset on the Ethereum side, can convert their assets directly back to the original assets.

There will be no impact for nNEO and pONT.

For liquidity providers, you need to migrate to a new trading pair, unstake your liquidity pool, remove the liquidity, convert pn assets to f-assets, add liquidity to new pair, then stake.

Community Q&A

Q1: What is the role of GAS in the Flamingo platform? Will we see GAS as LP pair in the future?

Yuan: We are definitely considering adding GAS/nNEO in the future, but probably after migration. We need to create nGAS to make it work, since GAS is also UTXO.

Q2: Should we unstake FLP-FLM-nNEO?

Yuan: No, that pair will remain the same.

Q3: With Neo3’s NEP-17 tokens, will we still need to wrap NEP-based tokens on Flamingo?

Yuan: For NEO yes, because it is indivisible. For GAS, no.

Q4: What will be needed to add coins for new pools in the Swap? Will new listings need a vote?

Yuan: We will be establishing a channel for FIP community submissions. People will then be able to introduce new pairs and vote on them. When we migrate to Neo3, everyone can add pairs on their own.

Q5: Will it ever be be possible to vote with FLM while it is staked or in a liquidity pool?

Yuan: We will definitely consider this! It is a good suggestion. We will discuss this to see if this is feasible from a technical perspective.

Q6: What do you think makes Flamingo unique to other DeFi projects?

Yuan: First, it is a cluster of protocols rather than one, so it is much more difficult to build up a quite big stack. Second, the Poly Network is really an enabler, I think it is only on-chain cross-chain solution that’s working so far.

Q7: On a scale of one to ten, how keen are the Flamingo devs to see FIP #2 receive approval?

Yuan: Ten.

Q8: What is Da Hongfei’s role within the Flamingo project?

Yuan: Hongfei’s not directly involved in the day to day development and operations, but the Neo Foundation gave us a lot of support and suggestions along the way. Both financially and intellectually.

Q9: Since every transaction will require fees on Neo3, how will that impact the Flamingo economic model and infrastructure?

Yuan: I think the GAS fee will be lower on Neo3. After the smart contract adjustment, GAS fees will be marginal.

Q10: Has the team already begun preparing for Neo3 migration, or is that preparation that will begin when Neo3 TestNet is live?

Yuan: We have reviewed the technical difficulties, many codes can be reused. We are quite confident.

Q11: If FIP #2 passes, are there other blockchain networks that will integrate with Flamingo on the roadmap?

Yuan: Poly Network is expanding very fast now, I think we can support assets from many public blockchains in the future. When Neo3 launches, it would be even more permissionless. I believe the scene will be much more dynamic.

Q12: In the future, will the Flamingo team add loan and borrow option like Aave?

Yuan: Not for now. We don’t want to do everything. We urge people who are interested to apply for grants from Neo Foundation to start their own projects. 

The whole point of Flamingo is not to take it all, but to ignite the scene.

Q13: Will there be a second Perp trading competition? Or, is the team confident in making necessary adjustments from the first competition?

Yuan: At least one or two, we are taking the security of assets quite seriously.

Q14: Is there a point in Flamingo’s future where the community can create their own liquidity pools? For example, a FLP-GUARD-nNEO pool, if the community is able to provide the liquidity on their own?

Yuan: Yes, as I mentioned earlier. For Neo2 stage, we will be establishing a channel to have community FIPs to add new pairs or FLM incentives to certain pairs. For Neo3, it would easier, it would be completely permissionless.

Adam: Thanks for everyone’s enthusiasm! Please feel free to drop questions here as usual, our mods and the team will continue to answer and support.

Yuan: Thanks, everyone, for your time! We should do this more often.

Adam: Thanks everyone for your support all along! Remember to vote, please!

Note: Some edits have been made for formatting and readability.

The post Flamingo Finance product lead discusses asset flow design proposal and roadmap in AMA appeared first on Neo News Today.
