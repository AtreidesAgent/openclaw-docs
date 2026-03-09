---
title: "Neo News: Week in Review – February 9 – February 15"
date: 2026-02-16
url: https://neonewstoday.com/week-in-review/neo-news-week-in-review-february-9-february-15/
tags: [Week In Review, AxLabs, FRANK, ndapp, NeoSPCC, R3E]
source: neonewstoday
---

# Neo News: Week in Review – February 9 – February 15

**Published:** Mon, 16 Feb 2026 16:25:36 +0000
**URL:** https://neonewstoday.com/week-in-review/neo-news-week-in-review-february-9-february-15/
**Tags:** Week In Review, AxLabs, FRANK, ndapp, NeoSPCC, R3E

---

General Updates

Neo co-founder Da Hongfei announced that Neo is “upgrading” its upcoming Financial Report to align with a broader transparency framework, expanding the publication beyond financial data to include asset allocation and custody structures, treasury positioning, and token activities, along with a subsequent governance restructuring plan. He noted that the initial timeline was to release the report in Q1, with a preview before Feb. 15, but it has been extended due to the expanded scope. Honfgei added that Neo is engaging an international audit firm to conduct an asset possession review, framing the effort as a step toward higher transparency and long-term accountability.

Hongfei attended Consensus Hong Kong and shared a business development update on cross-chain integration discussions involving both Neo N3 and Neo X, saying the team recently met with a major protocol operator. He said the operator’s integration fees for Neo N3 are currently fourteen times higher than for Neo X, attributing the gap to current on-chain volume and economies of scale rather than an issue with NeoVM. Hongfei added that the integration plan remains under discussion and that Neo will continue evaluating viable economic paths for Neo N3.

Additionally, Hongfei commented on Tether’s continued work with LayerZero around cross-chain USDT0, emphasizing that unified stablecoin liquidity is important infrastructure for developers and users. He added that Neo intends to support USDT0 within its ecosystem, framing it as part of the network’s efforts to expand cross-chain functionality and stablecoin access.

SpoonOS extended the skills micro-challenge for an undisclosed period. The micro-challenge invites developers to submit “Agent Skills” via pull request to its designated repository. The challenge follows SpoonOS’ recent rollout of its Web3-native Skills marketplace, and is designed to seed that marketplace with more production-ready, reusable components while giving the team a structured way to identify high-quality builders and projects through real contributions. SpoonOS also hosted a Space titled, “Working with AI Agents: Skills, Collaboration, and Real Workflows.”

nDapp released a weekly N3 GAS check-in, noting that network users claimed approximately 56,281 GAS over the past week and that on-chain activity burned about 454 GAS.

NNT hosted a GasBot Trivia round, with participants competing for a pool of 4 GAS rewards.

Frank Coin hosted a GasBot trivia contest on the FrankCoin channel of the NeoF1 Discord server, rewarding participants with 3 GAS.

Developer Updates

Neo released NeoGUI v1.7, which updated the desktop client to be compatible with Neo v3.9.1 and upgraded its target framework from .NET 9.0 to .NET 10.0. The release also updates plugin download URLs to point to the neo-node repository and includes fixes for UI display behavior, unit tests, and API compatibility changes introduced in Neo v3.9.1.

R3E Network released a series of updates across its Neo developer tooling and SDKs, spanning compiler infrastructure, language SDK alignment, bytecode analysis improvements, security and performance fixes, and RPC compatibility improvements for Rust-based node infrastructure:

- NeoSwift v2.2 is a security and stability update that fixes empty catch blocks that could silently swallow errors and addresses several force-unwrapping and nil-handling issues across the SDK. The release also improves wallet balance fetching performance by parallelizing requests with TaskGroup, and updates Neo N3 compatibility to v3.9.1. No breaking changes were introduced, and the maintainers note that no migration steps are required for existing users.

- neo-rs v0.7.2 updates the Rust implementation of the Neo N3 blockchain node and CLI tools with RPC compatibility improvements that address issues affecting nodes during initial synchronization. The release fixes a cold-start issue where the getnativecontracts method would fail before persisted native contract state was present in local storage, and now returns active native contracts by falling back to registry-derived contract states when store-backed entries are unavailable. The release includes no breaking changes, and users are advised to rebuild and restart node binaries after upgrading.

