---
title: "Transcript: Neo SPCC joins Neo Live to talk about distributed cloud storage platforms"
date: 2020-11-21
url: https://neonewstoday.com/general/transcript-neo-spcc-joins-neo-live-to-talk-about-distributed-cloud-storage-platforms/
tags: [General, GAS, NEO, Neo Live, NeoFS, NeoSPCC]
source: neonewstoday
---

# Transcript: Neo SPCC joins Neo Live to talk about distributed cloud storage platforms

**Published:** Sat, 21 Nov 2020 22:02:17 +0000
**URL:** https://neonewstoday.com/general/transcript-neo-spcc-joins-neo-live-to-talk-about-distributed-cloud-storage-platforms/
**Tags:** General, GAS, NEO, Neo Live, NeoFS, NeoSPCC

---

Neo St. Petersburg Competence Center offered an in-depth overview of the NeoFS decentralized cloud platform and how it differs from competitors in the recent Neo Live Ask Me Anything.

The Neo SPCC participants included chief technical officer, Anatoly Bogatyrev, chief information officer, Stanislav Bogatyrev, and software engineer, Alexey Vanin.

The AMA begins with A. Bogatyrev discussing NeoFS smart contracts and its ring network, followed by the two types of network nodes. He went on to speak about the network map, and how the distributed network architecture was designed to avoid bottlenecks. Other topics included compensating nodes with GAS, working will various scales of data, and more.

Afterward, the trio answered community questions about NeoFS, technical capabilities required to use the network, interacting with smart contracts, the upcoming NeoFS launch, among others.

A transcript of the AMA can be found below:

Songping: Hey, guys, the NeoLive this week will feature on NeoFS, which is a decentralized object storage solution, playing a key role in Neo3. We are very excited to have team behind to join the conversation today, and share their insights.

Anatoly: Hello, today we will talk about NeoFS and other systems. We will also answer your questions. Let’s start with what we do – NeoFS.

NeoFS is a distributed, decentralized object storage platform developed by Neo SPCC and integrated with the Neo blockchain, focusing on fault tolerance, scalability, and performance. In NeoFS itself, we use the oracle mechanism to integrate with Neo nodes and use Neo Blockchain as a source of truth and orchestration for a storage network.

Data usage is growing faster than ever before, and we all need better solutions to store, share, and protect that data. The existing cloud storage services seek to offer the easiest and most robust approaches. NeoFS is among those services, but definitely stands out. In the field of decentralized public storage systems, other systems include Filecoin, Sia, Storj, plus more.

In this session, we will talk about how the NeoFS works and how it differs from others. To understand the advantages of NeoFS and compare it with others, first need to understand how it works.

Now let’s take a look at NeoFS architecture and functionality.

NeoFS heavily relies on Neo 3 blockchain and its features. This allows NeoFS nodes to concentrate on their primary task — storing and processing data, and leave assets management and distributed system coordination to Neo and a set of smart contracts.

Source: Neo SPCC

In this picture, the “Storage Node Owners” is equal to “Storage Node Owners and Data Owners.”

The main smart contracts that provide the input and output of GAS tokens to the NeoFS account and the list of Inner Ring nodes on the Neo MainNet. NeoFS internal banking and data audit results are stored on the sidechain. This makes it so the large number of NeoFS internal transactions don’t occur on the Neo blockchain network. This approach also allows us to complete the Inner Ring nodes’ anonymity and not disclose their identification to other network nodes.

The main NeoFS network contract is deployed in the Neo main network. This contract’s roles are to maintain the Inner Ring nodes list, maintain the list of nodes-candidates for the Inner Ring, accept GAS input assets from users, and withdraw GAS to users.

The NeoFS network’s service contracts, such as Network Map contract, Container contract, Balance contract, Data Audit contract, and Reputation contract, are stored on the NeoFS Neo sidechain.

Also, support for NeoFS protocol has been added into Neo3 native oracle contract, allowing NeoFS objects to be used inside smart contracts. For example, a contract could make the decision to transfer tokens or otherwise change its behavior based on the contents of an object stored in NeoFS.

We designed NeoFS to work reliably in an unstable network and a network with untrusted nodes. And, we took into account the need to scale globally with a constant change in the amount, and quality of the storage network nodes.

The system does not require operational attention, and is capable of self-healing or controllably degraded until the very end, retaining the ability to perform the target function of storing data with the possibility of emergency evacuation of data to other nodes in case of failures.

In the NeoFS network are two types of NeoFS nodes: Storage nodes and Inner Ring nodes.

The first type is responsible for receiving data from a user, reliably storing it according to storage policy, and providing access to the data according to Access Control Lists. The storage nodes are coordinated with smart contracts.

