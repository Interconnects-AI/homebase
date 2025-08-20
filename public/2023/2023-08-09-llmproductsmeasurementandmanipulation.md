---
title: "LLM products: measurement and manipulation"
subtitle: "Two stories will begin to unfold as the AI capabilities-to-product overhang is reduced."
date: 2023-08-09
type: newsletter
audience: everyone
visibility: public
post_id: 135853039.llm-products-measurement-manipulation
email_sent_at: 2023-08-09T14:00:45.424Z
---
##### Programming note: I\'m most likely not posting the next two weeks, vacation calls 🤙.

<div>

------------------------------------------------------------------------

</div>

Large language model (LLM) based products, and all AI products really, are downstream effects of software-based companies and the internet. Modern LLM tools let people build *and experiment with* products that would be too complex to ever build with rules-based software. The ability to approach problems that previously were thought impossible comes with the downside of not being able to guarantee performance, as long as deep learning is the dominant paradigm, which will be at least a while. The opposite side of deep learning and [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) giving us success after success is each application taken over by it \-- **these applications have lots of added uncertainty and decreased robustness**. The research trying to address this is often called [mechanistic interpretability](https://transformer-circuits.pub/2022/mech-interp-essay/index.html), which, unfortunately, has not shown a ton of progress to date.

AI products are a sort of continuation of software-based technologies with the ability to address even harder problems, so some characteristics of things that are hard in software products will be doubly hard with AI products (it is debate-able if this is due to the tool we\'re using the solve the problem or the complexity of the problem itself, but that is an aside). I\'m going to focus on **two product characteristics** that mirror two of my research topics in ML these days (evaluation and reinforcement learning): **measurement of performance and manipulation of users**. Both of these stem from us not knowing exactly how large machine learning systems work for each individual interaction while being absolutely sure that they work very well on average. To be more specific, I\'ll be focusing on measurement as tracking the impact of a change in a model, *how to target improvement to your products,* and manipulation as a downstream impact of unknown training processes, *how internet dynamics we\'ve seen combined with the LLM products we\'re building*. There are plenty of other ways that these two terms will come up, as they\'re core to software and internet-centric technologies.

When it comes to machine learning companies, measurement is innately hard as we try to use machine learning models in new untrodden use cases and manipulation is hard to prioritize for business reasons (on top of having its own measurement challenges, the dynamics it induces are likely not impacting the bottom line until potential negative press comes a company\'s way).

![natolambert\\\_a\\\_cartoon\\\_of\\\_a\\\_gaming\\\_computer\\\_on\\\_a\\\_desk\\\_with\\\_wizar\\\_ded17912-d726-4488-8d88-d494f8cbf114.png](images/135853039.llm-products-measurement-manipulation_13354f6b-53e7-47b8-8946-23b2d31820a4.png)

## Measurement: evals and A/B testing for chatbots

In the large language model (LLM) space, [evaluation is all the rage](https://www.interconnects.ai/p/evaluating-open-llms) these days because of how hard it has become. While we have leaderboards galore, we don\'t have a clear way to understand which models are best in most domains. This is especially true in general-purpose use cases like chat. This is especially important when deploying LLMs in specific applications, where marginal improvements drive meaningful value.

The reason I discussed the [objective underpinning reinforcement learning from human feedback](https://www.interconnects.ai/p/specifying-objectives-in-rlhf) (RLHF) at length last week is that we don\'t know how to measure chatbot performance directly. In other domains, it's a case more of that we don't know where RLHF will work, but we have a slightly better reward function design. There\'s a lot of discussion about implicit feedback, i.e. measurements that imply performance, such as users closing a session, re-rolling an answer, or responding angrily, because direct measurements don\'t exist.

There\'s a case to be made that most popular chatbots will reduce to another attention economy \-- e.g. running advertisements, like they already had begun experimenting with on BingChat. Attention is the most popular measurement in the digital economy to date because of its universality. I\'m hoping that AI enables a new bunch of internet mega-corporations that are more based on services and generating value rather than extracting value from users. Until this is proven, attention is a useful domain for analysis. In the case when performance is based on services provided, these companies will need new methods of measurement.

Much like is done with news feeds and search results, A/B testing of different solutions will be the norm for understanding the impact of changing a model underpinning a product (at least in the short term). In terms of how many interactions one has per session, chat falls nicely in between search (normally one interaction) and feeds (many interactions in one app session), where there will be a few engagements with a model over a narrow set of topics. This distribution is a starting point for researchers trying to understand attribution.

There are two ways to [A/B test](https://en.wikipedia.org/wiki/A/B_testing) with machine learning models, changing the model per response in a conversation or changing the model per chat. This essentially means giving a subset of users the updated version of the model and seeing if "it is better." Both will require measuring similar things from the user, including what prompt was given, how much-added delay beyond normal reading speed was needed, the number of turns in the conversation, the tone of the responses, and more. Companies should be able to start with more direct forms here, like an average number of messages sent by a user in a given conversation. All of these are not clear measurements in terms of performance.

If attention is the metric, more messages would mean a better model. If you've worked with RLHF and LLMs, you know that encouraging verbose-ness is super annoying (and it catches on).

It\'s interesting how similar the problem feels to news feeds or search results, while still remaining entirely different. There was an [entire field of literature studying how to compare the performance of two search-result algorithms even when a user only clicks one link](https://www.cs.cornell.edu/people/tj/publications/chapelle_etal_12a.pdf) (that is now used in all popular search engines). This looks pretty similar to how to measure the impact of each model\'s messages when they\'re filtering through a conversation.

Product-focused organizations likely have better tools for measuring user behavior, as we've seen with [Meta's versus Snap's response to the ATT shakeup of advertising](https://mobiledevmemo.com/meta-q1-earnings-did-ai-overcome-att/). Following the gap between ML-first organizations like OpenAI and Anthropic versus those with a history of delivering user benefits will be fascinating in the chatbot space. It's likely the biggest reason to bet on Meta's Llama moat strategy. I've heard from big model labs that they have evaluation problems --- they don't compare to other big models enough. If this is the case, they can be left behind quickly if one organization actually figures out how to measure and improve based on user engagement.

A further benefit of open-source companies in the LLM space is that they don't need to figure out both measurement and model performance, multiple organizations can build this complex infrastructure together. To be clear, we are far from being there yet. We saw in the Llama 2 paper that they reported beating ChatGPT on performance, but it's generally accepted that their evaluation prompts were not the right distribution. Without open-sourcing these or providing a service to evaluate more models with them, they won't serve Meta as much. If I can ask only a few questions to OpenAI, they'd all be around evaluation and if they've figured out anything to correlate user behavior with training metrics.

## Manipulation: AI feeds vs. AI friends

Folks living in technology hub cities hear time and time again about how those building new attention-grabbing technologies do not let their children use what they build. This is going to reach a new maximum as we position the next wave of technologies into a context that has much more emotional and relationship rich \-- direct messaging applications.

Generally, today, there are two types of social networks \-- content-based apps with algorithmic feeds and messaging apps for group chats. The former is totally dominated by AI technologies, whether or not we all admit that we like the algorithmic feeds, and the second is about to be crushed by that wave.

The general hypothesis reduces to the following fact: how people use technology depends heavily on the context, and people will be emotionally available in a much deeper way in a direct messaging app. News feeds are for passive engagement, messages are intentional. Direct messaging is where friendships are made and maintained. If, right next to your best friend, is a chat window that is always available, tunable to your interests (directly and indirectly), and supportive, tons of people will obviously use this in a manner different than reading a feed. We are going to increase the scale of the sociological experiment we\'re running: transitioning from the era of making friends in person and transitioning them online, to the era of making human friends online, to the final frontier of making artificial friends online.

This context change has a high likelihood of impacting our mental models already, but the way we\'re training and measuring this new technology makes the risks of manipulation higher. The LLMs we are deploying are more likely to be changing consistently as we build new habits with these apps, i.e. when we are more pliable.

If the models were static, the risk would be much smaller. The fact that relationships will be built within the bigger context of popular methods being trained with multiple intertwined and poorly characterized feedback loops is cause for further hesitation. Broadly, reinforcement learning from human feedback (RLHF), which drives the most popular language models, has two feedback loops \-- inner and outer. The inner feedback loop is the optimization to integrate a current batch of data into the model and the second is collecting new data to fix previous bugs or reinforce high-level behaviors in the model.

While both of these feedback loops are pretty new, there has been much less appetite for tracking and understanding the outer feedback loops of RL systems (something [we discussed in a whitepaper](https://arxiv.org/abs/2202.05716)). While I\'m mostly concerned about this feedback loop because I care deeply about how AI interfaces with society, there are also clear modalities where letting that outer feedback loop on user behavior evolve without constraint can be seen as beneficial, like entertainment. This same process of integrating the behavior of the user can let scenarios like entertainment become deeply personal.

As LLM companies get better tools for measurement, it is likely that they start to quantize the effects in this outer manipulation loop. Even with that data, it\'ll be very hard to control the impacts. They can run more experiments, and see how the RL policies are changing the context of the domain they\'re operating in, but so long as RL systems are designed with a specification that the problem is static, the long-time impacts will be hard to change. RL technologies were developed primarily in toy domains where the robots are always the same, but now they\'re going to slightly nudge humans, resulting in a long-term dance where the models and users co-evolve together.

<div>

------------------------------------------------------------------------

</div>

## AI first products

Technologies that would never exist in any form without state-of-the-art AI are going to be the most memorable releases of the next few years. We saw this with both Stable Diffusion for image generation and ChatGPT to text manipulation. As time goes on, the number of untapped modalities of digital information will continue to shrink, so opportunities for this may whither. Additionally, the opportunities people have still will be muddled by the competitive dynamics balancing first-to-market syndrome and magic product goals. If we wait long enough to deploy an ML model, eventually compute will get to the point where inference is near-instant and the application feels totally magic. Though, these companies need to signpost what they\'re doing and capture reputation, so most new domains will be shipped when it is still a little too slow to feel right. ChatGPT woke everyone up to try products, which can only happen once.

Generally, there are two domains where I see this feeling common in the next few years: adding more modalities to proven formulas (e.g. the best video generators and text-to-image-to-audio models) and [text-based agents](https://www.interconnects.ai/p/llm-agents-integration).

We\'re not used to working in domains where information can come and go in tons of different modalities. We\'re also not used to the words we type immediately becoming tangible in the real world. The litmus test for these is that we know they\'re coming, but it is incredibly hard to imagine life with them. My life without needing to book travel, schedule meetings, send generic emails, etc. is profoundly different.

While the blog has been predominantly technical while we try to make sense of why RLHF actually works, I think it is equally important to grapple with these forthcoming issues. There\'s plenty more to dig into here, such as some of my favorites:

-   Folks scrambling to make user interfaces and understand the human factors of ML research. When we\'re just thinking about scaling laws and benchmarks, interacting with the information isn\'t prioritized

-   Companies that\'ll deploy on-device learning and operating system integrations for acceleration. Bring my RLHF on my MacBook Pro.

-   Startups are scaling from their base model training GPU allotment to needing to for inference. Very different needs and costs will bring a second GPU crunch to the Valley.

<div>

------------------------------------------------------------------------

</div>

*Elsewhere:*

-   [An international security and AI workshop I participated in published a whitepaper](https://arxiv.org/abs/2308.00862). We focus on what international bodies can do to build trust around AI when it is not assumed that each entity trusts the other\'s actions in the space to being with.