- Neo Decompiler v0.5.2 updates the Rust-based tooling to be fully compatible with Neo v3.9.2. The release highlights new SSA transformation support, including φ (phi) nodes and variable versioning to improve analysis of Neo N3 bytecode.

- neo-llvm v0.4.7 updates the compiler toolchain to align with Neo v3.9.2. The release adds support for the System.Runtime.GetNotifications syscall and includes fixes to notification handling that improve compatibility with the latest protocol and tooling expectations.

- neo-zig-sdk v1.3.0 brings the Zig SDK in line with Neo N3 v3.9.0 (Faun hardfork) and adds full wrappers for three new native contracts: CryptoLib, Notary, and Treasury. The update also includes several protocol-compliance fixes to match the neo-project/neo C# reference implementation, such as correcting hardfork enum naming and aligning native contract method signatures. The release also introduces a NamedCurveHash enum for type-safe ECDSA curve and hash pairs.

Neo SPCC released a series of updates across its NeoFS gateway and management tooling, adding new session token support, expanding EACL functionality, and introducing configuration, dependency, and storage-handling changes alongside multiple fixes.

- NeoFS REST Gateway v0.16 introduces session token v2 support via a new auth/token model and adds gateway metadata. The update expands EACL functionality with support for numeric filters and account-based targets, while also fixing an issue that could push excessive CORS headers to users on OPTIONSrequests. The release removes support for session token v1 in container operations and requires applications to migrate immediately when upgrading from v0.15.1, with NeoFS SDK updated to RC17.

- NeoFS Panel v0.8 adds a configuration option to disable user self-registration and improves storage transparency by showing file sizes and other UI refinements. The update also refreshes its NeoFS dependencies to v0.42.0, aligning the panel with recent gateway changes. This release includes miscellaneous fixes and dependency updates across the project. Additionally, Neo SPCC released v0.8.1, which includes several bug fixes and uses a new NeoFS chain endpoint.

- NeoFS S3 Gateway v0.42.0 changes how bucket configuration data is stored by moving bucket settings (including notifications), CORS, and tags from objects into container attributes. The update also fixes an issue that could cause excessive node disconnects, and bumps dependencies to NeoFS SDK RC17 and neofs-contract v0.26.0.

AxLabs released neow3j v3.24.1, bringing the Java toolkit to full compatibility with the Neo N3 v3.9 protocol update and introducing new protocol-aligned SDK and devpack features with no breaking changes. The update adds multiple  PolicyContract methods (including  getBlockedAccounts and  recoverFund), expands devpack interops, and introduces additional native contract and Neo standard enum entries. The team also issued a deprecation notice for the devpack’s  StorageContext, which is planned for removal in v3.25.0.

In Case You Missed It

Neo SPCC published a coordinated wave of NeoFS releases, led by NeoFS Node v0.51.0, which delivers protocol-level changes including mutable NEP-11 containers, synchronous container operations, and the introduction of session token v2. The accompanying NeoFS SDK Go v1.0.0-rc.17 provides the underlying library support for these features, while XK6-NeoFS v0.2.1 brings stability fixes and dependency upgrades to the load testing extension. A TestNet upgrade has already been completed, with MainNet expected to follow in the coming days.

R3E Network revealed the Neo Solidity Compiler, a tool that compiles Solidity 0.8.x smart contracts to Neo N3 bytecode. The project allows developers to write contracts in Solidity and deploy them to the Neo N3 blockchain. The repository includes several example contracts that demonstrate the compiler’s functionality. WGAS is a wrapped GAS token implementation that follows the WETH9 pattern and complies with NEP-17. FlashLoan implements an Aave V2-style flash loan pool with 0.09% fees. SimpleAMM is a constant-product automated market maker based on Uniswap V2’s design. The project documentation indicates the core compiler is approximately 85% complete and described as production-ready.

R3E Network published a new version of NeoRust, a substantial maintenance release focused on code quality, security, and developer experience. NeoRust v1.0.3 is compatible with Neo v3.9.1 and later, ensuring developers can build applications that leverage the latest Neo N3 protocol features.

Events

Feb. 20: NNT hosting CC & BB #84 on The Smart Economy Podcast official X account.

The post Neo News: Week in Review – February 9 – February 15 appeared first on Neo News Today.