---
title: "Neo X launches TestNet v0.5.2 with post-merge architecture changes, blob storage support"
date: 2026-03-09
source: Neo News Today
url: https://neonewstoday.com/development/neo-x-launches-testnet-v0-5-2-with-post-merge-architecture-changes-blob-storage-support/
categories: ['Development', 'General', 'NeoX']
guid: https://neonewstoday.com/?p=58983
---

Neo X has released TestNet v0.5.2, a patch upgrade for its EVM-compatible blockchain that introduces infrastructure changes tied to newer Ethereum client...
The post Neo X launches TestNet v0.5.2 with post-merge architecture changes, blob storage support appeared first on Neo News Today.


## Full Content

<img width="800" height="450" src="https://neonewstoday.com/wp-content/uploads/2026/03/Neo-X-Template.png" class="webfeedsFeaturedVisual wp-post-image" alt="" style="display: block; margin-bottom: 5px; clear:both;max-width: 100%;" link_thumbnail="" decoding="async" loading="lazy" srcset="https://neonewstoday.com/wp-content/uploads/2026/03/Neo-X-Template.png 800w, https://neonewstoday.com/wp-content/uploads/2026/03/Neo-X-Template-300x169.png 300w, https://neonewstoday.com/wp-content/uploads/2026/03/Neo-X-Template-768x432.png 768w" sizes="auto, (max-width: 800px) 100vw, 800px" /><p>Neo X has released <a href="https://x.com/ngd_neo/status/2029819746208841807" target="_blank" rel="noopener">TestNet v0.5.2</a>, a patch upgrade for its EVM-compatible blockchain that introduces infrastructure changes tied to newer Ethereum client behavior, expands support for EIP-4844 blob data, and updates the network&#8217;s peer-to-peer communication model.</p>
<p>The release is framed as a patch rather than a chain reset. According to the team, v0.5.2 does not include a hard fork in the genesis file or database changes that would require node operators to reinitialize or resynchronize from scratch. However, the upgrade includes a protocol migration in the P2P layer, meaning nodes running versions older than v0.5.2 will no longer receive execution-layer block broadcasts needed for synchronization.</p>
<p>The release is framed as a patch rather than a chain reset. According to the team, v0.5.2 does not include a hard fork in the genesis file or database changes that would require node operators to reinitialize or resynchronize from scratch. However, the upgrade includes a protocol migration in the P2P layer, meaning nodes running versions older than v0.5.2 will no longer receive execution-layer block broadcasts needed for synchronization. The team encouraged node operators to perform the upgrade as soon as possible.</p>
<p>At a high level, the update completes Neo X as a Geth v1.15 implementation. The network is adopting a more modern Ethereum-style internal coordination between consensus and execution, without requiring a new consensus client or a &#8220;Merge&#8221;-style overhaul of the underlying consensus algorithm.</p>
<h2>Blob Data Storage<b></b></h2>
<p>Another headline change is support for execution-layer blob storage and related JSON APIs for EIP-4844. Blob data has become an important part of the broader Ethereum scaling conversation because it provides a more efficient way to handle certain data availability requirements. With v0.5.2, Neo X adds a configurable blob file system for persisting that data and exposes query APIs around it.</p>
<p>The tradeoff is storage demand. The team noted the new blob storage may require up to approximately 288 GB of disk space, a figure node operators will need to account for before upgrading production environments.</p>
<p>Neo X initially introduced Cancun and Prague fork support in <a href="https://github.com/bane-labs/go-ethereum/blob/bane-main/CHANGELOG.md" target="_blank" rel="noopener">v0.5.0 </a>in Oct. 2025, but noted at the time that EIP-4844 blob transactions were not fully implemented and blob data was only short-lived in the network with no API for proper access. The v0.5.2 release addresses that gap.</p>
<h2>Block Broadcasting<b></b></h2>
<p>The release also changes how the network handles block broadcasting. Neo X has introduced a beacon protocol and moved the block broadcast message to the consensus layer. Alongside that shift, the team removed execution-layer reorganization judgment and other deprecated pre-merge behaviors.</p>
<p>The effect is that Neo X is cleaning out legacy logic tied to older Ethereum-era assumptions and replacing it with patterns better suited to the current post-merge architecture.</p>
<h2>Additional fixes</h2>
<p>The update also includes improvements to snap synchronization for short chains and fixes for DKG synchronization failures &#8211; issues related to the <a href="https://neonewstoday.com/development/neo-x-testnet-updated-to-v0-4-1-with-audited-zk-dkg-full-anti-mev-functionality/" target="_blank" rel="noopener">zero-knowledge distributed key generation protocol</a> that underpins Neo X&#8217;s anti-MEV system. Node operators running validator nodes will need to update their configuration flag from <code>--miner.etherbase</code> to <code>--miner.pending.feeRecipient</code>.</p>
<p>The v0.5.2 release is live on TestNet and will be deployed to MainNet shortly, according to the announcement. The full announcement can be found at the link below:<br />
<a href="https://x.com/ngd_neo/status/2029819746208841807" target="_blank" rel="noopener">https://x.com/ngd_neo/status/2029819746208841807</a></p>
<p>The post <a href="https://neonewstoday.com/development/neo-x-launches-testnet-v0-5-2-with-post-merge-architecture-changes-blob-storage-support/">Neo X launches TestNet v0.5.2 with post-merge architecture changes, blob storage support</a> appeared first on <a href="https://neonewstoday.com">Neo News Today</a>.</p>

