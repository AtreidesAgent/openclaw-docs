---
title: "MEV-resistance features integrated into Neo X TestNet"
date: 2025-03-20
url: https://neonewstoday.com/development/mev-resistance-features-integrated-into-neo-x-testnet/
tags: [Development, General, GAS, NEO, NeoX]
source: neonewstoday
---

# MEV-resistance features integrated into Neo X TestNet

**Published:** Thu, 20 Mar 2025 14:59:00 +0000
**URL:** https://neonewstoday.com/development/mev-resistance-features-integrated-into-neo-x-testnet/
**Tags:** Development, General, GAS, NEO, NeoX

---

Anti-MEV functionality has launched on the Neo X EVM sidechain TestNet. Activated at block height 2,088,000, the upgrade introduces enveloped transactions and threshold signature support to enhance transaction fairness and network security.

MEV strategies – where miners, validators, or bots reorder, insert, or censor transactions to extract profit – are responsible for billions of dollars in user losses annually. These practices disproportionately affect retail users and undermine the integrity of DeFi products built on blockchains. Neo X is being developed in part to mitigate these exploits through an approach designed to prevent transaction-level manipulation by its network validators.

Enveloped transactions: A three-step MEV defense

The Neo X approach centers on “enveloped transactions,” a technique designed to obscure transaction details until after block finalization. The mechanism follows a three-step process:

- Encryption: Transactions are encrypted, or “enveloped,” before reaching consensus nodes. This prevents validators and MEV searchers from identifying transactions that could yield extractable value.

- Uniform Processing: Consensus nodes treat all enveloped transactions identically and package them alongside ordinary, unencrypted transactions.

- Threshold Decryption: Once the transaction order is finalized, the network performs threshold decryption. This step requires two-thirds of the consensus nodes to collaborate in decrypting transactions and finalizing the block.

The three-step process is made possible by “distributed key generation,” a cryptographic technique implemented by the Neo X development team.

Achieving single-block finality

Previously, Neo X required a one-block delay for block hash finality due to potential reorganization issues. A reorganization, or “reorg,” occurs when a node discovers a new, longer chain and switches to this chain from the previous longest chain, effectively changing the network’s historical record. This one-block delay impacted services dependent on immediate finality, such as XSig’s multi-signature wallet.

With the integration of threshold block signatures, the network now achieves single-block hash finality. This improvement reduces the potential for reorgs and enhances the sidechain’s usability and security.

Developers interested in experimenting with the MEV-resistant EVM environment can explore available documentation or join the official Neo Discord server for further engagement.

The full announcement can be found at the link below:

https://medium.com/neo-smart-economy/anti-mev-feature-now-live-on-neo-x-testnet-6f3cf667e794

The post MEV-resistance features integrated into Neo X TestNet appeared first on Neo News Today.