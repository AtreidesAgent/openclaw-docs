---
title: "NeoResearch highlights dBFT 2.0 stability over the three months following update"
date: 2019-09-02
url: https://neonewstoday.com/general/neoresearch-highlights-dbft-2-0-stability-over-the-three-months-following-update/
tags: [General, NeoResearch]
source: neonewstoday
---

# NeoResearch highlights dBFT 2.0 stability over the three months following update

**Published:** Mon, 02 Sep 2019 15:16:28 +0000
**URL:** https://neonewstoday.com/general/neoresearch-highlights-dbft-2-0-stability-over-the-three-months-following-update/
**Tags:** General, NeoResearch

---

On August 29th, NeoResearch co-founder, Vitor Coelho, posted an article highlighting the stability of the NEO blockchain in recent months since delegated Byzantine Fault Tolerance (dBFT) v2.0 was uploaded to MainNet around June 3rd, 2019. In the three months since the update, the NEO blockchain has not “sporked” as it had done so with the prior dBFT v1.

The term “spork” was originally coined by Joe Stewart (also known as Hal0x2328) who recently conducted an interview with NEO News Today. In a conventional blockchain fork, two blocks with the same block height (each pointing at the same previous block) exist, creating two independent blockchains with a shared history.

In NEO’s case, it was possible for a consensus node to gain enough signatures to create a valid block, but fail to broadcast it to the others. This node would then become stuck on its own single forked block, dubbed a “spork,” while the remaining nodes continued reaching consensus on their own.

In the upgrade to dBFT v2, a commit phase was added to the consensus protocol, which adds safeguards to ensure that consensus nodes are in agreement before the block can be propagated, preventing all forks and ensuring the finality of transactions on NEO.

Additionally, the research team sought input from experienced cryptography researchers and C# developers who were able to design unique recovery mechanisms and basic fault detection procedures.

NeoResearch has also begun work on building a mathematical programming model to prove the correctness of dBFT in various consensus states. Additionally, the team is building libbft “to allow easy implementation of BFT protocols in C++ and [other] languages.”

Such an example of a new dBFT implementation can be found in neopt, a lightweight version of NEO written in C++.

The full article can be found at the link below:

https://medium.com/neo-smart-economy/dbft-2-0-3-months-no-sporks-e2ab9fe1065b
                                    

The post NeoResearch highlights dBFT 2.0 stability over the three months following update appeared first on Neo News Today.
