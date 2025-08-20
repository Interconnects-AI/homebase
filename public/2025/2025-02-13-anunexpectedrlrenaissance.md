---
title: "An unexpected RL Renaissance"
subtitle: "New talk! Forecasting the Alpaca moment for reasoning models and why the new style of RL training is a far bigger deal than the emergence of RLHF."
date: 2025-02-13
type: podcast
audience: everyone
visibility: public
post_id: 156830514.an-unexpected-rl-renaissance
email_sent_at: 2025-02-13T15:34:52.423Z
---
The era we are living through in language modeling research is one characterized by complete faith that reasoning and new reinforcement learning (RL) training methods will work. This is well-founded. A [day](https://x.com/jonasgeiping/status/1888985929727037514?t=CuNvoj_kH3NkFEziZFBT2w&s=33) \| [cannot](https://x.com/rdolmedo_/status/1887882323674194094) \| [go](https://arxiv.org/abs/2502.01456) \| [by](https://arxiv.org/abs/2501.19393) \| [without](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1) \| [a new](https://allenai.org/blog/tulu-3-405B) \| [reasoning model](https://huggingface.co/cognitivecomputations/Dolphin3.0-R1-Mistral-24B), [RL training result](https://x.com/junxian_he/status/1883183099787571519?s=46), or [dataset](https://x.com/JiaLi52524397/status/1888949470798426186) distilled from [DeepSeek R1](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

The difference, compared to the last time RL was at the forefront of the AI world with the fact that reinforcement learning from human feedback (RLHF) was needed to create ChatGPT, is that we have *way* better infrastructure than our first time through this. People are already successfully using [TRL](https://github.com/huggingface/trl), [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF), [veRL](https://github.com/volcengine/verl), and of course, [Open Instruct](https://github.com/allenai/open-instruct) (our tools for [Tülu 3](https://www.interconnects.ai/p/tulu-3)/OLMo) to train models like this.

When models such as Alpaca, Vicuña, Dolly, etc. were coming out they were all built on basic instruction tuning. Even though RLHF was the motivation of these experiments, tooling, and lack of datasets made complete and substantive replications rare. On top of that, every organization was trying to recalibrate its AI strategy for the second time in 6 months. The reaction and excitement of Stable Diffusion was all but overwritten by ChatGPT.

This time is different. With reasoning models, everyone already has raised money for their AI companies, open-source tooling for RLHF exists and is stable, and everyone is already feeling the AGI.

*Aside: For a history of what happened in the Alpaca era of open instruct models, watch my [recap lecture here](https://www.youtube.com/watch?v=AdLgPmcrXwQ) --- it's one of my favorite talks in the last few years.*

The goal of this talk is to try and make sense of the story that is unfolding today:

-   Given it is becoming obvious that RL with verifiable rewards works on old models --- why did the AI community sleep on the potential of these reasoning models?

-   How to contextualize the development of RLHF techniques with the new types of RL training?

-   What is the future of post-training? How far can we scale RL?

-   How does today's RL compare to historical successes of Deep RL?

And other topics. This is a longer-form recording of a talk I gave this week at a local Seattle research meetup (slides are [here](https://docs.google.com/presentation/d/1z-i4NuqSc7rFKmI9zNnz3CJ_eshUBpJpbvcswCeWvPk/edit#slide=id.p)). I'll get back to covering the technical details soon!

Some of the key points I arrived on:

-   RLHF was necessary, but not sufficient for ChatGPT. RL training like for reasoning could become the primary driving force of future LM developments. There's a path for "post-training" to just be called "training" in the future.

-   While this will feel like the Alpaca moment from 2 years ago, it will produce much deeper results and impact.

-   Self-play, inference-time compute, and other popular terms related to this movement are more "side quests" than core to the RL developments. They're both either inspirations or side-effects of good RL.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

-   There is just so much low-hanging fruit for improving models with RL. It's wonderfully exciting.

For the rest, you'll have to watch the talk. Soon, I'll cover more of the low level technical developments we are seeing in this space.

00:00 The ingredients of an RL paradigm shift\
16:04 RL with verifiable rewards\
27:38 What DeepSeek R1 taught us\
29:30 RL as the focus of language modeling

:::::::: {#youtube2-YXTYbr3hiFU .youtube-wrap attrs="{\"videoId\":\"YXTYbr3hiFU\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=YXTYbr3hiFU){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Inference time compute is also orthogonal. With any model, spending more on inference makes it more likely that you will arrive at the correct answer. This is foundational to modern AI stacks, but not necessarily the same thing as pursuing the new RL ideas.
:::
::::