The second type does not store any user data. It’s for tracking NeoFS network health, calculation Storage nodes reputation ratings, and performing data audits, giving out penalties and bounties depending on those audit results.

Each Storage node in the system has a set of key-value attributes, describing different node’s properties like geographical location or presence of SSD drives. Inner Ring nodes generate the Network Map, a multi-graph structure, allowing to a group and select Storage nodes Based on those key-value attributes.

In NeoFS, users put their files into Containers. Containers are like folders in a file system or buckets in Amazon’s S3, but with Storage Policy attached. A storage policy is defined by the user and tells how objects in this container must be stored.

The policy can use nodes attributes, so it can say, “Store my data in three different countries on two different continents in three copies on nodes with SSD disks and good reputation.” Storage nodes will do their best to keep data in accordance with this policy. Otherwise, they will not get paid for their service.

All storage nodes’ service fees are paid in GAS. We believe it’s good for the ecosystem and more convenient for users. They may own storage nodes and receive GAS, but at the same time, spend that GAS on paying for storage of their backups on other NeoFS nodes in the network.

This unique combination of Network Map, Storage Policy, and monetary incentives allows users to have full control over their data. They define where and how it should be stored and who can have access to it without trusting any third-party service or company.

Source: Neo SPCC

NeoFS network is presented in the form of a multigraph (Network map), which allows the use of mathematics (placement policy for the container and the placement function for the object) without requiring additional requests to the network to determine where to look for the object or where it should be placed.

In this case, the result is the same for all network nodes, and the recipient of the object can also check the correctness of the storage request without additional network requests.

The ability to define a container (like an s3 bucket) allows you to quickly perform object search operations and work with objects, even if the user does not store their identifiers. Also, the container (as a group of nodes) itself controls the compliance of the storage policy and is responsible for replicating objects in the case of node failure.

This allows you to get rid of bottlenecks in the form of central nodes that store information about the distribution of objects (as is done in Storj (satellites) for example) for GET/PUT operations or bottlenecks in the form of Orderbooks for PUT operations, as is done in Filecoin.

In this case, the GET operation of the object in NeoFS is possible without additional network requests to other nodes to determine where to look for the object. For example, in Filecoin, it is necessary to send requests to the Retrieval market service and imposes very high costs.

With the NeoFS approach, the speed of working with objects does not depend either on the size of the network or on the number of objects; all operations are independent, parallel, and do not have a limiter or single point of failure in the form of central metadata storage.

Simultaneously, the language for describing the storage policy allows you to express almost any rule, easily encode compliance with the requirements of the regulator or set the desired level of service quality, getting predictable behavior regardless of the momentary “weather” in the network. Geo-distributed and data replication are at the heart of the system and does not require additional operational loads.

Thus, due to the unique architecture and adaptation to the decentralized world of methods and algorithms of classical distributed systems, we have achieved that the speed of placing and receiving objects on the network occurs at the speed of the network without additional restrictions.

For a one megabyte object, it can take less than a second in the NeoFS real network. At the same time, in Filecoin, based on current high-level benchmarks, PUT steps are estimated to take around five to ten minutes for a one megabyte file in the Filecoin network, and the same is true for data retrieval.

And for use in real cases, Filecoin is forced to use an additional out-of-protocol caching layer in the form of additional IPFS nodes (Powergate solution, for example). These out-of-network nodes, in fact, either deprive Filecoin of advantages over centralized systems in the case when the application owner deploys his own nodes for caching data.

Or, it adds an unwarranted time for receiving data – since the public free IPFS network is outside the economic model and cannot guarantee data storage, which can lead to delays of tens of minutes even for a two MB file since it will have to be obtained from the Filecoin network itself.

In addition to the NeoFS network protocol, it is interesting to look at the storage entity – object.

In NeoFS, a storage object consists not only of a payload but also has a set of metadata. Including the user himself can assign his own metadata for more flexible work with objects. This allows you to work with data in NeoFS as in classical object storage systems and use NeoFS to store unstructured data and use it for IoT and Big Data analytics.

Also, the NeoFS protocol supports operations such as searching through the metadata of user objects or filtering rules in the Access Control List to give access to objects with certain metadata. This allows building any application for working with data to get objects from a container by their metadata.

Unlike most decentralized competitors, NeoFS allows such data operations as Search, Delete, Put, Head, Get, GetRange, GetRangeHash. While the Filecoin protocol only supports Put and Get of a payload.

