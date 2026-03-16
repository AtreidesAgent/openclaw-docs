---
title: "Neo Frontier Launchpad participants report positive experiences building with N3 tools"
date: 2021-07-09
url: https://neonewstoday.com/development/neo-frontier-launchpad-participants-report-positive-experiences-building-with-n3-tools/
tags: [Development, General, GAS, NEO]
source: neonewstoday
---

# Neo Frontier Launchpad participants report positive experiences building with N3 tools

**Published:** Fri, 09 Jul 2021 22:57:01 +0000
**URL:** https://neonewstoday.com/development/neo-frontier-launchpad-participants-report-positive-experiences-building-with-n3-tools/
**Tags:** Development, General, GAS, NEO

---

Neo Frontier Launchpad participants are reporting positive experiences using tools that have been developed since N3 was announced in March 2019. Their initial reflections indicate that Neo is making progress on its ambition to become one of the most developer-friendly platforms in blockchain.

Developer friendliness has been a goal for years. The philosophy for N3 tooling was not just to attract blockchain developers, but to target all developers. NGD Enterprise lead, John deVadoss, has unwaveringly reiterated this point since joining the Neo ecosystem. In a May 2020 Neo News Today podcast, deVadoss said:

For us, the starting point is very simple: How do we take blockchain development mainstream? Across the globe [there are] about 20 – 21 million developers. That was the goal. It was not the Ethereum 50,000 or 100,000. No, it was 21 million developers.

The Neo Frontier Launchpad is a global event bringing together more than 600 developers to compete for prizes and incubation opportunities. One of the main objectives for Launchpad is to seed new dApps on the soon-to-be-launched Neo N3 network. All project submissions are due on July 12, and winners will be announced by the end of the month.

To learn more about the N3 developer experience, Neo News Today reached out to Launchpad participants, many of whom are brand new to the ecosystem. We asked developers to comment on aspects such as maturity, completeness, ease-of-use, and supporting resources, to paint a picture of the current state of Neo’s tooling suite.

New to N3, but not blockchain development

While some participants of the Neo Frontier Launchpad are brand new to blockchain, others had previously built on Neo Legacy or Ethereum.

Thomas Geyer is finishing his Master’s degree in Innovation and Technology Management. In the Summer of 2020, he built an NFT-based smart contract on Neo Legacy, intended for a game that was ultimately never released.

Geyer compared his experience developing on Neo Legacy to using N3 during the Neo Frontier Launchpad. He said, “Back then, the provided tooling was good, but it was way harder to set up the developer environment.” Ultimately, he had found that debugging the smart contract was complicated, and running a PrivateNet was a challenging experience.

In comparison, N3’s tooling “synergises perfectly.” Geyer is using COZ’s neo-boa to write his smart contracts, which interact with his dApp through neon-js. He is using NGD Enterprise’s Neo Blockchain Toolkit for VS Code to debug and test in a local environment.

Geyer noted, “The whole development stack offered for the Neo ecosystem is great.”

Jason Tezanos is a traditional developer with more than 20 years of experience. Although he considers himself a mobile engineer, primarily working on iOS, he started his career working with C++, Flash, and Actionscript. He also has done quite a bit of work with Ethereum and written contracts in Solidity.

Tezanos noted that coming from Ethereum meant adjusting to the idiosyncrasies of a new platform. For example, Update is a new N3 feature implemented in the native “ContractManagement” contract, which is the part of the Neo protocol that oversees the creation and management of all smart contracts on the blockchain. If the Update method is included in a smart contract, then the developer can use ContractManagement to update the code after it has been deployed.

This is a feature that does not exist on the Ethereum platform. Instead, every time a developer would like to update their smart contract code, they would need to deploy the contract to a new address.

Tezanos believes N3’s Update feature could be a double-edged sword. While he finds it positive that Update allows Neo contracts to remain on the same address, he noted the underlying code could theoretically be rewritten, potentially in a malicious manner. Tezanos said, “Products will need to highly emphasize trust because of this, which may not be a bad thing really. I wouldn’t be surprised if writing contracts without an Update function ends up becoming the norm.”

Making use of N3 features

Generally, Launchpad participants have communicated positive sentiments regarding the features available for N3. This includes the launch of NeoFS, a distributed object storage network that natively integrates with the Neo blockchain.

Mitrasish Mukherjee is a full-stack developer with more than two years experience working with enterprise software solutions. Alongside his professional resume, Mukherjee has contributed open-source code to multiple blockchain protocols, and won a handful of hackathons.

Mukherjee and his team are building an application that heavily integrates NeoFS. He noted a particular affinity for the S3 style of NeoFS as well as its unique policy-based storage mechanism. Mukherjee said:

