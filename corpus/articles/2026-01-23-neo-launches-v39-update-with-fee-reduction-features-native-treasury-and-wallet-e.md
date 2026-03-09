---
title: "Neo launches v3.9 update with fee reduction features, native treasury, and wallet enhancements"
date: 2026-01-23
url: https://neonewstoday.com/development/neo-launches-v3-9-update-with-fee-reduction-features-native-treasury-and-wallet-enhancements/
tags: [Development, Neo4]
source: neonewstoday
---

# Neo launches v3.9 update with fee reduction features, native treasury, and wallet enhancements

**Published:** Fri, 23 Jan 2026 02:30:54 +0000
**URL:** https://neonewstoday.com/development/neo-launches-v3-9-update-with-fee-reduction-features-native-treasury-and-wallet-enhancements/
**Tags:** Development, Neo4

---

The Neo core development team has released Neo‑CLI v3.9.0, marking the first official release since May 2025 and the first since the return of Neo co-founder, Erik Zhang. Announced on Jan. 19, the update was scheduled for deployment to the T5 TestNet on Jan. 21, with MainNet activation slated for Feb. 3. This version introduces a wide range of enhancements spanning the protocol, native contracts, and developer tooling, and will require a hard fork. Critical hotfixes were released as v3.9.2 on Jan. 21, with all node operators needing upgrade to v3.9.2 or later before the Feb. 3 MainNet fork.

Key upgrades in Neo‑CLI v3.9.0

The v3.9.0 update consolidates progress over the past several months and includes features backported from the Neo 4 codebase. These additions remain fully compatible with Neo N3, allowing the current ecosystem to benefit from forward-compatible improvements without sacrificing stability. Key features include:

Protocol & native contract enhancements

Contract fee whitelist: The new fee whitelist mechanism enables specified contract methods to execute without GAS fees, reducing costs for users and supporting zero-cost interactions for infrastructure-style contracts. Selected contracts can be whitelisted by committee governance, promoting adoption of stablecoins and reducing barriers for payment and settlement use cases.

Treasury native contract: A new Treasury native contract is introduced to enhance on-chain governance for managing funds and distributing network incentives. The contract implements NEP-26 (Payment Callback) and NEP-27 (Transfer Callback) standards, includes committee verification logic, and is designed to improve network sustainability and simplify protocol-level fund workflows.

Execution fee factor precision: The execution fee factor now supports greater decimal precision, allowing for more granular control over network fee economics and enabling finer adjustments to transaction costs. The feature will allow for significant reductions of GAS fees.

Policy contract enhancement: The Policy Contract now includes a GetBlockedAccounts method, providing a standardized way to query the list of blocked accounts on the network. This improves transparency and tooling capabilities for monitoring network governance.

Smart contract development improvements

Isolated contract storage (Storage.Local API): Developers can now use isolated, contract-specific storage through the new Storage.Local API. This gives smart contracts access to local storage that is visible only to the invoking contract, minimizing key-space conflicts, improving smart contract maintainability, and enabling safer and more modular data management within dApps.

Hex encode/decode utilities: Native hexadecimal encoding and decoding functions have been added to the standard library (StdLib), reducing boilerplate code and potential implementation errors in smart contracts.

Wallet & security enhancements

Hierarchical deterministic wallets & mnemonics: Neo‑CLI adds support for BIP32 hierarchical deterministic wallets and BIP39 mnemonic phrases, aligning Neo wallet security with industry standards and elevating the user experience for key management. The new infrastructure is aimed at enhancing security, recoverability, and tool interoperability across the ecosystem.

SignClient Vsock support: Added support for AWS Nitro Enclave integration through Vsock protocol, enabling secure key management and signing operations in trusted execution environments. This enhancement is particularly valuable for institutional and enterprise deployments requiring hardware-backed security guarantees.

Infrastructure & tooling

RESTful API server plugin: Neo‑CLI v3.9.0 ships with a new RESTful API server plugin. This optional module exposes HTTP endpoints for accessing blockchain data, invoking contracts, and querying tokens. The plugin significantly improves integration options for tooling, external services, and web applications, providing a more accessible alternative to RPC interfaces.

Plugin loading improvements: Enhanced plugin loading mechanism now loads plugins from the current application domain, improving plugin isolation and compatibility across different deployment scenarios.

Developer experience

Deployment toolkit (neo-devpack-dotnet): While not part of the core node software, the corresponding neo-devpack-dotnet update includes a production-ready deployment toolkit with deterministic RPC handling, confirmation policies, and state snapshotting for manifest-driven deployments. This significantly streamlines the contract deployment workflow.

Template compilation fixes: Smart contract template compilation issues in Release mode have been resolved, ensuring consistent builds across Debug and Release configurations.

Ordered release workflow: The devpack now includes dependency-aware release processes to prevent “dependency not found” errors, improving the reliability of package releases for the developer ecosystem.

Bug fixes & stability

Several critical bug fixes are included in this release:

- Fixed native contract name handling in GetStorage and FindStorage operations

- Corrected NullReferenceException in getnep17transfers RPC method

- Fixed plugin download URLs for improved plugin management

- WhiteList implementation fixes

Compatibility

To maintain compatibility with the updated protocol, all node operators must upgrade to Neo‑CLI v3.9.0 before the MainNet hard fork at block height 8,800,000. The corresponding TestNet fork will occur at block height 12,960,000. Nodes upgraded prior to the fork will not require a full resync, while those that delay may face extended downtime.

Operators are advised not to reuse existing config.json files and to install the latest compatible plugin versions, including the new RESTful API server plugin. All plugins should be downloaded using the updated plugin management system to ensure compatibility with v3.9.0.

Breaking changes

This release includes breaking changes that necessitate the hard fork:

- Contract fee whitelist implementation

- Treasury native contract addition

- Execution fee factor decimal precision changes

- Storage isolation mechanisms

Developers with deployed contracts should review the changes to ensure compatibility, particularly those implementing custom fee logic or storage access patterns.

Post-release updates

Shortly after the initial v3.9.0 announcement, the Neo development team released critical hotfixes v3.9.1 and v3.9.2 on Jan. 21. These patches addressed three critical bugs discovered during pre-fork testing: improper execution fee factor conversion during hard fork activation, blocked account timestamp persistence issues affecting fund recovery, and whitelist fee reduction not applying to non-native contracts. The bugs were identified through collaborative testing with the Neo SPCC team during NeoGo implementation. Node operators must upgrade to Neo-CLI v3.9.2 before the MainNet fork to ensure proper functionality of the new features.

The original announcement can be found at the link below:

https://x.com/Neo_Blockchain/status/2013918138480660696?s=20

The post Neo launches v3.9 update with fee reduction features, native treasury, and wallet enhancements appeared first on Neo News Today.