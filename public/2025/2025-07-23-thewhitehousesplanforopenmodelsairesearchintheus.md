---
title: "The White House's plan for open models & AI research in the U.S."
subtitle: "Thoughts on the new AI Action plan, American DeepSeek, and what comes next."
date: 2025-07-23
type: newsletter
audience: everyone
visibility: public
post_id: 169050741.the-white-houses-plan-for-open-models
email_sent_at: 2025-07-23T16:09:27.262Z
---
Today, the White House released its [AI Action Plan](https://www.ai.gov/action-plan), the document we've been waiting for to understand how the new administration plans to achieve "global dominance in artificial intelligence (AI)." There's a lot to unpack in this document, which you'll be hearing a lot about from the entire AI ecosystem. This post covers one narrow piece of the puzzle --- its limited comments on open models and AI research investment.

For some context, I was a co-author on the [Ai2 official comment](https://allenai.org/blog/ostp)[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"} to the Office of Science and Technology Policy (OSTP) for the AI Action Plan and have had some private discussions with White House staff on the state of the AI ecosystem.

A focus of mine through this document is **how the government can enable better fully open models to exist**, rather than just more AI research in general, as we're in a shrinking time window where if we don't create better fully open models then the academic community could be left with a bunch of compute to do research on models that are not reflective of the frontier of performance and behavior. This is why I give myself \~18 months to finish [The American DeepSeek Project](https://www.interconnects.ai/p/the-american-deepseek-project).

Important context for this document is to consider what the federal government can actually do to make changes here. The executive branch has limited levers it can pull to disperse funding and make rules, but it sends important signaling to the rest of the government and private sector.

Overall, the **White House AI Action Plan comes across very clearly that we should increase investment in open models, and for the right reasons**.

This reflects a shift from previous federal policy, where the [Biden executive order](https://bidenwhitehouse.archives.gov/briefing-room/presidential-actions/2025/01/14/executive-order-on-advancing-united-states-leadership-in-artificial-intelligence-infrastructure/) had little to say about open models other than them getting grouped into models needing pre-release testing if they were trained with more than 10\^26 FLOPS (which led to substantial discussion on the general uselessness of [compute thresholds](https://arxiv.org/abs/2407.05694v1) as a policy intervention). Later, the National Telecommunications and Information Administration (NTIA) released a [report](https://www.ntia.gov/press-release/2024/ntia-supports-open-models-promote-ai-innovation) from under the umbrella of the Biden Administration that was far more positive on open models, but much more limited in the scope of its ability for agenda setting.

This is formatted as comments in line with the full text on open models and related topics in the action plan. Let's dive in, any *emphasis* in italics is mine.

> ### Encourage Open-Source and Open-Weight AI
>
> Open-source and open-weight AI models are made freely available by developers for anyone in the world to download and modify. Models distributed this way have unique value for innovation because startups can use them flexibly without being dependent on a closed model provider. They also benefit commercial and government adoption of AI because many businesses and governments have sensitive data that they cannot send to closed model vendors. And they are essential for academic research, which often relies on access to the weights and ***training data*** of a model to perform scientifically rigorous experiments.

This covers three things we're seeing play out with open models and is quite sensible as an introduction:

1.  Startups use open models to a large extent because pretraining themselves is expensive and modifying the model layer of the stack can provide a lot of flexibility with low serving costs. Today, most of this happens on Qwen at startups, where larger companies are more hesitant to adopt Chinese models.

2.  Open model deployments are slowly building up around sensitive data domains such as health care.

3.  Researchers need strong and transparent models to perform valuable research. This is the one I'm most interested in, as it is the one with the highest long-term impact by determining the fundamental pace of progress in the research community.

> We need to ensure America has leading open models founded on American values. *Open-source and open-weight models could become global standards in some areas of business and in academic research worldwide. For that reason, they also have geostrategic value.* While the decision of whether and how to release an open or closed model is fundamentally up to the developer, the Federal government should create a supportive environment for open models.

The emphasized section is entirely the motivation behind ongoing efforts for [The American DeepSeek Project](https://www.interconnects.ai/p/the-american-deepseek-project). The interplay between the three groups above is inherently geopolitical, where Chinese model providers are actively trying to [develop mindshare with Western developers](https://www.interconnects.ai/p/latest-open-artifacts-12-qwen3-235b-a22b-instruct-2507) and release model suites that offer great tools for research (e.g. Qwen).

The document is highlighting why fewer open models exist right now from leading Western AI companies, simply "the decision of whether and how to release an open or closed model is fundamentally up to the developer" --- this means that the government itself can mostly just stay out of the way of leading labs releasing models if we think the artifacts will come from the likes of Anthropic, OpenAI, Google, etc. The other side of this is that we need to invest in building organizations around releasing strong open models for certain use cases that do not have economic conflicts or different foci.

Onto the policy steps.

> #### Recommended Policy Actions
>
> -   **Ensure access to large-scale computing power for startups and academics by improving the financial market for compute.** Currently, a company seeking to use large-scale compute must often sign long-term contracts with hyperscalers---far beyond the budgetary reach of most academics and many startups. America has solved this problem before with other goods through financial markets, such as spot and forward markets for commodities. Through collaboration with industry, the National Institute of Standards and Technology (NIST) at the Department of Commerce (DOC), the Office of Science and Technology Policy (OSTP), and the National Science Foundation's (NSF) National AI Research Resource (NAIRR) pilot, the Federal government can accelerate the maturation of a healthy financial market for compute.

The sort of issue the White House is alluding to here is that if you want to have 1000 GPUs as a startup or research laboratory you often need to sign a 2-3 year commitment in order to get low prices. Market prices for on-demand GPUs tend to be higher. The goal here is to make it possible for people to get the GPU chunks they need through financial incentives.

We've already seen a partial step for this in the recent budget bill, where [AI training costs now can be classified as R&D expenses](https://x.com/tamaybes/status/1940983352087269430), but this largely helps big companies. Actions here that are even more beneficial for small groups releasing open weight or open-source models would be great to see.

One of the biggest problems I see for research funding is going to be the challenge of getting *concentrated* compute into the hands of researchers, so I hope the administration follows through here for compute density in places. A big pool of compute spread across the entire academic ecosystem means too little compute for models to get trained at any one location. It reads as if the OSTP understands this and has provided suitable guidance.

> -   **Partner with leading technology companies** to increase the research community's access to world-class private sector computing, models, data, and software resources as part of the NAIRR pilot.
>
> -   **Build the foundations for a lean and sustainable NAIRR operations capability** that can connect an increasing number of researchers and educators across the country to critical AI resources.

This is simple and to my knowledge has largely been under way. NAIRR provided a variety of resources to many academic parties, such as API credits, data, and compute access, so it should be expanded upon. I wrote an entire piece on [saving the NAIRR](https://www.interconnects.ai/p/saving-the-nairr) last November when its funding future was unclear (and needed Congressional action).

This is the balance to what I was talking about above on model training. It provides smaller resource chunks to many players, which is crucial, but doesn't address the problem of building great open models.

> -   **Continue to foster the next generation of AI breakthroughs** by publishing a new National AI Research and Development (R&D) Strategic Plan, led by OSTP, to guide Federal AI research investments.

This seems like a nod to a logical next step.

Where the overall picture of research funding in the U.S. has been completely dire, the priority in AI research has already been expressed through AI being the only area of NSF grant areas without major cuts. There is likely to be many other direct effects of this, but it is out of scope of the article.

More exact numbers can be found in the [NSF 2026 proposed budget](https://nsf-gov-resources.nsf.gov/files/00-NSF-FY26-CJ-Entire-Rollup.pdf?VersionId=O06XnbgojADDf9uCPe_MIkjRPBScU1Lt), where AI is an outlier as one of the only topics with a positive net change from 2024 or 2025.

![](images/169050741.the-white-houses-plan-for-open-models_9fc65b49-8841-468f-a798-40cb73ba892e.png)

> -   **Led by DOC through the National Telecommunications and Information Administration (NTIA),** convene stakeholders to help drive adoption of open-source and open-weight models by small and medium-sized businesses.

This is a more unexpected line item, but a welcome one. It'll be harder to implement, but if it works it'll do a lot of good for building momentum around open model investment. A large part of why few open models exist in the U.S. is just because there's not a lot of business value from releasing them. A big story of 2025 has been how [open models are closing the gap in capabilities](https://www.interconnects.ai/p/gemma-3-olmo-2-32b-and-the-growing), or at least crossing important ability thresholds, which could start to change this equilibrium.

That's it for the core section on open models! It's right to the point.

There are a couple related sections I wanted to point you to, which largely complement the above or show how it is hard for a document like this to acknowledge things like "our R&D ecosystem is being outcompeted by Chinese models."

First, more on AI research itself.

> ### Advance the Science of AI
>
> Just as LLMs and generative AI systems represented a paradigm shift in the science of AI, future breakthroughs may similarly transform what is possible with AI. It is imperative that the United States remain the leading pioneer of such breakthroughs, and this begins with strategic, targeted investment in the most promising paths at the frontier.
>
> #### Recommended Policy Actions
>
> -   Prioritize investment in theoretical, computational, and experimental research to preserve America's leadership in discovering new and transformative paradigms that advance the capabilities of AI, reflecting this priority in the forthcoming National AI R&D Strategic Plan.

Something in my mind that is very missing from this document is a comment on immigration. If we want the U.S. to be a leader in AI research we need to prioritize fixing the immigration ecosystem as soon as possible. Leading AI conferences [can no longer be located solely in the U.S.](https://x.com/natolambert/status/1945632827032121491) because too many authors cannot get a travel visa in time to attend the conference, let alone the other issues on hiring or funding at academic institutions.

This section on the Science of AI reads very similar to the section on open models.

And the only mentions of China, which is related as the party pushing open models the furthest today:

> ### Counter Chinese Influence in International Governance Bodies
>
> A large number of international bodies, including the United Nations, the Organisation for Economic Co-operation and Development, G7, G20, International Telecommunication Union, Internet Corporation for Assigned Names and Numbers, and others have proposed AI governance frameworks and AI development strategies. The United States supports likeminded nations working together to encourage the development of AI in line with our shared values. But too many of these efforts have advocated for burdensome regulations, vague "codes of conduct" that promote cultural agendas that do not align with American values, or have been influenced by Chinese companies attempting to shape standards for facial recognition and surveillance.
>
> #### Recommended Policy Actions
>
> -   Led by DOS and DOC, leverage the U.S. position in international diplomatic and standard-setting bodies to vigorously advocate for international AI governance approaches that promote innovation, reflect American values, and counter authoritarian influence.

and a quick comment on Chinese talking points in the section "Ensure that Frontier AI Protects Free Speech and American Values":

> -   Led by DOC through NIST's Center for AI Standards and Innovation (CAISI), conduct research and, as appropriate, publish evaluations of frontier models from the People's Republic of China for alignment with Chinese Communist Party talking points and censorship.

This reads as there being a low probability that we see any immediate executive action trying to ban the likes of Qwen or DeepSeek, which is good for the time being. The evaluation of Chinese and American values is a slippery slope in some ways, as it quickly will become enmeshed in the idea of "woke AI," but in the meantime it is likely to be a major talking point with respect to the open models we're seeing from Chinese companies, which do often parrot very simple talking points reflective of "[Chinese socialist values](https://x.com/natolambert/status/1945959796382859372)."

We need our ecosystem to compete on merits of the technology being better at useful tasks if we want to lead in the long-term technological arc, rather than political games. That's [my number one focus](https://www.interconnects.ai/p/the-american-deepseek-project) over the next couple of years and why I reiterate the need for open models for fundamental AI research and innovation. The biggest beneficiaries of this sort of innovation have historically been the biggest American technology companies, who now should do their part to support them existing --- with some government encouragement.

Let me know if I missed anything, as this was a quick pass to make sure I read the details and connected the recent dots.

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
The call for comments was here: https://www.whitehouse.gov/briefings-statements/2025/02/public-comment-invited-on-artificial-intelligence-action-plan/
:::
::::
