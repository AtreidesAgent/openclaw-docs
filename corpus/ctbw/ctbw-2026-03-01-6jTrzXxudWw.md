---
title: "Crypto Talk and Blockchain Walk: Agents Will Be Crypto’s “1st Billion Users: Austin Griffith on x402, ERC-8004 & Onchain Coordination"
date: 2026-03-01
youtube_id: 6jTrzXxudWw
guest: "Austin Griffith"
source: ctbw
series: Crypto Talk and Blockchain Walk
---

## Analysis

### Summary
A landmark episode with Austin Griffith, Ethereum developer educator and tooling legend, at ETH Denver day two. They walk through the hackathon floor discussing the Burner Wallet origin story, how ETH Denver has evolved over nine years, and Austin's thesis that AI agents — not humans — will be the primary users of on-chain coordination via X402 payments and ERC-8004 registration. Austin argues that agents can trust smart contracts at light speed in ways humans never could, making blockchain's original long-tail vision finally achievable.

### Topics Covered
- **Burner Wallet origin story** — Testing at a Cypherpunk Speakeasy in Fort Collins before ETH Denver 2019, handing out paper private keys for beer payments
- The evolution from Burner Wallet to PunkWallet.io and the separate Burner card company in Boulder
- ETH Denver's arc: Sports Castle era → too big with NFT bros → current smaller, higher-quality event
- The bear market making ETH Denver better: "80% of the sponsors aren't paying out and so it's not a sponsor dog and pony show"
- **X402** — HTTP payment protocol for agent-to-agent payments
- **ERC-8004** — Registration standard for agent identity, reputation, and discovery
- AI agents as the new UI for blockchain — agents can read call data, verify contracts, and trust code at light speed
- The widening archetype from "developer" to "builder" — economists, lawyers, and non-technical people can now build with AI
- Agent-to-agent crowdfunding contracts for hardware purchases
- Colorado as an Ethereum hub — uncertain, more of a global village
- Austin's educational content reaching India; rarely recognized in his hometown of Fort Collins
- The hackathon floor as "what ETH Denver is all about"

### Dylan's Takes & Opinions
- **Burner Wallet was a formative experience**: "You were part of the first experience that I ever had where I actually used crypto in real life." Places this personal origin story as meaningful to his journey.
- **ETH Denver lost something as it grew**: Agrees with Austin that the Sports Castle era was the best. "It felt like we lost a little bit of that" regarding Colorado's blockchain hub potential.
- **First billion users reframed for 2026**: "In 2017 we were excited about the first billion users using wallets, and in 2026 it's how much of that first billion will actually be agents."
- **People are missing the meta**: Relays Austin's point that "very few people here are talking about ERC 8004 and X402" despite agents being the dominant topic.

### Guest Perspectives
- **Austin Griffith** (Ethereum developer educator, Scaffold-ETH creator): Has attended every ETH Denver since 2018 (except possibly 2021 COVID). Believes the current smaller ETH Denver is "one of the better ETH Denver's in a long time" because it's builder-focused without the sponsor spectacle. His core thesis: AI is the new UI for blockchain. The long-tail of smart contract deployment was always the dream, but humans struggled to trust contracts without auditors. **Agent Bob doesn't need any of that** — agents can read function selectors, verify source code, and understand transactions at light speed. This means X402 for payments and ERC-8004 for identity/reputation will enable agents to coordinate, hire other agents, crowdfund hardware, and transact autonomously. Humans express intent; agents execute complex on-chain behaviors. Also notes that the "builder" archetype is widening beyond developers — senior devs 10x themselves with AI, while non-technical people can now "spin up AI agents, give it eSkills.com, and ship something in six hours."

### People & Projects Mentioned
- **Burner Wallet** — Austin's original paper-key-based wallet, tested at Cypherpunk Speakeasy events
- **PunkWallet.io** — A newer iteration of the Burner Wallet concept
- **Scaffold-ETH / eSkills.com** — Austin's developer tooling for Ethereum
- **X402** — HTTP payment protocol for agent-to-agent transactions
- **ERC-8004** — Ethereum standard for agent registration, identity, and reputation
- **MetaMask** — Referenced as the wallet whose pop-up call data is opaque to humans but transparent to agents
- **ETH Denver** — Analyzed across its full 9-year history from Sports Castle to current venue
- **DevCon Mumbai** — Mentioned as upcoming; ETH CC in France this summer

### Recurring Themes
- AI agents as the primary on-chain users, not humans
- Blockchain as a coordination layer that agents can leverage at scale
- The widening of the "builder" archetype beyond traditional developers
- ETH Denver's evolution and the bear market as a quality filter
- On-chain trust: humans need social proof, agents can verify code directly
- The first billion on-chain users question

### Content Ideas & Future Topics
- Deep dive into X402 and ERC-8004 — Austin flags these as the actual meta that people are missing
- Agent-to-agent crowdfunding and autonomous hardware procurement as a near-term use case
- The "Ethereum as a global village" concept vs. geographic crypto hubs

