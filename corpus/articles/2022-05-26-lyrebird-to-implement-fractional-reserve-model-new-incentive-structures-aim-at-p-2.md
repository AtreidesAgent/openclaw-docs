---
title: "Lyrebird to implement fractional reserve model, new incentive structures aim at protocol resiliency"
date: 2022-05-26
url: https://neonewstoday.com/defi/lyrebird-to-implement-fractional-reserve-model-new-incentive-structures-aim-at-protocol-resiliency/
tags: [DeFi, General, LRB, USDL]
source: neonewstoday
---

# Lyrebird to implement fractional reserve model, new incentive structures aim at protocol resiliency

**Published:** Thu, 26 May 2022 20:13:57 +0000
**URL:** https://neonewstoday.com/defi/lyrebird-to-implement-fractional-reserve-model-new-incentive-structures-aim-at-protocol-resiliency/
**Tags:** DeFi, General, LRB, USDL

---

Lyrebird proposes a fractional reserve method for the USDL stablecoin and new incentive structures to combat an algorithmic protocol collapse. By implementing two forms of collateral, Lyrebird aims to give the protocol a better chance to recover if its stablecoin loses the peg to the US dollar.

Lyrebird launched in April 2022 as an algorithmic stablecoin protocol utilizing a dollar-pegged token, USDL, and stabilization utility (aka reserve) token, LRB. The protocol was designed to peg its stablecoin to the US dollar via bots and arbitrageurs monitoring supply and demand between LRB and USDL and taking advantage of asset price discrepancies.

In May 2022, a protocol Lyrebird was modeled after, Terra, suffered a “death spiral” in the face of rapidly decreasing demand for its UST stablecoin and LUNA reserve token. The vicious cycle started when UST began to trade for less than US $1 and could not regain its peg. When UST was sold, it was burnt on the Terra blockchain, and more LUNA was minted to act as collateral for the remaining UST supply. However, the price of LUNA rapidly depreciated as the market sold in large swaths. Amidst quickly falling prices, LUNA could no longer act as a viable form of collateral for the remaining UST stablecoin supply, and the assets trended downward in unison.

The Lyrebird development team believes it can utilize a fractional reserve model and incentivize token holders to delay USDL redemptions in times of extreme stress to avoid a similar fate.

Protocol Reserves

Stablecoins have been in the blockchain space since 2014 and could only be collateralized with fiat reserves, over-collateralized by cryptocurrency, or pegged to a price by algorithms. Until the launch of the Frax Protocol in Dec. 2020, stablecoin projects fell into one of these three categories.

FRAX is a fractional reserve stablecoin that manages a collateral ratio of a fiat-backed stablecoin (i.e., USDC, USDT) and a reserve token (i.e., FXS). For example, a collateral ratio of 0.5 would mean the stablecoin is backed by 50% USDC and 50% FXS. If FRAX is redeemed at a collateral ratio of 0.75, the user receives 75% USDC and 25% FXS.

In theory, the higher the collateral ratio favoring the fiat-backed stablecoin, the lower the probability of a death spiral as the reserve token can more readily absorb a decrease in FRAX supply.

Modeling itself after the Frax protocol, Lyrebird intends to back the USDL stablecoin with collateral consisting of fUSDT and LRB. The team believes that algorithmic stablecoins offer the highest capital efficiency and seeks to innovate in this particular aspect of stablecoins.

The Stablecoin Trilemma

On the Smart Economy Podcast, Lyrebird founder William Song introduced considerations of different stablecoin structures and how they’re interconnected. There are various interpretations of the “Stablecoin Trilemma,” but consensus generally posits that a stablecoin can prioritize two out of three key areas. They include decentralization, peg stability, and capital efficiency.

Decentralization refers to the level of control an entity has over the collateral backing its stablecoin. For example, USDC and USDT are the most centralized, as registered and regulated entities manage those treasuries. However, DAI leans more decentralized as the treasury and direction of the ecosystem are governed by the MakerDAO.

Peg stability requires stablecoins to maintain a tight correlation with a particular asset. Projects like USDC and USDT have exhibited a long track record of keeping the price near the US dollar. Over DAI’s lifecycle, the stablecoin has gradually improved its ability to maintain the $1 peg. On the other hand, purely algorithmic projects like UST and IRON have failed to maintain the peg.

Capital efficiency represents the ability to create a stablecoin and use it for other purposes within an ecosystem (i.e., lending and borrowing). If more collateral needs to be locked up to mint a stablecoin, like with DAI, it loses the ability to effectively deploy the capital that is backing the stablecoin. Centralized stablecoins like USDT and USDC have a capital efficiency of 1:1 as a dollar backs every floating stablecoin. However, algorithmic stablecoins have the highest efficiency as less collateral is necessary, reducing constraints to create a stablecoin and deploy it elsewhere.

Lyrebird’s forthcoming fractional reserve solution will prioritize capital efficiency but reduce its levels of decentralization and acknowledges potential of peg instability. Centralization will increase through a Lyrebird-managed treasury of fUSDT, and a new incentive strategy will accept that the peg can be lost and regained through dynamic collateral redemption ratios.

Accept The Peg Can Break

Along with a new fractional reserve for collateral, Lyrebird will lean into the potential that USDL can lose its peg to the US dollar. However, the team also seeks to incentivize holding the USDL stablecoin through downward market turbulence. The development team believes that if a portion of the collateral is held in a fiat-backed stablecoin (i.e., fUSDT), it can be used as a last resort to defend the peg in significant deviations.

In the case of Terra, collateral reserves were held in Bitcoin and depleted upfront to maintain UST’s peg to $1. However, the reserve was quickly exhausted, and there was no defense against algorithmic instability.

In previous algorithmic death spirals, the incentive structure led holders to sell the stablecoin as confidence in the protocol began to wane. If they acted later, they would have to sell the stablecoin at a much lower price as it fell further from the peg. Lyrebird seeks to flip the incentive model and use the fiat-backed stablecoin collateral as the final redemption method.

USDL will first be redeemable with the LRB reserve token in case of a major sell-off event. Once the LRB backing the USDL token has been used for redemptions, then future redemptions will be distributed in the fiat-backed fUSDT. This is designed to incentivize users to hold on to USDL longer because it will eventually be redeemable at a 1 USDL:1 fUSDT ratio.

Initially, Lyrebird will implement a 0.5 collateral ratio, but the community can later vote to change it through governance processes. With the fractional reserve method, USDL may lose its peg from the US dollar more quickly by design, but is potentially more resilient in the face of major downward market swings.

Moving Forward

The Lyrebird team has slowed the growth of the protocol by burning a majority of the initial mint of the USDL supply while it implements a fractional reserve. Lyrebird has burnt 9.95 million of the initial 10 million USDL supply minted for reserves. The initial 50,000 USDL used to seed Flamingo’s FRP-FLM-USDL will remain in the reverse liquidity pool. The current supply of approximately 226,000 USDL indicates a user base that continues to remain active.

The development team will focus on implementing a mechanism to purchase portions of fUSDT whenever USDL is minted. The team also aims to build a redemption mechanism that swaps USDL for fUSDT when the USDL supply is equal to or greater than the fUSDT reserves.

Lyrebird anticipates a tentative Summer 2022 launch for the fractional reserve protocol.

The full announcement can be found at the link below:

https://lyrebird-finance.medium.com/fractional-reserves-defending-against-death-spirals-28080a7f777b

 

The post Lyrebird to implement fractional reserve model, new incentive structures aim at protocol resiliency appeared first on Neo News Today.
