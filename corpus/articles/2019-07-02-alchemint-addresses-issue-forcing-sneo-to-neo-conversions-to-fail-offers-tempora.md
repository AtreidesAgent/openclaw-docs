---
title: "Alchemint addresses issue forcing SNEO to NEO conversions to fail, offers temporary solution"
date: 2019-07-02
url: https://neonewstoday.com/general/alchemint-addresses-issue-forcing-sneo-to-neo-conversions-to-fail-offers-temporary-solution/
tags: [General, SDUSD]
source: neonewstoday
---

# Alchemint addresses issue forcing SNEO to NEO conversions to fail, offers temporary solution

**Published:** Tue, 02 Jul 2019 23:12:47 +0000
**URL:** https://neonewstoday.com/general/alchemint-addresses-issue-forcing-sneo-to-neo-conversions-to-fail-offers-temporary-solution/
**Tags:** General, SDUSD

---

On June 24th, Alchemint acknowledged its users were experiencing delays when attempting to convert SNEO back to NEO on its stablecoin issuance platform. The Alchemint team has cited problems stemming from the transaction fee changes in the neo-cli v2.10.2 update, which took effect at 9:00 am (GMT) on June 3rd, 2019.

Temporary Solution and Next Steps

Speaking with NEO News Today, Stephen Hu, Alchemint community manager, said that users of the stablecoin issuance platform noticed transaction failures when converting SNEO to NEO after the neo-cli node software update. As NEO and GAS assets are UTXO-based and not easily integrated into smart contracts, Alchemint requires users to convert NEO to SNEO (a NEP-5 asset), which can then be collateralized into SDUSD. To liquidate a contract, users need to refund the SDUSD in exchange for SNEO, which can then be withdrawn back into NEO.

After two weeks of troubleshooting, Alchemint admitted it had yet to identify the issue. Should users wish to convert their SNEO into NEO, they will need to contact Alchemint and a member of the team will manually handle the conversion. Instructions for the manual conversion service can be found in the link to the announcement.

Alchemint also noted that its team is coordinating with NEO developers on a solution. Currently, the SNEO smart contract does not allow for GAS fees to be attached to transactions. A mandatory fee of 0.001 GAS + (0.00001 * (transaction size – 1,024)) for all transactions larger than 1,024 bytes was introduced by the neo-cli 2.10.2 update. An inability to attach a transaction fee is likely to be the root cause of transaction delays and cancellations.

Ultimately, Alchemint claims it will implement corresponding NEO3 upgrades to resolve the issue once NEO3 launches on MainNet, as the NEO and GAS assets will no longer use the UTXO model.

The link to the temporary solution announcement can be found below:

https://medium.com/@AlchemintIO/sneo-issue-temporary-solution-163091e006f1?postPublishedType=initial
                                    

The post Alchemint addresses issue forcing SNEO to NEO conversions to fail, offers temporary solution appeared first on Neo News Today.