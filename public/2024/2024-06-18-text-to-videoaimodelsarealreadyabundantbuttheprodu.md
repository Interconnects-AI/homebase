---
title: "Text-to-video AI models are already abundant, but the products?"
subtitle: "Signs point to a general use Sora-like model coming very soon, maybe even with open weights."
date: 2024-06-18
type: newsletter
audience: everyone
visibility: public
post_id: 145737056.text-to-video-ai-is-already-abundant
email_sent_at: 2024-06-18T12:02:48.259Z
---
*I'm bringing you this a day early as I'm off on Wednesday this week. Audio of this post is [available on podcast players](https://podcast.interconnects.ai/episodes/text-to-video-ai-is-already-abundant), and I'm pausing the [AI generated YouTube](https://www.youtube.com/@interconnects) videos for a bit (too much marginal stuff going on).*

Now that AI is mainstream, companies are too strongly incentivized to show us what they have built before we get to use it. For the previous transformative AI modalities, in the form of Stable Diffusion for images and ChatGPT for text, net capabilities came onto the scene with a blog post and general access. Video generation models are poised to be the next major transformation in how people use, and in this case, consume AI-generated content. With the rise of TikTok and its downstream transformation (a.k.a. shortification) or our media internet, video is now the default medium. AI is ready to accelerate this arena.

OpenAI's text-to-video model Sora [was announced on February 16th](https://www.interconnects.ai/p/sora-gemini-and-mistral-next) (the same data as Gemini's million-token context length), and it spawned [substantial discussions on everything from whether OpenAI should release the model to whether video can be used as a world model](https://www.interconnects.ai/p/sora-gemini-follow-up). It seemed like these models were a thing of the future that we wouldn't get any time soon --- mostly due to cost and locked down technical complexity.

::: {.native-video-embed attrs="{\"mediaUploadId\":\"fefb71f6-a034-492d-bd05-605345545178\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

The assumption in February seemed to be that OpenAI wouldn't be willing to take the risk to make this model publicly available before the 2024 American election due to destabilization concerns, whether or not you think that is good. Today, looking at the text-to-video space makes it seem like a publicly available model at Sora caliber is around the corner, and may even be released via open weights (more on this later).

Text-to-video now is the most concentrated area of foundation model competition. The capabilities are all remarkably similar. What changed?

This week, Runway ML announced their [Gen-3 model](https://runwayml.com/blog/introducing-gen-3-alpha/), which they also brand as a [general world model](https://research.runwayml.com/introducing-general-world-models), similar to OpenAI. I don't think these models capture any reality of dynamics given my background in linear systems and particularly some chaos theory. For short timescales and dynamics that are low-priority, these do fine. They're not creating a world that is measurable, though. They're great at creating background scenes and randomization to use within many other AI stacks. Here's Gen-3:

::: {.native-video-embed attrs="{\"mediaUploadId\":\"1224b180-00ed-4c3c-b6ee-ffdd3dcfe459\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

Just before Runway's announcement, a Chinese company [Kling AI](https://x.com/kling_ai) opened up a [Sora competitor](https://x.com/minchoi/status/1798840754015748109) to influencers and public figures with a Chinese phone number. Here's Kling:

::: {.native-video-embed attrs="{\"mediaUploadId\":\"8d8e312e-1c2e-4825-92fe-72403c26ceb1\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

Back at Google IO this year, they announced [Veo](https://deepmind.google/technologies/veo/), which seemed extremely similar to Sora. Here's Veo:

::: {.native-video-embed attrs="{\"mediaUploadId\":\"e9f74a70-c91d-4147-a351-9bd04c9ff76f\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

Just last week, [Luma Labs announced and released their model](https://x.com/LumaLabsAI/status/1800921380034379951), which you can [sign up for on their website](https://lumalabs.ai/). Their model seems a half tier below some of the likes of Sora and Veo in quality, but the general availability matters more. Now that people understand generative video is coming, they want to get their hands on it and learn what it can do. Sora cannot fulfill those needs. Here's Dream Machine:

::: {.native-video-embed attrs="{\"mediaUploadId\":\"838a71ba-8706-4e5c-8aaf-a687770afcf6\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

A similar player to Luma is Pika. [Pika was a bit earlier to make their model public](https://venturebeat.com/ai/pika-labs-text-to-video-ai-platform-opens-to-all-heres-how-to-use-it/), doing so last December, but the quality then was clearly a level behind Sora, so it didn't make the breakthrough splash (like many research papers on the topic before Sora). Here's Pika 1.0:

::: {.native-video-embed attrs="{\"mediaUploadId\":\"7b6dfadf-e41b-41b6-ba52-f178b477e8f5\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

The text-to-video space is expansive if you start including the long tail of companies doing similar things. Eventually, I expect the companies who win here to have a specialty but need to have offerings in many other modalities in order to please their users. The most important thing these companies can do is acquire users. If adding audio or editing your video is with a competitor, that will be a lost customer.

Some similar offerings include [Apparate's video avatars](https://apparate.ai/), [Wayve's reconstructive imaging for self-driving](https://wayve.ai/thinking/prism-1/), [ElevenLab's](https://www.notion.so/Text-to-video-AI-is-already-abundant-fe2137181bc64775902eda14b42a2186?pvs=21) or [Google's text-to-sound-effects](https://x.com/rowancheung/status/1802734770117333257), image-to-video tools, video-to-video tools, [Viggle's character rendering](https://viggle.ai/) that is built on Discord like Midjourney, my [friend's startup Cartwheel for animations](https://getcartwheel.com/home), [Common Sense Machines](https://www.csm.ai/) for rendering worlds, and likely many other integrations with text.

We know there are more big players that will join the space. Midjourney's CEO has said it will "begin training its video models starting in January," and this seems closely aligned with Meta's core business so we can expect them to have an offering shortly.

A sort of mental block was unlocked by the collective AI community by watching the Sora videos. Many people expected something like this to work but didn't know if the capability was within existing compute and data availabilities. Given the number of players that have emerged at Sora's level since its announcement, it's clear that the cost and compute are dramatically lower than that of the leading language models. The opportunity is currently viewed as being smaller, which I think is fair because all visual models will still be controlled by text models through things like prompt re-writing.

Many startups will be eager to ship something and dethrone the incumbents. I expect in the coming weeks to months we'll have another Sora-like moment that transitions text-to-video AI from a magical announcement to something people can use. I'm excited to see competition on price, inference speed, clever ways to preview generations before committing to an entire rendering, model quality, etc. --- it feels like many more ways than LLMs can be different!

On the technical side, it seems like most of these companies are relying on similar core stacks. When Sora worked, [OpenAI released some core details on its training](https://openai.com/index/video-generation-models-as-world-simulators/) (here's [another explainer on Lil'Log](https://lilianweng.github.io/posts/2024-04-12-diffusion-video/)). I suspect all of the competitors here are running very similar stacks, from the big-picture "diffusion transformer" headlines to the low-level data transformation and processing ideas. I don't think there were any high-profile leaks of what the Sora team did, but rather more natural information flow through Silicon Valley. People like to talk around here, and until there's substantial money on the line, executives are not going to be as protective of trade secrets.

### What's next for the text-to-video market?

The near future for text-to-video AI will follow a similar path to what we have seen with language models --- product and performance. For video models, I expect the product to be weighted higher. Rumors are that a model like Sora can take up to 5 or 10 minutes to generate a response. To go from a 5-minute generation lag to 3 seconds would be a 100 times reduction in inference speed. Improvements like this only come with sustained usage.

For a startup trying to monetize these models and retain users, inference *time* is a fundamental challenge. The development cycle will likely hinge on who can figure out how to deploy more cheaply or build new workflows around these inference costs. Scaling up a model that already takes 10 minutes to infer has little gain. Would you wait twice as long for a Sora that is 10% better?

Given the breadth of companies engaging here, an upstart company will likely release a minimal open weights text-to-video model. The entire suite of companies are preparing their v2 models which are much stronger than the current generation, so [releasing the first generation has little downside risk and can bring in substantial customer interest](https://www.interconnects.ai/p/open-llm-company-playbook). If you look up the fundraising rounds of companies releasing these models to general use, it's often in the 10 to 100 million dollars. The model likely costs a fraction of that to train (but maybe close to crazy inference costs), so new players coming in is still very likely.

I do not expect the dataset to follow suit in becoming open. The creator-trainer relationship in visual domains is understandably more tense, so data disclosure will be even more limited.

The market looks even riper than the language counterparts for consolidation, given the valuations of the leading startups are at least a bit lower and the use-cases less proven.

If scaling works the same way it has for language models, such as driving inference costs down, this will really feel like another exponential explosion of progress in the next 18 months. If the costs of inference remain too high, this will still look like a niche AI tool that is fun but average people don't use.

<div>

------------------------------------------------------------------------

</div>

### Are text-to-video models good for the world?

Text-to-video is an extremely evocative domain for AI. The models are trained on the same internet as the language-based models in a way but with a different scraping technique. From what the model sees, the distribution of content is quite similar. The generations from the video model will have substantially higher variance in their poignance than the textual. Has an output from a written language model ever left you momentarily stunned? I still get this much more with images and expect it another 10 times more with videos. This moment is a release of built-up inertia for how the world works being interrupted.

Text is restrictive. There are ideas that cannot be expressed just with text. Text-to-video models will be effectively drawing on this substrate even though all they are doing is interpolation. When a human creates visual beauty, I believe we are drawing on deep lived experience that is extremely far from language. What does it mean for an AI to evoke something similar without having remotely similar information?

I will have many domains where AI-generated video makes me recoil, but others I will love. Will these views overlap enough that deploying general endpoints for video models makes sense? Can we personalize it with prompts to the same extent that we can images?

I have many optimistic and pessimistic views of what video AI will do.

What are you excited about for AI video? Are you more excited than nervous? How would different audiences than my extremely technical AI-forward audience feel about this? There is a lot of sociology, ethics, and technicalities to dig into in the coming years.

<div>

------------------------------------------------------------------------

</div>

*We discussed [some of our reactions to Sora on an older episode of The Retort](https://retortai.com/episodes/model-release-therapy-session-1), but I expect us to revisit this soon and answer some of the above questions.*

**Housekeeping**

-   My real podcast is at [retortai.com](http://retortai.com).

-   *Paid subscriber Discord access in email footer.*

-   Referrals → paid sub: Use the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   Student discounts in [About page](https://www.interconnects.ai/about).
