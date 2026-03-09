---
title: "Transcript: GrantShares maintainers Guil. Sperb Machado and Claude Mueller discuss community grants"
date: 2022-06-26
url: https://neonewstoday.com/dao/transcript-grantshares-maintainers-guil-sperb-machado-and-claude-mueller-discuss-community-grants/
tags: [DAO, Development, General, GAS, GrantShares, NEO, Neo Live]
source: neonewstoday
---

# Transcript: GrantShares maintainers Guil. Sperb Machado and Claude Mueller discuss community grants

**Published:** Sun, 26 Jun 2022 22:15:09 +0000
**URL:** https://neonewstoday.com/dao/transcript-grantshares-maintainers-guil-sperb-machado-and-claude-mueller-discuss-community-grants/
**Tags:** DAO, Development, General, GAS, GrantShares, NEO, Neo Live

---

AxLabs Senior Software Engineers Guil. Sperb Machado and Claude Muller recently joined the Neo Live AMA series to talk about GrantShares, Neo’s fundraising DAO. Participants in the AMA shared rewards from a prize pool comprising 10 Neoverse blindbox NFTs.

GrantShares is the first DAO to launch on Neo N3, and is designed to provide financial support to smaller initiatives that do not fit the scope of Neo’s existing grant programs.

In the AMA, Muller and Machado discussed the genesis of the GrantShares project, the types of applicants the team would like to see apply for grant funding, the application process, transparency in the discussions surrounding proposals, and the future vision for GrantShares.

The full transcript can be found below:

Sef (Neo Telegram admin): AxLabs is a Swiss-based company passionate about building open-source software tools with a strong focus on blockchain, ranging from SDKs, compilers to DAOs. They joined the Neo community in 2018, and since then have kept developing and maintaining projects to provide a great Developer Experience to the ecosystem. As maintainers of the neow3j project, their focus lies in empowering other developers to build great things on Neo. They are also a Neo Council member and are happy to push Neo’s growth as maintainers of the GrantShares program and application.

Guil is a researcher, entrepreneur, and software engineer. He is a serial open-source project contributor and brings more than 20 years of experience in the software industry and academic projects. He holds a Ph.D. in Computer Science from the University of Zürich, where he also contributed to his first blockchain project in 2013. Together with AxLabs, he joined the Neo ecosystem in late 2018 and since then he has been building various tools to make the developer experience on Neo as smooth and intuitive as possible. Guil brings his passion and is constantly on the hunt to discover and materialize the next big thing in the blockchain space.

Claude is a lead software engineer, blockchain specialist, and passionate about open-source communities. He holds a M.Sc. in Computer Science from the University of Zürich, with a focus on blockchain and electronic voting. Claude is currently a senior software engineer at AxLabs, leading projects from the conceptual phase to execution. He has been working with blockchain technology for over 3 years – mainly on tools and infrastructure for the Neo Blockchain. Before joining AxLabs, he worked as a business software developer.

Claude Muller (AxLabs senior engineer): Hi all!

Guil. Sperb Machado (AxLabs founder): Hello guys!

Q1: What is GrantShares, and what purpose does it serve?

Claude: GrantShares is a grant program governed by the GrantShares DAO (Decentralized Autonomous Organization), with the goal of supporting independent projects in the Neo ecosystem. Technical projects are only one category that GrantShares wants to support. We are sure that work on marketing, community building, documentation, or tutorials is equally important to help Neo grow. Thus, such projects should also find a way to fund themselves through GrantShares.

GrantShares is designed to give the Neo community more agility to execute initiatives beyond those directly supported by the programs in Neo ecosystem support.

Technically speaking, we want the GrantShares DAO implementation to serve as an example for the implementation of DAO-related projects in the future. E.g., it is an interesting example of how to handle contract updates, which was a big topic on the Neo Discord server for the last two days.

Q2: Why is GrantShares structured as a DAO, and what does that entail?

