---
title: "Flamingo launches FUSD on TestNet, to begin beta testing margin maintenance bot soon"
date: 2022-12-23
url: https://neonewstoday.com/defi/flamingo-launches-fusd-on-testnet-to-begin-beta-testing-margin-maintenance-bot-soon/
tags: [DeFi, General, bNEO, FLUND, FUSD, fWBTC]
source: neonewstoday
---

# Flamingo launches FUSD on TestNet, to begin beta testing margin maintenance bot soon

**Published:** Fri, 23 Dec 2022 22:39:07 +0000
**URL:** https://neonewstoday.com/defi/flamingo-launches-fusd-on-testnet-to-begin-beta-testing-margin-maintenance-bot-soon/
**Tags:** DeFi, General, bNEO, FLUND, FUSD, fWBTC

---

Flamingo Finance has launched the FUSD stablecoin on Neo N3 TestNet ahead of its tentative MainNet launch in early 2023. The FUSD stablecoin will be modeled after MakerDAO’s DAI token, which uses over-collateralization of digital assets to ensure its peg is held to US $1. In parallel, the team is also working on a margin maintenance bot to help an FUSD loan maintain its collateral value before liquidating the Vault.

Stablecoins are designed to maintain a consistent price, typically $1, and can enable users to generate yield on a digital asset while potentially alleviating adverse effects from market volatility. At the time of press, the Neo blockchain only supports one stablecoin – a wrapped version of the Tether stablecoin, fUSDT, which is backed 1:1 by the US Dollar. Instead of a fiat-backed stablecoin, digital assets will overcollateralize FUSD, the first native stablecoin on Neo N3.

Source: Flamingo Finance

To mint FUSD, a user must open a Vault with FLUND, bNEO, or fWBTC. Users can mint FUSD up to a loan-to-value of 35% of the collateral tokens’ value (i.e., an equivalent of $1,000 of FLUND can mint up to $350 of FUSD). If the market value of the underlying assets increases, the LTV will decrease (and vice versa). At any point, Vault owners can withdraw any underlying collateral provided the LTV doesn’t exceed 35%. Users who want to withdraw the initial underlying collateral will need to repay all the outstanding minted FUSD and the interest it has accrued.

Each “loan” can only be backed by one type of underlying digital asset. If a user wants to mint FUSD using different tokens, then a separate loan will need to be created for each asset. This also means that existing loans backed by different underlying assets can’t be merged together.

Source: Flamingo Finance

Much like a loan in traditional finance, once the user has minted FUSD, they will pay a fixed annual interest rate. When the user exits their initial FUSD position, they’ll have to redeem the value of the initial mint and pay the additional interest to reclaim ownership of the underlying collateral tokens.

For example, if a user mints 100 FUSD using FLUND tokens as collateral, after a year, the wallet will have 100 FUSD plus an additional 6 FUSD in interest to pay back in order to access the FLUND initially provided for collateral. If the user doesn’t redeem after a year, they are then incurring interest at 6% on 106 FUSD.

The initial interest rates will be 4% for bNEO, and 6% for FLUND and fWBTC.

Users can request TestNet fWBTC, bNEO, and GAS assets from the #testnet-funds channel in the official Flamingo Finance Discord server to test the front-end. The testing phase will run until the MainNet launch of FUSD in early 2023, and users are encouraged to provide feedback and report any bugs to the Flamingo team.

Margin Maintenance Bot

Alongside minting FUSD with bNEO, FLUND, or fWBTC collateral, users can also utilize a bot to perform margin maintenance on active Vaults. If the LTV of a Vault exceeds 40% due to market movements of the underlying asset, then other users can transfer FUSD to that Vault and repay some of the loan. A maintainer can pay up to 50% of the outstanding FUSD on a Vault’s loan, and earn a 5% bonus on the underlying asset they’ve purchased.

Using the previous figures, for example, assume User A mints 350 FUSD initially backed by $1,000 equivalent of FLUND. Then let’s say the value of the FLUND collateral decreases by 50%, so the initial 350 FUSD is now backed by just $500 of FLUND. In this case, the LTV is now 70%. User B can act as a margin maintainer and send 175 FUSD to User A’s Vault to partially repay the loan, and receive $175 equivalent of FLUND and a 5% bonus, totaling $183.75 equivalent of FLUND.

As a rebalancing tactic, the margin maintainer pays down the loan in FUSD, essentially purchasing the underlying collateral from the Vault at depressed prices. This reduces the amount of collateral backing the loan while simultaneously providing the Vault with FUSD to bring it closer to parity with the 35% LTV benchmark.

When User A’s Vault incurs margin maintenance, they will pay an 8% penalty fee. For example, when User B sends 175 FUSD to User A’s Vault, 92% (161 FUSD) will be deducted from the Vault and look like a repayment to lower the LTV. The Flamingo Lend module will keep the remaining 8% (14 FUSD), of which 33.33% will be distributed to FLUND, the Security Fund, and the LRB Fund.

Following the pivot of the Lyrebird project, post-Terra collapse, the LRB Fund is designed to ensure that LRB and USDL token holders will benefit from the adoption of FUSD. The LRB Fund will accrue interest on fees from minting and burning FUSD, as well as FUSD liquidations. LRB token holders can claim access to the LRB Fund determined by the amount of their LRB holdings. After the first two years, the LRB Fund will no longer receive any of the fees, and its 33.33% portion of the Vault liquidation penalty fees will be directed toward FLUND.

Looking forward, the team intends to publish the code for the margin maintenance bot, which users will also be able to test.

The announcement can be found at the link below:

https://twitter.com/FlamingoFinance/status/1605208567782465537?s=20&t=-G48VVHeYTVj4K1PUJsoQg

The post Flamingo launches FUSD on TestNet, to begin beta testing margin maintenance bot soon appeared first on Neo News Today.