The initial impression is pretty good. The multipart series on working with NeoFS service and Neo gateways are really awesome. It gave us a lot of information needed to start building our solution on Neo.

Although Mukherjee did acknowledge some “rough edges,” he expressed satisfaction on how quickly the Neo SPCC team provided support, fixing and adding features at their request.

Hu Rui is a college student and Java developer. Prior to the Launchpad, Hu had worked on several backend projects that involved traditional databases, Rest API, and microservices utilizing gRPC and cloud infrastructure. Neo N3 is the first public blockchain Hu has built on, with previous development experience building a permissioned blockchain using Solidity.

An attractive feature of building on the Neo blockchain, Hu said, is the support to code and compile multiple developer languages:

Unlike the ‘traditional blockchain programing language,’ Solidity, Neo N3 supports a lot of native (compared with the blockchain VM) languages, which helps a lot, since not everyone is capable of mastering a new tech/language in short amount of time. Picking what they are already skilled in is the best choice.

So far, Hu and his team have not hit any roadblocks to prevent them from building their application. However, he note that developing on blockchain comes with its own learning curve – even if you’re using a language you are already familiar with:

“Here is my experience: Doing blockchain programming is different from developing a native application, caused by a different execution model, but it’s nothing special. Just like programming, you speak English, but you have to speak it in computer’s style, so the computer can understand you. Doing blockchain programing is more like speaking Java/Python/other language, but you have to speak them in blockchain’s manner, so your code can work properly on the NeoVM.”

On the road, but not yet at the destination

The Neo Frontier Launchpad is as much an opportunity to stress test real-world development as it is an incubation event.

The first Neo N3 release candidate was rolled out in March 2021 and is now on its third major version. Upon each release, every developer tool across all languages must be updated to align with the core code. The rapid evolution and sheer volume of work meant that developer documentation is still playing catch up. To bridge the gap, the Neo community has served as an invaluable resource to those seeking information, as has historically been the case.

For the past eight years, William Song has been writing trading system software, primarily in Java. While Song kept an eye on the blockchain space, he never tried blockchain development until the Neo Frontier Launchpad. Song opted to build in the Neo ecosystem because of the heavy focus on developer tools and its all-in-one solution. Regarding document standardization, Song noted:

My biggest suggestion for improvement is that while each organization seems to have its own tutorials and documentation, there is little cohesion across organizations. The tooling is excellent and will only get better from here as common use cases are uncovered and documentation becomes more complete.

Robert Oschler is a natural language processing developer with medical application, blockchain, and robotics software experience. Before the Launchpad, Oschler spent a year working on an Ethereum dApp using Solidity and the Truffle development suite.

Oschler is all too familiar with the pain of outdated documentation. Regarding his experience on Ethereum, Oschler said, “There were so many references to code samples and tutorials that no longer worked because they reference older versions of the codebase. The documents were never updated with instructions to see newer versions, so I had the repeated experience of wasting tons of time implementing a big tutorial, only to waste several days after that figuring out that some bug or another was due to an old compiler version reference, or a legacy code idiom, or just bad information.”

Though N3 documentation may currently be lacking, there are Neo leaders on-hand to help provide answers through web and chat forums. Oschler said, “N3’s docs are lagging the platform, but the Discord is more than making up for it due to the tenacity and responsiveness of folks like DevHawk and Hal0x2328.”

As the Neo N3 codebase formalizes on approach to MainNet, the groups responsible for building Neo’s tooling will shift focus towards standardizing documentation and offering more sample code to help new developers bootstrap projects. The feedback provided by Neo Frontier Launchpad participants will be invaluable in identifying priorities.

Ecosystem activity in a post Legacy era

Looking forward, N3 already looks more equipped to support the efficient development of dApps than its Legacy predecessor. Participants who spoke with Neo News Today outlined plans to build projects such as DeFi services, games, and social media services, using technologies such as NFTs and NeoFS.

Final submissions will be judged in July 2021 by a panel that includes Da Hongfei, Erik Zhang, John deVadoss, and representatives from Exodus, Ledger, Blockchain Cuties, Coin Telegraph, and other entities. 

Ultimately, 11 projects will be awarded prizes and offered post-hackathon incubation opportunities. These will be the first seeds of renewed activity in the Neo ecosystem. Afterward, more businesses and projects are welcome to build on N3 with encouragement to migrate from Neo Legacy or other blockchain networks. In addition, Neo Global Development aims to spur development on the new Neo blockchain through its N3 Early Adoption Program.

 

The post Neo Frontier Launchpad participants report positive experiences building with N3 tools appeared first on Neo News Today.