But in addition to direct storage, it is also important to differentiate access rights and have algorithms for verifying that data is stored on the network correctly. Let’s start with data permissions. Data security is critical for any data storage system. It is important to define whether a user has access to a particular piece of information or not.

NeoFS supports access control inside the NeoFS network protocol with a flexible multi-level ACL system. ACLs specify users’ IDs and their rights, namely to read (search through the container) or write (other object operations). While receiving a request, any storage node gets a container and compares the sender (the first element in the chain of signatures) and the container’s ACL. The container’s ACL covers all objects therein. Thus, the container owner obtains full control and sets certain permissions authorizing defined groups of users only.

NeoFS uses a flexible ACL system involving basic ACL, extended ACL if it is allowed, and bearer tokens for specific or temporary access to obtain information on authorization rules.

In NeoFS, you can differentiate access rights both for the container (basic ACL) and for a specific object or a group of objects (extended ACL), united by any arbitrary attribute. Also, it is possible to define access rights for each specific operation. Basic and extended ACL together uses multiple parameters, thus, providing greater control. In this way, the owner of the data has complete control over who has access to it.

Whereas, Filecoin doesn’t have data access rights and permissions control. Anyone who knows the object ID can download the data. The only way to regulate access is to create one’s own contracts in the Filecoin blockchain for object placement, access, verification, and payment.

However, this looks like an almost impossible complex operation. It will require the user, bypassing the order book, to look for storage nodes himself and directly communicate with them off-chain to agree to work with custom untrusted contracts. It also requires a lot of development work from the user to implement and verify these contracts.

So far, we have determined how the network works without central servers and a single point of failure. Further, we mathematically defined how the vector of nodes where the object is stored or should be stored is determined. But, before working with the object, we must figure out how to make sure data is stored on the network correctly and how that work should be compensated.

In the case of a large number of objects in a distributed network of untrusted nodes with an ever-changing topology, the classical approach of comparing objects’ hashes with some sample in a central meta-data storage is not efficient. This causes unacceptable overhead.

To solve this problem, NeoFS uses Homomorphic hashing. It is a special type of hashing algorithm that allows computing the hash of a composite block from individual blocks’ hashes.

Source: Neo SPCC

For integrity checks, NeoFS calculates a composite homomorphic hash of all the objects in a group under control and puts it into a structure called Storage Group. During integrity checks, NeoFS nodes can ensure that hashes of stored objects are correct and a part of that initially created composite hash. This can be done without moving the object’s data over the network, and no matter how many objects are in the Storage Group, the hash size is the same.

Each epoch, Inner Ring nodes perform a data audit. It is a two-stage game in terms of game theory.

At the first stage, nodes in the selected container are asked to collectively reconstruct a list of homomorphic hashes that form a composite hash stored in Storage Group. By doing that, nodes demonstrate that they have all objects and can provide a hash of those objects. The provided list of hashes can be validated, but it is unknown if some nodes are lying at the current stage.

In the second stage, it is necessary to ensure that nodes are honest and do not fake the check results. The Inner Ring nodes calculate a set of nodes’ pairs that store the same object and ask each node to provide the homomorphic hashes of that object. Ranges are chosen in a way that the hash of a range asked from one node is the composite hash of ranges asked from another node in that pair. Nodes cannot predict objects or ranges that are chosen for audit. They cannot even predict a pair node for the game.

This stage discovers malicious nodes fast because each node serves multiple containers and Storage Groups and participates in many data audit sessions. When a node is caught in a lie, it will not get any rewards for this epoch. So the price of faking checks and risks are too high, and it is easier and cheaper for the node to be honest and behave correctly.

Combining the fact of nodes being able to reconstruct the Storage Group’s composite hash and the fact of nodes’ honest behavior, the system can consider that the data is safely stored, not corrupted, and available with a high probability.

In the case of a successful data audit result, the Inner Ring nodes initiate microtransactions between the data owner’s accounts and the storage node’s owner.

Each of the decentralized systems tries to solve the problem in its own unique way. We focus on a probabilistic approach and homomorphic hashing to minimize the network load and not have single points of failure.

Returning to the comparison with Filecoin, we can summarize this by the fact that Filecoin network protocol is well suited for storing large objects as a cold storage backup. NeoFS is well suited for working with application data and is equally well adapted for a big data stream of small objects and working with large cold data. Access control systems and metadata make NeoFS an efficient and flexible storage platform for creating applications.

We can spend hours talking about the structure of the NeoFS network, but I would like to summarize the advantages of NeoFS:

- Infinitely scalable due to Network Map and Data Placement mechanisms

- Each node can initiate object operations without additional network requests

- Speed of placing and receiving objects on the network occurs almost at the speed of the internet without additional restrictions