Guil: Grants are already available through Neo Eco Support. Thus, GrantShares wouldn’t be a great addition to the community if it would simply be controlled by a single entity like Neo Foundation in the case of the Neo Eco Support. GrantShares takes a fully transparent approach with more distributed decision power.

DAO, in this case, means that there are smart contracts with a mechanism to execute on-chain proposals. The DAO members control the acceptance of these proposals. A majority of members have to vote yes on proposals for them to pass and implement. The DAO has a treasury, and proposals can spend money from that treasury. (Note, proposals can do much more than spend money from the treasury.)

I think it’s important to mention that no single entity has ownership over the GrantShares contracts. If something should be changed, e.g., parameter updates or even contract code updates, that change has to take the form of a proposal and go through the voting of the members.

Q3: How long does it take from proposal submission to actually getting the funds?

Claude: In theory, a proposal can go from submission to execution in 10 days, because the voting period is set to 7 days and the following time lock period to 3 days.

This will likely not happen in practice, though. Once you submit a proposal, it doesn’t immediately go on-chain; even if it does, it has to wait for endorsement by a member. Most of the time will be spent discussing proposals that happen before the voting period. By the way, we invite everyone to take part in proposal discussions.

Q4: Where does the GrantShares funding come from?

Guil: Initially, the Neo Foundation will fund the GrantShares treasury. They have committed to providing US $1,000,000 to GrantShares over time. Depending on the success of GrantShares, we have to explore other funding mechanisms extending their reach and incentivizing other parties to fund GrantShares treasury. In this regard, we are open to ideas!

Q5: Are non-technical proposals accepted? If yes, can you please give examples?

Claude: The Community Growth category aims at such proposals. This includes activities that widen the knowledge about Neo in society.

Society is a bit broad of a term since, e.g., my grandmother doesn’t need to know about Neo. GrantShares is interested in contributors that already have a network of prospects with an interest in technology and blockchain.

The idea is to plugin such networks into the broader Neo community or create local sub-communities interested in Neo.

The work done in such growth proposals can be manifold and ranges from organizing meet-ups, workshops, hackathons, competitions, setting up educational/academic partnerships, creating online tutorials, or regularly distributing articles on Neo to an interested network of prospects.

Check this proposal as an example: https://grantshares.io/app/details/c3c3497a49dd4247cab753fb3706bce9

Q6: What kind of voting mechanism is implemented, and what were the reasons for selecting the mechanism? Also, what steps are in place to ensure proposals are community-driven, open, and transparent?

Guil: The current voting mechanism is simple. There is a group of members that have voting rights. They are registered in the GrantShares governance smart contract, and each member has one vote per proposal.

Voting rights cannot be bought (that’s important, right?!), there is no token involved in membership, and the initial members were chosen by the Neo Foundation (initial members can be found on https://grantshares.io). The good thing is: that members can be added and removed through proposals.

Everything is, in the end, a proposal submitted to the DAO. Important to note that: the addition/removal of members through proposals is not yet supported by the dApp (frontend), but it will be added soon.

Also, there is no direct financial incentive for the members. The member’s primary incentive is the growth of the Neo ecosystem. In summary, the goal was to give voting power to a group that we know has skin in the game. The game is Neo and its growth.

Other voting models were considered but seemed either not to have the right incentives or were too complicated for the first version of GrantShares. But, the plan (part of our vision for GrantShares) is to distribute voting power to the broader Neo community in the future.

How and when that is going to happen is not decided yet. We are open to suggestions!

Let me answer the second part of the question, “what steps are in place to ensure proposals are community-driven, open, and transparent?”

While voting is restricted to GrantShares members, the proposal discussion is open to everyone. Anyone with a GitHub account can comment on proposals.

Yeah, the members could ignore the community sentiment when voting, but this would only damage their reputation and credibility (that’s why we require members with “skin in the game”).

Also, the actual intents of a proposal (i.e., the things that will be executed on-chain if the proposal gets accepted) are verifiable directly on the blockchain (bypassing the web app). So, the history of actions taken to vote and execute proposals is auditable on the blockchain.

We need the web app and the GitHub issues to make things accessible to the users and provide a platform for the discussion. It’s a matter of usability and convenience.

As a side note: updating the GrantShares contracts without anyone noticing is not possible. Contract code updates require a proposal like any other change or action taken by the GrantShares contracts.

Q7: Have GrantShares contracts been audited? And what have you done to assure the transparency of the grants program?

Claude: Yes, the GrantShares contracts have been audited by Red4Sec. The audit report can be found here: https://bit.ly/3wZ14uI.

The audit was a big part of the contract development phase with many learnings.

Regarding the second part of the question, Guil mentioned transparency in his answers above. In addition to his response, I’ll redirect you to the open-source smart contracts that can be found here: https://github.com/axlabs/grantshares-contracts.

So, the GrantShares public code is also part of the transparency.

Q8: Can you tell us the current GrantShares roadmap? What target do you want to achieve? And what will you realize in the future?

Guil: Oh, yes, the big picture! We can say that this is only the beginning of GrantShares. Besides adding more features to the web app and improving the existing experience, there are two main points that we will be working on in the future: 1) distributing decision power and 2) expanding sources for funding.

