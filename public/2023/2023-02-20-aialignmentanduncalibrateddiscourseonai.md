---
title: ""AI alignment" and uncalibrated discourse on AI"
subtitle: "Re-naming arms races; bridging communities; aligning ChatGPT, and more."
date: 2023-02-20
type: newsletter
audience: everyone
visibility: public
post_id: 103944747.ai-alignment
email_sent_at: 2023-02-20T18:04:33.866Z
---
*Disclaimer: I did limited reading on definitions of AI Alignment, value alignment, etc. for this article. There is a large literature of posts on forums I have tended not to read. It\'s based on my years encountering the community and recent discourse around AI progress. If you\'re an expert on AI safety / alignment, please feel free to correct me!*

<div>

------------------------------------------------------------------------

</div>

I wanted to take the long overdue exercise of capturing my thoughts on AI alignment, safety, and AGI, and more importantly, what\'s missing.

To start, I figured I should roughly sketch what different terms in this article mean to me. These definitions are intentionally broad to give the rest of the piece space to unfold with nuance and insight:

-   Artificial General Intelligence (AGI): any AI system sufficiently powerful to replace human(s) at a task.

-   AI Alignment: the problem space of figuring out how to capture human values (and how messy they may be) in advanced computation systems.

-   AI Safety: the research direction motivated by reducing the existential risk of future AI applications.

As an RL researcher, I\'ve been exposed to the AI alignment/safety community and AGI discussions for years. It\'s interesting that the RL community has incubated so much of the discussion on AGI (because of the [metaphor that RL was the most likely path to AGI](https://robotic.substack.com/p/rl-tool-or-framework-or-agi) that some pioneers in the field of RL propagated). RL as AGI imprinted a vision on people that AGI will be "interaction first" by design. If the likely paths to AGI were incubated in a field with a proven track record of real-world progress and success, the arguments against the \"AI Alignment Cult\" may have been less lofty. It almost seems like people equated the fact that RL was kind of a toy field with the fact that alignment may be a toy problem.

Doubling down on this shows the potential differences in what AGI means to people if they have predispositions that it\'s based on a framework for open-ended learning (RL) or a tool for solving at-scale language problems (the Transformer). We assumed that RL would be the starting point, but we are starting to see signs that language models can also learn to interact with tools \-- [Toolformer](https://arxiv.org/abs/2302.04761) has a transformer that learns to use APIs via *self-supervised learning*.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

When interviewing for jobs, I had established researchers in other fields ask me \"what\'s up with this alignment thing\" because of my seat in RL. This was last year \-- the collective community was not ready to grapple with this. I didn\'t really have a good answer. I always felt that alignment needed to be treated differently from AGI, but did not take the personal time to figure out how. Now, I\'m pointed to as the right person to do RLHF because of my seat in RL. These cycles always flow.

