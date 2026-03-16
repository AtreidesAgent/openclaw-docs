---
title: "Switcheo delivers post mortem on TradeHub chain halt"
date: 2021-02-09
url: https://neonewstoday.com/general/switcheo-delivers-post-mortem-on-tradehub-chain-halt/
tags: [DeFi, General, SWTH]
source: neonewstoday
---

# Switcheo delivers post mortem on TradeHub chain halt

**Published:** Tue, 09 Feb 2021 13:19:44 +0000
**URL:** https://neonewstoday.com/general/switcheo-delivers-post-mortem-on-tradehub-chain-halt/
**Tags:** DeFi, General, SWTH

---

Switcheo TradeHub experienced a chain halt on Feb. 7, which it was able to address while ensuring any funds or assets on the chain remained safe. The chain went down at 10:30 a.m. (UTC) on Sunday, and its liveliness was restored a few hours later at 3:00 p.m.

The Switcheo TradeHub chain was designed to shut down when there is a disparity between modules in its system infrastructure. Switcheo noted, “the TradeHub code was designed to prefer safety over liveliness.” In the post mortem, Switcheo Labs identified the issue:

The root cause of the incident was that an incorrect rounding direction was used when rounding decimals to integers in the new implementation that was introduced in the v1.12 upgrade.

Switcheo TradeHub is structured as multiple independent modules, and this incorrect rounding violated a safety invariant in another module — the output amount expected by the automated market maker module was slightly more than the output allowed by the liquidity pool module, triggering an internal consistency safeguard and halting the chain. 

The code was not caught in pre-testing because the parameters did not include the set of values that would trigger the fault. Switcheo has updated its unit testing and fuzz test input values to catch similar issues in future updates.

A hotfix was included in an emergency upgrade to TradeHub v1.12.1. Looking forward, Switcheo Labs plans to permanently address the underlying issue in an upcoming upgrade to v1.13.1.

The full announcement can be found at the link below:

https://medium.com/switcheo/switcheo-tradehub-incident-report-7th-feb-2021-f609e3832f57 

The post Switcheo delivers post mortem on TradeHub chain halt appeared first on Neo News Today.
