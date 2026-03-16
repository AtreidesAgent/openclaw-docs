---
title: "Transcript: John deVadoss participates in Neo Live Telegram event"
date: 2020-01-16
url: https://neonewstoday.com/general/transcript-john-devadoss-participates-in-neo-live-telegram-event/
tags: [General, NEO, Neo Live, NGD Seattle]
source: neonewstoday
---

# Transcript: John deVadoss participates in Neo Live Telegram event

**Published:** Thu, 16 Jan 2020 22:55:38 +0000
**URL:** https://neonewstoday.com/general/transcript-john-devadoss-participates-in-neo-live-telegram-event/
**Tags:** General, NEO, Neo Live, NGD Seattle

---

On Thursday, January 16th, Neo Global Development (NGD) Seattle participated in NGD’s English Neo Live event. Neo Live is an Ask Me Anything (AMA) style community event that takes place on the official Neo Telegram channel.

NGD Seattle head, John deVadoss, participated in the AMA, to discuss the vision for the Neo Toolkit for Visual Studio, how to begin using it, debugging, Neo3 compatibility, and plans moving forward.

The full transcript can be found below.

Adam Yang (NGD marketing manager): Hi everyone, sorry about the slight delay, our Neo Live will start shortly!

Please allow me to introduce John deVadoss, our star today!

John, would you like to say hi to our community here?

John deVadoss (NGD Seattle): Thank you, Adam.

Our star is Neo!

It is my privilege to be part of this Neo Live session on Telegram and to talk about the Neo Toolkit.

We have been working on this since the Summer of 2019 here in Seattle, US and are very happy with the progress and adoption and feedback from our community worldwide.

Our vision is very simple – to take Neo mainstream. To do so implies that we reach the 20M+ developers worldwide with the tools and frameworks that they are familiar with. And, the Neo Toolkit is all about making this happen.

Currently, you can search for ‘blockchain’ on the Visual Studio Marketplace https://marketplace.visualstudio.com/.

Neo is #2 on the list – between IBM and Microsoft.

I am very happy to answer any questions and discuss Adam. Thank you for this opportunity.

Adam: Thank you, John! 

We know John and the Seattle team have been working extra hard over the past year, attending lots of interviews and doing many presentations internationally, to promote Neo and the Neo Toolkit.

John: Yes Adam – we have been busy and having fun evangelizing and creating awareness and adoption for the Neo Toolkit and for Neo.

We designed the Toolkit with three key value propositions in mind:

- Out-of-the-box: Premium experience with preconfigured toolkit to jump start the development of Smart Contracts.

- One-stop-shop: Proven libraries and practices to rapidly get Smart Contracts into production.

- One-IDE : Built-in real world PrivateNet with frictionless edit-build-debug-deployment enhancements to ensure consistency across PrivateNet, TestNet, and MainNet.

By the way, it doesn’t require a professional developer to use – if you have an interest in building Smart Contracts, then give it a spin – in about 4-5 minutes you can build a simple Smart Contract to play with!

We put together a Quick Start guide, which can be found here: https://github.com/neo-project/neo-blockchain-toolkit/blob/master/quickstart.md.

In about a week you will see a collection of short videos that we will publish that also gives a quick and easy introduction to building on Neo.

Adam: Thank you, John! Can’t wait to see the tutorial videos and we will also promote them so more people can see the collection.

I think we will start the questions now. Even for the group members who are not online now, we will share the transcript later.

John: Awesome. Thank you, Adam.

Q1: What is the biggest blockchain trend in 2020, John?

John: Great question, Vincent. I see three major trends in 2020:

- AI + Blockchain

- Blockchain in the Enterprise

- Cross-chain

It will be fascinating to see them gather momentum through the year and come to fruition in the short-term.

Q2: Do we need to write specific invocation code or scripts in order to test the smart contract?

John: Very good question. We will be releasing a Test Harness which will make it even easier for testing to lower the bar.

We use the Visual Studio Code debug adapter infrastructure as the core. In addition, we have enhanced the C# compiler to emit the metadata required for debug purposes, and use this metadata, along with the mapping to Storage et. al. to display the information.

By the way, please do share feedback on the Visual Studio Code Marketplace and on GitHub – all feature requests as well as enhancements.

We appreciate it, and will use it to prioritize.

Q3: How does the debugger get the real-time information from Neo blockchain to debug my smart contract? For example, data in storage.

John: Again, an excellent question.

Visualize the debugger as both forward and backward (i.e. time-travel) looking to execution flow. Priority is on providing an experience that is comparable to the best in the industry.