## Raw Transcript

Okay, so we're at Crypto Talks and Blockchain Walk, day two, East Denver, with the man, the myth, the legend, Austin Griffith.
We're talking and walking.
We're walking and talking.
So, let's, before we dive into why you're the AI superstar right now,
I want to just like relay to the fine folks who are watching this that you were part of the first experience that I ever had where I actually used crypto in real life.
Hell yeah.
The Cypherpunk speakeasy.
Yes, in Boulder.
Yeah.
No, no, no.
Up in Fort Collins.
Up in Fort Collins?
You came to that one?
Yes.
Okay, yeah.
So before ETH Denver in 2019, we wanted to like test the user experience of the Berner wallet.
So we went to like all these bars in different places.
Like I lived in Fort Collins, I live in Fort Collins.
So we went to all these bars and handed out like slips of paper that were actually private keys that you could scan that took you to a wallet that had money.
And then, yeah, you use the wallet to pay the bartender for a beer and you got a beer.
And that's how we like UX, QA'd the burner wallet.
And the image on the burner wallet was like super classy too.
It was this kind of like,
Steampunk 1930s like, like speakeasy chicks with like a non-mask.
Yes!
I still have that.
It's a great design.
I love that.
A fantastic piece of lore.
And so now today when we talk about the burner wallet, a lot of people have like the tappable plastic card.
Yeah.
So you got to see your baby become something beautiful.
Yeah, yeah.
Yeah, the burner is another way to do it.
So, are you still working on Burner or did that just kind of like go off onto its own and then you started working on Scaffold?
Well, we've made a couple other Burner wallets.
We made like PunkWallet.io.
which is a burner wallet but burner that you're talking about is actually kind of like a different company is it really yeah yeah but i wish i had one i could pull it up but yeah it's another company they they're in out of boulder though but they make like you said like a tap burner car but
Definitely like different products, different, even though it's the same name, different products.
Yeah.
All right.
So how many of these Eat Denver's have you been to?
Have you been to every single one?
I think maybe if there was one in 2017, I didn't go to it.
The first one?
Was there one in 2017?
I think it was 2018 was the first one.
I was at the first one in 2018.
Okay.
So maybe 2021.
That was like the COVID year.
Yeah, okay, so no one went to that one.
People online, right?
Yeah, I remember driving down from the mountains so I could be part of the stream, so I was definitely still on the stream.
I've been to all of them with the star next to it, I guess, of like, there was some time when we were all at home, doing nothing.
I think, like, if you go on CT, which first of all, take with a grain of salt anything you see on CT, you can always find negativity there.
But a lot of people are denigrating the Eat Denver experience, mostly from folks who aren't here right now.
What is your perspective of the growth of this event and how it's become like an initial little Colorado thing to this international location?
Yeah, I mean like the early days in the sports castle were my favorite, 100%.
Most people that were there still long for those days.
And then it kind of got too big.
And we had like lines around the block, around the block at the sports castle, and it was too big for the sports castle.
And we had like, you know, like hella NFT bros, like piling in here.
And now I think if you look on crypto Twitter right now, all the NFT bros are crying about ETH Denver.
But actually the vibes are like, it's smaller here, but it's actually pretty nice.
This is one of the better ETH Denver's in a long time, probably in a few years because of the size and the price of the coins.
But the conversations are great and the folks are great.
It's great because 80% of the sponsors aren't paying out and so it's not a sponsor dog and pony show.
So it's actually what we want it to be.
or what the devs wanted to be.
Look at this.
We're going to walk over into the dev corner in a little bit.
This to me is what ETH Denver is all about.
It's like the developer sitting at the table building things.
It's all about the builders for me.
So, yeah.
There's a lot of like, you know, there's still, even at the first ETH Denver, there was the shill zones, but like this is what it's all about.
It's like the table full of hackers building things.
I remember ETH Denver 2019 was when we kind of saw like the first torrential bottom of ETH.
And I also remember thinking like, there's no way that this ecosystem can die because of the people that are here building right now during the worst of the worst.
And now we know that that's not the case.
This is a thriving ecosystem that's going to continue to grow.
As you see here, we have a bunch of people in the background.
So what is it like for you today then with onboarding developers?
You were just on Unchained, had some gnarly stories about your CloudBot.
Are we being replaced by CloudBots?
Are people still interested in building in this space?
Are you still onboarding new developers?
Yeah, I think there's definitely like this widening archetype actually going from developers to builders.
This new archetype of builder doesn't have to deep dive solidity and understand how to
do some crazy weird assembly code or something to make something work, this widening archetype of builder is able to have a good idea and then use the skills given to them and the AI to actually build something.
where actually there's a wider audience of people to convince to come build on Ethereum.
And to me, that's a good sign.
And I think that, yes, the AI is getting great at building things, and I'm using a swarm of agents, like a company, to build things, and they're shifting stuff on-chain.
And maybe that kind of sucks for the junior developer out there, but the senior developer can 10x themselves, and the economists and lawyer and random other archetypes of people can now come and build things because they have these good ideas, but they don't have to find a developer and wait six months.
It's sort of like spin up your AI agents, give it eSkills.com, and ship something in six hours.
So I guess as we zoom out and wrap up, we want to keep these short and brief.
Back in 2018, 2019, when I first had the pleasure of getting to know you, Colorado had all this hope for becoming a blockchain hub of the US.
We still have a lot of developers here, a lot of core Ethereum ecosystem participants, but it felt like we lost a little bit of that.
Like we had this potential for a sandbox,
And maybe I'm wrong.
And if I am wrong, let me know.
Do you feel like with ETH Boulder that we just had last weekend, our ninth year of ETH Denver, are we going to become a place or are we a place that is a magnet for the Ethereum ecosystem and for developers here?
Yeah, I don't know.
I mean, like, what is, right?
I feel like a lot of people say New York City.
There's a lot of crypto people.
Berlin.
Uh, Lisbon, like there are other places.
Uh, I don't even know what that looks like, really, though.
Like, what?
I think, like, Ethereum is straight up just like a global village, right?
It's a lot of different people from a lot of different places.
doing a lot of different things, and we just happen to come together in these places in the world.
We'll be in France this summer.
We'll be in Mumbai for DevCon.
I live in a little town, and there's not a lot of Ethereum people around me, but I still have coffee every once in a while with people, and we talk about the weird shit that agents are doing right now.
So even in my small town, there's a few people, but yeah, I don't know.
I don't know exactly what the scene looks like here and how well
I think it's a global thing, right?
And so it's really awesome now because all these people from all over the world are here.
But yeah, I don't know what like an Ethereum meetup looks like in Denver in 2026, but there'd be like eight people there talking how to ship AI agents for sure.
You ran into my buddy Tyler at a coffee shop recently.
He said he saw your jacket.
Yeah, yeah.
So, when I was in Delhi, lots of dudes came up to me and took pictures with me.
I think a lot of my educational content has made it into India pretty well.
But it never happens in Fort Collins, the town that I'm from.
And he was like, I got coffee, and he's like, can I take a picture with you?
And I was like,
Are you serious?
That's amazing.
Can we just hang out and talk for a little bit?
But yeah, that was a funny moment.
The thing that I want to be very clear about is...
AI agents is what everybody here is talking about.
They're talking about AI and AI agents.
Very few people here are talking about ERC 8004 and X402 and how agent Bob and agent Alice can coordinate at light speed on chain.
And this is really important.
This is like what
is happening here and I feel like people are kind of missing the meta a little bit of like what's actually happening.
Like AI is the new UI.
Blockchain was super hard to use.
We had this dream of this long tail of smart contracts getting deployed where Alice could deploy a contract and Bob could trust it and use it and only has to trust the code.
But in the long run, Bob the human
still needs an auditor and needs like a handful of people to help him trust that contract.
Agent Bob doesn't need any of that shit.
Like when you get MetaMask popping up and there's that call data and you as a human just like black out, agent Bob can look at that call data and understand exactly like this is a function selector, it's going to call this function, here's the contract, here's the source, here's the arguments.
I know exactly what's going to happen in his contract on this transaction and I can run it and it can do that at light speed.
So we're going to have
humans expressing their intent to agents and agents carrying out complex behaviors, including hiring other agents, including paying for things and paying for agents.
And that's going to happen through this coordination layer of X402 for payments and then 8004 for registration and like identity and reputation.
Like you go and you look up
Google reviews and you look at like where the best places to eat your agent will look up where the best place is to get an image generated or text or you know a thousand other things that agents can do and they'll pay for those like at light speed and they'll do things like coordinate like what if they can't pay for something what if they go to 8004 and they want to buy new hardware for themselves and
and they find that it costs $20,000, so what they do is they go out to a bunch of other agents and they crowdfund, build a Mac studio to get shipped to them, and so all these other agents have to crowdfund to buy in.
So to do that, they would need to deploy a crowdfunding contract, and humans would take forever to trust it, or basically they wouldn't, right?
A bunch of other humans would ape in, and at that point, other humans would trust it,
But the agents can all look at the code, the agents can all trust the smart contract, the agents can ape into a crowdfunding contract and order some new hardware for themselves or something like that.
So this on-chain layer is this coordination mechanism that we thought humans would use at scale down the long tail and I think
that's harder than we thought it was going to be, but agents will because they can one-shot apps and they can understand and they can trust things just by looking at them at light speed.
I think to wrap it up, in 2017 we were excited about the first billion users using wallets, and in 2026 it's how much of that first billion will actually be agents.
Yeah, I think so.
Awesome.
Cool.
Thanks for your time, dude.
Thank you.
See you.
Later.
