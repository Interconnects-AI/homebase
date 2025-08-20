---
title: "A realistic path to robotic foundation models"
subtitle: "Some thoughts and excitement after revisiting the industry thanks to Physical Intelligence founders Sergey Levine and Chelsea Finn. Not “agents” and not “AGI.” "
date: 2024-06-05
type: newsletter
audience: everyone
visibility: public
post_id: 145280822.robotic-foundation-models
email_sent_at: 2024-06-05T12:03:01.120Z
---
*This post is available as an AI generated audio essay fine-tuned on my voice on [podcast players](https://podcast.interconnects.ai/episodes/a-realistic-path-to-robotic-foundation-models) and [YouTube](https://youtu.be/N46i2c8Kfq8).*

<div>

------------------------------------------------------------------------

</div>

Progress in the field of robotics is nearly completely under the media shroud cast by the seeming exponential progress in language models (LMs). The only things that break through are potentially staged [humanoid robot hardware advancements](https://x.com/Tesla_Optimus/status/1734756150137225501) and [making humanoid robots a ChatGPT wrapper](https://www.reddit.com/r/singularity/comments/1bdsh2x/with_openai_figure_01_can_now_have_full/). While recent progress in robotics is coupled with progress in multimodal LMs, scaling of robotic learning could be leading the AI narrative with image generation if not for ChatGPT (depending on how bored of Midjourney people are, which is still well bigger). Multiple barriers have been crossed in robotic learning research by continuing trends that started with [sensor motor learning work as early as 2016](https://arxiv.org/abs/1504.00702). Robotics is still facing the same physical constraints of getting more devices into more varied tasks and distributions, but the end goals for what robotic learning can solve are grander than they ever have been.

I've been excited about robotics companies making this transition to generality for a long time. Years ago, I somewhat chunkily coined the future of robotics *[Horizontal Modularity](https://www.interconnects.ai/p/robotics-take-two)* before the reality of "one large model solves every task" ate the world of AI. I summarized the shift from vertical to horizontal robotics companies:

> The most popular robotics startups these days are the likes of Boston Dynamics, Tesla Motors, and maybe even SpaceX. All of these companies are vertically integrating a product with best-in-class autonomy to create extremely valuable products **years before their competition**. Eventually, the competition will catch up, and my interest is in the new companies that get 90 or 99% of the same ability on one task but solve a variety of similar ones all at once. The ability to solve other problems simultaneously appears from viewing problem statements that are heuristically the same (avoid crashing, locate an object) on platforms that are physically different.

In this article, I painted Covariant, a popular robotic learning startup spun out of Berkeley as the company leading this new revolution. It turns out they, and their peer robotic learning companies in the Bay Area of [Ambi](https://www.ambirobotics.com/) and [Dexterity](https://www.dexterity.ai/), were all too early to capitalize on this vision, even if they had it.

Today, we're seeing a race of new companies that want to build the foundation model labs of robotics. I visited [Physical Intelligence](https://physicalintelligence.company/), which feels more like a lab than a startup. The goal is to build general robotics models that work on many robots, for many tasks, with a general interface. They want to be the colloquial OpenAI for robotics. The system that more robotics companies build on top of, via an API, to build magical things.

This new wave of companies, of which there are surely more I'm not familiar with, are being built at exactly the right time when investors are willing to spend hundreds of millions of dollars to get new AI ventures off the ground. This level of investment will be the only way for the next generation of robotics companies, which can only succeed by getting hundreds and thousands of robots out into the world. Meanwhile, likely sensing all this, [OpenAI is rebuilding its robotics team](https://www.forbes.com/sites/kenrickcai/2024/05/30/openai-robotics-team/?sh=35030a284f33) after [disbanding it in 2021](https://venturebeat.com/business/openai-disbands-its-robotics-research-team/).

### Key factors for the future of robotics

Robotic learning does not have the benefits that we do when training large visual or language models --- everything for an LLM can be done remotely. Scraping, training, clusters, evaluation, etc. all do not need any interface with the real world. When it comes to robotics, we don't have data to scrape and we need to evaluate our systems in the real world. While there are exciting inflection points coming that could make this 10 or 100 times easier to do, it'll never be free.

There are three or four core trends I see building on each other in the coming years of robotic learning. Two present a similar upside that we have seen with language models, one of them will become a standard for every new autonomous system, and one of them presents a large uncertainty of success:

1.  **Multi-robot policies work**. This trend got serious with the release of [RT-X and Open X-Embodiment](https://robotics-transformer-x.github.io/) which showed that not only do cross-robot policies work, but they do so in the open ecosystem of robotics researchers. By making every action a token, these models can easily handle robots with different action spaces and adapt zero-shot to a new environment. To make a true robotic foundation model company succeed you need to either a) get your robots into the world or b) fund enough people to do robotics work in exchange for their data. The latter seems doable in a traditional VC model.

2.  **Robotic instruction prompting in plain text**: We've established that the outputs are just tokens, but changing the inputs to this view is even more impressive. Robots will most often be prompted in language that is adaptable to controllers. If you have a general idea of what you want the robot to do, you'll tell it. If it fails in a certain way, you can put it in the prompt too. This requires all the models to understand text and likely see the world, but it seems very natural to fuse robotic policies to LLMs much like [people have fused vision components to them in the past](https://arxiv.org/abs/2204.14198). In the context of what we have seen with GPT-4o, it feels crazier to not be able to prompt robots in the same way. Text in, action out, is not very different from text in, audio out.

3.  **Teleoperation markets**: For serious autonomous vehicle companies, [human labor has been a central part of the stack for years](https://www.understandingai.org/i/144853177/waymo-relies-on-remote-operators) --- they help guide the robots through tricky situations. For driving, this is handled in a first-party, high-trust way. In other domains, this remote teleoperation can have different market dynamics. If a home robot doesn't know how to solve a task or gets stuck when no one is home, I'm sure someone on the other side of the world would happily take a micro-transaction fee to solve it for you. Ethical employment practices aside, this could be the norm that lets robots learn iteratively in personal domains.

4.  **Manufacturing low-cost robots:** For this all to succeed, the cost of robots needs to be drastically lower. If we need a trillion tokens of data to train these models, we'll need about 40000 high-quality robot years of data (assuming it is all collected at 50Hz and one token per sample, which is imprecise). This is a ballpark that makes sense on the data side, but not yet on the hardware side. I think Physically Intelligent had about 20 robots.

The silver lining is that robotics hasn't been subject to the process manufacturing revolution of other physical fields. Lithium-ion batteries started decades ago and are continuing to break barriers no one thought was possible, solar prices are now getting decimated to the point where it is arguably a better path to a green power future than nuclear. Bringing this to robotics is crucial. Some of this has happened in China, e.g. [Unitree](https://m.unitree.com/), but there's a 25% import tariff on robots and those are still the most common ones American researchers buy. Robotics is a far broader category than batteries or solar panels, but if the economic upside is available the efficiency will kick in.

### Everything is a token: The transformerification of robotics

I've largely accepted that [Moravec's paradox --- the idea that physical motion is fundamentally harder to solve than digital tasks](https://www.interconnects.ai/p/robotics-vs-moravecs) --- will not be the limiting factor of this field. We've seen the mentality of converting everything to tokens, scaling data, and building the compute work in so many domains. It's how everything became the Transformer. It looks good for robotics that both multi-robot and multi-task generalization can be handled by having the right tokens. For robotics, the limitation is data and getting robotic boots on the ground.

The extent to which these new robotic foundation model labs succeed is governed largely by the efficiency of modern process engineering driving the cost of robotics down. If, and yes, only *if*, this cost comes down, then comes the second challenge: getting robots into the world to collect data. It takes a leap of imagination to see robotic policies generalizing from a lab in San Francisco to then be able to empty your dishwasher at home. If people were to have these robots in their homes, I actually see an easier path to getting the task done. I don't see much of a path to people having humanoid robots in their homes in the next 5 years for sure, and a decade maybe. If the product is all academic and manufacturing applications in the 5-year timeline, it seems almost inevitable that the current batch of companies will look similar to the Ambi, Covariant, and Dexteritys I mentioned earlier, but I would love to be proven wrong.

Combining these new robotics foundation models with the text-to-video models we've seen demoed in the last year will represent something that feels like it has to understand some aspect of the physical reality.

*For the curious, here are two resources on scaling robotic learning that you can dig into if you're curious. First are some [notes from CoRL 2023 on the topic](https://nishanthjkumar.com/Will-Scaling-Solve-Robotics-Perspectives-from-CoRL-2023/) and the second is a small review on [embodied scaling laws for AI](https://arxiv.org/abs/2405.14005).*

<div>

------------------------------------------------------------------------

</div>

**Housekeeping**

-   Audio of this post is available (soon) in [podcast](https://podcast.interconnects.ai/) form or on [YouTube](https://www.youtube.com/@interconnects).

-   My real podcast is at [retortai.com](http://retortai.com).

-   *Paid subscriber Discord access in email footer.*

-   Referrals → paid sub: Use the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   Student discounts in [About page](https://www.interconnects.ai/about).