- Work with objects’ metadata and operate over it (search by headers or use in the permission conditions)

- Designed to work reliably in a chaotic environment

- NeoFS puts the control over data in users’ hands due to placement rule and flexible ACL system

- Integrated with popular protocols such as HTTP and S3

- Zero-knowledge data validation (Data Audit) based on homomorphic cryptography

- Directly accessible from smart contract code

- GAS is used for payments, instead of self-made token

- Incentive model based on market principles

- Runs on commodity hardware

And a few words about the future, NeoFS will be released with the Neo3 network. Neo SPCC also plans to add a layer for decentralized data processing in the future, providing computation in addition to storage.

Source: Neo SPCC

This will make it possible to perform complex calculations on data inside smart contracts without the prohibitive on-chain cost.

For example, you will be able to upload a photo to NeoFS, process it with a neural network to confirm authenticity, and trigger a subsequent transfer of tokens. All this would be performed inside one smart contract on the Neo network with integrated Oracle protocol, leveraging the cost efficiency of the NeoFS storage network (and future data processing) network.

This is what we will strive for, and this is what will allow us to achieve previously impossible solutions. The Neo SPCC team views this full decentralized stack as the future for FinTech and DeFi blockchain applications.

So, we are ready to answer your questions.

Q1: What’s the maximum size of data we can upload in one file, or different files per upload?

Stanislav: An object in NeoFS may not have a payload and contain only meta-information in the form of headers. Thus, we can say that the minimum size of an object is zero. However, payment for a large group of null objects will be charged a minimal fee for validation of the correct storage of data (Data audit). This fee encourages users to create storage groups as large as possible, which minimizes the storage of redundant metadata on the network.

There is no technically maximum object size limit in the system. All large objects are converted into a chain of smaller linked objects that are placed in a container. Splitting and assembling of objects is done transparently and allows applying other sequential transformations.

Q2: Do I need to know how to code to use NeoFS?

Stanislav: To use NeoFS, you are not required to code smart contracts. NeoFS has simple gRPC-based protocol and supports HTTP and S3 protocol gateways (more to come soon). Someone may use NeoFS in almost the same way as the would use AWS S3.

Q3: Is there a minimum system requirement or technical skills to be a Storage node on NeoFS?

Anatoly: To do this, it is enough to start the NeoFS daemon on your node and configure it. It will be as simple as possible.

Simultaneously, within the epoch (on the test network, it is about six hours), you will be included in the network map and begin to participate in data storage, receiving payment for the stored users’ data each epoch. For now, the only limitation is Linux and a normal internet connection.

Q4: How long has your team been working on the project and how many people are on the Neo SPCC team?

Anatoly: NeoSPCС was founded in August 2018, with the support of Neo Global Development to research and develop a public open-source decentralized cloud platform for storing and processing data, under the auspices of the global open source ecosystem development. And by the end of September 2018, we had already started developing the NeoFS architecture.

One year and a half later, in the spring of 2020, we completed the full functional Proof-of-Concept NeoFS version, which confirmed all technological concepts and showed its effectiveness in testing. This also included public testing based on a private Neo2 network.

When we received confirmation of all hypotheses, we began implementing the final version of NeoFS, which will soon be released on the Neo3 network. In it, we took into account all the test results, optimized the architecture, expanded the API, implemented improvements to all major protocols and methods, and built the NeoFS network on Neo3, which by this time had found its final solutions.

Our strategy requires deep expertise in distributed storage and data processing and related areas of computer science. We have brought together talented professionals with experience in renowned international cloud companies. All employees are graduates of leading technical universities, including PhDs. There are 12 developers in our company now. You can find their individual profiles on the Neo SPCC website.

Q5: What happens to an object when a user stops paying for its storage?

Alexey: To keep your files safe in a container, you should create “storage group” entity. It is not a variable or a smart-contract parameter, it is just a special object in NeoFS storage.

Inner ring audits containers with storage groups and provides payments. If a user removes “storage group” entity or doesn’t have assets to pay, the inner ring won’t make payment transfers to storage nodes. Storage nodes can track it and then remove unpaid objects if they want to (this is a configurable option).

Q6: Other than storage, what Neo3 feature are you most excited about?

Stanislav: Oracles! We believe it’s vital to be able to interface external systems from smart contract code to build the Smart Economy. With NeoFS, it becomes possible to offload heavy data storage off-chain, while having similar trust in it.

Later, we hope to add possibility to offload heavy computations.

Q7: Is it correct to say that Neo3 smart contracts will directly access NeoFS? Who will pay for the storage in that case? The contract owner?

