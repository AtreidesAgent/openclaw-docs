---
title: "Transcript – FutureDAO/NEL participates in NEO LIVE Telegram event"
date: 2019-09-28
url: https://neonewstoday.com/general/transcript-futuredao-nel-participates-in-neo-live-telegram-event/
tags: [General, FutureDAO, NEL, Neo Live]
source: neonewstoday
---

# Transcript – FutureDAO/NEL participates in NEO LIVE Telegram event

**Published:** Sat, 28 Sep 2019 19:26:57 +0000
**URL:** https://neonewstoday.com/general/transcript-futuredao-nel-participates-in-neo-live-telegram-event/
**Tags:** General, FutureDAO, NEL, Neo Live

---

On Thursday, September 26th, NewEconoLabs and FutureDAO founder, Yongxin (Bruce) Liu, participated in NEO Global Development’s (NGD) English NEO LIVE event. NEO LIVE is an AMA-style community event that takes place on the official NEO Telegram channel. In addition to the English events, NGD also hosts weekly NEO LIVE events in Chinese via WeChat.

FutureDAO released its whitepaper in July 2019, which outlines its design and vision to create an efficient and responsible “next generation of financing” for equity crowdfunding. By improving on previous iterations of the decentralized autonomous ICO (DAICO) model, FutureDAO aims to reduce costs and provide each project with a guaranteed market. In the FutureDAO token model, the crowdsale never ends, but the smart contract controls the project’s funding at a rate controlled by its token holders.

In the NEO LIVE AMA, Liu describes the DAICO funding and governance process, FutureDAO’s approach with the financing and seeding of projects in the gaming market, and products NEL has worked on in 2019.

The full transcript can be found below:

Songping Que: Welcome to the 9th NEO Live on Telegram! This is Songping Que from the NEO marketing team. I will be your host tonight.

