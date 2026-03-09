---
title: "Aphelion make contribution to NEO core mempool, hint at solution towards compliance"
date: 2018-12-06
url: https://neonewstoday.com/general/aphelion-make-contribution-to-neo-core-mempool-hint-at-solution-towards-compliance/
tags: [General, APH]
source: neonewstoday
---

# Aphelion make contribution to NEO core mempool, hint at solution towards compliance

**Published:** Thu, 06 Dec 2018 22:10:48 +0000
**URL:** https://neonewstoday.com/general/aphelion-make-contribution-to-neo-core-mempool-hint-at-solution-towards-compliance/
**Tags:** General, APH

---

Aphelion has released a weekly update, which covers NEO core code contributions, and hints at a solution for regulatory compliance. Aphelion is a decentralized exchange (DEX) that recently suspended MainNet activities under legal advice following the SEC action against EtherDelta. 

Aphelion CEO Ian Holtz stated “after 2 solid weeks of round the clock analysis, legal calls and diligence, we have landed on a solution to get us compliant and are working on an integration.” Though a concrete timeline was not provided, Holtz said the Aphelion team “are hopeful a fully compliant DEX can be turned back on in a matter of weeks.”

In its downtime, Aphelion has been adjusting its contract code, testing pricing models, and contributing to the NEO core code. Aphelion’s NEO core contribution, GitHub Pull Request #500 offers a solution for issues with the NEO MemoryPool that have lead to congestion.

Initially, when large amounts of transactions were broadcast to the chain, overhead in the current design would cause delays. This even included new transactions with higher tx fees. This large mempool would lead to many transactions that might require re-verification on the block.

The proposal suggests re-verifying only as many transactions necessary to begin a pool with the max amount of transactions a block can accept. To facilitate this process, PR #500 sorts and prioritizes transactions ordered by “fee per byte, then fee, then TX hash.” The fix will attempt to re-verify transactions that are only at the header height. 

The full report can be found at the link below:

https://medium.com/@ianholtz/aphelion-weekly-updates-december-5th-2018-path-forward-making-neo-stronger-c92294e81f27 
                                    

The post Aphelion make contribution to NEO core mempool, hint at solution towards compliance appeared first on Neo News Today.