---
title: "gpt-oss: OpenAI validates the open ecosystem (finally)"
subtitle: "OpenAI's first open language model release since GPT 2 and what it means for the ecosystem."
date: 2025-08-05
type: newsletter
audience: everyone
visibility: public
post_id: 170127813.gpt-oss-openai-validates-the-open
email_sent_at: 2025-08-05T17:24:09.752Z
---
OpenAI released two open-weight, text-only reasoning models today, both mixture of experts (MoE) sized to run efficiently on a range of hardware from consumer GPUs to the cloud. These models have the Apache 2.0 license, so they're available for distillation into other reasoning models, deployment into commercial products, and are free of downstream restrictions. These two models, the smaller gpt-oss-20B with 3.6B active parameters and 21B total and the larger gpt-oss-120B with 5.1B active parameters, follow the trends we've seen with the other leading open models in architecture choices.

Where this release shines is in the dramatic change in open model performance and strategy that comes with the leading name in AI releasing an open model that undercuts some of their own API products.

We'll get to the technical details on the model later, but the main point of this post is how much OpenAI has changed by releasing their first open language model since GPT-2. The larger 120B model "achieves near-parity with OpenAI o4 mini on core reasoning benchmarks‬" and is a major moment for the ecosystem:[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

-   OpenAI has released an open model at the frontier of current open model performance --- highlighting how **major concerns over open models that OpenAI leadership mentioned in 2023 were overblown**. The marginal risks of open models have been shown to not be as extreme as many people thought (at least for text only --- multimodal is far riskier). Once other organizations, particularly Meta and China showed OpenAI that there was no risk here, the path was opened to release a model.

-   **OpenAI has revealed far more of their technical stack than any release to date.** This blog post has light details on many things in the model, but community tinkering will begin to better understand what is going on here. This includes basic things like our first time seeing a raw chain of thought (CoT) for an OpenAI reasoning model, but also more interesting things like how this model is trained to use tools in the CoT like their o3 model. Other details include researchers being able to play with OpenAI's [instruction hierarchy](https://arxiv.org/abs/2404.13208) in raw weights (where pieces of it are untouchable in the API), a new "harmony" prompt format, the same "reasoning efforts" of low, medium & high from the API, a huge proof of concept on how far basic, community standard architectures with MoEs can be pushed, and other small details for the AI community to unpack.

-   **OpenAI has initiated a scorched earth policy on the API market**, undercutting their own offerings and unleashing an extremely strong, trusted model brand with a permissive license. While adoption of any open model is much slower than an API due to testing, additional configuration, etc., this is set up to go about as fast as it can. Any API model that competes with current models like OpenAI o4 mini, Claude Haiku, Gemini Flash, DeepSeek R1 etc. are all going to have to compete with this model.\
    \
    OpenAI's o4 mini model is currently served at \$1.1 per million input tokens and \$4.4 per million output. Serving this open model will likely cost at least 10x less. There are many potential strategic reasons for this, all of which paint OpenAI as having a clearer vision of what makes it valuable.\
    \
    What OpenAI hasn't touched with this model is interesting too --- "For those seeking multimodal support, built-in tools, and‬ seamless integration with our platform, models available through our API platform remain the‬ best option." These are dropped for reasons above, and "headaches" discussed later in the post.

Together, these paint a much clearer vision by OpenAI on how they'll control the AI ecosystem. The top potential reasons on my mind are:

1.  OpenAI could be trying to make all API models potentially obsolete on cost ahead of the GPT-5 release, which they hope to capture the top end of the market on. Or,

2.  OpenAI could be realizing that models are no longer their differentiation, as ChatGPT users continue to steadily climb --- and they'll soon pass 1 billion weekly actives.

There are plenty of other reasons, such as the politics alluded to at the end of the blog post, but OpenAI tends to only act when it serves them directly --- they've always been a focused company on their goals.

There's also a long list of head scratchers or in-between the lines points that illuminate OpenAI's strategy a bit more. OpenAI of course didn't release training data, code, or a technical report, as expected. OpenAI is trying to make a big splash with the name that captures more of the enterprise market, but in doing so takes some collateral damage in the research and true "open source" AI communities. These future questions include:

-   **The naming is bad** --- a mixture of cringe, confusion-inducing, and still useful for their marketing goals. For anyone following [open-source AI](https://www.interconnects.ai/t/open-source) for a long time it won't be new that a major company is blurring the association of the term open-source with the community accepted [definitions](https://www.interconnects.ai/p/defining-open-source-ai). I understand why OpenAI did this, but the naming conflict further enforces that the true open source AI community isn't the target of this release --- it's people that want to try an "open source AI model" for their business, and OpenAI has made the target too big to miss for enterprises.

-   **OpenAI did not release the base models**. Anyone following the space would've expected this, but it matters substantially for researchers. These two sparse, low numerical precision MoE models won't be easy for researchers to use. The best model for researchers and tinkerers are dense, base models from 1 to 7 billion parameters. These are much "longer term" artifacts in the open community that will still be using almost only Qwen.

I need to take a second before the "unknowns" section and comment on the architecture. These models are reinforcing trends we're seeing in modeling across the industry. Recent frontier open models are *all* very sparse MoEs inspired by the [DeepSeek architecture](https://arxiv.org/abs/2412.19437v1). DeepSeek V3 had 37B active and 671B total parameters. [Kimi K2](https://www.interconnects.ai/p/kimi-k2-and-when-deepseek-moments) had 32B active and 1T total parameters. With 5B active and 121B total, the sparsity factor fits right in with normal. Sparsity in MoEs is totally king right now. The smaller gpt-oss is a bit less sparse than [Qwen's](https://www.interconnects.ai/p/qwen-3-the-new-open-standard) 3B active, 30B total smaller MoE, but expect the sparsity of these models to continue to increase.

Some things we need more testing to know the impact of include:

-   **The model has been quantized for release** to MXFP4 (4 bit floating point). It's not clear exactly who will be impacted here, but this could make it benefit people most with the newest hardware, cause minor issues across Torch/Cuda versions, or even make some of the behaviors weird relative to the trained version internal to OpenAI.\
    \
    This could also be a plus, depending on performance, as the bigger model is quantized to 4 bit precision to enable it to be run on GPUs with 80GB of memory, such as the A/H100 line from NVIDIA.

-   **Safety measures have been taken to change how finetunable the model is**. With, or soon after, this release OpenAI is releasing a research paper on new methods to make it so you can't "[finetune the safety away](https://www.interconnects.ai/p/undoing-rlhf)" from a released instruct model. This is a very long-standing issue that people have concerns with over releasing open models. The main question here is if the models OpenAI releases are still able to be finetuned or not for productive use-cases. OpenAI claims they can be in their blog post, but this will be left up to the community to decide. Is finetuning the safety away actually a feature of an easy to use model?\
    \
    For example, Gemma has been tougher for people to finetune historically because it uses a different attention implementation and has a different parameter space from being [distilled](https://www.interconnects.ai/i/145870222/are-gemini-flash-and-claude-haiku-distilled). Open finetuning stacks are still tuned for Llama and Qwen --- this takes a long time to change.\
    \
    Many people will take the "we made it impossible to un-censor this model" as a challenge, which will be interesting to follow in the jailbreaking research community. There is a substantial market for modifiable models.

-   **The model was trained to expect tools, but open model tool use is a mess**. One of the biggest problems I worry about in designing an OLMo model with native o3-style tool use is that I need to make it seamless for users to use the same tools from training time at inference time. An early tester in my network mentioned that the model would hallucinate tool calls from training (sort of like what was mentioned around [o3's full release](https://www.interconnects.ai/p/openais-o3-over-optimization-is-back)). I don't expect this to be an unsolvable issue, but it could slow adoption. It could also allow people to reverse engineer the tools that OpenAI uses during training, we'll see!

-   **We need to re-benchmark the model on open infrastructure**. OpenAI did a good job for this release integrating it everywhere, but we need to confirm that the community can *easily* replicate their evaluation scores. [Evaluation at closed labs](https://www.interconnects.ai/p/building-on-evaluation-quicksand) has increasingly become bespoke to suit their internal needs, which is a logical decision, but this comes at a cost of friction when an open model is released.\
    \
    This is me saying loud and clear that this isn't a model performance review in a nuanced sense, but a summary of the importance of OpenAI's approach (and where the opportunity is for the rest of us). Not all good models are easy to use. Some models benchmark well and are useful --- e.g. Qwen. Some models benchmark well and are forgotten. Regardless of scores, I expect this to be a useful model.

Overall, I would give OpenAI a very strong grade on their first open release in a while --- they definitely listened to the [feedback](https://natolambert.substack.com/p/some-thoughts-on-openai-returning) given by the community. The path to earning goodwill with the open community, especially with researchers, is to embrace more risk in making models that are easier to modify (and potentially even more revealing), such as the base models for these checkpoints.

Open models from the U.S. labs were in such a dire spot that we need any step back in the right direction. As the rollout of the model begins and we have more understanding of it, we'll include more updates on Interconnects, such as in the next [Artifacts Log](https://www.interconnects.ai/t/artifacts-log) issue.

So, OpenAI is the new open champion, right? There's no more risk vis-a-vis China? We don't need Llama anymore? Not quite, let me explain.

## OpenAI, ATOM, and national champions

It's a phenomenal step for the open ecosystem, especially for the West and its allies, that the most known brand in the AI space has returned to openly releasing models. This is momentum and could be the start of the turning point of adoption and impact of open models relative to China.

The open ecosystem moves fast in some ways and slow in others. Many workflows and expertise is now built on Qwen models due to their frequent, accessible releases. Some of these will try OpenAI the next time they want to make a change, but it's far from the fact that everyone will immediately switch to OpenAI's model now that it's out.

To me, OpenAI dropping a strong model has switched the second derivative on the open model scales. The U.S. and its allies will no longer be falling further and further behind, which was the main story of 2025, but we need to build on this momentum if we want to have competitive open models for all use cases in the order of months rather than years.

There's a lot of uncertainty in the incentives for open models. Some of the best China analysts I know share how China is sensing that releasing open models is a successful strategy for them and are doubling down. This is a very reasonable take. The retort is that if we use it as a weakness of the American ecosystem that it is so reliant on Meta's Llamas, or now GPT OSS, the same could happen for Qwen. So then, what happens if Alibaba decides Qwen's stellar releases no longer serve them?

In this case, there would be a large opportunity in the series of small models from 1 to 70B parameters, but there's so much competition from China at the larger scales. These are currently the big mixture of experts (MoE) models like DeepSeek V3/R1, [Z.ai's / Zhipu's GLM 4.5](https://huggingface.co/zai-org/GLM-4.5), [Kimi K2](https://www.interconnects.ai/p/kimi-k2-and-when-deepseek-moments), and so on. China has more models that are close to this performance level, such as [MiniMax](https://huggingface.co/collections/MiniMaxAI/minimax-m1-68502ad9634ec0eeac8cf094) or [Tencent](https://huggingface.co/tencent/Tencent-Hunyuan-Large).

All of these companies have uncertainty, but there's a strength in numbers that reinforces standard practice and sets standards. Releasing strong, large, open models is now the standard in China. We're back in the precarious period of establishing standards for American companies, who are exposed to the legal risk of not being able to un-release models with many open lawsuits, such as in areas like copyright.

These two sides of the open ecosystem are at very different stages and need very different actions. In many ways, we shared [The ATOM Project](https://www.atomproject.ai/) when we did because we could tell this was a local (and hopefully global) minimum in terms of the distance between Western contributions to the open science of AI compared to any point in the recent past and near future.

OpenAI's release is a step in the right direction, but it is still a precarious position. Many people make noise about creating open models, from the [AI Action Plan](https://www.interconnects.ai/p/the-white-houses-plan-for-open-models) to [venture capitalists](https://x.com/martin_casado/status/1952442509600366708) and [academics](https://www.deeplearning.ai/the-batch/issue-312/). What all of these parties have in common is that its not their number one goal. The goal of The ATOM Project is to give an outlet for people like myself that want to make this project their number one priority.

This is why we need to keep nurturing entrants into the open model space that are releasing their best models there. It is what made the early versions of Llama great, and is what will be the defining factor of the outputs of ATOM. Models that are designed from first principles to be modifiable, interpretable, and extendable is what will enable a new decade of AI research to be born. This needs base models, training details, convenient sizes, and other little details that are missing from many recent open model releases, including OpenAI's.

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
OpenAI has made other exceptional model releases including [Whisper](https://openai.com/index/whisper/) for speech recognition or [CLIP](https://openai.com/index/clip/) for image-to-text embeddings.
:::
::::