The second thing that has been hard for my brain to confidently believe *all is fine* is the media coverage around ChatGPT, Bing, etc., and the affiliation with AGI. Saying that any new cutting-edge AI is AGI totally sidesteps prerequisite and important questions around potential harms. Value alignment is somehow already a real-world problem given how these models are trained on literal human preferences. RLHF being popular should be the call to arms that alignment/safety researchers user to finally see eye to eye with fairness and bias researchers (often labeled as AI Ethics, but there\'s a huge distribution)\![2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

Somehow, when I read Twitter, it already seems like there is a social reward for dunking on AI alignment (examples: comparing it to [gun alignment](https://twitter.com/qntm/status/1626723399216103425), even though guns changed the power dynamics of the world quite a bit; saying AI alignment is [only a business reality](https://twitter.com/yoavgo/status/1626356049459511298); here\'s the [Twitter search](https://twitter.com/search?q=ai%20alignment%20safety&src=typed_query) I used).

AI alignment is a real problem. Until we can start to discuss it productively, I won't really be commenting on the existential risk side of things. If humans cannot address the problems of today, there's no chance for the 10+ year out ones.

![A bank vault with a (1).jpeg](images/103944747.ai-alignment_b112f423-2c58-4257-863d-460ea8981d2c.png)

### An arms race?

With Google and Microsoft launching chatbots, society has already labeled this era of AI as an *arms race*. This word has a lot of historical meaning and actually does mean that the technology being used is affiliated with weapons. I find this branding particularly disappointing. Technological races have similarities to arms races, but we should reserve the arms label for what is also likely happening with international relations.

On the domestic side (e.g. with our favorite technology companies) we should encourage a more nuanced discussion on the dynamics we are encouraging. We are feeding into the company's goals of mass market share, without clear definitions or any hopes of regulation. This lack of regulation is strongly related to community members\' biases around open sourcing. The outcome that I am most worried about due to the normal process of a weighting of likelihood with potential harms is market consolidation way beyond what we\'ve seen in the last decade of FAANG.

If you\'re not yet on board for these language models creating disruptive market value, please get on. We are in the early days, but some of the features of autoregressive language models are truly riveting for the human brain. The ability to talk to seemingly intelligent \"characters\" is deeply addicting for the brain. I expect a similar amount of brain re-wiring to need to be done for AI-generated chat as we needed for internet-enabled instant communications. Every website will have a useful chatbot and AI-generated content will become a dominant media platform (likely a bigger disruptor to Meta, as I don\'t expect TikTok / Snap / an existing company to deploy it). These are both substantially value constructive.

This fits into OpenAI\'s somewhat silly simple definition of AGI (taken from this blog post on [aligning ChatGPT](https://openai.com/blog/how-should-ai-systems-behave/)):

> By AGI, we mean highly autonomous systems that outperform humans at most economically valuable work.

For me, I\'m happy calling any AI system that enables a company to accumulate sufficient market power (e.g. 10x valuation of Apple or Microsoft or something) AGI. It makes the downstream discussions easier, and it\'s practical. Maybe we just call it a \"Super-AI\".

In that end, it turns out I am pretty happy with Erik Hoel\'s motivation (though we have different writing styles) \-- [Source](https://erikhoel.substack.com/p/i-am-bing-and-i-am-evil?utm_source=pocket_saves):

> The simplest stance on AI safety is that **corporations don't get to decide if we have competitors as a species**.

With this, we\'re kind of in the following situation:

-   People are intellectually behind on their considerations of real AGI-like / Super-AI scenarios,

-   Companies are racing towards the future realizing there is substantial competition against them in securing this value,

-   The public discourse is fractured to start with, and the metaphors we use are making it worse.

![A bank vault with a.jpeg](images/103944747.ai-alignment_9b550562-3045-4139-8021-18423d6ae0fb.png)

### Bridging communities

As someone who has read the books like [Human Compatible](https://en.wikipedia.org/wiki/Human_Compatible) or [Superintelligence](https://en.wikipedia.org/wiki/Superintelligence:_Paths,_Dangers,_Strategies), I\'m trying to figure out why the books don\'t resonate in the same way this product-focused AI escalation period does. Studying technical problems for matching the distribution of human values is incredibly important, but to me, it is not that big of a surprise that we\'re in a product-focused brouhaha. ML has been used for years by some of the most profitable companies in the world to entrench their moats and improve user experiences. This remains the most likely reason that an AI winter v2 will be avoided.

Honestly, I\'m okay with it if the chatbot revolution is overblown and the AI market resets much as the broader technology industry did in the last year. It gives everyone the experience of an AGI-adjacent scare without the reality of the acceleration. A cooled-down discourse is needed to bridge gaps across communities. For example, I\'m preparing a tutorial on RLHF for the next FAccT conference (🤞on acceptance), which wouldn\'t be until June. We need brilliant researchers worried about immediate biases and societal harms controlling the trajectory of this AI acceleration.

### Aligning ChatGPT

On the ChatGPT side of things, OpenAI\'s plans for alignment actually seem quite calibrated in balancing long-term safety goals with practical short-term limitations. I\'m cutting the interesting parts from their [post](https://openai.com/blog/how-should-ai-systems-behave/) clarifying ChatGPT's current and future behaviors. To start, I want to hear what people think about this:

> Though not a perfect analogy, the process is more similar to training a dog than to ordinary programming.

Is this a good take? I\'m going too deep thinking about it, but it is true that a lot of top engineers have lost the ability to fully capture the abstractions and capabilities of modern software systems. From an alignment perspective, that should be worth digging into further.

Much later in the article, OpenAI elaborates on the high-level goals of ChatGPT\'s development. An absolutely crucial one is the following:

> **2. Define your AI's values, within broad bounds**. We believe that AI should be a useful tool for individual people, and thus customizable by each user up to limits defined by society. Therefore, we are developing an upgrade to ChatGPT to allow users to easily customize its behavior.

I\'m glad they\'re talking about this before it's force-fed to them in the coming AI culture wars. OpenAI\'s take here is a pretty substantial divergence from what Anthropic has shown us via Constitutional AI (they wrote down a set of terms that provided feedback on language model outputs). I would say that long-term, Anthropic probably agrees with OpenAI\'s plans here too. A lot of their recent work has been along the lines of \"we have these powerful tools, can they work together to reduce harm\" and not a long-term vision statement of how people should and should not interact with AI. For example, this practical approach to alignment is continued in the work where they just *ask the model to be nice*!

This comparison is actually an interesting statement in how we are reviewing material from these two companies right now \-- papers versus blog posts. OpenAI publishes non-technical blog posts focused on narratives and Anthropic primarily publishes papers where the running assumption is they\'re incentivized to tell the truth, for alignment goals.

The last talking point in the OpenAI blog post is regarding public input.

> **3. Public input on defaults and hard bounds**. One way to avoid undue concentration of power is to give people who use or are affected by systems like ChatGPT the ability to influence those systems' rules.

Essentially, this reads like OpenAI agreeing with the post I just wrote. In order to arrive at a public consensus on norms, we need to bridge some of the broken lines of communication I addressed above. So long as the alignment researchers are not joined with ethics/fairness researchers, we are going to have problems.

Does anyone want to help crowdsource things that alignment and fairness researchers agree on? Comment below!

Thanks for reading.

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
In my taxonomy, Toolformer is doing RL.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
[Joshua Achiam](https://twitter.com/jachiam0/status/1627052852295376896) at OpenAI is a good person to follow if you agree with this.
:::
::::
