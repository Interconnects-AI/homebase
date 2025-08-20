---
title: "We aren’t running out of training data, we are running out of open training data"
subtitle: "Data licensing deals, scaling, human inputs, and repeating trends in open vs. closed LLMs."
date: 2024-05-29
type: newsletter
audience: everyone
visibility: public
post_id: 145096252.the-data-wall
email_sent_at: 2024-05-29T15:08:36.775Z
---
For months we've been getting stories about how the leading teams training language models (LMs) are running out of data for their next generation of models --- vaguely insinuating a struggle for big tech's darling industry with no strategic claims beyond the fact that the second derivative on training dataset size is negative.

All the real facts on the ground point to the decision makers in charge of these companies being extremely bullish on the impacts of scaling language models regardless of the data issue --- capital expenditures are at all-time highs across big tech and they're forecasted to stay this way. This sort of capital risk isn't taken if we're all going to get stuck by the data wall blocking every aspect they use to improve models. However, as we have seen with AI again and again in recent years, it'll be the long tail of open players that get pinched by the data bottleneck, not OpenAI and Google.

To be clear, data is definitely getting harder to access. The primary mode of operating in the last few years was to scrape some area of the web, clean it, and train on it. There are no longer major areas of the textual web just waiting to be grabbed. Data curation being different does not mean that it becomes impossible. Currently, synthetic and multimodal data are just at the early stages of their integration (estimates place YouTube's daily uploads at about 4 petabytes of data). [Synthetic data, i.e. training data outputted by an LM](https://www.interconnects.ai/p/llm-synthetic-data), is starting because LMs have just crossed the capability boundary needed for training on the outputs reliably. YouTube is starting because of the goals of multimodality being grander than the costs of sifting through the low average quality on the massive platform.

This piece, and most of the news around LM data focuses on text, where synthetic data will have a bigger role than transcription. The dichotomy of synthetic data usage has been something I've been monitoring for some time. From my first [major piece on synthetic data](https://www.interconnects.ai/p/llm-synthetic-data):

> the big companies of the world will be spending \$10million+ on inference compute to create datasets (pretraining scale synthetic data), while open-source competitors spend \$10 or so on an instruction dataset.

This still largely holds. The open counterparts even spend more time combining existing datasets than creating new ones, especially when it comes to prompts, which are crucial for dataset diversity.

If we figured out how to create remarkable artifacts by filtering the mess that is internet-scale data, I'm confident the AI industry will figure out many, many ways to use synthetic data for frontier-level models. A recent example is [Phi 3's synthetic focus](https://www.interconnects.ai/i/144153650/phi-synthetic-data-and-small-models). The best way to think of Phi 3's "synthetic textbook" data in relation to these efforts would be a research project, textbook style data, at ablation model scales, 3-14 billion parameters. Places like OpenAI and Google will be running experiments like this end-to-end on a monthly basis to easily hurdle the so-called data wall.

The clear Achilles heel of the Phi 3 work is the lack of clarity on how many tokens they can generate reliably, and if it is enough data to shift the needle on frontier LLMs. As an exercise, let's try to get an estimate for how many tokens OpenAI is already generating on a daily basis that it could train on.

### Synthetic data: 1 trillion new tokens per day

ChatGPT has approximately 100 million monthly active users, let's call it 10 million daily queries into ChatGPT, of which the average answer is 1000 tokens.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"} This puts them at 10 billion candidate tokens to retrain their models every single day. Not all of this is valuable, and as little as possible will be released, but if they really need more places to look for text data, they have it.

Regardless, the real point is about the long-term trend of this. The current class of ChatGPT applications are running on v0 or v1 of the new inference stack for these models, and all the major players are trying to 10 or 100x these. Once the inference clusters start reaching these numbers, a company like OpenAI could generate over 1 trillion tokens of training data every day. Generating 1 trillion tokens with GPT-4o on the API would cost about \$ 7.5 million on batch mode, [which gives a 50% discount for bulk jobs not requiring answers immediately](https://platform.openai.com/docs/guides/batch/batch-api) (great product). Given the competition in the API space, I would guess this would cost OpenAI at least \$ 5 million in direct costs. Expensive, yes; prohibitive, no. It's likely 10 to 100 times cheaper than buying data.

This obviously doesn't solve the quality issue, but people are creative, and that is a vast resource to experiment with. It's largely rumored that Mistral AI has already been doing this for their models: collecting generations from APIs, filtering them, and including them in the pretraining mix.[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"} All of these at-scale sources for synthetic training data are never going to be permissively released for the open community, at least not without year(s) of delay.

### Data licensing deals: High costs per token

Despite the definite advantages that the big tech players have in this domain, they've still signed dumb data deals with mid-sized technology companies and small platforms to get access to their customer data. Examples include [Reddit](https://openai.com/index/openai-and-reddit-partnership/), [news agencies](https://www.nytimes.com/2024/05/22/business/media/openai-news-corp-content-deal.html), [Stack Overflow](https://openai.com/index/api-partnership-with-stack-overflow/), and more, where labs sign these deals that present as "crucial infrastructure" for the next generation of models, where in reality it seems most like a legal strategy to punt potential lawsuits to firms with shallower financial pockets.

Here, we can do more math to roughly estimate the importance of these deals. In OLMo's dataset Dolma, which we're trying to make as close to industry labs as possible (even though it is clearly missing some key pieces like [the forbidden books](https://www.reuters.com/technology/meta-used-copyrighted-books-ai-training-despite-its-own-lawyers-warnings-authors-2023-12-12/#:~:text=Meta%20used%20copyrighted%20books%20for,'%20warnings%2C%20authors%20allege%20%7C%20Reuters)), Reddit is 3.4% of the overall training corpus. Similar web entities in that size are the Common Crawl version [C4](https://huggingface.co/datasets/c4), StarCorder from HuggingFace, Arxiv papers, and StackExchange. All of these dataset sizes were the publicly available components up until the companies changed their data license policies. It'll take years of platform usage for the private portion to match the size of the public portion that we have. At the time of the signing, the actual amount of data is quite low.

The costs of these deals are not marginal to mid-sized technology startups. For example, the Reddit data contracts are rumored to be at about \$60million in annual costs. This figure, if you're well connected, can be the equivalent cost to a 2-5000 H100 GPU cluster all included. Companies like Cohere and Mistral will have a hard time paying these deals, and the likes of Google or OpenAI will happily shift more narrative risks and table stakes to squeeze out potential competitors.

There are some technical questions, such as if these data sources are needed for current events, which may be a high-value area for the models, or if they're needed for multi-turn training, which the open models still struggle with. Either way, it feels like paying because they can, and not because they're a crucial asset. Over the years, as the platform powers shift further to the LM providers (much like it did with Google search), Reddit et al.'s leverage will continue to dwindle. We'll see if the data deals can keep up with the pace of inflation as market pressures drive the value down.

In some ways, we're playing the story of platforms with news feeds in reverse, where recently media companies have been [trying to get their pound of flesh from Google and Meta](https://www.cnn.com/2023/06/20/tech/gannett-newspapers-google-lawsuit/index.html) for the rights to their content. Given that the technology platforms concentrate on user demand, I don't expect the media companies to have much to stand on. The same power will accrue to the likes of ChatGPT.

### Better tokens: Search and new frontiers

As we scale up LMs, most of the problems facing these companies reduce to compute amortization. As they're building these huge clusters, if they don't have enough data to train as long as they want for that model size, they could spend more of that compute at inference time and improve their models. Generating synthetic training is spending available compute on future models. Using more compute per token with various alignment techniques is spent on the current model (better generations).

These techniques, the most prominent of which is [best-of-N sampling](https://openai.com/index/measuring-goodharts-law/), are often studied in the literature of reinforcement learning from human feedback (RLHF). This research has continued to proceed on the academic side of things, with cool research like [Monte-Carlo Tree Search guided decoding](https://arxiv.org/abs/2309.15028). For now, it isn't economically viable for large companies to implement this for a variety of reasons: variability across tasks, safety considerations, bandwidth, blindspots, current user satisfaction, etc.

While these techniques haven't been scaled up to the domains like ChatGPT, as usage and data needs grow more complex, all signs point to the return of search-like methods to all parts of the LM training stack. Q\* is the most popular variant to date, [rumoring some sort of search over reasoning trees](https://www.interconnects.ai/p/q-star), but many more variants will come about. When generating synthetic data for a specific task, a search will be used to guide the models towards it. Intuitively, search and post-generation filtering play very similar roles.

Most of the new data used to train the next generations of language models will be augmented by an existing language model in some way. More and more Reddit comments will be guided by predictive text via a transformer or copied out of ChatGPT. Explicit datasets will be used to enable language models to procedurally generate content. Yann LeCun's long-term view of ML is that [Reinforcement Learning (RL) will be the cherry on top](https://syncedreview.com/2019/02/22/yann-lecun-cake-analogy-2-0/), generating the last bit of data, but this is shifting one level down the stack. We're seeing with LMs that human data is the final piece of the puzzle. Where current LMs fail wildly, we will keep asking humans to generate the data. Human data is the most expensive and most prohibitive for the long-tail of open players to share and have access to.

<div>

------------------------------------------------------------------------

</div>

**Housekeeping**

-   Audio of this post is available (soon) in [podcast](https://podcast.interconnects.ai/) form or on [YouTube](https://www.youtube.com/@interconnects).

-   My real podcast is at [retortai.com](http://retortai.com).

-   *Paid subscriber Discord access in email header+footer.*

-   Referrals → paid sub: Use the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   Student discounts in [About page](https://www.interconnects.ai/about).

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
This is taken from some of my recent answers and [tokenizer tools](https://gptforwork.com/tools/tokenizer) that show token count (like word count).
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Most intuitions would make us think that this would happen early in pretraining, where the quality of data is less important as the model learns representations, but the Q\* rumors and Anthropic CAI rumors make it uncertain where teams can get positive signals out of synthetic training data. It's a broad tool, so different flavors of it will likely be used in the entire training process.
:::
::::