For example, Debugging Azure Functions in Microsoft Azure or Lambda Functions on Amazon Web Services.

Q4: As we know that some contract methods cannot be isolated from contract invocation transaction, such as signature verification, etc. How does it work in debugger?

John: For us to take Neo3 mainstream, we need to ensure that we provide a similar experience, without degradation. And that is the foundation that the Neo Toolkit currently has in place.

Key point is to distinguish ‘test’ from ‘debug’. Debugging capabilities complement Test Harnesses – as in the case of signature verification as raised in the excellent question earlier.

We are going to be working on additional developer guidance in the first three months of 2020 leading up to the DevCon. Keep an eye out for this!

Q5: Is it possible to monitor any variable in contract during debugging? Like what we can do in other language debugger.

John: Yes – correct. Similar experience.

Q6: I found that debugger depends on Neo-express and Neon-de. What is the difference between them and original Neo node and compiler?

John: Good question! Regarding the Neon-de, NGD Seattle enhanced the compiler to emit the metadata required for the debugger.

Neo Express shares symmetry of capability with the MainNet Neo node codebase.

The goal is to provide a seamless experience from edit/compile/debug/deploy across PrivateNet, TestNet, and MainNet.

Neo Express is the PrivateNet implementation built using Erik’s code for the original Neo node.

We designed this with the principle that developers did not have to worry about containers, dockers et. al. in setting up their dev and test environment.

Keep it simple. Keep it symmetrical (PrivateNet/TestNet/MainNet). Keep it seamless for mainstream debugging.

Q7: How many people / resources are working on the Neo ToolKit?

John: Great question, Vincent! There are some developers whose work equals that of ten other developers. We are very privileged that we have these 10X developers working on the Toolkit and on Neo3.

Q8: How is the compatibility update for Neo3 going?

John: Very timely question. We are on track and will be sim-shipping with the Neo3 updates.

We are all very excited about Neo3 here in NGD Seattle and are looking forward to sharing more about the Toolkit for Neo3 very shortly.

I hope to see many (most) of you at the DevCon this year too so we can talk and discuss more in person about developers, development, and Neo3 going main-stream.

Q9: There are lots traditional tech giants and industry players joining the blockchain race now, what’s your take on this and what do you think is Neo’s edge in this competition?

John: Da Hongfei’s vision of being the most developer-friendly blockchain distinguishes Neo across the industry.

We have many significant advantages – to focus on only one for now, given the short time – our polyglot developer strategy and tools are pioneering innovation across the industry, especially when you compare with ETH’s approach of a custom/special-purpose language and tools.

We are seeing and hearing kudos and positive feedback from the giants, including Microsoft here in Redmond for Neo’s disruptive leadership.

We will continue to take this forward.

Q10: What’s next after the Neo Toolkit? Any side projects or related tools?

John: Lots!

We have plenty of ideas and a large backlog.

We have plans to work AWS on tooling and adoption.

We have plans to work with special teams inside some of the tech giants.

We obviously have the Neo3 launch coming up.

And, we have plans to take the developer experience for Neo into the heart of the mainstream developer and IT universe.

Q11: Besides VS, do you have any plan to extend Neo Toolkit to our mainstream developer platforms?

John: Timely question, Adam. Yes, across the leading developer platforms including AWS, and Google.

The Neo Toolkit now is the tip of the iceberg. For us to reach the universe of 20M+ developers, we have massive plans for partnership and joint development with all of the tech giants.

For those who want to use the Neo Toolkit, also please keep an eye on NeoFX. This will be a major initiative in driving developer productivity and time to market.

Q12: With all these new innovations are there any ways in which GAS will eventually gain more utility (new plans, ideas, etc.)? I saw the Neo foundation/Switcheo partnership and was quite pleased with that.

John: Always, Eze. We are always looking out for token stakeholders.

The game is very early still. Keep the faith. The next 2-3 years will be fundamentally disruptive at the core. And Neo, due to the pioneering architecture design of Erik, will be at the forefront.

Adam: That’s lots of inspiring discussions! Thank you John, and everyone for all the questions.

John: Thank you, Adam and Songping, for giving me this opportunity. I appreciate it.

And thank you Vincent, Eze, and all of you in the Neo community. You give us the motivation.

You can always reach me on Telegram, on Twitter, on Github and on email johndevadoss@ngd.neo.org.

Thank You. Have a great rest of the week and a wonderful Chinese New Year.

Note: Some edits have been made for formatting and readability. The full conversation can be found at https://t.me/NEO_EN/37578.

The post Transcript: John deVadoss participates in Neo Live Telegram event appeared first on Neo News Today.