I will not elaborate on everything we have discussed internally about the first point, but I can say that we plan to include the wider Neo community into the decision process. That could be with a token-based model or something like quadratic funding and funding rounds instead of the current continuous voting process.

In both cases, the solution should include a new source of funds for the GrantShares treasury.

Quadratic funding already implies that participants bring in funds for the proposals they vote on and a token-based participation model could include, e.g., that NEO-holder participants agree to divert part of their GAS rewards into the treasury (in a Neo-wide perspective, this has the property of a tax that gets invested back into the system).

It’s a bit complicated to explain, but I think the audience understands what we’re trying to do. Otherwise, everyone is welcome to shoot questions to our GrantShares Twitter account.

Q9: Please tell us about the team working on the project! What are their backgrounds? How many of you are working on GrantShares at the moment?

Claude: I’ll start at the beginning of the ideation of GrantShares. The GrantShares idea was initially conceived by Neo News Today and got the attention of Neo Foundation and other core community members (e.g. AxLabs). The properties and design of GrantShares were fleshed out with contributions from NNT, COZ, AxLabs, and others.

The implementation and maintenance of the project are done by AxLabs. In short: We are long-term Neo community members and the creators of the neow3j devpack and SDK.

For the GrantShares project, we are working with external frontend engineers that will help us create a beautiful web app. James Weybourne did the UI design, a UI/UX designer often working with COZ. Currently, two full-time engineers are working on GrantShares, depending on availability and other tasks.

Q10: Can you explain the three main spending categories: Community Growth, Ecosystem Recruitment, and Internal Development?

Guil: First of all, I want to mention that if you have a proposal that you think doesn’t fit into one of these categories, you can still formulate and post it. Note that: like any other proposal, it must be detailed and informative! Please. Otherwise, it will have no chance of getting through the discussion phase.

Having said that, these categories should inspire project ideas in people. Instead of only mentioning technical projects, e.g., implementing a Neo SDK in a language not supported, we also want to call forward projects that grow the community. This is important and the goal.

The Community Growth category aims at that – growing the community through different activities teaching people about Neo. The Ecosystem Recruitment category is meant for small technical projects that should attract new developers into the Neo ecosystem.

For example, one scenario you can imagine, is: a new dev wants to try Neo and has a concrete project idea that can manifest as a simple application on Neo. Such a developer could ask for a GrantShares grant and thereby have an easier onboarding into Neo’s developer community. We believe this approach targets projects from members that already in the community. Often such members have ideas that they would like to try out and implement on Neo but lack the time and financial resource for.

That’s where GrantShares wants to step in and distribute funding to help and support a lively developer community.

Note: Some edits have been made for formatting and readability.

The full conversation can be found at the link below:

https://t.me/NEO_EN/246051

The post Transcript: GrantShares maintainers Guil. Sperb Machado and Claude Mueller discuss community grants appeared first on Neo News Today.