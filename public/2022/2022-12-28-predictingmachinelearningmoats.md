---
title: "Predicting machine learning moats"
subtitle: "Models aren't moats and how emergent behavior scaling laws will change the business landscape."
date: 2022-12-28
type: newsletter
audience: everyone
visibility: public
post_id: 93241359.ml-moats
email_sent_at: 2022-12-28T14:53:35.061Z
---
In most ways, machine learning (ML) systems function a lot like software systems. It\'s worth making comparisons on how business moats will and will not translate, but the X-factor lies in different scaling laws. Software scales with zero marginal costs, but machine learning scales with nonlinear emergent behaviors.

The most important exercise right now is figuring out ML moats is tracking the interface between scaling laws (of emergent behavior in high-quality data) and products. Let\'s talk about definitions of moats, if OpenAI is building a moat, and where ML companies are going to get spicy (e.g. model theft).

### Ceci n\'est pas une *moat*

\[*[reference](https://en.wikipedia.org/wiki/The_Treachery_of_Images)*\]

In *old-school* technology companies, an important defining factor is how they can create a moat protecting investment from their (potential) competitors. Moats often involve technological advantages, users, data, and, most importantly, feedback loops. Feedback loops are what make users continue using the technology and give the companies the resources to make it an advantage more solid. Some modern examples include Office\'s incumbency for Microsoft, network effects at Facebook or Google, economies of scale at Amazon, branding and proprietary technology at Apple, etc.

Warren Buffett says in a [2007 shareholder letter](https://www.berkshirehathaway.com/letters/2007ltr.pdf) can tell you what these have in common:

> A truly great business must have an enduring \"moat\" that protects excellent returns on invested capital.

Bring on the great debates as people figure out machine learning moats. ML technological capacity in the form of cutting-edge research is greatly outpacing business knowledge, so it\'s an open exercise to think about how these principles of *moats* will adapt to a new paradigm.

For the sake of discussion, what are some things that could create a moat in machine learning companies?

-   A state-of-the-art model? We could list both Stability and OpenAI here. OpenAI is leaning in much more.

-   Private data? Facebook, Google, and anyone not impacted by [App Tracking Transparency](https://www.theverge.com/2021/12/11/22828713/apple-app-tracking-transparancy-psa-privacy-ads-cohorts) lead here. Interestingly, places like Surge AI or Scale are seeing if they land in this (I don\'t think they do).

-   Network effects/branding? Again, these are how Facebook and Google have classically succeeded. This is how HuggingFace currently plans on succeeding.

-   User interfaces? Being the go-to location where someone does something. Amazon dominates shopping, Google dominates search. Will one company be irreplaceable by being the metaphorical *search bar* for ML?

For each of these, some analogs to existing technology companies make sense, and for others, they don\'t. There are some usage and scaling factors that are fundamentally different. If the best ML model like ChatGPT always costs on the order of \$.01 per query (I know it won\'t, but variants might), would an advertising business a la Google or Facebook even be financially sustainable? The other option is something like Microsoft and the business software suite.

The moats I go on to define here will be in for a total shakeup in the next few years, as I am mostly defining my worldview here. Hence, we\'ll repeatedly be in the place where a failing company tells you \"this is a moat\" and it\'s not a moat.

![result.jpeg](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/9f5f3637-b383-4d3d-abcc-dbf3a08b8d9d_1514x1080.jpeg)

<div>

------------------------------------------------------------------------

</div>

## Models are not moats

Everything in ML except for the model itself is the moat. It seems like the model is the most important artifact created in an ML pipeline, and I agree. The problem is, models can easily be replaced with fine-tuning or some other procedural change. The model is the part of the system users will interface with the most, but the dataset, infrastructure, and processes are what will create structural advantages. Because the model is what is revealed (in the form of an API) or shared (in the form of a release), it is likely to be extracted and manipulated whether or not the \"controlling party\" wants that.

We\'ve seen this multiple times in 2022 already. The most obvious one is Stability with the release of different Stable Diffusion (SD) versions. Runway.ml and Stability *both* have employees who worked on the original Stable Diffusion paper (yes, it\'s a branding job by Stability, they didn\'t create this model from scratch). This resulted in Runway releasing the next version of SD without Stability knowing, and a brief [legal spat followed](https://huggingface.co/runwayml/stable-diffusion-v1-5/discussions/1).

This was a wild, brief explosion, and a tame version of what is to come. Companies will try and protect their brand value by being associated with a popular model, but, at the end of the day, these positions are not stable.

Talent will so often come and go on 6-12 month cycles, so it\'s hard to keep a lasting advantage by scooping people out of academic labs (and the professors are always there to train the next generation). Even if Stable Diffusion wasn\'t open source, there will *rapidly* be openly available alternatives. DALL-E mini (now [Cr](https://www.craiyon.com/)**[ai](https://www.craiyon.com/)**[yon](https://www.craiyon.com/)) got more attention from the general public than the original DALL-E did.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

Next for the lesser-known way a model can be stolen: **model** **distillation**.[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

When a model like GPT3 is opened up via an API, users can generate numerous outputs associated with prompts, and use them to fine-tune a model of a similar architecture. While this isn\'t perfect, it\'s expected to create a model of similar performance (and is conceptually much simpler than doing so from scratch). ChatGPT, for example, is currently free, so people could be doing this in the background. If a typical NLP training set has 1 billion training tokens, you would burn about \$ 10 million of computation from OpenAI/Microsoft and be able to train something like chatGPT.[3](#footnote-3){#footnote-anchor-3 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

Though, this is illegal in the OpenAI [terms of service](https://openai.com/terms/):

> \[One cannot\] use the Services to develop foundation models or other large scale models that compete with OpenAI

Models are more challenging to keep under wraps than something like supply chain and manufacturing that spreads out expertise and physical goods (ML models are just trained in the cloud!). Data is the moat for ML systems *right now*. When training data is well defined and curated over time, it can't be taken by one leaving employee or a simple leak. OpenAI is on the record saying that they re-use prompts from the API to fine-tune their model and curate their datasets. There are likely other feedback loops there we don\'t know about.

Think about how many hilarious things people have put into ChatGPT. Probably \~0.1% of these requests are things we didn\'t think the models needed to do but would be truly insightful behavior driving business value. OpenAI has an advantage here and will continue to accrue it. As models get better, people will be more ambitious in crowdsourcing tasks for them.

This feedback loop actually could unlock astounding things.

### Emergent behavior as a new type of moat

My brother forwarded me [this article](https://a16z.com/2019/05/09/data-network-effects-moats/) from Andreessen Horowitz in 2019 on *The Empty Promise of Data Moats*, and the themes are becoming increasingly relevant as the ML product landscape solidifies. The gist of the article is that more data does not necessarily solidify a business position. This is defined by an era where adding data added marginal capabilities.

For some areas of deep learning, we are still seeing adding data follow a log curve of growth. More data improves performance less and less.

For the accelerating areas of deep learning, we are seeing increasingly incredible behaviors emerge *suddenly* when a certain data threshold is reached. Sound far out? It\'s studied to the point where well-known authors in the field have written a [review/position paper on](https://arxiv.org/abs/2206.07682) the *Emergent Abilities of Large Language Models*.

Let\'s look at one of the core figures from the paper --- the x-axis is model size, and the y-axis is performance. It shows emergence across a variety of tasks and models versus a random baseline. It\'s fairly astounding.

![Image.png](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/88b76a95-939f-4e58-8cb6-ed72f82fda8a_1288x1150.png)

Emergence is the nonlinear growth in performance relative to dataset size. This scaling is closely coupled to diverse and large datasets (scaling laws can be studied [here](https://arxiv.org/abs/2203.15556)). User data is a sure way to get the most diverse data, which is crucial because the data needs to be diverse and not repeated when scaling.

Combine this propensity for emergence in large ML models with the high cost for OpenAI\'s most crucial data sources, and this traditional notion that \"data moats are fake\" seems to fall straight on its head (see my past post on RLHF data and access concerns, [here](https://robotic.substack.com/p/rlhf-chatgpt-data-moats)). Given how paper after paper has shown unexpected behaviors emerging when reaching an arbitrary scaling point, we can form new guesses on how data network effects can work for ML-first companies. *If* adding new data leads to new abilities and extremely concentrated usage, *then* data can provide lasting advantages in a way not seen before.

This sort of hypothesis, where scaling laws and network effects change, is why I am so interested in the next 10 years of machine learning products and industry.

::: pullquote
The feedback from multiple models being better to use, rather than any model weights themselves, is the moat.
:::

## Other opportunities for moats

There are a few other thoughts worth considering when discussing ML moats.

-   Companies like [Runway](https://runwayml.com/) and [Jasper](https://www.jasper.ai/) are **crafting moats in verticals**, where they are the best-in-class companies and brand names;

-   [Lensa](https://prisma-ai.com/lensa) is built on Stable Diffusion, so it may not have a moat at all. It **won by being first**;

-   [Weights and Biases](https://wandb.ai/) and [HuggingFace](https://hf.co/) are early winners by building incumbency in ML stacks;

-   Existing giants like Google or DeepMind could conceivably have a moat by building their giant ML training infrastructure. What happens if GPUs aren't available and they're the only ones scaling models to the next size scale?

There are tons of ways that companies can defend their business, but I'm most interested in those that are ML specific. Time to keep reading about scaling laws.

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Craiyon is an interesting business model attempt, the dev is trying to make it work with ads paying enough for development, deployment, and maintenance. From what I heard, it\'s not going amazing, but it is afloat.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Distillation is a loaded term in ML. There are a ton of things relevant here, like [knowledge distillation](https://neptune.ai/blog/knowledge-distillation), which this is the closest to, [dataset distillation](https://ai.googleblog.com/2021/12/training-machine-learning-models-more.html), or other things that are colloquially called distillation.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[3](#footnote-anchor-3){#footnote-3 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Let me know if distillation like this is actually expected to work well. Some professors I work with tended to think it does, but I am not entirely an expert and it could have been lost in translation.
:::
::::
