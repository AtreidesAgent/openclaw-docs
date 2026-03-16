---
title: "Aphelion processes user withdrawals, contributes to NEO codebase and releases mobile DEX demo"
date: 2018-12-01
url: https://neonewstoday.com/general/aphelion-processes-user-withdrawals-contributes-to-neo-codebase-and-releases-mobile-dex-demo/
tags: [General, APH, GAS]
source: neonewstoday
---

# Aphelion processes user withdrawals, contributes to NEO codebase and releases mobile DEX demo

**Published:** Sat, 01 Dec 2018 00:51:39 +0000
**URL:** https://neonewstoday.com/general/aphelion-processes-user-withdrawals-contributes-to-neo-codebase-and-releases-mobile-dex-demo/
**Tags:** General, APH, GAS

---

On November 28th, Aphelion released an update noting what had occurred in the following week after taking its decentralized exchange (DEX) off MainNet. The DEX was taken offline on the advice of Aphelion’s legal counsel following the recent action taken against EtherDelta by the SEC. NEO News Today provided coverage on the story.

Throughout the week, Aphelion’s web, desktop, iOS, and Windows wallets have remained operational. The TestNet DEX also remained in operation for both the desktop application, and the mobile application released last week.

Any user-induced order cancellations or withdrawal requests have been processed by the Aphelion team. In addition to cancellations and withdrawals, Aphelion has distributed a GAS equivalent of the fractions of NEO “forever stuck on the contract because they are non-divisible.” 

Until the path to compliance has been identified and the DEX re-launched onto MainNet, Aphelion have scaled back costs to remain solvent. Potential paths to compliance include obtaining a broker-dealer license, or integrating Aphelion’s technology into other DEX’s that are compliant, among other options. 

The full update can be found at the link below:

https://medium.com/@ianholtz/aphelion-weekly-updates-november-28th-2018-933bf146686f

Aphelion Mobile DEX Demo

On November 29th, Aphelion released a demo of their mobile DEX, which launched earlier in the week.

The DEX is immediately available to all mobile wallets and can be accessed by toggling to TestNet in the wallet settings; no additional downloads or updates are necessary. Once the TestNet has been toggled, the “Trade DEX” option will become available in the menu navigation on the left navigation menu.

Aphelion stated the mobile DEX will go live on MainNet at the same time its desktop DEX application is back online.

The demo of the mobile DEX can be found at the link below:

https://medium.com/@ianholtz/aphelion-mobile-dex-demo-8f531477f49a

Contributions to NEO GitHub

Aphelion developers have contributed to Pull Request #485 and Pull Request #489.

Pull Request #485 fixed a delay on nodes that would force them to be a block behind the chain. By allowing three concurrent tasks (instead of one) to get block data, the task timeout does not need to expire for the task to get picked up again.

Pull Request #489 fixed nodes that would become occasionally become stuck and prevented from syncing. After auditing the TaskManager and Blockchain.cs, the Aphelion team identified the scenario that causes the issue and provided a fix.

Both these changes are hoped to increase performance for NEO. The Aphelion report documenting these fixes can be found here.
                                    

The post Aphelion processes user withdrawals, contributes to NEO codebase and releases mobile DEX demo appeared first on Neo News Today.