Anatoly: Yes, based on integration at the Oracle protocol level, calls to NeoFS from a smart contract will be available.

In the initial implementation of the Oracle protocol, a get object operation will be available. In the future, the implementation of other operations is also planned. In the case of PUT operation, the owner of the container will pay for data storage. But also, from the smart contract, it can get pre-paid from contract executors.

Also, in the next versions of NeoFS, we are considering adding the possibility of paying for storage of objects at choice, either from the owner of the container or from the owners of the data. This will allow the creation of public (or for a specific group of users) containers without worrying about payment issues.

Q8: When will NeoFS MainNet release?

Alexey: NeoFS will be released with the release of Neo3 MainNet. And before that, NeoFS will be available on the Neo3-Preview4 TestNet for the public testing, scheduled to launch at the end of Q4 2020.

A development SDK and locally running NeoFS setup are already available on the Neo SPCC GitHub. With neofs-dev-env you can deploy the entire network locally (Neo and NeoFS) for experiments or for your applications development and testing.

Q9: What are the most interesting or groundbreaking practical use cases that NeoFS will enable for Neo3?

Stanislav: First, GAS will become useful for NeoFS payments.

Second, old blockchain blocks can be offloaded to NeoFS in the future.

Lastly, smart contracts can produce data, store it on NeoFS, and become available via regular HTTP. This opens interesting possibilities for blockchain games and dApps to become really distributed.

Q10: Can you elaborate on the differences between NeoFS and Filecoin? Why should the user choose NeoFS over Filecoin?

Anatoly: First, the main difference (and why shall we choose NeoFS) is the inability to use Filecoin as a storage system for real applications with a high store or retrieve flow of the data due to its very slow data operating. If we are talking about the Filecoin protocol itself. Even tests from the Filecoin authors themselves show five to ten minutes per one-megabyte file. This is only suitable for cold storage.

And for use in real cases, Filecoin is forced to use an additional out-of-protocol caching layer in the form of additional IPFS nodes (Powergate solution, for example). I talked about the limitations of out-of-protocol nodes in more detail above in the main part.

The second reason, is the ability of the NeoFS to work with objects metadata, which Filecoin cannot do.

Thirdly, the flexible ACL system to control permissions to the objects in the NeoFS.

Q11: How does NeoFS ensure that data access rights are only controlled by the uploader? And, will NeoFS be more secure than Filecoin?

Alexey: You are correct, data security is quite important. NeoFS ensures data control through container’s Access Control Lists. Basic ACL rules provide general control, making container private, public, or read only.

With extended ACL rules user can provide or restrict access to specific objects (e.g. permit access to objects with some ‘secret’ attribute) or specific request senders (e.g. object is available for users with specific public keys).

As for Filecoin, I think our approach with ACLs is more traditional for storage systems, which is good for end users. But, I am not sure we can compare them which is more secure this way.

Q12: How do you plan to promote NeoFS? Will there be a promotional campaign?

Stanislav: NeoFS is the decentralized distributed object storage that uses Neo3 blockchain features extensively in it’s core, so it’s not “selling blockchain to people.” It’s more so that we propose truly decentralized independent data storage alternative to centralized clouds (i.e., AWS, Google, and Microsoft).

And, the key feature here is the full control over data from the user side. Recent stories with centralized clouds deleting user’s data and denying service is the best promo campaign.

Q13: Who are NeoFS’ target users?

Alexey: Developers of the distributed applications and smart contracts.

Tech-savvy users of existing apps that support S3.

Web developers looking for an independent CDN solution with geo-replication.

Q14: Will you provide any GUI for NeoFS?

Anatoly: Not for now. We are focused on NeoFS storage software and protocol development, tasks requiring a lot of research. We want to achieve excellent results in the creation of technology.

But we hope that in the release of Neo3, NeoFS support will be added to Neo GUI by its development team. It can also become someone’s good start-up from the open-source community.

As GUI for NeoFS, or various applications on top of it – for example, photo galleries, file managers like Dropbox, and so on.

We are also engaged in the creation and support of the S3 gate to use GUI that can work with the Amazon S3.

Q15: You said that there are S3 gates. So, can I use my app with S3 storage? Can I use NeoFS with S3 gate instead of Amazon? Is it possible without changing my app?

Stanislav: Yes, it is possible right now. It is enough to declare in your application S3-gate as an S3 endpoint and the pre-prepared credentials.

Note: Some edits have been made for formatting and readability.

The full AMA can be found at the link below: https://t.me/NEO_EN/98063

The post Transcript: Neo SPCC joins Neo Live to talk about distributed cloud storage platforms appeared first on Neo News Today.
