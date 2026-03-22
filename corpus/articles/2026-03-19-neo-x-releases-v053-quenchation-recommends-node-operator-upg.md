---
title: "Neo X releases v0.5.3 “Quenchation,” recommends node operator upgrade"
date: 2026-03-19
source: Neo News Today
url: https://neonewstoday.com/development/neo-x-releases-v0-5-3-quenchation-recommends-node-operator-upgrade/
categories: ['Development', 'General', 'NeoX']
guid: https://neonewstoday.com/?p=59247
---

Neo X has released v0.5.3, a patch update for the EVM-compatible blockchain that introduces several incremental improvements and bug fixes. The team...
The post Neo X releases v0.5.3 “Quenchation,” recommends node operator upgrade appeared first on Neo News Today.


## Full Content

<img width="800" height="450" src="https://neonewstoday.com/wp-content/uploads/2026/03/Neo-X-Template-1-1.png" class="webfeedsFeaturedVisual wp-post-image" alt="" style="display: block; margin-bottom: 5px; clear:both;max-width: 100%;" link_thumbnail="" decoding="async" loading="lazy" srcset="https://neonewstoday.com/wp-content/uploads/2026/03/Neo-X-Template-1-1.png 800w, https://neonewstoday.com/wp-content/uploads/2026/03/Neo-X-Template-1-1-300x169.png 300w, https://neonewstoday.com/wp-content/uploads/2026/03/Neo-X-Template-1-1-768x432.png 768w" sizes="auto, (max-width: 800px) 100vw, 800px" /><p>Neo X has <a href="https://x.com/ngd_neo/status/2034216094664372332?s=20" target="_blank" rel="noopener">released v0.5.3</a>, a patch update for the EVM-compatible blockchain that introduces several incremental improvements and bug fixes. The team said the upgrade is “highly recommended” for node operators currently running v0.5.2.</p>
<p>Dubbed “Quenchation,” the release continues Neo X’s convention of assigning distinctive names to version updates. It follows the March 6 “Polarization” release, which introduced broader infrastructure changes tied to newer Ethereum client behavior, added execution-layer blob data storage and APIs for EIP-4844, and migrated the network’s peer-to-peer communication model to support post-merge behaviors.</p>
<p>Neo X v0.5.3 is a narrower maintenance release focused on stability and cleanup. According to the release notes, the update refreshes sealing proposals when ChangeView happens, updates the error message shown when etherbase is missing, and reduces the log level for missing blob transactions.</p>
<p>The patch also includes two bug fixes: excluding transaction blob sidecars in the OnTransaction callback and correcting blob error handling for blocks committed by the dBFT consensus protocol. Both address edge cases in the blob-related functionality introduced in the prior release.</p>
<p>The release notes outline a straightforward upgrade path for node operators moving from v0.5.2: download the new binary, gracefully stop the node, replace the old binary, and restart the node. Unlike the previous upgrade, v0.5.3 does not require additional configuration changes.</p>
<p>The full release notes can be found at the link below:<br />
<a href="https://github.com/bane-labs/go-ethereum/releases/tag/v0.5.3" target="_blank" rel="noopener">https://github.com/bane-labs/go-ethereum/releases/tag/v0.5.3</a></p>
<p>The post <a href="https://neonewstoday.com/development/neo-x-releases-v0-5-3-quenchation-recommends-node-operator-upgrade/">Neo X releases v0.5.3 “Quenchation,” recommends node operator upgrade</a> appeared first on <a href="https://neonewstoday.com">Neo News Today</a>.</p>

