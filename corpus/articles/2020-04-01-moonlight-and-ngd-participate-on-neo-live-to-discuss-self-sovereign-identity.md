---
title: "Moonlight and NGD participate on Neo Live to discuss self-sovereign identity"
date: 2020-04-01
url: https://neonewstoday.com/general/moonlight-and-ngd-participate-on-neo-live-to-discuss-self-sovereign-identity/
tags: [General, LX, Neo Live, SeraphID]
source: neonewstoday
---

# Moonlight and NGD participate on Neo Live to discuss self-sovereign identity

**Published:** Wed, 01 Apr 2020 22:16:21 +0000
**URL:** https://neonewstoday.com/general/moonlight-and-ngd-participate-on-neo-live-to-discuss-self-sovereign-identity/
**Tags:** General, LX, Neo Live, SeraphID

---

Neo Global Development (NGD) recently hosted an English-based Neo Live with the founder of Moonlight and co-founder of COZ, Tyler Adams, and senior engineer on the NGD protocol team, Justin Jin. Neo Live is an ask me anything (AMA) style event that aims to showcase projects and partners within the Neo ecosystem. The event was moderated by NGD community operations specialist, Songping Que.

The conversation focused primarily on decentralized and self-sovereign identity (SSI) solutions on the Neo blockchain, an area which Adams and Jin are both actively working on projects.

Adams’ Moonlight is an application that allows its users to create privacy-protected profiles that have verification built-in through its VivID SSI solution. In using VivID Adams said, “applications don’t necessarily need to know anything about blockchain, all that they really want is access to verified information. If one of their users doesn’t have that verified information on their identity, we provide those workflows for the users or third parties to issue to their users through industry-standard protocols.”

Jin is currently working on SeraphID, a framework that provides the tools to form SSI networks with three key participant types: identity issuers, verifiers, and claim holders. Any entity can deploy an issuer contract to the Neo blockchain to create their own unique SSI network, designed to suit their own specific use case by defining credential schemas.

Topics discussed during Neo Live included the differences between SSI and decentralized identities (DID), security benefits offered by blockchain, resilience to quantum computing, regulation and compliance, use cases, next steps, and more.

SSI and DID

According to Jin, SSI describes the identity system that provides an individual ownership over their identity. With SSI, entities can prove their identities to others without requiring authentication from a body of authority. DID, on the other hand, refers to the design of an ID system offers the owner the ability to prove control of their identity and is able to be implemented independently of any centralized registry.

“I think these two terms are similar in purpose, and these two guarantee self-controllability of identity, rather than by some certain authority. DID is more focused on technical means of realization of such purpose.” Jin clarified.

Adams included that SSI mechanisms already exist and are used relatively often in our daily lives. He cited the driver’s license as a form of SSI, as the user has been granted an authenticated document that can be shown to prove an identity. In this case, the person verifying the identity does not need to contact the issuing authority to verify the details on the document, but instead is able to trust in its authentication.

Security benefits of blockchain

Que pointed out that traditional digital identity management requires a centralized database of information that is a lucrative target for hackers. She inquired, “how can blockchain and SSI solve vulnerabilities from technical and implementation standards?”

Adams began by discussing data entropy. Specifically, he noted that when information is shared there’s no real way of revoking that knowledge because an individual can write that information down or store it elsewhere. Thus, most SSI projects focus on the “verification and proof” piece of identity attributes, while data privacy is a separate and a more nuanced topic for the wider blockchain privacy ecosystem.

With SSI and DID, projects seek to define a framework for how that original data should be secured. Guidelines from smart contracts can enforce certain levels of security around the original dataset provided to other applications for use. However, Adams said, “if you give access to your data to Facebook, nothing is saying that they won’t take that information and copy it into their servers.”

Jin added that as SSI allows the owner to store and manage their identities, they at least have the ability to choose when they want to share personal information with third parties.

How can immutable data be safe from future computation power

Que stated that current encryption standards via distributed ledger technology meet the privacy requirements of blockchain users. She asked, “how can we ensure that the data will be safe from quantum computing or other technological innovations in the future?”

Adams stated that the Moonlight team assumes that malicious actors will eventually be able to reverse engineer encrypted data with advances in technology over time and effort. Therefore, the level of security should be based on the sensitivity of the data and that potential risk. This equation can be better balanced by two variables: security mechanisms and time.

First, depending on the data, the information could be encrypted using anything from zero-knowledge proofs to a symmetric or asymmetric encryption algorithm. Secondly, there is eventually a time horizon where the data is no longer valuable (i.e., in 300 years, today’s data isn’t nearly as pertinent).

Jin added that a lot of data stored on blockchain today is public, such as issued identity, revocation registries, and gamer hashes. As this data is already public, it isn’t a top priority to defend against hacks.

Further, he believes apps can choose whether they want to store data onchain or offchain, a combination of which could create enough of a safety barrier from quantum cracking.

In the future, when quantum computing can crack encrypted messages, Jin believes cracking encrypted data from hashed data will still be an impossible task. And if it does become possible, it’ll be so far in the future that current claims will not be at risk (as the user will likely not be alive).

At that time, he also anticipates there will be other hashing and encryption methods in service that will be able to resist quantum computing.

Regulation and compliance

GDPR is an aggressive regulation that gives European citizens more control over their personal data. Que asked, “What is the impact of GDPR on the development of DID and SSI solutions?”

Jin responded that, currently, the majority of services around the world don’t meet the GDPR requirements and have two paths forward. First, to reach these standards, and second, not conduct business in Europe.

He said, “for those who want to survive, an SSI strategy that can prevent personal data leakage is in great need. The implementation of GDPR brings a good chance for SSI development, as SSI provides an exactly suitable solution for GDPR.”

Adams believes SSI projects have slow timelines because of various GDPR issues that arise for blockchain-based projects and how they can be handled. He said, “as soon as data is put on the chain, it can’t be deleted. It’s immutable. So, in theory, as soon as a company releases a product on a public network, they are potentially liable for that data in perpetuity.”

As an example, he highlighted the California Consumer Privacy Act (CCPA), which “creates new consumer rights relating to the access to, deletion of, and sharing of personal information that is collected by businesses.” 

Regarding various data laws, Adams noted, “I’m not looking forward to supporting all of them in [Moonlight] because it’s going to be very patchwork at first until something at a higher level shows up. Or, maybe in decentralized fashion they all agree on what it needs to look like.”

Looking forward

To round off the conversation, Que asked Adams and Jin what the next steps are for their respective projects.

Adams stated that Moonlight intends to increase the available verifiable attributes on its platform to strengthen its VivID solution. Further, Moonlight aims to release technical specifications about the VivID solution in the coming weeks.

SeraphID aims to release a smart contract template and SDK for DID resolvers that will be able to integrate with Neo3. Jin also intends to integrate recovery strategies for when issuers lose private keys, integrate with other ecosystem components like NeoFS, and integrate identity fraud features.

Following the publishing of the Neo Live interview, a Q&A is being held on the Neo Reddit through April 6th, 2020, where both Adams and Jin will answer questions from the community.

The Neo Live interview can be found at the link below:

https://youtu.be/xGtr4wsB-ys
                                    

The post Moonlight and NGD participate on Neo Live to discuss self-sovereign identity appeared first on Neo News Today.