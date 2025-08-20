---
title: "The American DeepSeek Project"
subtitle: "What I think the next goal for the open-source AI community is."
date: 2025-07-04
type: newsletter
audience: everyone
visibility: public
post_id: 167320130.the-american-deepseek-project
email_sent_at: 2025-07-04T12:03:08.013Z
---
While America has the best AI models in Gemini, Claude, o3, etc. and the best infrastructure with Nvidia it's rapidly losing its influence over the future directions of AI that unfold in the open-source and academic communities. [Chinese organizations are releasing the most notable](https://www.interconnects.ai/p/latest-open-artifacts-11-visualizing) **[open](https://www.interconnects.ai/p/latest-open-artifacts-11-visualizing)** [models and datasets](https://www.interconnects.ai/p/latest-open-artifacts-11-visualizing) across all modalities, from text to robotics or video, and at the same time it's common for researchers worldwide to read far more new research papers from Chinese organizations rather than their Western counterparts.

This balance of power has been shifting rapidly in the last 12 months and reflects shifting, [structural advantages that Chinese companies have with open-source AI](https://interconnect.substack.com/p/chinas-structural-advantage-in-open) --- [China has more AI researchers](https://finance.yahoo.com/news/nvidia-ceo-jensen-huang-sounds-035916833.html), data[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}, and an open-source default.

On the other hand, America's open technological champions for AI, like Meta, are "[reconsidering their open approach](https://www.nytimes.com/2025/06/27/technology/mark-zuckerberg-meta-ai.html)" after yet another expensive re-org and the political environment is dramatically [reducing the interest of the world's best scientists in coming to our country](https://www.noahpinion.blog/p/america-needs-its-foreign-students).

It's famous lore of the AI industry that much of the flourishing of progress around ChatGPT is downstream from Google Research's, and the industry's writ-large, practice of openly sharing the science of AI until approximately 2022. Stopping this practice, and the resulting power shifts mean it will be likely that the next "Transformer"-style breakthrough will be built on or related to Chinese AI models, AI chips, ideas, or companies. Countless Chinese individuals are some of the best people I've worked with, both at a technical and personal level, but this direction for the ecosystem points to AI models being less accountable, auditable, and trustworthy due to inevitable ties to the Chinese Government.

The goal for my next few years of work is what I'm calling ***The American DeepSeek Project*** **--- a fully open-source model at the scale and performance of current (publicly available) frontier models, within 2 years.**[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"} A fully open model, as opposed to just an "open weights" model, comes with data, training code, logs, and decision making --- on top of the weights to run inference --- in order to distribute the knowledge and access for how to train AI models fully.

This project serves two goals, where balancing the scales with the pace of the Chinese ecosystem is only one piece:

1.  Reclaim the AI research default home being on top of American (or Western) technologies and tools, and

2.  Reduce the risk that the only viable AI ecosystem for cutting edge products is built atop of proprietary, closed, for-profit AI models.

![](images/167320130.the-american-deepseek-project_2cd5defe-11b1-4506-ba12-182b41aed456.png)

More people should be focused on this happening. A lot of people talk about how nice it would be to have "open-source AGI for all," but very few people are investing in making it reality. With the right focus, I estimate this will take \~\$100M-500M over the next two years.[3](#footnote-3){#footnote-anchor-3 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

Within the context of recent trends, this is a future that has a diminishing, minute probability. I want to do this at [Ai2](https://allenai.org/), but it takes far more than just us to make it happen. We need advocates, peers, advisors, and compute.

The time to do this is now, if we wait then the future will be in the balance of extremely powerful, closed American models counterbalancing a sea of strong, ubiquitous, open Chinese models. This is a world where the most available models are the hardest to trust. The West historically has better systems to create AI models that are trustworthy and fair across society. Consider how:

-   Practically speaking, there will never be proof that Chinese models cannot leave vulnerabilities in code or execute tools in malicious ways, even though it's very unlikely in the near future.

-   Chinese companies will not engage as completely in the U.S. legal system on topics from fair use or non-consensual deepfakes.[4](#footnote-4){#footnote-anchor-4 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

-   Chinese models will over time shift to support a competitive software ecosystem that weakens many of America and the West's strongest companies due to in-place compute restrictions.

Many of these practical problems cannot be fixed by simply fine-tuning the model, such as Perplexity's R1-1776 model. These are deep, structural realities that can only be avoided with different incentives and pretrained models.

My goal is to make a fully open-source model at the scale of DeepSeek V3/R1 in the next two years. I've been starting to champion this vision in multiple places that summarizes the next frontier for performance on open-source language models, so I needed this document to pin it down.

I use scale and not performance as a reference point for the goal because the models we're collectively using as consumers of the AI industry [haven't really been getting much bigger](https://www.interconnects.ai/i/166556899/scaling-parameters-is-going-to-go-very-slow-for-consumer-models). This "frontier scale" is a ballpark for where you've crossed into a very serious model, and, by the time a few years has gone by, the efficiency gains that would've accumulated by then will mean this model will far outperform DeepSeek V3. The leading models used for synthetic data (and maybe served to some users) will continue to get bigger, but not as quickly as capabilities will grow and new types of agents will emerge.

The terminology "American DeepSeek" is stretching words in order to be identifiable to a broad public. It combines the need for true American values with a breakthrough open release that marks a new milestone in capabilities.

DeepSeek is known for many things to the general public --- [training cheap frontier models](https://www.interconnects.ai/p/deepseek-v3-and-the-actual-cost-of), [bringing reasoning models to consumers](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1), and [largely being the face of Chinese AI efforts](https://www.interconnects.ai/p/what-people-get-wrong-about-the-leading?utm_source=publication-search). Since ChatGPT, DeepSeek is the first organization to release an open, permissively licensed AI model at the frontier of performance. This was a major milestone and the name DeepSeek will forever be known in AI lore for it. It contributes to why [2025 has been a transformative year](https://www.interconnects.ai/p/gemma-3-olmo-2-32b-and-the-growing?utm_source=publication-search) in the perception of feasibility for open models generally --- many viable products exist (at least partially) on current Llamas, Qwens, or DeepSeeks, but the companies building these are banking on the models getting better!

At the same time, what will count as a "DeepSeek moment" is changing. The new directions for where AI is heading is [more in line with agents that use models a lot](https://www.interconnects.ai/i/166556899/progress-on-agents-will-be-higher-variance-than-modeling-was-but-often-still-extremely-rapid) (sometimes even *smaller* models) rather than relying on scaling performance of single model generations.

This changes what it'll mean for models to be "at the frontier." More releases will look like [Claude 4](https://www.interconnects.ai/p/claude-4-and-anthropics-bet-on-code?utm_source=publication-search) and be about usability, where the benchmarks that people are hillclimbing on represent new types of capabilities or outlandish, harder than human expert tasks. For the suite of tasks that were core for the current generation of models: MATH, GPQA, SWE-Bench Verified, etc., solving them represents a challenging, but reasonable, baseline for human performance.

The next major milestone will be when fully open-source models reach this performance threshold. With fully open-source models at this level, "anyone" can specialize the model to their task and the possibility of an open ecosystem that runs efficiently on a single architecture can coalesce. This doesn't mean releasing the best AI models of 2027 with complete openness --- just that we should, come 2027, have fully open models of 2025's capabilities in order to enable new types of companies and research.

The efficiencies of open-source software style development are dramatically stronger for agentic systems than models. Models are singular entities built with expensive resources and incredible focus. Agents are systems that can use many models off the shelf and route requests depending on what's needed.

This agentic era is the opportunity open models have needed, but we need to clear much stronger performance thresholds before the open counterparts are viable. We have companies like OpenAI and Google launching Claude Code competitors that pretty much flop. Imagine what this would look like with open models today? Not good.

For this reason, we have finite time to get there. Surely, eventually this level of models will exist, but if we want a new type of ecosystem to form we need to build the raw resources while developers and new companies are getting started. We need people willing to take the risk on something different while there is still potential for it to be comparable across performance trade-offs.

Today, the [best fully open language models](https://www.interconnects.ai/i/158931739/the-state-of-the-open-closed-model-gap) are catching up to the levels of the *original* GPT-4. This is a major step from GPT-3 levels. The required step I'm shooting for is reaching the modern GPT-4 type models, the likes of recent Sonnet, DeepSeek V3, or Gemini Pro. It's a big step, but a transformative one in terms of what the models can do.

Of course, some of this still works with open weight models and not just fully open models, but to date we have not had good success with having open weight models that can fully be trusted. The best American models are plagued by the Llama license (and rumors that future versions will be discontinued). At the same time, Chinese models [aren't trusted](https://www.interconnects.ai/p/what-people-get-wrong-about-the-leading?utm_source=publication-search) because the models are being integrated directly with more complex tools that muddy the water with a weak security reputation, and European models are largely off the map.

If we want models we can trust, we need something that's a bit different. If the models all converge on a certain capability level, and the differentiation is on integration and finetuning to specific skills, this is something the open community can do.

In many ways, obtaining this goal is a quintessentially American volition. In the face of a technology that is poised to bring such extreme financial, and by proxy literal, power to a few companies, opening AI is one of the only things we can do to reduce it. Technology proceeds in a one-way direction --- for a variety of geopolitical and capitalistic reasons it is impractical to pause AI development to "do AI another way" --- the best we can do is chart a path that makes this future better.

Along the same vein, if AGI already exists and something closer to ASI is coming, it will be intertwined with countless details of billions of people's lives in a matter of just years. Something so indispensable to our lives in work, play, entertainment, and relationships is a closer analog to electricity than other traditional technology products that one can opt into. Such technology should be available for all to benefit from.

We need new systems to mitigate misuse, but it shouldn't be solely up to corporations to control this. Safety by isolating technology to a select few is something we're in the later stages of with nuclear weapons[5](#footnote-5){#footnote-anchor-5 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}, and AI progress is far harder to monitor. Robustness to AI can only come from designing systems that expect it to be pervasive --- not that it is an easy task.

Realistically, all of this is fighting gravity. The corporations will win, but we can control to what extent. We can control how good the other options are. The open options.

The call to action here is simple --- consider how you can slightly shift your decision making to make The American DeepSeek more likely. This approach succeeds just as much by having one model at the end of it, as it does by having the community form better habits and norms around the way AI models are conceived, built, shared, and used.

<div>

------------------------------------------------------------------------

</div>

*Thanks to Jordan Schneider, Miles Brundage, and Kevin Xu for feedback on early versions of this post.*

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Kevin's explanation on [Interconnected](https://interconnect.substack.com/p/chinas-structural-advantage-in-open) is the best way to get this across:

> China's structural data advantage can be understood in two ways. **One**, and connected to the previous advantage in domain expertise, there is a lot of vertical industrial data being produced. These datasets are both large in quantity, because many Chinese industries tend to be more 5G-connected and IOT-ready, and high in quality, because they reflect real world use cases and problems. It is really the best type of training and evaluation data.
>
> **Two**, while the overall Chinese internet data is less open and less plentiful, it is still a large source of information that most leading American AI labs have self-selected out of. Contrary to the consensus narrative, ChatGPT wasn't "banned" right off the bat by China when it was released; **OpenAI proactively decided to not make ChatGPT available in China and opted out of that market**, in order to more cleanly align and shape the geopolitical landscape of AI (democratic AI vs authoritarian AI). Other closed source American AI labs more or less followed suit. So Chinese internet data is of little use or value to them. Chinese AI labs effectively have that dataset all to themselves, while their access to the global Internet data is unfettered.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
I'm not the first one to use the term "American DeepSeek," see [this](https://danieljeffries.substack.com/p/how-to-build-an-american-deepseek?utm_source=chatgpt.com) blog or [this](https://x.com/kolelee_/status/1884895002071035913?utm_source=chatgpt.com) Tweet.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[3](#footnote-anchor-3){#footnote-3 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Most of this is definitely compute costs.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[4](#footnote-anchor-4){#footnote-4 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
They, of course, have their own political challenges, but not ones the world can practically influence.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[5](#footnote-anchor-5){#footnote-5 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
It didn't really work.
:::
::::
