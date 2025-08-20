---
title: "Open LLM company playbook"
subtitle: "Where does releasing model weights fit into company strategy? 3 requirements, 3 actions, and 3 benefits of being in the open LLM space."
date: 2023-11-01
type: newsletter
audience: everyone
visibility: public
post_id: 138475106.open-llm-company-playbook
email_sent_at: 2023-11-01T12:01:43.889Z
---
Companies releasing the weights of cutting-edge language models in 2023 is one of the most popular things they can do, but there are few serious analyses into what this is doing for their long-term business prospects. Combine this with the fact that I have had to be really vocal in [challenging the branding that some company PR departments present about openness](https://www.interconnects.ai/p/are-open-llms-viable) or [responding to general criticism for the open-source ML ecosystem](https://www.interconnects.ai/p/how-the-open-source-llm-ecosystem), I figured it was about time I put together a **clear notion of what companies should be doing to leverage open LLM weights**.

Throughout, I am trying to be as realistic as possible. It will be pretty apparent that I don\'t think these companies should be adhering to complete open-source principles (which means [the LLMs they release will not truly be open-source](https://www.interconnects.ai/p/if-its-not-fully-closed-ml-its-open)). Being open gives companies avenues for adoption and development not available to their closed counterparts. This article will not focus on potential business risks or liabilities from being open (even though I think [open releases will make liability less of a problem when compared to model-and-fine-tuning services](https://www.interconnects.ai/i/137911702/moderation-training-infrastructure-liability) like Open AI).

This post is about building and how releasing LLM weights in the open will make it easier for a company to iterate, gain customers, and deliver better products. It\'s about how creating open LLMs facilitates a healthier, more collaborative, ML economy with broad stakeholders building a wonderful future.

I outline 3 prerequisites, 3 actions, and 3 benefits for open LLM companies, but you'll quickly see they all interweave throughout.

Let\'s get into it.

![\\\_8c37326b-e4ee-415c-85be-2add3ab43194.jpeg](images/138475106.open-llm-company-playbook_39d8a285-edd3-49f7-a821-95367faf3921.png)

## Requirements

### 1) Have a niche

This is the most important part of building a successful open LLM company. You need a specific objective. Training models is one thing, but **without knowing your positioning, someone else will be making the product/customer connections you need**. These connections are going to be crucial when everyone starts running out of money in 1-2 years. With the startup valuation correction incoming, every few months of a head-start iterating on monetization will be how you don\'t lose the musical chairs.

Open LLMs are not going to compete directly with OpenAI. They are targeting very different economies of scale and monetization strategies. Closed API companies are [building computing platforms](https://www.interconnects.ai/p/llms-are-computing-platforms) and open LLM companies are building the best products the internet has ever seen.

Having a niche sets your company on a direct roadmap, and makes the things that come after this a little bit easier. You know what data you need to prioritize, evaluations that are worthless, people you need to hire, and everything in between.

### 2) Train good models

If you can\'t train good models, GPT-N will always be better at your niche, making adoption a fraught curve. Good is not always SOTA, but it means your experiments match benchmarks generally across the industry. If you focus on an evaluation, can it go up? For example, my team at HuggingFace spent maybe 4 months focusing on [MT Bench](https://lmsys.org/blog/2023-06-22-leaderboard/) as our primary indicator of chat capabilities, and we got towards the top of the size bracket with [Zephyr](https://arxiv.org/abs/2310.16944) models \-- the right ballpark in a few months is good enough. Have a mechanism for a reality check.

Not all startups will figure out how to do this, but it is going to be table stakes to keeping up in the VC-backed trajectory of the next few years (because it\'ll be needed to keep your customers happy, see above). To do this, you need to invest in fundamentals. You need compute to train models in the relevant ballpark and do a lot of experimentation. **You need the time in your runway and leadership direction *****to go deep***** and not just release the first thing that breaths**.

### 3) Have a technical team that interfaces with the community

You need to be able to get some initial momentum behind your models. It is unlikely that every model your organization releases will be the best in class. Being the best obviously works, but what happens when an iteration is behind? This is the first fold back into having a niche, which we will see time and time again: Benchmarks stop mattering if you do something unique that people care about!

This all ends up being storytelling in a way. Having people that can mobilize interest can have outsized impacts across all timescales. It helps correct mistakes, amplify reach, add personal touches, and bring in customer leads. It is not fun work, but **if you want to rely on being open**, **people need to see your models!**

## Actions

### 1) Release the model weights

Lots of people are still getting stuck here! Releasing the weights, lets other people do the hard work for you of training, evaluation, and efficient inferences. It lets people verify your claims and improve on them. **ML is not going to be like previous open-source companies where GitHub is the core of adoption, ML is on HuggingFace**. Everything starts with the model, and then stuff like scripts to use it comes next.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

### 2) Get a data pipeline, don\'t share your in-domain data

Now and for a few years, data is the core engine behind the successes of LLMs (as long as you aren\'t a hyper-scale company). Data is primarily from humans to get started but soon will also involve carefully curated AI data. With the data, similar performance will be achievable with enough compute. While this is the case, unfortunately, it doesn\'t really make sense to release your niche data. **The** **data is your most defensible moat, as AI budgets will oscillate wildly as the economy figures out what LLMs are actually worth**. I do think there are still many reasons to share pretraining data, as I [discussed here](https://www.interconnects.ai/i/137597328/medium-term-sharing-data-competition).

To be clear, I don\'t see how open LLM companies can be open-source absolutists too. HuggingFace is a different story \-- they\'re building a platform in the style of many that have come before (Google, GitHub, whatever), so usage in that code directly converts to growth and improving their moat.

### 3) Extensively benchmark price and performance vs. closed models

[OpenAI\'s tools are actually very cheap](https://generatingconversation.substack.com/p/openai-is-too-cheap-to-beat) for developers just trying out models. It\'s safe to assume GPT4 will be 10x cheaper in 18 months. Given that, there\'s still plenty of runway for smaller models to be better and cheaper, even with OpenAI\'s economies of scale, but it is important to not delude your customers. **Many of your customers will be trying to figure out this pricing balance on their own, so you should do it for them and make it clear where you\'re winning**. These price comparisons will help you win back middle-of-the-curve customers who are starting to deploy models here and there, and they provide the justification that an executive needs to set up a new enterprise account beyond OpenAI.

There\'s a common problem among fast-moving and high-flying ML companies to not benchmark against their competitors (especially among closed source). By getting the cost numbers down it\'s not so hard to add other evaluations to the mix. These evaluations are the only competitive market research that matters for an LLM company \-- the market size and demand will be growing so fast as we learn about these models that staying ahead can be a winning strategy.

## Benefits

### 1) Crowdsourced evaluations (capabilities and inference) improve models

The biggest benefit that Meta has gotten from open-sourcing their models is advanced evaluations before rolling the models out into their products. **All the stuff about \"too much RLHF in Llama 2\" (which was mostly a system prompt problem) came without burning any reputation from real customers**. Then, people answered [how to run Llama on laptops](https://github.com/ggerganov/llama.cpp), how to train it for many domains like [code](https://arxiv.org/abs/2306.08568) or [math](https://huggingface.co/WizardLM/WizardMath-70B-V1.0), and how far quantization can take it (links here are more distributed).

Costs should always be a driving point for open models winning. People create their own stack, so they don\'t have to pay the markup factor on compute, monitoring, compliance, etc. A lot of this benefit will be arrived at by community members pushing the limits to run your models locally.

### 2) Crowdsourced use cases build product leads

Open source will just keep you on the cutting edge of what certain AI qualities will translate into products and you can monetize it. Given how deep people are going with AI right now, open-source communities will take your models into applications well beyond the wildest dreams of your product team. **By keeping up with how people are using your model, you can figure out which paid products you should build in the future**.

### 3) Good PR: Recruiting, values, vibes, etc

**Openness unequivocally makes your employees' careers more successful and you should tell them this as a recruiting ploy**. This is the biggest reason by HuggingFace was so good for me, and they\'re far from the only company winning here. It\'s simply an easier and more robust playbook than creating a cult culture that people will pour their entire lifeblood into. Recruiting is likely the biggest differentiating factor between all the duplicated LLM startups we have right now.

People like to work at places where it doesn\'t feel like there is an iron fist over your shoulder. Lean into all of this. Let people speak their minds, let people lead in public, and let people promote their work online. This good PR energy feeds back into everything above.

<div>

------------------------------------------------------------------------

</div>

## Some examples of open-model feedback loops

-   Adept AI, with its [Fuyu model](https://huggingface.co/adept/fuyu-8b), is likely going to get a ton of ideas about how multimodal models can be used for developers to improve their quality of life. Open-sourcing could take them from marketing as building general computer agents to simple products that people love today.

-   Twelve Labs, a video understanding startup, released a model [Pegasus](https://app.twelvelabs.io/blog/introducing-pegasus-1) that does just that (though TBD if it\'s a good enough model to get traction). A good start (and let me know if you\'ve used the model and have thoughts).

-   Stable Diffusion clearly could help Runway, which is building a platform for visual GenAI, but doesn\'t do as much for Stability, which is building what exactly?

-   Meta has two angles unfolding at once with the Llamas. The first one, \"get developers onboard, then they scale up (if they want to make money on the cloud)\" only really applies to the absolutely best open LLMs, particularly those that are general use or heavy developer use (code). The second, \"let's learn about the models we use for products\" also is much simpler and makes a lot of sense.

## Open-source ML hot takes

-   If Perplexity is training models with access to super recent information (as in, it isn\'t a modular system that is hard to release), they should release one. Smart people would figure out the use case beyond chat and search \-- like financial analysis models or something that they could target with products and make that \$.

-   Cohere should consider pivoting to open source. They seem to be falling behind / aren\'t leading the narrative as much as OpenAI and Anthropic (their closest peers), so they maybe could jump over Meta? At least *some* of their models could be relevant there.

-   Regarding niches for LLMs: You don't need a big audience just the right audience (unless you\'re trying to compete with OpenAI or Llama).

-   Mosaic is a place that could actually stand to release all of its training data. If they release their training data, they can show that their software makes the *best possible model* given the data and compute provided. This is really valuable! If anyone proves them wrong, they get better. Someone training the model they already trained doesn\'t really matter, because it is a bit more general!

<div>

------------------------------------------------------------------------

</div>

If you were looking on comments on the Executive Order (EO), I generally agree with this quote from [AI Snake Oil](https://www.aisnakeoil.com/p/what-the-executive-order-means-for?utm_source=post-email-title&publication_id=1008003&post_id=138461039&utm_campaign=email-post-title&isFreemail=true&r=68gy5&utm_medium=email) (Casey Newton also [covered it on Platformer](https://www.platformer.news/p/biden-seeks-to-rein-in-ai?utm_campaign=email-half-post&r=68gy5&token=eyJ1c2VyX2lkIjoxMDQ3MjkwOSwicG9zdF9pZCI6MTM4MjIzNjgxLCJpYXQiOjE2OTg3OTY3MTUsImV4cCI6MTcwMTM4ODcxNSwiaXNzIjoicHViLTc5NzYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.Tf5PSPx-X_UkrJbs-siowXiVeWc-AM3nC3Yh_Dg6JMw&utm_source=substack&utm_medium=email), and we\'re covering it this week on [The Retort AI Podcast](https://retortai.com/)):

> In short, the Biden-Harris EO is bold in its breadth and ambition, but it is a bit of an experiment, and we just have to wait and see what its effects will be.

It does things that should help openness. It does things that could hurt it. It does, though, have some parts that seem blatantly written by AI Safety folks.

That\'s not always bad, so it is an issue for another time. With the AI Safety Summit in the U.K. around the corner, I think that time may be soon.

<div>

------------------------------------------------------------------------

</div>

### Newsletter stuff

Elsewhere from me:

-   \[Podcast 🎤\] On [episode 7 of The Retort](https://retortai.com/episodes/transparency-stanfords-version), Tom and I discuss transparency and AI, the FMTI, my critique, what it all means for the world, why, and other topics.

-   \[Paper\] My old team at HuggingFace published a [technical report](https://arxiv.org/abs/2310.16944) on the 7 billion parameter chat model we trained with Direct Preference Optimization (DPO). The extent to which open models are pushing the limits of MT Bench and AlpacaEval (I think it may be going too far) is awesome, and the code is in the process of being fully released.

-   \[Career\] I officially started at the [Allen Institute for AI](https://allenai.org/). I\'m stoked to keep building open ML and fight for everything that stands for.

Only one link this week:

-   [Another AI leader calls out what I think is clear regulatory capture attempts](https://www.afr.com/technology/google-brain-founder-says-big-tech-is-lying-about-ai-human-extinction-danger-20231027-p5efnz) (found via [Platformer](https://www.platformer.news/p/biden-seeks-to-rein-in-ai)): "There are definitely large tech companies that would rather not have to try to compete with open source \[AI\], so they're creating fear of AI leading to human extinction," Ng told the Australian Financial Review. "It's been a weapon for lobbyists to argue for legislation that would be very damaging to the open-source community."

Housekeeping:

-   **Interconnects referrals:** You'll accumulate a free paid sub if you use a referral link from the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   **Student discounts:** Want a large paid student discount, go to the [About page](https://www.interconnects.ai/about).

-   **Like this?** A comment or like helps Interconnects grow!

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
As long as you\'re not a consumer-focused application Safety filters are not important, or they won\'t be any time soon.
:::
::::