As usual, I would like to repeat the background of the NEO Live initiative in case that you are new to the group. NEO Live is a marketing Initiative from NEO Global Development, to bring latest blockchain knowledge and NEO news to the community. It’s one hour live chatting every Thursday night 8pm (UTC+8) in NEO official telegram group (https://t.me/NEO_EN). NGD core teams/NEO Eco Project leaders/NEO dev community leaders/pioneering blockchain leaders will be invited to share latest technological development, industry insights with the community members.

Our guest tonight is Yongxin (Bruce) Liu. Bruce graduated from Xidian University which is a public research university directly under the Ministry of Education of China. He joined Onchain in 2016 and started his journey in blockchain ever since. So far Bruce has successfully led the design development of multiple dAPPs and internet products. He is the founder of NEL and FutureDAO.

Bruce Liu (founder of NEL and FutureDAO): Hello, everyone.

Songping: If you are familiar with NEO developer communities, you must have heard about NEL, short of NewEconoLabs. It’s established in 2017 by a group of Chinese developers. They have developed several NEO ecosystem infrastructure tools such as NNS (NEO Name Service), Teemo extension wallet, NEORay contract development tool, NEO blockchain explorer and so forth. In 2017, NEL also hosted the first NEO Game Development Competition, which promoted the ecosystem development of NEO.

FutureDAO is a creative project financing and governance platform that utilizes blockchain technology to provide incentives for early investors by implementing a sustainable financing model and a reserve funds mechanism while avoiding project fraud through on-chain funds governance. It protects investors’ rights and interests through a series of smart contracts and ultimately promotes the development of angel investment and the prosperity of creative projects.

What Bruce would like to share today is about DAICO, the next hot topic for DeFi!

So Bruce, feel free to start sharing.

Bruce: Ok, thank you.

The topic I would like to share with you today is the DAICO. The concept of DAICO was proposed by Vitalik in 2017. It is a combination of DAO + ICO and it is a better financing model.

FutureDAO is implemented in DAICO, and today I mainly share the main considerations in the FutureDAO design.

First of all, I want to ask a question. What kind of financing model is reasonable?

Let’s take a look at the traditional financing model.

Source: NEL

When a company moves from a start-up to its maturity, it is usually accompanied by multiple financing processes, from the seed round, the angel to the A, B, C… rounds, and finally to the IPO.

The risk-to-benefit ratio is different for each round. The earlier the round, the higher the risk is, the lower the price is, and the higher the return is.

Such a multi-round financing model is reasonable. In the process of the company’s growth, the company’s income and risks are continuously evaluated, and reasonable prices are given, which can effectively control the risks faced by investors.

At the same time, early investors have the opportunity to exit in the subsequent rounds, not necessarily waiting until being listed to exit.

However, the financing cost is relatively large, requiring the company to spend more resources in the financing, and it is more difficult for investors to exit.

Later, we had ICO, which once seemed to be quite successful.

Projects using ICO raise a lot of money in the early stage of the project, which is enough to support the project, and then its token quickly gets listed, investors can quickly exit through the secondary market.

Such a one-time financing method has many unreasonable features.

Compared with multiple rounds of financing, ICO does not have risk pricing based on project development. The risk of project failure at the early stage is too high and projects should not raise so much money at the early stage.

The reason why investors are willing to participate in ICO is that it has high liquidity and can exit quickly.

This can be profitable during the boom period, but in a bear market, even if it can be traded, it is a loss.

In order to create the illusion of profit, the project operator needs to pump its token price with the money they raise, rather than develop the project to make profits, which is unsustainable.

At the same time, funds are not supervised, and there are many cheating and scams. Arguably, the main reason for the success of ICO is its ultra-high liquidity.

So when we design a new financing model, we need to consider the investor’s risk-to-reward ratio, liquidity, and governance.

Let’s look back at the graph of the multi-round financing model.

Source: NEL

The rectangular area represents the financing amount. We can mathematically fit these rectangular areas and fit them into a continuous curve so that the area under the curve is equal to the sum of the rectangular areas as the picture shows.

Source: NEL

The curve can be expressed as a relational function of the price and the number of tokens issued. It has a basic feature that as the number of tokens issued increases, the issue price of tokens rises, reflecting the relationship between risk and price. We can further simplify the curve function into a slash, denoted by y=kx, y is the price, x is the token circulation, and k is the slope.

Applying such an issuance curve, a sustainable financing model can be implemented.

We can write such a token issuing function in the contract. At any time, investors can buy tokens, and the total circulation of tokens will increase. The purchase funds can be used as a liquidity reserve, allowing investors to sell tokens at any time. In the 100% reserve mode, the sell price formula is the same as the buy price. Tokens are burned and the circulated amount of tokens decreases when tokens are sold, and the token price will fall. For early investors, you can sell at the later stage with profits. The constant buying and selling process provides continuous risk pricing for the project.

Source: NEL

Therefore, the sustainable financing model can solve the investor’s liquidity problem, realize the incentives for the early investors, and realized the risk pricing for the project. As financing is continuous, it reduces the financing cost for the project.

After the financing incentives and liquidity problems are solved, what remains is the governance problem after financing.

In the 100% reserve mode, a run on the funds is more likely to occur, resulting in depletion of liquidity and affecting project development. Therefore, FutureDAO adopts a partial reserve dual token bonding curve model. For example, when buying tokens, 70% of the funds raised are used as a governance pool and 30% of funds are used as a reserve pool. At the same time, the selling price will be lower than the buying price. If you want to make a profit, you need to wait for more people to buy.

Source: NEL

The funds in the governance pool needed to be voted to determine how to use it, so the key to governance is how to deal with 51% attacks.

We use a simple majority vote, that is, we do not ask for the number of votes, and the minority accepts the majority in the result of the vote.

51% attacks are hard to be avoided, but we can increase the difficulty of 51% attacks.

When the attack accounted for 30% of the total votes, the proposal would not pass. This increases the difficulty of a 51% attack to 71%.

Under normal circumstances, most people will not participate in governance. At this time, a simple majority vote works, but when an attack occurs, the attack will spread in the community. Everyone should protect themselves with a vote in their hands. At this time, 30% NO votes will play a role.

Many governance designs include complex voting incentives, but we don’t have that. Corporate governance is not governance of public land. Corporate governance involves your own money rather than someone else’s money. The complex design brings about additional problems, such as the use of new tokens for rewards.

The purpose of governance is not to call on everyone involved in governance. The investment itself is a process of giving money to others, so we are not motivated to participate in voting. The core purpose of on-chain governance is the transparency of the use of funds, avoiding the risk of scams. NO votes is the main way for investors to vote compared with YES votes.

In addition to the 30% negative right and exits from the current reserve pool, investors can protect themselves by getting their funds refunded.

When the project is at risk, you can initiate a clearing vote to reach the threshold for clearing. For example, if 30% of the total votes approve, then investors can get refunded. When the clearing occurs, you can take the corresponding proportion of funds from the total fund pool based on your token holdings.

The refunding threshold will not be higher than 51%, which is also a check on 51% attacks. The refunding may affect the development of the project, but at least the investor’s money is protected, so the refunding is benign.

This is the main governance logic of FutureDAO.

Then the financing and governance issues have been solved, what kind of projects are suitable for such financing models?

A basic prerequisite for a project to finance is it has profit expectations. We believe that most of the financing of current blockchain projects are not based on this assumption, but based on post-listing hype expectations, which is unsustainable.

FutureDAO wishes to serve game projects, but not blockchain-based games. Because the current blockchain game user base is not enough to support the profit expectations. We hope to organize the game production through DAO, and the game itself is traditional player-oriented. Games are distributed through traditional channels such as the Steam channel to maximize profitability.

First solve the problem of financing and governance, I think this is a feasible way to combine the blockchain and traditional industries.

And the game project has light asset attributes, the development cycle is not very long, and it is easier to see the profit effect. After the end of a project cycle, everyone can exit and then continue to invest in the next project.

The game project is financed by DAICO, which not only gets funding but also gets its own seed users. To kill two birds with one stone.

For game planning, one success is to expand the boundaries of the game type, but does our commercial infrastructure support such innovation and control the risk?

FutureDAO promotes angel investment through blockchain technology to protect the rights and interests of investors and ultimately promotes the prosperity of social culture. This is what we want to do.

That’s it, thank you all.

Songping: Wow, that’s a lot of info to digest. Bruce, thanks a lot for the sharing! Everybody, it’s time for Questions now!

For anyone who wants to ask questions, to make it easy for the team to trace the question, please kindly number your questions, following the previous. Please keep the questions about NEO, NEL, and FutureDAO, we will remain the right to select the questions. Also, the team won’t make comments on the token price.

Q1: Is the governing voting system a way to keep whales away?

Bruce: I see this as a challenge to avoid the 51% attack. What we did is give 30% of the total vote a veto right, which in fact increase the difficulty from 51% to 71%.

Q2: What has NEL done in 2019?

Bruce: In addition to NNS, our blockchain browsers continue to be updated. We have done a lot of infrastructure projects this year, such as Teemo browser extension wallet, NEORay contract online development tools, and NELSwap decentralized exchange.

Q3: Does FutureDAO have financing needs?

Bruce: As a start-up project, there is naturally a need for financing. However, we haven’t decided the specific financing method, considering that many investors are not familiar with the DAICO now.

Q4: Could you tell us your thoughts on the development trend of DeFi?

Bruce: At present, the development of DeFi is mainly restricted by the infrastructure conditions. The core problem is the public blockchain’s scalability, followed by the user usability problem. These two problems are expected to be better solved in 2–3 years. There will be a huge growth in the DeFi market.

Q5: What do you think the role of FutureDAO will play in the NEO ecosystem, and what will the changes be?

Bruce: The DAICO platform can be used as a catalyst for the public blockchain ecosystem. Investment and governance are all on the chain, which is very helpful for enriching the public blockchain ecosystem. At the same time, there are many requirements for the public blockchain infrastructure, such as performance, identity scheme, reliable stable currency scheme, easy to use wallets, and more.

Q6: How do you think about DeFi’s security and compliance?

Bruce: Security is very important and is our biggest concern. Therefore, the audit of the contract is very important, and we also hope that the public blockchain and the contract programming language will continue to develop and have a safer infrastructure.

Compliance is a trend, but at the same time, the contract itself is actually a form of regulation and risk control. If we think what kind of risk control measures are needed, we can write directly in the contract. Therefore, contractually controlled investment and financing is actually regulatory friendly. Regulators should also understand the changes brought about by new technologies, rather than applying old regulatory rules, such as stipulating the most publicly funded amounts each year. We should strive for compliance, but not necessarily need to be compliant.

Songping: Okay, we are close to the end of the session now. 

Please note that there won’t be a NEO LIVE next week since we have a weeklong holiday here in China.

Our guest for October 10th is the team from Cardmaker.

Note: Some edits have been made for formatting and readability. The full conversation can be found at https://t.me/NEO_EN/25440.
                                    

The post Transcript – FutureDAO/NEL participates in NEO LIVE Telegram event appeared first on Neo News Today.